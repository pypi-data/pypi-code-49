import sys

from PyQt5.QtWidgets import QMessageBox

from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import ParameterBox
from orangecontrib.wonder.widgets.gui.ow_generic_phases_widget import OWGenericWidget, OWGenericPhases
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.util import congruence
from orangecontrib.wonder.util.fit_utilities import Symmetry

from orangecontrib.wonder.fit.parameters.measured_data.phase import Phase

class OWPhases(OWGenericPhases):
    name = "Phases"
    description = "Phases description"
    icon = "icons/phases.png"
    priority = 1.2

    def __init__(self):
        super().__init__()

    def get_phase_box_instance(self, index, phase_tab):
        return PhaseBox(widget=self,
                        parent=phase_tab,
                        index=index,
                        a=self.a[index],
                        a_fixed=self.a_fixed[index],
                        a_has_min=self.a_has_min[index],
                        a_min=self.a_min[index],
                        a_has_max=self.a_has_max[index],
                        a_max=self.a_max[index],
                        a_function=self.a_function[index],
                        a_function_value=self.a_function_value[index],
                        symmetry=self.symmetry[index],
                        use_structure=self.use_structure[index],
                        formula=self.formula[index],
                        intensity_scale_factor=self.intensity_scale_factor[index],
                        intensity_scale_factor_fixed=self.intensity_scale_factor_fixed[index],
                        intensity_scale_factor_has_min=self.intensity_scale_factor_has_min[index],
                        intensity_scale_factor_min=self.intensity_scale_factor_min[index],
                        intensity_scale_factor_has_max=self.intensity_scale_factor_has_max[index],
                        intensity_scale_factor_max=self.intensity_scale_factor_max[index],
                        intensity_scale_factor_function=self.intensity_scale_factor_function[index],
                        intensity_scale_factor_function_value=self.intensity_scale_factor_function_value[index],
                        phase_name=self.phase_name[index])

    def get_empty_phase_box_instance(self, index, phase_tab):
        return PhaseBox(widget=self, parent=phase_tab, index=index)

    def check_congruence(self):
        use_structure_first = self.phases_box_array[0].use_structure

        for index in range(1, len(self.phases_box_array)):
            if use_structure_first != self.phases_box_array[index].use_structure:
                raise Exception("Incongruity: all the Phases must have the same setup of the structural model")

    def set_phases(self):
        self.fit_global_parameters.measured_dataset.set_phases([self.phases_box_array[index].get_phase() for index in range(len(self.phases_box_array))])

