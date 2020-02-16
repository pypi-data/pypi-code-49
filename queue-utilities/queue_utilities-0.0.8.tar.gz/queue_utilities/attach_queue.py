import typing as _typing
from threading import Thread as _Thread
from queue import Queue as _Queue


def attach_queue(
    input_queue: _Queue, output_queue: _typing.Optional[_Queue] = None
) -> _typing.Callable[[_typing.Callable[..., _typing.Any]], _Thread]:
    # TODO make a class component for thread cleanup
    def inner(func: _typing.Callable[..., _typing.Any]) -> _Thread:
        def queue_awaiter(func, *args, **kwargs):
            while True:
                message = input_queue.get()
                result = func(message, *args, **kwargs)
                if output_queue is not None:
                    output_queue.put(result)

        def threaded(*args, **kwargs) -> _Thread:
            thread = _Thread(
                target=queue_awaiter, args=(func, *args), kwargs=kwargs, daemon=True,
            )
            thread.start()
            return thread

        return threaded()

    return inner
