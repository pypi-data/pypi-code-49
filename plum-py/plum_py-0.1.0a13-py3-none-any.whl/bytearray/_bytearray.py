# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a byte array."""

from .._plum import Plum, getbytes
from ._bytearraytype import ByteArrayType


class ByteArray(bytearray, Plum, metaclass=ByteArrayType):

    """Interpret bytes as a byte array.

    .. code-block:: none

        ByteArray(iterable_of_ints) -> bytes array
        ByteArray(string, encoding[, errors]) -> bytes array
        ByteArray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
        ByteArray(int) -> bytes array of size given by the parameter initialized with null bytes
        ByteArray() -> empty bytes array

    """

    # filled in by metaclass
    __nbytes__ = None
    __fill__ = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if (self.__nbytes__ is not None) and (self.__fill__ is not None):
            nfill = self.__nbytes__ - len(self)
            if nfill > 0:
                self.extend([self.__fill__] * nfill)

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        # pylint: disable=too-many-arguments
        chunk, offset = getbytes(buffer, offset, cls.__nbytes__, dump, cls)

        if dump:
            dump.memory = b''
            for i in range(0, len(chunk), 16):
                subchunk = chunk[i:i + 16]
                dump.add_record(
                    access=f'[{i}:{i + len(subchunk)}]',
                    value=str(bytearray(subchunk)),
                    memory=subchunk)

        return bytearray(chunk), offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        if dump:
            dump.cls = cls

        nbytes = cls.__nbytes__
        if nbytes is None:
            nbytes = len(value)
        else:
            if len(value) != nbytes:
                raise ValueError(
                    f'expected length to be {nbytes} but instead found {len(value)}')

        end = offset + nbytes
        buffer[offset:end] = value

        if dump:
            for i in range(0, nbytes, 16):
                chunk = value[i:i + 16]
                dump.add_record(
                    access=f'[{i}:{i + len(chunk)}]',
                    value=str(bytearray(chunk)),
                    memory=chunk)

        return end

    def __str__(self):
        return f"{type(self).__name__}({bytearray.__repr__(self).split('(', 1)[1][:-1]})"

    __baserepr__ = __str__

    __repr__ = __str__
