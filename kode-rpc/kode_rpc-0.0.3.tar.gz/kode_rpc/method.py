from typing import Coroutine, Callable, Optional


class RPCMethod:
    def __init__(self, func: Callable[..., Coroutine], name: str, version: int):
        self.name = name
        self.version = version
        self._func = func

    async def __call__(self, *args, **kwargs):
        return await self._func(*args, **kwargs)


def method(*, name: Optional[str] = None, version: int):
    def inner(function):
        return RPCMethod(function, name or function.__name__, version)
    return inner
