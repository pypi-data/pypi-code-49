# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Control command data packet.
Inherited from DataPacket class, implements:
    1. Constructor given control commands data as a dict
    2. Parser to get control commands data as a dict
'''

from .packet import PacketType
from .data import DataPacket

class ControlPacket(DataPacket):
    '''
    Control command data packet object. (see above)
    '''

    pType = PacketType.STREAM_DATA
    pData = bytes()

    # Empty Constructor
    def __init__(self):
        super().__init__()
    
