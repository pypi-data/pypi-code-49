# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as integer enumerated constants."""

import enum

from ..._plum import getbytes
from .._int import Int
from ._enumtype import EnumType


class Enum(Int, enum.Enum, metaclass=EnumType):

    """Interpret bytes as integer enumerated constants.

    :param x: value
    :type x: number or str
    :param int base: base of x when x is ``str``

    """

    __enum__ = True
    __strict_enum__ = True

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        chunk, offset = getbytes(buffer, offset, cls.__nbytes__, dump, cls)

        value = int.from_bytes(chunk, cls.__byteorder__, signed=cls.__signed__)

        try:
            value = cls(value)
        except ValueError:
            if cls.__strict_enum__:
                raise

        if dump:
            dump.value = value
            cls._add_flags_to_dump(value, dump)

        return value, offset

    __str__ = enum.IntEnum.__str__

    def __repr__(self):
        # override so representation turns out in Python 3.6
        # e.g. <Sample.A: Int(1)> -> <Sample.A: 1>
        enum_repr = enum.IntEnum.__repr__(self)
        if '(' in enum_repr:  # pragma: no cover
            beg, _, int_repr, _ = enum_repr.replace('(', ' ').replace(')', ' ').split()
            enum_repr = f'{beg} {int_repr}>'
        return enum_repr
