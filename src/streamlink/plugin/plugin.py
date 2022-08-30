import ast
import logging
import operator
import re
import time
from collections import OrderedDict, namedtuple
from functools import partial
from http.cookiejar import Cookie
from typing import Any, Callable, ClassVar, Dict, List, Optional, Pattern, Sequence, Type, Union

import requests.cookies

from streamlink.cache import Cache
from streamlink.compat import str
from streamlink.exceptions import FatalPluginError, NoStreamsError, PluginError
from streamlink.options import Argument, Arguments, Options
from streamlink.user_input import UserInputRequester


log = logging.getLogger(__name__)

# FIXME: This is a crude attempt at making a bitrate's
# weight end up similar to the weight of a resolution.
# Someone who knows math, please fix.
BIT_RATE_WEIGHT_RATIO = 2.8

ALT_WEIGHT_MOD = 0.01

QUALITY_WEIGTHS_EXTRA = {
    "other": {
        "live": 1080,
    },
    "tv": {
        "hd": 1080,
        "sd": 576,
    },
    "quality": {
        "ehq": 720,
        "hq": 576,
        "sq": 360,
    },
}

FILTER_OPERATORS = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
}

PARAMS_REGEX = r"(\w+)=({.+?}|\[.+?\]|\(.+?\)|'(?:[^'\\]|\\')*'|\"(?:[^\"\\]|\\\")*\"|\S+)"

HIGH_PRIORITY = 30
NORMAL_PRIORITY = 20
LOW_PRIORITY = 10
NO_PRIORITY = 0

_COOKIE_KEYS = \
    "version", "name", "value", "port", "domain", "path", "secure", "expires", "discard", "comment", "comment_url", "rfc2109"


def stream_weight(stream):
    for group, weights in QUALITY_WEIGTHS_EXTRA.items():
        if stream in weights:
            return weights[stream], group

    match = re.match(r"^(\d+)(k|p)?(\d+)?(\+)?(?:[a_](\d+)k)?(?:_(alt)(\d)?)?$", stream)

    if match:
        weight = 0

        if match.group(6):
            if match.group(7):
                weight -= ALT_WEIGHT_MOD * int(match.group(7))
            else:
                weight -= ALT_WEIGHT_MOD

        name_type = match.group(2)
        if name_type == "k":  # bit rate
            bitrate = int(match.group(1))
            weight += bitrate / BIT_RATE_WEIGHT_RATIO

            return weight, "bitrate"

        elif name_type == "p":  # resolution
            weight += int(match.group(1))

            if match.group(3):  # fps eg. 60p or 50p
                weight += int(match.group(3))

            if match.group(4) == "+":
                weight += 1

            if match.group(5):  # bit rate classifier for resolution
                weight += int(match.group(5)) / BIT_RATE_WEIGHT_RATIO

            return weight, "pixels"

    return 0, "none"


def iterate_streams(streams):
    for name, stream in streams:
        if isinstance(stream, list):
            for sub_stream in stream:
                yield (name, sub_stream)
        else:
            yield (name, stream)


def stream_type_priority(stream_types, stream):
    stream_type = type(stream[1]).shortname()

    try:
        prio = stream_types.index(stream_type)
    except ValueError:
        try:
            prio = stream_types.index("*")
        except ValueError:
            prio = 99

    return prio


def stream_sorting_filter(expr, stream_weight):
    match = re.match(r"(?P<op><=|>=|<|>)?(?P<value>[\w+]+)", expr)

    if not match:
        raise PluginError("Invalid filter expression: {0}".format(expr))

    op, value = match.group("op", "value")
    op = FILTER_OPERATORS.get(op, operator.eq)
    filter_weight, filter_group = stream_weight(value)

    def func(quality):
        weight, group = stream_weight(quality)

        if group == filter_group:
            return not op(weight, filter_weight)

        return True

    return func


def parse_url_params(url):
    split = url.split(" ", 1)
    url = split[0]
    params = split[1] if len(split) > 1 else ''
    return url, parse_params(params)


