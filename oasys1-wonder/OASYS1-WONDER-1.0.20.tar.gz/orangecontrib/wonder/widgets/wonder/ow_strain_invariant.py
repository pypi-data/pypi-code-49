import sys

from PyQt5.QtWidgets import QMessageBox

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericPhaseParameterWidget, ParameterActivableBox
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.fit.parameters.microstructure.strain import InvariantPAH, InvariantPAHLaueGroup14, InvariantPAHLaueGroup13, LaueGroup

class OWStrainInvariant(OWGenericPhaseParameterWidget):
    name = "Invariant PAH Strain"
    description = "Define Invariant PAH Strain"
    icon = "icons/strain.png"
    priority = 17

    active = Setting([1])

    laue_id = Setting([13])
    aa = Setting([0.0])
    aa_fixed = Setting([0])
    aa_has_min = Setting([0])
    aa_min = Setting([0.0])
    aa_has_max = Setting([0])
    aa_max = Setting([0.0])
    aa_function = Setting([0])
    aa_function_value = Setting([""])
    bb = Setting([0.0])
    bb_fixed = Setting([0])
    bb_has_min = Setting([0])
    bb_min = Setting([0.0])
    bb_has_max = Setting([0])
    bb_max = Setting([0.0])
    bb_function = Setting([0])
    bb_function_value = Setting([""])
    e1 = Setting([0.0])
    e1_fixed = Setting([0])
    e1_has_min = Setting([0])
    e1_min = Setting([0.0])
    e1_has_max = Setting([0])
    e1_max = Setting([0.0])
    e1_function = Setting([0])
    e1_function_value = Setting([""])
    e4 = Setting([0.0])
    e4_fixed = Setting([0])
    e4_has_min = Setting([0])
    e4_min = Setting([0.0])
    e4_has_max = Setting([0])
    e4_max = Setting([0.0])
    e4_function = Setting([0])
    e4_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 500

    def get_parameter_name(self):
        return "Strain P-A-H"

    def get_current_dimension(self):
        return len(self.laue_id)

    def get_parameter_box_instance(self, parameter_tab, index):
        return StrainBox(widget=self,
                         parent=parameter_tab, 
                         index=index,
                         active=self.active[index],
                         laue_id=self.laue_id[index],
                         aa=self.aa[index],
                         aa_fixed=self.aa_fixed[index],
                         aa_has_min=self.aa_has_min[index],
                         aa_min=self.aa_min[index],
                         aa_has_max=self.aa_has_max[index],
                         aa_max=self.aa_max[index],
                         aa_function=self.aa_function[index],
                         aa_function_value=self.aa_function_value[index],
                         bb=self.bb[index],
                         bb_fixed=self.bb_fixed[index],
                         bb_has_min=self.bb_has_min[index],
                         bb_min=self.bb_min[index],
                         bb_has_max=self.bb_has_max[index],
                         bb_max=self.bb_max[index],
                         bb_function=self.bb_function[index],
                         bb_function_value=self.bb_function_value[index],
                         e1=self.e1[index],
                         e1_fixed=self.e1_fixed[index],
                         e1_has_min=self.e1_has_min[index],
                         e1_min=self.e1_min[index],
                         e1_has_max=self.e1_has_max[index],
                         e1_max=self.e1_max[index],
                         e1_function=self.e1_function[index],
                         e1_function_value=self.e1_function_value[index],
                         e4=self.e4[index],
                         e4_fixed=self.e4_fixed[index],
                         e4_has_min=self.e4_has_min[index],
                         e4_min=self.e4_min[index],
                         e4_has_max=self.e4_has_max[index],
                         e4_max=self.e4_max[index],
                         e4_function=self.e4_function[index],
                         e4_function_value=self.e4_function_value[index])


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
            if not isinstance(data.get_strain_parameters(0), InvariantPAH):
                raise Exception("Only 1 Strain Model is allowed in a line of fit: it should be branched before")

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpOtherSettings(self):
        self.dump_active()
        self.dump_laue_id()
        self.dump_aa()
        self.dump_bb()
        self.dump_e1()
        self.dump_e4()
            
    def dump_laue_id(self): self.dump_variable("laue_id")
    def dump_aa(self): self.dump_parameter("aa")
    def dump_bb(self): self.dump_parameter("bb")
    def dump_e1(self): self.dump_parameter("e1")
    def dump_e4(self): self.dump_parameter("e4")

