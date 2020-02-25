"""RSFSUP - an interface to the Rohde&Schwarz FSUP Signal Source Analyzer

Basic usage to plot the spectrum:
>>> from rsfsup import CommChannel
>>> with CommChannel("<ip address>") as fsup:
...     spectrum = fsup.read()
...
>>> import matplotlib.pyplot as plt
>>> plt.plot(*spectrum)
[<matplotlib.lines.Line2D object at ...>]
>>> plt.show()
"""
import pyvisa
from unyt import define_unit, matplotlib_support
from rsfsup.common import get_idn
from rsfsup.fsup import Fsup
from rsfsup.version import __version__

__all__ = ["CommChannel"]

define_unit("dBm", (1.0, "dB"))
matplotlib_support()
matplotlib_support.label_style = "/"


class CommChannel:
    """Connect to a R&S FSUP using VISA

    Attributes:
        address (str): instrument's TCPIP address or host name

    Returns:
        CommChannel or Fsup
    """

    def __init__(self, address):
        self._address = address
        self._rm = pyvisa.ResourceManager()
        self._visa = self._rm.open_resource(f"TCPIP::{address}")
        self._visa.read_termination = "\n"

    def __enter__(self):
        self._visa.write("*CLS")
        idn = get_idn(self._visa)
        if idn.manufacturer != "Rohde&Schwarz" and not idn.model.startswith("FSUP"):
            raise ValueError(f"Device at {self._address} is a not a R&S FSUP")
        self._visa.write("SYSTEM:DISPLAY:UPDATE ON")
        self._visa.write("SYSTEM:DISPLAY:FPANEL ON")
        return Fsup(self._visa)

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._visa.write("SYSTEM:DISPLAY:FPANEL ON")
        self._visa.write("SYSTEM:KLOCK OFF")
        self._visa.close()
        self._rm.close()

    def get_instrument(self):
        """Return the Fsup instrument object"""
        return self.__enter__()

    def close(self):
        """Close the CommChannel"""
        self.__exit__(None, None, None)


def __dir__():
    return ["CommChannel", "__version__"]
