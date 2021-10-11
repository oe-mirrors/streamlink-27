"""
  YoutubeDL Plugin for Streamlink by Billy2011.
  This plugin is only for youtube streams.
  The URL's must have a "youtubedl://" prefix
  Version 0.30 / 2021-09-30
"""

from __future__ import unicode_literals

import logging
import os
import re
from platform import node as hostname

from streamlink.plugin import Plugin, PluginArgument, PluginArguments, PluginError, pluginmatcher
from streamlink.stream import HLSStream, HTTPStream
from streamlink.stream.ffmpegmux import MuxedStream

log = logging.getLogger(__name__)

try:
    from youtube_dl import YoutubeDL
    youtubedl = True
except ImportError:
    youtubedl = False
    log.trace("YoutubeDL is not available")


@pluginmatcher(re.compile(r"""
    youtubedl://(?:https?://)?(?:\w+\.)?youtu(?:\.be|be\.com)
    (?:
        (?:
            /(?:
                watch.+v=
                |
                embed/(?!live_stream)
                |
                (?:v/)?
            )(?P<video_id>[\w-]{11})(?P<pl_id>(?:&list=)[\w-]+)?
        )
        |
        (?:
            /(?:
                (?:user|c(?:hannel)?)/
                |
                embed/live_stream\?channel=
            )[^/?&]+
        )
        |
        (?:
            /(?:c/)?[^/?]+/live/?$
        )
    )
""", re.VERBOSE))
class YouTubeDL(Plugin):
    _re_ytInitialPlayerResponse = re.compile(r"""var\s+ytInitialPlayerResponse\s*=\s*({.*?});\s*var\s+meta\s*=""", re.DOTALL)

    _url_canonical = "https://www.youtube.com/watch?v={video_id}"

    adp_video_h264 = {
        135: "480p",  # h264
        136: "720p",  # h264
        137: "1080p",  # h264
    }
    adp_video_vp9 = {
        247: "720p",  # vp9
        302: "720p60",  # vp9 HFR
        248: "1080p",  # vp9
        271: "1440p",  # vp9
        308: "1440p60",  # vp9 HFR
        313: "2160p",  # vp9
        315: "2160p60",  # vp9 HFR
    }
    adp_video_vp9_hdr = {
        334: "720p60hdr",  # vp9 HFR HDR
        335: "1080p60hdr",  # vp9 HFR HDR
        336: "1440p60hdr",  # vp9 HFR HDR
        337: "2160p60hdr",  # vp9 HFR HDR
    }
    video = {  # h264
        93: "360p",  # HLS
        94: "480p",  # HLS
        95: "720p",  # HLS
        96: "1080p",  # HLS
        300: "720p60",  # HLS HFR
        301: "1080p60",  # HLS HFR
        22: "720p",
        35: "480p",
        18: "360p",
        34: "360p",
    }
    adp_audio = {
        140: 128,
        141: 256,
        171: 128,
        172: 256,
        249: 48,
        250: 64,
        251: 160,
        256: 256,
        258: 258,
    }
    ytdl_options = {
        "nocheckcertificate": True,
        "restrictfilenames": True,
        "no_warnings": True,
        "quiet": True,
        "print_json": True,
        "extract_flat": True,
        "list_thumbnails": False,
        "youtube_include_dash_manifest": False,
    }
    stb_vp9_1 = frozenset(["vuuno4k", "vuuno4kse", "vuultimo4k"])  # vp9 profile 1 supp.
    stb_vp9_2 = frozenset(["vuzero4k", "vuduo4k"])  # vp9 profile 2 supp.

    arguments = PluginArguments(
        PluginArgument(
            "playlist-dir",
            type=str,
            metavar="PATH",
        ),
        PluginArgument(
            "yes-vp9-codecs",
            action="store_true",
        ),
        PluginArgument(
            "no-vp9-codecs",
            action="store_true",
        ),
        PluginArgument(
            "yes-vp9-hdr-codecs",
            action="store_true",
        ),
        PluginArgument(
            "no-adaptive-streams",
            action="store_true",
        ),
        PluginArgument(
            "no-opus-codec",
            action="store_true",
        ),
    )

    @classmethod
    def stream_weight(cls, stream):
        match_3d = re.match(r"(\w+)_3d", stream)
        match_hfr = re.match(r"(\d+p)(\d+)", stream)
        if match_3d:
            weight, group = Plugin.stream_weight(match_3d.group(1))
            weight -= 1
            group = "youtube_3d"
        elif match_hfr:
            weight, group = Plugin.stream_weight(match_hfr.group(1))
            weight += 1
            group = "high_frame_rate"
        else:
            weight, group = Plugin.stream_weight(stream)

        return weight, group

    def _create_adaptive_streams(self, info, streams):
        if not MuxedStream.is_usable(self.session):
            log.info("Cannot use FFMPEG")
            return streams

        adaptive_streams = {}
        best_audio_itag = None
        adp_video = self.adp_video_h264.copy()
        vp9 = "vp9" if hostname() in self.stb_vp9_1 or hostname() in self.stb_vp9_2 else ""
        if not vp9:
            log.debug("STB w/o vp9 4K support detected")
            if self.get_option("yes-vp9-codecs"):
                vp9 = "vp9"
        elif self.get_option("no-vp9-codecs"):
            vp9 = ""
            log.info("VP9 Codecs are skipped")
        if vp9:
            adp_video.update(self.adp_video_vp9)
            if self.get_option("yes-vp9-hdr-codecs") or hostname() in self.stb_vp9_2:
                adp_video.update(self.adp_video_vp9_hdr)

        # Extract streams from the DASH format list
        for stream_info in info.get("formats", []):
            itag = int(stream_info["format_id"])
            if itag not in self.adp_audio and itag not in adp_video:
                log.debug(
                    "Skipped format:{}, Codec:{}",
                    stream_info["format"],
                    stream_info["acodec"] if stream_info["acodec"] != "none" else stream_info["vcodec"],
                )
                continue

            # extract any high quality streams only available in adaptive formats and not skipped
            adaptive_streams[itag] = stream_info["url"]
            stream_format = stream_info["ext"]
            if itag in self.adp_audio:
                if self.get_option("no-opus-codec") and stream_info["acodec"] == "opus":
                    log.debug("Skipped format:{}, Codec:{}", stream_info["format"], stream_info["acodec"])
                    continue

                stream = HTTPStream(self.session, stream_info["url"])
                name = "audio_{0}".format(stream_format)
                streams[name] = stream

                # find the best quality audio stream m4a, opus or vorbis
                if best_audio_itag is None or self.adp_audio[itag] > self.adp_audio[best_audio_itag]:
                    best_audio_itag = itag

        if best_audio_itag and adaptive_streams and MuxedStream.is_usable(self.session):
            aurl = adaptive_streams[best_audio_itag]
            for itag, name in adp_video.items():
                if itag in adaptive_streams:
                    vurl = adaptive_streams[itag]
                    log.debug(
                        "MuxedStream: v {video} a {audio} = {name}".format(
                            audio=best_audio_itag,
                            name=name,
                            video=itag,
                        )
                    )
                    streams[name] = MuxedStream(self.session, HTTPStream(self.session, vurl), HTTPStream(self.session, aurl))

        return streams

    def _save2M3U(self, pl_path, info, ua):
        m3u = "#EXTM3U,$MODE=IPTV\n"
        if pl_path.startswith("/tmp/." + __name__):
            pl_title = "Playlist(temp.)"
        else:
            pl_title = info["title"]
        for item in info.get("entries", []):
            title = item.get("title")
            url = item.get("id")
            if not (url and title):
                continue

            url = "http://127.0.0.1:8088/youtubedl://youtube.com/watch?v={0}".format(url)
            if title not in ["[Deleted video]", "[Private video]"]:
                m3u += "#EXTINF:0,{0}\n{1}\n".format(title, url)

        path = os.path.join(pl_path, "YTDL: " + pl_title + ".m3u").encode("utf8")
        if not os.path.isfile(path) or path.startswith("/tmp/." + __name__):
            with open(path, "w") as f:
                f.write(m3u)
            log.info("M3U Playlist '{0}' written".format(path))
        else:
            log.info("M3U Playlist '{0}' exists, skipped".format(path))

    def _get_stream_info(self, video_id, pl_id):
        info = None
        log.debug("Starting YoutubeDL process")
        try:
            ytdl = YoutubeDL(self.ytdl_options)
            url = "https://www.youtube.com/watch?v=%s" % video_id
            info = ytdl.extract_info(url, ie_key="Youtube", download=False, process=True)
            ua = info["formats"][-1]["http_headers"]["User-Agent"]
            self.session.http.headers.update({"User-Agent": ua})

            pl_path = self.get_option("playlist-dir")
            if pl_id and pl_path:
                if not os.path.isdir(pl_path):
                    os.makedirs(pl_path)
                    log.debug("Playlist directory '{0}' created".format(pl_path))

                url = "https://www.youtube.com/playlist?list=%s" % pl_id
                _info = ytdl.extract_info(url, ie_key="YoutubePlaylist", download=False, process=True)
                self._save2M3U(pl_path, _info, ua)
        except Exception as e:
            raise PluginError(e)

        return info

    def _get_streams(self):
        is_live = False
        self.video_id = self.match.group("video_id")
        self.pl_id = self.match.group("pl_id")
        if not self.video_id:
            log.trace("Bypass youtubedl...")
            return self.session.streams(self.url.replace("youtubedl://", ""))

        if not youtubedl:
            return

        info = self._get_stream_info(self.video_id, self.pl_id)
        if not info:
            log.error("Could not get video info")
            return

        if info.get("is_live"):
            log.debug("This video is live.")
            is_live = True

        streams = {}
        for stream_info in info.get("formats", []):
            itag = int(stream_info["format_id"])
            if itag not in self.video:
                if is_live:
                    log.debug(
                        "Skipped format:{}, Codecs: v {} a {}",
                        stream_info["format"],
                        stream_info["vcodec"],
                        stream_info["acodec"],
                    )
                continue

            url = stream_info["url"]
            name = self.video[itag]
            if stream_info.get("protocol", "") != "m3u8":
                stream = HTTPStream(self.session, url)
                streams[name] = stream
            else:
                stream = HLSStream(self.session, url)
                streams[name] = stream

        if not is_live and not self.get_option("no-adaptive-streams"):
            streams = self._create_adaptive_streams(info, streams)
        else:
            log.info("Adaptive streams are skipped")

        return streams


__plugin__ = YouTubeDL
