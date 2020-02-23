from itertools import zip_longest
from typing import Sequence, List

from .bits import Bit
from .circuits import Adder


class Bytes:

    def __init__(self, bits: Sequence[Bit], architecture: int = None):
        """Bytes class

        :param bits: sequence of bits to make a bytes
            :type: Sequence[Bit]
        :param architecture: bytes architecture
            :type: int
            :default: len(bits) if len(bits) > 8 else 8
        """

        bits = list(bits)
        bits_length = len(bits)

        if not architecture:
            architecture = 8 if bits_length < 8 else bits_length

        if bits_length <= architecture:
            bits = [Bit(0)] * (architecture - bits_length) + bits
            bits_length = len(bits)
        else:
            raise ValueError('architecture must be greater or equal to bits\' length')

        self._bits = bits
        self._architecture = bits_length

    @property
    def bits(self) -> List[Bit]:
        """getter list of bits"""
        return self._bits

    @property
    def architecture(self) -> int:
        """getter bytes architecture"""
        return self._architecture

    def change_architecture(self, value: int) -> 'Bytes':
        """Return a new Bytes class with another architecture

        :param value: new architecture value
            :type: int
        :return: new Bytes object
            :type: Bytes
        """
        cls = type(self)
        return cls(self, value)

    def __iter__(self):
        return iter(self.bits)

    def __add__(self, other):
        # TODO: optimization without reversed method
        cls = type(self)
        if isinstance(other, cls):
            result = []
            carry = Bit(0)
            for self_bit, other_bit in zip_longest(reversed(self.bits), reversed(other.bits), fillvalue=Bit(0)):
                sum_, carry = Adder.full(self_bit, other_bit, carry)
                result.append(sum_)
            return cls(reversed(result))
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __int__(self):
        bits = ''.join(str(bit.value) for bit in self.bits)
        bits = '0b' + bits
        return int(bits, 2)

    def __index__(self):
        return self.__int__()

    def __eq__(self, other: 'Bytes') -> bool:
        if self.architecture != other.architecture or int(self) != int(other):
            return False
        return True

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}{tuple(bit.value for bit in self.bits)}'
