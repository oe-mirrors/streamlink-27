import logging
import re
import struct
from collections import OrderedDict, defaultdict, namedtuple

from requests.exceptions import ChunkedEncodingError, ConnectionError, ContentDecodingError

from streamlink.compat import str, urlparse
from streamlink.exceptions import StreamError
from streamlink.stream.ffmpegmux import FFMPEGMuxer, MuxedStream
from streamlink.stream.hls_playlist import load as load_hls_playlist
from streamlink.stream.http import HTTPStream
from streamlink.stream.segmented import SegmentedStreamReader, SegmentedStreamWorker, SegmentedStreamWriter
from streamlink.utils.crypto import AES, unpad
from streamlink.utils.formatter import Formatter

log = logging.getLogger(__name__)
Sequence = namedtuple("Sequence", "num segment")


class HLSStreamWriter(SegmentedStreamWriter):
    def __init__(self, reader, *args, **kwargs):
        options = reader.stream.session.options
        kwargs["ignore_names"] = options.get("hls-segment-ignore-names")
        SegmentedStreamWriter.__init__(self, reader, *args, **kwargs)

        self.byterange_offsets = defaultdict(int)
        self.key_data = None
        self.key_uri = None
        self.key_uri_override = options.get("hls-segment-key-uri")
        self.stream_data = options.get("hls-segment-stream-data")

        if self.ignore_names:
            # creates a regex from a list of segment names,
            # this will be used to ignore segments.
            self.ignore_names = list(set(self.ignore_names))
            self.ignore_names = "|".join(list(map(re.escape, self.ignore_names)))
            self.ignore_names_re = re.compile(r"(?:{blacklist})\.ts".format(
                blacklist=self.ignore_names), re.IGNORECASE)

    @staticmethod
    def num_to_iv(n):
        # type: (int) -> bytes
        return struct.pack(">8xq", n)

    def create_decryptor(self, key, sequence):
        if key.method != "AES-128":
            raise StreamError("Unable to decrypt cipher {0}".format(key.method))

        if not self.key_uri_override and not key.uri:
            raise StreamError("Missing URI for decryption key")

        if self.key_uri_override:
            p = urlparse(key.uri)
            formatter = Formatter({
                "url": lambda: key.uri,
                "scheme": lambda: p.scheme,
                "netloc": lambda: p.netloc,
                "path": lambda: p.path,
                "query": lambda: p.query,
            })
            key_uri = formatter.format(self.key_uri_override)
        else:
            key_uri = key.uri

        if self.key_uri != key_uri:
            res = self.session.http.get(key_uri, exception=StreamError,
                                        retries=self.retries,
                                        **self.reader.request_params)
            res.encoding = "binary/octet-stream"
            self.key_data = res.content
            self.key_uri = key_uri

        iv = key.iv or self.num_to_iv(sequence)

        # Pad IV if needed
        iv = b"\x00" * (16 - len(iv)) + iv

        return AES.new(self.key_data, AES.MODE_CBC, iv)

    def create_request_params(self, sequence):
        request_params = dict(self.reader.request_params)
        headers = request_params.pop("headers", {})

        if sequence.segment.byterange:
            bytes_start = self.byterange_offsets[sequence.segment.uri]
            if sequence.segment.byterange.offset is not None:
                bytes_start = sequence.segment.byterange.offset

            bytes_len = max(sequence.segment.byterange.range - 1, 0)
            bytes_end = bytes_start + bytes_len
            headers["Range"] = "bytes={0}-{1}".format(bytes_start, bytes_end)
            self.byterange_offsets[sequence.segment.uri] = bytes_end + 1

        request_params["headers"] = headers

        return request_params

    def fetch(self, sequence, retries=None):
        if self.closed or not retries:
            return

        try:
            request_params = self.create_request_params(sequence)
            # skip ignored segment names
            if self.ignore_names and self.ignore_names_re.search(sequence.segment.uri):
                log.debug("Skipping segment {0}".format(sequence.num))
                return

            return self.session.http.get(sequence.segment.uri,
                                         stream=self.stream_data,
                                         timeout=self.timeout,
                                         exception=StreamError,
                                         retries=self.retries,
                                         **request_params)
        except StreamError as err:
            log.error("Failed to open segment {0}: {1}", sequence.num, err)
            return

    def write(self, sequence, result, chunk_size=8192):
        if sequence.segment.key and sequence.segment.key.method != "NONE":
            try:
                decryptor = self.create_decryptor(sequence.segment.key,
                                                  sequence.num)
            except (StreamError, ValueError) as err:
                log.error("Failed to create decryptor: {0}".format(err))
                self.close()
                return

            try:
                # Unlike plaintext segments, encrypted segments can't be written to the buffer in small chunks
                # because of the byte padding at the end of the decrypted data, which means that decrypting in
                # smaller chunks is unnecessary if the entire segment needs to be kept in memory anyway, unless
                # we defer the buffer writes by one read call and apply the unpad call only to the last read call.
                encrypted_chunk = result.content
                decrypted_chunk = decryptor.decrypt(encrypted_chunk)
                chunk = unpad(decrypted_chunk, AES.block_size, style="pkcs7")
                self.reader.buffer.write(chunk)
            except (ChunkedEncodingError, ContentDecodingError, ConnectionError) as err:
                log.error("Download of segment {0} failed: {1}".format(sequence.num, err))
                return
            except ValueError as err:
                log.error("Error while decrypting segment {0}: {1}".format(sequence.num, err))
                return
        else:
            try:
                for chunk in result.iter_content(chunk_size):
                    self.reader.buffer.write(chunk)
            except (ChunkedEncodingError, ContentDecodingError, ConnectionError) as err:
                log.error("Download of segment {0} failed: {1}".format(sequence.num, err))
                return

        log.debug("Download of segment {0} complete".format(sequence.num))


