import warnings

from sys import version_info

if version_info.major < 3 or version_info.major == 3 and version_info.minor < 6:
    msg = "The '%s' package is not tested with your Python version. " % __name__
    msg += "Please consider upgrading to the latest Python distribution."
    warnings.warn(msg)
