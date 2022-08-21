from typing import Any, Callable, Dict, Optional, Tuple

from lxml.etree import XPathError, iselement

from streamlink.compat import urlparse
from streamlink.plugin.api.validate._exception import ValidationError
from streamlink.plugin.api.validate._schemas import AllSchema, AnySchema, TransformSchema
from streamlink.plugin.api.validate._validate import validate
from streamlink.utils.parse import (
    parse_html as _parse_html,
    parse_json as _parse_json,
    parse_qsd as _parse_qsd,
    parse_xml as _parse_xml,
)


# String related validators


def validator_length(number):
    # type: (int) -> Callable[[str], bool]
    """
    Check input for minimum length using len().
    """

    def min_len(value):
        if not len(value) >= number:
            raise ValidationError(
                "Minimum length is {number}, but value is {value}",
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return min_len


def validator_startswith(string):
    # type (str) -> Callable[[str], bool]
    """
    Check if the input string starts with another string.
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def validator_endswith(string):
    # type (str) -> Callable[[str], bool]
    """
    Check if the input string ends with another string.
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def validator_contains(string):
    # type (str) -> Callable[[str], bool]
    """
    Check if the input string contains another string.
    """

    def contains_str(value):
        validate(str, value)
        if string not in value:
            raise ValidationError(
                "{value} does not contain {string}",
                value=repr(value),
                string=repr(string),
                schema="contains",
            )

        return True

    return contains_str


def validator_url(**attributes):
    # type: (**) -> Callable[[str], bool]
    """
    Parse a URL and validate its attributes using sub-schemas.
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                    context=err,
                )

        return True

    return check_url


# Object related validators


def validator_getattr(attr, default=None):
    # type: (Any, Any) -> TransformSchema
    """
    Get a named attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.
    """

    def getter(value):
        return getattr(value, attr, default)

    return TransformSchema(getter)


def validator_hasattr(attr):
    # type: (Any) -> Callable[[Any], bool]
    """
    Verify that the input object has an attribute with the given name.
    """

    def getter(value):
        return hasattr(value, attr)

    return getter


# Sequence related validators


def validator_filter(func):
    # type: (Callable[[Any], bool]) -> TransformSchema
    """
    Filter out unwanted items from the input using the specified function.

    Supports both dicts and sequences. key/value pairs are expanded when applied to a dict.
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


def validator_map(func):
    # type: (Callable[[Any], Any]) -> TransformSchema
    """
    Transform items from the input using the specified function.

    Supports both dicts and sequences. key/value pairs are expanded when applied to a dict.
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


# lxml.etree related validators


def validator_xml_find(
    path,
    namespaces=None,
):
    # type: (str, Optional[Dict[str, str]]) -> TransformSchema
    """
    Find an XML element (:meth:`Element.find`).
    This method uses the ElementPath query language, which is a subset of XPath.
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
                context=err,
            )

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


def validator_xml_findall(
    path,
    namespaces=None,
):
    # type: (str, Optional[Dict[str, str]]) -> TransformSchema
    """
    Find a list of XML elements (:meth:`Element.findall`).
    This method uses the ElementPath query language, which is a subset of XPath.
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def validator_xml_findtext(
    path,
    namespaces=None,
):
    # type: (str, Optional[Dict[str, str]]) -> AllSchema
    """
    Find an XML element (:meth:`Element.find`) and return its text.
    This method uses the ElementPath query language, which is a subset of XPath.
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        validator_getattr("text"),
    )


def validator_xml_xpath(
    xpath,
    namespaces=None,
    extensions=None,
    smart_strings=True,
    **variables
):
    """
    Query XML elements via XPath (:meth:`Element.xpath`) and return None if the result is falsy.
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
                context=err
            )

        return result or None

    return TransformSchema(transform_xpath)


def validator_xml_xpath_string(
    xpath,
    namespaces=None,
    extensions=None,
    **variables
):
    # type: (str, Optional[Dict[str, str]], Optional[Dict[Tuple[Optional[str], str], Callable[..., Any]]]) -> TransformSchema
    """
    Query XML elements via XPath (:meth:`Element.xpath`),
    transform the result into a string and return None if the result is falsy.
    """

    return validator_xml_xpath(
        "string({0})".format(xpath),
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=False,
        **variables
    )


# Parse utility related validators


def validator_parse_json(*args, **kwargs):
    # type: () -> TransformSchema
    """
    Parse JSON data via the :func:`streamlink.utils.parse.parse_json` utility function.
    """

    return TransformSchema(_parse_json, exception=ValidationError, schema=None, *args, **kwargs)


def validator_parse_html(*args, **kwargs):
    # type: () -> TransformSchema
    """
    Parse HTML data via the :func:`streamlink.utils.parse.parse_html` utility function.
    """

    return TransformSchema(_parse_html, exception=ValidationError, schema=None, *args, **kwargs)


def validator_parse_xml(*args, **kwargs):
    # type: () -> TransformSchema
    """
    Parse XML data via the :func:`streamlink.utils.parse.parse_xml` utility function.
    """

    return TransformSchema(_parse_xml, exception=ValidationError, schema=None, *args, **kwargs)


def validator_parse_qsd(*args, **kwargs):
    # type: () -> TransformSchema
    """
    Parse a query string via the :func:`streamlink.utils.parse.parse_qsd` utility function.
    """

    return TransformSchema(_parse_qsd, exception=ValidationError, schema=None, *args, **kwargs)
