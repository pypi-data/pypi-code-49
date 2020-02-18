from re import search
from typing import FrozenSet

from hypothesis import given
from hypothesis import infer

from functional_itertools import CFrozenSet


@given(x=infer)
def test_repr(x: FrozenSet[int]) -> None:
    y = repr(CFrozenSet(x))
    if x:
        assert search(r"^CFrozenSet\(\{[\d\s\-,]*\}\)$", y)
    else:
        assert y == "CFrozenSet()"


@given(x=infer)
def test_str(x: FrozenSet[int]) -> None:
    y = str(CFrozenSet(x))
    if x:
        assert search(r"^CFrozenSet\(\{[\d\s\-,]*\}\)$", y)
    else:
        assert y == "CFrozenSet()"
