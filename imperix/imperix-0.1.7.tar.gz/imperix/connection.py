# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

import asyncio

from .protocol import *

# socket handler
async def connectionHandler(node):
    '''
    socket handling task - to be started as a thread.

    Parameters
    ----------
    @param node [NodeLink] - NodeLink object
    '''
    
    while node.threadsActive: # Keep socket open

        # Wait for packet
        p = await Packet.receive(node.socket)

        # Node can only receive image feedback, manual command and mission update packets
        if p.pType == PacketType.IMAGE_FDBK:

            p.__class__ = ImageFeedbackPacket
            feedbackData = p.getData()

            node.imageLatency = feedbackData["LATENCY"]
            node.imageFrameRate = feedbackData["FRAME_RATE"]

            print(feedbackData)

            if node.imageQuality > 0 and (feedbackData["LATENCY"] > 0.05 or feedbackData["FRAME_RATE"] < 15):
                node.imageQuality -= 1 # Drop quality

            elif node.imageQuality < 3 and (feedbackData["LATENCY"] < 0.01 and feedbackData["FRAME_RATE"] > 15):
                node.imageQuality += 1 # Increase quality

            # print(node.imageQuality)
            # Else, maintain quality


        elif p.pType == PacketType.MANUAL_CMD:
            
            p.__class__ = ControlPacket

            # Manual control callback
            if node.manualControlCallback is not None:
                await node.manualControlCallback(p.getData()) # ControlPacket.getData returns a dictionary


        elif p.pType == PacketType.MISSION:

            p.__class__ = MissionPacket

            # Mission update callback
            if node.missionUpdateCallback is not None:

                mission = p.getData()

                # If FETCH is set, then re-fetch mission
                if "FETCH" in mission and mission["FETCH"]:
                    mission = await node.fetchMission() # Re-fetch mission

                await node.missionUpdateCallback(mission) # MissionPacket.getData returns a dictionary


        else:

            print("Received unexpected packet:", p.pType)
            continue