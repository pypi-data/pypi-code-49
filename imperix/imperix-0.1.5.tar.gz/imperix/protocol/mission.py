# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Mission update data packet.
Inherited from DataPacket class, implements:
    1. Constructor given mission data as a dict
    2. Parser to get mission data as a dict
'''

from .packet import PacketType
from .data import DataPacket

class MissionPacket(DataPacket):
    '''
    Mission update data packet object. (see above)
    '''

    pType = PacketType.MISSION
    pData = bytes()

    # Empty Constructor
    def __init__(self):
        super().__init__()
    

    # Set mission
    def setMissionStatus(self, activeWaypoint=-1, missionStatus="Standby"):
        self.setData({
            "ACTIVE_WPT": activeWaypoint,
            "STATUS": missionStatus
        })


    # Set mission waypoints
    def setWaypoints(self, waypoints=[]):
        self.setData({
            "WAYPOINTS": waypoints
        })