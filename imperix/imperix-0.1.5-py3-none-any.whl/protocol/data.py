# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Stream data packet.
Inherited from Packet class, implements:
    1. Constructor given stream data as a dict
    2. Parser to get stream data as a dict

Stream data payload format: JSON string (for flexibility)
Stream data may contain any variables and any data types supported by JSON.
'''

import json
from .packet import Packet, PacketType

class DataPacket(Packet):
    '''
    Stream data packet object. (see above)
    '''

    pType = PacketType.STREAM_DATA

    # Empty Constructor
    def __init__(self):
        super().__init__()


    # Construct data packet from dict
    @staticmethod
    def constructFromData(data):
        p = DataPacket()
        p.setData(data)
        return p


    # Set packet data from dict
    def setData(self, data):
        # Serialize dict to JSON string
        self.pData = bytes(json.dumps(data), 'utf-8') # UTF-8 encoded string


    # Set packet data from raw payload
    def setPayload(self, payload):
        self.pData = payload[1:] # First byte is a type identifier - ignore

    
    # Get telemetry data dict from object
    def getData(self):
        return json.loads(self.pData.decode())