from typing import Any, Callable, FrozenSet, List, Optional, Pattern, Set, Tuple, Type, Union


class SchemaContainer(object):
    """
    A simple schema container.
    """

    def __init__(self, schema):
        self.schema = schema


class _CollectionSchemaContainer(SchemaContainer):
    def __init__(self, *schemas):
        super(_CollectionSchemaContainer, self).__init__(schemas)


class AllSchema(_CollectionSchemaContainer):
    """
    Collection of schemas where every schema must be valid.
    The last validation result gets returned.
    """


class AnySchema(_CollectionSchemaContainer):
    """
    Collection of schemas where at least one schema must be valid.
    The first successful validation result gets returned.
    """


class NoneOrAllSchema(_CollectionSchemaContainer):
    """
    Collection of schemas where every schema must be valid. If the initial input is None, all validations will be skipped.
    The last validation result gets returned.
    """


class ListSchema(_CollectionSchemaContainer):
    """
    Collection of schemas where every indexed schema must be valid, as well as the input type and length.
    A new list of the validated input gets returned.
    """


class GetItemSchema(object):
    """
    Get an item from the input.

    Unless strict is set to True, item can be a tuple of items for recursive lookups.
    If the item is not found in the last object of a recursive lookup, return the default.
    Supported inputs are XML elements, regex matches and anything that implements __getitem__.
    """

    def __init__(
        self,
        item,
        default=None,
        strict=False,
    ):
        # type: (Union[Any, Tuple[Any]], Any, bool)
        self.item = item
        self.default = default
        self.strict = strict


class RegexSchema(object):
    """
    A regex pattern that must match using the provided method.
    """

    def __init__(
        self,
        pattern,
        # TODO: change type from str to Literal["search", "match", "fullmatch", "findall", "split", "sub", "subn"]
        method="search",
    ):
        # type: (Pattern, str)
        self.pattern = pattern
        self.method = method


class TransformSchema(object):
    """
    Transform the input using the specified function and args/keywords.
    """

    def __init__(
        self,
        func,
        *args,
        **kwargs
    ):
        # type: (Callable,)
        self.func = func
        self.args = args
        self.kwargs = kwargs


class OptionalSchema(object):
    """
    An optional key set in a dict or dict in a :class:`UnionSchema`.
    """

    def __init__(self, key):
        # type: (Any)
        self.key = key


class AttrSchema(SchemaContainer):
    """
    Validate attributes of an input object.
    """


class XmlElementSchema(object):
    """
    Validate an XML element.
    """

    # signature is weird because of backwards compatiblity
    def __init__(
        self,
        tag=None,
        text=None,
        attrib=None,
        tail=None
    ):
        # type: (Optional[Any], Optional[Any], Optional[Any], Optional[Any])
        self.tag = tag
        self.attrib = attrib
        self.text = text
        self.tail = tail


class UnionGetSchema(object):
    """
    Validate multiple :class:`GetItemSchema` schemas on the same input.
    """

    def __init__(self, *getters, **kw):
        self.getters = tuple(GetItemSchema(getter) for getter in getters)
        self.seq = kw.get("seq", tuple)
        # type: Type[Union[List, FrozenSet, Set, Tuple]]


class UnionSchema(SchemaContainer):
    """
    Validate multiple schemas on the same input.

    Can be a tuple, list, set, frozenset or dict of schemas.
    """