class HLSStreamWorker(SegmentedStreamWorker):
    def __init__(self, *args, **kwargs):
        SegmentedStreamWorker.__init__(self, *args, **kwargs)
        self.stream = self.reader.stream

        self.playlist_changed = False
        self.playlist_end = None
        self.playlist_sequence = -1
        self.playlist_sequences = []
        self.playlist_reload_time = 6
        self.playlist_reload_time_override = self.session.options.get("hls-playlist-reload-time")
        self.playlist_reload_retries = self.session.options.get("hls-playlist-reload-attempts")
        self.live_edge = self.session.options.get("hls-live-edge")
        self.duration_offset_start = int(self.stream.start_offset + (self.session.options.get("hls-start-offset") or 0))
        self.duration_limit = self.stream.duration or (
            int(self.session.options.get("hls-duration")) if self.session.options.get("hls-duration") else None)
        self.hls_live_restart = self.stream.force_restart or self.session.options.get("hls-live-restart")

        if str(self.playlist_reload_time_override).isnumeric() and float(self.playlist_reload_time_override) >= 2:
            self.playlist_reload_time_override = float(self.playlist_reload_time_override)
        elif self.playlist_reload_time_override not in ["segment", "live-edge"]:
            self.playlist_reload_time_override = 0

        self.reload_playlist()

        if self.playlist_end is None:
            if self.duration_offset_start > 0:
                log.debug("Time offsets negative for live streams, skipping back {0} seconds".format(
                          self.duration_offset_start))
            # live playlist, force offset durations back to None
            self.duration_offset_start = -self.duration_offset_start

        if self.duration_offset_start != 0:
            self.playlist_sequence = self.duration_to_sequence(self.duration_offset_start, self.playlist_sequences)

        if self.playlist_sequences:
            log.debug("First Sequence: {0}; Last Sequence: {1}".format(
                      self.playlist_sequences[0].num, self.playlist_sequences[-1].num))
            log.debug("Start offset: {0}; Duration: {1}; Start Sequence: {2}; End Sequence: {3}".format(
                      self.duration_offset_start, self.duration_limit,
                      self.playlist_sequence, self.playlist_end))

    def _fetch_playlist(self):
        res = self.session.http.get(
            self.stream.url,
            exception=StreamError,
            retries=self.playlist_reload_retries,
            **self.reader.request_params
        )
        res.encoding = "utf-8"

        return res

    # TODO: rename to _parse_playlist
    def _reload_playlist(self, *args, **kwargs):
        return load_hls_playlist(*args, **kwargs)

    def reload_playlist(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()

        log.debug("Reloading playlist")
        res = self._fetch_playlist()

        try:
            playlist = self._reload_playlist(res)
        except ValueError as err:
            raise StreamError(err)

        if playlist.is_master:
            raise StreamError("Attempted to play a variant playlist, use "
                              "'hls://{0}' instead".format(self.stream.url))

        if playlist.iframes_only:
            raise StreamError("Streams containing I-frames only is not playable")

        media_sequence = playlist.media_sequence or 0
        sequences = [Sequence(media_sequence + i, s)
                     for i, s in enumerate(playlist.segments)]

        self.playlist_reload_time = self._playlist_reload_time(playlist, sequences)

        if sequences:
            self.process_sequences(playlist, sequences)

    def _playlist_reload_time(self, playlist, sequences):
        if self.playlist_reload_time_override == "segment" and sequences:
            return sequences[-1].segment.duration
        if self.playlist_reload_time_override == "live-edge" and sequences:
            return sum([s.segment.duration for s in sequences[-max(1, self.live_edge - 1):]])
        if type(self.playlist_reload_time_override) is float and self.playlist_reload_time_override > 0:
            return self.playlist_reload_time_override
        if playlist.target_duration:
            return playlist.target_duration
        if sequences:
            return sum([s.segment.duration for s in sequences[-max(1, self.live_edge - 1):]])

        return self.playlist_reload_time

    def process_sequences(self, playlist, sequences):
        first_sequence, last_sequence = sequences[0], sequences[-1]

        if first_sequence.segment.key and first_sequence.segment.key.method != "NONE":
            log.debug("Segments in this playlist are encrypted")

        self.playlist_changed = ([s.num for s in self.playlist_sequences] != [s.num for s in sequences])
        self.playlist_sequences = sequences

        if not self.playlist_changed:
            self.playlist_reload_time = max(self.playlist_reload_time / 2, 1)

        if playlist.is_endlist:
            self.playlist_end = last_sequence.num

        if self.playlist_sequence < 0:
            if self.playlist_end is None and not self.hls_live_restart:
                edge_index = -(min(len(sequences), max(int(self.live_edge), 1)))
                edge_sequence = sequences[edge_index]
                self.playlist_sequence = edge_sequence.num
            else:
                self.playlist_sequence = first_sequence.num

    def valid_sequence(self, sequence):
        return sequence.num >= self.playlist_sequence

    def duration_to_sequence(self, duration, sequences):
        d = 0
        default = -1

        sequences_order = sequences if duration >= 0 else reversed(sequences)

        for sequence in sequences_order:
            if d >= abs(duration):
                return sequence.num
            d += sequence.segment.duration
            default = sequence.num

        # could not skip far enough, so return the default
        return default

    def iter_segments(self):
        total_duration = 0
        while not self.closed:
            for sequence in filter(self.valid_sequence, self.playlist_sequences):
                log.debug("Adding segment {0} to queue".format(sequence.num))
                yield sequence
                total_duration += sequence.segment.duration
                if self.duration_limit and total_duration >= self.duration_limit:
                    log.info("Stopping stream early after {0}".format(self.duration_limit))
                    return

                # End of stream
                stream_end = self.playlist_end and sequence.num >= self.playlist_end
                if self.closed or stream_end:
                    return

                self.playlist_sequence = sequence.num + 1

            if self.wait(self.playlist_reload_time):
                try:
                    self.reload_playlist()
                except StreamError as err:
                    log.warning("Failed to reload playlist: {0}", err)


class HLSStreamReader(SegmentedStreamReader):
    __worker__ = HLSStreamWorker
    __writer__ = HLSStreamWriter

    def __init__(self, stream, *args, **kwargs):
        SegmentedStreamReader.__init__(self, stream, *args, **kwargs)
        self.request_params = dict(stream.args)

        # These params are reserved for internal use
        self.request_params.pop("exception", None)
        self.request_params.pop("stream", None)
        self.request_params.pop("timeout", None)
        self.request_params.pop("url", None)


class MuxedHLSStream(MuxedStream):
    __shortname__ = "hls-multi"

    def __init__(
        self,
        session,
        video,
        audio,
        url_master=None,
        multivariant=None,
        force_restart=False,
        ffmpeg_options=None,
        **args
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param video: Video stream URL
        :param audio: Audio stream URL or list of URLs
        :param url_master: The URL of the HLS playlist's multivariant playlist (deprecated)
        :param multivariant: The parsed multivariant playlist
        :param force_restart: Start from the beginning after reaching the playlist's end
        :param ffmpeg_options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`
        :param args: Additional keyword arguments passed to :class:`HLSStream`
        """

        tracks = [video]
        maps = ["0:v?", "0:a?"]
        if audio:
            if isinstance(audio, list):
                tracks.extend(audio)
            else:
                tracks.append(audio)
        for i in range(1, len(tracks)):
            maps.append("{0}:a".format(i))
        substreams = map(lambda url: HLSStream(session, url, force_restart=force_restart, **args), tracks)
        ffmpeg_options = ffmpeg_options or {}

        super(MuxedHLSStream, self).__init__(session, *substreams, format="mpegts", maps=maps, **ffmpeg_options)
        self._url_master = url_master
        self.multivariant = multivariant if multivariant and multivariant.is_master else None

    @property
    def url_master(self):
        """Deprecated"""
        return self.multivariant.uri if self.multivariant and self.multivariant.uri else self._url_master

    def to_manifest_url(self):
        url = self.multivariant.uri if self.multivariant and self.multivariant.uri else self.url_master

        if url is None:
            return super(MuxedHLSStream, self).to_manifest_url()

        return url


class HLSStream(HTTPStream):
    """Implementation of the Apple HTTP Live Streaming protocol

    *Attributes:*

    - :attr:`url` The URL to the HLS playlist.
    - :attr:`args` A :class:`dict` containing keyword arguments passed
      to :meth:`requests.request`, such as headers and cookies.

    """

    __shortname__ = "hls"
    __reader__ = HLSStreamReader

    def __init__(
        self,
        session_,
        url,
        url_master=None,
        multivariant=None,
        force_restart=False,
        start_offset=0,
        duration=None,
        **args
    ):
        """
        :param streamlink.Streamlink session_: Streamlink session instance
        :param url: The URL of the HLS playlist
        :param url_master: The URL of the HLS playlist's multivariant playlist (deprecated)
        :param multivariant: The parsed multivariant playlist
        :param force_restart: Start from the beginning after reaching the playlist's end
        :param start_offset: Number of seconds to be skipped from the beginning
        :param duration: Number of seconds until ending the stream
        :param args: Additional keyword arguments passed to :meth:`requests.Session.request`
        """
        super(HLSStream, self).__init__(session_, url, **args)
        self._url_master = url_master
        self.multivariant = multivariant if multivariant and multivariant.is_master else None
        self.force_restart = force_restart
        self.start_offset = start_offset
        self.duration = duration

    def __json__(self):
        json = HTTPStream.__json__(self)

        try:
            json["master"] = self.to_manifest_url()
        except TypeError:
            pass

        del json["method"]
        del json["body"]

        return json

    @property
    def url_master(self):
        """Deprecated"""
        return self.multivariant.uri if self.multivariant and self.multivariant.uri else self._url_master

    def to_manifest_url(self):
        url = self.multivariant.uri if self.multivariant and self.multivariant.uri else self.url_master

        if url is None:
            return super(HLSStream, self).to_manifest_url()

        args = self.args.copy()
        args.update(url=url)

        return self.session.http.prepare_new_request(**args).url

    def open(self):
        reader = self.__reader__(self)
        reader.open()

        return reader

    @classmethod
    def _fetch_variant_playlist(cls, session, url, **request_params):
        res = session.http.get(url, exception=OSError, **request_params)
        res.encoding = "utf-8"

        return res

    # TODO: rename to _parse_variant_playlist
    @classmethod
    def _get_variant_playlist(cls, *args, **kwargs):
        return load_hls_playlist(*args, **kwargs)

    @classmethod
    def parse_variant_playlist(cls, session_, url, name_key="name",
                               name_prefix="", check_streams=False,
                               force_restart=False, name_fmt=None,
                               start_offset=0, duration=None,
                               **request_params):
        """Attempts to parse a variant playlist and return its streams.

        :param url: The URL of the variant playlist.
        :param name_key: Prefer to use this key as stream name, valid keys are:
                         name, pixels, bitrate.
        :param name_prefix: Add this prefix to the stream names.
        :param check_streams: Only allow streams that are accessible.
        :param force_restart: Start at the first segment even for a live stream
        :param name_fmt: A format string for the name, allowed format keys are
                         name, pixels, bitrate.
        """
        locale = session_.localization
        audio_select = session_.options.get("hls-audio-select") or []

        res = cls._fetch_variant_playlist(session_, url, **request_params)

        try:
            multivariant = cls._get_variant_playlist(res)
        except ValueError as err:
            raise IOError("Failed to parse playlist: {0}".format(err))

        streams = OrderedDict()
        for playlist in filter(lambda p: not p.is_iframe, multivariant.playlists):
            names = dict(name=None, pixels=None, bitrate=None)
            audio_streams = []
            fallback_audio = []
            default_audio = []
            preferred_audio = []
            for media in playlist.media:
                if media.type == "VIDEO" and media.name:
                    names["name"] = media.name
                elif media.type == "AUDIO":
                    audio_streams.append(media)
            for media in audio_streams:
                # Media without a uri is not relevant as external audio
                if not media.uri:
                    continue

                if not fallback_audio and media.default:
                    fallback_audio = [media]

                # if the media is "audoselect" and it better matches the users preferences, use that
                # instead of default
                if not default_audio and (media.autoselect and locale.equivalent(language=media.language)):
                    default_audio = [media]

                # select the first audio stream that matches the users explict language selection
                if (('*' in audio_select or media.language in audio_select or media.name in audio_select)
                        or ((not preferred_audio or media.default) and locale.explicit and locale.equivalent(
                            language=media.language))):
                    preferred_audio.append(media)

            # final fallback on the first audio stream listed
            fallback_audio = fallback_audio or (len(audio_streams) and audio_streams[0].uri and [audio_streams[0]])

            if playlist.stream_info.resolution:
                width, height = playlist.stream_info.resolution
                names["pixels"] = "{0}p".format(height)

            if playlist.stream_info.bandwidth:
                bw = playlist.stream_info.bandwidth

                if bw >= 1000:
                    names["bitrate"] = "{0}k".format(int(bw / 1000.0))
                else:
                    names["bitrate"] = "{0}k".format(bw / 1000.0)

            if name_fmt:
                stream_name = name_fmt.format(**names)
            else:
                stream_name = (
                    names.get(name_key)
                    or names.get("name")
                    or names.get("pixels")
                    or names.get("bitrate")
                )

            if not stream_name:
                continue
            if name_prefix:
                stream_name = "{0}{1}".format(name_prefix, stream_name)

            if stream_name in streams:  # rename duplicate streams
                stream_name = "{0}_alt".format(stream_name)
                num_alts = len(list(filter(lambda n: n.startswith(stream_name), streams.keys())))

                # We shouldn't need more than 2 alt streams
                if num_alts >= 2:
                    continue
                elif num_alts > 0:
                    stream_name = "{0}{1}".format(stream_name, num_alts + 1)

            if check_streams:
                try:
                    session_.http.get(playlist.uri, **request_params)
                except KeyboardInterrupt:
                    raise
                except Exception:
                    continue

            external_audio = preferred_audio or default_audio or fallback_audio

            if external_audio and FFMPEGMuxer.is_usable(session_):
                external_audio_msg = u", ".join([
                    u"(language={0}, name={1})".format(x.language, (x.name or "N/A"))
                    for x in external_audio
                ])
                log.debug(u"Using external audio tracks for stream {0} {1}".format(
                          stream_name, external_audio_msg))

                stream = MuxedHLSStream(session_,
                                        video=playlist.uri,
                                        audio=[x.uri for x in external_audio if x.uri],
                                        multivariant=multivariant,
                                        force_restart=force_restart,
                                        start_offset=start_offset,
                                        duration=duration,
                                        **request_params)
            else:
                stream = cls(session_,
                             playlist.uri,
                             multivariant=multivariant,
                             force_restart=force_restart,
                             start_offset=start_offset,
                             duration=duration,
                             **request_params)
            streams[stream_name] = stream

        return streams
