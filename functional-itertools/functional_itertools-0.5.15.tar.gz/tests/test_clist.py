from typing import Callable
from typing import List
from typing import Optional

from hypothesis import given
from hypothesis import infer
from hypothesis.strategies import none

from functional_itertools.classes import CList
from tests.test_utilities import assert_is_instance_and_equal_to
from tests.test_utilities import int_to_int_funcs


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
