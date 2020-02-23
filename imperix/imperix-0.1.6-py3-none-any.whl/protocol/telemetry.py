# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

'''
Telemetry data packet.
Inherited from Packet class, implements:
    1. Constructor given telemetry data as a dict
    2. Parser to get telemetry as a dict

Telemetry payload format: JSON string (for flexibility)

Telemetry payload object keys: (TODO: Keep updated!)

    1. Attitude
        ATT_ROLL (degrees)
        ATT_PITCH (degrees)
        ATT_HEADING (degrees)

    2. Location
        LOC_LATITUDE (degrees)
        LOC_LONGITUDE (degrees)
        LOC_ALTITUDE (meters)

    3. Velocities/Rates
        VEL_GROUNDSPEED (meters per second)
        VEL_AIRSPEED (meters per second)
        VEL_VERTICAL_SPEED (meters per second)
        VEL_ROLL_RATE (degrees per second)
        VEL_PITCH_RATE (degrees per second)
        VEL_YAW_RATE (degrees per second)

    4. Node Status
        STS_BATTERY (percentage 0-100)
        STS_SIGNAL (percentage 0-100)
'''

import json
from .packet import PacketType
from .data import DataPacket

class TelemetryPacket(DataPacket):
    '''
    Telemetry data packet object. (see above)
    '''

    pType = PacketType.TELEMETRY
    pData = bytes()

    # Empty Constructor
    def __init__(self):
        super().__init__()
    

