import sys, copy

from orangewidget.settings import Setting

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.fit.parameters.instrument.instrumental_parameters import ZeroError

class OWZeroErrorPeakShift(OWGenericDiffractionPatternParametersWidget):

    name = "Zero Error Peak Shift"
    description = "Zero Error Peak Shift"
    icon = "icons/zero_error_peak_shift.png"
    priority = 14

    shift = Setting([0.0])
    shift_fixed = Setting([0])
    shift_has_min = Setting([0])
    shift_min = Setting([0.0])
    shift_has_max = Setting([0])
    shift_max = Setting([0.0])
    shift_function = Setting([0])
    shift_function_value = Setting([""])

    def get_max_height(self):
        return 310

    def get_parameter_name(self):
        return "Peak Shift"

    def get_current_dimension(self):
        return len(self.shift)

    def get_parameter_box_instance(self, parameter_tab, index):
        return ZeroErrorPeakShiftBox(widget=self,
                                     parent=parameter_tab,
                                     index=index,
                                     shift=self.shift[index],
                                     shift_fixed=self.shift_fixed[index],
                                     shift_has_min=self.shift_has_min[index],
                                     shift_min=self.shift_min[index],
                                     shift_has_max=self.shift_has_max[index],
                                     shift_max=self.shift_max[index],
                                     shift_function=self.shift_function[index],
                                     shift_function_value=self.shift_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return ZeroErrorPeakShiftBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_shift_parameters([self.get_parameter_box(index).get_peak_shift() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_shift_parameters(ZeroError.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_shift_parameters_item(ZeroError.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_shift()

    def dump_shift(self): self.dump_parameter("shift")

class ZeroErrorPeakShiftBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 shift=0.0,
                 shift_fixed=0,
                 shift_has_min=0,
                 shift_min=0.0,
                 shift_has_max=0,
                 shift_max=0.0,
                 shift_function=0,
                 shift_function_value=""):
        super(ZeroErrorPeakShiftBox, self).__init__(widget=widget,
                                                    parent=parent,
                                                    index=index,
                                                    shift = shift,
                                                    shift_fixed = shift_fixed,
                                                    shift_has_min = shift_has_min,
                                                    shift_min = shift_min,
                                                    shift_has_max = shift_has_max,
                                                    shift_max = shift_max,
                                                    shift_function = shift_function,
                                                    shift_function_value = shift_function_value)
    def get_height(self):
        return 100
    
    def init_fields(self, **kwargs):
        self.shift = kwargs["shift"]
        self.shift_fixed = kwargs["shift_fixed"]
        self.shift_has_min = kwargs["shift_has_min"]
        self.shift_min = kwargs["shift_min"]
        self.shift_has_max = kwargs["shift_has_max"]
        self.shift_max = kwargs["shift_max"]
        self.shift_function = kwargs["shift_function"]
        self.shift_function_value = kwargs["shift_function_value"]

    def init_gui(self, container):
        OWGenericWidget.create_box_in_widget(self, container, "shift", add_callback=True, trim=25)

    def callback_shift(self):
        if not self.is_on_init: self.widget.dump_shift()

    def get_basic_parameter_prefix(self):
        return ZeroError.get_parameters_prefix()

    def set_data(self, shift_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "shift", shift_parameters.shift, value_only=True)

    def get_peak_shift(self):
        return ZeroError(shift=OWGenericWidget.populate_parameter_in_widget(self, "shift", self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWZeroErrorPeakShift()
    ow.show()
    a.exec_()
    ow.saveSettings()
