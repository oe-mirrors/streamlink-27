import os
import signal
import warnings

import pytest

# import streamlink_cli as early as possible to execute its default signal overrides
# noinspection PyUnresolvedReferences
import streamlink_cli  # noqa: F401
from streamlink.compat import is_py2, is_py3


# immediately restore default signal handlers for the test runner
signal.signal(signal.SIGINT, signal.default_int_handler)
signal.signal(signal.SIGTERM, signal.default_int_handler)


# make pytest rewrite assertions in dynamically parametrized plugin tests
# https://docs.pytest.org/en/stable/how-to/writing_plugins.html#assertion-rewriting
pytest.register_assert_rewrite("tests.plugins")


def catch_warnings(record=False, module=None):
    def _catch_warnings_wrapper(f):
        def _catch_warnings(*args, **kwargs):
            with warnings.catch_warnings(record=True, module=module) as w:
                if record:
                    return f(*(args + (w,)), **kwargs)
                else:
                    return f(*args, **kwargs)

        return _catch_warnings

    return _catch_warnings_wrapper


windows_only = pytest.mark.skipif(os.name != "nt", reason="test only applicable on Windows")
posix_only = pytest.mark.skipif(os.name != "posix", reason="test only applicable on a POSIX OS")
py3_only = pytest.mark.skipif(not is_py3, reason="test only applicable for Python 3")
py2_only = pytest.mark.skipif(not is_py2, reason="test only applicable for Python 2")


__all__ = ['catch_warnings', 'windows_only', 'posix_only', 'py2_only', 'py3_only']
