"""
Module for type related to JSON objects.
"""
from typing import TypeVar, Union, Optional

from ..serialise import JSONValidatedBiserialisable
from ..raw import RawJSONElement

# ====== #
# ABSENT #
# ====== #


class AbsentType:
    """
    Singleton class representing a property that is absent from
    a configuration. This is used instead of None, because None
    is a valid value for some properties (represents JSON null).
    """
    # The singleton instance
    __instance: Optional['AbsentType'] = None

    # Create the instance the first time, then just return it
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __str__(self) -> str:
        return "Absent"


# Create the singleton instance for export
Absent = AbsentType()


# ================= #
# OptionallyPresent #
# ================= #


# The type of the value if it is present
PresentType = TypeVar("PresentType")

OptionallyPresent = Union[AbsentType, PresentType]
"""
Type which can take values of some other type or the singleton Absent value.

E.g. a: OptionallyPresent[int] = |any int or Absent|
"""


# ================= #
# PropertyValueType #
# ================= #


# The type of values a property can take
PropertyValueType = Union[RawJSONElement, JSONValidatedBiserialisable]
