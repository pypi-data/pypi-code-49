import queue as _queue
import threading as _threading
from typing import Any, List, Iterator

from .pipe import Pipe


class Select:
    """Analogue to select in Golang to be able to wait on multiple queues simultaneously.
    This is similar in functionality to the builtin python select
    but acting on queues instead of unix pipes.
    Usage:
        q1 = Queue()
        q2 = Queue()
        queue_select = Select(q1, q2)
        for (which_q, message) in queue_select:
            if which_q is q1:
                print(f"I got a message {message} from queue 1")
            elif which_q is q2:
                print(f"I got a message {message} from queue 2")
    """

    def __init__(
        self, *queues: _queue.Queue,
    ):
        self.__multiplexed_queue = _queue.Queue(maxsize=0)
        self._input_queues = queues
        self._pipes: List[Pipe] = [
            Pipe(q_in, self.__multiplexed_queue, with_queue=True)
            for q_in in self._input_queues
        ]
        self.is_stopped = False

    def stop(self) -> None:
        for pipe in self._pipes:
            pipe.stop()
        self.is_stopped = True

    def ouput(self) -> _queue.Queue:
        return self.__multiplexed_queue

    def __call__(self) -> Any:
        return self.__multiplexed_queue.get()

    def __next__(self) -> Any:
        if self.is_stopped:
            raise StopIteration
        return self.__multiplexed_queue.get()

    def __iter__(self) -> Iterator[Any]:
        return self
