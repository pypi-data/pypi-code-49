from typing import List, Iterable, Optional

from ...error import OfPropertySelectionError
from ...schema import one_of
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._OfProperty import OfProperty
from ._Property import Property


class OneOfProperty(OfProperty):
    """
    Property which validates JSON that matches exactly one of
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
            schema_function=one_of,
            optional=optional,
            default=default
        )

    @classmethod
    def _choose_subproperty(cls, successes: List[bool]) -> int:
        # Start with an invalid index
        index = -1

        # Search the list
        for i, success in enumerate(successes):
            if success:
                # If a previous success occurred, we have matched multiple sub-properties
                if index >= 0:
                    raise OfPropertySelectionError(f"Value matched more than one sub-property")

                index = i

        if index == -1:
            raise OfPropertySelectionError(f"Value didn't match any sub-properties")

        return index
