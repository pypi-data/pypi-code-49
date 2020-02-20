# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Image data packets - list of packets containing image header and data chunks.

Image header must contain the following variables:
    1. NUM_CHUNKS - number of chunks to follow header
    2. TIMESTAMP - image data timestamp
    3. LIVE - is image data live?
    7. FEED - name of video feed
'''

MAX_PAYLOAD_SIZE = 60000
JPEG_COMPRESSION_RATIO = 70 # percent


import time


import io
import json
import asyncio
import numpy as np
from PIL import Image
from datetime import datetime

from .packet import Packet, PacketType
from .data import DataPacket


# Image header packet
class ImageHeaderPacket(DataPacket):
    pType = PacketType.IMAGE_HEADER

    # Empty Constructor
    def __init__(self):
        super().__init__()


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

    # List of associated packets for image in order starting from header
    header = None
    headerData = {}
    chunks = list() # List of chunks

    # Constructor
    def __init__(self, header, chunks):
        self.header = header
        self.chunks = chunks

        if self.header is None:
            raise Exception('Image header is invalid.')

        self.headerData = self.header.getData()


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

        # Construct image header packet
        imageHeader = ImageHeaderPacket()
        imageHeader.setData({
            "NUM_CHUNKS": np.ceil(len(imageData) / MAX_PAYLOAD_SIZE),
            "TIMESTAMP": str(datetime.utcnow()) if timestamp is None else timestamp,
            "LIVE": (timestamp is None),
            "FEED": feed
        })

        imageChunks = list()

        # Construct image data packets (chunkify)
        for chunkStart in range(0,len(imageData),MAX_PAYLOAD_SIZE):

            chunkEnd = chunkStart + MAX_PAYLOAD_SIZE

            chunkPacket = ImageChunkPacket()
            chunkPacket.pData = imageData[chunkStart:chunkEnd]
            
            imageChunks.append(chunkPacket)

        return ImageData(imageHeader, imageChunks)


    @staticmethod
    def constructFromImage(
            image,
            timestamp=None,
            feed="PRIMARY"
        ):
        '''
        Generate an image packet set given an image, and optional parameters.

        Parameters
        ----------
        @param image [np.ndarray] - image data
        @param timestamp [datetime] - if None, use current timestamp, and set to Live
        @param feed [str] - feed name
        '''
        
        # Construct image data and then call the bytes constructor
        imageData = io.BytesIO()
        imageJPEG = Image.fromarray(image.astype(np.uint8))

        # Compress JPEG for transmission (sorry, but we need fast transmissions)
        imageJPEG.save(imageData, format='JPEG', quality=JPEG_COMPRESSION_RATIO)

        return ImageData.constructFromBytes(
            imageData.getvalue(),
            timestamp=timestamp,
            feed=feed
        )

    
    def getImage(self):
        '''
        Return image as numpy array from packet data

        Returns
        -------
        @out image [np.ndarray] - image as numpy array
        '''

        if len(self.chunks) != self.headerData["NUM_CHUNKS"]:
            raise Exception('Image data chunks inconsistent.')

        
        # Construct image as byte array
        imageData = bytes()

        for chunk in self.chunks:
            imageData += chunk.pData

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
            
            # Transmit image header
            await self.header.transmit(socket)

            # Transmit image data chunks
            for chunk in self.chunks:
                await chunk.transmit(socket)

            return True # Success

        except:
            pass

    
    # Parse static method (parse set of packets)
    @staticmethod
    async def parse(imageHeader, socket):
        '''
        Parse image data packets.

        Parameters
        ----------
        @param imageHeader [ImageHeaderPacket] - parsed image header packet
        @param socket [socket.socket] - connected socket object/reference to receive the image data chunks

        Returns
        -------
        @out imageData [ImageData] - parsed image data packet set
        '''

        # Extract image data - header and chunks
        imageChunks = list()

        numChunks = int(imageHeader.getData()["NUM_CHUNKS"])

        # Parse chunks
        for _ in range(numChunks):
            chunkPayload = await socket.recv()

            # Ensure chunk is actually a chunk
            if PacketType(bytes([chunkPayload[0]])) != PacketType.IMAGE_CHUNK:
                raise Exception('Unexpected packet type received as image chunk.')

            imageChunk = ImageChunkPacket()
            imageChunk.pData = chunkPayload[1:]
            imageChunks.append(imageChunk)
            
        imageData = ImageData(imageHeader, imageChunks)
        return imageData