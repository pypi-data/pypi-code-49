from typing import Callable
from typing import Dict
from typing import Tuple

from hypothesis import given
from hypothesis import infer

from functional_itertools import CDict
from functional_itertools import CFrozenSet
from functional_itertools import CIterable
from functional_itertools import CList
from functional_itertools import CSet
from tests.test_utilities import assert_is_instance_and_equal_to
from tests.test_utilities import int_and_int_to_bool_funcs
from tests.test_utilities import int_and_int_to_int_and_int_funcs
from tests.test_utilities import int_to_bool_funcs
from tests.test_utilities import int_to_int_funcs


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
def test_filter_keys(x: Dict[int, str], func: Callable[[int], bool]) -> None:
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


@given(x=infer)
def test_frozenset_keys(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).frozenset_keys(), CFrozenSet, frozenset(x.keys()),
    )


@given(x=infer)
def test_frozenset_values(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).frozenset_values(), CFrozenSet, frozenset(x.values()),
    )


@given(x=infer)
def test_frozenset_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).frozenset_items(), CFrozenSet, frozenset(x.items()),
    )


@given(x=infer)
def test_list_keys(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).list_keys(), CList, list(x.keys()),
    )


@given(x=infer)
def test_list_values(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).list_values(), CList, list(x.values()),
    )


@given(x=infer)
def test_list_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).list_items(), CList, list(x.items()),
    )


@given(x=infer, func=int_to_int_funcs)
def test_map_keys(x: Dict[int, str], func: Callable[[int], int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).map_keys(func), CDict, {func(k): v for k, v in x.items()},
    )


@given(x=infer, func=int_to_int_funcs)
def test_map_values(x: Dict[str, int], func: Callable[[int], int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).map_values(func), CDict, {k: func(v) for k, v in x.items()},
    )


@given(x=infer, func=int_and_int_to_int_and_int_funcs)
def test_map_items(
    x: Dict[int, int], func: Callable[[int, int], Tuple[int, int]],
) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).map_items(func), CDict, dict(func(k, v) for k, v in x.items()),
    )


@given(x=infer)
def test_set_keys(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).set_keys(), CSet, set(x.keys()),
    )


@given(x=infer)
def test_set_values(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).set_values(), CSet, set(x.values()),
    )


@given(x=infer)
def test_set_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CDict(x).set_items(), CSet, set(x.items()),
    )
