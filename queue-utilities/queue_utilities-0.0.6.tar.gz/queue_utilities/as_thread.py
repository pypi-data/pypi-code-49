import typing as _typing
from threading import Thread as _Thread


def as_thread(func: _typing.Callable[_typing.List[_typing.Any], None]):
    def threaded(*args, **kwargs) -> _Thread:
        thread = _Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread

    return threaded

