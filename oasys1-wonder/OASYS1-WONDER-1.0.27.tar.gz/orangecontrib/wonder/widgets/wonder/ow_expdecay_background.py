import sys

from orangewidget.settings import Setting

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.fit.parameters.instrument.background_parameters import ExpDecayBackground

class OWExpDecayBackground(OWGenericDiffractionPatternParametersWidget):
    name = "ExpDecay Background"
    description = "Define ExpDecay background"
    icon = "icons/expdecay_background.png"
    priority = 11

    a0 = Setting([0.0])
    b0 = Setting([0.0])
    a1 = Setting([0.0])
    b1 = Setting([0.0])
    a2 = Setting([0.0])
    b2 = Setting([0.0])
    a0_fixed = Setting([0])
    b0_fixed = Setting([0])
    a1_fixed = Setting([0])
    b1_fixed = Setting([0])
    a2_fixed = Setting([0])
    b2_fixed = Setting([0])
    a0_has_min = Setting([0])
    b0_has_min = Setting([0])
    a1_has_min = Setting([0])
    b1_has_min = Setting([0])
    a2_has_min = Setting([0])
    b2_has_min = Setting([0])
    a0_min = Setting([0.0])
    b0_min = Setting([0.0])
    a1_min = Setting([0.0])
    b1_min = Setting([0.0])
    a2_min = Setting([0.0])
    b2_min = Setting([0.0])
    a0_has_max = Setting([0])
    b0_has_max = Setting([0])
    a1_has_max = Setting([0])
    b1_has_max = Setting([0])
    a2_has_max = Setting([0])
    b2_has_max = Setting([0])
    a0_max = Setting([0.0])
    b0_max = Setting([0.0])
    a1_max = Setting([0.0])
    b1_max = Setting([0.0])
    a2_max = Setting([0.0])
    b2_max = Setting([0.0])
    a0_function = Setting([0])
    b0_function = Setting([0])
    a1_function = Setting([0])
    b1_function = Setting([0])
    a2_function = Setting([0])
    b2_function = Setting([0])
    a0_function_value = Setting([""])
    b0_function_value = Setting([""])
    a1_function_value = Setting([""])
    b1_function_value = Setting([""])
    a2_function_value = Setting([""])
    b2_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 500

    def get_parameter_name(self):
        return "Exponential Background"

    def get_current_dimension(self):
        return len(self.a0)

    def get_parameter_box_instance(self, parameter_tab, index):
        return ExpDecayBackgroundBox(widget=self,
                                     parent=parameter_tab,
                                     index=index,
                                     a0=self.a0[index],
                                     b0=self.b0[index],
                                     a1=self.a1[index],
                                     b1=self.b1[index],
                                     a2=self.a2[index],
                                     b2=self.b2[index],
                                     a0_fixed=self.a0_fixed[index],
                                     b0_fixed=self.b0_fixed[index],
                                     a1_fixed=self.a1_fixed[index],
                                     b1_fixed=self.b1_fixed[index],
                                     a2_fixed=self.a2_fixed[index],
                                     b2_fixed=self.b2_fixed[index],
                                     a0_has_min=self.a0_has_min[index],
                                     b0_has_min=self.b0_has_min[index],
                                     a1_has_min=self.a1_has_min[index],
                                     b1_has_min=self.b1_has_min[index],
                                     a2_has_min=self.a2_has_min[index],
                                     b2_has_min=self.b2_has_min[index],
                                     a0_min=self.a0_min[index],
                                     b0_min=self.b0_min[index],
                                     a1_min=self.a1_min[index],
                                     b1_min=self.b1_min[index],
                                     a2_min=self.a2_min[index],
                                     b2_min=self.b2_min[index],
                                     a0_has_max=self.a0_has_max[index],
                                     b0_has_max=self.b0_has_max[index],
                                     a1_has_max=self.a1_has_max[index],
                                     b1_has_max=self.b1_has_max[index],
                                     a2_has_max=self.a2_has_max[index],
                                     b2_has_max=self.b2_has_max[index],
                                     a0_max=self.a0_max[index],
                                     b0_max=self.b0_max[index],
                                     a1_max=self.a1_max[index],
                                     b1_max=self.b1_max[index],
                                     a2_max=self.a2_max[index],
                                     b2_max=self.b2_max[index],
                                     a0_function=self.a0_function[index],
                                     b0_function=self.b0_function[index],
                                     a1_function=self.a1_function[index],
                                     b1_function=self.b1_function[index],
                                     a2_function=self.a2_function[index],
                                     b2_function=self.b2_function[index],
                                     a0_function_value=self.a0_function_value[index],
                                     b0_function_value=self.b0_function_value[index],
                                     a1_function_value=self.a1_function_value[index],
                                     b1_function_value=self.b1_function_value[index],
                                     a2_function_value=self.a2_function_value[index],
                                     b2_function_value=self.b2_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return ExpDecayBackgroundBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_background_parameters([self.get_parameter_box(index).get_background() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_background_parameters(ExpDecayBackground.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_background_parameters_item(ExpDecayBackground.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_a0()
        self.dump_b0()
        self.dump_a1()
        self.dump_b1()
        self.dump_a2()
        self.dump_b2()

    def dump_a0(self): self.dump_parameter("a0")
    def dump_b0(self): self.dump_parameter("b0")
    def dump_a1(self): self.dump_parameter("a1")
    def dump_b1(self): self.dump_parameter("b1")
    def dump_a2(self): self.dump_parameter("a2")
    def dump_b2(self): self.dump_parameter("b2")

class ExpDecayBackgroundBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 a0=0.0,
                 b0=0.0,
                 a1=0.0,
                 b1=0.0,
                 a2=0.0,
                 b2=0.0,
                 a0_fixed=0,
                 b0_fixed=0,
                 a1_fixed=0,
                 b1_fixed=0,
                 a2_fixed=0,
                 b2_fixed=0,
                 a0_has_min=0,
                 b0_has_min=0,
                 a1_has_min=0,
                 b1_has_min=0,
                 a2_has_min=0,
                 b2_has_min=0,
                 a0_min=0.0,
                 b0_min=0.0,
                 a1_min=0.0,
                 b1_min=0.0,
                 a2_min=0.0,
                 b2_min=0.0,
                 a0_has_max=0,
                 b0_has_max=0,
                 a1_has_max=0,
                 b1_has_max=0,
                 a2_has_max=0,
                 b2_has_max=0,
                 a0_max=0.0,
                 b0_max=0.0,
                 a1_max=0.0,
                 b1_max=0.0,
                 a2_max=0.0,
                 b2_max=0.0,
                 a0_function=0,
                 b0_function=0,
                 a1_function=0,
                 b1_function=0,
                 a2_function=0,
                 b2_function=0,
                 a0_function_value="",
                 b0_function_value="",
                 a1_function_value="",
                 b1_function_value="",
                 a2_function_value="",
                 b2_function_value=""):
        super(ExpDecayBackgroundBox, self).__init__(widget=widget,
                                                    parent=parent,
                                                    index=index,
                                                    a0=a0,
                                                    b0 = b0,
                                                    a1 = a1,
                                                    b1 = b1,
                                                    a2 = a2,
                                                    b2 = b2,
                                                    a0_fixed = a0_fixed,
                                                    b0_fixed = b0_fixed,
                                                    a1_fixed = a1_fixed,
                                                    b1_fixed = b1_fixed,
                                                    a2_fixed = a2_fixed,
                                                    b2_fixed = b2_fixed,
                                                    a0_has_min = a0_has_min,
                                                    b0_has_min = b0_has_min,
                                                    a1_has_min = a1_has_min,
                                                    b1_has_min = b1_has_min,
                                                    a2_has_min = a2_has_min,
                                                    b2_has_min = b2_has_min,
                                                    a0_min = a0_min,
                                                    b0_min = b0_min,
                                                    a1_min = a1_min,
                                                    b1_min = b1_min,
                                                    a2_min = a2_min,
                                                    b2_min = b2_min,
                                                    a0_has_max = a0_has_max,
                                                    b0_has_max = b0_has_max,
                                                    a1_has_max = a1_has_max,
                                                    b1_has_max = b1_has_max,
                                                    a2_has_max = a2_has_max,
                                                    b2_has_max = b2_has_max,
                                                    a0_max = a0_max,
                                                    b0_max = b0_max,
                                                    a1_max = a1_max,
                                                    b1_max = b1_max,
                                                    a2_max = a2_max,
                                                    b2_max = b2_max,
                                                    a0_function = a0_function,
                                                    b0_function = b0_function,
                                                    a1_function = a1_function,
                                                    b1_function = b1_function,
                                                    a2_function = a2_function,
                                                    b2_function = b2_function,
                                                    a0_function_value = a0_function_value,
                                                    b0_function_value = b0_function_value,
                                                    a1_function_value = a1_function_value,
                                                    b1_function_value = b1_function_value,
                                                    a2_function_value = a2_function_value,
                                                    b2_function_value = b2_function_value)

    def get_height(self):
        return 300

    def init_fields(self, **kwargs):
        self.a0 = kwargs["a0"]
        self.b0 = kwargs["b0"]
        self.a1 = kwargs["a1"]
        self.b1 = kwargs["b1"]
        self.a2 = kwargs["a2"]
        self.b2 = kwargs["b2"]
        self.a0_fixed = kwargs["a0_fixed"]
        self.b0_fixed = kwargs["b0_fixed"]
        self.a1_fixed = kwargs["a1_fixed"]
        self.b1_fixed = kwargs["b1_fixed"]
        self.a2_fixed = kwargs["a2_fixed"]
        self.b2_fixed = kwargs["b2_fixed"]
        self.a0_has_min = kwargs["a0_has_min"]
        self.b0_has_min = kwargs["b0_has_min"]
        self.a1_has_min = kwargs["a1_has_min"]
        self.b1_has_min = kwargs["b1_has_min"]
        self.a2_has_min = kwargs["a2_has_min"]
        self.b2_has_min = kwargs["b2_has_min"]
        self.a0_min = kwargs["a0_min"]
        self.b0_min = kwargs["b0_min"]
        self.a1_min = kwargs["a1_min"]
        self.b1_min = kwargs["b1_min"]
        self.a2_min = kwargs["a2_min"]
        self.b2_min = kwargs["b2_min"]
        self.a0_has_max = kwargs["a0_has_max"]
        self.b0_has_max = kwargs["b0_has_max"]
        self.a1_has_max = kwargs["a1_has_max"]
        self.b1_has_max = kwargs["b1_has_max"]
        self.a2_has_max = kwargs["a2_has_max"]
        self.b2_has_max = kwargs["b2_has_max"]
        self.a0_max = kwargs["a0_max"]
        self.b0_max = kwargs["b0_max"]
        self.a1_max = kwargs["a1_max"]
        self.b1_max = kwargs["b1_max"]
        self.a2_max = kwargs["a2_max"]
        self.b2_max = kwargs["b2_max"]
        self.a0_function = kwargs["a0_function"]
        self.b0_function = kwargs["b0_function"]
        self.a1_function = kwargs["a1_function"]
        self.b1_function = kwargs["b1_function"]
        self.a2_function = kwargs["a2_function"]
        self.b2_function = kwargs["b2_function"]
        self.a0_function_value = kwargs["a0_function_value"]
        self.b0_function_value = kwargs["b0_function_value"]
        self.a1_function_value = kwargs["a1_function_value"]
        self.b1_function_value = kwargs["b1_function_value"]
        self.a2_function_value = kwargs["a2_function_value"]
        self.b2_function_value = kwargs["b2_function_value"]

    def init_gui(self, container):
        OWGenericWidget.create_box_in_widget(self, container, "a0", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "b0", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "a1", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "b1", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "a2", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "b2", add_callback=True, trim=25)

    def callback_a0(self):
        if not self.is_on_init: self.widget.dump_a0()

    def callback_b0(self):
        if not self.is_on_init: self.widget.dump_b0()

    def callback_a1(self):
        if not self.is_on_init: self.widget.dump_a1()

    def callback_b1(self):
        if not self.is_on_init: self.widget.dump_b1()

    def callback_a2(self):
        if not self.is_on_init: self.widget.dump_a2()

    def callback_b2(self):
        if not self.is_on_init: self.widget.dump_b2()


    def get_basic_parameter_prefix(self):
        return ExpDecayBackground.get_parameters_prefix()

    def set_data(self, background_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "a0", background_parameters.a0, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "b0", background_parameters.b0, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "a1", background_parameters.a1, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "b1", background_parameters.b1, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "a2", background_parameters.a2, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "b2", background_parameters.b2, value_only=True)

    def get_background(self):
        return ExpDecayBackground(a0=OWGenericWidget.populate_parameter_in_widget(self, "a0", self.get_parameters_prefix()),
                                  b0=OWGenericWidget.populate_parameter_in_widget(self, "b0", self.get_parameters_prefix()),
                                  a1=OWGenericWidget.populate_parameter_in_widget(self, "a1", self.get_parameters_prefix()),
                                  b1=OWGenericWidget.populate_parameter_in_widget(self, "b1", self.get_parameters_prefix()),
                                  a2=OWGenericWidget.populate_parameter_in_widget(self, "a2", self.get_parameters_prefix()),
                                  b2=OWGenericWidget.populate_parameter_in_widget(self, "b2", self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWExpDecayBackground()
    ow.show()
    a.exec_()
    ow.saveSettings()
