# This example uses two distance sensors to avoid obstacles

from skribot import Skribot
from skribrain import * # pinout definition

# Define the robot
robot = Skribot()

# Configure connections
robot.add_dc_rotor(MOTOR1, 'LEFT')
robot.add_dc_rotor(MOTOR3, 'RIGHT')
robot.add_claw(SERVO1, SERVO2)
robot.add_distance_sensor(D1)
robot.add_distance_sensor(D2)

robot.set_speed(200)

# Raise the gripper to make it not disturb the distance sensors
robot.pick_up() 

while True:
    # Move forward for half a second
    robot.move_forward(500)
    
    # Read distance from both of the sensors
    left_distance = robot.read_distance_sensor(D1)
    right_distance = robot.read_distance_sensor(D2)
    
    # If any sensor is less than 30 cm from an obstacle, turn left
    if left_distance < 30 or right_distance < 30:
        robot.face_left(700)

