import logging
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor
from sys import version_info
from threading import Event, Thread, current_thread

from streamlink.buffers import RingBuffer
from streamlink.compat import queue
from streamlink.stream.stream import StreamIO

log = logging.getLogger(__name__)


class CompatThreadPoolExecutor(ThreadPoolExecutor):
    if version_info < (3, 9):
        def shutdown(self, wait=True, cancel_futures=False):
            with self._shutdown_lock:
                self._shutdown = True
                if cancel_futures:
                    # Drain all work items from the queue, and then cancel their
                    # associated futures.
                    while True:
                        try:
                            work_item = self._work_queue.get_nowait()
                        except queue.Empty:
                            break
                        if work_item is not None:
                            work_item.future.cancel()

                # Send a wake-up to prevent threads calling
                # _work_queue.get(block=True) from permanently blocking.
                self._work_queue.put(None)
            if wait:
                for t in self._threads:
                    t.join()


class AwaitableMixin(object):
    def __init__(self, *args, **kwargs):
        super(AwaitableMixin, self).__init__(*args, **kwargs)
        self._wait = Event()

    def wait(self, time):
        # type: (float) -> bool
        """
        Pause the thread for a specified time.
        Return False if interrupted by another thread and True if the time runs out normally.
        """
        return not self._wait.wait(time)


class SegmentedStreamWorker(AwaitableMixin, Thread):
    """The general worker thread.

    This thread is responsible for queueing up segments in the
    writer thread.
    """

    def __init__(self, reader, **kwargs):
        super(SegmentedStreamWorker, self).__init__(name="Thread-{0}".format(self.__class__.__name__))
        self.daemon = True
        self.closed = False
        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.stream.session

    def close(self):
        """Shuts down the thread."""
        if not self.closed:
            log.debug("Closing worker thread")

        self.closed = True
        if self._wait:
            self._wait.set()

    def iter_segments(self):
        """The iterator that generates segments for the worker thread.

        Should be overridden by the inheriting class.
        """
        return
        yield

    def run(self):
        for segment in self.iter_segments():
            if self.closed:
                break
            self.writer.put(segment)

        # End of stream, tells the writer to exit
        self.writer.put(None)
        self.close()


class SegmentedStreamWriter(AwaitableMixin, Thread):
    """The writer thread.

    This thread is responsible for fetching segments, processing them
    and finally writing the data to the buffer.
    """

    def __init__(self, reader, size=20, retries=None, threads=None, timeout=None, ignore_names=None):
        super(SegmentedStreamWriter, self).__init__(name="Thread-{0}".format(self.__class__.__name__))
        self.daemon = True
        self.closed = False
        self.reader = reader
        self.stream = reader.stream
        self.session = reader.stream.session

        if not retries:
            retries = self.session.options.get("stream-segment-attempts")

        if not threads:
            threads = self.session.options.get("stream-segment-threads")

        if not timeout:
            timeout = self.session.options.get("stream-segment-timeout")

        self.retries = retries
        self.timeout = timeout
        self.ignore_names = ignore_names
        self.executor = CompatThreadPoolExecutor(max_workers=threads)
        self.futures = queue.Queue(size)

    def close(self):
        """Shuts down the thread."""
        if not self.closed:
            log.debug("Closing writer thread")

        self.closed = True
        self.reader.buffer.close()
        self.executor.shutdown(wait=True, cancel_futures=True)
        self._wait.set()

    def put(self, segment):
        """Adds a segment to the download pool and write queue."""
        if self.closed:
            return

        if segment is not None:
            future = self.executor.submit(self.fetch, segment,
                                          retries=self.retries)
        else:
            future = None

        self.queue(self.futures, (segment, future))

    def queue(self, queue_, value):
        """Puts a value into a queue but aborts if this thread is closed."""
        while not self.closed:
            try:
                queue_.put(value, block=True, timeout=1)
                return
            except queue.Full:
                continue

    def fetch(self, segment):
        """Fetches a segment.

        Should be overridden by the inheriting class.
        """
        pass

    def write(self, segment, result):
        """Writes a segment to the buffer.

        Should be overridden by the inheriting class.
        """
        pass

    def run(self):
        while not self.closed:
            try:
                segment, future = self.futures.get(block=True, timeout=0.5)
            except queue.Empty:
                continue

            # End of stream
            if future is None:
                break

            while not self.closed:
                try:
                    result = future.result(timeout=0.5)
                except futures.TimeoutError:
                    continue
                except futures.CancelledError:
                    break

                if result is not None:
                    self.write(segment, result)

                break

        self.close()


class SegmentedStreamReader(StreamIO):
    __worker__ = SegmentedStreamWorker
    __writer__ = SegmentedStreamWriter

    def __init__(self, stream, timeout=None):
        StreamIO.__init__(self)
        self.session = stream.session
        self.stream = stream

        if not timeout:
            timeout = self.session.options.get("stream-timeout")

        self.timeout = timeout

    def open(self):
        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)
        self.writer = self.__writer__(self)
        self.worker = self.__worker__(self)

        self.writer.start()
        self.worker.start()

    def close(self):
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker:  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer:  # pragma: no branch
            self.writer.join(timeout=self.timeout)

    def read(self, size):
        if not self.buffer:
            return b""

        return self.buffer.read(size, block=self.writer.is_alive(),
                                timeout=self.timeout)
