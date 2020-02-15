from functools import reduce
from itertools import accumulate
from itertools import chain
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import compress
from itertools import count
from itertools import cycle
from itertools import dropwhile
from itertools import filterfalse
from itertools import groupby
from itertools import islice
from itertools import permutations
from itertools import product
from itertools import repeat
from itertools import starmap
from itertools import tee
from itertools import zip_longest
from operator import add
from sys import maxsize
from typing import Any
from typing import Callable
from typing import Dict
from typing import FrozenSet
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from more_itertools.recipes import all_equal
from more_itertools.recipes import consume
from more_itertools.recipes import dotproduct
from more_itertools.recipes import first_true
from more_itertools.recipes import flatten
from more_itertools.recipes import grouper
from more_itertools.recipes import iter_except
from more_itertools.recipes import ncycles
from more_itertools.recipes import nth
from more_itertools.recipes import nth_combination
from more_itertools.recipes import padnone
from more_itertools.recipes import pairwise
from more_itertools.recipes import partition
from more_itertools.recipes import powerset
from more_itertools.recipes import prepend
from more_itertools.recipes import quantify
from more_itertools.recipes import random_combination
from more_itertools.recipes import random_combination_with_replacement
from more_itertools.recipes import random_permutation
from more_itertools.recipes import random_product
from more_itertools.recipes import repeatfunc
from more_itertools.recipes import roundrobin
from more_itertools.recipes import tabulate
from more_itertools.recipes import tail
from more_itertools.recipes import take
from more_itertools.recipes import unique_everseen
from more_itertools.recipes import unique_justseen

from functional_itertools.compat import MAX_MIN_KEY_ANNOTATION
from functional_itertools.compat import MAX_MIN_KEY_DEFAULT
from functional_itertools.errors import EmptyIterableError
from functional_itertools.errors import MultipleElementsError
from functional_itertools.errors import UnsupportVersionError
from functional_itertools.utilities import drop_sentinel
from functional_itertools.utilities import last_helper
from functional_itertools.utilities import Sentinel
from functional_itertools.utilities import sentinel
from functional_itertools.utilities import VERSION
from functional_itertools.utilities import Version


_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")
_W = TypeVar("_W")

_GroupByTU = Tuple[_U, Iterator[_T]]


if VERSION in {Version.py36, Version.py37}:

    def _accumulate(
        self: "CIterable[_T]", func: Callable[[_T, _T], _T] = add,
    ) -> "CIterable[_T]":
        return CIterable(accumulate(self._iterable, func))


elif VERSION is Version.py38:

    def _accumulate(  # type: ignore
        self: "CIterable[_T]",
        func: Callable[[_T, _T], _T] = add,
        initial: Optional[_T] = None,
    ) -> "CIterable[_T]":
        return CIterable(accumulate(self._iterable, func, initial=initial))


else:
    raise UnsupportVersionError(VERSION)  # pragma: no cover


