#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Supercube Typ A module.
"""

from time import sleep

from hvl_ccb.configuration import configdataclass
from . import constants
from .base import (
    SupercubeBase,
    SupercubeOpcUaCommunication,
    SupercubeOpcUaCommunicationConfig,
)


@configdataclass
class SupercubeAOpcUaConfiguration(SupercubeOpcUaCommunicationConfig):
    endpoint_name: str = constants.SupercubeOpcEndpoint.A.value  # type: ignore


class SupercubeAOpcUaCommunication(SupercubeOpcUaCommunication):
    @staticmethod
    def config_cls():
        return SupercubeAOpcUaConfiguration


class SupercubeWithFU(SupercubeBase):
    """
    Variant A of the Supercube with frequency converter.
    """

    @staticmethod
    def default_com_cls():
        return SupercubeAOpcUaCommunication

    def set_target_voltage(self, volt_v: float) -> None:
        """
        **TODO: test set_target_voltage with device**

        Set the output voltage to a defined value in V.

        :param volt_v: the desired voltage in V
        """

        self.write(constants.Power.voltage_target, volt_v)

    def get_target_voltage(self) -> float:
        """
        **TODO: test get_target_voltage with device**

        Gets the current setpoint of the output voltage value in V. This is not a
        measured value but is the corresponding function to :meth:`set_target_voltage`.

        :return: the setpoint voltage in V.
        """

        return float(self.read(constants.Power.voltage_target))

    def get_max_voltage(self) -> float:
        """
        **TODO: test get_max_voltage with device**

        Reads the maximum voltage of the setup and returns in V.

        :return: the maximum voltage of the setup in V.
        """

        return float(self.read(constants.Power.voltage_max))

    def set_slope(self, slope: float) -> None:
        """
        **TODO: test set_slope with device**

        Sets the dV/dt slope of the Supercube frequency converter to a new value in
        V/s.

        :param slope: voltage slope in V/s (0..15)
        """

        self.write(constants.Power.voltage_slope, slope)

    def get_primary_voltage(self) -> float:
        """
        **TODO: test get_primary_voltage with device**

        Read the current primary voltage at the output of the frequency converter (
        before transformer).

        :return: primary voltage in V
        """

        return float(self.read(constants.Power.voltage_primary))

    def get_primary_current(self) -> float:
        """
        **TODO: get_primary_current with device**

        Read the current primary current at the output of the frequency converter (
        before transformer).

        :return: primary current in A
        """

        return float(self.read(constants.Power.current_primary))

    def get_frequency(self) -> float:
        """
        **TODO: test get_frequency with device**

        Read the electrical frequency of the current Supercube setup.

        :return: the frequency in Hz
        """

        return float(self.read(constants.Power.frequency))

    def get_power_setup(self) -> constants.PowerSetup:
        """
        **TODO: test get_power_setup with device**

        Return the power setup selected in the Supercube's settings.

        :return: the power setup
        """

        return constants.PowerSetup(self.read(constants.Power.setup))

    def get_fso_active(self) -> bool:
        """
        **TODO: test get_fso_active with device**

        Get the state of the fast switch off functionality. Returns True if it is
        enabled, False otherwise.

        :return: state of the FSO functionality
        """

        return self.read(constants.BreakdownDetection.activated)

    def fso_reset(self) -> None:
        """
        **TODO: test fso_reset with device**

        Reset the fast switch off circuitry to go back into normal state and allow to
        re-enable operate mode.
        """

        self.write(constants.BreakdownDetection.reset, True)
        sleep(0.1)
        self.write(constants.BreakdownDetection.reset, False)
