"""
$description Japanese live-streaming and video hosting social platform.
$url live.line.me
$type live, vod
"""

import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream


@pluginmatcher(re.compile(
    r"https?://live\.line\.me/channels/(?P<channel>\d+)/broadcast/(?P<broadcast>\d+)"
))
class LineLive(Plugin):
    _URL_API = "https://live-api.line-apps.com/web/v4.0/channel/{channel}/broadcast/{broadcast}/player_status"

    def _get_streams(self):
        channel = self.match.group("channel")
        broadcast = self.match.group("broadcast")

        schema_hls_urls = validate.any(None, {
            validate.text: validate.any(None, validate.url(path=validate.endswith(".m3u8"))),
        })

        status, liveUrls, vodUrls = self.session.http.get(
            self._URL_API.format(channel=channel, broadcast=broadcast),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "liveStatus": validate.text,
                    "liveHLSURLs": schema_hls_urls,
                    "archivedHLSURLs": schema_hls_urls,
                },
                validate.union_get("liveStatus", "liveHLSURLs", "archivedHLSURLs"),
            ),
        )
        streams = {"LIVE": liveUrls, "FINISHED": vodUrls}.get(status, {})

        if streams.get("abr"):
            return HLSStream.parse_variant_playlist(self.session, streams.get("abr"))

        return {
            "{0}p".format(quality): HLSStream(self.session, url)
            for quality, url in streams.items()
            if url and quality.isdecimal()
        }


__plugin__ = LineLive
