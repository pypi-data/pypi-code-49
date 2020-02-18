#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Constants, variable names for the Supercube OPC-connected devices.
"""

from aenum import IntEnum

from hvl_ccb.utils.enum import ValueEnum, unique


@unique
class SupercubeOpcEndpoint(ValueEnum):
    """
    OPC Server Endpoint strings for the supercube variants.
    """

    A = "Supercube Typ A"
    B = "Supercube Typ B"


@unique
class GeneralSupport(ValueEnum):
    """
    NodeID strings for the support inputs and outputs.
    """

    in_1_1 = '"Ix_Allg_Support1_1"'
    in_1_2 = '"Ix_Allg_Support1_2"'
    in_2_1 = '"Ix_Allg_Support2_1"'
    in_2_2 = '"Ix_Allg_Support2_2"'
    in_3_1 = '"Ix_Allg_Support3_1"'
    in_3_2 = '"Ix_Allg_Support3_2"'
    in_4_1 = '"Ix_Allg_Support4_1"'
    in_4_2 = '"Ix_Allg_Support4_2"'
    in_5_1 = '"Ix_Allg_Support5_1"'
    in_5_2 = '"Ix_Allg_Support5_2"'
    in_6_1 = '"Ix_Allg_Support6_1"'
    in_6_2 = '"Ix_Allg_Support6_2"'
    out_1_1 = '"Qx_Allg_Support1_1"'
    out_1_2 = '"Qx_Allg_Support1_2"'
    out_2_1 = '"Qx_Allg_Support2_1"'
    out_2_2 = '"Qx_Allg_Support2_2"'
    out_3_1 = '"Qx_Allg_Support3_1"'
    out_3_2 = '"Qx_Allg_Support3_2"'
    out_4_1 = '"Qx_Allg_Support4_1"'
    out_4_2 = '"Qx_Allg_Support4_2"'
    out_5_1 = '"Qx_Allg_Support5_1"'
    out_5_2 = '"Qx_Allg_Support5_2"'
    out_6_1 = '"Qx_Allg_Support6_1"'
    out_6_2 = '"Qx_Allg_Support6_2"'

    @classmethod
    def output(cls, port, contact):
        """
        Get the NodeID string for a support output.

        :param port: the desired port (1..6)
        :param contact: the desired contact at the port (1..2)
        :return: the node id string
        """

        return getattr(cls, "out_{}_{}".format(port, contact))

    @classmethod
    def input(cls, port, contact):
        """
        Get the NodeID string for a support input.

        :param port: the desired port (1..6)
        :param contact: the desired contact at the port (1..2)
        :return: the node id string
        """

        return getattr(cls, "in_{}_{}".format(port, contact))


@unique
class BreakdownDetection(ValueEnum):
    """
    Node ID strings for the breakdown detection.

    TODO: these variable NodeIDs are not tested and/or correct yet.
    """

    #: Boolean read-only variable indicating whether breakdown detection and fast
    #: switchoff is enabled in the system or not.
    activated = '"Ix_Allg_Breakdown_activated"'

    #: Boolean read-only variable telling whether the fast switch-off has triggered.
    #: This can also be seen using the safety circuit state, therefore no method is
    #: implemented to read this out directly.
    triggered = '"Ix_Allg_Breakdown_triggered"'

    #: Boolean writable variable to reset the fast switch-off. Toggle to re-enable.
    reset = '"Qx_Allg_Breakdown_reset"'


@unique
class GeneralSockets(ValueEnum):
    """
    NodeID strings for the power sockets (3x T13 and 1xCEE16).
    """

    #: SEV T13 socket No. 1 (writable boolean).
    t13_1 = '"Qx_Allg_Socket_T13_1"'

    #: SEV T13 socket No. 2 (writable boolean).
    t13_2 = '"Qx_Allg_Socket_T13_2"'

    #: SEV T13 socket No. 3 (writable boolean).
    t13_3 = '"Qx_Allg_Socket_T13_3"'

    #: CEE16 socket (writeable boolean).
    cee16 = '"Qx_Allg_Socket_CEE16"'


T13_SOCKET_PORTS = (1, 2, 3)
"""
Port numbers of SEV T13 power socket
"""


@unique
class Safety(ValueEnum):
    """
    NodeID strings for the basic safety circuit status and green/red switches "ready"
    and "operate".
    """

    #: Status is a read-only integer containing the state number of the
    #: supercube-internal state machine. The values correspond to numbers in
    #: :class:`SafetyStatus`.
    status = '"DB_Safety_Circuit"."si_safe_status"'

    #: Writable boolean for switching to Red Ready (locked, HV off) state.
    switchto_ready = '"DB_Safety_Circuit"."sx_safe_switchto_ready"'

    #: Writable boolean for switching to Red Operate (locket, HV on) state.
    switchto_operate = '"DB_Safety_Circuit"."sx_safe_switchto_operate"'


class SafetyStatus(IntEnum):
    """
    Safety status values that are possible states returned from
    :meth:`hvl_ccb.dev.supercube.base.Supercube.get_status`. These
    values correspond to the states of the Supercube's safety circuit statemachine.
    """

    #: System is initializing or booting.
    Initializing = 0

    #: System is safe, lamps are green and some safety elements are not in place such
    #: that it cannot be switched to red currently.
    GreenNotReady = 1

    #: System is safe and all safety elements are in place to be able to switch to
    #: *ready*.
    GreenReady = 2

    #: System is locked in red state and *ready* to go to *operate* mode.
    RedReady = 3

    #: System is locked in red state and in *operate* mode, i.e. high voltage on.
    RedOperate = 4

    #: Fast turn off triggered and switched off the system. Reset FSO to go back to a
    #: normal state.
    QuickStop = 5

    #: System is in error mode.
    Error = 6


@unique
class Power(ValueEnum):
    """
    Variable NodeID strings concerning power data.

    TODO: these variable NodeIDs are not tested and/or correct yet, they don't exist
        yet on Supercube side.
    """

    #: Primary voltage in volts, measured by the frequency converter at its output.
    #: (read-only)
    voltage_primary = "Qr_Power_FU_actualVoltage"

    #: Primary current in ampere, measured by the frequency converter. (read-only)
    current_primary = "Qr_Power_FU_actualCurrent"

    #: Power setup that is configured using the Supercube HMI. The value corresponds to
    #: the ones in :class:`PowerSetup`. (read-only)
    setup = "Qi_Power_Setup"

    #: Voltage slope in V/s.
    voltage_slope = "Ir_Power_dUdt"

    #: Target voltage setpoint in V.
    voltage_target = "Ir_Power_TargetVoltage"

    #: Maximum voltage allowed by the current experimental setup. (read-only)
    voltage_max = "Iw_Power_maxVoltage"

    #: Frequency converter output frequency. (read-only)
    frequency = "Ir_Power_FU_Frequency"


class PowerSetup(IntEnum):
    """
    Possible power setups corresponding to the value of variable :attr:`Power.setup`.
    """

    #: No safety switches, use only safety components (doors, fence, earthing...)
    #: without any power.
    NoPower = 0

    #: External power supply fed through blue CEE32 input using isolation transformer
    #: and safety switches of the Supercube, or using an external safety switch
    #: attached to the Supercube Type B.
    External = 1

    #: AC voltage with MWB transformer set to 50kV maximum voltage.
    AC_SingleStage_50kV = 2

    #: AC voltage with MWB transformer set to 100kV maximum voltage.
    AC_SingleStage_100kV = 3

    #: AC voltage with two MWB transformers, one at 100kV and the other at 50kV,
    #: resulting in a total maximum voltage of 150kV.
    AC_DoubleStage_150kV = 4

    #: AC voltage with two MWB transformers both at 100kV, resulting in a total
    #: maximum voltage of 200kV
    AC_DoubleStage_200kV = 5

    #: Internal usage of the frequency converter, controlling to the primary voltage
    #: output of the supercube itself (no measurement transformer used)
    Internal = 6

    #: DC voltage with one AC transformer set to 100kV AC, resulting in 140kV DC
    DC_SingleStage_140kV = 7

    #: DC voltage with two AC transformers set to 100kV AC each, resulting in 280kV
    #: DC in total (or a single stage transformer with Greinacher voltage doubling
    #: rectifier)
    DC_DoubleStage_280kV = 8


@unique
class MeasurementsScaledInput(ValueEnum):
    """
    Variable NodeID strings for the four analog BNC inputs for measuring voltage.
    The voltage returned in these variables is already scaled with the set ratio,
    which can be read using the variables in :class:`MeasurementsDividerRatio`.

    TODO: these variable NodeIDs are not tested and/or correct yet.
    """

    input_1 = "Qr_Measure_Input1_scaledVoltage"
    input_2 = "Qr_Measure_Input2_scaledVoltage"
    input_3 = "Qr_Measure_Input3_scaledVoltage"
    input_4 = "Qr_Measure_Input4_scaledVoltage"

    @classmethod
    def get(cls, channel: int):
        """
        Get the attribute for an input number.

        :param channel: the channel number (1..4)
        :return: the enum for the desired channel.
        """

        return getattr(cls, "input_{}".format(channel))


@unique
class MeasurementsDividerRatio(ValueEnum):
    """
    Variable NodeID strings for the measurement input scaling ratios. These ratios
    are defined in the Supercube HMI setup and are provided in the python module here
    to be able to read them out, allowing further calculations.

    TODO: these variable nodeIDs are not tested and/or correct yet.
    """

    input_1 = "Ir_Measure_DividerRatio_1"
    input_2 = "Ir_Measure_DividerRatio_2"
    input_3 = "Ir_Measure_DividerRatio_3"
    input_4 = "Ir_Measure_DividerRatio_4"

    @classmethod
    def get(cls, channel: int):
        """
        Get the attribute for an input number.

        :param channel: the channel number (1..4)
        :return: the enum for the desired channel.
        """

        return getattr(cls, "input_{}".format(channel))


class EarthingStickStatus(IntEnum):
    """
    Status of an earthing stick. These are the possible values in the status integer
    e.g. in :attr:`EarthingStick.status_1`.
    """

    #: Earthing stick is deselected and not enabled in safety circuit. To get out of
    #: this state, the earthing has to be enabled in the Supercube HMI setup.
    inactive = 0

    #: Earthing is closed (safe).
    closed = 1

    #: Earthing is open (not safe).
    open = 2

    #: Earthing is in error, e.g. when the stick did not close correctly or could not
    #: open.
    error = 3


@unique
class EarthingStick(ValueEnum):
    """
    Variable NodeID strings for all earthing stick statuses (read-only integer) and
    writable booleans for setting the earthing in manual mode.
    """

    status_1 = '"DB_Safety_Circuit"."Erdpeitsche 1"."si_HMI_Status"'
    status_2 = '"DB_Safety_Circuit"."Erdpeitsche 2"."si_HMI_Status"'
    status_3 = '"DB_Safety_Circuit"."Erdpeitsche 3"."si_HMI_Status"'
    status_4 = '"DB_Safety_Circuit"."Erdpeitsche 4"."si_HMI_Status"'
    status_5 = '"DB_Safety_Circuit"."Erdpeitsche 5"."si_HMI_Status"'
    status_6 = '"DB_Safety_Circuit"."Erdpeitsche 6"."si_HMI_Status"'

    manual_1 = '"DB_Safety_Circuit"."Erdpeitsche 1"."sx_earthing_manually"'
    manual_2 = '"DB_Safety_Circuit"."Erdpeitsche 2"."sx_earthing_manually"'
    manual_3 = '"DB_Safety_Circuit"."Erdpeitsche 3"."sx_earthing_manually"'
    manual_4 = '"DB_Safety_Circuit"."Erdpeitsche 4"."sx_earthing_manually"'
    manual_5 = '"DB_Safety_Circuit"."Erdpeitsche 5"."sx_earthing_manually"'
    manual_6 = '"DB_Safety_Circuit"."Erdpeitsche 6"."sx_earthing_manually"'

    @classmethod
    def status(cls, number: int):
        """
        Get the status enum attribute for an earthing stick number.

        :param number: the earthing stick (1..6)
        :return: the status enum
        """

        return getattr(cls, "status_{}".format(number))

    @classmethod
    def manual(cls, number: int):
        """
        Get the manual enum attribute for an earthing stick number.

        :param number: the earthing stick (1..6)
        :return: the manual enum
        """

        return getattr(cls, "manual_{}".format(number))


@unique
class Errors(ValueEnum):
    """
    Variable NodeID strings for information regarding error, warning and message
    handling.
    """

    #: Boolean read-only variable telling if a message is active.
    message = '"DB_Meldepuffer"."Hinweis_aktiv"'

    #: Boolean read-only variable telling if a warning is active.
    warning = '"DB_Meldepuffer"."Warnung_aktiv"'

    #: Boolean read-only variable telling if a stop is active.
    stop = '"DB_Meldepuffer"."Stop_aktiv"'

    #: Writable boolean for the error quit button.
    quit = '"DB_Meldepuffer"."Quittierbutton"'


class _AlarmsBase(ValueEnum):
    @classmethod
    def get(cls, number: int):
        return getattr(cls, f"Alarm{number}")


#: Alarms enumeration containing all variable NodeID strings for the alarm array.
Alarms = _AlarmsBase(
    "Alarms", {f"Alarm{n}": f'"DB_Alarm_HMI"."Alarm{n}"' for n in range(1, 152)}
)


class DoorStatus(IntEnum):
    """
    Possible status values for doors.
    """

    #: not enabled in Supercube HMI setup, this door is not supervised.
    inactive = 0

    #: Door is open.
    open = 1

    #: Door is closed, but not locked.
    closed = 2

    #: Door is closed and locked (safe state).
    locked = 3

    #: Door has an error or was opened in locked state (either with emergency stop or
    #: from the inside).
    error = 4


class Door(ValueEnum):
    """
    Variable NodeID strings for doors.
    """

    status_1 = '"DB_Safety_Circuit"."Türe 1"."si_HMI_status_door"'
    status_2 = '"DB_Safety_Circuit"."Türe 2"."si_HMI_status_door"'
    status_3 = '"DB_Safety_Circuit"."Türe 3"."si_HMI_status_door"'

    @classmethod
    def get(cls, door: int):
        """
        Get the attribute for a door status.

        :param door: the door number (1..3)
        :return: the enum for the desired door status NodeID string.
        """

        return getattr(cls, "status_{}".format(door))


class AlarmText(ValueEnum):
    """
    This enumeration contains textual representations for all error classes (stop,
    warning and message) of the Supercube system. Use the :meth:`AlarmText.get`
    method to retrieve the enum of an alarm number.
    """

    # Safety elements
    Alarm1 = "STOP Emergency Stop 1"
    Alarm2 = "STOP Emergency Stop 2"
    Alarm3 = "STOP Emergency Stop 3"
    Alarm4 = "STOP Safety Switch 1 error"
    Alarm5 = "STOP Safety Switch 2 error"
    Alarm6 = "STOP Door 1 lock supervision"
    Alarm7 = "STOP Door 2 lock supervision"
    Alarm8 = "STOP Door 3 lock supervision"
    Alarm9 = "STOP Earthing stick 1 error while opening"
    Alarm10 = "STOP Earthing stick 2 error while opening"
    Alarm11 = "STOP Earthing stick 3 error while opening"
    Alarm12 = "STOP Earthing stick 4 error while opening"
    Alarm13 = "STOP Earthing stick 5 error while opening"
    Alarm14 = "STOP Earthing stick 6 error while opening"
    Alarm15 = "STOP Earthing stick 1 error while closing"
    Alarm16 = "STOP Earthing stick 2 error while closing"
    Alarm17 = "STOP Earthing stick 3 error while closing"
    Alarm18 = "STOP Earthing stick 4 error while closing"
    Alarm19 = "STOP Earthing stick 5 error while closing"
    Alarm20 = "STOP Earthing stick 6 error while closing"
    Alarm21 = "STOP Safety fence 1"
    Alarm22 = "STOP Safety fence 2"
    Alarm23 = "STOP OPC connection error"
    Alarm24 = "STOP Grid power failure"
    Alarm25 = "STOP UPS failure"
    Alarm26 = "STOP 24V PSU failure"

    # Doors
    Alarm41 = "WARNING Door 1: Use earthing rod!"
    Alarm42 = "MESSAGE Door 1: Earthing rod is still in setup."
    Alarm43 = "WARNING Door 2: Use earthing rod!"
    Alarm44 = "MESSAGE Door 2: Earthing rod is still in setup."
    Alarm45 = "WARNING Door 3: Use earthing rod!"
    Alarm46 = "MESSAGE Door 3: Earthing rod is still in setup."

    # General
    Alarm47 = "MESSAGE UPS charge < 85%"
    Alarm48 = "MESSAGE UPS running on battery"

    # generic not defined alarm text
    not_defined = "NO ALARM TEXT DEFINED"

    @classmethod
    def get(cls, alarm: int):
        """
        Get the attribute of this enum for an alarm number.

        :param alarm: the alarm number
        :return: the enum for the desired alarm number
        """

        try:
            return getattr(cls, "Alarm{}".format(alarm))
        except AttributeError:
            return cls.not_defined


class OpcControl(ValueEnum):
    """
    Variable NodeID strings for supervision of the OPC connection from the
    controlling workstation to the Supercube.

    TODO: this variable nodeID string is not tested and/or correct yet.
    """

    #: writable boolean to enable OPC remote control and display a message window on
    #: the Supercube HMI.
    active = "Ix_OPC_active"
