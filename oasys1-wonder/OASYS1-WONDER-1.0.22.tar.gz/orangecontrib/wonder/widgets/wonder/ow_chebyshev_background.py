import sys

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.fit.parameters.instrument.background_parameters import ChebyshevBackground

class OWChebyshevBackground(OWGenericDiffractionPatternParametersWidget):

    name = "Chebyshev Background"
    description = "Define Chebyshev background"
    icon = "icons/chebyshev_background.png"
    priority = 10

    c0                = Setting([0.0])
    c1                = Setting([0.0])
    c2                = Setting([0.0])
    c3                = Setting([0.0])
    c4                = Setting([0.0])
    c5                = Setting([0.0])
    c6                = Setting([0.0])
    c7                = Setting([0.0])
    c8                = Setting([0.0])
    c9                = Setting([0.0])
    c0_fixed          = Setting([0])
    c1_fixed          = Setting([0])
    c2_fixed          = Setting([0])
    c3_fixed          = Setting([0])
    c4_fixed          = Setting([0])
    c5_fixed          = Setting([0])
    c6_fixed          = Setting([1])
    c7_fixed          = Setting([1])
    c8_fixed          = Setting([1])
    c9_fixed          = Setting([1])
    c0_has_min        = Setting([0])
    c1_has_min        = Setting([0])
    c2_has_min        = Setting([0])
    c3_has_min        = Setting([0])
    c4_has_min        = Setting([0])
    c5_has_min        = Setting([0])
    c6_has_min        = Setting([0])
    c7_has_min        = Setting([0])
    c8_has_min        = Setting([0])
    c9_has_min        = Setting([0])
    c0_min            = Setting([0.0])
    c1_min            = Setting([0.0])
    c2_min            = Setting([0.0])
    c3_min            = Setting([0.0])
    c4_min            = Setting([0.0])
    c5_min            = Setting([0.0])
    c6_min            = Setting([0.0])
    c7_min            = Setting([0.0])
    c8_min            = Setting([0.0])
    c9_min            = Setting([0.0])
    c0_has_max        = Setting([0])
    c1_has_max        = Setting([0])
    c2_has_max        = Setting([0])
    c3_has_max        = Setting([0])
    c4_has_max        = Setting([0])
    c5_has_max        = Setting([0])
    c6_has_max        = Setting([0])
    c7_has_max        = Setting([0])
    c8_has_max        = Setting([0])
    c9_has_max        = Setting([0])
    c0_max            = Setting([0.0])
    c1_max            = Setting([0.0])
    c2_max            = Setting([0.0])
    c3_max            = Setting([0.0])
    c4_max            = Setting([0.0])
    c5_max            = Setting([0.0])
    c6_max            = Setting([0.0])
    c7_max            = Setting([0.0])
    c8_max            = Setting([0.0])
    c9_max            = Setting([0.0])
    c0_function       = Setting([0])
    c1_function       = Setting([0])
    c2_function       = Setting([0])
    c3_function       = Setting([0])
    c4_function       = Setting([0])
    c5_function       = Setting([0])
    c6_function       = Setting([0])
    c7_function       = Setting([0])
    c8_function       = Setting([0])
    c9_function       = Setting([0])
    c0_function_value = Setting([""])
    c1_function_value = Setting([""])
    c2_function_value = Setting([""])
    c3_function_value = Setting([""])
    c4_function_value = Setting([""])
    c5_function_value = Setting([""])
    c6_function_value = Setting([""])
    c7_function_value = Setting([""])
    c8_function_value = Setting([""])
    c9_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 600

    def get_parameter_name(self):
        return "Chebyshev Background"

    def get_current_dimension(self):
        return len(self.c0)

    def get_parameter_box_instance(self, parameter_tab, index):
        return ChebyshevBackgroundBox(widget=self,
                                      parent=parameter_tab,
                                      index = index,
                                      c0                = self.c0[index],
                                      c1                = self.c1[index],
                                      c2                = self.c2[index],
                                      c3                = self.c3[index],
                                      c4                = self.c4[index],
                                      c5                = self.c5[index],
                                      c6                = self.c6[index],
                                      c7                = self.c7[index],
                                      c8                = self.c8[index],
                                      c9                = self.c9[index],
                                      c0_fixed          = self.c0_fixed[index],
                                      c1_fixed          = self.c1_fixed[index],
                                      c2_fixed          = self.c2_fixed[index],
                                      c3_fixed          = self.c3_fixed[index],
                                      c4_fixed          = self.c4_fixed[index],
                                      c5_fixed          = self.c5_fixed[index],
                                      c6_fixed          = self.c6_fixed[index],
                                      c7_fixed          = self.c7_fixed[index],
                                      c8_fixed          = self.c8_fixed[index],
                                      c9_fixed          = self.c9_fixed[index],
                                      c0_has_min        = self.c0_has_min[index],
                                      c1_has_min        = self.c1_has_min[index],
                                      c2_has_min        = self.c2_has_min[index],
                                      c3_has_min        = self.c3_has_min[index],
                                      c4_has_min        = self.c4_has_min[index],
                                      c5_has_min        = self.c5_has_min[index],
                                      c6_has_min        = self.c6_has_min[index],
                                      c7_has_min        = self.c7_has_min[index],
                                      c8_has_min        = self.c8_has_min[index],
                                      c9_has_min        = self.c9_has_min[index],
                                      c0_min            = self.c0_min[index],
                                      c1_min            = self.c1_min[index],
                                      c2_min            = self.c2_min[index],
                                      c3_min            = self.c3_min[index],
                                      c4_min            = self.c4_min[index],
                                      c5_min            = self.c5_min[index],
                                      c6_min            = self.c6_min[index],
                                      c7_min            = self.c7_min[index],
                                      c8_min            = self.c8_min[index],
                                      c9_min            = self.c9_min[index],
                                      c0_has_max        = self.c0_has_max[index],
                                      c1_has_max        = self.c1_has_max[index],
                                      c2_has_max        = self.c2_has_max[index],
                                      c3_has_max        = self.c3_has_max[index],
                                      c4_has_max        = self.c4_has_max[index],
                                      c5_has_max        = self.c5_has_max[index],
                                      c6_has_max        = self.c6_has_max[index],
                                      c7_has_max        = self.c7_has_max[index],
                                      c8_has_max        = self.c8_has_max[index],
                                      c9_has_max        = self.c9_has_max[index],
                                      c0_max            = self.c0_max[index],
                                      c1_max            = self.c1_max[index],
                                      c2_max            = self.c2_max[index],
                                      c3_max            = self.c3_max[index],
                                      c4_max            = self.c4_max[index],
                                      c5_max            = self.c5_max[index],
                                      c6_max            = self.c6_max[index],
                                      c7_max            = self.c7_max[index],
                                      c8_max            = self.c8_max[index],
                                      c9_max            = self.c9_max[index],
                                      c0_function       = self.c0_function[index],
                                      c1_function       = self.c1_function[index],
                                      c2_function       = self.c2_function[index],
                                      c3_function       = self.c3_function[index],
                                      c4_function       = self.c4_function[index],
                                      c5_function       = self.c5_function[index],
                                      c6_function       = self.c6_function[index],
                                      c7_function       = self.c7_function[index],
                                      c8_function       = self.c8_function[index],
                                      c9_function       = self.c9_function[index],
                                      c0_function_value = self.c0_function_value[index],
                                      c1_function_value = self.c1_function_value[index],
                                      c2_function_value = self.c2_function_value[index],
                                      c3_function_value = self.c3_function_value[index],
                                      c4_function_value = self.c4_function_value[index],
                                      c5_function_value = self.c5_function_value[index],
                                      c6_function_value = self.c6_function_value[index],
                                      c7_function_value = self.c7_function_value[index],
                                      c8_function_value = self.c8_function_value[index],
                                      c9_function_value = self.c9_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return ChebyshevBackground(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_background_parameters([self.get_parameter_box(index).get_background() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_background_parameters(ChebyshevBackground.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_background_parameters_item(ChebyshevBackground.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_c0()
        self.dump_c1()
        self.dump_c2()
        self.dump_c3()
        self.dump_c4()
        self.dump_c5()
        self.dump_c6()
        self.dump_c7()
        self.dump_c8()
        self.dump_c9()

    def dump_c0(self): self.dump_parameter("c0")
    def dump_c1(self): self.dump_parameter("c1")
    def dump_c2(self): self.dump_parameter("c2")
    def dump_c3(self): self.dump_parameter("c3")
    def dump_c4(self): self.dump_parameter("c4")
    def dump_c5(self): self.dump_parameter("c5")
    def dump_c6(self): self.dump_parameter("c6")
    def dump_c7(self): self.dump_parameter("c7")
    def dump_c8(self): self.dump_parameter("c8")
    def dump_c9(self): self.dump_parameter("c9")

class ChebyshevBackgroundBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index = 0,
                 c0                = 0.0,
                 c1                = 0.0,
                 c2                = 0.0,
                 c3                = 0.0,
                 c4                = 0.0,
                 c5                = 0.0,
                 c6                = 0.0,
                 c7                = 0.0,
                 c8                = 0.0,
                 c9                = 0.0,
                 c0_fixed          = 0,
                 c1_fixed          = 0,
                 c2_fixed          = 0,
                 c3_fixed          = 0,
                 c4_fixed          = 0,
                 c5_fixed          = 0,
                 c6_fixed          = 1,
                 c7_fixed          = 1,
                 c8_fixed          = 1,
                 c9_fixed          = 1,
                 c0_has_min        = 0,
                 c1_has_min        = 0,
                 c2_has_min        = 0,
                 c3_has_min        = 0,
                 c4_has_min        = 0,
                 c5_has_min        = 0,
                 c6_has_min        = 0,
                 c7_has_min        = 0,
                 c8_has_min        = 0,
                 c9_has_min        = 0,
                 c0_min            = 0.0,
                 c1_min            = 0.0,
                 c2_min            = 0.0,
                 c3_min            = 0.0,
                 c4_min            = 0.0,
                 c5_min            = 0.0,
                 c6_min            = 0.0,
                 c7_min            = 0.0,
                 c8_min            = 0.0,
                 c9_min            = 0.0,
                 c0_has_max        = 0,
                 c1_has_max        = 0,
                 c2_has_max        = 0,
                 c3_has_max        = 0,
                 c4_has_max        = 0,
                 c5_has_max        = 0,
                 c6_has_max        = 0,
                 c7_has_max        = 0,
                 c8_has_max        = 0,
                 c9_has_max        = 0,
                 c0_max            = 0.0,
                 c1_max            = 0.0,
                 c2_max            = 0.0,
                 c3_max            = 0.0,
                 c4_max            = 0.0,
                 c5_max            = 0.0,
                 c6_max            = 0.0,
                 c7_max            = 0.0,
                 c8_max            = 0.0,
                 c9_max            = 0.0,
                 c0_function       = 0,
                 c1_function       = 0,
                 c2_function       = 0,
                 c3_function       = 0,
                 c4_function       = 0,
                 c5_function       = 0,
                 c6_function       = 0,
                 c7_function       = 0,
                 c8_function       = 0,
                 c9_function       = 0,
                 c0_function_value = "",
                 c1_function_value = "",
                 c2_function_value = "",
                 c3_function_value = "",
                 c4_function_value = "",
                 c5_function_value = "",
                 c6_function_value = "",
                 c7_function_value = "",
                 c8_function_value = "",
                 c9_function_value = ""):
        super(ChebyshevBackgroundBox, self).__init__(widget=widget,
                                                     parent=parent,
                                                     index=index,
                                                     c0=c0,
                                                     c1 = c1,
                                                     c2 = c2,
                                                     c3 = c3,
                                                     c4 = c4,
                                                     c5 = c5,
                                                     c6 = c6,
                                                     c7 = c7,
                                                     c8 = c8,
                                                     c9 = c9,
                                                     c0_fixed = c0_fixed,
                                                     c1_fixed = c1_fixed,
                                                     c2_fixed = c2_fixed,
                                                     c3_fixed = c3_fixed,
                                                     c4_fixed = c4_fixed,
                                                     c5_fixed = c5_fixed,
                                                     c6_fixed = c6_fixed,
                                                     c7_fixed = c7_fixed,
                                                     c8_fixed = c8_fixed,
                                                     c9_fixed = c9_fixed,
                                                     c0_has_min = c0_has_min,
                                                     c1_has_min = c1_has_min,
                                                     c2_has_min = c2_has_min,
                                                     c3_has_min = c3_has_min,
                                                     c4_has_min = c4_has_min,
                                                     c5_has_min = c5_has_min,
                                                     c6_has_min = c6_has_min,
                                                     c7_has_min = c7_has_min,
                                                     c8_has_min = c8_has_min,
                                                     c9_has_min = c9_has_min,
                                                     c0_min = c0_min,
                                                     c1_min = c1_min,
                                                     c2_min = c2_min,
                                                     c3_min = c3_min,
                                                     c4_min = c4_min,
                                                     c5_min = c5_min,
                                                     c6_min = c6_min,
                                                     c7_min = c7_min,
                                                     c8_min = c8_min,
                                                     c9_min = c9_min,
                                                     c0_has_max = c0_has_max,
                                                     c1_has_max = c1_has_max,
                                                     c2_has_max = c2_has_max,
                                                     c3_has_max = c3_has_max,
                                                     c4_has_max = c4_has_max,
                                                     c5_has_max = c5_has_max,
                                                     c6_has_max = c6_has_max,
                                                     c7_has_max = c7_has_max,
                                                     c8_has_max = c8_has_max,
                                                     c9_has_max = c9_has_max,
                                                     c0_max = c0_max,
                                                     c1_max = c1_max,
                                                     c2_max = c2_max,
                                                     c3_max = c3_max,
                                                     c4_max = c4_max,
                                                     c5_max = c5_max,
                                                     c6_max = c6_max,
                                                     c7_max = c7_max,
                                                     c8_max = c8_max,
                                                     c9_max = c9_max,
                                                     c0_function = c0_function,
                                                     c1_function = c1_function,
                                                     c2_function = c2_function,
                                                     c3_function = c3_function,
                                                     c4_function = c4_function,
                                                     c5_function = c5_function,
                                                     c6_function = c6_function,
                                                     c7_function = c7_function,
                                                     c8_function = c8_function,
                                                     c9_function = c9_function,
                                                     c0_function_value = c0_function_value,
                                                     c1_function_value = c1_function_value,
                                                     c2_function_value = c2_function_value,
                                                     c3_function_value = c3_function_value,
                                                     c4_function_value = c4_function_value,
                                                     c5_function_value = c5_function_value,
                                                     c6_function_value = c6_function_value,
                                                     c7_function_value = c7_function_value,
                                                     c8_function_value = c8_function_value,
                                                     c9_function_value = c9_function_value)

    def get_height(self):
        return 400

    def init_fields(self, **kwargs):
        self.c0                = kwargs["c0"]
        self.c1                = kwargs["c1"]
        self.c2                = kwargs["c2"]
        self.c3                = kwargs["c3"]
        self.c4                = kwargs["c4"]
        self.c5                = kwargs["c5"]
        self.c6                = kwargs["c6"]
        self.c7                = kwargs["c7"]
        self.c8                = kwargs["c8"]
        self.c9                = kwargs["c9"]
        self.c0_fixed          = kwargs["c0_fixed"]
        self.c1_fixed          = kwargs["c1_fixed"]
        self.c2_fixed          = kwargs["c2_fixed"]
        self.c3_fixed          = kwargs["c3_fixed"]
        self.c4_fixed          = kwargs["c4_fixed"]
        self.c5_fixed          = kwargs["c5_fixed"]
        self.c6_fixed          = kwargs["c6_fixed"]
        self.c7_fixed          = kwargs["c7_fixed"]
        self.c8_fixed          = kwargs["c8_fixed"]
        self.c9_fixed          = kwargs["c9_fixed"]
        self.c0_has_min        = kwargs["c0_has_min"]
        self.c1_has_min        = kwargs["c1_has_min"]
        self.c2_has_min        = kwargs["c2_has_min"]
        self.c3_has_min        = kwargs["c3_has_min"]
        self.c4_has_min        = kwargs["c4_has_min"]
        self.c5_has_min        = kwargs["c5_has_min"]
        self.c6_has_min        = kwargs["c6_has_min"]
        self.c7_has_min        = kwargs["c7_has_min"]
        self.c8_has_min        = kwargs["c8_has_min"]
        self.c9_has_min        = kwargs["c9_has_min"]
        self.c0_min            = kwargs["c0_min"]
        self.c1_min            = kwargs["c1_min"]
        self.c2_min            = kwargs["c2_min"]
        self.c3_min            = kwargs["c3_min"]
        self.c4_min            = kwargs["c4_min"]
        self.c5_min            = kwargs["c5_min"]
        self.c6_min            = kwargs["c6_min"]
        self.c7_min            = kwargs["c7_min"]
        self.c8_min            = kwargs["c8_min"]
        self.c9_min            = kwargs["c9_min"]
        self.c0_has_max        = kwargs["c0_has_max"]
        self.c1_has_max        = kwargs["c1_has_max"]
        self.c2_has_max        = kwargs["c2_has_max"]
        self.c3_has_max        = kwargs["c3_has_max"]
        self.c4_has_max        = kwargs["c4_has_max"]
        self.c5_has_max        = kwargs["c5_has_max"]
        self.c6_has_max        = kwargs["c6_has_max"]
        self.c7_has_max        = kwargs["c7_has_max"]
        self.c8_has_max        = kwargs["c8_has_max"]
        self.c9_has_max        = kwargs["c9_has_max"]
        self.c0_max            = kwargs["c0_max"]
        self.c1_max            = kwargs["c1_max"]
        self.c2_max            = kwargs["c2_max"]
        self.c3_max            = kwargs["c3_max"]
        self.c4_max            = kwargs["c4_max"]
        self.c5_max            = kwargs["c5_max"]
        self.c6_max            = kwargs["c6_max"]
        self.c7_max            = kwargs["c7_max"]
        self.c8_max            = kwargs["c8_max"]
        self.c9_max            = kwargs["c9_max"]
        self.c0_function       = kwargs["c0_function"]
        self.c1_function       = kwargs["c1_function"]
        self.c2_function       = kwargs["c2_function"]
        self.c3_function       = kwargs["c3_function"]
        self.c4_function       = kwargs["c4_function"]
        self.c5_function       = kwargs["c5_function"]
        self.c6_function       = kwargs["c6_function"]
        self.c7_function       = kwargs["c7_function"]
        self.c8_function       = kwargs["c8_function"]
        self.c9_function       = kwargs["c9_function"]
        self.c0_function_value = kwargs["c0_function_value"]
        self.c1_function_value = kwargs["c1_function_value"]
        self.c2_function_value = kwargs["c2_function_value"]
        self.c3_function_value = kwargs["c3_function_value"]
        self.c4_function_value = kwargs["c4_function_value"]
        self.c5_function_value = kwargs["c5_function_value"]
        self.c6_function_value = kwargs["c6_function_value"]
        self.c7_function_value = kwargs["c7_function_value"]
        self.c8_function_value = kwargs["c8_function_value"]
        self.c9_function_value = kwargs["c9_function_value"]

    def init_gui(self, container):
        OWGenericWidget.create_box_in_widget(self, container, "c0", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c1", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c2", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c3", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c4", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c5", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c6", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c7", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c8", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, container, "c9", add_callback=True, trim=25)

    def callback_c0(self):
        if not self.is_on_init: self.widget.dump_c0()

    def callback_c1(self):
        if not self.is_on_init: self.widget.dump_c1()
        
    def callback_c2(self):
        if not self.is_on_init: self.widget.dump_c2()
        
    def callback_c3(self):
        if not self.is_on_init: self.widget.dump_c3()
        
    def callback_c4(self):
        if not self.is_on_init: self.widget.dump_c4()
        
    def callback_c5(self):
        if not self.is_on_init: self.widget.dump_c5()
        
    def callback_c6(self):
        if not self.is_on_init: self.widget.dump_c6()
        
    def callback_c7(self):
        if not self.is_on_init: self.widget.dump_c7()
        
    def callback_c8(self):
        if not self.is_on_init: self.widget.dump_c8()
        
    def callback_c9(self):
        if not self.is_on_init: self.widget.dump_c9()

    def get_basic_parameter_prefix(self):
        return ChebyshevBackground.get_parameters_prefix()

    def set_data(self, background_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "c0", background_parameters.c0, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c1", background_parameters.c1, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c2", background_parameters.c2, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c3", background_parameters.c3, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c4", background_parameters.c4, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c5", background_parameters.c5, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c6", background_parameters.c6, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c7", background_parameters.c7, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c8", background_parameters.c8, value_only=True)
        OWGenericWidget.populate_fields_in_widget(self, "c9", background_parameters.c9, value_only=True)

    def get_background(self):
        return ChebyshevBackground(c0=OWGenericWidget.populate_parameter_in_widget(self, "c0", self.get_parameters_prefix()),
                                   c1=OWGenericWidget.populate_parameter_in_widget(self, "c1", self.get_parameters_prefix()),
                                   c2=OWGenericWidget.populate_parameter_in_widget(self, "c2", self.get_parameters_prefix()),
                                   c3=OWGenericWidget.populate_parameter_in_widget(self, "c3", self.get_parameters_prefix()),
                                   c4=OWGenericWidget.populate_parameter_in_widget(self, "c4", self.get_parameters_prefix()),
                                   c5=OWGenericWidget.populate_parameter_in_widget(self, "c5", self.get_parameters_prefix()),
                                   c6=OWGenericWidget.populate_parameter_in_widget(self, "c6", self.get_parameters_prefix()),
                                   c7=OWGenericWidget.populate_parameter_in_widget(self, "c7", self.get_parameters_prefix()),
                                   c8=OWGenericWidget.populate_parameter_in_widget(self, "c8", self.get_parameters_prefix()),
                                   c9=OWGenericWidget.populate_parameter_in_widget(self, "c9", self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a =  QApplication(sys.argv)
    ow = OWChebyshevBackground()
    ow.show()
    a.exec_()
    ow.saveSettings()
