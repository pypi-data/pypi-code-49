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

from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import Qt

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.fit.parameters.additional.pseudo_voigt_peak import SpuriousPeaks, PseudoVoigtPeak


class OWPseudoVoigtPeak(OWGenericDiffractionPatternParametersWidget):
    name = "Pseudo-Voigt Peaks"
    description = "Add Pseudo-Voigt Peaks"
    icon = "icons/pv.png"
    priority = 11.1

    pv_peaks = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 550

    def get_parameter_name(self):
        return "Pseudo-Vigt Peaks"

    def get_current_dimension(self):
        return len(self.pv_peaks)

    def get_parameter_box_instance(self, parameter_tab, index):
        return PseudoVoigtPeakBox(widget=self,
                                      parent=parameter_tab,
                                      index=index,
                                      pv_peaks=self.pv_peaks[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return PseudoVoigtPeakBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_additional_parameters([self.get_parameter_box(index).get_pv_peaks() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_additional_parameters(SpuriousPeaks.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_additional_parameters_item(SpuriousPeaks.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_pv_peaks()

    def dump_pv_peaks(self): self.dump_variable("pv_peaks")

class PseudoVoigtPeakBox(ParameterBox):
    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 pv_peaks=0.0):
        super(PseudoVoigtPeakBox, self).__init__(widget=widget,
                                                 parent=parent,
                                                 index=index,
                                                 pv_peaks=pv_peaks)

    def get_height(self):
        return 300

    def init_fields(self, **kwargs):
        self.pv_peaks = kwargs["pv_peaks"]

    def init_gui(self, container):
        orangegui.label(container, self, "2\u03b8_0, \u03b7, fwhm, intensity\n\nevery parameter: <name> int <, fixed> or <, min value, max value> or <name> := function")

        scrollarea = QScrollArea(container)
        scrollarea.setMaximumWidth(self.CONTROL_AREA_WIDTH - 10)
        scrollarea.setMinimumWidth(self.CONTROL_AREA_WIDTH - 10)

        def write_text():
            self.pv_peaks = self.text_area.toPlainText()
            if not self.is_on_init: self.widget.dump_pv_peaks()

        self.text_area = gui.textArea(height=220, width=self.CONTROL_AREA_WIDTH - 30, readOnly=False)
        self.text_area.setText(self.pv_peaks)
        self.text_area.textChanged.connect(write_text)

        scrollarea.setWidget(self.text_area)
        scrollarea.setWidgetResizable(1)

        container.layout().addWidget(scrollarea, alignment=Qt.AlignHCenter)

    def get_basic_parameter_prefix(self):
        return PseudoVoigtPeak.get_parameters_prefix()

    def set_data(self, spurious_peaks):
        self.pv_peaks = ""
        for pseudo_voigt_peak in spurious_peaks.get_pseudo_voigt_peaks():
            self.pv_peaks += str(pseudo_voigt_peak) + "\n"

        self.text_area.setText(self.pv_peaks)

    def get_pv_peaks(self):
        pseudo_voigt_peaks = SpuriousPeaks()
        pseudo_voigt_peaks.parse_peaks(self.pv_peaks)

        return pseudo_voigt_peaks

