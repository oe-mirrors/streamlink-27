import os.path
import re
import unittest

from streamlink import Streamlink, plugins as streamlinkplugins
from streamlink.compat import is_py2
from streamlink_cli.argparser import build_parser


class TestPluginMeta(unittest.TestCase):
    """
    Test that each plugin has an entry in the plugin matrix and a test file
    """
    longMessage = False

    protocol_tests = ["http", "hls", "dash", "stream", "rtmp"]

    @classmethod
    def setUpClass(cls):
        cls.session = Streamlink()
        docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs"))
        plugins_dir = streamlinkplugins.__path__[0]

        with open(os.path.join(docs_dir, "plugin_matrix.rst")) as plfh:
            parts = re.split(r"\n[= ]+\n", plfh.read())
            cls.plugins_in_docs = list(re.findall(r"^([\w_]+)\s", parts[3], re.MULTILINE))

        with open(os.path.join(plugins_dir, ".removed")) as rmfh:
            cls.plugins_removed = [pname for pname in rmfh.read().split("\n") if pname and not pname.startswith("#")]

        cls.plugins = cls.session.plugins.keys()
        cls.plugins_no_protocols = [pname for pname in cls.plugins if pname not in cls.protocol_tests]

    def test_plugin_has_docs_matrix(self):
        for pname in self.plugins_no_protocols:
            self.assertIn(pname, self.plugins_in_docs, "{0} is not in plugin matrix".format(pname))

    def test_docs_matrix_has_plugin(self):
        for pname in self.plugins_in_docs:
            self.assertIn(pname, self.plugins_no_protocols, "{0} plugin does not exist".format(pname))

    def test_plugin_has_valid_global_args(self):
        parser = build_parser()
        global_arg_dests = [action.dest for action in parser._actions]
        for pname, plugin in self.session.plugins.items():
            for parg in plugin.arguments:
                if not parg.is_global:  # pragma: no cover
                    continue
                self.assertIn(
                    parg.dest,
                    global_arg_dests,
                    "{0} from plugins.{1} is not a valid global argument".format(parg.name, pname)
                )
