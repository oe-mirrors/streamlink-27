import logging
import re

from streamlink.plugin import Plugin
from streamlink.plugin.api import validate
from streamlink.stream import HLSStream
from streamlink.utils import parse_json
from streamlink.utils.url import url_concat

log = logging.getLogger(__name__)


class Mildom(Plugin):
    _re_url = re.compile(r"""https?://(?:www\.)?mildom\.com/
        (?:
            playback/(\d+)(/(?P<video_id>(\d+)\-(\w+)))
            |
            (?P<channel_id>\d+)
        )
    """, re.VERBOSE)

    @classmethod
    def can_handle_url(cls, url):
        return cls._re_url.match(url)

    def _get_vod_streams(self, video_id):
        data = self.session.http.get(
            "https://cloudac.mildom.com/nonolive/videocontent/playback/getPlaybackDetail",
            params={
                "__platform": "web",
                "v_id": video_id,
            },
            schema=validate.Schema(validate.transform(parse_json), {
                "code": int,
                validate.optional("message"): validate.text,
                validate.optional("body"): {
                    "playback": {
                        "video_link": [{"name": validate.text, "url": validate.url()}],
                    },
                },
            })
        )
        log.trace("{0!r}".format(data))
        if data["code"] != 0:
            log.debug(data.get("message", "Mildom API returned an error"))
            return
        for stream in data["body"]["playback"]["video_link"]:
            yield stream["name"], HLSStream(self.session, stream["url"])

    def _get_live_streams(self, channel_id):
        # Get quality info and check if user is live1
        data = self.session.http.get(
            "https://cloudac.mildom.com/nonolive/gappserv/live/enterstudio",
            params={
                "__platform": "web",
                "user_id": channel_id,
            },
            headers={"Accept-Language": "en"},
            schema=validate.Schema(
                validate.transform(parse_json),
                {
                    "code": int,
                    validate.optional("message"): validate.text,
                    validate.optional("body"): {
                        validate.optional("status"): int,
                        "anchor_live": int,
                        validate.optional("live_type"): int,
                        "ext": {
                            "cmode_params": [{
                                "cmode": validate.text,
                                "name": validate.text,
                            }],
                            validate.optional("live_mode"): int,
                        },
                    },
                },
            )
        )
        log.trace("{0!r}".format(data))
        if data["code"] != 0:
            log.debug(data.get("message", "Mildom API returned an error"))
            return
        if data["body"]["anchor_live"] != 11:
            log.debug("User doesn't appear to be live")
            return
        qualities = []
        for quality_info in data["body"]["ext"]["cmode_params"]:
            qualities.append((quality_info["name"], "_" + quality_info["cmode"] if quality_info["cmode"] != "raw" else ""))

        # Create stream URLs
        data = self.session.http.get(
            "https://cloudac.mildom.com/nonolive/gappserv/live/liveserver",
            params={
                "__platform": "web",
                "user_id": channel_id,
                "live_server_type": "hls",
            },
            headers={"Accept-Language": "en"},
            schema=validate.Schema(
                validate.transform(parse_json),
                {
                    "code": int,
                    validate.optional("message"): validate.text,
                    validate.optional("body"): {
                        "stream_server": validate.url(),
                    }
                }
            )
        )
        log.trace("{0!r}".format(data))
        if data["code"] != 0:
            log.debug(data.get("message", "Mildom API returned an error"))
            return
        base_url = url_concat(data["body"]["stream_server"], "{0}{{}}.m3u8".format(channel_id))
        self.session.http.headers.update({"Referer": "https://www.mildom.com/"})
        for quality in qualities:
            yield quality[0], HLSStream(self.session, base_url.format(quality[1]))

    def _get_streams(self):
        match = self._re_url.match(self.url)
        channel_id = match.group("channel_id")
        video_id = match.group("video_id")
        if video_id:
            return self._get_vod_streams(video_id)
        else:
            return self._get_live_streams(channel_id)
        return


__plugin__ = Mildom