class CIterable(Iterable[_T]):
    __slots__ = ("_iterable",)

    def __init__(self, iterable: Iterable[_T]) -> None:
        try:
            iter(iterable)
        except TypeError as error:
            (msg,) = error.args
            raise TypeError(
                f"{type(self).__name__} expected an iterable, but {msg}",
            )
        else:
            self._iterable = iterable

    def __eq__(self, other: Any) -> bool:
        try:
            iter(other)
        except TypeError:
            return False
        else:
            return self.list() == list(other)

    @overload  # noqa: U100
    def __getitem__(self, item: int) -> _T:
        ...

    @overload  # noqa: F811,U100
    def __getitem__(self, item: slice) -> "CIterable[_T]":
        ...

    def __getitem__(  # noqa: F811
        self, item: Union[int, slice],
    ) -> Union[_T, "CIterable[_T]"]:
        if isinstance(item, int):
            if item < 0:
                raise IndexError(f"Expected a non-negative index; got {item}")
            elif item > maxsize:
                raise IndexError(
                    f"Expected an index at most {maxsize}; got {item}",
                )
            else:
                slice_ = islice(self._iterable, item, item + 1)
                try:
                    return next(slice_)
                except StopIteration:
                    raise IndexError(
                        f"{type(self).__name__} index out of range",
                    )
        elif isinstance(item, slice):
            return self.islice(item.start, item.stop, item.step)
        else:
            raise TypeError(
                f"Expected an int or slice; got a(n) {type(item).__name__}",
            )

    def __iter__(self) -> Iterator[_T]:
        yield from self._iterable

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._iterable!r})"

    def __str__(self) -> str:
        return f"{type(self).__name__}({self._iterable})"

    # built-in

    def all(self) -> bool:
        return all(self._iterable)

    def any(self) -> bool:
        return any(self._iterable)

    def dict(self: "CIterable[Tuple[_T,_U]]") -> "CDict[_T, _U]":
        return CDict(dict(self._iterable))

    def enumerate(self, start: int = 0) -> "CIterable[Tuple[int, _T]]":
        return CIterable(enumerate(self._iterable, start=start))

    def filter(self, func: Optional[Callable[[_T], bool]]) -> "CIterable[_T]":
        return CIterable(filter(func, self._iterable))

    def frozenset(self) -> "CFrozenSet[_T]":
        return CFrozenSet(self._iterable)

    def list(self) -> "CList[_T]":
        return CList(self._iterable)

    def map(
        self, func: Callable[..., _U], *iterables: Iterable,
    ) -> "CIterable[_U]":
        return CIterable(map(func, self._iterable, *iterables))

    def max(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self._iterable, **kwargs)

    def min(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return min(self._iterable, **kwargs)

    @classmethod
    def range(
        cls: Type["CIterable"],
        start: int,
        stop: Union[int, Sentinel] = sentinel,
        step: Union[int, Sentinel] = sentinel,
    ) -> "CIterable[int]":
        args, _ = drop_sentinel(stop, step)
        return cls(range(start, *args))

    def set(self) -> "CSet[_T]":
        return CSet(self._iterable)

    def sorted(
        self,
        *,
        key: Optional[Callable[[_T], Any]] = None,
        reverse: bool = False,
    ) -> "CList[_T]":
        return CList(sorted(self._iterable, key=key, reverse=reverse))

    def sum(self, start: Union[_T, int] = 0) -> Union[_T, int]:
        args, _ = drop_sentinel(start)
        return sum(self._iterable, *args)

    def tuple(self) -> Tuple[_T, ...]:
        return tuple(self._iterable)

    def zip(self, *iterables: Iterable) -> "CIterable[Tuple]":
        return CIterable(zip(self._iterable, *iterables))

    # extra public methods

    def first(self) -> _T:
        try:
            return next(iter(self._iterable))
        except StopIteration:
            raise EmptyIterableError from None

    def last(self) -> _T:
        return self.reduce(last_helper)

    def one(self) -> _T:
        head: CList[_T] = self.islice(2).list()
        if head:
            try:
                (x,) = head
            except ValueError:
                x, y = head
                raise MultipleElementsError(f"{x}, {y}")
            else:
                return x
        else:
            raise EmptyIterableError

    def pipe(
        self,
        func: Callable[..., Iterable[_U]],
        *args: Any,
        index: int = 0,
        **kwargs: Any,
    ) -> "CIterable[_U]":
        new_args = chain(
            islice(args, index), [self._iterable], islice(args, index, None),
        )
        return CIterable(func(*new_args, **kwargs))

    # functools

    def reduce(
        self,
        func: Callable[[_T, _T], _T],
        initial: Union[_U, Sentinel] = sentinel,
    ) -> Any:
        args, _ = drop_sentinel(initial)
        try:
            return reduce(func, self._iterable, *args)
        except TypeError as error:
            (msg,) = error.args
            if msg == "reduce() of empty sequence with no initial value":
                raise EmptyIterableError from None
            else:
                raise error

    def reduce_as_iterable(
        self,
        func: Callable[[_T, _T], _T],
        initial: Union[_U, Sentinel] = sentinel,
    ) -> "CIterable[_T]":
        return CIterable(self.reduce(func, initial=initial))

    # itertools

    @classmethod
    def count(
        cls: Type["CIterable"], start: int = 0, step: int = 1,
    ) -> "CIterable[int]":
        return cls(count(start=start, step=step))

    def cycle(self) -> "CIterable[_T]":
        return CIterable(cycle(self._iterable))

    @classmethod
    def repeat(
        cls: Type["CIterable[_T]"], x: _T, times: int,
    ) -> "CIterable[_T]":
        return cls(repeat(x, times=times))

    accumulate = _accumulate

    def chain(self, *iterables: Iterable[_U]) -> "CIterable[Union[_T,_U]]":
        return self.pipe(chain, *iterables, index=0)

    def compress(self, selectors: Iterable) -> "CIterable[_T]":
        return self.pipe(compress, selectors, index=0)

    def dropwhile(self, func: Callable[[_T], bool]) -> "CIterable[Tuple[_T]]":
        return self.pipe(dropwhile, func, index=0)

    def filterfalse(
        self, func: Callable[[_T], bool],
    ) -> "CIterable[Tuple[_T]]":
        return self.pipe(filterfalse, func, index=0)

    def groupby(
        self, key: Optional[Callable[[_T], _U]] = None,
    ) -> "CIterable[_GroupByTU]":
        return self.pipe(groupby, key=key, index=0)

    def islice(
        self,
        start: int,
        stop: Union[int, Sentinel] = sentinel,
        step: Union[int, Sentinel] = sentinel,
    ) -> "CIterable[_T]":
        args, _ = drop_sentinel(stop, step)
        return self.pipe(islice, start, *args, index=0)

    def starmap(self, func: Callable[[Tuple], _U]) -> "CIterable[_U]":
        return self.pipe(starmap, func, index=1)

    def tee(self, n: int = 2) -> "CIterable[Iterator[_T]]":
        return self.pipe(tee, n=n, index=0)

    def zip_longest(
        self, *iterables: Iterable, fillvalue: Any = None,
    ) -> "CIterable[Iterable[Tuple]]":
        return self.pipe(zip_longest, *iterables, fillvalue=fillvalue, index=0)

    def product(
        self, *iterables: Iterable, repeat: int = 1,
    ) -> "CIterable[Tuple[_T, ...]]":
        return self.pipe(product, *iterables, repeat=repeat, index=0)

    def permutations(
        self, r: Optional[int] = None,
    ) -> "CIterable[Tuple[_T, ...]]":
        return self.pipe(permutations, r=r, index=0)

    def combinations(self, r: int) -> "CIterable[Tuple[_T, ...]]":
        return self.pipe(combinations, r, index=0)

    def combinations_with_replacement(
        self, r: int,
    ) -> "CIterable[Tuple[_T, ...]]":
        return self.pipe(combinations_with_replacement, r, index=0)

    # itertools-recipes

    def take(self, n: int) -> "CIterable[_T]":
        return self.pipe(take, n, index=1)

    def prepend(self, value: _T) -> "CIterable[_T]":
        return self.pipe(prepend, value, index=1)

    @classmethod
    def tabulate(
        cls: Type["CIterable"], func: Callable[[int], _T], start: int = 0,
    ) -> "CIterable[_T]":
        return cls(tabulate(func, start=start))

    def tail(self, n: int) -> "CIterable[_T]":
        return self.pipe(tail, n, index=1)

    def consume(self, n: Optional[int] = None) -> "CIterable[_T]":
        consume(self._iterable, n=n)
        return self

    def nth(
        self, n: int, default: Optional[_U] = None,
    ) -> Optional[Union[_T, _U]]:
        return nth(self._iterable, n, default=default)

    def all_equal(self) -> bool:
        return all_equal(self._iterable)

    def quantify(self, pred: Callable[[_T], bool] = bool) -> int:
        return quantify(self._iterable, pred=pred)

    def padnone(self) -> "CIterable[Optional[_T]]":
        return self.pipe(padnone, index=0)

    def ncycles(self, n: int) -> "CIterable[_T]":
        return self.pipe(ncycles, n, index=0)

    def dotproduct(
        self: "CIterable[object]", iterable: Iterable[object],
    ) -> object:
        return dotproduct(self._iterable, iterable)

    def flatten(self: "CIterable[Iterable[_T]]") -> "CIterable[_T]":
        return self.pipe(flatten, index=0)

    @classmethod
    def repeatfunc(
        cls: Type["CIterable"],
        func: Callable[..., _T],
        times: Optional[int] = None,
        *args: Any,
    ) -> "CIterable[_T]":
        return cls(repeatfunc(func, times=times, *args))  # type: ignore

    def pairwise(self) -> "CIterable[Tuple[_T,_T]]":
        return self.pipe(pairwise, index=0)

    def grouper(
        self, n: int, fillvalue: Optional[_T] = None,
    ) -> "CIterable[Tuple[_T,...]]":
        return self.pipe(grouper, n, fillvalue=fillvalue, index=0)

    def partition(
        self, func: Callable[[_T], bool],
    ) -> Tuple["CIterable[_T]", ...]:
        return self.pipe(partition, func, index=1).map(type(self)).tuple()

    def powerset(self) -> "CIterable[Tuple[_T,...]]":
        return self.pipe(powerset, index=0)

    def roundrobin(self, *iterables: Iterable[_T]) -> "CIterable[_T]":
        return self.pipe(roundrobin, *iterables, index=0)

    def unique_everseen(
        self, key: Optional[Callable[[_T], Any]] = None,
    ) -> "CIterable[_T]":
        return self.pipe(unique_everseen, key=key, index=0)

    def unique_justseen(
        self, key: Optional[Callable[[_T], Any]] = None,
    ) -> "CIterable[_T]":
        return self.pipe(unique_justseen, key=key, index=0)

    @classmethod
    def iter_except(
        cls: Type["CIterable"],
        func: Callable[..., _T],
        exception: Type[Exception],
        first: Optional[Callable[..., _U]] = None,
    ) -> "CIterable[Union[_T,_U]]":
        return cls(iter_except(func, exception, first=first))

    def first_true(
        self,
        default: bool = False,
        pred: Optional[Callable[[_T], object]] = None,
    ) -> Union[_T, bool]:
        return first_true(self._iterable, default=default, pred=pred)

    def random_product(
        self, *iterables: Iterable, repeat: int = 1,
    ) -> Tuple[_T, ...]:
        return random_product(self._iterable, *iterables, repeat=repeat)

    def random_permutation(self, r: Optional[int] = None) -> Tuple[_T, ...]:
        return random_permutation(self._iterable, r=r)

    def random_combination(self, r: int) -> Tuple[_T, ...]:
        return random_combination(self._iterable, r)

    def random_combination_with_replacement(self, r: int) -> Tuple[_T, ...]:
        return random_combination_with_replacement(self._iterable, r)

    def nth_combination(self, r: int, index: int) -> Tuple[_T, ...]:
        return nth_combination(self._iterable, r, index)


class CList(List[_T]):
    """A list with chainable methods."""

    def __repr__(self) -> str:
        return f"{type(self).__name__}({super().__repr__()})"

    def __str__(self) -> str:
        return f"{type(self).__name__}({super().__str__()})"

    # built-in

    def all(self) -> bool:
        return all(self)

    def any(self) -> bool:
        return any(self)

    def dict(self: "CList[Tuple[_T,_U]]") -> "CDict[_T, _U]":
        return CDict(dict(self))

    def enumerate(self, start: int = 0) -> "CList[Tuple[int, _T]]":
        return CList(enumerate(self, start=start))

    def filter(self, func: Optional[Callable[[_T], bool]]) -> "CList[_T]":
        return CList(filter(func, self))

    def frozenset(self) -> "CFrozenSet[_T]":
        return CFrozenSet(self)

    def iter(self) -> "CIterable[_T]":
        return CIterable(self)

    def map(
        self, func: Callable[..., _U], *iterables: Iterable,
    ) -> "CList[_U]":
        return CList(map(func, self, *iterables))

    def max(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self, **kwargs)

    def min(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return min(self, **kwargs)

    def reversed(self) -> "CList[_T]":
        return CList(reversed(self))

    def sort(
        self,
        *,
        key: Optional[Callable[[_T], Any]] = None,
        reverse: bool = False,
    ) -> "CList[_T]":
        super().sort(key=key, reverse=reverse)
        return self


class CSet(Set[_T]):
    """A set with chainable methods."""

    def __repr__(self) -> str:
        return f"{type(self)}({super().__repr__()})"

    def __str__(self) -> str:
        return f"{type(self)}({super().__str__()})"

    # set & frozenset methods

    def all(self) -> bool:
        return all(self)

    def any(self) -> bool:
        return any(self)

    def filter(self, func: Optional[Callable[[_T], bool]]) -> "CSet[_T]":
        return CSet(filter(func, self))

    def frozenset(self) -> "CFrozenSet[_T]":
        return CFrozenSet(self)

    def list(self) -> "CList[_T]":
        return CList(self)

    def union(self, *others: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().union(*others))

    def intersection(self, *others: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().intersection(*others))

    def difference(self, *others: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().difference(*others))

    def symmetric_difference(self, other: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().symmetric_difference(other))

    def copy(self) -> "CSet[_T]":
        return type(self)(super().copy())

    # set methods

    def update(self) -> NoReturn:
        raise RuntimeError("Use the 'union' method instead of 'update'")

    def intersection_update(self) -> NoReturn:
        raise RuntimeError(
            "Use the 'intersection' method instead of 'intersection_update'",
        )

    def difference_update(self) -> NoReturn:
        raise RuntimeError(
            "Use the 'difference' method instead of 'difference_update'",
        )

    def symmetric_difference_update(self) -> NoReturn:
        raise RuntimeError(
            "Use the 'symmetric_difference' method instead of "
            "'symmetric_difference_update'",
        )

    def add(self, element: _T) -> "CSet[_T]":
        super().add(element)
        return self

    def remove(self, element: _T) -> "CSet[_T]":
        super().remove(element)
        return self

    def discard(self, element: _T) -> "CSet[_T]":
        super().discard(element)
        return self

    def pop(self) -> "CSet[_T]":
        super().pop()
        return self

    def clear(self) -> "CSet[_T]":
        super().clear()
        return self


class CFrozenSet(FrozenSet[_T]):
    """A frozenset with chainable methods."""

    def __repr__(self) -> str:
        return f"{type(self)}({super().__repr__()})"

    def __str__(self) -> str:
        return f"{type(self)}({super().__str__()})"

    # built-in

    def all(self) -> bool:
        return all(self)

    def any(self) -> bool:
        return any(self)

    def filter(self, func: Optional[Callable[[_T], bool]]) -> "CFrozenSet[_T]":
        return CFrozenSet(filter(func, self))

    def list(self) -> "CList[_T]":
        return CList(self)

    # set & frozenset methods

    def union(self, *others: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().union(*others))

    def intersection(self, *others: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().intersection(*others))

    def difference(self, *others: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().difference(*others))

    def symmetric_difference(self, other: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().symmetric_difference(other))

    def copy(self) -> "CFrozenSet[_T]":
        return type(self)(super().copy())


class CDict(Mapping[_T, _U]):
    """A mapping with chainable methods."""

    __slots__ = ("_mapping",)

    def __init__(self, mapping: Mapping[_T, _U]) -> None:
        if isinstance(mapping, Mapping):
            self._mapping = mapping
        else:
            raise TypeError(
                f"{type(self).__name__} expected a mapping, "
                f"but {type(mapping).__name__} is not a mapping",
            )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Mapping):
            return self._mapping == other
        else:
            return False

    def __getitem__(self, item: _T) -> _U:
        return self._mapping[item]

    def __iter__(self) -> Iterator[_T]:
        yield from self._mapping

    def __len__(self) -> int:
        return len(self._mapping)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._mapping!r})"

    def __str__(self) -> str:
        return f"{type(self).__name__}({self._mapping})"

    def keys(self) -> CList[_T]:
        return CList(super().keys())

    def values(self) -> CList[_U]:
        return CList(super().values())

    def items(self) -> CList[Tuple[_T, _U]]:
        return CList(super().items())

    # built-in

    def all_keys(self) -> bool:
        return all(self._mapping.keys())

    def all_values(self) -> bool:
        return all(self._mapping.values())

    def any_keys(self) -> bool:
        return any(self._mapping.keys())

    def any_values(self) -> bool:
        return any(self._mapping.values())

    def dict(self) -> Dict[_T, _U]:
        return dict(self._mapping)

    def filter_keys(self, func: Callable[[_T], bool]) -> "CDict[_T, _U]":
        return self._new(
            {key: value for key, value in self._mapping.items() if func(key)},
        )

    def filter_values(self, func: Callable[[_U], bool]) -> "CDict[_T, _U]":
        return self._new(
            {key: value for key, value in self._mapping.items() if func(value)},
        )

    def filter_items(self, func: Callable[[_T, _U], bool]) -> "CDict[_T, _U]":
        return self._new(
            {
                key: value
                for key, value in self._mapping.items()
                if func(key, value)
            },
        )

    def frozenset_keys(self) -> FrozenSet[_T]:
        return frozenset(self.keys())

    def frozenset_values(self) -> FrozenSet[_U]:
        return frozenset(self.values())

    def frozenset_items(self) -> FrozenSet[Tuple[_T, _U]]:
        return frozenset(self.items())

    def list_keys(self) -> List[_T]:
        return list(self.keys())

    def list_values(self) -> List[_U]:
        return list(self.values())

    def list_items(self) -> List[Tuple[_T, _U]]:
        return list(self.items())

    def map_keys(self, func: Callable[[_T], _V]) -> "CDict[_V, _U]":
        return self._new(
            {func(key): value for key, value in self._mapping.items()},
        )

    def map_values(self, func: Callable[[_U], _V]) -> "CDict[_T, _V]":
        return self._new(
            {key: func(value) for key, value in self._mapping.items()},
        )

    def map_items(
        self, func: Callable[[_T, _U], Tuple[_V, _W]],
    ) -> "CDict[_V, _W]":
        out = {}
        for key, value in self._mapping.items():
            new_key, new_value = func(key, value)
            out[new_key] = new_value
        return self._new(out)

    def max_keys(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self.keys(), **kwargs)

    def max_values(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self.values(), **kwargs)

    def max_items(
        self,
        *,
        key: MAX_MIN_KEY_ANNOTATION = MAX_MIN_KEY_DEFAULT,
        default: Union[_T, Sentinel] = sentinel,
    ) -> _T:
        _, kwargs = drop_sentinel(key=key, default=default)
        return max(self.items(), **kwargs)

    def set_keys(self) -> Set[_T]:
        return set(self.keys())

    def set_values(self) -> Set[_U]:
        return set(self.values())

    def set_items(self) -> Set[Tuple[_T, _U]]:
        return set(self.items())

    # private

    @classmethod
    def _new(cls: Type["CDict"], mapping: Dict[_V, _W]) -> "CDict[_V, _W]":
        return cls(type(mapping)(mapping))
