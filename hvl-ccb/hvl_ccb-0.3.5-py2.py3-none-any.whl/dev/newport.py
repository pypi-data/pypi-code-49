#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Device class for Newport SMC100PP stepper motor controller with serial communication.

The SMC100PP is a single axis motion controller/driver for stepper motors up to 48 VDC
at 1.5 A rms. Up to 31 controllers can be networked through the internal RS-485
communication link.

Manufacturer homepage:
https://www.newport.com/f/smc100-single-axis-dc-or-stepper-motion-controller
"""

import logging
from time import sleep, time
from typing import Union, Dict, List

from aenum import Enum, IntEnum

from .base import SingleCommDevice
from ..comm import SerialCommunication, SerialCommunicationConfig
from ..comm.serial import (
    SerialCommunicationParity,
    SerialCommunicationStopbits,
    SerialCommunicationBytesize,
)
from ..configuration import configdataclass
from ..utils.enum import NameEnum, AutoNumberNameEnum

Param = Union[int, float, str, None]
Number = Union[int, float]


@configdataclass
class NewportSMC100PPSerialCommunicationConfig(SerialCommunicationConfig):
    #: Baudrate for Heinzinger power supplies is 9600 baud
    baudrate: int = 57600

    #: Heinzinger does not use parity
    parity: Union[str, SerialCommunicationParity] = SerialCommunicationParity.NONE

    #: Heinzinger uses one stop bit
    stopbits: Union[int, SerialCommunicationStopbits] = SerialCommunicationStopbits.ONE

    #: One byte is eight bits long
    bytesize: Union[
        int, SerialCommunicationBytesize
    ] = SerialCommunicationBytesize.EIGHTBITS

    #: The terminator is CR/LF
    terminator: bytes = b"\r\n"

    #: use 10 seconds timeout as default
    timeout: Number = 10


class NewportSMC100PPSerialCommunication(SerialCommunication):
    """
    Specific communication protocol implementation Heinzinger power supplies.
    Already predefines device-specific protocol parameters in config.
    """

    class ControllerErrors(Enum):
        """
        Possible controller errors with values as returned by the device in response
        to sent commands.
        """

        _init_ = "value message"

        NO_ERROR = "@", "No error."
        CODE_OR_ADDR_INVALID = (
            "A",
            "Unknown message code or floating point controller address.",
        )
        ADDR_INCORRECT = "B", "Controller address not correct."
        PARAM_MISSING_OR_INVALID = "C", "Parameter missing or out of range."
        CMD_NOT_ALLOWED = "D", "Command not allowed."
        HOME_STARTED = "E", "Home sequence already started."
        ESP_STAGE_NAME_INVALID = (
            "F",
            "ESP stage name unknown.",
        )
        DISPLACEMENT_OUT_OF_LIMIT = (
            "G",
            "Displacement out of limits.",
        )
        CMD_NOT_ALLOWED_NOT_REFERENCED = (
            "H",
            "Command not allowed in NOT REFERENCED state.",
        )
        CMD_NOT_ALLOWED_CONFIGURATION = (
            "I",
            "Command not allowed in CONFIGURATION state.",
        )
        CMD_NOT_ALLOWED_DISABLE = "J", "Command not allowed in DISABLE state."
        CMD_NOT_ALLOWED_READY = "K", "Command not allowed in READY state."
        CMD_NOT_ALLOWED_HOMING = "L", "Command not allowed in HOMING state."
        CMD_NOT_ALLOWED_MOVING = "M", "Command not allowed in MOVING state."
        POSITION_OUT_OF_LIMIT = "N", "Current position out of software limit."
        COM_TIMEOUT = (
            "S",
            "Communication Time Out.",
        )
        EEPROM_ACCESS_ERROR = "U", "Error during EEPROM access."
        CMD_EXEC_ERROR = "V", "Error during command execution."
        CMD_NOT_ALLOWED_PP = "W", "Command not allowed for PP version."
        CMD_NOT_ALLOWED_CC = "X", "Command not allowed for CC version."

    @staticmethod
    def config_cls():
        return NewportSMC100PPSerialCommunicationConfig

    def _send_command_unsafe(self, add: int, cmd: str, param: Param = None) -> None:
        """
        Send a command to the controller.

        :param add: the controller address (1 to 31)
        :param cmd: the command to be sent
        :param param: optional parameter (int/float/str) appended to the command
        """

        if param is None:
            param = ""

        self._write_text_unsafe(f"{add}{cmd}{param}")
        logging.debug(f"sent: {add}{cmd}{param}")

    def _query_unsafe(self, add: int, cmd: str, param: Param = None) -> str:
        """
        Send a command to the controller and read the answer. The prefix add+cmd is
        removed from the answer.

        :param add: the controller address (1 to 31)
        :param cmd: the command to be sent
        :param param: optional parameter (int/float/str) appended to the command
        :return: the answer from the device without the prefix
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if param is None:
            param = ""

        prefix = f"{add}{cmd}"
        query = f"{add}{cmd}{param}"

        self._send_command_unsafe(add, cmd, param)
        sleep(0.01)
        answer = self._read_text_unsafe().strip()
        if len(answer) == 0:
            message = f"Newport controller {add} did not answer to query {query}."
            logging.error(message)
            raise NewportSerialCommunicationError(message)
        elif not answer.startswith(prefix):
            message = (
                f"Newport controller {add} answer {answer} to query {query} "
                f"does not start with expected prefix {prefix}."
            )
            logging.error(message)
            raise NewportSerialCommunicationError(message)
        else:
            logging.debug(f"Newport com: {answer}")
            return answer[len(prefix):].strip()

    def _check_for_error_unsafe(self, add: int) -> None:
        """
        Ask the Newport controller for the last error it recorded. This should be done
        after every command or query.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        error = self.ControllerErrors(self._query_unsafe(add, "TE"))
        if error is not self.ControllerErrors.NO_ERROR:
            logging.error(f"NewportControllerError: {error.message}")
            raise NewportControllerError(error.message)

    def send_command(self, add: int, cmd: str, param: Param = None) -> None:
        """
        Send a command to the controller, and check for errors.

        :param add: the controller address (1 to 31)
        :param cmd: the command to be sent
        :param param: optional parameter (int/float/str) appended to the command
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if param is None:
            param = ""

        with self.access_lock:
            self._send_command_unsafe(add, cmd, param)
            self._check_for_error_unsafe(add)

    def send_stop(self, add: int) -> None:
        """
        Send the general stop ST command to the controller, and check for errors.

        :param add: the controller address (1 to 31)
        :return: ControllerErrors reported by Newport Controller
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        """

        with self.access_lock:
            self._write_text_unsafe("ST")
            self._check_for_error_unsafe(add)

    def query(self, add: int, cmd: str, param: Param = None) -> str:
        """
        Send a query to the controller, read the answer, and check for errors. The
        prefix add+cmd is removed from the answer.

        :param add: the controller address (1 to 31)
        :param cmd: the command to be sent
        :param param: optional parameter (int/float/str) appended to the command
        :return: the answer from the device without the prefix
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        with self.access_lock:

            try:
                answer = self._query_unsafe(add, cmd, param)
            finally:
                self._check_for_error_unsafe(add)

        return answer

    def query_multiple(self, add: int, cmd: str, prefixes: List[str]) -> List[str]:
        """
        Send a query to the controller, read the answers, and check for errors. The
        prefixes are removed from the answers.

        :param add: the controller address (1 to 31)
        :param cmd: the command to be sent
        :param prefixes: prefixes of each line expected in the answer
        :return: list of answers from the device without prefix
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        with self.access_lock:

            try:
                self._send_command_unsafe(add, cmd)
                answer = []
                for prefix in prefixes:
                    line = self._read_text_unsafe().strip()
                    if not line.startswith(prefix):
                        message = (
                            f"Newport controller {add} answer {line} to command "
                            f"{cmd} does not start with expected prefix {prefix}."
                        )
                        logging.error(message)
                        raise NewportSerialCommunicationError(message)
                    else:
                        answer.append(line[len(prefix):])
            finally:
                self._check_for_error_unsafe(add)

        return answer


