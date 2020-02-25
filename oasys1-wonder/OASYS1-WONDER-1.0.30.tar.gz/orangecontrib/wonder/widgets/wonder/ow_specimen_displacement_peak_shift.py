#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################

import sys

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui
from oasys.widgets import congruence
from orangecontrib.wonder.fit.parameters.instrument.instrumental_parameters import SpecimenDisplacement


class OWSpecimenDisplacementPeakShift(OWGenericDiffractionPatternParametersWidget):

    name = "Specimen Displacement Peak Shift"
    description = "Specimen Displacement Peak Shift"
    icon = "icons/specimen_displacement_peak_shift.png"
    priority = 15

    goniometer_radius = Setting([1.0])

    displacement = Setting([0.0])
    displacement_fixed = Setting([0])
    displacement_has_min = Setting([0])
    displacement_min = Setting([0.0])
    displacement_has_max = Setting([0])
    displacement_max = Setting([0.0])
    displacement_function = Setting([0])
    displacement_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 350

    def get_parameter_name(self):
        return "Specimen Displacement"

    def get_current_dimension(self):
        return len(self.displacement)

    def get_parameter_box_instance(self, parameter_tab, index):
        return SpecimenDisplacementPeakShiftBox(widget=self,
                                         parent=parameter_tab,
                                         index=index,
                                         goniometer_radius=self.goniometer_radius[index],
                                         displacement=self.displacement[index],
                                         displacement_fixed=self.displacement_fixed[index],
                                         displacement_has_min=self.displacement_has_min[index],
                                         displacement_min=self.displacement_min[index],
                                         displacement_has_max=self.displacement_has_max[index],
                                         displacement_max=self.displacement_max[index],
                                         displacement_function=self.displacement_function[index],
                                         displacement_function_value=self.displacement_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return SpecimenDisplacementPeakShiftBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_shift_parameters([self.get_parameter_box(index).get_peak_shift() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_shift_parameters(SpecimenDisplacement.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_shift_parameters_item(SpecimenDisplacement.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_goniometer_radius()
        self.dump_displacement()

    def dump_goniometer_radius(self): self.dump_variable("goniometer_radius")

    def dump_displacement(self): self.dump_parameter("displacement")

class SpecimenDisplacementPeakShiftBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 goniometer_radius = 1.0,
                 displacement=0.0,
                 displacement_fixed=0,
                 displacement_has_min=0,
                 displacement_min=0.0,
                 displacement_has_max=0,
                 displacement_max=0.0,
                 displacement_function=0,
                 displacement_function_value=""):
        super(SpecimenDisplacementPeakShiftBox, self).__init__(widget=widget,
                                                               parent=parent,
                                                               index=index,
                                                               goniometer_radius=goniometer_radius,
                                                               displacement = displacement,
                                                               displacement_fixed = displacement_fixed,
                                                               displacement_has_min = displacement_has_min,
                                                               displacement_min = displacement_min,
                                                               displacement_has_max = displacement_has_max,
                                                               displacement_max = displacement_max,
                                                               displacement_function = displacement_function,
                                                               displacement_function_value = displacement_function_value)

    def get_height(self):
        return 100

    def init_fields(self, **kwargs):
        self.goniometer_radius           = kwargs["goniometer_radius"]
        self.displacement                = kwargs["displacement"]
        self.displacement_fixed          = kwargs["displacement_fixed"]
        self.displacement_has_min        = kwargs["displacement_has_min"]
        self.displacement_min            = kwargs["displacement_min"]
        self.displacement_has_max        = kwargs["displacement_has_max"]
        self.displacement_max            = kwargs["displacement_max"]
        self.displacement_function       = kwargs["displacement_function"]
        self.displacement_function_value = kwargs["displacement_function_value"]

    def init_gui(self, container):
        gui.lineEdit(container, self, "goniometer_radius", "Goniometer Radius [m]", labelWidth=300, valueType=float, callback=self.widget.dump_goniometer_radius)
        orangegui.separator(container)
        OWGenericWidget.create_box_in_widget(self, container, "displacement", add_callback=True, label_width=75, trim=15)

    def callback_displacement(self):
        if not self.is_on_init: self.widget.dump_displacement()

    def get_basic_parameter_prefix(self):
        return SpecimenDisplacement.get_parameters_prefix()

    def set_data(self, shift_parameters):
        self.goniometer_radius = shift_parameters.goniometer_radius

        OWGenericWidget.populate_fields_in_widget(self, "displacement", shift_parameters.displacement, value_only=True)

    def get_peak_shift(self):
        congruence.checkStrictlyPositiveNumber(self.goniometer_radius, "Goniometer Radius")

        return SpecimenDisplacement(goniometer_radius=self.goniometer_radius,
                                    displacement=OWGenericWidget.get_fit_parameter_from_widget(self, "displacement", self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWSpecimenDisplacementPeakShift()
    ow.show()
    a.exec_()
    ow.saveSettings()
