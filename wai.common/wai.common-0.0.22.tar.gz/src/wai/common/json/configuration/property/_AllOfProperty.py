from typing import List, Iterable

from ...schema import all_of
from ._OfProperty import OfProperty
from ._Property import Property


class AllOfProperty(OfProperty):
    """
    Property which validates JSON that matches all of
    a number of sub-properties.
    """
    def __init__(self,
                 name: str = "",
                 sub_properties: Iterable[Property] = tuple(),
                 *,
                 optional: bool = False):
        super().__init__(
            name,
            sub_properties,
            all_of,
            optional=optional
        )

    def choose_subproperty(self, successes: List[bool]) -> int:
        # If all sub-properties match, just pick the first one
        if all(successes):
            return 0

        raise ValueError(f"Value didn't match all sub-properties")
