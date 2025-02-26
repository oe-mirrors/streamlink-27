import unittest
from threading import Event

from streamlink.stream.hls import HLSStream
from streamlink.stream.hls_filtered import FilteredHLSStreamReader, FilteredHLSStreamWriter
from tests.mixins.stream_hls import Playlist, Segment, TestMixinStreamHLS
from tests.mock import MagicMock, call, patch

FILTERED = "filtered"


class SegmentFiltered(Segment):
    def __init__(self, *args, **kwargs):
        super(SegmentFiltered, self).__init__(*args, **kwargs)
        self.title = FILTERED


class _TestSubjectFilteredHLSStreamWriter(FilteredHLSStreamWriter):
    def __init__(self, *args, **kwargs):
        super(_TestSubjectFilteredHLSStreamWriter, self).__init__(*args, **kwargs)
        self.write_wait = Event()
        self.write_done = Event()

    def write(self, *args, **kwargs):
        # only write once per step
        self.write_wait.wait()
        self.write_wait.clear()

        try:
            # don't write again during teardown
            if not self.closed:
                super(_TestSubjectFilteredHLSStreamWriter, self).write(*args, **kwargs)
        finally:
            # notify main thread that writing has finished
            self.write_done.set()


class _TestSubjectFilteredHLSReader(FilteredHLSStreamReader):
    __writer__ = _TestSubjectFilteredHLSStreamWriter


class _TestSubjectFilteredHLSStream(HLSStream):
    __reader__ = _TestSubjectFilteredHLSReader


