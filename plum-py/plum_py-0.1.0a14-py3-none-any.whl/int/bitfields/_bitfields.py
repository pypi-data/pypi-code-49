# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""BitFields type."""

from ..._plum import Plum, getbytes
from ._bitfieldstype import BitFieldsType


class BitFields(Plum, metaclass=BitFieldsType, nbytes=4, byteorder='little', default=0, ignore=0):

    """Interpret bytes as an unsigned integer with bit fields."""

    # filled in by metaclass
    __byteorder__ = 'little'
    __compare_mask__ = 0xffffffff
    __fields__ = dict()
    __default__ = 0
    __fields_with_defaults__ = set()
    __ignore__ = 0
    __max__ = 0xffffffff
    __nbytes__ = 4

    def __init__(self, *args, **kwargs):
        # pylint: disable=too-many-branches

        cls = type(self)

        try:
            value = args[0]
        except IndexError:
            self.__value__ = cls.__default__
        else:
            if len(args) > 1:
                raise TypeError(
                    f'{cls.__name__} expected at most 1 arguments, got {len(args)}')

            try:
                default = int(value)
            except TypeError:
                default = cls.__default__

                try:
                    # copy (so we don't mutate) -or- convert key/value pairs
                    values = dict(value)
                except TypeError:
                    raise TypeError(
                        f'{value!r} object is not an int or bit field dict')

                if kwargs:
                    values.update(kwargs)
                    kwargs = values
                else:
                    kwargs = values

            else:
                if kwargs:
                    raise TypeError('cannot specify both integer value and keyword arguments')

                if (default < 0) or (default > cls.__max__):
                    raise ValueError(
                        f'{cls.__name__} requires 0 <= number <= {cls.__max__}')

            self.__value__ = default

        if kwargs:
            fields = cls.__fields__

            extras = set(kwargs) - set(fields)

            if extras:
                plural = 's' if len(extras) > 1 else ''
                message = (
                    f'{cls.__name__}() '
                    f'got {len(extras)} unexpected bit field{plural}: ')
                message += ', '.join(repr(e) for e in sorted(extras))
                raise TypeError(message)

            missing = set(fields) - set(kwargs) - cls.__fields_with_defaults__

            if missing:
                plural = 's' if len(missing) > 1 else ''
                message = (
                    f'{cls.__name__}() '
                    f'missing {len(missing)} required bit field{plural}: ')
                message += ', '.join(repr(m) for m in sorted(missing))
                raise TypeError(message)

            for name, value in kwargs.items():
                fields[name].__set__(self, value)

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        chunk, offset = getbytes(buffer, offset, cls.__nbytes__, dump, cls)

        value = int.from_bytes(chunk, cls.__byteorder__, signed=False)

        self = cls.__new__(cls, value)
        cls.__init__(self, value)

        if dump:
            dump.value = self.__value__
            cls.__add_bitfields_to_dump__(self, dump)

        return self, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        try:
            ivalue = int(value)
        except TypeError:
            value = cls(value)
            ivalue = value.__value__

        nbytes = cls.__nbytes__

        chunk = ivalue.to_bytes(nbytes, cls.__byteorder__, signed=False)

        end = offset + nbytes
        buffer[offset:end] = chunk

        if dump:
            dump.value = str(ivalue)
            dump.memory = chunk
            dump.cls = cls
            cls.__add_bitfields_to_dump__(value, dump)

        return end

    @classmethod
    def __add_bitfields_to_dump__(cls, value, dump, bitoffset=0):
        if not isinstance(value, cls):
            value = cls(value)
        for name, field in cls.__fields__.items():
            if issubclass(field.cls, BitFields):
                row = dump.add_record(access='.' + name, cls=field.cls)
                field.cls.__add_bitfields_to_dump__(
                    getattr(cls, name).__get__(value, cls), row, bitoffset + field.pos)
            else:
                dump.add_record(
                    access='.' + name,
                    bits=(bitoffset + field.pos, field.size),
                    value=str(getattr(cls, name).__get__(value, cls)),
                    cls=field.cls)

    def __repr__(self):
        # str( ) around getattr formats enumerations correctly (otherwise shows
        # as int)
        args = ', '.join(f'{n}={str(getattr(self, n))}' for n in self.__fields__)
        return f'{type(self).__name__}({args})'

    __baserepr__ = __repr__

    @classmethod
    def _normalize_for_compare(cls, value, other):
        if isinstance(other, cls):
            other = other.__value__ & cls.__compare_mask__
            value = value & cls.__compare_mask__
        else:
            try:
                other = int(other)
            except TypeError:
                other = int(cls(other)) & cls.__compare_mask__
                value = value & cls.__compare_mask__
        return value, other

    def __lt__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__lt__(value, other)

    def __le__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__le__(value, other)

    def __eq__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__eq__(value, other)

    def __ne__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__ne__(value, other)

    def __gt__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__gt__(value, other)

    def __ge__(self, other):
        value, other = self._normalize_for_compare(self.__value__, other)
        return int.__ge__(value, other)

    def __hash__(self):
        return int.__hash__(self.__value__ & type(self).__compare_mask__)

    def __bool__(self):
        return int.__bool__(self.__value__ & type(self).__compare_mask__)

    def __add__(self, other):
        return int.__add__(self.__value__, other)

    def __sub__(self, other):
        return int.__sub__(self.__value__, other)

    def __mul__(self, other):
        return int.__mul__(self.__value__, other)

    def __truediv__(self, other):
        return int.__truediv__(self.__value__, other)

    def __floordiv__(self, other):
        return int.__floordiv__(self.__value__, other)

    def __mod__(self, other):
        return int.__mod__(self.__value__, other)

    def __divmod__(self, other):
        return int.__divmod__(self.__value__, other)

    def __pow__(self, other, *args):
        return int.__pow__(self.__value__, other, *args)

    def __lshift__(self, other):
        return int.__lshift__(self.__value__, other)

    def __rshift__(self, other):
        return int.__rshift__(self.__value__, other)

    def __and__(self, other):
        return int.__and__(self.__value__, other)

    def __xor__(self, other):
        return int.__xor__(self.__value__, other)

    def __or__(self, other):
        return int.__or__(self.__value__, other)

    def __radd__(self, other):
        return int.__radd__(self.__value__, other)

    def __rsub__(self, other):
        return int.__rsub__(self.__value__, other)

    def __rmul__(self, other):
        return int.__rmul__(self.__value__, other)

    def __rtruediv__(self, other):
        return int.__rtruediv__(self.__value__, other)

    def __rfloordiv__(self, other):
        return int.__rfloordiv__(self.__value__, other)

    def __rmod__(self, other):
        return int.__rmod__(self.__value__, other)

    def __rdivmod__(self, other):
        return int.__rdivmod__(self.__value__, other)

    def __rpow__(self, other, *args):
        return int.__rpow__(self.__value__, other, *args)

    def __rlshift__(self, other):
        return int.__rlshift__(self.__value__, other)

    def __rrshift__(self, other):
        return int.__rrshift__(self.__value__, other)

    def __rand__(self, other):
        return int.__rand__(self.__value__, other)

    def __rxor__(self, other):
        return int.__rxor__(self.__value__, other)

    def __ror__(self, other):
        return int.__ror__(self.__value__, other)

    def __iadd__(self, other):
        return self.__value__ + other

    def __isub__(self, other):
        return self.__value__ - other

    def __imul__(self, other):
        return self.__value__ * other

    def __itruediv__(self, other):
        return self.__value__ / other

    def __ifloordiv__(self, other):
        return self.__value__ // other

    def __imod__(self, other):
        return self.__value__ % other

    def __ilshift__(self, other):
        return self.__value__ << other

    def __irshift__(self, other):
        return self.__value__ >> other

    def __iand__(self, other):
        return self.__value__ & other

    def __ixor__(self, other):
        return self.__value__ ^ other

    def __ior__(self, other):
        return self.__value__ | other

    def __neg__(self):
        return -self.__value__

    def __pos__(self):
        return self.__value__

    def __abs__(self):
        return self.__value__

    def __invert__(self):
        return ~self.__value__

    def __int__(self):
        return self.__value__

    def __float__(self):
        return int.__float__(self.__value__)

    def __index__(self):
        return int.__index__(self.__value__)

    def __round__(self, *args):
        return int.__round__(self.__value__, *args)

    def asdict(self):
        """Return bit field values in dictionary form.

        :returns: bit field names/values
        :rtype: dict

        """
        return {name: getattr(self, name) for name in self.__fields__}

    def update(self, *args, **kwargs):
        """update bit fields.

        ``D.update([E, ]**F)`` -> ``None``

        Update bit fields in "D" from dict/iterable E and F.

        - If E is present and has a .keys() method, then does:  for k in E: D.k = E[k]
        - If E is present and lacks a .keys() method, then does:  for k, v in E: D.k. = v
        - In either case, this is followed by: for k in F:  D.k = F[k]

        """
        updates = {}
        updates.update(*args, **kwargs)

        for name, value in updates.items():
            setattr(self, name, value)
