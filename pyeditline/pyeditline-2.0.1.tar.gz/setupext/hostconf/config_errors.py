"""
Defining custom exception and error types for the `configure` process

"""

import os

class ConfigureError(Exception):
    """Signal a fault in the configuration process.

    Args:
        message:  the message to pass up to the user

    """

    def __init__(self, message):
        msg = os.linesep + os.linesep
        msg += '*' * 60 + os.linesep
        msg += message + os.linesep
        msg += '*' * 60 + os.linesep
        super().__init__(msg)


class ConfigureSystemLibraryError(ConfigureError):
    """System libraries do not contain adequate support.

    Args:
        fcn: name of function being checked
        test_libs:  additional libraries inspected

    Notes:
        It is assumed that the default `system` libraries are also checked.

    """

    def __init__(self, fcn, test_libs):
        msg = "Must have '{0}' in one of:".format(fcn) + os.linesep
        msg += "  " + ', '.join(test_libs) + os.linesep
        msg += "Please install one of these system libraries on your platform."
        super().__init__(msg)


class ConfigureSystemHeaderFileError(ConfigureError):
    """System C-header files are not present

    Args:
        headers: list of headers
        selection:  string indicating request (default: 'one of')

    """

    def __init__(self, headers, selection='one of'):
        msg = 'Must have ' + selection + os.linesep
        msg += '  ' + ', '.join(headers) + os.linesep
        msg += 'Please install a (development) package containing one.'
        super().__init__(msg)
