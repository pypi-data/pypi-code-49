import sys

from orangewidget.settings import Setting

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.fit.parameters.instrument.instrumental_parameters import Lab6TanCorrection

class OWCalibrationPeakShift(OWGenericDiffractionPatternParametersWidget):
    name = "Calibration Peak Shift"
    description = "Calibration Peak Shift"
    icon = "icons/calibration_peak_shift.png"
    priority = 13

    ax = Setting([0.0])
    bx = Setting([0.0])
    cx = Setting([0.0])
    dx = Setting([0.0])
    ex = Setting([0.0])
    ax_fixed = Setting([0])
    bx_fixed = Setting([0])
    cx_fixed = Setting([0])
    dx_fixed = Setting([0])
    ex_fixed = Setting([0])
    ax_has_min = Setting([0])
    bx_has_min = Setting([0])
    cx_has_min = Setting([0])
    dx_has_min = Setting([0])
    ex_has_min = Setting([0])
    ax_min = Setting([0.0])
    bx_min = Setting([0.0])
    cx_min = Setting([0.0])
    dx_min = Setting([0.0])
    ex_min = Setting([0.0])
    ax_has_max = Setting([0])
    bx_has_max = Setting([0])
    cx_has_max = Setting([0])
    dx_has_max = Setting([0])
    ex_has_max = Setting([0])
    ax_max = Setting([0.0])
    bx_max = Setting([0.0])
    cx_max = Setting([0.0])
    dx_max = Setting([0.0])
    ex_max = Setting([0.0])
    ax_function = Setting([0])
    bx_function = Setting([0])
    cx_function = Setting([0])
    dx_function = Setting([0])
    ex_function = Setting([0])
    ax_function_value = Setting([""])
    bx_function_value = Setting([""])
    cx_function_value = Setting([""])
    dx_function_value = Setting([""])
    ex_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 450

    def get_parameter_name(self):
        return "LaB6 Tan Correction"

    def get_current_dimension(self):
        return len(self.ax)

    def get_parameter_box_instance(self, parameter_tab, index):
        return CalibrationPeakShiftBox(widget=self,
                                       parent=parameter_tab,
                                       index=index,
                                       ax=self.ax[index],
                                       bx=self.bx[index],
                                       cx=self.cx[index],
                                       dx=self.dx[index],
                                       ex=self.ex[index],
                                       ax_fixed=self.ax_fixed[index],
                                       bx_fixed=self.bx_fixed[index],
                                       cx_fixed=self.cx_fixed[index],
                                       dx_fixed=self.dx_fixed[index],
                                       ex_fixed=self.ex_fixed[index],
                                       ax_has_min=self.ax_has_min[index],
                                       bx_has_min=self.bx_has_min[index],
                                       cx_has_min=self.cx_has_min[index],
                                       dx_has_min=self.dx_has_min[index],
                                       ex_has_min=self.ex_has_min[index],
                                       ax_min=self.ax_min[index],
                                       bx_min=self.bx_min[index],
                                       cx_min=self.cx_min[index],
                                       dx_min=self.dx_min[index],
                                       ex_min=self.ex_min[index],
                                       ax_has_max=self.ax_has_max[index],
                                       bx_has_max=self.bx_has_max[index],
                                       cx_has_max=self.cx_has_max[index],
                                       dx_has_max=self.dx_has_max[index],
                                       ex_has_max=self.ex_has_max[index],
                                       ax_max=self.ax_max[index],
                                       bx_max=self.bx_max[index],
                                       cx_max=self.cx_max[index],
                                       dx_max=self.dx_max[index],
                                       ex_max=self.ex_max[index],
                                       ax_function=self.ax_function[index],
                                       bx_function=self.bx_function[index],
                                       cx_function=self.cx_function[index],
                                       dx_function=self.dx_function[index],
                                       ex_function=self.ex_function[index],
                                       ax_function_value=self.ax_function_value[index],
                                       bx_function_value=self.bx_function_value[index],
                                       cx_function_value=self.cx_function_value[index],
                                       dx_function_value=self.dx_function_value[index],
                                       ex_function_value=self.ex_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return CalibrationPeakShiftBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_shift_parameters([self.get_parameter_box(index).get_peak_shift() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_shift_parameters(Lab6TanCorrection.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_shift_parameters_item(Lab6TanCorrection.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_ax()
        self.dump_bx()
        self.dump_cx()
        self.dump_dx()
        self.dump_ex()

    def dump_ax(self): self.dump_parameter("ax")
    def dump_bx(self): self.dump_parameter("bx")
    def dump_cx(self): self.dump_parameter("cx")
    def dump_dx(self): self.dump_parameter("dx")
    def dump_ex(self): self.dump_parameter("ex")

class CalibrationPeakShiftBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 ax=0.0,
                 bx=0.0,
                 cx=0.0,
                 dx=0.0,
                 ex=0.0,
                 ax_fixed=0,
                 bx_fixed=0,
                 cx_fixed=0,
                 dx_fixed=0,
                 ex_fixed=0,
                 ax_has_min=0,
                 bx_has_min=0,
                 cx_has_min=0,
                 dx_has_min=0,
                 ex_has_min=0,
                 ax_min=0.0,
                 bx_min=0.0,
                 cx_min=0.0,
                 dx_min=0.0,
                 ex_min=0.0,
                 ax_has_max=0,
                 bx_has_max=0,
                 cx_has_max=0,
                 dx_has_max=0,
                 ex_has_max=0,
                 ax_max=0.0,
                 bx_max=0.0,
                 cx_max=0.0,
                 dx_max=0.0,
                 ex_max=0.0,
                 ax_function=0,
                 bx_function=0,
                 cx_function=0,
                 dx_function=0,
                 ex_function=0,
                 ax_function_value="",
                 bx_function_value="",
                 cx_function_value="",
                 dx_function_value="",
                 ex_function_value=""):
        super(CalibrationPeakShiftBox, self).__init__(widget=widget,
                                                      parent=parent,
                                                      index=index,
                                                      ax=ax,
                                                      bx = bx,
                                                      cx = cx,
                                                      dx = dx,
                                                      ex = ex,
                                                      ax_fixed = ax_fixed,
                                                      bx_fixed = bx_fixed,
                                                      cx_fixed = cx_fixed,
                                                      dx_fixed = dx_fixed,
                                                      ex_fixed = ex_fixed,
                                                      ax_has_min = ax_has_min,
                                                      bx_has_min = bx_has_min,
                                                      cx_has_min = cx_has_min,
                                                      dx_has_min = dx_has_min,
                                                      ex_has_min = ex_has_min,
                                                      ax_min = ax_min,
                                                      bx_min = bx_min,
                                                      cx_min = cx_min,
                                                      dx_min = dx_min,
                                                      ex_min = ex_min,
                                                      ax_has_max = ax_has_max,
                                                      bx_has_max = bx_has_max,
                                                      cx_has_max = cx_has_max,
                                                      dx_has_max = dx_has_max,
                                                      ex_has_max = ex_has_max,
                                                      ax_max = ax_max,
                                                      bx_max = bx_max,
                                                      cx_max = cx_max,
                                                      dx_max = dx_max,
                                                      ex_max = ex_max,
                                                      ax_function = ax_function,
                                                      bx_function = bx_function,
                                                      cx_function = cx_function,
                                                      dx_function = dx_function,
                                                      ex_function = ex_function,
                                                      ax_function_value = ax_function_value,
                                                      bx_function_value = bx_function_value,
                                                      cx_function_value = cx_function_value,
                                                      dx_function_value = dx_function_value,
                                                      ex_function_value = ex_function_value)

    def get_height(self):
        return 300

    def init_fields(self, **kwargs):
        self.ax = kwargs["ax"]
        self.bx = kwargs["bx"]
        self.cx = kwargs["cx"]
        self.dx = kwargs["dx"]
        self.ex = kwargs["ex"]
        self.ax_fixed = kwargs["ax_fixed"]
        self.bx_fixed = kwargs["bx_fixed"]
        self.cx_fixed = kwargs["cx_fixed"]
        self.dx_fixed = kwargs["dx_fixed"]
        self.ex_fixed = kwargs["ex_fixed"]
        self.ax_has_min = kwargs["ax_has_min"]
        self.bx_has_min = kwargs["bx_has_min"]
        self.cx_has_min = kwargs["cx_has_min"]
        self.dx_has_min = kwargs["dx_has_min"]
        self.ex_has_min = kwargs["ex_has_min"]
        self.ax_min = kwargs["ax_min"]
        self.bx_min = kwargs["bx_min"]
        self.cx_min = kwargs["cx_min"]
        self.dx_min = kwargs["dx_min"]
        self.ex_min = kwargs["ex_min"]
        self.ax_has_max = kwargs["ax_has_max"]
        self.bx_has_max = kwargs["bx_has_max"]
        self.cx_has_max = kwargs["cx_has_max"]
        self.dx_has_max = kwargs["dx_has_max"]
        self.ex_has_max = kwargs["ex_has_max"]
        self.ax_max = kwargs["ax_max"]
        self.bx_max = kwargs["bx_max"]
        self.cx_max = kwargs["cx_max"]
        self.dx_max = kwargs["dx_max"]
        self.ex_max = kwargs["ex_max"]
        self.ax_function = kwargs["ax_function"]
        self.bx_function = kwargs["bx_function"]
        self.cx_function = kwargs["cx_function"]
        self.dx_function = kwargs["dx_function"]
        self.ex_function = kwargs["ex_function"]
        self.ax_function_value = kwargs["ax_function_value"]
        self.bx_function_value = kwargs["bx_function_value"]
        self.cx_function_value = kwargs["cx_function_value"]
        self.dx_function_value = kwargs["dx_function_value"]
        self.ex_function_value = kwargs["ex_function_value"]

    def init_gui(self, container):
        OWGenericWidget.create_box_in_widget(self, container, "ax", add_callback=True)
        OWGenericWidget.create_box_in_widget(self, container, "bx", add_callback=True)
        OWGenericWidget.create_box_in_widget(self, container, "cx", add_callback=True)
        OWGenericWidget.create_box_in_widget(self, container, "dx", add_callback=True)
        OWGenericWidget.create_box_in_widget(self, container, "ex", add_callback=True)

    def callback_ax(self):
        if not self.is_on_init: self.widget.dump_ax()

    def callback_bx(self):
        if not self.is_on_init: self.widget.dump_bx()

    def callback_cx(self):
        if not self.is_on_init: self.widget.dump_cx()

    def callback_dx(self):
        if not self.is_on_init: self.widget.dump_dx()

    def callback_ex(self):
        if not self.is_on_init: self.widget.dump_ex()

    def get_basic_parameter_prefix(self):
        return Lab6TanCorrection.get_parameters_prefix()

    def set_data(self, shift_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "ax", shift_parameters.ax, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "bx", shift_parameters.bx, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "cx", shift_parameters.cx, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "dx", shift_parameters.dx, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "ex", shift_parameters.ex, value_only=True)

    def get_peak_shift(self):
        return Lab6TanCorrection(ax=OWGenericWidget.populate_parameter_in_widget(self, "ax", self.get_parameters_prefix()),
                                 bx=OWGenericWidget.populate_parameter_in_widget(self, "bx", self.get_parameters_prefix()),
                                 cx=OWGenericWidget.populate_parameter_in_widget(self, "cx", self.get_parameters_prefix()),
                                 dx=OWGenericWidget.populate_parameter_in_widget(self, "dx", self.get_parameters_prefix()),
                                 ex=OWGenericWidget.populate_parameter_in_widget(self, "ex", self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWCalibrationPeakShift()
    ow.show()
    a.exec_()
    ow.saveSettings()
