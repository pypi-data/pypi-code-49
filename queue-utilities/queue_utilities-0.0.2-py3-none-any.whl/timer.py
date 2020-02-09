from queue import Queue as _Queue
import time as _time
from threading import Thread as _Thread
from typing import Optional
from .select import Select as _Select


class Timer:
    """TODO: cleanup thread after timer is manually stopped.
    """

    def __init__(self, time_to_wait: float, output_queue=_Queue()):
        if time_to_wait <= 0:
            raise TypeError("time_to_wait must be greater than zero")
        self._time_to_wait = time_to_wait
        self._is_finished = False
        self._stop_q = _Queue()
        self._output_q = output_queue
        self._select = _Select(self._stop_q)
        self._timer_thread = _Thread(
            target=self._timer, args=(self._output_q, self._time_to_wait), daemon=True
        )
        self._timer_thread.start()

    def _timer(self, output_q: _Queue, wait_time: float) -> None:
        _time.sleep(wait_time)
        output_q.put(_time.time())

    def _wait_select(self):
        message = None
        for (which_q, message) in self._select:
            if which_q is self._output_q:
                message = None
            elif which_q is self._stop_q:
                break

        self._is_finished = True
        self._select.stop()
        return message

    def get(self, *, timeout: Optional[float] = None) -> float:
        return self._output_q.get(timeout=timeout)

    def __call__(self):
        return self.get()

    def stop(self) -> bool:
        if self._is_finished:
            return False
        else:
            self._stop_q.put(None)
            return True
