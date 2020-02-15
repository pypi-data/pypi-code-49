from functools import reduce
from itertools import count
from itertools import cycle
from itertools import islice
from itertools import repeat
from re import escape
from sys import maxsize
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import Union

from hypothesis import assume
from hypothesis import given
from hypothesis import infer
from hypothesis.strategies import DataObject
from hypothesis.strategies import fixed_dictionaries
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import none
from hypothesis.strategies import sampled_from
from hypothesis.strategies import tuples
from more_itertools import chunked
from pytest import mark
from pytest import raises

from functional_itertools import CDict
from functional_itertools import CFrozenSet
from functional_itertools import CIterable
from functional_itertools import CList
from functional_itertools import CSet
from functional_itertools import EmptyIterableError
from functional_itertools import MultipleElementsError
from functional_itertools.errors import UnsupportVersionError
from functional_itertools.utilities import drop_sentinel
from functional_itertools.utilities import Sentinel
from functional_itertools.utilities import sentinel
from functional_itertools.utilities import VERSION
from functional_itertools.utilities import Version
from tests.test_utilities import assert_is_instance_and_equal_to
from tests.test_utilities import int_and_int_to_int_funcs
from tests.test_utilities import int_to_bool_funcs
from tests.test_utilities import int_to_int_funcs


@given(x=infer)
def test_init(x: Union[int, List[int]]) -> None:
    if isinstance(x, int):
        with raises(
            TypeError,
            match="CIterable expected an iterable, "
            "but 'int' object is not iterable",
        ):
            CIterable(x)  # type: ignore
    else:
        assert isinstance(CIterable(iter(x)), CIterable)


@given(x=infer, y=infer)
def test_eq(x: List[int], y: Union[int, List[int]]) -> None:
    assert_is_instance_and_equal_to(
        CIterable(x) == y, bool, x == y,
    )


@given(x=infer, index=infer)
def test_get_item(x: List[int], index: int) -> None:
    y = CIterable(x)
    num_ints = len(x)
    if index < 0:
        with raises(
            IndexError, match=f"Expected a non-negative index; got {index}",
        ):
            y[index]
    elif 0 <= index < num_ints:
        assert_is_instance_and_equal_to(y[index], x[index])
    elif num_ints <= index <= maxsize:
        with raises(IndexError, match="CIterable index out of range"):
            y[index]
    else:
        with raises(
            IndexError,
            match=f"Expected an index at most {maxsize}; got {index}",
        ):
            y[index]


@given(x=infer)
def test_iter(x: List[int]) -> None:
    assert CIterable(x) == x


# repr and str


@given(x=infer)
def test_repr(x: Iterable[int]) -> None:
    assert repr(CIterable(x)) == f"CIterable({x!r})"


@given(x=infer)
def test_str(x: Iterable[int]) -> None:
    assert str(CIterable(x)) == f"CIterable({x})"


# built-ins


classes = sampled_from([CIterable, CList, CFrozenSet, CSet])


@given(cls=classes, x=infer)
def test_all(cls: Type, x: Set[bool]) -> None:
    assert_is_instance_and_equal_to(cls(x).all(), bool, all(x))


@given(cls=classes, x=infer)
def test_any(cls: Type, x: Set[bool]) -> None:
    assert_is_instance_and_equal_to(cls(x).any(), bool, any(x))


@given(x=infer)
def test_dict(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CIterable(x).dict(), CDict, x,
    )


@given(x=infer, start=infer)
def test_enumerate(x: List[int], start: int) -> None:
    assert_is_instance_and_equal_to(
        CIterable(x).enumerate(start=start),
        CIterable,
        enumerate(x, start=start),
    )


@given(
    cls=sampled_from([CIterable, CList, CSet, CFrozenSet]),
    x=infer,
    func=int_to_bool_funcs,
)
def test_filter(cls: Type, x: List[int], func: Callable[[int], bool]) -> None:
    y = cls(x).filter(func)
    assert isinstance(y, cls)
    if cls in {CIterable, CList}:
        assert y == list(filter(func, x))
    else:
        assert set(y) == set(filter(func, x))


@given(cls=sampled_from([CIterable, CList, CSet]), x=infer)
def test_frozenset(cls: Type, x: Set[int]) -> None:
    assert_is_instance_and_equal_to(cls(x).frozenset(), CFrozenSet, x)


@given(cls=sampled_from([CIterable, CSet, CFrozenSet]), x=infer)
def test_list(cls: Type, x: List[int]) -> None:
    y = cls(x).list()
    assert isinstance(y, CList)
    if cls is CIterable:
        assert y == x
    else:
        assert set(y) == set(x)


@given(cls=sampled_from([CIterable, CList]), x=infer, func=int_to_bool_funcs)
def test_map(cls: Type, x: List[int], func: Callable[[int], bool]) -> None:
    assert_is_instance_and_equal_to(
        cls(x).map(func), cls, list(map(func, x)),
    )


