from typing import Iterable, Optional, Tuple, Set

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
        # Consume the iterable
        self._values: Set[RawJSONPrimitive] = set(values)

        super().__init__(
            name,
            schema=enum(*self._values),
            optional=optional
        )

    @property
    def values(self) -> Set[RawJSONPrimitive]:
        """
        Gets the values this property takes.

        :return:    The set of values.
        """
        return self._values.copy()
