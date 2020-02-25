"""Common definitions"""
from collections import namedtuple
import functools

IDN = namedtuple("IDN", ["manufacturer", "model", "serial_number", "firmware_version"])

FREQUENCY_UNITS = {0: "Hz", 3: "kHz", 6: "MHz", 9: "GHz"}

TIME_UNITS = {0: "s", 3: "ms", 6: "µs", 9: "ns"}

BOOLEAN = {"0": "OFF", "1": "ON"}


def get_idn(visa):
    """Get IDN"""
    idn = visa.query("*IDN?").strip(":\n").split(",")
    return IDN(*idn)


class CommandError(Exception):
    """Raised when CME bit of SESR is set"""


def validate(func):
    """Read the Command Error bit (CME) of the Event-Status Register (ESR)"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # pylint: disable=protected-access
        cme = 32
        self = args[0]
        self._visa.write("*CLS")
        self._visa.write("SYSTEM:ERROR:CLEAR:ALL")
        original_ese = int(self._visa.query("*ESE?"))
        self._visa.write(f"*ESE {cme}")
        result = func(*args, **kwargs)
        if bool(int(self._visa.query("*ESR?")) & cme):
            err_id, err_msg = self._visa.query("SYSTEM:ERROR?").split(",")
            err_id = int(err_id)
            err_msg = err_msg.strip('"\r')
            raise CommandError(err_msg)
        self._visa.write(f"*ESE {original_ese}")
        return result

    return wrapper


class RSBase:
    """Instrument base class

    Attributes:
        visa (pyvisa.resources.Resource): pyvisa resource
    """

    def __init__(self, visa):
        self._visa = visa

    def __setattr__(self, name, value):
        if hasattr(self, name) and isinstance(getattr(self, name), RSBase):
            raise AttributeError(f"can't set '{name}'")
        if hasattr(self.__class__, name):
            prop = getattr(self.__class__, name)
            try:
                prop.fset(self, value)
            except TypeError:
                raise AttributeError(f"can't set '{name}'") from None
        else:
            self.__dict__[name] = value

    def __repr__(self):
        raise NotImplementedError

    def __dir__(self):
        inst_attr = list(filter(lambda k: not k.startswith("_"), self.__dict__.keys()))
        cls_attr = list(filter(lambda k: not k.startswith("_"), dir(self.__class__)))
        return inst_attr + cls_attr

    def _screen(self):
        """Get the active screen"""
        return self._visa.query("DISPLAY:ACTIVE?")


class Subsystem(RSBase):
    """Base class for a specific measurement function

    Attributes:
        instr (Fsup)
    """

    _kind = "Instrument"

    def __init__(self, instr):
        super().__init__(instr._visa)
        self._instr = instr

    def __init_subclass__(cls, kind):
        cls._kind = kind

    def __get__(self, instance, owner=None):
        return self

    def __repr__(self):
        return f"<{self._instr.model} {self._kind}>"


def scale_frequency(value):
    """value (float): convert value to quantity"""
    exp = 0
    scaled = value
    while scaled >= 1.0 and exp < 9:
        exp += 3
        scaled = value / 10 ** exp
    unit = FREQUENCY_UNITS[exp]
    return f"{scaled} {unit}"


def scale_time(value):
    """value (float): convert value to quantity"""
    exp = 0
    scaled = value
    while scaled < 1.0 and exp < 12:
        exp += 3
        scaled = value * 10 ** exp
    unit = TIME_UNITS[exp]
    return f"{scaled} {unit}"
