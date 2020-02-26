from typing import Iterable, Optional, FrozenSet

from ...raw import RawJSONPrimitive
from ...schema import enum
from .._typing import PropertyValueType, Absent, OptionallyPresent
from ._RawProperty import RawProperty


class EnumProperty(RawProperty):
    """
    Property which accepts one of a set of specific primitive values.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 *,
                 values: Iterable[RawJSONPrimitive] = tuple(),
                 optional: bool = False,
                 default: OptionallyPresent[PropertyValueType] = Absent):
        # Consume the iterable
        self._values: FrozenSet[RawJSONPrimitive] = frozenset(values)

        super().__init__(
            name,
            schema=enum(*self._values),
            optional=optional,
            default=default
        )

    @property
    def values(self) -> FrozenSet[RawJSONPrimitive]:
        """
        Gets the values this property takes.

        :return:    The set of values.
        """
        return self._values
