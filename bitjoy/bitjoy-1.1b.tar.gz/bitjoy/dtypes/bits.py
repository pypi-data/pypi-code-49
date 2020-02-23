from typing import Union
from numbers import Integral


class Bit:
    _VALUE = None

    def __new__(cls, value: int):
        if value > 0:
            return super().__new__(OneBit)
        else:
            return super().__new__(ZeroBit)

    def __add__(self, other):
        if isinstance(other, Bit):
            return Bit(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}({self.value})'

    def __eq__(self, other: Union['Bit', Integral]):
        cls = type(self)
        if isinstance(other, cls):
            return self.value == other.value
        elif isinstance(other, Integral):
            return self.value == other
        return NotImplemented

    @property
    def value(self):
        return self._VALUE


class OneBit(Bit):
    _VALUE = 1


class ZeroBit(Bit):
    _VALUE = 0
