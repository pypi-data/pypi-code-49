from typing import Optional

from ...schema import BOOL_SCHEMA
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._RawProperty import RawProperty


class BoolProperty(RawProperty):
    """
    Configuration property which validates a boolean value.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        super().__init__(
            name,
            schema=BOOL_SCHEMA,
            optional=optional,
            default=default
        )
