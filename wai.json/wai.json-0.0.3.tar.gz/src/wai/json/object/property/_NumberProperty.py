from typing import Optional

from ...raw import RawJSONNumber
from ...schema import number
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._RawProperty import RawProperty


class NumberProperty(RawProperty):
    """
    Property which validates a number.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 minimum: Optional[RawJSONNumber] = None,
                 maximum: Optional[RawJSONNumber] = None,
                 integer_only: bool = False,
                 multiple_of: Optional[RawJSONNumber] = None,
                 exclusive_minimum: bool = False,
                 exclusive_maximum: bool = False,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        super().__init__(
            name,
            schema=number(
                minimum,
                maximum,
                integer_only,
                multiple_of,
                exclusive_minimum,
                exclusive_maximum
            ),
            optional=optional,
            default=default
        )
