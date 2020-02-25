# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Video chunk packet. Similar to image chunk, but meant to contain MPEG-encoded binary data.
'''

import struct
from datetime import datetime
from .packet import Packet, PacketType

class VideoPacket(Packet):
    '''
    Video packet
    '''

    pType = PacketType.VIDEO_CHUNK

    # Empty Constructor
    def __init__(self):
        super().__init__()

    
    # Pack chunk into packet
    # Chunk must be a segment of MPEG-encoded video
    # Maybe set up a UDP/TCP port for ffmpeg to stream video to and translate to websocket from here?
    @staticmethod
    def constructFromChunk(chunk, feedName='PRIMARY'):
        
        p = VideoPacket()

        # First 8 bytes represent UTC UNIX timestamp as 64-bit float (double-precision)
        utc = datetime.utcnow().timestamp()

        # Construct feedname
        feedNameBytes = bytes(''.join([ feedName[i] if i < len(feedName) else chr(0) for i in range(12) ]), 'utf-8')

        p.pData = bytes(struct.pack("d", utc)) + feedNameBytes + chunk

        return p
    

    # Get timestamp from packet
    def getTimestamp(self):
        utc = struct.unpack("d", self.pData[:8])[0]
        return datetime.fromtimestamp(utc)

    # Get image/video feed name
    def getFeedName(self):
        return ''.join([ chr(c) for c in self.pData[8:20] if c > 0 ])
    
    # Get chunk from packet
    def getChunk(self):
        return self.pData[20:]