def parse_params(params=None):
    # type: (Optional[str]) -> Dict[str, Any]
    rval = {}
    if not params:
        return rval

    matches = re.findall(PARAMS_REGEX, params)

    for key, value in matches:
        try:
            value = ast.literal_eval(value)
        except Exception:
            pass

        rval[key] = value

    return rval


Matcher = namedtuple("Matcher", "pattern priority")


class Plugin(object):
    """
    Plugin base class for retrieving streams and metadata from the URL specified.
    """

    matchers = None  # type: ClassVar[Optional[List[Matcher]]]
    """
    The list of plugin matchers (URL pattern + priority).

    Use the :func:`pluginmatcher` decorator to initialize this list.
    """

    arguments = None  # type: ClassVar[Optional[Arguments]]
    """
    The plugin's :class:`Arguments <streamlink.options.Arguments>` collection.

    Use the :func:`pluginargument` decorator to initialize this collection.
    """

    matchers = None  # type: ClassVar[List[Matcher]]
    # the list of plugin matchers (URL pattern + priority)
    # use the streamlink.plugin.pluginmatcher decorator for initializing this list

    # matches: Sequence[Optional[Match]]
    # a tuple of `re.Match` results of all defined matchers

    # matcher: Pattern
    # a reference to the compiled `re.Pattern` of the first matching matcher

    # match: Match
    # a reference to the `re.Match` result of the first matching matcher

    # plugin metadata attributes
    id = None        # type: Optional[str]
    author = None    # type: Optional[str]
    category = None  # type: Optional[str]
    title = None     # type: Optional[str]

    cache = None
    logger = None
    module = "unknown"
    options = Options()
    session = None
    _url = None  # type: Optional[str]

    @classmethod
    def bind(cls, session, module):
        cls.cache = Cache(filename="plugin-cache.json",
                          key_prefix=module)
        cls.logger = logging.getLogger("streamlink.plugins." + module)
        cls.module = module
        cls.session = session

    @property
    def url(self):
        # type: () -> str
        return self._url

    @url.setter
    def url(self, value):
        # type: (str)
        self._url = value

        matches = [(pattern, pattern.match(value)) for pattern, priority in self.matchers or []]
        self.matches = tuple(m for p, m in matches)
        self.matcher, self.match = next(((p, m) for p, m in matches if m is not None), (None, None))

    def __init__(self, url):
        # type: (str) -> None
        self.url = url

        try:
            self.load_cookies()
        except RuntimeError:
            pass  # unbound cannot load

    @classmethod
    def set_option(cls, key, value):
        cls.options.set(key, value)

    @classmethod
    def get_option(cls, key):
        return cls.options.get(key)

    @classmethod
    def get_argument(cls, key):
        return cls.arguments.get(key)

    @classmethod
    def stream_weight(cls, stream):
        return stream_weight(stream)

    @classmethod
    def default_stream_types(cls, streams):
        stream_types = ["rtmp", "hls", "http"]

        for name, stream in iterate_streams(streams):
            stream_type = type(stream).shortname()

            if stream_type not in stream_types:
                stream_types.append(stream_type)

        return stream_types

    @classmethod
    def broken(cls, issue=None):
        def func(*args, **kwargs):
            msg = (
                "This plugin has been marked as broken. This is likely due to "
                "changes to the service preventing a working implementation. "
            )

            if issue:
                msg += "More info: https://github.com/streamlink/streamlink/issues/{0}".format(issue)

            raise PluginError(msg)

        def decorator(*args, **kwargs):
            return func

        return decorator

    def streams(self, stream_types=None, sorting_excludes=None):
        """Attempts to extract available streams.

        Returns a :class:`dict` containing the streams, where the key is
        the name of the stream, most commonly the quality and the value
        is a :class:`Stream` object.

        The result can contain the synonyms **best** and **worst** which
        points to the streams which are likely to be of highest and
        lowest quality respectively.

        If multiple streams with the same name are found, the order of
        streams specified in *stream_types* will determine which stream
        gets to keep the name while the rest will be renamed to
        "<name>_<stream type>".

        The synonyms can be fine tuned with the *sorting_excludes*
        parameter. This can be either of these types:

            - A list of filter expressions in the format
              *[operator]<value>*. For example the filter ">480p" will
              exclude streams ranked higher than "480p" from the list
              used in the synonyms ranking. Valid operators are >, >=, <
              and <=. If no operator is specified then equality will be
              tested.

            - A function that is passed to filter() with a list of
              stream names as input.


        :param stream_types: A list of stream types to return.
        :param sorting_excludes: Specify which streams to exclude from
                                 the best/worst synonyms.

        """

        try:
            ostreams = self._get_streams()
            if isinstance(ostreams, dict):
                ostreams = ostreams.items()

            # Flatten the iterator to a list so we can reuse it.
            if ostreams:
                ostreams = list(ostreams)
        except NoStreamsError:
            return {}
        except (IOError, OSError, ValueError) as err:
            raise PluginError(err)

        if not ostreams:
            return {}

        if stream_types is None:
            stream_types = self.default_stream_types(ostreams)

        # Add streams depending on stream type and priorities
        sorted_streams = sorted(iterate_streams(ostreams),
                                key=partial(stream_type_priority,
                                            stream_types))

        streams = {}
        for name, stream in sorted_streams:
            stream_type = type(stream).shortname()

            # Use * as wildcard to match other stream types
            if "*" not in stream_types and stream_type not in stream_types:
                continue

            # drop _alt from any stream names
            if name.endswith("_alt"):
                name = name[:-len("_alt")]

            existing = streams.get(name)
            if existing:
                existing_stream_type = type(existing).shortname()
                if existing_stream_type != stream_type:
                    name = "{0}_{1}".format(name, stream_type)

                if name in streams:
                    name = "{0}_alt".format(name)
                    num_alts = len(list(filter(lambda n: n.startswith(name), streams.keys())))

                    # We shouldn't need more than 2 alt streams
                    if num_alts >= 2:
                        continue
                    elif num_alts > 0:
                        name = "{0}{1}".format(name, num_alts + 1)

            # Validate stream name and discard the stream if it's bad.
            match = re.match("([A-z0-9_+]+)", name)
            if match:
                name = match.group(1)
            else:
                self.logger.debug("The stream '{0}' has been ignored "
                                  "since it is badly named.", name)
                continue

            # Force lowercase name and replace space with underscore.
            streams[name.lower()] = stream

        # Create the best/worst synonyms
        def stream_weight_only(s):
            return (self.stream_weight(s)[0] or (len(streams) == 1 and 1))

        stream_names = filter(stream_weight_only, streams.keys())
        sorted_streams = sorted(stream_names, key=stream_weight_only)
        unfiltered_sorted_streams = sorted_streams

        if isinstance(sorting_excludes, list):
            for expr in sorting_excludes:
                filter_func = stream_sorting_filter(expr, self.stream_weight)
                sorted_streams = list(filter(filter_func, sorted_streams))
        elif callable(sorting_excludes):
            sorted_streams = list(filter(sorting_excludes, sorted_streams))

        final_sorted_streams = OrderedDict()

        for stream_name in sorted(streams, key=stream_weight_only):
            final_sorted_streams[stream_name] = streams[stream_name]

        if len(sorted_streams) > 0:
            best = sorted_streams[-1]
            worst = sorted_streams[0]
            final_sorted_streams["worst"] = streams[worst]
            final_sorted_streams["best"] = streams[best]
        elif len(unfiltered_sorted_streams) > 0:
            best = unfiltered_sorted_streams[-1]
            worst = unfiltered_sorted_streams[0]
            final_sorted_streams["worst-unfiltered"] = streams[worst]
            final_sorted_streams["best-unfiltered"] = streams[best]

        return final_sorted_streams

    def _get_streams(self):
        raise NotImplementedError

    def get_metadata(self):
        # type: () -> Dict[str, Optional[str]]
        return dict(
            id=self.get_id(),
            author=self.get_author(),
            category=self.get_category(),
            title=self.get_title()
        )

    def get_id(self):
        # type: () -> Optional[str]
        return None if self.id is None else str(self.id).strip()

    def get_title(self):
        # type: () -> Optional[str]
        return None if self.title is None else str(self.title).strip()

    def get_author(self):
        # type: () -> Optional[str]
        return None if self.author is None else str(self.author).strip()

    def get_category(self):
        # type: () -> Optional[str]
        return None if self.category is None else str(self.category).strip()

    def save_cookies(
        self,
        cookie_filter=None,
        default_expires=60 * 60 * 24 * 7,
    ):
        # type: (Optional[Callable[[Cookie], bool]], int) -> List[str]
        """
        Store the cookies from ``http`` in the plugin cache until they expire. The cookies can be filtered
        by supplying a filter method. eg. ``lambda c: "auth" in c.name``. If no expiry date is given in the
        cookie then the ``default_expires`` value will be used.

        :param cookie_filter: a function to filter the cookies
        :type cookie_filter: function
        :param default_expires: time (in seconds) until cookies with no expiry will expire
        :type default_expires: int
        :return: list of the saved cookie names
        """
        if not self.session or not self.cache:
            raise RuntimeError("Cannot cache cookies in unbound plugin")

        cookie_filter = cookie_filter or (lambda c: True)
        saved = []

        for cookie in filter(cookie_filter, self.session.http.cookies):
            cookie_dict = {}
            for key in _COOKIE_KEYS:
                cookie_dict[key] = getattr(cookie, key, None)
            cookie_dict["rest"] = getattr(cookie, "rest", getattr(cookie, "_rest", None))

            expires = default_expires
            if cookie_dict["expires"]:
                expires = int(cookie_dict["expires"] - time.time())
            key = "__cookie:{0}:{1}:{2}:{3}".format(
                cookie.name,
                cookie.domain,
                cookie.port_specified and cookie.port or "80",
                cookie.path_specified and cookie.path or "*",
            )
            self.cache.set(key, cookie_dict, expires)
            saved.append(cookie.name)

        if saved:  # pragma: no branch
            self.logger.debug("Saved cookies: {0}".format(', '.join(saved)))

        return saved

    def load_cookies(self):
        """
        Load any stored cookies for the plugin that have not expired.

        :return: list of the restored cookie names
        """
        if not self.session or not self.cache:
            raise RuntimeError("Cannot load cached cookies in unbound plugin")

        restored = []

        for key, value in self.cache.get_all().items():
            if key.startswith("__cookie"):
                cookie = requests.cookies.create_cookie(**value)
                self.session.http.cookies.set_cookie(cookie)
                restored.append(cookie.name)

        if restored:  # pragma: no branch
            self.logger.debug("Restored cookies: {0}".format(', '.join(restored)))

        return restored

    def clear_cookies(self, cookie_filter=None):
        """
        Removes all of the saved cookies for this Plugin. To filter the cookies that are deleted
        specify the ``cookie_filter`` argument (see :func:`save_cookies`).

        :param cookie_filter: a function to filter the cookies
        :type cookie_filter: function
        :return: list of the removed cookie names
        """
        if not self.session or not self.cache:
            raise RuntimeError("Cannot clear cached cookies in unbound plugin")

        cookie_filter = cookie_filter or (lambda c: True)
        removed = []

        for key, value in sorted(self.cache.get_all().items(), key=operator.itemgetter(0), reverse=True):
            if key.startswith("__cookie"):
                cookie = requests.cookies.create_cookie(**value)
                if cookie_filter(cookie):
                    del self.session.http.cookies[cookie.name]
                    self.cache.set(key, None, 0)
                    removed.append(key)

        return removed

    def input_ask(self, prompt):
        # type: (str) -> str
        user_input_requester = self.session.get_option("user-input-requester")  # type: Optional[UserInputRequester]
        if user_input_requester:
            try:
                return user_input_requester.ask(prompt)
            except (IOError, OSError) as err:
                raise FatalPluginError("User input error: {0}".format(err))
        raise FatalPluginError("This plugin requires user input, however it is not supported on this platform")

    def input_ask_password(self, prompt):
        # type: (str) -> str
        user_input_requester = self.session.get_option("user-input-requester")  # type: Optional[UserInputRequester]
        if user_input_requester:
            try:
                return user_input_requester.ask_password(prompt)
            except (IOError, OSError) as err:
                raise FatalPluginError("User input error: {0}".format(err))
        raise FatalPluginError("This plugin requires user input, however it is not supported on this platform")


