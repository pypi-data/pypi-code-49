from __future__ import annotations
from .ReservedBytes import ReservedBytes


# define a packet class
class Packet:
    def __init__(self, *args: bytes, sending: bool = True):
        # byte array
        self.bytes = bytearray()

        # marks if the packet is being used for sending data
        self.sending = sending

        # go through all of the args and add them
        for arg in args:
            self.bytes.extend(arg)

        # if the packet is going to be used for sending add the end message byte
        if sending:
            # add the end message char if it is a sending packet
            self.bytes.extend(ReservedBytes.END_MESSAGE.value)

    # used for removing the end message sequence if desired
    def pop_tail(self) -> bool:
        # size of the end message value (negative to get the last x values)
        end_size = -1 * len(ReservedBytes.END_MESSAGE.value)

        # ensure that the current bytes array is at least the size of the end message sequence
        if len(self.bytes) < end_size:
            return False

        # get the last sequence of bytes equal in length to the end message sequence
        tail = self.bytes[end_size:]

        # check if the tail of self.bytes marches the sequence for an end message sequence
        if tail != ReservedBytes.END_MESSAGE.value:
            return False

        # remove the tail
        else:
            # remove the tail (last x bytes equal to the length of the end message sequence)
            del self.bytes[end_size:]

            return True

    # overload the equality operator in python
    def __eq__(self, other: Packet) -> bool:
        if self.bytes == other.bytes:
            return True
        else:
            return False
