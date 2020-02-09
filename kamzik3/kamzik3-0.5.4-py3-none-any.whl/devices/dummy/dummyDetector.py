import time
from threading import Event, Thread

import numpy as np

from kamzik3.devices.dummy.deviceDummy import DeviceDummy
from kamzik3 import DeviceError
from kamzik3.constants import *
from kamzik3.snippets.snippetsDecorators import expose_method
from kamzik3.snippets.snippetsUnits import device_units

ATTR_ACQUIRED_FRAMES = "Acquired frames"
ATTR_FRAME_NAME = u"Frame name"
ATTR_FRAME_FILE = u"Frame file"


class DummyDetector(DeviceDummy):

    def __init__(self, device_id=None, config=None):
        self.acquisition_running = Event()
        DeviceDummy.__init__(self, device_id, config)

    def _init_attributes(self):
        DeviceDummy._init_attributes(self)
        self.create_attribute(ATTR_EXPOSURE_TIME, default_value=0, readonly=False, default_type=np.float, unit="ms",
                              min_value=1)
        self.create_attribute(ATTR_FRAME_IMAGE, default_value=0, readonly=True, default_type=np.uint64)
        self.create_attribute(ATTR_FRAME_NAME, default_value="Frame", readonly=False)
        self.create_attribute(ATTR_FRAME_FILE, default_value=0, readonly=True)
        self.create_attribute(ATTR_SUMMED_FRAMES, default_value=0, readonly=False, default_type=np.uint64, min_value=1)
        self.create_attribute(ATTR_ACQUIRED_FRAMES, default_value=0, readonly=True, default_type=np.uint64)

    @expose_method()
    def stop(self):
        self.acquisition_running.clear()

    @expose_method({"Name": ATTR_FRAME_NAME, "Frames": ATTR_SUMMED_FRAMES, "Exposure": ATTR_EXPOSURE_TIME})
    def start_acquisition(self, Name, Frames, Exposure):
        if self.acquisition_running.isSet():
            raise DeviceError("Another acquisition is already running")
        self.acquisition_running.set()
        Frames = device_units(self, ATTR_SUMMED_FRAMES, Frames)
        Exposure = device_units(self, ATTR_EXPOSURE_TIME, Exposure)

        self.set_status(STATUS_BUSY)
        self.set_value(ATTR_FRAME_NAME, Name)
        self.set_value(ATTR_SUMMED_FRAMES, Frames)
        self.set_value(ATTR_EXPOSURE_TIME, Exposure)
        self.set_value(ATTR_ACQUIRED_FRAMES, 0)

        def _acquire():
            exposure_time_increment = 100
            current_exposure_time = 0

            while self.acquisition_running.isSet():
                time.sleep(exposure_time_increment * 1e-3)
                current_exposure_time += exposure_time_increment
                acquired_frames = int(current_exposure_time / Exposure.m)

                if acquired_frames >= Frames:
                    self.set_value(ATTR_ACQUIRED_FRAMES, Frames)
                    break
                else:
                    self.set_value(ATTR_ACQUIRED_FRAMES, acquired_frames)

            if self.connected:
                self.acquisition_running.clear()
                self.set_status(STATUS_IDLE)

        Thread(target=_acquire).start()
