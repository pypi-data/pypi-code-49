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

from PyQt5.QtWidgets import QMessageBox

from orangewidget.settings import Setting

from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericDiffractionPatternParametersWidget, ParameterBox


class OWDecreasePoints(OWGenericDiffractionPatternParametersWidget):

    name = "Decrease Number of Points"
    description = "Decrease Number of Points"
    icon = "icons/decrease.png"
    priority = 1000
    
    reduction_factor = Setting([1])
    
    def get_max_height(self):
        return 310

    def get_parameter_name(self):
        return "Reduction Factor"

    def get_current_dimension(self):
        return len(self.reduction_factor)

    def get_parameter_box_instance(self, parameter_tab, index):
        return DecreasePointsBox(widget=self,
                                     parent=parameter_tab,
                                     index=index,
                                     reduction_factor=self.reduction_factor[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return DecreasePointsBox(widget=self, parent=parameter_tab, index=index)

    def set_data(self, data):
        try:
            if not data is None: self.input_diffraction_patterns = data.measured_dataset.duplicate_diffraction_patterns()

            super().set_data(data)
        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 str(e),
                                 QMessageBox.Ok)

            if self.IS_DEVELOP: raise e

    def set_parameter_data(self):
        for diffraction_pattern_index in range(self.fit_global_parameters.measured_dataset.get_diffraction_patterns_number()):
            reduction_factor = self.get_parameter_box(diffraction_pattern_index).get_reduction_factor()
            if reduction_factor > 1:
                self.fit_global_parameters.measured_dataset.diffraction_patterns[diffraction_pattern_index].diffraction_pattern = \
                    self.input_diffraction_patterns[diffraction_pattern_index].diffraction_pattern[::reduction_factor]

    def get_parameter_array(self):
        return self.fit_global_parameters.measured_dataset.diffraction_patterns

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.measured_dataset.diffraction_patterns[diffraction_pattern_index]

    def dumpSettings(self):
        self.dump_reduction_factor()

    def dump_reduction_factor(self): self.dump_variable("reduction_factor")

class DecreasePointsBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 reduction_factor=1):
        super(DecreasePointsBox, self).__init__(widget=widget,
                                                    parent=parent,
                                                    index=index,
                                                    reduction_factor = reduction_factor)
    def get_height(self):
        return 100
    
    def init_fields(self, **kwargs):
        self.reduction_factor = kwargs["reduction_factor"]

    def init_gui(self, container):
        gui.lineEdit(container, self, "reduction_factor", "Reduction Factor", labelWidth=300, valueType=int, callback=self.widget.dump_reduction_factor)

    def get_basic_parameter_prefix(self):
        pass

    def set_data(self, data):
        pass

    def get_reduction_factor(self):
        return self.reduction_factor

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWDecreasePoints()
    ow.show()
    a.exec_()
    ow.saveSettings()
