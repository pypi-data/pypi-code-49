# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

import asyncio

from ..protocol import *

# socket handler
async def connectionHandler(active, manualControlCallback, socket):
    '''
    socket handling task - to be started as a thread.

    Parameters
    ----------
    @param active [bool] - should thread be running?
    @param manualControlCallback [func(control)] - callback function to be called when a manual control command is received.
    @param socket [socket.socket] - socket to socket
    '''
    
    while active: # Keep socket open

        # Wait for packet
        p = await Packet.receive(socket)

        # Node can only receive manual command packets
        if p.pType != PacketType.MANUAL_CMD:
            print("Received unexpected packet:", p.pType)
            continue

        p.__class__ = ControlPacket

        # Manual control callback
        if manualControlCallback is not None:
            manualControlCallback(p.getData()) # ControlPacket.getData returns a dictionary