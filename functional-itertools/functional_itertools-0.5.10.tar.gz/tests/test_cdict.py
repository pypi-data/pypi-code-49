from typing import Callable
from typing import Dict

from hypothesis import given
from hypothesis import infer

from functional_itertools import CDict
from functional_itertools import CIterable
from tests.test_utilities import assert_is_instance_and_equal_to
from tests.test_utilities import int_and_int_to_bool_funcs
from tests.test_utilities import int_to_bool_funcs


@given(x=infer)
def test_keys(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).keys(), CIterable, list(x.keys()))


@given(x=infer)
def test_values(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).values(), CIterable, list(x.values()),
    )


@given(x=infer)
def test_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).items(), CIterable, list(x.items()),
    )


# built-in


@given(x=infer)
def test_all_keys(x: Dict[bool, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).all_keys(), bool, all(x.keys()))


@given(x=infer)
def test_all_values(x: Dict[str, bool]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).all_values(), bool, all(x.values()),
    )


@given(x=infer)
def test_all_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).all_items(), bool, all(x.items()))


@given(x=infer)
def test_any_keys(x: Dict[bool, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).any_keys(), bool, any(x.keys()))


@given(x=infer)
def test_any_values(x: Dict[str, bool]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).any_values(), bool, any(x.values()),
    )


@given(x=infer)
def test_any_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).any_items(), bool, any(x.items()))


@given(x=infer, func=int_to_bool_funcs)
def test_filter_keys(x: Dict[int, int], func: Callable[[int], bool]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).filter_keys(func),
        CDict,
        {k: v for k, v in x.items() if func(k)},
    )


@given(x=infer, func=int_to_bool_funcs)
def test_filter_values(x: Dict[str, int], func: Callable[[int], bool]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).filter_values(func),
        CDict,
        {k: v for k, v in x.items() if func(v)},
    )


@given(x=infer, func=int_and_int_to_bool_funcs)
def test_filter_items(
    x: Dict[int, int], func: Callable[[int, int], bool],
) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).filter_items(func),
        CDict,
        {k: v for k, v in x.items() if func(k, v)},
    )
