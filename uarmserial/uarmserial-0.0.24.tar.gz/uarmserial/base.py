# Imports
import threading
import serial
import os
import sys
import time
import random
# import logging
from uf.wrapper.swift_api import SwiftAPI
from .transporter import Transport
from .comm import Communicator

class UARM:
    # Camera (OpenMV)
    camera = None
    # uARM
    uarm = None
    # Position
    xPos = 350
    yPos = 0
    zPos = 50
    # Timing
    startTime = 0
    # Control
    mode = 0 # Idle = 0, Running = 1
    # Locks
    moveLock = threading.Lock()

    def __init__(self, camera_port="COM4", uarm_port="COM3", serial_baudrate=115200, serial_timeout=1):
        # Setup camera serial
        self.camera = serial.Serial(camera_port, baudrate=serial_baudrate, timeout=serial_timeout)
        # Setup uARM
        self.uarm = SwiftAPI()
        time.sleep(2)
        self.uarm.set_position(self.xPos, self.yPos, self.zPos, speed=250, timeout=20)

    def get_uarm(self):
        return self.uarm

    def get_camera(self):
        return self.camera

    def in_idle_pos(self):
        return (self.xPos == 0 and self.yPos == 0 and self.zPos == 170)

    def set_idle(self):
        self.camera.write("Ix".encode("ascii"))

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
        #self.camera.write("Rx".encode("ascii")) # Send 'Rx' to camera for running

        while self.mode == 1:
            lambda arg: func(arg)
        else:
            if not self.in_idle_pos():
                self.set_idle()
                self.go_to_idle()
