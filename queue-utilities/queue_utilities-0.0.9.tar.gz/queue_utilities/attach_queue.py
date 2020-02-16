import typing as _typing
from threading import Thread as _Thread
from queue import Queue as _Queue


def with_output_queue(
    output_queue: _Queue,
) -> _typing.Callable[
    [_typing.Callable[..., _typing.Any]], _typing.Callable[..., None]
]:
    def inner(func: _typing.Callable[..., _typing.Any]) -> _typing.Callable[..., None]:
        def with_result_pipe(*args, **kwargs) -> None:
            result = func(*args, **kwargs)
            output_queue.put(result)

        return with_result_pipe

    return inner


def with_input_queue(
    input_queue: _Queue, output_queue: _typing.Optional[_Queue] = None
) -> _typing.Callable[[_typing.Callable[..., _typing.Any]], _Thread]:
    # TODO make a class component for thread cleanup
    def inner(func: _typing.Callable[..., _typing.Any]) -> _Thread:

        wrapped_func = (
            with_output_queue(output_queue)(func) if output_queue is not None else func
        )

        def queue_awaiter(func_to_invoke, *args, **kwargs):
            while True:
                message = input_queue.get()
                func_to_invoke(message, *args, **kwargs)

        def threaded(*args, **kwargs) -> _Thread:
            thread = _Thread(
                target=queue_awaiter,
                args=(wrapped_func, *args),
                kwargs=kwargs,
                daemon=True,
            )
            thread.start()
            return thread

        return threaded()

    return inner
