"""Marker subsystem"""
from rsfsup.common import Subsystem, validate, BOOLEAN, scale_frequency


class Marker(Subsystem, kind="Marker"):
    """A marker

    Attributes:
        instr (Fsup)
        num (int): marker number {1, 2, 3, 4}
    """

    def __init__(self, instr, num):
        super().__init__(instr)
        self._num = num
        self._name = f"marker_{num}"

    @property
    def state(self):
        """(str): {ON, OFF}"""
        result = self._visa.query(f"CALC{self._screen()}:MARK{self._num}:STATE?")
        return BOOLEAN.get(result, result)

    @state.setter
    @validate
    def state(self, value):
        self._visa.write(f"CALC{self._screen()}:MARK{self._num}:STATE {value}")

    @property
    def count(self):
        """value (str): frequency counter for marker 1 {ON, OFF}"""
        if self._num != 1:
            raise ValueError("Frequency counter only available on marker 1")
        result = self._visa.query(f"CALC{self._screen()}:MARK:COUNT?")
        return BOOLEAN.get(result, result)

    @count.setter
    @validate
    def count(self, value):
        if self._num != 1:
            raise ValueError("Frequency counter only available on marker 1")
        self._visa.write(f"CALC{self._screen()}:MARK:COUNT {value}")

    @property
    def frequency(self):
        """(str): measured frequency at marker 1"""
        value = float(self._visa.query(f"CALC{self._screen()}:MARK:COUNT:FREQUENCY?"))
        return scale_frequency(value)

    @property
    def resolution(self):
        """value (int or str): frequency counter resolution {0.1, 1, 10, ..., 10000} Hz"""
        value = float(self._visa.query(f"CALC{self._screen()}:MARK:COUNT:RESOLUTION?"))
        return scale_frequency(value)

    @resolution.setter
    @validate
    def resolution(self, value):
        self._visa.write(f"CALC{self._screen()}:MARK:COUNT:RESOLUTION {value}")

    @property
    def X(self):
        """value (int or str): 0 to f_max Hz"""
        value = float(self._visa.query(f"CALC{self._screen()}:MARK{self._num}:X?"))
        return scale_frequency(value)

    @X.setter
    @validate
    def X(self, value):
        self._visa.write(f"CALC{self._screen()}:MARK{self._num}:X {value}")

    @property
    def Y(self):
        """(str): level in dBm"""
        # change to single sweep, complete acquisition, measure power
        continuous = self._visa.query(f"INIT{self._screen()}:CONT?")
        original_continuous = BOOLEAN.get(continuous, continuous)
        state = self._visa.query(f"CALC{self._screen()}:MARK{self._num}:STATE?")
        original_state = BOOLEAN.get(state, state)
        original_timeout = self._visa.timeout
        sweep_time = float(self._visa.query(f"SENSE{self._screen()}:SWEEP:TIME?"))  # s
        self._visa.timeout = original_timeout + 1000 * sweep_time
        self._visa.write(f"INIT{self._screen()}:CONT OFF")
        self._visa.write(f"CALC{self._screen()}:MARK{self._num}:STATE ON")
        self._visa.write(f"INIT{self._screen()};*WAI")
        self._visa.timeout = original_timeout
        value = self._visa.query(f"CALC{self._screen()}:MARK{self._num}:Y?")
        self._visa.write(f"CALC{self._screen()}:MARK{self._num}:STATE {original_state}")
        self._visa.write(f"INIT{self._screen()}:CONT {original_continuous}")
        return f"{value} dBm"

    def move_to(self, location="PEAK"):
        """location (str): {PEAK, NEXT PEAK, NEXT PEAK RIGHT, NEXT PEAK LEFT}"""
        prefix = f"CALC{self._screen()}:MARK{self._num}:MAX"
        if location == "NEXT PEAK":
            suffix = "NEXT"
        elif location.endswith("RIGHT"):
            suffix = "RIGHT"
        elif location.endswith("LEFT"):
            suffix = "LEFT"
        else:
            suffix = "PEAK"
        self._visa.write(f"{prefix}:{suffix}")


class DeltaMarker(Subsystem, kind="Deltamarker"):
    """Deltamarker

    Attributes:
        instr (Fsup)
        num (int): deltamarker number {1, 2, 3, 4}
    """

    def __init__(self, instr, num):
        super().__init__(instr)
        self._num = num
        self._name = f"deltamarker_{num}"

    @property
    def state(self):
        """(str): {ON, OFF}"""
        result = self._visa.query(f"CALC{self._screen()}:DELT{self._num}?")
        return BOOLEAN.get(result, result)

    @state.setter
    @validate
    def state(self, value):
        self._visa.write(f"CALC{self._screen()}:DELT{self._num}:STATE {value}")

    @property
    def X(self):
        """value (int or str): 0 to f_max Hz"""
        value = float(self._visa.query(f"CALC{self._screen()}:DELT{self._num}:X?"))
        return scale_frequency(value)

    @property
    def Y(self):
        """(str): level in dBm"""
        # change to single sweep, complete acquisition, measure power
        continuous = self._visa.query(f"INIT{self._screen()}:CONT?")
        original_continuous = BOOLEAN.get(continuous, continuous)
        state = self._visa.query(f"CALC{self._screen()}:DELT{self._num}:STATE?")
        original_state = BOOLEAN.get(state, state)
        original_timeout = self._visa.timeout
        sweep_time = float(self._visa.query(f"SENSE{self._screen()}:SWEEP:TIME?"))  # s
        self._visa.timeout = original_timeout + 1000 * sweep_time
        self._visa.write(f"INIT{self._screen()}:CONT OFF")
        self._visa.write(f"CALC{self._screen()}:DELT{self._num}:STATE ON")
        self._visa.write(f"INIT{self._screen()};*WAI")
        self._visa.timeout = original_timeout
        value = self._visa.query(f"CALC{self._screen()}:DELT{self._num}:Y?")
        self._visa.write(f"CALC{self._screen()}:DELT{self._num}:STATE {original_state}")
        self._visa.write(f"INIT{self._screen()}:CONT {original_continuous}")
        return f"{value} dBm"

    def move_to(self, location="PEAK"):
        """location (str): {PEAK, NEXT PEAK, NEXT PEAK RIGHT, NEXT PEAK LEFT}"""
        prefix = f"CALC{self._screen()}:DELT{self._num}:MAX"
        if location == "NEXT PEAK":
            suffix = "NEXT"
        elif location.endswith("RIGHT"):
            suffix = "RIGHT"
        elif location.endswith("LEFT"):
            suffix = "LEFT"
        else:
            suffix = "PEAK"
        self._visa.write(f"{prefix}:{suffix}")
