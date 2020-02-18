#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Base classes for the Supercube device.
"""

import logging
from time import sleep

from opcua import Node

from hvl_ccb import configdataclass
from hvl_ccb.comm import OpcUaSubHandler, OpcUaCommunicationConfig, OpcUaCommunication
from . import constants
from ..base import SingleCommDevice


class SupercubeSubscriptionHandler(OpcUaSubHandler):
    """
    OPC Subscription handler for datachange events and normal events specifically
    implemented for the Supercube devices.
    """

    def datachange_notification(self, node: Node, val, data):
        """
        In addition to the standard operation (debug logging entry of the datachange),
        alarms are logged at INFO level using the alarm text.

        :param node: the node object that triggered the datachange event
        :param val: the new value
        :param data:
        """

        super().datachange_notification(node, val, data)

        # assume an alarm datachange
        try:
            alarm_number_string = constants.Alarms(node.nodeid.Identifier).name
            alarm_text = getattr(constants.AlarmText, alarm_number_string)
            if val:
                alarm_text = "Coming: " + str(alarm_text)
            else:
                alarm_text = "Going: " + str(alarm_text)
            logging.getLogger(__name__).info(alarm_text)
            return
        except (AttributeError, ValueError):
            pass

        # assume a status datachnage
        if node.nodeid.Identifier == constants.Safety.status:
            new_status = str(constants.SafetyStatus(val))
            logging.getLogger(__name__).info(f"Safety: {new_status}")
            return

        # assume an earthing stick status datachange
        for num in range(1, 7):
            if node.nodeid.Identifier == constants.EarthingStick.status(num):
                new_status = str(constants.EarthingStickStatus(val))
                logging.getLogger(__name__).info(f"Earthing {num}: {new_status}")
                return


@configdataclass
class SupercubeConfiguration:
    """
    Configuration dataclass for the Supercube devices.
    """

    #: Namespace of the OPC variables, typically this is 3 (coming from Siemens)
    namespace_index: int = 3


@configdataclass
class SupercubeOpcUaCommunicationConfig(OpcUaCommunicationConfig):
    """
    Communication protocol configuration for OPC UA, specifications for the Supercube
    devices.
    """

    #: Subscription handler for data change events
    sub_handler: OpcUaSubHandler = SupercubeSubscriptionHandler()


class SupercubeOpcUaCommunication(OpcUaCommunication):
    """
    Communication protocol specification for Supercube devices.
    """

    @staticmethod
    def config_cls():
        return SupercubeOpcUaCommunicationConfig


class SupercubeBase(SingleCommDevice):
    """
    Base class for Supercube variants.
    """

    def __init__(self, com, dev_config=None):
        """
        Constructor for Supercube base class.

        :param com: the communication protocol or its configuration
        :param dev_config: the device configuration
        """

        super().__init__(com, dev_config)

        self.logger = logging.getLogger(__name__)

    @staticmethod
    def default_com_cls():
        return SupercubeOpcUaCommunication

    def start(self) -> None:
        """
        Starts the device. Sets the root node for all OPC read and write commands to
        the Siemens PLC object node which holds all our relevant objects and variables.
        """

        self.logger.info("Starting Supercube Base device")
        super().start()

        self.logger.debug("Add monitoring nodes")
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.GeneralSockets
            ),
            self.config.namespace_index,
        )
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.GeneralSupport
            ),
            self.config.namespace_index,
        )
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.Safety
            ),
            self.config.namespace_index,
        )
        self.com.init_monitored_nodes(
            str(constants.Errors.message), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            str(constants.Errors.warning), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            str(constants.Errors.stop), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            map(str, constants.Alarms), self.config.namespace_index
        )
        self.com.init_monitored_nodes(
            map(  # type: ignore
                str, constants.EarthingStick
            ),
            self.config.namespace_index,
        )

        # self.set_remote_control(True)  TODO: This variable does not exist yet

        self.logger.debug("Finished starting")

    def stop(self) -> None:
        """
        Stop the Supercube device. Deactivates the remote control and closes the
        communication protocol.
        """

        # self.set_remote_control(False)  TODO: This variable does not exist yet

        super().stop()

    @staticmethod
    def config_cls():
        return SupercubeConfiguration

    def read(self, node_id: str):
        """
        Local wrapper for the OPC UA communication protocol read method.

        :param node_id: the id of the node to read.
        :return: the value of the variable
        """

        self.logger.debug(f"Read from node ID {node_id} ...")
        result = self.com.read(str(node_id), self.config.namespace_index)
        self.logger.debug(f"Read from node ID {node_id}: {result}")
        return result

    def write(self, node_id, value) -> None:
        """
        Local wrapper for the OPC UA communication protocol write method.

        :param node_id: the id of the node to read
        :param value: the value to write to the variable
        """

        self.logger.debug(f"Write to node ID {node_id}: {value}")
        self.com.write(str(node_id), self.config.namespace_index, value)

    def set_remote_control(self, state: bool) -> None:
        """
        **TODO: test set_remote_control with device**

        Enable or disable remote control for the Supercube. This will effectively
        display a message on the touchscreen HMI.

        :param state: desired remote control state
        """

        self.write(constants.OpcControl.active, bool(state))

    def get_support_input(self, port: int, contact: int) -> bool:
        """
        Get the state of a support socket input.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :return: digital input read state
        """

        return bool(self.read(constants.GeneralSupport.input(port, contact)))

    def get_support_output(self, port: int, contact: int) -> bool:
        """
        Get the state of a support socket output.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :return: digital output read state
        """

        return bool(self.read(constants.GeneralSupport.output(port, contact)))

    def set_support_output(self, port: int, contact: int, state: bool) -> None:
        """
        Set the state of a support output socket.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :param state: is the desired state of the support output
        """

        self.write(constants.GeneralSupport.output(port, contact), bool(state))

    def set_support_output_impulse(
        self, port: int, contact: int, duration: float = 0.2, pos_pulse: bool = True
    ) -> None:
        """
        Issue an impulse of a certain duration on a support output contact. The polarity
        of the pulse (On-wait-Off or Off-wait-On) is specified by the pos_pulse
        argument.

        This function is blocking.

        :param port: is the socket number (1..6)
        :param contact: is the contact on the socket (1..2)
        :param duration: is the length of the impulse in seconds
        :param pos_pulse: is True, if the pulse shall be HIGH, False if it shall be LOW
        """

        self.set_support_output(port, contact, pos_pulse)
        sleep(duration)
        self.set_support_output(port, contact, not pos_pulse)

    def get_t13_socket(self, port: int) -> bool:
        """
        Read the state of a SEV T13 power socket.

        :param port: is the socket number, one of `constants.T13_SOCKET_PORTS`
        :return: on-state of the power socket
        """

        if port not in constants.T13_SOCKET_PORTS:
            raise ValueError(f"port not in {constants.T13_SOCKET_PORTS}: {port}")

        return bool(self.read(getattr(constants.GeneralSockets, f"t13_{port}")))

    def set_t13_socket(self, port: int, state: bool) -> None:
        """
        Set the state of a SEV T13 power socket.

        :param port: is the socket number, one of `constants.T13_SOCKET_PORTS`
        :param state: is the desired on-state of the socket
        """

        if not isinstance(state, bool):
            raise ValueError(f"state is not <bool>: {state}")

        if port not in constants.T13_SOCKET_PORTS:
            raise ValueError(f"port not in {constants.T13_SOCKET_PORTS}: {port}")

        self.write(getattr(constants.GeneralSockets, f"t13_{port}"), state)

    def get_cee16_socket(self) -> bool:
        """
        Read the on-state of the IEC CEE16 three-phase power socket.

        :return: the on-state of the CEE16 power socket
        """

        return bool(self.read(constants.GeneralSockets.cee16))

    def set_cee16_socket(self, state: bool) -> None:
        """
        Switch the IEC CEE16 three-phase power socket on or off.

        :param state: desired on-state of the power socket
        :raises ValueError: if state is not of type bool
        """

        if not isinstance(state, bool):
            raise ValueError(f"state is not <bool>: {state}")

        self.write(constants.GeneralSockets.cee16, state)

    def get_status(self) -> constants.SafetyStatus:
        """
        Get the safety circuit status of the Supercube.
        :return: the safety status of the supercube's state machine.
        """

        return constants.SafetyStatus(self.read(constants.Safety.status))

    def ready(self, state: bool) -> None:
        """
        Set ready state. Ready means locket safety circuit, red lamps, but high voltage
        still off.

        :param state: set ready state
        """

        self.write(constants.Safety.switchto_ready, state)

    def operate(self, state: bool) -> None:
        """
        Set operate state. If the state is RedReady, this will turn on the high
        voltage and close the safety switches.

        :param state: set operate state
        """

        self.write(constants.Safety.switchto_operate, state)

    def get_measurement_ratio(self, channel: int) -> float:
        """
        **TODO: test get_measurement_ratio with device**

        Get the set measurement ratio of an AC/DC analog input channel. Every input
        channel has a divider ratio assigned during setup of the Supercube system.
        This ratio can be read out.

        :param channel: number of the input channel (1..4)
        :return: the ratio
        """

        return float(self.read(constants.MeasurementsDividerRatio.get(channel)))

    def get_measurement_voltage(self, channel: int) -> float:
        """
        **TODO: test get_measurement_voltage with device**

        Get the measured voltage of an analog input channel. The voltage read out
        here is already scaled by the configured divider ratio.

        :param channel: number of the input channel (1..4)
        :return: measured voltage
        """

        return float(self.read(constants.MeasurementsScaledInput.get(channel)))

    def get_earthing_status(self, number: int) -> constants.EarthingStickStatus:
        """
        Get the status of an earthing stick, whether it is closed, open or undefined
        (moving).

        :param number: number of the earthing stick (1..6)
        :return: earthing stick status
        """

        return constants.EarthingStickStatus(
            self.read(constants.EarthingStick.status(number))
        )

    def get_earthing_manual(self, number: int) -> bool:
        """
        **TODO: Test get_earthing_manual with device**

        Get the manual status of an earthing stick. If an earthing stick is set to
        manual, it is closed even if the system is in states RedReady or RedOperate.

        :param number: number of the earthing stick (1..6)
        :return: earthing stick manual status
        """

        return bool(self.read(constants.EarthingStick.manual(number)))

    def set_earthing_manual(self, number: int, manual: bool) -> None:
        """
        **TODO: Test set_earthing_manual with device**

        Set the manual status of an earthing stick. If an earthing stick is set to
        manual, it stays closed even if the system is in states RedReady or RedOperate.

        :param number: number of the earthing stick (1..6)
        :param manual: earthing stick manual status (True or False)
        """

        self.write(constants.EarthingStick.manual(number), manual)

    def quit_error(self) -> None:
        """
        Quits errors that are active on the Supercube.
        """

        self.write(constants.Errors.quit, True)
        sleep(0.1)
        self.write(constants.Errors.quit, False)

    def get_door_status(self, door: int) -> constants.DoorStatus:
        """
        Get the status of a safety fence door. See :class:`constants.DoorStatus` for
        possible returned door statuses.

        :param door: the door number (1..3)
        :return: the door status
        """

        return constants.DoorStatus(self.read(constants.Door.get(door)))