def pluginmatcher(pattern, priority=NORMAL_PRIORITY):
    # type: (Pattern, int) -> Callable[[Type[Plugin]], Type[Plugin]]
    """
    Decorator for plugin URL matchers.

    A matcher consists of a compiled regular expression pattern for the plugin's input URL and a priority value.
    The priority value determines which plugin gets chosen by
    :meth:`Streamlink.resolve_url <streamlink.Streamlink.resolve_url>` if multiple plugins match the input URL.

    Plugins must at least have one matcher. If multiple matchers are defined, then the first matching one
    according to the order of which they have been defined (top to bottom) will be responsible for setting the
    :attr:`Plugin.matcher` and :attr:`Plugin.match` attributes on the :class:`Plugin` instance.
    The :attr:`Plugin.matchers` and :attr:`Plugin.matches` attributes are affected by all defined matchers.

    .. code-block:: python

        import re

        from streamlink.plugin import HIGH_PRIORITY, Plugin, pluginmatcher


        @pluginmatcher(re.compile("https?://example:1234/(?:foo|bar)/(?P<name>[^/]+)"))
        @pluginmatcher(priority=HIGH_PRIORITY, pattern=re.compile(\"\"\"
            https?://(?:
                 sitenumberone
                |adifferentsite
                |somethingelse
            )
            /.+\\.m3u8
        \"\"\", re.VERBOSE))
        class MyPlugin(Plugin):
            ...
    """

    matcher = Matcher(pattern, priority)

    def decorator(cls):
        # type: (Type[Plugin]) -> Type[Plugin]
        if not issubclass(cls, Plugin):
            raise TypeError("{0} is not a Plugin".format(repr(cls)))
        if cls.matchers is None:
            cls.matchers = []
        cls.matchers.insert(0, matcher)

        return cls

    return decorator


