#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Test for typing utils
"""
from typing import List, Union, Callable

import pytest

from hvl_ccb.utils.typing import (
    is_type_hint,
    is_generic,
    check_generic_type,
)


def test_is_generic():

    for type_ in (1, "a", (), int, str, object):
        assert not is_type_hint(type_)
        assert not is_generic(type_)

    for type_ in (List[int], List, Union[None, List[int]], Union, Callable):
        assert is_type_hint(type_)

    for type_ in (List, List[int], Union[None, List[int]]):
        assert is_generic(type_)

    for type_ in (Union, Callable):
        assert not is_generic(type_)


def test_check_generic_type():

    with pytest.raises(ValueError):
        check_generic_type([], list)

    assert check_generic_type([], List) is None

    with pytest.raises(TypeError):
        check_generic_type(['a'], List[int])

    assert check_generic_type([1, 2], List[int]) is None

    with pytest.raises(TypeError):
        check_generic_type([1, 1.0], List[int])

    assert check_generic_type([1, 1.0], List[Union[int, float]]) is None
    assert check_generic_type(None, Union[None, List[int]]) is None
    assert check_generic_type([1, 2], Union[None, List[int]]) is None
