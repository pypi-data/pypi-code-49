from typing import List, Iterable, Optional

from ...error import OfPropertySelectionError
from ...schema import any_of
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._OfProperty import OfProperty
from ._Property import Property


class AnyOfProperty(OfProperty):
    """
    Property which validates JSON that matches at least one of
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
            schema_function=any_of,
            optional=optional,
            default=default
        )

    @classmethod
    def _choose_subproperty(cls, successes: List[bool]) -> int:
        # Search the list
        for i, success in enumerate(successes):
            # Return the first valid index found
            if success:
                return i

        raise OfPropertySelectionError(f"Value didn't match any sub-properties")
