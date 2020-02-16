from typing import Union
from numbers import Integral


class Bit:
    VALUE = None

    def __new__(cls, value: int):
        if value > 0:
            return super().__new__(PositiveBit)
        else:
            return super().__new__(NegativeBit)

    def __add__(self, other):
        if isinstance(other, Bit):
            return Bit(self.VALUE + other.VALUE)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}({self.VALUE})'

    def __eq__(self, other: Union['Bit', Integral]):
        cls = type(self)
        if isinstance(other, cls):
            return self.VALUE == other.VALUE
        elif isinstance(other, Integral):
            return self.VALUE == other
        return NotImplemented


class PositiveBit(Bit):
    VALUE = 1


class NegativeBit(Bit):
    VALUE = 0
