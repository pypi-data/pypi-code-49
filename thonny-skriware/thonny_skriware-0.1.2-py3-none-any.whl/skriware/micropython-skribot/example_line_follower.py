# This example uses two line distance sensors of the robot
# to follow a black line

from skribot import Skribot
from skribrain import * # pinout definition

# Define the robot
robot = Skribot()

# Set the speed to a small value
# to make robot detect the line better
robot.set_speed(45)

while True:
    # Check if the sensors detected a black line
    left_black = robot.read_line_sensor(LINE1)
    right_black = robot.read_line_sensor(LINE3)

    # If no line is detected, then move a little bit forward
    if (not left_black and not right_black):
        robot.move_forward(25)

    else:
        if left_black:
            robot.face_right(25)

        elif right_black:
            robot.face_left(25)
            
