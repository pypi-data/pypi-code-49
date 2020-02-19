from typing import Optional

from ...raw import RawJSONPrimitive
from ...schema import constant
from ._RawProperty import RawProperty


class ConstantProperty(RawProperty):
    """
    Configuration property which validates a constant primitive value.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 value: RawJSONPrimitive = None,
                 *,
                 optional: bool = False):
        super().__init__(
            name,
            schema=constant(value),
            optional=optional
        )