@patch("streamlink.stream.hls.HLSStreamWorker.wait", MagicMock(return_value=True))
class TestFilteredHLSStream(TestMixinStreamHLS, unittest.TestCase):
    __stream__ = _TestSubjectFilteredHLSStream

    @classmethod
    def filter_sequence(cls, sequence):
        return sequence.segment.title == FILTERED

    def close_thread(self):
        self.thread.reader.writer.write_wait.set()
        super(TestFilteredHLSStream, self).close_thread()

    # make one write call on the write thread and wait until it has finished
    def await_write(self):
        writer = self.thread.reader.writer
        writer.write_wait.set()
        writer.write_done.wait()
        writer.write_done.clear()

    def get_session(self, options=None, *args, **kwargs):
        session = super(TestFilteredHLSStream, self).get_session(options)
        session.set_option("hls-live-edge", 2)
        session.set_option("stream-timeout", 0)

        return session

    def subject(self, *args, **kwargs):
        thread, segments = super(TestFilteredHLSStream, self).subject(*args, **kwargs)

        return thread, thread.reader, thread.reader.writer, segments

    # don't patch should_filter_sequence here (it always returns False)
    def test_not_filtered(self):
        thread, reader, writer, segments = self.subject([
            Playlist(0, [SegmentFiltered(0), SegmentFiltered(1)], end=True)
        ])

        self.await_write()
        self.await_write()
        data = self.await_read()
        self.assertEqual(data, self.content(segments), "Does not filter by default")

    @patch("streamlink.stream.hls_filtered.FilteredHLSStreamWriter.should_filter_sequence", new=filter_sequence)
    @patch("streamlink.stream.hls_filtered.log")
    def test_filtered_logging(self, mock_log):
        thread, reader, writer, segments = self.subject([
            Playlist(0, [SegmentFiltered(0), SegmentFiltered(1)]),
            Playlist(2, [Segment(2), Segment(3)]),
            Playlist(4, [SegmentFiltered(4), SegmentFiltered(5)]),
            Playlist(6, [Segment(6), Segment(7)], end=True)
        ])
        data = b""

        self.assertTrue(reader.filter_event.is_set(), "Doesn't let the reader wait if not filtering")

        for i in range(2):
            self.await_write()
            self.await_write()
            self.assertEqual(len(mock_log.info.mock_calls), i * 2 + 1)
            self.assertEqual(mock_log.info.mock_calls[i * 2 + 0], call("Filtering out segments and pausing stream output"))
            self.assertFalse(reader.filter_event.is_set(), "Lets the reader wait if filtering")

            self.await_write()
            self.await_write()
            self.assertEqual(len(mock_log.info.mock_calls), i * 2 + 2)
            self.assertEqual(mock_log.info.mock_calls[i * 2 + 1], call("Resuming stream output"))
            self.assertTrue(reader.filter_event.is_set(), "Doesn't let the reader wait if not filtering")

            data += self.await_read()

        self.assertEqual(
            data,
            self.content(segments, cond=lambda s: s.num % 4 > 1),
            "Correctly filters out segments"
        )
        self.assertTrue(all([self.called(s) for s in segments.values()]), "Downloads all segments")

    @patch("streamlink.stream.hls_filtered.FilteredHLSStreamWriter.should_filter_sequence", new=filter_sequence)
    def test_filtered_timeout(self):
        thread, reader, writer, segments = self.subject([
            Playlist(0, [Segment(0), Segment(1)], end=True)
        ])

        self.await_write()
        data = self.await_read()
        self.assertEqual(data, segments[0].content, "Has read the first segment")

        # simulate a timeout by having an empty buffer
        # timeout value is set to 0
        with self.assertRaises(IOError) as cm:
            self.await_read()
        self.assertEqual(str(cm.exception), "Read timeout", "Raises a timeout error when no data is available to read")

    @patch("streamlink.stream.hls_filtered.FilteredHLSStreamWriter.should_filter_sequence", new=filter_sequence)
    def test_filtered_no_timeout(self):
        thread, reader, writer, segments = self.subject([
            Playlist(0, [SegmentFiltered(0), SegmentFiltered(1)]),
            Playlist(2, [Segment(2), Segment(3)], end=True)
        ])

        self.assertTrue(reader.filter_event.is_set(), "Doesn't let the reader wait if not filtering")

        self.await_write()
        self.await_write()
        self.assertFalse(reader.filter_event.is_set(), "Lets the reader wait if filtering")

        # make reader read (no data available yet)
        thread.read_wait.set()
        # once data becomes available, the reader continues reading
        self.await_write()
        self.assertTrue(reader.filter_event.is_set(), "Reader is not waiting anymore")

        thread.read_done.wait()
        thread.read_done.clear()
        self.assertFalse(thread.error, "Doesn't time out when filtering")
        self.assertEqual(b"".join(thread.data), segments[2].content, "Reads next available buffer data")

        self.await_write()
        data = self.await_read()
        self.assertEqual(data, self.content(segments, cond=lambda s: s.num >= 2))

    @patch("streamlink.stream.hls_filtered.FilteredHLSStreamWriter.should_filter_sequence", new=filter_sequence)
    def test_filtered_closed(self):
        thread, reader, writer, segments = self.subject([
            Playlist(0, [SegmentFiltered(0), SegmentFiltered(1)])
        ])

        # mock the reader thread's filter_event.wait method, so that the main thread can wait on its call
        filter_event_wait_called = Event()
        orig_wait = reader.filter_event.wait

        def mocked_wait(*args, **kwargs):
            filter_event_wait_called.set()
            return orig_wait(*args, **kwargs)

        mock = patch.object(reader.filter_event, "wait", side_effect=mocked_wait)
        mock.start()

        # write first filtered segment and trigger the filter_event's lock
        self.assertTrue(reader.filter_event.is_set(), "Doesn't let the reader wait if not filtering")
        self.await_write()
        self.assertFalse(reader.filter_event.is_set(), "Lets the reader wait if filtering")

        # make reader read (no data available yet)
        thread.read_wait.set()
        # before calling reader.close(), wait until reader thread's filter_event.wait was called
        filter_event_wait_called.wait()

        # close stream while reader is waiting for filtering to end
        thread.reader.close()
        thread.read_done.wait()
        thread.read_done.clear()
        self.assertEqual(thread.data, [b""], "Stops reading on stream close")
        self.assertFalse(thread.error, "Is not a read timeout on stream close")

        mock.stop()
