import warnings

from sys import version_info as python_version

from .info import VERSION

if python_version.major < 3 or python_version.major == 3 and python_version.minor < 6:
    msg = "The '%s' package is not tested with your Python version. " % __name__
    msg += "Please consider upgrading to the latest Python distribution."
    warnings.warn(msg)

__version__ = VERSION
