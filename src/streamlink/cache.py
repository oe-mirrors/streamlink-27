import json
import os
import shutil
import tempfile
from time import mktime, time

from streamlink.compat import is_win32

if is_win32:
    xdg_cache = os.environ.get("APPDATA", os.path.expanduser("~"))
else:
    xdg_cache = "/home/root/.cache"

cache_dir = os.path.join(xdg_cache, "streamlink")


class Cache(object):
    """Caches Python values as JSON and prunes expired entries."""

    def __init__(self, filename, key_prefix=""):
        self.key_prefix = key_prefix
        self.filename = os.path.join(cache_dir, filename)

        self._cache = {}

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as fd:
                    self._cache = json.load(fd)
            except Exception:
                self._cache = {}
        else:
            self._cache = {}

    def _prune(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def _save(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        fd.close()

        # Silently ignore errors
        try:
            if not os.path.exists(os.path.dirname(self.filename)):
                os.makedirs(os.path.dirname(self.filename))

            shutil.move(tempname, self.filename)
        except (IOError, OSError):
            os.remove(tempname)

    def set(self, key, value, expires=60 * 60 * 24 * 7, expires_at=None):
        self._load()
        self._prune()

        if self.key_prefix:
            key = "{0}:{1}".format(self.key_prefix, key)

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = mktime(expires_at.timetuple())
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def get(self, key, default=None):
        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = "{0}:{1}".format(self.key_prefix, key)

        if key in self._cache and "value" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def get_all(self):
        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = self.key_prefix + ":"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix):]
                ret[okey] = value["value"]

        return ret


__all__ = ["Cache"]
