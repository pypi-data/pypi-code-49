from typing import Optional

from ...raw import RawJSONPrimitive
from ...schema import constant
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._RawProperty import RawProperty


class ConstantProperty(RawProperty):
    """
    Configuration property which validates a constant primitive value.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 value: RawJSONPrimitive = None,
                 *,
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        self._value = value

        super().__init__(
            name,
            schema=constant(value),
            optional=optional,
            default=default
        )

    @property
    def value(self) -> RawJSONPrimitive:
        """
        Gets the constant value this property takes.

        :return:    The constant value.
        """
        return self._value