class StrainBox(ParameterActivableBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 active=1,
                 laue_id=13,
                 aa=0.0,
                 aa_fixed=0,
                 aa_has_min=0,
                 aa_min=0.0,
                 aa_has_max=0,
                 aa_max=0.0,
                 aa_function=0,
                 aa_function_value="",
                 bb=0.0,
                 bb_fixed=0,
                 bb_has_min=0,
                 bb_min=0.0,
                 bb_has_max=0,
                 bb_max=0.0,
                 bb_function=0,
                 bb_function_value="",
                 e1=0.0,
                 e1_fixed=0,
                 e1_has_min=0,
                 e1_min=0.0,
                 e1_has_max=0,
                 e1_max=0.0,
                 e1_function=0,
                 e1_function_value="",
                 e4=0.0,
                 e4_fixed=0,
                 e4_has_min=0,
                 e4_min=0.0,
                 e4_has_max=0,
                 e4_max=0.0,
                 e4_function=0,
                 e4_function_value=""):
        super(StrainBox, self).__init__(widget=widget,
                                        parent=parent,
                                        index=index,
                                        active=active,
                                        laue_id=laue_id,
                                        aa = aa,
                                        aa_fixed = aa_fixed,
                                        aa_has_min = aa_has_min,
                                        aa_min = aa_min,
                                        aa_has_max = aa_has_max,
                                        aa_max = aa_max,
                                        aa_function = aa_function,
                                        aa_function_value = aa_function_value,
                                        bb = bb,
                                        bb_fixed = bb_fixed,
                                        bb_has_min = bb_has_min,
                                        bb_min = bb_min,
                                        bb_has_max = bb_has_max,
                                        bb_max = bb_max,
                                        bb_function = bb_function,
                                        bb_function_value = bb_function_value,
                                        e1 = e1,
                                        e1_fixed = e1_fixed,
                                        e1_has_min = e1_has_min,
                                        e1_min = e1_min,
                                        e1_has_max = e1_has_max,
                                        e1_max = e1_max,
                                        e1_function = e1_function,
                                        e1_function_value = e1_function_value,
                                        e4 = e4,
                                        e4_fixed = e4_fixed,
                                        e4_has_min = e4_has_min,
                                        e4_min = e4_min,
                                        e4_has_max = e4_has_max,
                                        e4_max = e4_max,
                                        e4_function = e4_function,
                                        e4_function_value = e4_function_value)

    def init_fields(self, **kwargs):
        self.laue_id           = kwargs["laue_id"]
        self.aa                = kwargs["aa"]
        self.aa_fixed          = kwargs["aa_fixed"]
        self.aa_has_min        = kwargs["aa_has_min"]
        self.aa_min            = kwargs["aa_min"]
        self.aa_has_max        = kwargs["aa_has_max"]
        self.aa_max            = kwargs["aa_max"]
        self.aa_function       = kwargs["aa_function"]
        self.aa_function_value = kwargs["aa_function_value"]
        self.bb                = kwargs["bb"]
        self.bb_fixed          = kwargs["bb_fixed"]
        self.bb_has_min        = kwargs["bb_has_min"]
        self.bb_min            = kwargs["bb_min"]
        self.bb_has_max        = kwargs["bb_has_max"]
        self.bb_max            = kwargs["bb_max"]
        self.bb_function       = kwargs["bb_function"]
        self.bb_function_value = kwargs["bb_function_value"]
        self.e1                = kwargs["e1"]
        self.e1_fixed          = kwargs["e1_fixed"]
        self.e1_has_min        = kwargs["e1_has_min"]
        self.e1_min            = kwargs["e1_min"]
        self.e1_has_max        = kwargs["e1_has_max"]
        self.e1_max            = kwargs["e1_max"]
        self.e1_function       = kwargs["e1_function"]
        self.e1_function_value = kwargs["e1_function_value"]
        self.e4                = kwargs["e4"]
        self.e4_fixed          = kwargs["e4_fixed"]
        self.e4_has_min        = kwargs["e4_has_min"]
        self.e4_min            = kwargs["e4_min"]
        self.e4_has_max        = kwargs["e4_has_max"]
        self.e4_max            = kwargs["e4_max"]
        self.e4_function       = kwargs["e4_function"]
        self.e4_function_value = kwargs["e4_function_value"]

    def init_main_box(self):
        OWGenericWidget.create_box_in_widget(self, self.main_box, "aa", add_callback=True, min_value=0.0, min_accepted=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.main_box, "bb", add_callback=True, min_value=0.0, min_accepted=True, trim=25)

        invariant_box = gui.widgetBox(self.main_box, "Invariant Parameters", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 10)

        self.cb_laue_id = orangegui.comboBox(invariant_box, self, "laue_id", label="Laue Group", items=LaueGroup.tuple(), callback=self.set_laue_id, orientation="horizontal")

        OWGenericWidget.create_box_in_widget(self, invariant_box, "e1", add_callback=True, trim=25)
        OWGenericWidget.create_box_in_widget(self, invariant_box, "e4", add_callback=True, trim=25)

    def set_laue_id(self):
        if not (self.laue_id == 12 or self.laue_id == 13):
            QMessageBox.critical(self, "Error",
                                 "Only " + LaueGroup.get_laue_group(14) + " and " + LaueGroup.get_laue_group(13) + " are supported",
                                 QMessageBox.Ok)

            self.laue_id = 13
            
            self.widget.dump_laue_id()

    def callback_aa(self):
        if not self.is_on_init: self.widget.dump_aa()

    def callback_bb(self):
        if not self.is_on_init: self.widget.dump_bb()

    def callback_e1(self):
        if not self.is_on_init: self.widget.dump_e1()

    def callback_e4(self):
        if not self.is_on_init: self.widget.dump_e4()

    def get_basic_parameter_prefix(self):
        return InvariantPAH.get_parameters_prefix()

    def set_data(self, strain_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "aa", strain_parameters.aa)
        OWGenericWidget.populate_fields_in_widget(self, "bb", strain_parameters.bb)
        OWGenericWidget.populate_fields_in_widget(self, "e1", strain_parameters.e1)
        OWGenericWidget.populate_fields_in_widget(self, "e4", strain_parameters.e4)

    def get_strain_parameters(self):
        if self.active == 0: return None
        else:
            if self.laue_id == 12:
                return InvariantPAHLaueGroup13(aa=OWGenericWidget.populate_parameter_in_widget(self, "aa", self.get_parameters_prefix()),
                                               bb=OWGenericWidget.populate_parameter_in_widget(self, "bb", self.get_parameters_prefix()),
                                               e1=OWGenericWidget.populate_parameter_in_widget(self, "e1", self.get_parameters_prefix()),
                                               e4=OWGenericWidget.populate_parameter_in_widget(self, "e4", self.get_parameters_prefix()))
            elif self.laue_id == 13:
                return InvariantPAHLaueGroup14(aa=OWGenericWidget.populate_parameter_in_widget(self, "aa", self.get_parameters_prefix()),
                                               bb=OWGenericWidget.populate_parameter_in_widget(self, "bb", self.get_parameters_prefix()),
                                               e1=OWGenericWidget.populate_parameter_in_widget(self, "e1", self.get_parameters_prefix()),
                                               e4=OWGenericWidget.populate_parameter_in_widget(self, "e4", self.get_parameters_prefix()))
            else:
                return None

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a =  QApplication(sys.argv)
    ow = OWStrainInvariant()
    ow.show()
    a.exec_()
    ow.saveSettings()
