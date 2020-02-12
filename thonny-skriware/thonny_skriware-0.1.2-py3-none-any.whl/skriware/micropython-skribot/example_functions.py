# This example shows all of the functions of the robot
# Uncomment the lines to see the effects of the functions

# Import time module so we can use sleep function
import time

from skribot import Skribot
from skribrain import * # pinout definition

# Define the robot
# with all the standard sensors connected
robot = Skribot(predef='SKRIBRAIN')

move_time = 500 # milliseconds
speed = 50 # max = 255

# DC Motor
#robot.speed = speed
#robot.move_forward(move_time)
#robot.move_backward(move_time)
#robot.turn_left(move_time)
#robot.turn_right(move_time)
#robot.face_left(move_time)
#robot.face_right(move_time)

'''
robot.move_forward()
time.sleep(2)
robot.stop()
'''

# Gripper
#robot.pick_up()
#robot.put_down()
#robot.close_claw()
#robot.open_claw()

# LED
#robot.turn_led_on(255, 255, 0)
#robot.turn_led_on(0, 0, 255, LED1)
#robot.turn_led_on(0, 255, 255, LED2)
#robot.turn_led_off()

# Distance sensor
#print('Distance (left):', robot.read_distance_sensor(D1), 'cm')
#print('Distance (right):', robot.read_distance_sensor(D2), 'cm')

# Line sensor
#print('Line sensor #1 black?', robot.read_line_sensor(LINE1))
#print('Line sensor #2 black?', robot.read_line_sensor(LINE2))
#print('Line sensor #3 black?', robot.read_line_sensor(LINE3))

