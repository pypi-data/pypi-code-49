from queue import Queue as _Queue
from typing import Any, List, Iterator
from .pipe import Pipe as _Pipe


class MultiplexClosed(Exception):
    pass


class Multiplex:
    def __init__(
        self, *queues: _Queue,
    ):
        self.__multiplexed_queue = _Queue(maxsize=0)
        self._input_queues = queues
        self._pipes: List[_Pipe] = [
            _Pipe(q_in, self.__multiplexed_queue) for q_in in self._input_queues
        ]
        self.is_stopped = False

    def stop(self) -> None:
        for pipe in self._pipes:
            pipe.stop()
        self.is_stopped = True

    def ouput(self) -> _Queue:
        return self.__multiplexed_queue

    def get(self) -> Any:
        if self.is_stopped:
            raise MultiplexClosed
        return self.__multiplexed_queue.get()

    def __call__(self) -> Any:
        return self.get()

    def __next__(self) -> Any:
        if self.is_stopped:
            raise StopIteration
        return self.get()

    def __iter__(self) -> Iterator[Any]:
        return self
