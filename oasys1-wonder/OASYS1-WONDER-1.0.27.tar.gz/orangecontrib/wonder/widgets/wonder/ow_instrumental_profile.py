import sys, copy

from orangewidget.settings import Setting

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.fit.parameters.instrument.instrumental_parameters import Caglioti


class OWInstrumentalProfile(OWGenericDiffractionPatternParametersWidget):
    name = "Instrumental Profile"
    description = "Define Instrumental Profile Parameters"
    icon = "icons/instrumental_profile.png"
    priority = 12

    U = Setting([0.0])
    V = Setting([0.0])
    W = Setting([0.0])
    U_fixed = Setting([0])
    V_fixed = Setting([0])
    W_fixed = Setting([0])
    U_has_min = Setting([0])
    V_has_min = Setting([0])
    W_has_min = Setting([0])
    U_min = Setting([0.0])
    V_min = Setting([0.0])
    W_min = Setting([0.0])
    U_has_max = Setting([0])
    V_has_max = Setting([0])
    W_has_max = Setting([0])
    U_max = Setting([0.0])
    V_max = Setting([0.0])
    W_max = Setting([0.0])
    U_function = Setting([0])
    V_function = Setting([0])
    W_function = Setting([0])
    U_function_value = Setting([""])
    V_function_value = Setting([""])
    W_function_value = Setting([""])
    a = Setting([0.0])
    b = Setting([0.0])
    c = Setting([0.0])
    a_fixed = Setting([0])
    b_fixed = Setting([0])
    c_fixed = Setting([0])
    a_has_min = Setting([0])
    b_has_min = Setting([0])
    c_has_min = Setting([0])
    a_min = Setting([0.0])
    b_min = Setting([0.0])
    c_min = Setting([0.0])
    a_has_max = Setting([0])
    b_has_max = Setting([0])
    c_has_max = Setting([0])
    a_max = Setting([0.0])
    b_max = Setting([0.0])
    c_max = Setting([0.0])
    a_function = Setting([0])
    b_function = Setting([0])
    c_function = Setting([0])
    a_function_value = Setting([""])
    b_function_value = Setting([""])
    c_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 550

    def get_parameter_name(self):
        return "Instrumental Profile"

    def get_current_dimension(self):
        return len(self.U)

    def get_parameter_box_instance(self, parameter_tab, index):
        return InstrumentalProfileBox(widget=self,
                                      parent=parameter_tab,
                                      index=index,
                                      U=self.U[index],
                                      V=self.V[index],
                                      W=self.W[index],
                                      a=self.a[index],
                                      b=self.b[index],
                                      c=self.c[index],
                                      U_fixed=self.U_fixed[index],
                                      V_fixed=self.V_fixed[index],
                                      W_fixed=self.W_fixed[index],
                                      a_fixed=self.a_fixed[index],
                                      b_fixed=self.b_fixed[index],
                                      c_fixed=self.c_fixed[index],
                                      U_has_min=self.U_has_min[index],
                                      V_has_min=self.V_has_min[index],
                                      W_has_min=self.W_has_min[index],
                                      a_has_min=self.a_has_min[index],
                                      b_has_min=self.b_has_min[index],
                                      c_has_min=self.c_has_min[index],
                                      U_min=self.U_min[index],
                                      V_min=self.V_min[index],
                                      W_min=self.W_min[index],
                                      a_min=self.a_min[index],
                                      b_min=self.b_min[index],
                                      c_min=self.c_min[index],
                                      U_has_max=self.U_has_max[index],
                                      V_has_max=self.V_has_max[index],
                                      W_has_max=self.W_has_max[index],
                                      a_has_max=self.a_has_max[index],
                                      b_has_max=self.b_has_max[index],
                                      c_has_max=self.c_has_max[index],
                                      U_max=self.U_max[index],
                                      V_max=self.V_max[index],
                                      W_max=self.W_max[index],
                                      a_max=self.a_max[index],
                                      b_max=self.b_max[index],
                                      c_max=self.c_max[index],
                                      U_function=self.U_function[index],
                                      V_function=self.V_function[index],
                                      W_function=self.W_function[index],
                                      a_function=self.a_function[index],
                                      b_function=self.b_function[index],
                                      c_function=self.c_function[index],
                                      U_function_value=self.U_function_value[index],
                                      V_function_value=self.V_function_value[index],
                                      W_function_value=self.W_function_value[index],
                                      a_function_value=self.a_function_value[index],
                                      b_function_value=self.b_function_value[index],
                                      c_function_value=self.c_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return InstrumentalProfileBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_instrumental_parameters([self.get_parameter_box(index).get_instrumental_profile() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_instrumental_parameters(Caglioti.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_instrumental_parameters_item(Caglioti.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_U()
        self.dump_V()
        self.dump_W()
        self.dump_a()
        self.dump_b()
        self.dump_c()

    def dump_U(self): self.dump_parameter("U")
    def dump_V(self): self.dump_parameter("V")
    def dump_W(self): self.dump_parameter("W")
    def dump_a(self): self.dump_parameter("a")
    def dump_b(self): self.dump_parameter("b")
    def dump_c(self): self.dump_parameter("c")

class InstrumentalProfileBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 U=0.0,
                 V=0.0,
                 W=0.0,
                 a=0.0,
                 b=0.0,
                 c=0.0,
                 U_fixed=0,
                 V_fixed=0,
                 W_fixed=0,
                 a_fixed=0,
                 b_fixed=0,
                 c_fixed=0,
                 U_has_min=0,
                 V_has_min=0,
                 W_has_min=0,
                 a_has_min=0,
                 b_has_min=0,
                 c_has_min=0,
                 U_min=0.0,
                 V_min=0.0,
                 W_min=0.0,
                 a_min=0.0,
                 b_min=0.0,
                 c_min=0.0,
                 U_has_max=0,
                 V_has_max=0,
                 W_has_max=0,
                 a_has_max=0,
                 b_has_max=0,
                 c_has_max=0,
                 U_max=0.0,
                 V_max=0.0,
                 W_max=0.0,
                 a_max=0.0,
                 b_max=0.0,
                 c_max=0.0,
                 U_function=0,
                 V_function=0,
                 W_function=0,
                 a_function=0,
                 b_function=0,
                 c_function=0,
                 U_function_value="",
                 V_function_value="",
                 W_function_value="",
                 a_function_value="",
                 b_function_value="",
                 c_function_value=""):
        super(InstrumentalProfileBox, self).__init__(widget=widget,
                                                     parent=parent,
                                                     index=index,
                                                     U=U,
                                                     V = V,
                                                     W = W,
                                                     a = a,
                                                     b = b,
                                                     c = c,
                                                     U_fixed = U_fixed,
                                                     V_fixed = V_fixed,
                                                     W_fixed = W_fixed,
                                                     a_fixed = a_fixed,
                                                     b_fixed = b_fixed,
                                                     c_fixed = c_fixed,
                                                     U_has_min = U_has_min,
                                                     V_has_min = V_has_min,
                                                     W_has_min = W_has_min,
                                                     a_has_min = a_has_min,
                                                     b_has_min = b_has_min,
                                                     c_has_min = c_has_min,
                                                     U_min = U_min,
                                                     V_min = V_min,
                                                     W_min = W_min,
                                                     a_min = a_min,
                                                     b_min = b_min,
                                                     c_min = c_min,
                                                     U_has_max = U_has_max,
                                                     V_has_max = V_has_max,
                                                     W_has_max = W_has_max,
                                                     a_has_max = a_has_max,
                                                     b_has_max = b_has_max,
                                                     c_has_max = c_has_max,
                                                     U_max = U_max,
                                                     V_max = V_max,
                                                     W_max = W_max,
                                                     a_max = a_max,
                                                     b_max = b_max,
                                                     c_max = c_max,
                                                     U_function = U_function,
                                                     V_function = V_function,
                                                     W_function = W_function,
                                                     a_function = a_function,
                                                     b_function = b_function,
                                                     c_function = c_function,
                                                     U_function_value = U_function_value,
                                                     V_function_value = V_function_value,
                                                     W_function_value = W_function_value,
                                                     a_function_value = a_function_value,
                                                     b_function_value = b_function_value,
                                                     c_function_value = c_function_value)

    def get_height(self):
        return 350

    def init_fields(self, **kwargs):
        self.U = kwargs["U"]
        self.V = kwargs["V"]
        self.W = kwargs["W"]
        self.a = kwargs["a"]
        self.b = kwargs["b"]
        self.c = kwargs["c"]
        self.U_fixed = kwargs["U_fixed"]
        self.V_fixed = kwargs["V_fixed"]
        self.W_fixed = kwargs["W_fixed"]
        self.a_fixed = kwargs["a_fixed"]
        self.b_fixed = kwargs["b_fixed"]
        self.c_fixed = kwargs["c_fixed"]
        self.U_has_min = kwargs["U_has_min"]
        self.V_has_min = kwargs["V_has_min"]
        self.W_has_min = kwargs["W_has_min"]
        self.a_has_min = kwargs["a_has_min"]
        self.b_has_min = kwargs["b_has_min"]
        self.c_has_min = kwargs["c_has_min"]
        self.U_min = kwargs["U_min"]
        self.V_min = kwargs["V_min"]
        self.W_min = kwargs["W_min"]
        self.a_min = kwargs["a_min"]
        self.b_min = kwargs["b_min"]
        self.c_min = kwargs["c_min"]
        self.U_has_max = kwargs["U_has_max"]
        self.V_has_max = kwargs["V_has_max"]
        self.W_has_max = kwargs["W_has_max"]
        self.a_has_max = kwargs["a_has_max"]
        self.b_has_max = kwargs["b_has_max"]
        self.c_has_max = kwargs["c_has_max"]
        self.U_max = kwargs["U_max"]
        self.V_max = kwargs["V_max"]
        self.W_max = kwargs["W_max"]
        self.a_max = kwargs["a_max"]
        self.b_max = kwargs["b_max"]
        self.c_max = kwargs["c_max"]
        self.U_function = kwargs["U_function"]
        self.V_function = kwargs["V_function"]
        self.W_function = kwargs["W_function"]
        self.a_function = kwargs["a_function"]
        self.b_function = kwargs["b_function"]
        self.c_function = kwargs["c_function"]
        self.U_function_value = kwargs["U_function_value"]
        self.V_function_value = kwargs["V_function_value"]
        self.W_function_value = kwargs["W_function_value"]
        self.a_function_value = kwargs["a_function_value"]
        self.b_function_value = kwargs["b_function_value"]
        self.c_function_value = kwargs["c_function_value"]

    def init_gui(self, container):
        caglioti_box_1 = gui.widgetBox(container, "Caglioti's FWHM", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20)
        caglioti_box_2 = gui.widgetBox(container, "Caglioti's \u03b7", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20)

        OWGenericWidget.create_box_in_widget(self, caglioti_box_1, "U", add_callback=True, trim=35)
        OWGenericWidget.create_box_in_widget(self, caglioti_box_1, "V", add_callback=True, trim=35)
        OWGenericWidget.create_box_in_widget(self, caglioti_box_1, "W", add_callback=True, trim=35)
        OWGenericWidget.create_box_in_widget(self, caglioti_box_2, "a", add_callback=True, trim=35)
        OWGenericWidget.create_box_in_widget(self, caglioti_box_2, "b", add_callback=True, trim=35)
        OWGenericWidget.create_box_in_widget(self, caglioti_box_2, "c", add_callback=True, trim=35)

    def callback_U(self):
        if not self.is_on_init: self.widget.dump_U()

    def callback_V(self):
        if not self.is_on_init: self.widget.dump_V()

    def callback_W(self):
        if not self.is_on_init: self.widget.dump_W()

    def callback_a(self):
        if not self.is_on_init: self.widget.dump_a()

    def callback_b(self):
        if not self.is_on_init: self.widget.dump_b()

    def callback_c(self):
        if not self.is_on_init: self.widget.dump_c()

    def get_basic_parameter_prefix(self):
        return Caglioti.get_parameters_prefix()

    def set_data(self, instrumental_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "U", instrumental_parameters.U, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "V", instrumental_parameters.V, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "W", instrumental_parameters.W, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "a", instrumental_parameters.a, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "b", instrumental_parameters.b, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c", instrumental_parameters.c, value_only=True)

    def get_instrumental_profile(self):
        return Caglioti(U=OWGenericWidget.populate_parameter_in_widget(self, "U", self.get_parameters_prefix()),
                        V=OWGenericWidget.populate_parameter_in_widget(self, "V", self.get_parameters_prefix()),
                        W=OWGenericWidget.populate_parameter_in_widget(self, "W", self.get_parameters_prefix()),
                        a=OWGenericWidget.populate_parameter_in_widget(self, "a", self.get_parameters_prefix()),
                        b=OWGenericWidget.populate_parameter_in_widget(self, "b", self.get_parameters_prefix()),
                        c=OWGenericWidget.populate_parameter_in_widget(self, "c", self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWInstrumentalProfile()
    ow.show()
    a.exec_()
    ow.saveSettings()
