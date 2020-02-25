"""Sweep subsystem"""
from rsfsup.common import Subsystem, validate, scale_time, BOOLEAN


class Sweep(Subsystem, kind="SWEEP"):
    """Sweep subsystem

    Attributes:
        instr (Fsup)
    """

    def __init__(self, instr):
        super().__init__(instr)
        # For now, adjust sweep time automatically according to span and bandwidth
        # settings.
        self._visa.write("SWEEP:TIME:AUTO ON")

    @property
    def time(self):
        """(str): 2.5 ms to 16000 s"""
        value = self._visa.query(f"SENSE{self._screen()}:SWEEP:TIME?")
        return scale_time(float(value))

    @property
    def continuous(self):
        """value (str): {ON, OFF}"""
        result = self._visa.query(f"INITIATE{self._screen()}:CONTINUOUS?")
        return BOOLEAN.get(result, result)

    @continuous.setter
    @validate
    def continuous(self, value):
        self._visa.write(f"INITIATE:{self._screen()}:CONTINUOUS {value}")

    @property
    def points(self):
        """value (int): {155, 313, 625, ..., 30001}"""
        return int(self._visa.query(f"SENSE{self._screen()}:SWEEP:POINTS?"))

    @points.setter
    @validate
    def points(self, value):
        self._visa.write(f"SENSE{self._screen()}:SWEEP:POINTS {value}")

    @property
    def count(self):
        """value (int): 0 to 32767"""
        return int(self._visa.query(f"SENSE{self._screen()}:SWEEP:COUNT?"))

    @count.setter
    @validate
    def count(self, value):
        self._visa.write(f"SENSE{self._screen()}:SWEEP:COUNT {value}")
