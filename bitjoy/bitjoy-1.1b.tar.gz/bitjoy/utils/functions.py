from ..dtypes.bits import Bit
from ..dtypes.bytes_ import Bytes


def int_to_bytes(int_: int, architecture: int = None) -> Bytes:
    """Get Bytes object

    :param int_: number integer to convert to Bytes
        :type: int
    :param architecture: bytes length
        :type: int
    :return: bytes representation
        :type: Bytes
    """

    bin_ = f'{bin(int_)[2:]}'
    bytes_ = [Bit(int(bit)) for bit in bin_]
    return Bytes(bytes_, architecture)
