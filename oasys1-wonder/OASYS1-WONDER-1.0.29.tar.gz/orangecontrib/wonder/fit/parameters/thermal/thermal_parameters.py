import numpy

from oasys.widgets import congruence
from orangecontrib.wonder.util.fit_utilities import Utilities

from orangecontrib.wonder.fit.parameters.fit_parameter import ParametersList, FitParameter, Boundary, PARAM_HWMAX, PARAM_HWMIN
from orangecontrib.wonder.fit.parameters.measured_data.reflection import Reflection

class ThermalParameters(ParametersList):
    def __init__(self, phases_number=1):
        self.debye_waller_factors = [None]*phases_number

    def set_phases(self, phases_number=1):
        if len(self.debye_waller_factors) != len(phases_number):
            debye_waller_factors = [None]*phases_number

            for phase_index in range(min(phases_number, len(self.debye_waller_factors))):
                debye_waller_factors[phase_index] = self.debye_waller_factors[phase_index]

            self.debye_waller_factors = debye_waller_factors

    def set_debye_waller_factor(self, phase_index, debye_waller_factor):
        self.debye_waller_factors[phase_index] = debye_waller_factor

    def get_debye_waller_factor(self, phase_index):
        return self.debye_waller_factors[phase_index]

    @classmethod
    def get_parameters_prefix(cls):
        return "thermal_"


