from typing import Tuple

from .bits import Bit
from .operators import LogicalOperator


class Adder:

    @staticmethod
    def half(bit1: Bit, bit2: Bit) -> Tuple[Bit, Bit]:
        """Half-Adder circuit which do not receive CarryBit and pass the CarryBit

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :return: addition arithmetic operator
            :type: Tuple
            :example: Bit(1), Bit(0)
                      sum     carry
        """

        return LogicalOperator.xor_(bit1, bit2), LogicalOperator.and_(bit1, bit2)

    @staticmethod
    def full(bit1: Bit, bit2: Bit, carry: Bit) -> Tuple[Bit, Bit]:
        """Full-Adder circuit which receive CarryBit and pass the CarryBit

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :param carry: carry bit
            :type: Bit
        :return: addition arithmetic operator
            :type: Tuple
            :example: Bit(1), Bit(0)
                      sum     carry
        """
        # TODO: sub to 2 half method and a OR gate
        gate1 = LogicalOperator.xor_(bit1, bit2)
        gate2 = LogicalOperator.xor_(gate1, carry)
        gate3 = LogicalOperator.and_(carry, gate1)
        gate4 = LogicalOperator.and_(bit1, bit2)
        gate5 = LogicalOperator.or_(gate3, gate4)
        return gate2, gate5
