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

    # overload the equality operator in python
    def __eq__(self, other: Packet):
        if self.bytes == other.bytes:
            return True
        else:
            return False
