"""Traces subsystem"""
from rsfsup.common import Subsystem, validate


class Trace(Subsystem, kind="Trace"):
    """Trace subsystem

    Attributes:
        instr (Fsup)
        num (int): trace number {1, 2, 3}
    """

    def __init__(self, instr, num):
        super().__init__(instr)
        self._num = num

    @property
    def mode(self):
        """value (str): {WRITE, AVERAGE, MAXHOLD, MINHOLD}"""
        return self._visa.query(f"DISP:WIND{self._screen()}:TRAC{self._num}:MODE?")

    @mode.setter
    @validate
    def mode(self, value):
        self._visa.write(f"DISP:WIND{self._screen()}:TRAC{self._num}:MODE {value}")

    @property
    def state(self):
        """value (str): {ON , OFF}"""
        return self._visa.query(f"DISP:WIND{self._screen()}:TRAC{self._num}:STATE?")

    @state.setter
    @validate
    def state(self, value):
        self._visa.write(f"DISP:WIND{self._screen()}:TRAC{self._num}:STATE {value}")

    @property
    def y_unit(self):
        """(str) Y axis unit"""
        result = self._visa.query(f"DISP:WIND{self._screen()}:TRAC:Y:UNIT?")
        power_units = {"DBM": "dBm", "WATT": "W", "DB": "dB"}
        return power_units.get(result, result)

    @property
    def data(self):
        """(list of float): Y axis values in y_unit with length sweep points"""
        return self._visa.query_ascii_values(f"TRAC{self._screen()}? TRACE{self._num}")
