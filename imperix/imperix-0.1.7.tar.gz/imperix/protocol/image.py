# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Image data packets - list of packets containing image header and data chunks.

Image header must contain the following information:
    1. Timestamp
    2. Number of chunks, or -1/0 if live data stream
    3. Feed name
'''

MAX_PAYLOAD_SIZE = 60000
JPEG_MAX_COMPRESSION_RATIO = 80 # percent


import io
import json
import struct
import asyncio
import traceback
import numpy as np
from PIL import Image
from datetime import datetime

from .packet import Packet, PacketType
from .data import DataPacket


# Image header packet
class ImageFeedbackPacket(DataPacket):
    pType = PacketType.IMAGE_FDBK

    # Empty Constructor
    def __init__(self):
        super().__init__()


# Image start chunk
class ImageStartPacket(Packet):
    pType = PacketType.IMAGE_START

    # Empty Constructor
    def __init__(self):
        super().__init__()
    

    # Encode chunk in packet
    def encode(self, numChunks, firstChunk, feedName='PRIMARY'):

        # First 8 bytes represent UTC UNIX timestamp as 64-bit float (double-precision)
        utc = datetime.utcnow().timestamp()

        # Construct feedname
        feedNameBytes = bytes(''.join([ feedName[i] if i < len(feedName) else chr(0) for i in range(12) ]), 'utf-8')

        self.pData = bytes(struct.pack("d", utc)) + feedNameBytes + bytes([int(numChunks)]) + firstChunk


    # Get timestamp from packet
    def getTimestamp(self):
        utc = struct.unpack("d", self.pData[:8])[0]
        return datetime.fromtimestamp(utc)

    # Get image/video feed name
    def getFeedName(self):
        return ''.join([ chr(c) for c in self.pData[8:20] if c > 0 ])

    # Get number of chunks from packet
    def getNumChunks(self):
        return self.pData[20]

    # Get chunk from packet
    def getChunk(self):
        return self.pData[21:]


# Image chunk packet
class ImageChunkPacket(Packet):
    pType = PacketType.IMAGE_CHUNK

    # Empty Constructor
    def __init__(self):
        super().__init__()


class ImageData:
    '''
    We can't transmit an image with only a single packet, so this is a set of packets
    '''

    # First chunk is the start packet
    chunks = list() # List of chunks
    

    # Constructor
    def __init__(self, chunks):
        self.chunks = chunks


    @staticmethod
    def constructFromBytes(
        imageData,
        timestamp=None,
        feed="PRIMARY"
    ):
        '''
        Generate an image packet set given a pre-compressed image binary, and optional parameters.

        Parameters
        ----------
        @param imageBytes [bytes] - image bytes data
        @param timestamp [datetime] - if None, use current timestamp, and set to Live
        @param feed [str] - feed name
        '''

        imageChunks = list()

        # Construct image data packets (chunkify)
        for chunkStart in range(0,len(imageData),MAX_PAYLOAD_SIZE):

            chunkEnd = chunkStart + MAX_PAYLOAD_SIZE

            if chunkStart == 0:
                chunkPacket = ImageStartPacket()
                chunkPacket.encode(np.ceil(len(imageData) / MAX_PAYLOAD_SIZE), imageData[chunkStart:chunkEnd], feedName=feed)

            else:
                chunkPacket = ImageChunkPacket()
                chunkPacket.pData = imageData[chunkStart:chunkEnd]
            
            imageChunks.append(chunkPacket)

        return ImageData(imageChunks)


    @staticmethod
    def constructFromImage(
            image,
            timestamp=None,
            feed="PRIMARY",
            resize=None,
            compressionRatio=JPEG_MAX_COMPRESSION_RATIO
        ):
        '''
        Generate an image packet set given an image, and optional parameters.

        Parameters
        ----------
        @param image [np.ndarray] - image data
        @param timestamp [datetime] - if None, use current timestamp, and set to Live
        @param feed [str] - feed name
        @param resize - None (don't resize), or (w,h)
        @param compressionRatio - percentage JPEG compression

        Returns
        -------
        @out [ImageData]
        '''
        
        # Construct image data and then call the bytes constructor
        imageData = io.BytesIO()
        imageJPEG = Image.fromarray(image.astype(np.uint8))

        if resize is not None:
            imageJPEG = imageJPEG.resize(resize)

        # Compress JPEG for transmission (sorry, but we need fast transmissions)
        imageJPEG.save(imageData, format='JPEG', quality=compressionRatio)

        return ImageData.constructFromBytes(
            imageData.getvalue(),
            timestamp=timestamp,
            feed=feed
        )

    
    def getTimestamp(self):
        '''
        Return timestamp from when the image was created/sent.

        Returns
        -------
        @out timestamp [datetime] - image timestamp
        '''

        if len(self.chunks) < 1:
            raise Exception('Image does not have any data')

        return self.chunks[0].getTimestamp()


    def getImage(self):
        '''
        Return image as numpy array from packet data

        Returns
        -------
        @out image [np.ndarray] - image as numpy array
        '''

        if len(self.chunks) < 1:
            raise Exception('Image does not have any data')
        
        # Construct image as byte array
        imageData = bytes()

        for chunkId in range(len(self.chunks)):
            
            if chunkId == 0:
                chunk = self.chunks[chunkId].getChunk()

            else:
                chunk = self.chunks[chunkId].pData
            
            imageData += chunk


        imageJPEG = Image.open(io.BytesIO(imageData))
        
        # Generate numpy array from byte array
        image = np.array(imageJPEG, dtype=np.uint8)

        return image

    
    # Transmit class function
    async def transmit(self, socket):
        '''
        Transmit packet via socket.

        Parameters
        ----------
        @param socket [socket.socket] - connected socket object/reference

        Returns
        -------
        @out [bool] - true if success
        '''

        try:

            # Transmit image data chunks (including first)
            for chunk in self.chunks:
                await chunk.transmit(socket)

            return True # Success

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            pass

    
    # Parse static method (parse set of packets)
    @staticmethod
    async def parse(imageHeader, socket):
        '''
        Parse image data packets.

        Parameters
        ----------
        @param imageHeader [ImageStartPacket] - first chunk
        @param socket [socket.socket] - connected socket object/reference to receive the image data chunks

        Returns
        -------
        @out [ImageData] - parsed image data packet set
        '''

        # Extract image data - header and chunks
        imageChunks = [ imageHeader ]

        numChunks = imageHeader.getNumChunks()

        # Parse chunks
        for _ in range(1,numChunks):
            chunkPayload = await socket.recv()

            # Ensure chunk is actually a chunk
            if PacketType(bytes([chunkPayload[0]])) != PacketType.IMAGE_CHUNK:
                raise Exception('Unexpected packet type received as image chunk.')

            imageChunk = ImageChunkPacket()
            imageChunk.pData = chunkPayload[1:]
            imageChunks.append(imageChunk)
            
        return ImageData(imageChunks)