class NewportConfigCommands(NameEnum):
    """
    Commands predefined by the communication protocol of the SMC100PP
    """

    AC = "acceleration"
    BA = "backlash_compensation"
    BH = "hysteresis_compensation"
    FRM = "micro_step_per_full_step_factor"
    FRS = "motion_distance_per_full_step"
    HT = "home_search_type"
    JR = "jerk_time"
    OH = "home_search_velocity"
    OT = "home_search_timeout"
    QIL = "peak_output_current_limit"
    SA = "rs485_address"
    SL = "negative_software_limit"
    SR = "positive_software_limit"
    VA = "velocity"
    VB = "base_velocity"
    ZX = "stage_configuration"


@configdataclass
class NewportSMC100PPConfig:
    """
    Configuration dataclass for the Newport motor controller SMC100PP.
    """

    class HomeSearch(IntEnum):
        """
        Different methods for the motor to search its home position during
        initialization.
        """

        HomeSwitch_and_Index = 0
        CurrentPosition = 1
        HomeSwitch = 2
        EndOfRunSwitch_and_Index = 3
        EndOfRunSwitch = 4

    class EspStageConfig(IntEnum):
        """
        Different configurations to check or not the motor configuration upon power-up.
        """

        DisableEspStageCheck = 1
        UpdateEspStageInfo = 2
        EnableEspStageCheck = 3

    # The following parameters are added for convenience, they do not correspond to any
    # actual hardware configuration:

    # controller address (1 to 31)
    address: int = 1

    # user position offset (mm). For convenience of the user, the motor
    # position is given relative to this point:
    user_position_offset: Number = 23.987

    # correction for the scaling between screw turns and distance (should be close to 1)
    screw_scaling: Number = 1

    # nr of seconds to wait after exit configuration command has been issued
    exit_configuration_wait_sec: Number = 5

    # extra wait time added to distant-dependent wait time of a move
    move_finished_extra_wait_sec: Number = 1

    # The following parameters are actual hardware configuration parameters:

    # acceleration (preset units/s^2)
    acceleration: Number = 10

    # backlash compensation (preset units)
    # either backlash compensation or hysteresis compensation can be used, not both.
    backlash_compensation: Number = 0

    # hysteresis compensation (preset units)
    # either backlash compensation or hysteresis compensation can be used, not both.
    hysteresis_compensation: Number = 0.015

    # micro step per full step factor, integer between 1 and 2000
    micro_step_per_full_step_factor: int = 100

    # motion distance per full step (preset units)
    motion_distance_per_full_step: Number = 0.01

    # home search type
    home_search_type: Union[int, HomeSearch] = HomeSearch.HomeSwitch

    # jerk time (s) -> time to reach the needed acceleration
    jerk_time: Number = 0.04

    # home search velocity (preset units/s)
    home_search_velocity: Number = 4

    # home search time-out (s)
    home_search_timeout: Number = 27.5

    # home search polling interval (s)
    home_search_polling_interval: Number = 1

    # peak output current delivered to the motor (A)
    peak_output_current_limit: Number = 0.4

    # RS485 address, integer between 2 and 31
    rs485_address: int = 2

    # lower limit for the motor position (mm)
    negative_software_limit: Number = -23.5

    # upper limit for the motor position (mm)
    positive_software_limit: Number = 25

    # maximum velocity (preset units/s), this is also the default velocity unless a
    # lower value is set
    velocity: Number = 4

    # profile generator base velocity (preset units/s)
    base_velocity: Number = 0

    # ESP stage configuration
    stage_configuration: Union[int, EspStageConfig] = EspStageConfig.EnableEspStageCheck

    def clean_values(self):
        if self.address not in range(1, 32):
            raise ValueError("Address should be an integer between 1 and 31.")
        if abs(self.screw_scaling - 1) > 0.1:
            raise ValueError("The screw scaling should be close to 1.")
        if not 0 < self.exit_configuration_wait_sec:
            raise ValueError(
                "The exit configuration wait time must be a positive "
                "value (in seconds)."
            )
        if not 0 < self.move_finished_extra_wait_sec:
            raise ValueError(
                "The extra wait time for move to finish must be a "
                "positive value (in seconds)."
            )
        if not 1e-6 < self.acceleration < 1e12:
            raise ValueError("The acceleration should be between 1e-6 and 1e12.")
        if not 0 <= self.backlash_compensation < 1e12:
            raise ValueError("The backlash compensation should be between 0 and 1e12.")
        if not 0 <= self.hysteresis_compensation < 1e12:
            raise ValueError(
                "The hysteresis compensation should be between " "0 and 1e12."
            )
        if (
            not isinstance(self.micro_step_per_full_step_factor, int)
            or not 1 <= self.micro_step_per_full_step_factor <= 2000
        ):
            raise ValueError(
                "The micro step per full step factor should be between 1 " "and 2000."
            )
        if not 1e-6 < self.motion_distance_per_full_step < 1e12:
            raise ValueError(
                "The motion distance per full step should be between 1e-6" " and 1e12."
            )
        if not isinstance(self.home_search_type, self.HomeSearch):
            self.force_value("home_search_type", self.HomeSearch(self.home_search_type))
        if not 1e-3 < self.jerk_time < 1e12:
            raise ValueError("The jerk time should be between 1e-3 and 1e12.")
        if not 1e-6 < self.home_search_velocity < 1e12:
            raise ValueError(
                "The home search velocity should be between 1e-6 " "and 1e12."
            )
        if not 1 < self.home_search_timeout < 1e3:
            raise ValueError("The home search timeout should be between 1 and 1e3.")
        if not 0 < self.home_search_polling_interval:
            raise ValueError(
                "The home search polling interval (sec) needs to have "
                "a positive value."
            )
        if not 0.05 <= self.peak_output_current_limit <= 3:
            raise ValueError(
                "The peak output current limit should be between 0.05 A" "and 3 A."
            )
        if self.rs485_address not in range(2, 32):
            raise ValueError("The RS485 address should be between 2 and 31.")
        if not -1e12 < self.negative_software_limit <= 0:
            raise ValueError(
                "The negative software limit should be between -1e12 " "and 0."
            )
        if not 0 <= self.positive_software_limit < 1e12:
            raise ValueError(
                "The positive software limit should be between 0 " "and 1e12."
            )
        if not 1e-6 < self.velocity < 1e12:
            raise ValueError("The velocity should be between 1e-6 and 1e12.")
        if not 0 <= self.base_velocity <= self.velocity:
            raise ValueError(
                "The base velocity should be between 0 and the maximum " "velocity."
            )
        if not isinstance(self.stage_configuration, self.EspStageConfig):
            self.force_value(
                "stage_configuration", self.EspStageConfig(self.stage_configuration)
            )

    def _build_motor_config(self) -> Dict[str, float]:
        return {
            param.value: float(getattr(self, param.value))
            for param in NewportConfigCommands  # type: ignore
        }

    @property
    def motor_config(self) -> Dict[str, float]:
        """
        Gather the configuration parameters of the motor into a dictionary.

        :return: dict containing the configuration parameters of the motor
        """

        if not hasattr(self, "_motor_config"):
            self.force_value(  # type: ignore
                "_motor_config", self._build_motor_config(),
            )
        return self._motor_config  # type: ignore

    def post_force_value(self, fieldname, value):
        # if motor config is already cached and field is one of config commands fields..
        if hasattr(self, "_motor_config") and fieldname in self._motor_config:
            # ..update directly config dict value
            self._motor_config[fieldname] = value