def pluginargument(
    name,                # type: str
    required=False,      # type: bool
    requires=None,       # type: Optional[Union[str, Sequence[str]]]
    prompt=None,         # type: Optional[str]
    sensitive=False,     # type: bool
    argument_name=None,  # type: Optional[str]
    dest=None,           # type: Optional[str]
    is_global=False,     # type: bool
    **options
):
    # type: () -> Callable[[Type[Plugin]], Type[Plugin]]
    """
    Decorator for plugin arguments. Takes the same arguments as :class:`streamlink.options.Argument`.

    .. code-block:: python

        from streamlink.plugin import Plugin, pluginargument


        @pluginargument(
            "username",
            requires=["password"],
            metavar="EMAIL",
            help="The username for your account.",
        )
        @pluginargument(
            "password",
            sensitive=True,
            metavar="PASSWORD",
            help="The password for your account.",
        )
        class MyPlugin(Plugin):
            ...

    This will add the ``--myplugin-username`` and ``--myplugin-password`` arguments to the CLI,
    assuming the plugin's module name is ``myplugin``.
    """

    arg = Argument(
        name,
        required=required,
        requires=requires,
        prompt=prompt,
        sensitive=sensitive,
        argument_name=argument_name,
        dest=dest,
        is_global=is_global,
        **options
    )

    def decorator(cls):
        # type: (Type[Plugin]) -> Type[Plugin]
        if not issubclass(cls, Plugin):
            raise TypeError("{0} is not a Plugin".format(repr(cls)))
        if cls.arguments is None:
            cls.arguments = Arguments()
        cls.arguments.add(arg)

        return cls

    return decorator


__all__ = [
    "HIGH_PRIORITY", "NORMAL_PRIORITY", "LOW_PRIORITY", "NO_PRIORITY",
    "Plugin",
    "Matcher", "pluginmatcher",
    "pluginargument",
]
