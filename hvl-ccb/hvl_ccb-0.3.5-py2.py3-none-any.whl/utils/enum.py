#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#

import aenum


# Use abstract base class instead of Mixin to inherit from `aenum.Enum` to make Sphinx
# detect inheritance correctly and create docs for derived enums, including such as
# these in `dev.supercube.constants`. With Mixin approach, module-level enum classes
# are not documented.
class StrEnumBase(aenum.Enum):
    """
    String representation-based equality and lookup.
    """

    def __eq__(self, other):
        return (self is other) or (other.__eq__(str(self)))

    # use only with aenum enums
    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member == value:
                return member

    def __str__(self):
        raise NotImplementedError


unique = aenum.unique


class ValueEnum(StrEnumBase):
    """
    Enum with string representation of values used as string representation, and with
    lookup and equality based on this representation.

    Attention: to avoid errors, best use together with `unique` enum decorator.
    """

    def __str__(self):
        return str(self.value)


class NameEnum(StrEnumBase):
    """
    Enum with names used as string representation, and with lookup and equality based on
    this representation.
    """

    def __str__(self):
        return self.name


class AutoNumberNameEnum(StrEnumBase, aenum.AutoNumberEnum):
    """
    Auto-numbered enum with names used as string representation, and with lookup and
    equality based on this representation.
    """

    def __str__(self):
        return self.name
