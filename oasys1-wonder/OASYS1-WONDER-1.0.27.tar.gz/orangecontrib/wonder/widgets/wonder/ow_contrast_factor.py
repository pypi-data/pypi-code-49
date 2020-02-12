import sys

from PyQt5.QtWidgets import QMessageBox

from orangewidget.settings import Setting

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericPhaseParameterWidget, ParameterActivableBox
from orangecontrib.wonder.util.gui_utility import gui
from oasys.widgets import congruence
from orangecontrib.wonder.fit.parameters.microstructure.constrast_factor import calculate_A_B_coefficients
from orangecontrib.wonder.fit.parameters.microstructure.strain import KrivoglazWilkensModel

class OWContrastFactor(OWGenericPhaseParameterWidget):
    name = "Contrast Factor Calculator"
    description = "Contrast Factor Calculator"
    icon = "icons/contrast_factor.png"
    priority = 18

    active = Setting([1])

    c11    = Setting([24.65])
    c12    = Setting([13.45])
    c44    = Setting([2.87])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 580

    def check_input_global_parameters(self, data):
        if not data.strain_parameters is None:
            raise Exception("This widget should be put BEFORE the strain model widget")

    def get_parameter_name(self):
        return "Constrast Factor"

    def get_current_dimension(self):
        return len(self.c11)

    def get_parameter_box_instance(self, parameter_tab, index):
        return StrainBox(widget=self,
                         parent=parameter_tab,
                         index = index,
                         active = self.active[index],
                         c11=self.c11[index],
                         c12=self.c12[index],
                         c44=self.c44[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return StrainBox(widget=self, parent=parameter_tab, index=index, active=0)

    def get_parameter_array(self):
        return self.fit_global_parameters.strain_parameters

    def get_parameter_item(self, phase_index):
        return self.fit_global_parameters.get_strain_parameters(phase_index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_strain_parameters([self.get_parameter_box(index).get_strain_parameters() for index in range(self.get_current_dimension())])

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpOtherSettings(self):
        self.dump_c11()
        self.dump_c12()
        self.dump_c44()

    def dump_c11(self): self.dump_variable("c11")
    def dump_c12(self): self.dump_variable("c12")
    def dump_c44(self): self.dump_variable("c44")

from orangecontrib.wonder.fit.parameters.fit_parameter import FitParameter

class StrainBox(ParameterActivableBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 active=1,
                 c11=0.0,
                 c12=0.0,
                 c44=0.0):
        super(StrainBox, self).__init__(widget=widget,
                                        parent=parent,
                                        index=index,
                                        active=active,
                                        c11=c11,
                                        c12=c12,
                                        c44=c44)

    def init_fields(self, **kwargs):
        self.c11 = kwargs["c11"]
        self.c12 = kwargs["c12"]
        self.c44 = kwargs["c44"]

    def init_main_box(self):
        contrast_factor_box = gui.widgetBox(self.main_box, "Elastic Constants", orientation="vertical", height=120, width=self.CONTROL_AREA_WIDTH - 10)

        gui.lineEdit(contrast_factor_box, self, "c11", "c11", labelWidth=90, valueType=float, callback=self.widget.dump_c11)
        gui.lineEdit(contrast_factor_box, self, "c12", "c12", labelWidth=90, valueType=float, callback=self.widget.dump_c12)
        gui.lineEdit(contrast_factor_box, self, "c44", "c44", labelWidth=90, valueType=float, callback=self.widget.dump_c44)

        text_area_box = gui.widgetBox(self.main_box, "Calculation Result", orientation="vertical", height=160, width=self.CONTROL_AREA_WIDTH - 10)

        self.text_area = gui.textArea(height=120, width=self.CONTROL_AREA_WIDTH - 40, readOnly=True)
        self.text_area.setText("")

        text_area_box.layout().addWidget(self.text_area)

    def get_basic_parameter_prefix(self):
        return KrivoglazWilkensModel.get_parameters_prefix()

    def get_strain_parameters(self):
        if self.active == 0:
            return None
        else:
            congruence.checkStrictlyPositiveNumber(self.c11, "c11")
            congruence.checkStrictlyPositiveNumber(self.c12, "c12")
            congruence.checkStrictlyPositiveNumber(self.c44, "c44")

            symmetry = self.widget.fit_global_parameters.measured_dataset.get_phase(self.index).symmetry

            Ae, Be, As, Bs = calculate_A_B_coefficients(self.c11, self.c12, self.c44, symmetry)

            text = "Ae = " + str(Ae) + "\n"
            text += "Be = " + str(Be) + "\n"
            text += "As = " + str(As) + "\n"
            text += "Bs = " + str(Bs) + "\n"

            self.text_area.setText(text)

            return KrivoglazWilkensModel(Ae=FitParameter(parameter_name=self.get_parameters_prefix() + "Ae", value=Ae, fixed=True),
                                         Be=FitParameter(parameter_name=self.get_parameters_prefix() + "Be", value=Be, fixed=True),
                                         As=FitParameter(parameter_name=self.get_parameters_prefix() + "As", value=As, fixed=True),
                                         Bs=FitParameter(parameter_name=self.get_parameters_prefix() + "Bs", value=Bs, fixed=True))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWContrastFactor()
    ow.show()
    a.exec_()
    ow.saveSettings()
