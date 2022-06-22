from __future__ import absolute_import

import json
import logging
from threading import RLock, Thread, current_thread
from typing import Any, Dict, List, Optional, Tuple, Union

from websocket import ABNF, STATUS_NORMAL, WebSocketApp, enableTrace

from streamlink.compat import is_py2, str, unquote_plus, urlparse
from streamlink.logger import TRACE, root as rootlogger
from streamlink.session import Streamlink


log = logging.getLogger(__name__)


class WebsocketClient(Thread):
    OPCODE_CONT = ABNF.OPCODE_CONT      # type: int
    OPCODE_TEXT = ABNF.OPCODE_TEXT      # type: int
    OPCODE_BINARY = ABNF.OPCODE_BINARY  # type: int
    OPCODE_CLOSE = ABNF.OPCODE_CLOSE    # type: int
    OPCODE_PING = ABNF.OPCODE_PING      # type: int
    OPCODE_PONG = ABNF.OPCODE_PONG      # type: int

    _id = 0     # type: int

    ws = None   # type: WebSocketApp

    def __init__(
        self,
        session,
        # type: Streamlink
        url,
        # type: str
        subprotocols=None,
        # type: Optional[List[str]]
        header=None,
        # type: Optional[Union[List, Dict]]
        cookie=None,
        # type: Optional[str]
        sockopt=None,
        # type: Optional[Tuple]
        sslopt=None,
        # type: Optional[Dict]
        host=None,
        # type: Optional[str]
        origin=None,
        # type: Optional[str]
        suppress_origin=False,
        # type: bool
        ping_interval=0,
        # type: Union[int, float]
        ping_timeout=None,
        # type: Optional[Union[int, float]]
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, log)

        if not header:
            header = []
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append("User-Agent: {0}".format(session.http.headers['User-Agent']))

        proxy_options = {}
        http_proxy = session.get_option("http-proxy")
        # type: Optional[str]
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            **proxy_options
        )

        self._id += 1
        super(WebsocketClient, self).__init__(
            name="Thread-{0}-{1}".format(self.__class__.__name__, self._id)
        )
        self.daemon = True

    def _ws_init(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data
        )

    def run(self):
        # type: () -> None
        while True:
            log.debug("Connecting to: {0}".format(self.ws.url))
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if not self._reconnect:
                    return
                self._reconnect = False

    # ----

    def reconnect(
        self,
        url=None,
        subprotocols=None,
        header=None,
        cookie=None,
        closeopts=None
    ):
        # type: (str, Optional[List[str]], Optional[Union[List, Dict]], Optional[str], Optional[Dict]) -> None
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie
            )

    def close(self, status=STATUS_NORMAL, reason="", timeout=3):
        # type: (int, Union[str, bytes], int) -> None
        if type(reason) is str:
            if is_py2:
                reason = bytes(reason)
            else:
                reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def send(self, data, opcode=ABNF.OPCODE_TEXT):
        # type: (Union[str, bytes], int) -> None
        return self.ws.send(data, opcode)

    def send_json(self, data):
        # type: (Any) -> None
        return self.send(json.dumps(data, indent=None, separators=(",", ":")))

    # ----

    # noinspection PyMethodMayBeStatic
    def on_open(self, wsapp):
        # type: (WebSocketApp) -> None
        log.debug("Connected: {0}".format(wsapp.url))  # pragma: no cover

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def on_error(self, wsapp, error):
        # type: (WebSocketApp, Exception) -> None
        log.error(error)  # pragma: no cover

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def on_close(self, wsapp, status, message):
        # type: (WebSocketApp, int, str)
        log.debug("Closed: {0}".format(wsapp.url))  # pragma: no cover

    def on_ping(self, wsapp, data):
        # type: (WebSocketApp, bytes) -> None
        pass  # pragma: no cover

    def on_pong(self, wsapp, data):
        # type: (WebSocketApp, bytes) -> None
        pass  # pragma: no cover

    def on_message(self, wsapp, data):
        # type: (WebSocketApp, str) -> None
        pass  # pragma: no cover

    def on_cont_message(self, wsapp, data, cont):
        # type: (WebSocketApp, bytes, Any) -> None
        pass  # pragma: no cover

    def on_data(self, wsapp, data, data_type, cont):
        # type: (WebSocketApp, Union[bytes, str], int, Any) -> None
        pass  # pragma: no cover
