from __future__ import annotations

from typing import (
    Any,
    Generator,
    Generic,
    List,
    Mapping,
    Optional,
    Sequence,
    TypeVar,
    Union,
    Callable,
)

from aerie.fields import Field
from aerie.utils import chunked

E = TypeVar("E")


def attribute_reader(obj, attr, default=None) -> Any:
    return getattr(obj, attr, default)


class Collection(Generic[E]):
    def __init__(self, items: Sequence[Any]):
        self.items = items
        self._position = 0

    def first(self) -> Optional[E]:
        try:
            return next(self)
        except StopIteration:
            return None

    def last(self) -> Optional[E]:
        ...

    def chunk(self, batch: int) -> Generator[E, None, None]:
        return chunked(self, batch)

    def pluck(self, key: Union[str, Field]) -> Collection[Any]:
        key = str(key)
        return Collection([attribute_reader(item, key, None) for item in self])

    def all(self) -> Sequence[E]:
        return self.items

    def avg(self, field: Union[str, Field]) -> float:
        ...

    def min(self, field: Union[str, Field]) -> float:
        ...

    def mean(self, field: Union[str, Field]) -> float:
        ...

    def max(self, field: Union[str, Field]) -> float:
        ...

    def sum(self, field: Union[str, Field]) -> float:
        ...

    def mode(self, field: Union[str, Field]) -> float:
        # https://en.wikipedia.org/wiki/Mode_(statistics)
        ...

    def map(self, fn: Callable[[E, int], Any]):
        return type(self)(map(fn, list(self)))

    def each(self, fn: Callable[[E, int], None]) -> None:
        ...

    def every(self, fn: Callable[[E, int], bool]) -> Collection[E]:
        ...

    def pop(self) -> E:
        ...

    def prepend(self, item: E) -> Collection[E]:
        ...

    def append(self, item: E) -> Collection[E]:
        ...

    def except_(self, fn: Callable[[E, int], bool]) -> Collection[E]:
        ...

    def filter(self, fn: Callable[[E, int], bool]) -> Collection[E]:
        ...

    def reduce(self, fn: Callable[[E, int], bool]) -> Collection[E]:
        ...

    def sort(self) -> Collection[E]:
        ...

    def sort_by(self, key, dir="asc") -> Collection[E]:
        ...

    def group_by(self):
        ...

    def as_list(self) -> List[E]:
        return list(self)

    def __getitem__(self, index: Union[int, slice]) -> E:
        if isinstance(index, slice):
            return [
                self._process_item(item)
                for item in self.items[index.start : index.stop : index.step]
            ]
        return self._process_item(self.items[index])

    def __setitem__(self, key, value):
        raise NotImplementedError()

    def __delitem__(self, key):
        raise NotImplementedError()

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Collection[E]:
        return self

    def __next__(self) -> E:
        if self._position < len(self):
            entity = self._process_item(self.items[self._position])
            self._position += 1
            return entity
        raise StopIteration()

    def __contains__(self, item: E) -> bool:
        return item in self.items

    def __str__(self) -> str:
        truncate = 10
        remainder = 0
        if len(self) > truncate:
            remainder = len(self) - truncate

        contents = ",".join(map(str, self[0:10]))
        suffix = ""
        if remainder:
            suffix = f" and {remainder} items more"

        return f"[{contents}{suffix}]"

    def _process_item(self, item: Mapping) -> E:
        return item
