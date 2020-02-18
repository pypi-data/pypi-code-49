# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

import json
from .packet import PacketType
from .data import DataPacket

class RequestPacket(DataPacket):
    '''
    Request a datapoint and type from/for a node.
    '''

    pType = PacketType.REQUEST_DATA
    pData = bytes()

    # Empty Constructor
    def __init__(self):
        super().__init__()


    # Construct from settings
    @staticmethod
    def constructFromRequest(node, image=False, data=False):
        p = RequestPacket()
        p.setData({
            "NODE": node,
            "IMAGE": image,
            "DATA": data
        })
        return p