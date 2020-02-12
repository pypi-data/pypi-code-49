from typing import List, Iterable

from ...schema import any_of
from ._OfProperty import OfProperty
from ._Property import Property


class AnyOfProperty(OfProperty):
    """
    Property which validates JSON that matches at least one of
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
            any_of,
            optional=optional
        )

    def choose_subproperty(self, successes: List[bool]) -> int:
        # Search the list
        for i, success in enumerate(successes):
            # Return the first valid index found
            if success:
                return i

        raise ValueError(f"Value didn't match any sub-properties")
