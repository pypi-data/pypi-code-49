from pulseapi import *

def position_2_xyzrpw(robot_position):
    XYZ = robot_position.point.to_dict().values()
    RPW = robot_position.rotation.to_dict().values()

    return [*XYZ, *RPW]

def list_2_position(target_position):
    point = target_position[0:3]
    rotation = target_position[3:6]

    return position([*point],[*rotation])