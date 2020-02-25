# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

DATA_BUFFER_SIZE = 65536 #64kB

import os
import time
import errno
import socket
import asyncio
import threading
import websockets
import subprocess

from .protocol import *

# Load environment variables - includes connection config
from dotenv import load_dotenv
load_dotenv()

NODE_UUID = os.getenv('NODE_UUID', default="test")
TEAM_UUID = os.getenv('TEAM_UUID', default="test")
ACCESS_KEY = os.getenv('ACCESS_KEY', default="testKey")
API_URL = os.getenv('API_URL', default="https://api.imperix.ai")
STREAMER_URL = os.getenv('STREAMER_URI', default="ws://localhost:5000")


from .connection import connectionHandler


IMAGE_QUALITY_SIZE = [(360,240), (480,360), (640,480), (960,720)]


# NodeLink class definition
class NodeLink:
    '''
    A NodeLink object is used to interface with the Imperix Cloud.
    See the README.md file or read the complete documentation at:
    https://docs.imperix.ai
    '''

    socket = None

    # Video streams
    videoStreams = {} # Feed name to process dict

    # Image transmission feedback for auto-optimization
    imageQuality = 3 # Best quality
    imageLatency = 0
    imageFrameRate = 0


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
        self.videoStreams = {}

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
        
        await p.transmit(self.socket) # Transmit auth packet

        asyncio.ensure_future(self.start()) # Start processing connection handler coroutine


    # Coroutine
    async def start(self):

        while True: # Try again if we loose connection

            if self.socket is None:
                await asyncio.sleep(1) # Wait to connect

            try:
                await connectionHandler(self)

            except Exception as e:
                print("NodeLink Socket Error:", e)
                await asyncio.sleep(1) # Wait and try again


    # Get mission
    async def fetchMission(self):
        
        pass


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
    async def transmitImage(self, image, timeStamp=None, feed='PRIMARY', optimize=True):
        '''
        Transmit image as numpy array to Imperix Cloud.

        Parameters
        ----------
        @param image [np.ndarray] - numpy array image (1 or 3 channels)
        @param timeStamp [datetime.datetime] - timestamp as a datetime object
        @param feed [str] - name of image/video feed
        @param optimize [bool] - auto-optimize framerate?
        '''

        # Set image transmission parameters to optimize for frame-rate
        if optimize:
            p = ImageData.constructFromImage(image, timeStamp, feed, resize=IMAGE_QUALITY_SIZE[self.imageQuality], compressionRatio=70)

        else:
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


    # Encoded video stream (MPEG)
    async def streamVideoFromSource(self, feedName, source, frameRate=30, videoSize=(640,480), isFile=False):
        '''
        Stream live video from source - file or camera.
        Stream ends (and encoding subprocess is killed) at end of file, or if camera stream is empty.

        Parameters
        ----------
        @param feedName [str] - video feed name
        @param source [str] - video source
        @param frameRate [int] - video frame-rate
        @param videoSize [tuple.int] - video size (w,h)
        @param isFile [bool] - video source is a file?
        '''

        # Start encoding subprocess, add to map
        udpPort = 9000

        self.videoStreams[feedName] = {}

        # Start UDP socket
        self.videoStreams[feedName]["UDP"] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Try to bind on port until success
        for _ in range(10): # Max 10 attempts/streams
            try:
                self.videoStreams[feedName]["UDP"].bind(("localhost", udpPort))
                break # Success
                
            except:
                udpPort += 1 # Try next port
        

        # Start UDP server to handle FFMPEG stream
        self.videoStreams[feedName]["KILL"] = False

        # Threading
        # self.videoStreams[feedName]["THREAD"] = threading.Thread(target=udpPacketHandler, args=(self, feedName))
        # self.videoStreams[feedName]["THREAD"].start()

        # Asyncio coroutine
        asyncio.ensure_future(self.udpServer(feedName))

        # Start FFMPEG streaming
        self.videoStreams[feedName]["PROC"] = subprocess.Popen([
            "ffmpeg",

            # Input
            "-f", "v4l2",
            "-framerate", str(frameRate),
            "-video_size", f"{videoSize[0]}x{videoSize[1]}",
            "-i", source,

            # Settings
            "-preset", "ultrafast",
            "-tune", "zerolatency",
            "-threads", str(1),

            # Output
            "-vcodec", "mpeg1video",
            "-b", "900k", # Bit rate
            "-f", "mpegts",
            f"udp://localhost:{udpPort}" 
        ])

        return

    
    # Video stream UDP server packet handler
    async def udpServer(self, feedName):

        sock = self.videoStreams[feedName]["UDP"]
        sock.setblocking(0) # Non-blocking call

        # Run until either all node threads are killed, or specific feed is killed
        while self.threadsActive and not self.videoStreams[feedName]["KILL"]:

            try:
                rx,_ = sock.recvfrom(DATA_BUFFER_SIZE)
            
            except socket.error as e:
                if e.errno != errno.EAGAIN:
                    raise e

                await asyncio.sleep(0.01)
                continue

            except Exception as e:
                print(e)
                # TODO - handle broken connection
                break

            p = VideoPacket.constructFromChunk(rx, feedName=feedName)
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

        # Kill connection handler thread
        self.threadsActive = False

        # Kill video encoding subprocesses
        for feed in self.videoStreams:
            self.videoStreams[feed]["PROC"].terminate()
        #     self.videoStreams[feed]["KILL"] = True
        #     self.videoStreams[feed]["THREAD"].join()

        # Close socket
        self.socket.close()