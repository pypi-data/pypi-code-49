# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

import asyncio

from .protocol import *

# socket handler
async def connectionHandler(active, manualControlCallback, missionUpdateCallback, socket):
    '''
    socket handling task - to be started as a thread.

    Parameters
    ----------
    @param active [bool] - should thread be running?
    @param manualControlCallback [func(control)] - callback function to be called when a manual control command is received.
    @param socket [socket.socket] - socket to socket
    @param missionUpdateCallback [func(mission)] - callback function to be called when node's mission is updated.
    '''
    
    while active: # Keep socket open

        # Wait for packet
        p = await Packet.receive(socket)

        # Node can only receive manual command and mission update packets
        if p.pType == PacketType.MANUAL_CMD:
            
            p.__class__ = ControlPacket

            # Manual control callback
            if manualControlCallback is not None:
                await manualControlCallback(p.getData()) # ControlPacket.getData returns a dictionary


        elif p.pType != PacketType.MISSION:

            p.__class__ = MissionPacket

            # Mission update callback
            if missionUpdateCallback is not None:
                await missionUpdateCallback(p.getData()) # MissionPacket.getData returns a dictionary


        else:

            print("Received unexpected packet:", p.pType)
            continue