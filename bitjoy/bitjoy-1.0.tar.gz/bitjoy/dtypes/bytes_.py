from typing import Sequence

from .bits import Bit
from .circuits import Adder


class Bytes:

    def __init__(self, bits: Sequence[Bit]):
        self._bits = list(bits)

        assert len(self._bits) == 8, 'Bytes has only 8 bits'

    @property
    def bits(self):
        return self._bits

    def __iter__(self):
        return iter(self._bits)

    def __add__(self, other):
        cls = type(self)
        if isinstance(other, cls):
            self_bits = reversed(self.bits)
            other_bits = reversed(other.bits)
            result = []
            for i, (self_bit, other_bit) in enumerate(zip(self_bits, other_bits)):
                if i == 0:
                    sum_, carry = Adder.full(self_bit, other_bit, Bit(0))
                else:
                    sum_, carry = Adder.full(self_bit, other_bit, carry)
                result.append(sum_)
            return cls(reversed(result))
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def sum_(self, other: 'Bytes') -> 'Bytes':
        return self.__add__(other)

    def __int__(self):
        bits = ''.join(str(bit.VALUE) for bit in self._bits)
        bits = '0b' + bits
        return int(bits, 2)

    def __index__(self):
        return self.__int__()

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}{tuple(bit.VALUE for bit in self._bits)}'