class PhaseBox(ParameterBox):
    cif_file = ""

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 a=0.0,
                 a_fixed=0,
                 a_has_min=0,
                 a_min=0.0,
                 a_has_max=0,
                 a_max=0.0,
                 a_function=0,
                 a_function_value="",
                 symmetry=2,
                 use_structure=0,
                 formula="",
                 intensity_scale_factor=1.0,
                 intensity_scale_factor_fixed=0,
                 intensity_scale_factor_has_min=0,
                 intensity_scale_factor_min=0.0,
                 intensity_scale_factor_has_max=0,
                 intensity_scale_factor_max=0.0,
                 intensity_scale_factor_function=0,
                 intensity_scale_factor_function_value="",
                 phase_name=""):
        super(PhaseBox, self).__init__(widget=widget,
                                       parent=parent,
                                       index=index,
                                       a=a,
                                       a_fixed = a_fixed,
                                       a_has_min = a_has_min,
                                       a_min = a_min,
                                       a_has_max = a_has_max,
                                       a_max = a_max,
                                       a_function = a_function,
                                       a_function_value = a_function_value,
                                       symmetry = symmetry,
                                       use_structure = use_structure,
                                       formula = formula,
                                       intensity_scale_factor = intensity_scale_factor,
                                       intensity_scale_factor_fixed = intensity_scale_factor_fixed,
                                       intensity_scale_factor_has_min = intensity_scale_factor_has_min,
                                       intensity_scale_factor_min = intensity_scale_factor_min,
                                       intensity_scale_factor_has_max = intensity_scale_factor_has_max,
                                       intensity_scale_factor_max = intensity_scale_factor_max,
                                       intensity_scale_factor_function = intensity_scale_factor_function,
                                       intensity_scale_factor_function_value = intensity_scale_factor_function_value,
                                       phase_name = phase_name)
    def get_height(self):
        return 300

    def init_fields(self, **kwargs):
        self.a = kwargs["a"]
        self.a_fixed = kwargs["a_fixed"]
        self.a_has_min = kwargs["a_has_min"]
        self.a_min = kwargs["a_min"]
        self.a_has_max = kwargs["a_has_max"]
        self.a_max = kwargs["a_max"]
        self.a_function = kwargs["a_function"]
        self.a_function_value = kwargs["a_function_value"]
        self.symmetry = kwargs["symmetry"]
        self.use_structure = kwargs["use_structure"]
        self.formula = kwargs["formula"]
        self.intensity_scale_factor = kwargs["intensity_scale_factor"]
        self.intensity_scale_factor_fixed = kwargs["intensity_scale_factor_fixed"]
        self.intensity_scale_factor_has_min = kwargs["intensity_scale_factor_has_min"]
        self.intensity_scale_factor_min = kwargs["intensity_scale_factor_min"]
        self.intensity_scale_factor_has_max = kwargs["intensity_scale_factor_has_max"]
        self.intensity_scale_factor_max = kwargs["intensity_scale_factor_max"]
        self.intensity_scale_factor_function = kwargs["intensity_scale_factor_function"]
        self.intensity_scale_factor_function_value = kwargs["intensity_scale_factor_function_value"]
        self.phase_name = kwargs["phase_name"]

    def init_gui(self, container):
        gui.lineEdit(container, self, "phase_name", "Phase Name", labelWidth=110, valueType=str, callback=self.widget.dump_phase_name)

        self.cb_symmetry = orangegui.comboBox(container, self, "symmetry", label="Symmetry", items=Symmetry.tuple(),
                                              callback=self.set_symmetry, orientation="horizontal")

        OWGenericWidget.create_box_in_widget(self, container, "a", "a [nm]", add_callback=True, min_value=0.0,
                                             min_accepted=False, trim=5)

        orangegui.separator(container)

        structure_box = gui.widgetBox(container,
                                      "", orientation="vertical",
                                      width=self.CONTROL_AREA_WIDTH)

        orangegui.comboBox(structure_box, self, "use_structure", label="Use Structural Model", items=["No", "Yes"],
                           callback=self.set_structure, labelWidth=350, orientation="horizontal")

        self.structure_box_1 = gui.widgetBox(structure_box,
                                             "", orientation="vertical",
                                             width=self.CONTROL_AREA_WIDTH - 5, height=60)

        gui.lineEdit(self.structure_box_1, self, "formula", "Chemical Formula", labelWidth=110, valueType=str,
                     callback=self.widget.dump_formula)

        OWGenericWidget.create_box_in_widget(self, self.structure_box_1, "intensity_scale_factor", "I0",
                                             add_callback=True, min_value=0.0, min_accepted=False, trim=5)

        self.structure_box_2 = gui.widgetBox(structure_box,
                                             "", orientation="vertical",
                                             width=self.CONTROL_AREA_WIDTH - 5, height=60)


        self.set_structure()

    def set_structure(self):
        self.structure_box_1.setVisible(self.use_structure == 1)
        self.structure_box_2.setVisible(self.use_structure == 0)

        if not self.is_on_init: self.widget.dump_use_structure()

    def set_symmetry(self):
        if not Phase.is_cube(self.cb_symmetry.currentText()):
            QMessageBox.critical(self, "Error",
                                 "Only Cubic Systems are supported",
                                 QMessageBox.Ok)

            self.symmetry = 2

        if not self.is_on_init: self.widget.dump_symmetry()

    def callback_a(self):
        if not self.is_on_init: self.widget.dump_a()

    def callback_intensity_scale_factor(self):
        if not self.is_on_init: self.widget.dump_intensity_scale_factor()

    def get_basic_parameter_prefix(self):
        return Phase.get_parameters_prefix()

    def set_data(self, phase):
        OWGenericWidget.populate_fields_in_widget(self, "a", phase.a)
        self.use_structure = 1 if phase.use_structure else 0

        if self.use_structure == 1:
            OWGenericWidget.populate_fields_in_widget(self, "intensity_scale_factor", phase.intensity_scale_factor)
            self.formula = phase.formula

        simmetries = Symmetry.tuple()
        for index in range(0, len(simmetries)):
            if simmetries[index] == phase.symmetry:
                self.symmetry = index

        self.set_structure()
        self.set_symmetry()

        self.phase_name = phase.name

    def get_phase(self):
        if self.use_structure == 0:
            phase = Phase.init_cube(a0=OWGenericWidget.populate_parameter_in_widget(self, "a", self.get_parameters_prefix()),
                                    symmetry=self.cb_symmetry.currentText(),
                                    name=self.phase_name,
                                    progressive=self.get_parameter_progressive())
        elif self.use_structure == 1:
            phase = Phase.init_cube(a0=OWGenericWidget.populate_parameter_in_widget(self, "a", self.get_parameters_prefix()),
                                    symmetry=self.cb_symmetry.currentText(),
                                    use_structure=True,
                                    formula=congruence.checkEmptyString(self.formula, "Chemical Formula"),
                                    intensity_scale_factor=OWGenericWidget.populate_parameter_in_widget(self, "intensity_scale_factor", self.get_parameters_prefix()),
                                    name=self.phase_name,
                                    progressive=self.get_parameter_progressive())

        return phase

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWPhases()
    ow.show()
    a.exec_()
    ow.saveSettings()
