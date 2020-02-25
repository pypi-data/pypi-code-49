"""Frequency subsystem"""
from rsfsup.common import Subsystem, scale_frequency, validate
from rsfsup.markers import Marker


class Frequency(Subsystem, kind="FREQ"):
    """Frequency subsystem

    Attributes:
        instr (Fsup)
    """

    @property
    def center(self):
        """value (int or str):
            0 to f_max in hertz
            string such as '1 GHz'
            keyword such as 'UP' or 'DOWN'
            Marker
        """
        value = float(self._visa.query(f"SENSE{self._screen()}:FREQUENCY:CENTER?"))
        return scale_frequency(value)

    @center.setter
    @validate
    def center(self, value):
        if isinstance(value, Marker):
            # Set the center frequency and step size to the marker frequency
            # pylint: disable=protected-access
            marker = value
            self._visa.write(f"CALC{self._screen()}:MARK{marker._num}:FUNC:CENTER")
            self._visa.write(f"CALC{self._screen()}:MARK{marker._num}:FUNC:CSTEP")
        else:
            self._visa.write(f"SENSE{self._screen()}:FREQUENCY:CENTER {value}")

    @property
    def span(self):
        """value (int or str): 0 to f_max in hertz or string such as '100 MHz' or 'FULL'"""
        value = float(self._visa.query(f"SENSE{self._screen()}:FREQUENCY:SPAN?"))
        return scale_frequency(value)

    @span.setter
    @validate
    def span(self, value):
        if value == "FULL":
            self._visa.write(f"SENSE{self._screen()}:FREQUENCY:SPAN:FULL")
        else:
            self._visa.write(f"SENSE{self._screen()}:FREQUENCY:SPAN {value}")

    @property
    def start(self):
        """value (int or str): 0 to f_max in hertz or string such as '20 MHz'"""
        value = float(self._visa.query(f"SENSE{self._screen()}:FREQUENCY:START?"))
        return scale_frequency(value)

    @start.setter
    @validate
    def start(self, value):
        self._visa.write(f"SENSE{self._screen()}:FREQUENCY:START {value}")

    @property
    def stop(self):
        """value (int or str): 0 to f_max in hertz or string such as '20 MHz'"""
        value = float(self._visa.query(f"SENSE{self._screen()}:FREQUENCY:STOP?"))
        return scale_frequency(value)

    @stop.setter
    @validate
    def stop(self, value):
        self._visa.write(f"SENSE{self._screen()}:FREQUENCY:STOP {value}")

    @property
    def cf_step(self):
        """value (int or string): {f Hz, SPAN, CENTER, MARKER}"""
        value = float(self._visa.query(f"SENSE{self._screen()}:FREQ:CENT:STEP?"))
        return scale_frequency(value)

    @cf_step.setter
    @validate
    def cf_step(self, value):
        if value == "SPAN":
            self._visa.write(f"SENSE{self._screen()}:FREQ:CENT:STEP:LINK SPAN")
        elif value == "CENTER":
            cf = self.center
            self._visa.write(f"SENSE{self._screen()}:FREQ:CENT:STEP:LINK OFF")
            self._visa.write(f"SENSE{self._screen()}:FREQ:CENT:STEP {cf}")
        elif value == "MARKER":
            self._visa.write(f"CALCULATE{self._screen()}:MARKER:FUNCTION:CSTEP")
        else:
            self._visa.write(f"SENSE{self._screen()}:FREQ:CENT:STEP:LINK OFF")
            self._visa.write(f"SENSE{self._screen()}:FREQ:CENT:STEP {value}")
