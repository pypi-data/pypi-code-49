#
#    Copyright (c) 2015 Garret Hayes <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
"""Device nimbusdrivers for the weewx weather system."""

METRIC = 'METRIC'
US = 'ENGLISH'


class ViolatedPrecondition(StandardError):
    """Exception thrown when a function is called with violated preconditions."""


class WeeWxIOError(IOError):
    """Base class of exceptions thrown when encountering an I/O error with the console."""


class WakeupError(WeeWxIOError):
    """Exception thrown when unable to wake up or initially connect with the console"""


class CRCError(WeeWxIOError):
    """Exception thrown when unable to pass a CRC check."""


class RetriesExceeded(WeeWxIOError):
    """Exception thrown when max retries exceeded."""


class HardwareError(StandardError):
    """Exception thrown when an error is detected in the hardware."""


class UnknownArchiveType(HardwareError):
    """Exception thrown after reading an unrecognized archive type."""


class UnsupportedFeature(StandardError):
    """Exception thrown when attempting to access a feature that is not supported (yet)."""


class AbstractDevice(object):
    """Device nimbusdrivers should inherit from this class."""

    @property
    def hardware_name(self):
        raise NotImplementedError("Property 'hardware_name' not implemented")

    @property
    def archive_interval(self):
        raise NotImplementedError("Property 'archive_interval' not implemented")

    def genStartupRecords(self):
        raise NotImplementedError("Method 'genStartupRecords' not implemented")

    def genLoopPackets(self):
        raise NotImplementedError("Method 'genLoopPackets' not implemented")

    def getTime(self):
        raise NotImplementedError("Method 'getTime' not implemented")

    def setTime(self):
        raise NotImplementedError("Method 'setTime' not implemented")

    def closePort(self):
        pass

    def clearMemory(self):
        raise NotImplementedError("Method 'clearMemory' not implemented")


def get_driver_info():
    """Scan the nimbusdrivers folder, extracting information about each available
    driver. Return as a dictionary, keyed by the driver module name.

    Valid nimbusdrivers must be importable, and must have attribute "DRIVER_NAME"
    defined.
    """

    driver_info_dict = {
        'Vantage': {'module_name': 'nimbusdrivers.vantage',
                    'driver_name': 'Vantage'},
        'Simulator': {'module_name': 'nimbusdrivers.simulator',
                      'driver_name': 'Simulator'}
    }

    return driver_info_dict


def to_bool(x):
    """Convert an object to boolean.

    Examples:
    >>> print to_bool('TRUE')
    True
    >>> print to_bool(True)
    True
    >>> print tobool(1)
    True
    >>> print to_bool('FALSE')
    False
    >>> print to_bool(False)
    False
    >>> print to_bool(0)
    False
    >>> print to_bool('Foo')
    Traceback (most recent call last):
    ValueError: Unknown boolean specifier: 'Foo'.
    >>> print to_bool(None)
    Traceback (most recent call last):
    ValueError: Unknown boolean specifier: 'None'.
    """

    try:
        if x.lower() in ['true', 'yes']:
            return True
        elif x.lower() in ['false', 'no']:
            return False
    except AttributeError:
        pass
    try:
        return bool(int(x))
    except (ValueError, TypeError):
        pass
    raise ValueError("Unknown boolean specifier: '%s'." % x)
