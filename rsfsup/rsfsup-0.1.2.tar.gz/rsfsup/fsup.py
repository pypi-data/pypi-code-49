"""Fsup class"""
from datetime import datetime
import numpy as np
from unyt import unyt_quantity, unyt_array
from rsfsup.common import RSBase, get_idn, validate
from rsfsup.display import Display
from rsfsup.frequency import Frequency
from rsfsup.amplitude import Amplitude
from rsfsup.bandwidth import Bandwidth
from rsfsup.sweep import Sweep
from rsfsup.markers import Marker, DeltaMarker
from rsfsup.traces import Trace


class Fsup(RSBase):
    """Fsup class

    Attributes:
        visa (pyvisa.resources.Resource): pyvisa resource
    """

    _modes = {"SAN": "SPECTRUM", "PNO": "SSA"}
    _options = {
        "B4": "Low-aging OCXO",
        "B10": "External Generator Control",
        "B18": "Removable Hard Disk",
        "B19": "Second Hard Disk",
        "B21": "LO/IF Ports for External Mixers",
        "B23": "20 dB Preamplifier",
        "B25": "Electronic Attenuator",
        "B28": "Trigger Port",
        "B60": "Low Phase Noise",
        "B61": "Correlation Extension",
        "K5": "GSM/EDGE",
        "K8": "Bluetooth",
        "K9": "Power Sensor Measurements",
        "K30": "Noise Figure and Gain Measurements",
        "K70": "Vector Signal Analysis",
    }

    def __init__(self, visa):
        super().__init__(visa)
        self._visa.write("*CLS")
        self._visa.write("SYSTEM:ERROR:CLEAR:ALL")
        self._visa.write("ESE 255")
        self._visa.write("FORMAT ASCII")
        self._idn = get_idn(visa)
        self.display = Display(self)
        self.frequency = Frequency(self)
        self.amplitude = Amplitude(self)
        self.bandwidth = Bandwidth(self)
        self.sweep = Sweep(self)
        self._markers = [Marker(self, num) for num in range(1, 5)]
        self._deltamarkers = [DeltaMarker(self, num) for num in range(1, 5)]
        self._traces = [Trace(self, 1)]

    @property
    def model(self):
        """(str): the model number"""
        return self._idn.model

    @property
    def serial_number(self):
        """(str): the serial number"""
        return self._idn.serial_number

    @property
    def firmware_version(self):
        """(str): the firmware version"""
        return self._idn.firmware_version

    @property
    def mode(self):
        """(str): {SPECTRUM, SSA}"""
        result = self._visa.query("INSTRUMENT?")
        return Fsup._modes.get(result, result)

    @mode.setter
    @validate
    def mode(self, value):
        modes = dict((v, k) for k, v in Fsup._modes.items())
        try:
            value = modes[value]
        except KeyError:
            raise ValueError(f"{value} not a valid mode") from None
        self._visa.write(f"INSTRUMENT:SELECT {value}")

    def reset(self):
        """Reset the instrument to the factory default settings"""
        self._visa.write("*RST")

    def set_clock(self):
        """Set the date and time to local machine's time"""
        self._visa.write(f"SYSTEM:DATE {datetime.now().strftime('%Y,%m,%d')}")
        self._visa.write(f"SYSTEM:TIME {datetime.now().strftime('%H,%M,%S')}")

    def lock_frontpanel(self):
        """Lock the front panel"""
        self._visa.write("SYSTEM:DISPLAY:FPANEL OFF")
        self._visa.write("SYSTEM:KLOCK ON")

    def unlock_frontpanel(self):
        """Unlock the front panel"""
        self._visa.write("SYSTEM:KLOCK OFF")
        self._visa.write("SYSTEM:DISPLAY:FPANEL ON")

    @property
    def options(self):
        """List the installed options"""
        codes = self._visa.query("*OPT?").split(",")
        installed_codes = [code for code in codes if not code.startswith("0")]
        return [Fsup._options.get(code, code) for code in installed_codes]

    @property
    def impedance(self):
        """value (int): RF input impedance {50, 75} Ω"""
        return int(self._visa.query("INPUT:IMPEDANCE?"))

    @impedance.setter
    @validate
    def impedance(self, value):
        self._visa.write(f"INPUT:IMPEDANCE {value}")

    def turnoff_markers(self):
        """Turn off all markers in the active screen"""
        for marker in self._markers + self._deltamarkers:
            marker.state = "OFF"

    def reference_fixed(self, state="ON"):
        """state (str): {ON, OFF}
            Turn on markers 1 and 2, if necessary, and set markers 2 to 4 as delta
            markers fixed to marker 1
        """
        self.enable_marker(1)
        self.enable_marker(2, as_delta=True)
        self._visa.write(f"CALC{self._screen()}:DELT2:FUNC:FIX {state}")

    def enable_marker(self, num, as_delta=False):
        """num (int): marker/deltamarker number {1, 2, 3, 4}
        as_delta (bool): True if deltamarker"""
        i = num - 1
        marker = self._markers[i]
        deltamarker = self._deltamarkers[i]
        # pylint: disable=protected-access
        if as_delta:
            deltamarker.state = "ON"
            try:
                setattr(self, deltamarker._name, deltamarker)
            except AttributeError:
                pass
            marker.state = "OFF"
            try:
                delattr(self, marker._name)
            except AttributeError:
                pass
        else:
            deltamarker.state = "OFF"
            try:
                delattr(self, deltamarker._name)
            except AttributeError:
                pass
            marker.state = "ON"
            try:
                setattr(self, marker._name, marker)
            except AttributeError:
                pass

    def clear_traces(self):
        """Clear all traces"""
        self._visa.write(f"DISP:WIND{self._screen()}:TRACE:CLEAR")

    def read(self, trace=1):
        """Read trace data and return tuple (X, Y)

        Parameters:
            trace (int): {1, 2, 3}
        """
        num = self.sweep.points
        start_str = self.frequency.start
        value, unit = start_str.split(" ")
        start = unyt_quantity(float(value), unit)
        stop_str = self.frequency.stop
        value, unit = stop_str.split(" ")
        stop = unyt_quantity(float(value), unit)
        x = np.linspace(start, stop, num=num, endpoint=True)
        x.name = "$f$"
        i = trace - 1
        data = self._traces[i].data
        unit = self._traces[i].y_unit
        y = unyt_array(data, unit)
        y.name = "$A$"
        return (x, y)

    def __dir__(self):
        for marker in self._markers + self._deltamarkers:
            if marker.state == "OFF":
                try:
                    delattr(self, marker._name)
                except AttributeError:
                    pass
        return super().__dir__()

    def __repr__(self):
        return f"<R&S {self.model} at {self._visa.resource_name}>"
