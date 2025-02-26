# -*- coding: utf-8 -*-

import unittest

import pytest
import requests

from streamlink.exceptions import PluginError
from streamlink.plugin.api.http_session import HTTPSession, urllib3_version
from tests.mock import PropertyMock, call, patch


@pytest.mark.skipif(urllib3_version < (1, 25, 4), reason="test only applicable on urllib3 >=1.25.4")
class TestUrllib3Overrides:
    @pytest.fixture(scope="class")
    def httpsession(self):
        # type: () -> HTTPSession
        return HTTPSession()

    @pytest.mark.parametrize("url,expected,assertion", [
        ("https://foo/bar%3F?baz%21", "https://foo/bar%3F?baz%21", "Keeps encoded reserved characters"),
        ("https://foo/%62%61%72?%62%61%7A", "https://foo/bar?baz", "Decodes encoded unreserved characters"),
        ("https://foo/bär?bäz", "https://foo/b%C3%A4r?b%C3%A4z", "Encodes other characters"),
        ("https://foo/b%c3%a4r?b%c3%a4z", "https://foo/b%c3%a4r?b%c3%a4z", "Keeps percent-encodings with lowercase characters"),
        ("https://foo/b%C3%A4r?b%C3%A4z", "https://foo/b%C3%A4r?b%C3%A4z", "Keeps percent-encodings with uppercase characters"),
        ("https://foo/%?%", "https://foo/%25?%25", "Empty percent-encodings without valid encodings"),
        ("https://foo/%0?%0", "https://foo/%250?%250", "Incomplete percent-encodings without valid encodings"),
        ("https://foo/%zz?%zz", "https://foo/%25zz?%25zz", "Invalid percent-encodings without valid encodings"),
        ("https://foo/%3F%?%3F%", "https://foo/%253F%25?%253F%25", "Empty percent-encodings with valid encodings"),
        ("https://foo/%3F%0?%3F%0", "https://foo/%253F%250?%253F%250", "Incomplete percent-encodings with valid encodings"),
        ("https://foo/%3F%zz?%3F%zz", "https://foo/%253F%25zz?%253F%25zz", "Invalid percent-encodings with valid encodings"),
    ])
    def test_encode_invalid_chars(self, httpsession, url, expected, assertion):
        # type: (HTTPSession, str, str,str)
        req = requests.Request(method="GET", url=url)
        prep = httpsession.prepare_request(req)
        assert prep.url == expected, assertion


class TestPluginAPIHTTPSession(unittest.TestCase):
    @patch("streamlink.plugin.api.http_session.time.sleep")
    @patch("streamlink.plugin.api.http_session.Session.request")
    def test_read_timeout(self, mock_request, mock_sleep):
        mock_request.side_effect = requests.Timeout
        session = HTTPSession()

        with self.assertRaises(PluginError) as cm:
            session.get("http://localhost/", timeout=123, retries=3, retry_backoff=2, retry_max_backoff=5)
        self.assertTrue(str(cm.exception).startswith("Unable to open URL: http://localhost/"))
        self.assertEqual(mock_request.mock_calls, [
            call(session, "GET", "http://localhost/", headers={}, params={}, timeout=123, proxies={}, allow_redirects=True),
            call(session, "GET", "http://localhost/", headers={}, params={}, timeout=123, proxies={}, allow_redirects=True),
            call(session, "GET", "http://localhost/", headers={}, params={}, timeout=123, proxies={}, allow_redirects=True),
            call(session, "GET", "http://localhost/", headers={}, params={}, timeout=123, proxies={}, allow_redirects=True),
        ])
        self.assertEqual(mock_sleep.mock_calls, [
            call(2),
            call(4),
            call(5)
        ])

    def test_json_encoding(self):
        json_str = u"{\"test\": \"Α and Ω\"}"

        # encode the json string with each encoding and assert that the correct one is detected
        for encoding in ["UTF-32BE", "UTF-32LE", "UTF-16BE", "UTF-16LE", "UTF-8"]:
            with patch('requests.Response.content', new_callable=PropertyMock) as mock_content:
                mock_content.return_value = json_str.encode(encoding)
                res = requests.Response()

                self.assertEqual(HTTPSession.json(res), {u"test": u"\u0391 and \u03a9"})

    def test_json_encoding_override(self):
        json_text = u"{\"test\": \"Α and Ω\"}".encode("cp949")

        with patch('requests.Response.content', new_callable=PropertyMock) as mock_content:
            mock_content.return_value = json_text
            res = requests.Response()
            res.encoding = "cp949"

            self.assertEqual(HTTPSession.json(res), {u"test": u"\u0391 and \u03a9"})
