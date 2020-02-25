# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a floating point number."""

from struct import Struct

from .._plum import Plum, getbytes
from ._floattype import FloatType
from ._floatview import FloatView


class Float(float, Plum, metaclass=FloatType):

    """Interpret bytes as a floating point number.

    :param x: value
    :type x: number or str

    """

    __byteorder__ = 'little'
    __nbytes__ = 4
    __struct_pack__ = Struct('<f').pack
    __struct_unpack__ = Struct('<f').unpack

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        chunk, offset = getbytes(buffer, offset, cls.__nbytes__, dump, cls)

        self = cls.__struct_unpack__(chunk)[0]

        if dump:
            dump.value = self

        return self, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        if dump:
            dump.cls = cls

        chunk = cls.__struct_pack__(value)

        end = offset + cls.__nbytes__
        buffer[offset:end] = chunk

        if dump:
            dump.value = value
            dump.memory = chunk

        return end

    __baserepr__ = float.__repr__

    __repr__ = Plum.__repr__

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        """
        return FloatView(cls, buffer, offset)
