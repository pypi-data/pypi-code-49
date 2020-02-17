# Imports
import threading
import serial
import os
import sys
import time
import random
# import logging
from uarm.wrapper import SwiftAPI
# Local Imports
from comm import Communicator
from transport import Transport

class UARM:
    # Camera (OpenMV)
    camera = None
    # uARM
    uarm = None
    # Position
    xPos = 0
    yPos = 0
    zPos = 130
    # Timing
    startTime = 0
    # Control
    mode = 0 # Idle = 0, Running = 1
    # Communication
    comm = none
    # Locks
    moveLock = threading.Lock()

    def __init__(self, camera_port="COM3", uarm_port="COM4", clientPort=1500, clientAddr="localhost", serial_baudrate=115200, serial_timeout=1):
        # Setup camera serial
        self.camera = serial.Serial(camera_port, baudrate=serial_baudrate, timeout=serial_timeout)
        # Setup uARM
        self.uarm = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
        self.uarm.waiting_ready(timeout=3)
        self.uarm.set_mode(0)
        self.uarm.set_position(x=200, y=0, z=130, wait=True)
        self.uarm.set_wrist(90)
        # Setup comms
        self.comm = Communicator(self, clientPort, clientAddr)
        publisherThread = threading.Thread(target=self.comm.publishLoop)
        publisherThread.start()
        subscriberThread = threading.Thread(target=self.comm.subscribeLoop)
        subscriberThread.start()

    def get_uarm(self):
        return self.uarm

    def get_camera(self):
        return self.camera

    def in_idle_pos(self):
        return (self.xPos == 200 and self.yPos == 0 and self.zPos == 130)

    def set_idle(self):
        self.camera.write("Ix".encode("ascii"))

    def go_to_idle(self):
        self.moveLock.acquire()

        try:
            self.xPos = 200
            self.yPos = 0
            self.zPos = 130
            self.uarm.set_position(x=self.xPos, y=self.yPos, z=self.zPos, speed=500000, wait=True)
        finally:
            self.moveLock.release()

        time.sleep(3)

    def set_running(self, func):
        self.mode == 1
        run(self, func)

    def run(self, func):
        while True:
            if self.mode == 0: # Idle
                if not self.in_idle_pos():
                    self.set_idle()
                    self.go_to_idle()
            elif self.mode == 1: # Running
                func()
            else:
                print("[uarm_serial] - Unknown command.")
