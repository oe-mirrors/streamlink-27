import re

from streamlink.plugin import Plugin
from streamlink.stream.ffmpegmux import FFMPEGMuxer


class FFMPEGRTSPPlugin(Plugin):
    # _url_re = re.compile(r"(?P<url>rtsp://.+)")
    _url_re = re.compile(r"ffmpeg://(?P<url>.+)")

    @classmethod
    def can_handle_url(cls, url):
        return cls._url_re.match(url) is not None

    def _get_streams(self):
        url = self._url_re.search(self.url).group("url")
        return {"rtsp_stream": FFMPEGMuxer(self.session, *(url,), is_muxed=False)}


__plugin__ = FFMPEGRTSPPlugin
