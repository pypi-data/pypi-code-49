"""Byte operations."""
import struct

BIG_ENDIAN = ">"
LITTLE_ENDIAN = "<"

STRUCT_MAP = {1: "b", 2: "h", 4: "i", 8: "q"}


def byte_width_series(series):
    """Determine the smallest number of bytes to encode a series.

    Parameters
    ----------
    series: iterable
        A series of valeus

    Returns
    -------
    int
        The number of bytes based on the largest value in the series.

    """
    abs_series = [abs(x) for x in series]
    max_n = max(abs_series)
    return byte_width(max_n)


def byte_width(number):
    """Determine the smallest number of bytes that can encode a number.

    Parameters
    ----------
    number: int
        The number to be encoded

    Returns
    -------
    int
        The number of bytes required to encode this value.

    """
    abs_number = abs(number)
    if abs_number <= 127:
        return 1
    elif abs_number <= 32767:
        return 2
    elif abs_number <= 2147483647:
        return 4
    else:
        return 8


def structfmt(series):
    """Represent a series as a formatted struct string.

    Parameters
    ----------
    series : iter
        The series to encode

    Returns
    -------
    str
        A struct encoding string
    """
    byte_width = byte_width_series(series)
    struct_char = STRUCT_MAP[byte_width]
    return len(series) * struct_char


class IO(object):
    """High level interface for handling byte strings."""

    def __init__(self, byteOrder: str) -> None:
        self.bytesOrder = byteOrder

    def c_str(self, buffer: bytes) -> str:
        """Convert a byte array of any size into ascii and then unicode."""
        byte_tuple = struct.unpack(
            # because we assume that EACH byte represents text,
            # that means we've baked in ascii as the encoding method.
            # eg, if 5 bytes can be converted to 5 letters, the only
            # way to do this is if its ascii. so we decode via ascii
            # afterwards.
            # if this needed to change, then we woulndnt multiply
            # the length of the buffer by s. instead, every 4 bytes would
            # be an string, or whatever. if it fails, its probably
            # a malformed wavfile anyway, so /shrug
            f"{self.bytesOrder}{len(buffer)*'s'}",
            buffer,
        )
        return "".join([letter.decode("ascii") for letter in byte_tuple])

    def c_int(self, buffer: bytes) -> int:
        """Convert 4 bytes of a byte array to a signed int.

        Parameters
        ----------
        buffer : bytes
            The bytestring containing data to convert.

        Returns
        -------
        int
            A python int converted by way of a C int.
        """
        return struct.unpack(f"{self.bytesOrder}i", buffer)[0]

    def c_short(self, buffer: bytes) -> int:
        """Convert 2 bytes of a byte array to a signed int.

        Parameters
        ----------
        buffer : bytes
            The bytestring containing data to convert.

        Returns
        -------
        int
            A python int converted by way of a C short.
        """
        return struct.unpack(f"{self.bytesOrder}h", buffer)[0]

    def c_long(self, buffer: bytes) -> int:
        """Convert 8 bytes of a byte array to a signed int.

        Parameters
        ----------
        buffer : bytes
            The bytestring containing data to convert.

        Returns
        -------
        int
            A python int converted by way of a C long.
        """
        return struct.unpack(f"{self.bytesOrder}l", buffer)[0]
