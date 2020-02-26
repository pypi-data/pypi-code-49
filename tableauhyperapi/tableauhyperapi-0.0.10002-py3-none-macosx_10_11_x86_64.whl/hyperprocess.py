# -----------------------------------------------------------------------------
#
# This file is the copyrighted property of Tableau Software and is protected
# by registered patents and other applicable U.S. and international laws and
# regulations.
#
# Unlicensed use of the contents of this file is prohibited. Please refer to
# the NOTICES.txt file for further details.
#
# -----------------------------------------------------------------------------
import enum
import warnings

from pathlib import Path
from typing import Mapping, Union

from .endpoint import Endpoint
from .warning import UnclosedObjectWarning
from .impl import hapi
from .impl.dll import ffi
from .impl.dllutil import Error, Parameters, InteropUtil


class Telemetry(enum.Enum):
    """ Constants which define whether usage data is sent to Tableau to improve the Hyper API. """

    DO_NOT_SEND_USAGE_DATA_TO_TABLEAU = hapi.HYPER_DISABLE_TELEMETRY
    """ Do not share usage data with Tableau. """

    SEND_USAGE_DATA_TO_TABLEAU = hapi.HYPER_ENABLE_TELEMETRY
    """ Help us improve the Hyper API by sharing usage data with Tableau. """


class HyperProcess:
    """
    Starts a local Hyper server instance managed by the library.

    :param telemetry: :any:`Telemetry` constant which defines whether telemetry should be enabled.
    :param user_agent: arbitrary string which identifies the application. May be left unspecified.
    :param hyper_path: path to the directory which contains hyperd executable. If not specified, the library will
        try to locate it in pre-determined places.
    :param parameters: optional dictionary of additional startup parameters.

    Example usage:

    .. testsetup:: HyperProcess.__init__

        import os
        if os.path.exists('mydb.hyper'):
            os.remove('mydb.hyper')
        from tableauhyperapi import *

    .. testcode:: HyperProcess.__init__

        with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU, 'myapp') as hyper:
            with Connection(hyper.endpoint, 'mydb.hyper', CreateMode.CREATE) as connection:
                # ...
                pass

    .. testcleanup:: HyperProcess.__init__

        os.remove('mydb.hyper')

    The server must be stopped either implicitly by a ``with`` statement, or explicitly by the :any:`close()` or
    :any:`shutdown()` method. Even if it's not stopped, the server will be terminated when the process exits.
    You cannot use tableauhyperapi to start the server and let it stay running after the script exits.
    """

    def __init__(self, telemetry: Telemetry, user_agent: str = "",
                 hyper_path: Union[str, Path] = None,
                 parameters: Mapping[str, str] = None):
        self.__cdata = None

        native_params = Parameters.create_instance_parameters()
        if parameters:
            for key, value in parameters.items():
                native_params.set_value(key, value)

        self.__user_agent = user_agent

        if isinstance(hyper_path, Path):
            hyper_path = str(hyper_path)

        pp = ffi.new('hyper_instance_t**')
        Error.check(hapi.hyper_instance_create(InteropUtil.string_to_char_p(hyper_path),
                                               telemetry == Telemetry.SEND_USAGE_DATA_TO_TABLEAU,
                                               native_params.cdata, pp))
        self.__cdata = pp[0]

    @property
    def _cdata(self):
        return self.__cdata

    @property
    def is_open(self) -> bool:
        """ Returns true if the server has not been shut down yet. """
        return self.__cdata is not None

    def close(self):
        """ Stops the server, ignoring possible errors. This is called automatically when ``with`` statement is used.
        Use :any:`shutdown()` instead of :any:`close()` to get the shutdown errors as a :any:`HyperException`. """
        if self.__cdata is not None:
            try:
                hapi.hyper_instance_close(self.__cdata)
            finally:
                self.__cdata = None

    def shutdown(self, timeout_ms: int = -1):
        """ Stops the server. If the server could not be stopped, if it exited with an error or if the hyper process
        already exited with an non-zero exit code, a :any:`HyperException` is raised.

        :param timeout_ms: if positive, forcefully terminate the hyper process if it didn't shutdown after
            `timeout_ms` milliseconds.
        """
        if self.__cdata is not None:
            try:
                Error.check(hapi.hyper_instance_shutdown(self.__cdata, timeout_ms))
            finally:
                self.__cdata = None

    @property
    def endpoint(self) -> Endpoint:
        """
        Endpoint of this process to connect to.
        """
        if self.__cdata is None:
            raise RuntimeError('Server is closed')
        descriptor = InteropUtil.char_p_to_string(hapi.hyper_instance_get_endpoint_descriptor(self.__cdata))
        endpoint = Endpoint(descriptor, self.__user_agent)
        return endpoint

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        if self.__cdata is not None:
            warnings.warn('Server has not been stopped. Use Server object in a with statement or call its close() or '
                          'shutdown() method when done.', UnclosedObjectWarning)
            self.close()
