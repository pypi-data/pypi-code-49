# Imports
import threading
import serial
import os
import sys
import time
import random
# import logging
from uarm.wrapper import SwiftAPI

class UARM:
    # Camera (OpenMV)
    camera = None
    # uARM
    uarm = None
    # Position
    xPos = 0
    yPos = 0
    zPos = 170
    # Timing
    startTime = 0
    # Control
    mode = 0 # Idle = 0, Running = 1
    # Locks
    moveLock = threading.Lock()

    def __init__(self, camera_port="COM3", uarm_port="COM4", serial_baudrate=115200, serial_timeout=1):
        # Setup camera serial
        self.camera = serial.Serial(camera_port, baudrate=serial_baudrate, timeout=serial_timeout)
        # Setup uARM
        self.uarm = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
        self.uarm.waiting_ready(timeout=3)
        self.uarm.set_mode(0)
        self.uarm.set_position(x=self.xPos, y=self.yPos, z=self.zPos, wait=True)
        self.uarm.set_wrist(90)

    def get_uarm(self):
        return self.uarm

    def get_camera(self):
        return self.camera

    def in_idle_pos(self):
        return (self.xPos == 0 and self.yPos == 0 and self.zPos == 170)

    def set_idle(self):
        self.camera.write("I".encode("ascii"))

    def set_posx(x):
        self.uarm.set_position(x=x)

    def set_posy(y):
        self.uarm.set_position(y=y)

    def set_position(x, y, z):
        self.uarm.set_position(x=x, y=y, z=z)

    def go_to_idle(self):
        self.moveLock.acquire()

        try:
            self.xPos = 0
            self.yPos = 0
            self.zPos = 170
            self.uarm.set_position(x=self.xPos, y=self.yPos, z=self.zPos, speed=500000, wait=True)
        finally:
            self.moveLock.release()

        time.sleep(3)

    def run(self, func):
        self.mode = 1
        self.camera.write("R".encode("ascii")) # Send 'R' to camera for running

        while self.mode == 1:
            lambda arg: func(arg)
        else:
            if not self.in_idle_pos():
                self.set_idle()
                self.go_to_idle()
