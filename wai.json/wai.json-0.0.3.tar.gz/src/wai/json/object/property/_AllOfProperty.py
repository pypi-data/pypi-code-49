from typing import List, Iterable, Optional

from ...error import OfPropertySelectionError
from ...schema import all_of
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._OfProperty import OfProperty
from ._Property import Property


class AllOfProperty(OfProperty):
    """
    Property which validates JSON that matches all of
    a number of sub-properties.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 sub_properties: Iterable[Property] = tuple(),
                 *,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        super().__init__(
            name,
            sub_properties,
            schema_function=all_of,
            optional=optional,
            default=default
        )

    @classmethod
    def _choose_subproperty(cls, successes: List[bool]) -> int:
        # If all sub-properties match, just pick the first one
        if all(successes):
            return 0

        raise OfPropertySelectionError(f"Value didn't match all sub-properties")
