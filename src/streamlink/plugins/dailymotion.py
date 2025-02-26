"""
$description Global live-streaming and video on-demand hosting platform.
$url dailymotion.com
$type live, vod
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.stream.http import HTTPStream


log = logging.getLogger(__name__)


@pluginmatcher(re.compile(r"""
    https?://(?:\w+\.)?dailymotion\.com
    (?:
        (/embed)?/(video|live)/(?P<media_id>[^_?/]+)
        |
        /(?P<user>[\w-]+)
    )
""", re.VERBOSE))
class DailyMotion(Plugin):
    _URL_API_USER_VIDEO = "https://api.dailymotion.com/user/{user}/videos"
    _URL_STREAM_INFO = "https://www.dailymotion.com/player/metadata/video/{media_id}"

    def _get_streams_from_media(self, media_id):
        media = self.session.http.get(
            self._URL_STREAM_INFO.format(media_id=media_id),
            cookies={
                "family_filter": "off",
                "ff": "off",
            },
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    {
                        "error": {"type": "not_found"},
                    },
                    {
                        "error": {"title": validate.text},
                    },
                    {
                        "owner.username": validate.text,
                        "title": validate.text,
                        "qualities": {
                            validate.text: [{
                                "type": validate.text,
                                "url": validate.url(),
                            }],
                        },
                    },
                ),
            ),
        )

        error = media.get("error")
        if error:
            if error.get("type") == "not_found":
                log.error("Unknown media ID: {0}".format(media_id))
            else:
                log.error("Failed to get stream: {0}".format(error['title']))
            return

        self.id = media_id
        self.author = media["owner.username"]
        self.title = media["title"]

        for quality, streams in media["qualities"].items():
            for stream in streams:
                if stream["type"] == "application/x-mpegURL":
                    if quality != "auto":
                        # Avoid duplicate HLS streams with bitrate selector in the URL query
                        continue
                    for s in HLSStream.parse_variant_playlist(self.session, stream["url"]).items():
                        yield s
                elif stream["type"] == "video/mp4":
                    # Drop FPS in quality
                    quality = re.sub(r"@\d+", "", quality)
                    resolution = "{0}p".format(quality)
                    yield resolution, HTTPStream(self.session, stream["url"])

    def _get_media_id(self, user):
        # https://developers.dailymotion.com/tools/
        data = self.session.http.get(
            self._URL_API_USER_VIDEO.format(user=user),
            params={
                "fields": "id",
                "flags": "live_onair",
                "family_filter": "false",
            },
            acceptable_status=(200, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    {
                        "error": {"message": validate.text},
                    },
                    {
                        "list": [{"id": validate.text}],
                    },
                ),
            ),
        )

        if data.get("error"):
            log.error("Error while retrieving media ID: {0}".format(data['error']['message']))
            return

        if not data["list"]:
            log.error("No live streams found for channel {0}".format(user))
            return

        return data["list"][0]["id"]

    def _get_streams(self):
        media_id = self.match.group("media_id")
        user = self.match.group("user")

        if not media_id and user:
            media_id = self._get_media_id(user)

        if media_id:
            log.debug("Found media ID: {0}".format(media_id))
            return self._get_streams_from_media(media_id)


__plugin__ = DailyMotion
