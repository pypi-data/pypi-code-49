from queue import Queue as _Queue, Empty as _Empty
from threading import Thread as _Thread
from time import time as _time
from typing import Any


class Ticker:
    _alive = True
    _stop_q: _Queue = _Queue()

    def __init__(self, time_to_wait: float, output_queue=_Queue()):
        self._q = output_queue
        self.time_to_wait = time_to_wait
        self._thread = _Thread(target=self.__tick_looper,)
        self._thread.start()

    def __tick_looper(self) -> None:
        while True:
            try:
                exit = self._stop_q.get(timeout=self.time_to_wait)
                if exit:
                    break
            except _Empty:
                self._q.put(_time())

    def stop(self) -> None:
        self._stop_q.put(True)
        self._alive = False

    def is_stopped(self) -> bool:
        return not self._alive and self._thread.is_alive()

    def get(self) -> Any:
        return self._q.get()
