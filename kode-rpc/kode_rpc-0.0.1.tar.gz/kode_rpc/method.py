from typing import Coroutine, Callable


class RPCMethod:
    def __init__(self, func: Callable[..., Coroutine], name: str, version: int):
        self.name = name
        self.version = version
        self._func = func

    async def __call__(self, *args, **kwargs):
        return await self._func(*args, **kwargs)


def method(name: str, version: int):
    def inner(function):
        return RPCMethod(function, name, version)
    return inner
