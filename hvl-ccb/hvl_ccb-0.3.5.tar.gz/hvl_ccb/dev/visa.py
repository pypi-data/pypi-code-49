#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
import logging
import re
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
from typing import Callable, Type, Union, Optional

from bitstring import BitArray

from .base import SingleCommDevice
from ..comm import VisaCommunication, VisaCommunicationConfig
from ..configuration import configdataclass

Number = Union[int, float]


class VisaStatusPoller(Thread):
    """
    Thread to periodically poll the status byte of a VISA device.
    """

    def __init__(self, target: Callable, interval: float = 0.5, start_delay: float = 5):
        """
        Constructor of VisaStatusPoller.

        :param target: is the function that shall be called periodically
        :param interval: is the polling interval time in seconds
        :param start_delay: is the start delay time in seconds
        """
        super().__init__(target=target)
        self._interval = interval
        self._stop_request = False
        self._target = target
        self._start_delay = start_delay

    def run(self) -> None:
        """
        Threaded method.
        """

        if self._start_delay > 0:
            sleep(self._start_delay)

        while True:
            if self._stop_request:
                self._stop_request = False
                return

            self._target()

            sleep(self._interval)

    def stop(self) -> None:
        """
        Gracefully stop the poller.
        """

        self._stop_request = True
        self.join()


@configdataclass
class _VisaDeviceConfigBase:
    """
    Required VisaDeviceConfig keys, separated from the default ones to enable config
    extension by inheritance with required keys.
    """

    # NOTE: this class is unnecessary as there are no keys here; it's coded here only
    # to illustrate a solution; for detailed explanations of the issue see:
    # https://stackoverflow.com/questions/51575931/class-inheritance-in-python-3-7-dataclasses/
    pass


@configdataclass
class _VisaDeviceConfigDefaultsBase:

    spoll_interval: Number = 0.5
    """
    Seconds to wait between status polling.
    """

    spoll_start_delay: Number = 2
    """
    Seconds to delay the start of status polling.
    """

    def clean_values(self):
        if self.spoll_interval <= 0:
            raise ValueError("Polling interval needs to be positive.")

        if self.spoll_start_delay < 0:
            raise ValueError("Polling start delay needs to be non-negative.")


@configdataclass
class VisaDeviceConfig(_VisaDeviceConfigDefaultsBase, _VisaDeviceConfigBase):
    """
    Configdataclass for a VISA device.
    """

    pass


class VisaDevice(SingleCommDevice):
    """
    Device communicating over the VISA protocol using VisaCommunication.
    """

    def __init__(
        self,
        com: Union[VisaCommunication, VisaCommunicationConfig, dict],
        dev_config: Union[VisaDeviceConfig, dict, None] = None,
    ) -> None:

        super().__init__(com, dev_config)

        self._spoll_thread: Optional[VisaStatusPoller] = None

        self._notify_operation_complete: bool = False

    @staticmethod
    def default_com_cls() -> Type[VisaCommunication]:
        """
        Return the default communication protocol for this device type, which is
        VisaCommunication.

        :return: the VisaCommunication class
        """

        return VisaCommunication

    @staticmethod
    def config_cls():
        return VisaDeviceConfig

    def get_identification(self) -> str:
        """
        Queries `"*IDN?"` and returns the identification string of the connected device.

        :return: the identification string of the connected device
        """

        return self.com.query("*IDN?")

    def start(self) -> None:
        """
        Start the VisaDevice. Sets up the status poller and starts it.

        :return:
        """
        super().start()
        self._spoll_thread = VisaStatusPoller(
            interval=self.config.spoll_interval,
            start_delay=self.config.spoll_start_delay,
            target=self.spoll_handler,
        )
        self._spoll_thread.start()

    def stop(self) -> None:
        """
        Stop the VisaDevice. Stops the polling thread and closes the communication
        protocol.

        :return:
        """
        if self._spoll_thread:
            self._spoll_thread.stop()
        super().stop()

    def spoll_handler(self):
        """
        Reads the status byte and decodes it. The status byte STB is defined in
        IEEE 488.2. It provides a rough overview of the instrument status.

        :return:
        """
        stb = self.com.spoll()

        if stb:
            bits = BitArray(length=8, int=stb)
            bits.reverse()

            if bits[0]:
                # has no meaning, always zero
                pass

            if bits[1]:
                # has no meaning, always zero
                pass

            if bits[2]:
                # error queue contains new error
                logging.debug(f"Error bit set in STB: {stb}")
                self.get_error_queue()

            if bits[3]:
                # Questionable Status QUES summary bit
                logging.debug(f"Questionable status bit set in STB: {stb}")

            if bits[4]:
                # Output buffer holds data (RTO 1024), MAV bit (Message available)
                pass

            if bits[5]:
                # Event status byte ESB, summary of ESR register (RTO 1024)
                logging.debug(f"Operation status bit set in STB: {stb}")

                # read event status register
                esr = int(self.com.query("*ESR?"))
                esr_bits = BitArray(length=8, int=esr)
                esr_bits.reverse()

                if esr_bits[0]:
                    # Operation complete bit set. This bit is set on receipt of the
                    # command *OPC exactly when all previous commands have been
                    # executed.
                    logging.debug(f"Operation complete bit set in ESR: {esr}")
                    self._notify_operation_complete = True

            if bits[6]:
                # RQS/MSS bit (RTO 1024)
                pass

            if bits[7]:
                # Operation Status OPER summary bit
                pass

    def wait_operation_complete(self, timeout: Optional[float] = None) -> bool:
        """
        Waits for a operation complete event. Returns after timeout [s] has expired
        or the operation complete event has been caught.

        :param timeout: Time in seconds to wait for the event; `None` for no timeout.
        :return: True, if OPC event is caught, False if timeout expired
        """

        # reset event bit
        self._notify_operation_complete = False

        # compute timeout
        timeout_time = datetime.now() + timedelta(seconds=(timeout or 0))

        # wait until event is caught
        while not self._notify_operation_complete:
            sleep(0.01)
            if timeout is not None and datetime.now() > timeout_time:
                break

        # if event was caught, return true
        if self._notify_operation_complete:
            self._notify_operation_complete = False
            return True

        # if timeout expired, return false
        return False

    def get_error_queue(self) -> str:
        """
        Read out error queue and logs the error.

        :return: Error string
        """

        err_string = self.com.query("SYSTem:ERRor:ALL?")
        for error in re.findall("[^,]+,[^,]+", err_string):
            logging.error(f"VISA Error from Device: {error}")
        return err_string

    def reset(self) -> None:
        """
        Send `"*RST"` and `"*CLS"` to the device. Typically sets a defined state.
        """

        self.com.write("*RST", "*CLS")
