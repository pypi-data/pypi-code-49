from operator import add
from operator import mod
from operator import mul
from operator import sub
from typing import Any
from typing import Callable
from typing import Tuple
from typing import Type

from hypothesis import given
from hypothesis import infer
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import sampled_from
from hypothesis.strategies import tuples

from functional_itertools.utilities import sentinel


def assert_is_instance_and_equal_to(x: Any, cls: Type[Any], y: Any) -> None:
    assert isinstance(x, cls)
    assert x == y


def test_sentinel() -> None:
    assert repr(sentinel) == "<sentinel>"


int_to_bool_funcs = (
    integers(min_value=1)
    .flatmap(lambda x: tuples(just(x), integers(0, x - 1)))
    .map(lambda mod_rem: (lambda x: mod(x, mod_rem[0]) == mod_rem[1]))
)


@given(func=int_to_bool_funcs, x=infer)
def test_int_to_bool_funcs(func: Callable[[int], bool], x: int) -> None:
    assert isinstance(func(x), bool)


int_and_int_to_bool_funcs = int_to_bool_funcs.map(
    lambda f: (lambda x, y: f(x) and f(y)),
)


@given(func=int_and_int_to_bool_funcs, x=infer, y=infer)
def test_int_and_int_to_bool_funcs(
    func: Callable[[int, int], bool], x: int, y: int,
) -> None:
    assert isinstance(func(x, y), bool)


int_and_int_to_int_funcs = sampled_from([add, sub, mul])


@given(func=int_and_int_to_int_funcs, x=infer, y=infer)
def test_int_and_int_to_int_funcs(
    func: Callable[[int, int], int], x: int, y: int,
) -> None:
    assert isinstance(func(x, y), int)


int_to_int_funcs = tuples(int_and_int_to_int_funcs, integers()).map(
    lambda op_n: (lambda x: op_n[0](op_n[1], x)),
)


@given(func=int_to_int_funcs, x=infer)
def test_int_to_int_funcs(func: Callable[[int], int], x: int) -> None:
    assert isinstance(func(x), int)


int_and_int_to_int_and_int_funcs = tuples(
    int_to_int_funcs, int_to_int_funcs,
).map(lambda f_g: (lambda x, y: (f_g[0](x), f_g[1](x))))


@given(func=int_and_int_to_int_and_int_funcs, x=infer, y=infer)
def test_int_and_int_to_int_and_int_funcs(
    func: Callable[[int, int], Tuple[int, int]], x: int, y: int,
) -> None:
    z = func(x, y)
    assert isinstance(z, tuple)
    a, b = z
    assert isinstance(a, int)
    assert isinstance(b, int)
