from queue import Queue as _Queue
from typing import Any, List
from threading import Thread as _Thread
from .pipe import Pipe as _Pipe


class MulticastClose:
    pass


class Multicast:
    def __init__(self, *queues: _Queue, multicasted_queue: _Queue = _Queue()):
        self.__multicast_queue = multicasted_queue
        self._output_queues = queues
        self.is_stopped = False
        self._thread = _Thread(
            target=self._publisher_multicast,
            args=(self.__multicast_queue, *self._output_queues),
            daemon=True,
        )
        self._thread.start()

    def _publisher_multicast(self, input_queue: _Queue, *output_queues: _Queue):
        while True:
            mes = input_queue.get()
            if isinstance(mes, MulticastClose):
                return
            for o_q in output_queues:
                o_q.put(mes)

    def stop(self) -> None:
        self.__multicast_queue.put(MulticastClose())
        self.is_stopped = True

    def send(self, message: Any) -> None:
        if self.is_stopped:
            raise Exception()
        self.__multicast_queue.put(message)

    def put(self, message: Any) -> None:
        """Alias of the Multicast.send method
        
        Arguments:
            message {Any} -- message to put onto queue
        """
        self.send(message)

    def __call__(self, message: Any) -> None:
        self.send(message)

    def queue(self) -> _Queue:
        return self.__multicast_queue
