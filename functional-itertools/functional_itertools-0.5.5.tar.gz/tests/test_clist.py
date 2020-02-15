from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Set

from hypothesis import given
from hypothesis import infer
from hypothesis.strategies import none

from functional_itertools import CDict
from functional_itertools.classes import CList
from tests.test_utilities import assert_is_instance_and_equal_to
from tests.test_utilities import int_to_int_funcs


@given(x=infer)
def test_all(x: Set[bool]) -> None:
    assert_is_instance_and_equal_to(CList(x).all(), bool, all(x))


@given(x=infer)
def test_any(x: Set[bool]) -> None:
    assert_is_instance_and_equal_to(CList(x).any(), bool, any(x))


@given(x=infer)
def test_dict(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(
        CList(x.items()).dict(), CDict, x,
    )


@given(x=infer, start=infer)
def test_enumerate(x: List[int], start: int) -> None:
    assert_is_instance_and_equal_to(
        CList(x).enumerate(start=start), CList, list(enumerate(x, start=start)),
    )


@given(x=infer)
def test_reversed(x: List[int]) -> None:
    assert_is_instance_and_equal_to(
        CList(x).reversed(), CList, list(reversed(x)),
    )


@given(x=infer, key=none() | int_to_int_funcs, reverse=infer)
def test_sort(
    x: List[int], key: Optional[Callable[[int], int]], reverse: bool,
) -> None:
    assert_is_instance_and_equal_to(
        CList(x).sort(key=key, reverse=reverse),
        CList,
        sorted(x, key=key, reverse=reverse),
    )
