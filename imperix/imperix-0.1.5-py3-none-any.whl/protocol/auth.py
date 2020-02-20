# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
The first packet received from a client must be an authorization
request packet. This is done through the stream instead of an API
request in order to capture the client address and save it to a
white list.

The authorization packet/header must include the following:
    IS_NODE: True if node, False if ui
    ID: UUID for node, or user
    KEY: Secret key associated with node, or user access token
'''

from .packet import PacketType
from .data import DataPacket

class AuthPacket(DataPacket):
    '''
    Authorization header packet object. (see above)
    '''
    pType = PacketType.AUTH_HEADER

    # Empty Constructor
    def __init__(self):
        super().__init__()
    

    # Construct from auth info
    @staticmethod
    def constructFromAuth(ident, key, isNode=False):
        p = AuthPacket()

        p.setData({
            "IS_NODE": isNode,
            "ID": ident,
            "KEY": key
        })

        return p