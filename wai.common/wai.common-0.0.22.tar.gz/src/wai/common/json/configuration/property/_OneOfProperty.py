from typing import List, Iterable

from ...schema import one_of
from ._OfProperty import OfProperty
from ._Property import Property


class OneOfProperty(OfProperty):
    """
    Property which validates JSON that matches exactly one of
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
            one_of,
            optional=optional
        )

    def choose_subproperty(self, successes: List[bool]) -> int:
        # Start with an invalid index
        index = -1

        # Search the list
        for i, success in enumerate(successes):
            if success:
                # If a previous success occurred, we have matched multiple sub-properties
                if index >= 0:
                    raise ValueError(f"Value matched more than one sub-property")

                index = i

        if index == -1:
            raise ValueError(f"Value didn't match any sub-properties")

        return index