class NewportStates(AutoNumberNameEnum):
    """
    States of the Newport controller. Certain commands are allowed only in certain
    states.
    """

    NO_REF = ()
    HOMING = ()
    CONFIG = ()
    READY = ()
    MOVING = ()
    DISABLE = ()
    JOGGING = ()


class NewportSMC100PP(SingleCommDevice):
    """
    Device class of the Newport motor controller SMC100PP
    """

    States = NewportStates

    class MotorErrors(Enum):
        """
        Possible motor errors reported by the motor during get_state().
        """

        _init_ = "value message"

        OUTPUT_POWER_EXCEEDED = 2, "80W output power exceeded"
        DC_VOLTAGE_TOO_LOW = 3, "DC voltage too low"
        WRONG_ESP_STAGE = 4, "Wrong ESP stage"
        HOMING_TIMEOUT = 5, "Homing timeout"
        FOLLOWING_ERROR = 6, "Following error"
        SHORT_CIRCUIT = 7, "Short circuit detection"
        RMS_CURRENT_LIMIT = 8, "RMS current limit"
        PEAK_CURRENT_LIMIT = 9, "Peak current limit"
        POS_END_OF_TURN = 10, "Positive end of turn"
        NED_END_OF_TURN = 11, "Negative end of turn"

    class StateMessages(Enum):
        """
        Possible messages returned by the controller on get_state() query.
        """

        _init_ = "value message state"

        NO_REF_FROM_RESET = "0A", "NOT REFERENCED from reset.", NewportStates.NO_REF
        NO_REF_FROM_HOMING = "0B", "NOT REFERENCED from HOMING.", NewportStates.NO_REF
        NO_REF_FROM_CONFIG = (
            "0C",
            "NOT REFERENCED from CONFIGURATION.",
            NewportStates.NO_REF,
        )
        NO_REF_FROM_DISABLED = (
            "0D",
            "NOT REFERENCED from DISABLE.",
            NewportStates.NO_REF,
        )
        NO_REF_FROM_READY = "0E", "NOT REFERENCED from READY.", NewportStates.NO_REF
        NO_REF_FROM_MOVING = "0F", "NOT REFERENCED from MOVING.", NewportStates.NO_REF
        NO_REF_ESP_STAGE_ERROR = (
            "10",
            "NOT REFERENCED ESP stage error.",
            NewportStates.NO_REF,
        )
        NO_REF_FROM_JOGGING = "11", "NOT REFERENCED from JOGGING.", NewportStates.NO_REF
        CONFIG = "14", "CONFIGURATION.", NewportStates.CONFIG
        HOMING_FROM_RS232 = (
            "1E",
            "HOMING commanded from RS-232-C.",
            NewportStates.HOMING,
        )
        HOMING_FROM_SMC = "1F", "HOMING commanded by SMC-RC.", NewportStates.HOMING
        MOVING = "28", "MOVING.", NewportStates.MOVING
        READY_FROM_HOMING = "32", "READY from HOMING.", NewportStates.READY
        READY_FROM_MOVING = "33", "READY from MOVING.", NewportStates.READY
        READY_FROM_DISABLE = "34", "READY from DISABLE.", NewportStates.READY
        READY_FROM_JOGGING = "35", "READY from JOGGING.", NewportStates.READY
        DISABLE_FROM_READY = "3C", "DISABLE from READY.", NewportStates.DISABLE
        DISABLE_FROM_MOVING = "3D", "DISABLE from MOVING.", NewportStates.DISABLE
        DISABLE_FROM_JOGGING = "3E", "DISABLE from JOGGING.", NewportStates.DISABLE
        JOGGING_FROM_READY = "46", "JOGGING from READY.", NewportStates.JOGGING
        JOGGING_FROM_DISABLE = "47", "JOGGING from DISABLE.", NewportStates.JOGGING

    def __init__(self, com, dev_config=None):

        # Call superclass constructor
        super().__init__(com, dev_config)

        # address of the controller
        self.address = self.config.address

        # State of the controller (see state diagram in manual)
        self.state = self.States.NO_REF

        # position of the motor
        self.position = None

        # target position of the motor
        self.target_position = None

    def __repr__(self):
        return f"Newport motor controller SMC100PP {self.address}"

    @staticmethod
    def default_com_cls():
        return NewportSMC100PPSerialCommunication

    @staticmethod
    def config_cls():
        return NewportSMC100PPConfig

    def start(self):
        """
        Opens the communication protocol and applies the config.

        :raises SerialCommunicationIOError: when communication port cannot be opened
        """

        logging.info(f"Starting {self}")
        super().start()

        if self.get_state().state == self.States.NO_REF:
            if self.config.motor_config != self.get_motor_configuration():
                logging.info(f"Updating {self} configuration")
                self.go_to_configuration()
                self.set_motor_configuration()
                self.exit_configuration()
            logging.info(f"{self} configuration done")
            self.initialize()
            self.wait_until_motor_initialized()

    def stop(self) -> None:
        """
        Stop the device. Close the communication protocol.
        """

        try:
            if self.com.is_open:
                self.stop_motion()
        finally:
            logging.info(f"Stopping {self}")
            # close the com
            super().stop()

    def get_state(self, add: int = None) -> "StateMessages":
        """
        Check on the motor errors and the controller state

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        :raises NewportMotorError: if the motor reports an error
        :return: state message from the device (member of StateMessages)
        """

        if add is None:
            add = self.address

        ans = self.com.query(add, "TS")
        # the first symbol is not used, the next 3 symbols
        # are hexadecimal. Once converted to binary, they
        # indicate motor errors (see manual).
        errors = []
        for i in range(3):
            bin_errors = bin(int(ans[i + 1], 16))[2:].zfill(4)
            for j, b in enumerate(bin_errors):
                if b == "1":
                    errors.append(self.MotorErrors(i * 4 + j).message)
        if len(errors) > 0:
            logging.error(f"Motor {add} error(s): {', '.join(errors)}")
            raise NewportMotorError(f"Motor {add} error(s): {', '.join(errors)}")
        # the next two symbols indicate the controller state
        s = self.StateMessages(ans[4:6])
        logging.info(f"The newport controller {add} is in state {s.name}")
        self.state = s.state
        return s

    def get_motor_configuration(self, add: int = None) -> Dict[str, float]:
        """
        Query the motor configuration and returns it in a dictionary.

        :param add: controller address (1 to 31)
        :return: dictionary containing the motor's configuration
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        # The controller answer should be lines starting with the following prefixes
        prefixes = (
            [f"{add}PW1", f"{add}ID"]
            + [f"{add}{p.name}" for p in NewportConfigCommands]  # type: ignore
            + [f"{add}PW0"]
        )
        answers = self.com.query_multiple(add, "ZT", prefixes)
        # first and last line are expected to be only the prefixes
        assert not (answers[0] + answers[-1])
        # additionally, second line ID is not relevant
        answers = answers[2:-1]

        motor_config = {}
        # for each config param, read the answer given by the controller
        for prefix, answer in zip(NewportConfigCommands, answers):  # type: ignore
            # cast the config param as a float and add the result to the config dict
            motor_config[prefix.value] = float(answer)
        return motor_config

    def go_to_configuration(self, add: int = None) -> None:
        """
        This method is executed during start(). It can also be executed after a reset().
        The controller is put in CONFIG state, where configuration parameters
        can be changed.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        logging.info(f"Newport controller {add} entering CONFIG state.")
        self.com.send_command(add, "PW", 1)
        self.state = self.States.CONFIG

    def set_motor_configuration(self, add: int = None, config: dict = None) -> None:
        """
        Set the motor configuration. The motor must be in CONFIG state.

        :param add: controller address (1 to 31)
        :param config: dictionary containing the motor's configuration
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address
        if config is None:
            config = self.config.motor_config

        logging.info(f"Setting motor {add} configuration.")
        for param in config:
            if "compensation" in param and config[param] == 0:
                logging.debug(
                    f"Skipping command to set {param} to 0, which would cause"
                    f"ControllerErrors.PARAM_MISSING_OR_INVALID error. "
                    f"{param} will be set to 0 automatically anyway."
                )
            else:
                cmd = NewportConfigCommands(param).name
                self.com.send_command(add, cmd, config[param])

    def exit_configuration(self, add: int = None) -> None:
        """
        Exit the CONFIGURATION state and go back to the NOT REFERENCED state. All
        configuration parameters are saved to the device"s memory.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        logging.info(f"Newport controller {add} leaving CONFIG state.")
        with self.com.access_lock:
            self.com._send_command_unsafe(add, "PW", 0)
            sleep(self.config.exit_configuration_wait_sec)
            self.com._check_for_error_unsafe(add)
        self.state = self.States.NO_REF

    def initialize(self, add: int = None) -> None:
        """
        Puts the controller from the NOT_REF state to the READY state.
        Sends the motor to its "home" position.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        logging.info(f"Newport controller {add} is HOMING.")
        self.com.send_command(add, "OR")
        self.state = self.States.READY

    def wait_until_motor_initialized(self, add: int = None) -> None:
        """
        Wait until the motor leaves the HOMING state (at which point it should
        have arrived to the home position).

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        poll = True
        elapsed_time = 0.0
        start_time = time()
        while poll:
            state_message = self.get_state(add)
            elapsed_time += time() - start_time
            poll = (state_message.state == self.States.HOMING) and (
                elapsed_time < self.config.home_search_timeout
            )
            if poll:
                sleep(self.config.home_search_polling_interval)

        if state_message != self.StateMessages.READY_FROM_HOMING:
            raise NewportControllerError(
                f"Newport motor {add} should be READY from"
                f" HOMING but is {state_message}."
            )

    def reset(self, add: int = None) -> None:
        """
        Resets the controller, equivalent to a power-up. This puts the controller
        back to NOT REFERENCED state, which is necessary for configuring the controller.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        logging.info(f"Newport controller {add} is being reset to NO_REF.")
        self.com.send_command(add, "RS")
        # an additional read_text is needed to clean the buffer after reset()
        strange_char = self.com.read_text()
        logging.debug(f"{self} sent this: '{strange_char}' after reset()")
        self.state = self.States.NO_REF

    def get_position(self, add: int = None) -> float:
        """
        Returns the value of the current position.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        ans = self.com.query(add, "TP")

        self.position = (
            float(ans) * self.config.screw_scaling + self.config.user_position_offset
        )
        logging.info(f"Newport motor {add} position is {self.position}.")
        return self.position

    def move_to_absolute_position(self, pos: Number, add: int = None) -> None:
        """
        Move the motor to the specified position.

        :param pos: target absolute position (affected by the configured offset)
        :param add: controller address (1 to 31), defaults to self.address
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        # translate user-position into hardware-position
        hard_pos = pos - self.config.user_position_offset

        self.com.send_command(add, "PA", hard_pos)
        logging.info(
            f"Newport motor {add} moving from absolute position "
            f"{self.position} to absolute position {pos}."
        )
        self.target_position = pos

    def go_home(self, add: int = None) -> None:
        """
        Move the motor to its home position.

        :param add: controller address (1 to 31), defaults to self.address
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        self.com.send_command(add, "PA", 0)
        self.target_position = self.config.user_position_offset
        logging.info(
            f"Newport motor {add} moving from absolute position "
            f"{self.position} to home position {self.target_position}."
        )

    def move_to_relative_position(self, pos: Number, add: int = None) -> None:
        """
        Move the motor of the specified distance.

        :param pos: distance to travel (the sign gives the direction)
        :param add: controller address (1 to 31), defaults to self.address
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        self.com.send_command(add, "PR", pos)
        logging.info(f"Newport motor {add} moving of {pos} units.")
        self.target_position = self.get_position() + pos

    def wait_until_move_finished(self, add: int = None) -> None:
        """
        Wait until the motor leaves the MOVING state (at which point it should
        have arrived to the target position).

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        if self.get_state(add) != self.StateMessages.MOVING:
            logging.info(f"Newport motor {add} is not in MOVING state.")
            return
        else:
            distance = self.target_position - self.get_position()
            duration = (
                self.get_move_duration(distance)
                + self.config.move_finished_extra_wait_sec
            )
            sleep(duration)
            sm = self.get_state(add)
            if sm != self.StateMessages.READY_FROM_MOVING:
                raise NewportControllerError(
                    f"Newport motor {add} should be" f" READY from MOVING but is {sm}."
                )

    def get_move_duration(self, dist: Number, add: int = None) -> float:
        """
        Estimate the time necessary to move the motor of the specified distance.

        :param dist: distance to travel
        :param add: controller address (1 to 31), defaults to self.address
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        dist = round(dist, 2)
        duration = float(self.com.query(add, "PT", abs(dist)))
        logging.info(f"Newport motor {add} will need {duration}s to move {dist} units.")
        return duration

    def stop_motion(self, add: int = None) -> None:
        """
        Stop a move in progress by decelerating the positioner immediately with the
        configured acceleration until it stops. If a controller address is provided,
        stops a move in progress on this controller, else stops the moves on all
        controllers.

        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address
            logging.info("Stopping motion of all Newport motors.")
            self.com.send_stop(add)
        else:
            logging.info(f"Stopping motion of Newport motor {add}.")
            self.com.send_command(add, "ST")

    def get_acceleration(self, add: int = None) -> Number:
        """
        Leave the configuration state. The configuration parameters are saved to
        the device"s memory.

        :param add: controller address (1 to 31)
        :return: acceleration (preset units/s^2), value between 1e-6 and 1e12
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        acc = float(self.com.query(add, "AC", "?"))
        logging.info(f"Newport motor {add} acceleration is {acc}.")
        return acc

    def set_acceleration(self, acc: Number, add: int = None) -> None:
        """
        Leave the configuration state. The configuration parameters are saved to
        the device"s memory.

        :param acc: acceleration (preset units/s^2), value between 1e-6 and 1e12
        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        self.com.send_command(add, "AC", acc)
        logging.info(f"Newport motor {add} acceleration set to {acc}.")

    def get_controller_information(self, add: int = None) -> str:
        """
        Get information on the controller name and driver version

        :param add: controller address (1 to 31)
        :return: controller information
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        return self.com.query(add, "VE", "?")

    def get_positive_software_limit(self, add: int = None) -> Number:
        """
        Get the positive software limit (the maximum position that the motor is allowed
        to travel to towards the right).

        :param add: controller address (1 to 31)
        :return: positive software limit (preset units), value between 0 and 1e12
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        lim = float(self.com.query(add, "SR", "?"))
        logging.info(f"Newport motor {add} positive software limit is {lim}.")
        return lim

    def set_positive_software_limit(self, lim: Number, add: int = None) -> None:
        """
        Set the positive software limit (the maximum position that the motor is allowed
        to travel to towards the right).

        :param lim: positive software limit (preset units), value between 0 and 1e12
        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        self.com.send_command(add, "SR", lim)
        logging.info(f"Newport {add} positive software limit set to {lim}.")

    def get_negative_software_limit(self, add: int = None) -> Number:
        """
        Get the negative software limit (the maximum position that the motor is allowed
        to travel to towards the left).

        :param add: controller address (1 to 31)
        :return: negative software limit (preset units), value between -1e12 and 0
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        lim = float(self.com.query(add, "SL", "?"))
        logging.info(f"Newport motor {add} negative software limit is {lim}.")
        return lim

    def set_negative_software_limit(self, lim: Number, add: int = None) -> None:
        """
        Set the negative software limit (the maximum position that the motor is allowed
        to travel to towards the left).

        :param lim: negative software limit (preset units), value between -1e12 and 0
        :param add: controller address (1 to 31)
        :raises SerialCommunicationIOError: if the com is closed
        :raises NewportSerialCommunicationError: if an unexpected answer is obtained
        :raises NewportControllerError: if the controller reports an error
        """

        if add is None:
            add = self.address

        self.com.send_command(add, "SL", lim)
        logging.info(f"Newport {add} negative software limit set to {lim}.")


class NewportMotorError(Exception):
    """
    Error with the Newport motor.
    """

    pass


class NewportControllerError(Exception):
    """
    Error with the Newport controller.
    """

    pass


class NewportSerialCommunicationError(Exception):
    """
    Communication error with the Newport controller.
    """

    pass
