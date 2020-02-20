# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Protocol parser/generator for a given data point that was either
received (parser) or is to be transmitted (generator).
'''

import time
import asyncio

# Packet types
from enum import Enum
class PacketType(Enum):

    # Invalid/unset
    TYPE_UNSET =    b'\x00'

    # Data request from UI
    REQUEST_DATA =  b'\x01'

    # Authorization header
    AUTH_HEADER =   b'\x02'

    # Telemetry
    TELEMETRY =     b'\x03'

    # Image header/chunk
    IMAGE_HEADER =  b'\x04'
    IMAGE_CHUNK =   b'\x05'

    # Stream data (any variable)
    STREAM_DATA =   b'\x06'

    # Manual control command
    MANUAL_CMD =    b'\x07'

    # Mission update
    MISSION =       b'\x08'


# Packet object (base class)
class Packet:
    '''
    A packet is either transmitted or received.
    A packet may be of different types:
        1. Telemetry data
        2. Image header
        3. Image chunk
        4. Stream data
        5. Manual control commands

    A packet contains a data type id/field id (single byte),
    and the raw payload data.
    '''

    # Packet Type
    pType = PacketType.TYPE_UNSET
    pData = bytes()


    # Construct from type and data
    @staticmethod
    def constructFromData(packetType, packetData):
        '''
        Class constructor given packet type and data
        '''
        p = Packet()
        p.pType = packetType
        p.pData = packetData
        return p


    # Transmit packet
    async def transmit(self, socket):
        '''
        Transmit packet via socket.

        Parameters
        ----------
        @param socket [socket.socket] - connected socket object/reference
        '''

        await socket.send(self.pType.value + self.pData)


    # Parse packet - static method
    @staticmethod
    def parse(payload):
        '''
        Parse packet payload.

        Parameters
        ----------
        @param payload [bytes] - received bytes payload

        Returns
        -------
        @out packet [Packet] - parsed packet object
        '''

        if not isinstance(payload, bytes):
            raise Exception('Packet payload is not a bytes object.')

        if len(payload) < 1:
            raise Exception('Packet payload must have at least 1 byte.')

        # Create packet object to return
        try:
            packet = Packet.constructFromData(PacketType(bytes([payload[0]])), payload[1:])
            return packet

        except ValueError:
            raise Exception('Unknown packet type identifier.')

    
    # Receive packet and parse
    @staticmethod
    async def receive(socket):
        '''
        Receive and parse packet from socket.

        Parameters
        ----------
        @param socket [socket.socket] - connected socket object/reference

        Returns
        -------
        @out packet [Packet] - parsed packet object, or None if disconnected
        '''

        rx = await socket.recv()
        return Packet.parse(rx)







