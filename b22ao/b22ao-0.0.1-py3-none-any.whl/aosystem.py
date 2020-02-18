from epics import caget, caput, camonitor
from b22ao.pvs import *
from enum import Enum
from threading import Event


class AOSystem:

    def __init__(self):
        self.dm1 = DeformableMirror(DM1_PVBASE)
        self.dm2 = DeformableMirror(DM2_PVBASE)
        self.cam = AreaDetector(AD_PVBASE)
        self.dm = None  # DM of choice

    def select_dm(self, dm):
        self.dm = self.__get_dm(dm)

    def deform(self, mask, dm=None):
        if dm:
            self.__get_dm(dm).deform(mask)
        else:
            try:
                self.dm.deform(mask)
            except AttributeError:
                print("Call #select_dm(dm) first or specify a DM in #deform(mask, dm)")

    def capture(self):
        return self.cam.acquire()

    def __get_dm(self, dm):
        assert isinstance(dm, DM)
        if dm is DM.DM1:
            return self.dm1
        if dm is DM.DM2:
            return self.dm2
        raise TypeError("Unrecognised enum: %s" % dm.name)


class DeformableMirror:
    def __init__(self, pv_base):

        self.pv_base = pv_base if pv_base.endswith(':') else pv_base + ':'

    def deform(self, mask):
        for actuator in range(len(mask)):
            caput(self.pv_base + DM_ACTUATOR_PREFIX + str(actuator), mask[actuator])


class DM(Enum):
    DM1 = 1
    DM2 = 2


class AreaDetector:

    def __init__(self, pv_base):
        pv_base = pv_base if pv_base.endswith(':') else pv_base + ':'
        self.data_ready = Event()
        self.current_frame = None
        self.frame_counter_pv = pv_base + AD_ARRAY_COUNTER
        self.acquire_pv = pv_base + AD_ACQUIRE
        self.data_pv = pv_base + AD_ARRAY_DATA

        camonitor(self.frame_counter_pv, callback=self.frame_counter_callback)

    def acquire(self):
        self.current_frame = caget(self.frame_counter_pv)
        caput(self.acquire_pv, "Acquire")
        self.data_ready.wait()
        data = caget(self.data_pv)
        self.data_ready.clear()
        return data

    def frame_counter_callback(self, **kwargs):
        if kwargs['value'] == self.current_frame + 1:
            self.data_ready.set()
