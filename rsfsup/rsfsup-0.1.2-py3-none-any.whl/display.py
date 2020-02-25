"""Display subsystem"""
from rsfsup.common import Subsystem, validate


class Display(Subsystem, kind="Display"):
    """Display subsystem

    Attributes:
        instr (Fsup)
    """

    _formats = {"SING": "FULL SCREEN", "SPL": "SPLIT SCREEN"}
    _windows = {"1": "SCREEN A", "2": "SCREEN B"}
    _couplings = {
        "NONE": "NONE",
        "RLEVEL": "REF LEVEL",
        "CF_B": "CENTER B = MARKER A",
        "CF_A": "CENTER A = MARKER B",
    }

    def __init__(self, instr):
        super().__init__(instr)
        self._coupling = "NONE"
        self._visa.write(f"INSTRUMENT:COUPLE {self._coupling}")
        self._psave_holdoff = 0
        self._visa.write(f"DISPLAY:PSAVE:STATE OFF")

    @property
    def format(self):
        """value (str): {FULL SCREEN, SPLIT SCREEN}"""
        result = self._visa.query("DISPLAY:FORMAT?")
        return Display._formats.get(result, result)

    @format.setter
    @validate
    def format(self, value):
        formats = dict((v, k) for k, v in Display._formats.items())
        value = formats.get(value, value)
        self._visa.write(f"DISPLAY:FORMAT {value}")

    @property
    def screen(self):
        """value (str): {SCREEN A, SCREEN B}"""
        result = self._visa.query("DISPLAY:ACTIVE?")
        return Display._windows.get(result, result)

    @screen.setter
    @validate
    def screen(self, value):
        windows = dict((v, k) for k, v in Display._windows.items())
        try:
            value = windows[value]
        except KeyError:
            raise ValueError(f"{value} not a valid screen")
        self._visa.write(f"DISPLAY:WINDOW{value}:SELECT")

    def set_title(self, text=""):
        """text (str): active screen title up to 20 characters"""
        num = self._visa.query("DISPLAY:ACTIVE?")
        if text == "":
            self._visa.write(f"DISPLAY:WINDOW{num}:TEXT:STATE OFF")
        else:
            self._visa.write(f"DISPLAY:WINDOW{num}:TEXT:DATA '{text[:20]}'")
            self._visa.write(f"DISPLAY:WINDOW{num}:TEXT:STATE ON")

    @property
    def coupling(self):
        """value (str): {NONE, REF LEVEL, CENTER B = MARKER A, CENTER A = MARKER A}"""
        return self._coupling

    @coupling.setter
    @validate
    def coupling(self, value):
        couplings = dict((v, k) for k, v in Display._couplings.items())
        try:
            value = couplings[value]
        except KeyError:
            raise ValueError(f"{value} not a valid coupling")
        self._visa.write(f"INSTRUMENT:COUPLE {value}")

    @property
    def pwr_save(self):
        """value (int): screen-saver timeout in minutes (1 to 60), 0 disables pwr save"""
        return self._psave_holdoff

    @pwr_save.setter
    @validate
    def pwr_save(self, value):
        self._psave_holdoff = value
        if value:
            self._visa.write(f"DISPLAY:PSAVE:HOLDOFF {value}")
            self._visa.write("DISPLAY:PSAVE:STATE ON")
        else:
            self._visa.write("DISPLAY:PSAVE:STATE OFF")
