"""Bandwidth subsystem"""
from rsfsup.common import Subsystem, scale_frequency


class Bandwidth(Subsystem, kind="BW"):
    """Bandwidth subsystem

    Attributes:
        instr (Fsup)
    """

    def __init__(self, instr):
        super().__init__(instr)
        # For now, adjust resolution and video bandwidths automatically according to
        # the span.
        self._visa.write("BANDWIDTH:RESOLUTION:AUTO ON")
        self._visa.write("BANDWIDTH:RESOLUTION:TYPE NORMAL")
        self._visa.write("BANDWIDTH:VIDEO:AUTO ON")

    @property
    def resolution_bandwidth(self):
        """(str): 10 Hz to 50 MHz"""
        value = self._visa.query(f"SENSE{self._screen()}:BANDWIDTH:RESOLUTION?")
        return scale_frequency(float(value))

    @property
    def video_bandwidth(self):
        """(str): 1 Hz to 10 MHz"""
        value = self._visa.query(f"SENSE:{self._screen()}:BANDWIDTH:VIDEO?")
        return scale_frequency(float(value))
