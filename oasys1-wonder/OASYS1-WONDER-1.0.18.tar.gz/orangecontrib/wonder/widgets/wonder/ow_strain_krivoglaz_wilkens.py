import sys, copy

from orangewidget.settings import Setting

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericPhaseParameterWidget, ParameterActivableBox
from orangecontrib.wonder.util import congruence
from orangecontrib.wonder.fit.parameters.microstructure.strain import KrivoglazWilkensModel

class OWStrainKW(OWGenericPhaseParameterWidget):
    name = "Krivoglaz-Wilkens Strain"
    description = "Define Krivoglaz-Wilkens Strain"
    icon = "icons/strain.png"
    priority = 19

    active = Setting([1])

    rho = Setting([0.0])
    rho_fixed = Setting([0])
    rho_has_min = Setting([1])
    rho_min = Setting([0.0])
    rho_has_max = Setting([0])
    rho_max = Setting([0.0])
    rho_function = Setting([0])
    rho_function_value = Setting([""])
    Re = Setting([0.0])
    Re_fixed = Setting([0])
    Re_has_min = Setting([1])
    Re_min = Setting([0.0])
    Re_has_max = Setting([0])
    Re_max = Setting([0.0])
    Re_function = Setting([0])
    Re_function_value = Setting([""])
    Ae = Setting([0.0])
    Ae_fixed = Setting([1])
    Ae_has_min = Setting([0])
    Ae_min = Setting([0.0])
    Ae_has_max = Setting([0])
    Ae_max = Setting([0.0])
    Ae_function = Setting([0])
    Ae_function_value = Setting([""])
    Be = Setting([0.0])
    Be_fixed = Setting([1])
    Be_has_min = Setting([0])
    Be_min = Setting([0.0])
    Be_has_max = Setting([0])
    Be_max = Setting([0.0])
    Be_function = Setting([0])
    Be_function_value = Setting([""])
    As = Setting([0.0])
    As_fixed = Setting([1])
    As_has_min = Setting([0])
    As_min = Setting([0.0])
    As_has_max = Setting([0])
    As_max = Setting([0.0])
    As_function = Setting([0])
    As_function_value = Setting([""])
    Bs = Setting([0.0])
    Bs_fixed = Setting([1])
    Bs_has_min = Setting([0])
    Bs_min = Setting([0.0])
    Bs_has_max = Setting([0])
    Bs_max = Setting([0.0])
    Bs_function = Setting([0])
    Bs_function_value = Setting([""])
    mix = Setting([0.5])
    mix_fixed = Setting([0])
    mix_has_min = Setting([1])
    mix_min = Setting([0.0])
    mix_has_max = Setting([1])
    mix_max = Setting([1.0])
    mix_function = Setting([0])
    mix_function_value = Setting([""])
    b = Setting([0.0])
    b_fixed = Setting([0])
    b_has_min = Setting([0])
    b_min = Setting([0.0])
    b_has_max = Setting([0])
    b_max = Setting([0.0])
    b_function = Setting([1])
    b_function_value = Setting(["phase_1_a*sqrt(3)/2"])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 520

    def get_parameter_name(self):
        return "Strain K-W"

    def get_current_dimension(self):
        return len(self.rho)

    def get_parameter_box_instance(self, parameter_tab, index):
        return StrainBox(widget=self,
                         parent=parameter_tab,
                         index=index,
                         active=self.active[index],
                         rho=self.rho[index],
                         rho_fixed=self.rho_fixed[index],
                         rho_has_min=self.rho_has_min[index],
                         rho_min=self.rho_min[index],
                         rho_has_max=self.rho_has_max[index],
                         rho_max=self.rho_max[index],
                         rho_function=self.rho_function[index],
                         rho_function_value=self.rho_function_value[index],
                         Re=self.Re[index],
                         Re_fixed=self.Re_fixed[index],
                         Re_has_min=self.Re_has_min[index],
                         Re_min=self.Re_min[index],
                         Re_has_max=self.Re_has_max[index],
                         Re_max=self.Re_max[index],
                         Re_function=self.Re_function[index],
                         Re_function_value=self.Re_function_value[index],
                         Ae=self.Ae[index],
                         Ae_fixed=self.Ae_fixed[index],
                         Ae_has_min=self.Ae_has_min[index],
                         Ae_min=self.Ae_min[index],
                         Ae_has_max=self.Ae_has_max[index],
                         Ae_max=self.Ae_max[index],
                         Ae_function=self.Ae_function[index],
                         Ae_function_value=self.Ae_function_value[index],
                         Be=self.Be[index],
                         Be_fixed=self.Be_fixed[index],
                         Be_has_min=self.Be_has_min[index],
                         Be_min=self.Be_min[index],
                         Be_has_max=self.Be_has_max[index],
                         Be_max=self.Be_max[index],
                         Be_function=self.Be_function[index],
                         Be_function_value=self.Be_function_value[index],
                         As=self.As[index],
                         As_fixed=self.As_fixed[index],
                         As_has_min=self.As_has_min[index],
                         As_min=self.As_min[index],
                         As_has_max=self.As_has_max[index],
                         As_max=self.As_max[index],
                         As_function=self.As_function[index],
                         As_function_value=self.As_function_value[index],
                         Bs=self.Bs[index],
                         Bs_fixed=self.Bs_fixed[index],
                         Bs_has_min=self.Bs_has_min[index],
                         Bs_min=self.Bs_min[index],
                         Bs_has_max=self.Bs_has_max[index],
                         Bs_max=self.Bs_max[index],
                         Bs_function=self.Bs_function[index],
                         Bs_function_value=self.Bs_function_value[index],
                         mix=self.mix[index],
                         mix_fixed=self.mix_fixed[index],
                         mix_has_min=self.mix_has_min[index],
                         mix_min=self.mix_min[index],
                         mix_has_max=self.mix_has_max[index],
                         mix_max=self.mix_max[index],
                         mix_function=self.mix_function[index],
                         mix_function_value=self.mix_function_value[index],
                         b=self.b[index],
                         b_fixed=self.b_fixed[index],
                         b_has_min=self.b_has_min[index],
                         b_min=self.b_min[index],
                         b_has_max=self.b_has_max[index],
                         b_max=self.b_max[index],
                         b_function=self.b_function[index],
                         b_function_value=self.b_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return StrainBox(widget=self, parent=parameter_tab, index=index, active=0)

    def get_parameter_array(self):
        return self.fit_global_parameters.strain_parameters

    def get_parameter_item(self, phase_index):
        return self.fit_global_parameters.get_strain_parameters(phase_index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_strain_parameters([self.get_parameter_box(index).get_strain_parameters() for index in range(self.get_current_dimension())])

    def check_input_global_parameters(self, data):
        if not data.strain_parameters is None:
            if not isinstance(data.get_strain_parameters(0), KrivoglazWilkensModel):
                raise Exception("Only 1 Strain Model is allowed in a line of fit: it should be branched before")

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpOtherSettings(self):
        self.dump_rho()
        self.dump_Re()
        self.dump_Ae()
        self.dump_Be()
        self.dump_As()
        self.dump_Bs()
        self.dump_mix()
        self.dump_b()

    def dump_rho(self): self.dump_parameter("rho")
    def dump_Re(self): self.dump_parameter("Re")
    def dump_Ae(self): self.dump_parameter("Ae")
    def dump_Be(self): self.dump_parameter("Be")
    def dump_As(self): self.dump_parameter("As")
    def dump_Bs(self): self.dump_parameter("Bs")
    def dump_mix(self): self.dump_parameter("mix")
    def dump_b(self): self.dump_parameter("b")

class StrainBox(ParameterActivableBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 active=1,
                 rho=0.0,
                 rho_fixed=0,
                 rho_has_min=1,
                 rho_min=0.0,
                 rho_has_max=0,
                 rho_max=0.0,
                 rho_function=0,
                 rho_function_value="",
                 Re=0.0,
                 Re_fixed=0,
                 Re_has_min=1,
                 Re_min=0.0,
                 Re_has_max=0,
                 Re_max=0.0,
                 Re_function=0,
                 Re_function_value="",
                 Ae=0.0,
                 Ae_fixed=1,
                 Ae_has_min=0,
                 Ae_min=0.0,
                 Ae_has_max=0,
                 Ae_max=0.0,
                 Ae_function=0,
                 Ae_function_value="",
                 Be=0.0,
                 Be_fixed=1,
                 Be_has_min=0,
                 Be_min=0.0,
                 Be_has_max=0,
                 Be_max=0.0,
                 Be_function=0,
                 Be_function_value="",
                 As=0.0,
                 As_fixed=1,
                 As_has_min=0,
                 As_min=0.0,
                 As_has_max=0,
                 As_max=0.0,
                 As_function=0,
                 As_function_value="",
                 Bs=0.0,
                 Bs_fixed=1,
                 Bs_has_min=0,
                 Bs_min=0.0,
                 Bs_has_max=0,
                 Bs_max=0.0,
                 Bs_function=0,
                 Bs_function_value="",
                 mix=0.5,
                 mix_fixed=0,
                 mix_has_min=1,
                 mix_min=0.0,
                 mix_has_max=1,
                 mix_max=1.0,
                 mix_function=0,
                 mix_function_value="",
                 b=0.0,
                 b_fixed=0,
                 b_has_min=0,
                 b_min=0.0,
                 b_has_max=0,
                 b_max=0.0,
                 b_function=1,
                 b_function_value="phase_1_a*sqrt(3/2)"):
        super(StrainBox, self).__init__(widget=widget,
                                        parent=parent,
                                        index=index,
                                        active=active,
                                        rho=rho,
                                        rho_fixed = rho_fixed,
                                        rho_has_min = rho_has_min,
                                        rho_min = rho_min,
                                        rho_has_max = rho_has_max,
                                        rho_max = rho_max,
                                        rho_function = rho_function,
                                        rho_function_value = rho_function_value,
                                        Re = Re,
                                        Re_fixed = Re_fixed,
                                        Re_has_min = Re_has_min,
                                        Re_min = Re_min,
                                        Re_has_max = Re_has_max,
                                        Re_max = Re_max,
                                        Re_function = Re_function,
                                        Re_function_value = Re_function_value,
                                        Ae = Ae,
                                        Ae_fixed = Ae_fixed,
                                        Ae_has_min = Ae_has_min,
                                        Ae_min = Ae_min,
                                        Ae_has_max = Ae_has_max,
                                        Ae_max = Ae_max,
                                        Ae_function = Ae_function,
                                        Ae_function_value = Ae_function_value,
                                        Be = Be,
                                        Be_fixed = Be_fixed,
                                        Be_has_min = Be_has_min,
                                        Be_min = Be_min,
                                        Be_has_max = Be_has_max,
                                        Be_max = Be_max,
                                        Be_function = Be_function,
                                        Be_function_value = Be_function_value,
                                        As = As,
                                        As_fixed = As_fixed,
                                        As_has_min = As_has_min,
                                        As_min = As_min,
                                        As_has_max = As_has_max,
                                        As_max = As_max,
                                        As_function = As_function,
                                        As_function_value = As_function_value,
                                        Bs = Bs,
                                        Bs_fixed = Bs_fixed,
                                        Bs_has_min = Bs_has_min,
                                        Bs_min = Bs_min,
                                        Bs_has_max = Bs_has_max,
                                        Bs_max = Bs_max,
                                        Bs_function = Bs_function,
                                        Bs_function_value = Bs_function_value,
                                        mix = mix,
                                        mix_fixed = mix_fixed,
                                        mix_has_min = mix_has_min,
                                        mix_min = mix_min,
                                        mix_has_max = mix_has_max,
                                        mix_max = mix_max,
                                        mix_function = mix_function,
                                        mix_function_value = mix_function_value,
                                        b = b,
                                        b_fixed = b_fixed,
                                        b_has_min = b_has_min,
                                        b_min = b_min,
                                        b_has_max = b_has_max,
                                        b_max = b_max,
                                        b_function = b_function,
                                        b_function_value = b_function_value)

    def init_fields(self, **kwargs):
        self.rho = kwargs["rho"]
        self.rho_fixed = kwargs["rho_fixed"]
        self.rho_has_min = kwargs["rho_has_min"]
        self.rho_min = kwargs["rho_min"]
        self.rho_has_max = kwargs["rho_has_max"]
        self.rho_max = kwargs["rho_max"]
        self.rho_function = kwargs["rho_function"]
        self.rho_function_value = kwargs["rho_function_value"]
        self.Re = kwargs["Re"]
        self.Re_fixed = kwargs["Re_fixed"]
        self.Re_has_min = kwargs["Re_has_min"]
        self.Re_min = kwargs["Re_min"]
        self.Re_has_max = kwargs["Re_has_max"]
        self.Re_max = kwargs["Re_max"]
        self.Re_function = kwargs["Re_function"]
        self.Re_function_value = kwargs["Re_function_value"]
        self.Ae = kwargs["Ae"]
        self.Ae_fixed = kwargs["Ae_fixed"]
        self.Ae_has_min = kwargs["Ae_has_min"]
        self.Ae_min = kwargs["Ae_min"]
        self.Ae_has_max = kwargs["Ae_has_max"]
        self.Ae_max = kwargs["Ae_max"]
        self.Ae_function = kwargs["Ae_function"]
        self.Ae_function_value = kwargs["Ae_function_value"]
        self.Be = kwargs["Be"]
        self.Be_fixed = kwargs["Be_fixed"]
        self.Be_has_min = kwargs["Be_has_min"]
        self.Be_min = kwargs["Be_min"]
        self.Be_has_max = kwargs["Be_has_max"]
        self.Be_max = kwargs["Be_max"]
        self.Be_function = kwargs["Be_function"]
        self.Be_function_value = kwargs["Be_function_value"]
        self.As = kwargs["As"]
        self.As_fixed = kwargs["As_fixed"]
        self.As_has_min = kwargs["As_has_min"]
        self.As_min = kwargs["As_min"]
        self.As_has_max = kwargs["As_has_max"]
        self.As_max = kwargs["As_max"]
        self.As_function = kwargs["As_function"]
        self.As_function_value = kwargs["As_function_value"]
        self.Bs = kwargs["Bs"]
        self.Bs_fixed = kwargs["Bs_fixed"]
        self.Bs_has_min = kwargs["Bs_has_min"]
        self.Bs_min = kwargs["Bs_min"]
        self.Bs_has_max = kwargs["Bs_has_max"]
        self.Bs_max = kwargs["Bs_max"]
        self.Bs_function = kwargs["Bs_function"]
        self.Bs_function_value = kwargs["Bs_function_value"]
        self.mix = kwargs["mix"]
        self.mix_fixed = kwargs["mix_fixed"]
        self.mix_has_min = kwargs["mix_has_min"]
        self.mix_min = kwargs["mix_min"]
        self.mix_has_max = kwargs["mix_has_max"]
        self.mix_max = kwargs["mix_max"]
        self.mix_function = kwargs["mix_function"]
        self.mix_function_value = kwargs["mix_function_value"]
        self.b = kwargs["b"]
        self.b_fixed = kwargs["b_fixed"]
        self.b_has_min = kwargs["b_has_min"]
        self.b_min = kwargs["b_min"]
        self.b_has_max = kwargs["b_has_max"]
        self.b_max = kwargs["b_max"]
        self.b_function = kwargs["b_function"]
        self.b_function_value = kwargs["b_function_value"]

    def init_main_box(self):
        OWGenericWidget.create_box_in_widget(self, self.main_box, "rho", add_callback=True, label="\u03c1", min_value=0.0, min_accepted=False, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "Re", add_callback=True, min_value=0.0, min_accepted=False, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "Ae", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "Be", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "As", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "Bs", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "mix", add_callback=True, min_value=0.0, min_accepted=True, max_value=1.0, max_accepted=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "b", add_callback=True, min_value=0.0, min_accepted=False, trim=25)

    def callback_rho(self):
        if not self.is_on_init: self.widget.dump_rho()

    def callback_Re(self):
        if not self.is_on_init: self.widget.dump_Re()

    def callback_Ae(self):
        if not self.is_on_init: self.widget.dump_Ae()

    def callback_Be(self):
        if not self.is_on_init: self.widget.dump_Be()

    def callback_As(self):
        if not self.is_on_init: self.widget.dump_As()

    def callback_Bs(self):
        if not self.is_on_init: self.widget.dump_Bs()

    def callback_mix(self):
        if not self.is_on_init: self.widget.dump_mix()

    def callback_b(self):
        if not self.is_on_init: self.widget.dump_b()

    def get_basic_parameter_prefix(self):
        return KrivoglazWilkensModel.get_parameters_prefix()

    def set_data(self, strain_parameters):
        if strain_parameters.rho is None and \
                strain_parameters.Re is None and \
                strain_parameters.mix is None and \
                strain_parameters.mix is None:
            OWGenericWidget.populate_fields_in_widget(self, "Ae", strain_parameters.Ae, value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "Be", strain_parameters.Be, value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "As", strain_parameters.As, value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "Bs", strain_parameters.Bs, value_only=False)
        else:
            OWGenericWidget.populate_fields_in_widget(self, "rho", strain_parameters.rho)
            OWGenericWidget.populate_fields_in_widget(self, "Re", strain_parameters.Re)
            OWGenericWidget.populate_fields_in_widget(self, "Ae", strain_parameters.Ae)
            OWGenericWidget.populate_fields_in_widget(self, "Be", strain_parameters.Be)
            OWGenericWidget.populate_fields_in_widget(self, "As", strain_parameters.As)
            OWGenericWidget.populate_fields_in_widget(self, "Bs", strain_parameters.Bs)
            OWGenericWidget.populate_fields_in_widget(self, "mix", strain_parameters.mix)
            OWGenericWidget.populate_fields_in_widget(self, "b", strain_parameters.b)

    def get_strain_parameters(self):
        if self.active == 0: return None
        else:
            if not self.rho_function == 1: congruence.checkStrictlyPositiveNumber(self.rho, "\u03c1")
            if not self.Re_function == 1: congruence.checkStrictlyPositiveNumber(self.Re, "Re")
            if not self.mix_function == 1: congruence.checkPositiveNumber(self.mix, "mix")
            if not self.b_function == 1: congruence.checkStrictlyPositiveNumber(self.b, "b")

            return KrivoglazWilkensModel(rho=OWGenericWidget.populate_parameter_in_widget(self, "rho", self.get_parameters_prefix()),
                                         Re =OWGenericWidget.populate_parameter_in_widget(self, "Re",  self.get_parameters_prefix()),
                                         Ae =OWGenericWidget.populate_parameter_in_widget(self, "Ae",  self.get_parameters_prefix()),
                                         Be =OWGenericWidget.populate_parameter_in_widget(self, "Be",  self.get_parameters_prefix()),
                                         As =OWGenericWidget.populate_parameter_in_widget(self, "As",  self.get_parameters_prefix()),
                                         Bs =OWGenericWidget.populate_parameter_in_widget(self, "Bs",  self.get_parameters_prefix()),
                                         mix=OWGenericWidget.populate_parameter_in_widget(self, "mix", self.get_parameters_prefix()),
                                         b  =OWGenericWidget.populate_parameter_in_widget(self, "b",   self.get_parameters_prefix()))

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a =  QApplication(sys.argv)
    ow = OWStrainKW()
    ow.show()
    a.exec_()
    ow.saveSettings()
