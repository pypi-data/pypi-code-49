from typing import Optional

from ...schema import string_schema
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._RawProperty import RawProperty


class StringProperty(RawProperty):
    """
    Configuration property which validates a string.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 min_length: Optional[int] = None,
                 max_length: Optional[int] = None,
                 pattern: Optional[str] = None,
                 format: Optional[str] = None,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        super().__init__(
            name,
            schema=string_schema(
                min_length,
                max_length,
                pattern,
                format
            ),
            optional=optional,
            default=default
        )
