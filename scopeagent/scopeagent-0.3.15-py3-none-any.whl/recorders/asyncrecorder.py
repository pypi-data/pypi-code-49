import atexit
import logging
import os
import threading
import time
from abc import abstractmethod
import sys

import six

from scopeagent.recorders.utils import fix_timestamps, ProcessLocal, UnrecoverableClientError, RecoverableClientError

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty

from ..tracer import tags, SpanRecorder

SUCCESS_MESSAGE = """
** Scope Test Report **

Access the detailed test report for this build at:
{api_endpoint}/external/v1/results/{agent_id}
"""

PARTIAL_SUCCESS_MESSAGE = """
** Scope Test Report (partial results) **

There has been and error: {flush_error}
You can still access the test report for this build at:
{api_endpoint}/external/v1/results/{agent_id}
"""

ERROR_MESSAGE = 'There has been an error uploading your results: {flush_error}'


LOOP_PERIOD = 1  # seconds between buffer checks
logger = logging.getLogger(__name__)
_proclocal = ProcessLocal()

MAXIMUM_ALLOWED_MEMORY_IN_BUFFER = 5e7  # 50 Megabytes


class AsyncRecorder(SpanRecorder):
    def __init__(self, period=1, test_only=True, testing_mode=True):
        super(AsyncRecorder, self).__init__()
        self.period = period
        self.test_only = test_only
        self.main_pid = os.getpid()
        self.ensure_recorder_thread()
        self.testing_mode = testing_mode
        self._has_flushed = False
        self._test_found = False
        self._flush_error = None

    # We show the link so long as the agent has been initialised in testing mode and
    # we have found a test.
    @property
    def should_show_report_link(self):
        return self.testing_mode and self._test_found

    def _show_report_link(self):
        message = None
        if self._has_flushed:
            if self._flush_error:
                message = PARTIAL_SUCCESS_MESSAGE
            else:
                message = SUCCESS_MESSAGE
        elif self._flush_error:
            message = ERROR_MESSAGE

        if message:
            six.print_(
                message.format(
                    api_endpoint=self._api_endpoint, agent_id=self.metadata['agent.id'], flush_error=self._flush_error,
                )
            )

    def ensure_recorder_thread(self):
        if 'setup' not in _proclocal:
            logger.debug("[%d] starting asyncrecorder thread", os.getpid())
            thread = threading.Thread(target=self.run)
            thread.daemon = True
            thread.start()
            _proclocal['thread'] = thread
            atexit.register(self.stop)
            _proclocal['queue'] = Queue()
            _proclocal['setup'] = True

    def record_span(self, span):
        if not span.context.sampled:
            return

        if self.test_only and span.context.baggage.get(tags.TRACE_KIND) != 'test':
            return

        self.ensure_recorder_thread()
        _proclocal['queue'].put(fix_timestamps(span), block=False)

    def run(self):
        running = True
        buffer = []
        loop_duration = 0
        while running:
            time.sleep(LOOP_PERIOD)
            loop_duration += LOOP_PERIOD
            try:
                while True:
                    # This raises Empty() if the queue is empty
                    item = _proclocal['queue'].get(block=False)
                    _proclocal['queue'].task_done()
                    # This only happens if None has been explicitly put in the queue, when
                    # we want to stop the thread.
                    if item is None:
                        running = False
                        self.flush_final_payload()
                        raise Empty()
                    self._test_found = True
                    if sys.getsizeof(buffer) + sys.getsizeof(item) <= MAXIMUM_ALLOWED_MEMORY_IN_BUFFER:
                        buffer.append(item)
            except Empty:
                pass

            # We flush the buffer if any of the following apply:
            # * Last time we flushed was more than `self.period` seconds ago (even if buffer is empty)
            #   and we are in the parent process
            # * The recorder is being shut down
            # * There is data to be flushed in the buffer
            if (loop_duration >= self.period and os.getpid() == self.main_pid) or not running or len(buffer) > 0:
                loop_duration = 0
                try:
                    self.flush(buffer)
                    if len(buffer) > 0:
                        self._has_flushed = True
                    buffer = []
                except UnrecoverableClientError as e:
                    self._flush_error = str(e)
                    logger.debug("exception while flushing buffer - stopped trying: %s", self._flush_error)
                    running = False
                except RecoverableClientError as e:
                    self._flush_error = str(e)
                    logger.debug("exception while flushing buffer - retrying: %s", self._flush_error)
                    buffer = []
                except Exception as e:
                    self._flush_error = str(e)
                    logger.debug(
                        "exception while flushing buffer - trying again in next iteration: %s", self._flush_error
                    )

    def stop(self):
        try:
            if 'setup' in _proclocal:
                logger.debug("stopping asyncrecorder thread")
                _proclocal['queue'].put(None)
                _proclocal['thread'].join()
        except Exception as e:
            logger.debug("failed to stop: %s", e)

        if self.should_show_report_link:
            self._show_report_link()

    @abstractmethod
    def flush(self, spans):
        raise NotImplementedError()