@given(
    data=infer,
    x=infer,
    default_kwargs=just({}) | fixed_dictionaries({"default": integers()}),
)
@mark.parametrize("func", [max, min])
def test_max_and_min(
    data: DataObject,
    x: List[int],
    func: Callable[..., int],
    default_kwargs: Dict[str, int],
) -> None:
    method = getattr(CIterable(iter(x)), func.__name__)
    key_kwargs_strategies = just({}) | fixed_dictionaries(
        {"key": int_to_int_funcs},
    )
    if VERSION in {Version.py36, Version.py37}:
        key_kwargs = data.draw(key_kwargs_strategies)
    elif VERSION is Version.py38:
        key_kwargs = data.draw(key_kwargs_strategies | just({"key": None}))
    else:
        raise UnsupportVersionError(VERSION)
    try:
        res = method(**key_kwargs, **default_kwargs)
    except ValueError:
        with raises(
            ValueError,
            match=escape(f"{func.__name__}() arg is an empty sequence"),
        ):
            func(x, **key_kwargs, **default_kwargs)
    else:
        assert_is_instance_and_equal_to(
            res, int, func(x, **key_kwargs, **default_kwargs),
        )


@given(start=infer, stop=infer, step=infer, n=integers(0, 1000))
def test_range(
    start: int, stop: Union[int, Sentinel], step: Union[int, Sentinel], n: int,
) -> None:
    if step is sentinel:
        assume(stop is not sentinel)
    else:
        assume(step != 0)
    args, _ = drop_sentinel(stop, step)
    x = CIterable.range(start, *args)
    assert isinstance(x, CIterable)
    assert x[:n] == islice(range(start, *args), n)


@given(x=infer)
def test_set(x: Set[int]) -> None:
    y = CIterable(x).set()
    assert isinstance(y, CSet)
    assert y == x


@given(x=infer, key=none() | int_to_int_funcs, reverse=infer)
def test_sorted(
    x: List[int], key: Optional[Callable[[int], int]], reverse: bool,
) -> None:
    y = CIterable(x).sorted(key=key, reverse=reverse)
    assert isinstance(y, CList)
    assert y == sorted(x, key=key, reverse=reverse)


@given(x=infer, args=just(()) | tuples(integers()))
def test_sum(x: List[int], args: Tuple[int, ...]) -> None:
    y = CIterable(x).sum(*args)
    assert isinstance(y, int)
    assert y == sum(x, *args)


@given(x=infer)
def test_tuple(x: List[int]) -> None:
    y = CIterable(x).tuple()
    assert isinstance(y, tuple)
    assert y == tuple(x)


@given(x=infer, iterables=infer)
def test_zip(x: List[int], iterables: List[List[int]]) -> None:
    y = CIterable(x).zip(*iterables)
    assert isinstance(y, CIterable)
    assert y == zip(x, *iterables)


# public


@given(x=infer)
@mark.parametrize("method_name, index", [("first", 0), ("last", -1)])
def test_first_and_last(x: List[int], method_name: str, index: int) -> None:
    method = getattr(CIterable(x), method_name)
    if x:
        assert method() == x[index]
    else:
        with raises(EmptyIterableError):
            method()


@given(x=infer)
def test_one(x: List[int]) -> None:
    num_ints = len(x)
    if num_ints == 0:
        with raises(EmptyIterableError):
            CIterable(x).one()
    elif num_ints == 1:
        assert CIterable(x).one() == x[0]
    else:
        with raises(MultipleElementsError, match=f"{x[0]}, {x[1]}"):
            CIterable(x).one()


@given(x=infer, n=integers(0, maxsize))
def test_pipe(x: List[int], n: int) -> None:
    y = CIterable(x).pipe(chunked, n)
    assert isinstance(y, CIterable)
    assert y == chunked(x, n)


# functools


@given(
    x=infer,
    func=int_and_int_to_int_funcs,
    initial_args=just(()) | tuples(integers()),
)
def test_reduce(
    x: List[int],
    func: Callable[[int, int], int],
    initial_args: Tuple[int, ...],
) -> None:
    try:
        res = CIterable(x).reduce(func, *initial_args)
    except EmptyIterableError:
        with raises(
            TypeError,
            match=escape(f"reduce() of empty sequence with no initial value"),
        ):
            reduce(func, x, *initial_args)
    else:
        assert_is_instance_and_equal_to(
            res, int, reduce(func, x, *initial_args),
        )


# itertools


@given(
    start=infer, step=infer, n=integers(0, 1000),
)
def test_count(start: int, step: int, n: int) -> None:
    x = CIterable.count(start=start, step=step)
    assert isinstance(x, CIterable)
    assert x[:n] == islice(count(start=start, step=step), n)


@given(x=infer, n=integers(0, 1000))
def test_cycle(x: List[int], n: int) -> None:
    y = CIterable(x).cycle()
    assert isinstance(y, CIterable)
    assert y[:n] == islice(cycle(x), n)


@given(x=infer, times=infer, n=integers(0, 1000))
def test_repeat(x: int, times: int, n: int) -> None:
    try:
        y = CIterable.repeat(x, times=times)
    except OverflowError:
        assume(False)
    assert isinstance(y, CIterable)
    assert y[:n] == islice(repeat(x, times=times), n)
