from typing import Dict

from hypothesis import given
from hypothesis import infer

from functional_itertools import CDict
from functional_itertools import CList
from tests.test_utilities import assert_is_instance_and_equal_to


@given(x=infer)
def test_keys(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).keys(), CList, list(x.keys()))


@given(x=infer)
def test_values(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).values(), CList, list(x.values()))


@given(x=infer)
def test_items(x: Dict[str, int]) -> None:
    assert_is_instance_and_equal_to(CDict(x).items(), CList, list(x.items()))
