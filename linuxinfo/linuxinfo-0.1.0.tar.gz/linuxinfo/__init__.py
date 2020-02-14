try:
    from importlib_metadata import version # type: ignore
except ImportError:
    from importlib.metadata import version # type: ignore

# from .rpi import pi_info, RPiInfo, decode
from .rpi import pi_info, RPiInfo
from .linux import linux_info, LinuxInfo


__author__ = "Kevin J. Walchko"
__license__ = "MIT"
__version__ = version("linuxinfo")
