from ..dtypes.bits import Bit, OneBit


class LogicalOperator:

    # Basic gates
    @staticmethod
    def not_(bit: Bit) -> Bit:
        """ Basic NOT logical operator

        :param bit: first bit
            :type: Bit
        :return: ~bit
            :type: Bit
        """
        if isinstance(bit, OneBit):
            return Bit(0)
        else:
            return Bit(1)

    @staticmethod
    def or_(bit1: Bit, bit2: Bit) -> Bit:
        """ Basic OR logical operator

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :return: bit1 | bit2
            :type: Bit
        """

        return bit1 + bit2

    @classmethod
    def and_(cls, bit1: Bit, bit2: Bit) -> Bit:
        """ Basic AND logical operator

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :return: bit1 & bit2
            :type: Bit
        """

        gate1 = cls.not_(cls.or_(bit1, bit1))
        gate2 = cls.not_(cls.or_(bit2, bit2))
        gate3 = cls.not_(cls.or_(gate1, gate2))
        return gate3

    # Derivative gates
    @classmethod
    def nor_(cls, bit1: Bit, bit2: Bit) -> Bit:
        """ Basic NOR logical operator

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :return: ~(bit1 | bit2)
            :type: Bit
        """

        return cls.not_(cls.or_(bit1, bit2))

    @classmethod
    def nand_(cls, bit1: Bit, bit2: Bit) -> Bit:
        """ Basic NAND logical operator

       :param bit1: first bit
           :type: Bit
       :param bit2: second bit
           :type: Bit
       :return: ~(bit1 & bit2)
           :type: Bit
       """

        return cls.not_(cls.and_(bit1, bit2))

    @classmethod
    def xor_(cls, bit1: Bit, bit2: Bit) -> Bit:
        """ Basic XOR logical operator

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :return: bit1 x bit2
            :type: Bit
        """

        gate1 = cls.nand_(bit1, bit2)
        gate2 = cls.or_(bit1, bit2)
        gate3 = cls.and_(gate1, gate2)
        return gate3

    @classmethod
    def xnor_(cls, bit1: Bit, bit2: Bit) -> Bit:
        """ Basic XNOR logical operator

        :param bit1: first bit
            :type: Bit
        :param bit2: second bit
            :type: Bit
        :return: bit1 x bit2
            :type: Bit
        """

        return cls.not_(cls.xor_(bit1, bit2))
