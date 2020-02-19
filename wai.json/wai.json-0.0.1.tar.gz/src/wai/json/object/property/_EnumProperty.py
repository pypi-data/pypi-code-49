from typing import Iterable, Optional

from ...raw import RawJSONPrimitive
from ...schema import enum
from ._RawProperty import RawProperty


class EnumProperty(RawProperty):
    """
    Property which accepts one of a set of specific primitive values.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 values: Iterable[RawJSONPrimitive] = tuple(),
                 optional: bool = False):
        super().__init__(
            name,
            schema=enum(*values),
            optional=optional
        )
