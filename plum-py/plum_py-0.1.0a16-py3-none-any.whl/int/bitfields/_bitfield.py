# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Bit field definition."""

from enum import IntEnum
from importlib import import_module


class BitField:

    """Bit field definition.

    :param int size: size in bits
    :param int pos: bit offset of least significant bit
    :param int default: initial value when unspecified
    :param bool signed: interpret as signed integer
    :param bool ignore: do not include field in comparisons

    """

    # pylint: disable=too-many-instance-attributes

    __slots__ = [
        '_make_type',
        '_cls',
        'mask',
        'signbit',
        'default',
        'ignore',
        'name',
        'pos',
        'size',
    ]

    def __init__(self, *, size, cls=None, pos=None, default=None, signed=False, ignore=False):
        if pos is not None:
            pos = int(pos)
            if pos < 0:
                raise TypeError(
                    'bit field position must be greater than or equal to zero')

        size = int(size)
        signed = bool(signed)

        if signed:
            if size < 2:
                raise ValueError(
                    'signed bit field must have bit size of 2 or greater')
            signbit = 1 << (size - 1)
        else:
            if size < 1:
                raise ValueError(
                    'unsigned bit field must have bit size of 1 or greater')
            signbit = 0

        self.default = default
        self.ignore = ignore
        self.mask = (1 << size) - 1
        self.name = None  # filled in later by BitFieldsType
        self.pos = pos
        self.signbit = signbit
        self.size = size
        if cls is None:
            # filled in later using type annotation byte BitFieldsType
            self._cls = None
            self._make_type = None
        else:
            self.cls = cls

    @property
    def cls(self):
        """Bit field type.

        :returns: bit field type
        :rtype: type

        """
        return self._cls

    @cls.setter
    def cls(self, cls):
        # delay import to avoid circular import issue
        bitfields = import_module('.bitfields', 'plum.int')

        self._cls = cls

        acceptable = True

        try:
            if issubclass(cls, IntEnum):
                self._make_type = self._make_enum
            elif issubclass(cls, int):
                self._make_type = self._make_int
            elif issubclass(cls, bitfields.BitFields):
                self._make_type = self._make_bits
            else:
                acceptable = False
        except TypeError:
            acceptable = False  # not a class

        if not acceptable:
            if self.name:
                raise TypeError(
                    f'bit field {self.name!r} type must be int-like')

            raise TypeError(
                f"bit field type must be int-like")

    @property
    def signed(self):
        """Indication if bit field is a signed integer.

        :returns: indication
        :rtype: bool

        """
        return bool(self.signbit)

    def __repr__(self):
        return ('BitField('
                f'name={self.name!r},'
                f'cls={self._cls!r},'
                f'pos={self.pos!r},'
                f'size={self.size!r},'
                f'default={self.default!r},'
                f'signed={self.signed!r}'
                ')')

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        value = (int(obj) >> self.pos) & self.mask

        if self.signbit & value:
            # its a signed number and its negative
            value = -((1 << self.size) - value)

        return self._make_type(obj, value)

    def _make_bits(self, obj, value):
        item = self._cls(value)
        try:
            bitoffset, store = obj.__bitoffset_store__
        except AttributeError:
            bitoffset, store = self.pos, obj
        else:
            bitoffset += self.pos
        item.__bitoffset_store__ = bitoffset, store
        return item

    def _make_int(self, obj, value):
        # pylint: disable=unused-argument
        return self._cls(value)

    def _make_enum(self, obj, value):
        # pylint: disable=unused-argument
        try:
            # pylint: disable=not-callable
            value = self.cls(value)
        except ValueError:
            # must not be a part of the enumeration
            pass

        return value

    def __set__(self, obj, value):
        mask = self.mask
        size = self.size
        pos = self.pos

        try:
            value = int(value)
        except TypeError:
            # must be a nested bit field (where value could be a dict)
            value = self._cls(value)

        if self.signbit:
            minvalue = -(1 << (size - 1))
            maxvalue = -(1 + minvalue)
        else:
            minvalue = 0
            maxvalue = (1 << size) - 1

        if (value < minvalue) or (value > maxvalue):
            raise ValueError(
                f'bit field {self.name!r} requires {minvalue} <= number <= {maxvalue}')

        try:
            bitoffset, obj = obj.__bitoffset_store__
        except AttributeError:
            pass
        else:
            pos += bitoffset

        obj.__value__ = (obj.__value__ & ~(mask << pos)) | ((value & mask) << pos)
