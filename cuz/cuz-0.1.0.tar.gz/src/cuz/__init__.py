import typing as t

T = t.TypeVar("T")


def only(it: t.Iterable[T]) -> T:
    """Return the only member in an iterable."""
    [x] = it
    return x


__version__ = "0.1.0"
