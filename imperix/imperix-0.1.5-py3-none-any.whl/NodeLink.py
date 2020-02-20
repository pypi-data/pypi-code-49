# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

DATA_BUFFER_SIZE = 65536 #64kB

import os
import time
import socket
import asyncio
import websockets

from .protocol import *

# Load environment variables - includes connection config
from dotenv import load_dotenv
load_dotenv()

NODE_UUID = os.getenv('NODE_UUID', default="test")
ACCESS_KEY = os.getenv('ACCESS_KEY', default="testKey")
API_URL = os.getenv('API_URL', default="https://api.imperix.ai/")
STREAMER_URL = os.getenv('STREAMER_URI', default="ws://localhost:5000")


from .connection import connectionHandler


# NodeLink class definition
class NodeLink:
    '''
    A NodeLink object is used to interface with the Imperix Cloud.
    See the README.md file or read the complete documentation at:
    https://docs.imperix.ai
    '''

    socket = None

    # Constructor
    def __init__(self, missionUpdateCallback=None, manualControlCallback=None):
        '''
        Initialize link to Imperix Cloud for the node with environment config, and provided mission update callback and manual control callback.

        Parameters
        ----------
        @param missionUpdateCallback [func(mission)] - callback function to be called when node's mission is updated.
        @param manualControlCallback [func(control)] - callback function to be called when a manual control command is received.
        '''

        self.threadsActive = True

        # Set manual control callback thread
        self.manualControlCallback = manualControlCallback
        self.missionUpdateCallback = missionUpdateCallback


    # Destructor
    def __del__(self):
        self.disconnect() # Disconnect before deletion to kill threads


    # Connect
    async def connect(self):

        # Create socket to streamer
        self.socket = await websockets.connect(STREAMER_URL)

        # Send authorization packet
        p = AuthPacket.constructFromAuth(
            NODE_UUID,
            ACCESS_KEY,
            isNode=True
        )
        
        await p.transmit(self.socket)


    # Coroutine
    async def start(self):

        while True: # Try again if we loose connection

            if self.socket is None:
                await asyncio.sleep(1) # Wait to connect

            try:
                await connectionHandler(
                    self.threadsActive,
                    self.manualControlCallback,
                    self.missionUpdateCallback,
                    self.socket
                )

            except Exception as e:
                print("NodeLink Socket Error:", e)
                await asyncio.sleep(1) # Wait and try again


    # Mission update
    async def updateMission(self, activeWaypoint, missionStatus):
        '''
        Update mission state for display on Imperix Commander.

        Parameters
        ----------
        @param activeWaypoint [int] - active waypoint index, must be less than number of waypoints
        @param missionStatus [str] - mission status/error
        '''
        
        packet = MissionPacket()
        packet.setMissionStatus(
            activeWaypoint=activeWaypoint,
            missionStatus=missionStatus
        )

        await packet.transmit(self.socket)


    # Streaming data to the cloud
    # Telemetry
    async def transmitTelemetry(self, telemetry):
        '''
        Transmit dict with JSON-serializable telemetry parameters to Imperix Cloud.

        Parameters
        ----------
        @param telemetry [dict] - see README.md or documentation.
        '''

        packet = TelemetryPacket()

        packet.setData(telemetry)
        await packet.transmit(self.socket)

    
    # Image (array)
    async def transmitImage(self, image, timeStamp=None, feed='PRIMARY'):
        '''
        Transmit image as numpy array to Imperix Cloud.

        Parameters
        ----------
        @param image [np.ndarray] - numpy array image (1 or 3 channels)
        @param timeStamp [datetime.datetime] - timestamp as a datetime object
        @param feed [str] - name of image/video feed
        '''

        p = ImageData.constructFromImage(image, timeStamp, feed)
        await p.transmit(self.socket)

    
    # Image (binary)
    async def transmitImageBinary(self, image, timeStamp=None, feed='PRIMARY'):
        '''
        Transmit image as numpy array to Imperix Cloud.

        Parameters
        ----------
        @param image [bytes] - JPEG images as bytes object
        @param timeStamp [datetime.datetime] - timestamp as a datetime object
        @param feed [str] - name of image/video feed
        '''

        p = ImageData.constructFromBytes(image, timeStamp, feed)
        await p.transmit(self.socket)

    
    # Data stream
    async def transmitData(self, data):
        '''
        Transmit any JSON-serializable data to Imperix Cloud.

        Parameters
        ----------
        @param data [dict] - JSON-serializable data dictionary
        '''

        packet = DataPacket()
        packet.setData(data)
        await packet.transmit(self.socket)

    
    # Disconnect and close threads
    async def disconnect(self):
        '''
        Disconnect and close sockets, and kill threads.
        '''

        self.threadsActive = True

        # Close socket
        self.socket.close()