import sys, copy

from PyQt5.QtWidgets import QMessageBox, QScrollArea
from PyQt5.QtCore import Qt

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.util import congruence
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
        orangegui.label(container, self, "2\u03b8_0, \u03b7, fwhm, intensity")

        scrollarea = QScrollArea(container)
        scrollarea.setMaximumWidth(self.CONTROL_AREA_WIDTH - 10)
        scrollarea.setMinimumWidth(self.CONTROL_AREA_WIDTH - 10)

        def write_text():
            self.pv_peaks = self.text_area.toPlainText()
            if not self.is_on_init: self.widget.dump_pv_peaks()

        self.text_area = gui.textArea(height=250, width=self.CONTROL_AREA_WIDTH - 30, readOnly=False)
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

