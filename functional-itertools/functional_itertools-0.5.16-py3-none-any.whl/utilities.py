from enum import auto
from enum import Enum
from sys import version_info
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple
from typing import TypeVar

from functional_itertools.errors import UnsupportVersionError


_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")
_W = TypeVar("_W")


def filter_keys_helper(
    func: Callable[[_T], _U],
) -> Callable[[Tuple[_T, Any]], _U]:
    def inner(item: Tuple[_T, Any]) -> _U:  # noqa: U101
        key, _ = item
        return func(key)

    return inner


def filter_values_helper(
    func: Callable[[_T], _U],
) -> Callable[[Tuple[Any, _T]], _U]:
    def inner(item: Tuple[Any, _T]) -> _U:  # noqa: U101
        _, value = item
        return func(value)

    return inner


def filter_items_helper(
    func: Callable[[_T, _U], _V],
) -> Callable[[Tuple[_T, _U]], _V]:
    def inner(item: Tuple[_T, _U]) -> _V:  # noqa: U101
        key, value = item
        return func(key, value)

    return inner


def map_keys_helper(func: Callable[[_T], _U]) -> Callable[[Tuple[_T, Any]], _U]:
    def inner(item: Tuple[_T, _V]) -> Tuple[_U, _V]:
        key, value = item
        return func(key), value

    return inner


def map_values_helper(
    func: Callable[[_T], _U],
) -> Callable[[Tuple[Any, _T]], _U]:
    def inner(item: Tuple[_V, _T]) -> Tuple[_V, _U]:
        key, value = item
        return key, func(value)

    return inner


def map_items_helper(
    func: Callable[[_T, _U], Tuple[_V, _W]],
) -> Callable[[Tuple[_T, _U]], _V]:
    def inner(item: Tuple[_T, _U]) -> Tuple[_V, _W]:
        key, value = item
        return func(key, value)

    return inner


def last_helper(_: Any, second: _T) -> _T:  # noqa: U101
    return second


# sentinel


class Sentinel:
    def __repr__(self) -> str:
        return "<sentinel>"

    __str__ = __repr__


sentinel = Sentinel()


def drop_sentinel(*args: Any, **kwargs: Any) -> Tuple[Tuple, Dict[str, Any]]:
    return (
        tuple(x for x in args if x is not sentinel),
        {k: v for k, v in kwargs.items() if v is not sentinel},
    )


# version


class Version(Enum):
    py36 = auto()
    py37 = auto()
    py38 = auto()


def _get_version() -> Version:
    major, minor, *_ = version_info
    if major != 3:  # pragma: no cover
        raise RuntimeError(f"Expected Python 3; got {major}")
    mapping = {6: Version.py36, 7: Version.py37, 8: Version.py38}
    try:
        return mapping[minor]
    except KeyError:  # pragma: no cover
        raise UnsupportVersionError(
            f"Expected Python 3.6-3.8; got 3.{minor}",
        ) from None


VERSION = _get_version()
