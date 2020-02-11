import sys

from PyQt5.QtWidgets import QMessageBox

from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import ParameterBox
from orangecontrib.wonder.widgets.gui.ow_generic_phases_widget import OWGenericWidget, OWGenericPhases
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.util import congruence
from orangecontrib.wonder.util.fit_utilities import Symmetry

from orangecontrib.wonder.fit.parameters.gsasii.gsasii_phase import GSASIIPhase
from orangecontrib.wonder.fit.parameters.gsasii.gsasii_functions import gsasii_load_reflections

class OWGSASIIPhases(OWGenericPhases):
    name = "GSAS-II Phases"
    description = "Phases description"
    icon = "icons/gsas2.png"
    priority = 1.21

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 650

    def get_phase_box_instance(self, index, phase_tab):
        return PhaseBox(widget=self,
                        parent=phase_tab,
                        index = index,
                        a                                    = self.a[index],
                        a_fixed                              = self.a_fixed[index],
                        a_has_min                            = self.a_has_min[index],
                        a_min                                = self.a_min[index],
                        a_has_max                            = self.a_has_max[index],
                        a_max                                = self.a_max[index],
                        a_function                           = self.a_function[index],
                        a_function_value                     = self.a_function_value[index],
                        symmetry                             = self.symmetry[index],
                        cif_file                             = self.cif_file[index],
                        formula                              = self.formula[index],
                        intensity_scale_factor               = self.intensity_scale_factor[index],
                        intensity_scale_factor_fixed         = self.intensity_scale_factor_fixed[index],
                        intensity_scale_factor_has_min       = self.intensity_scale_factor_has_min[index],
                        intensity_scale_factor_min           = self.intensity_scale_factor_min[index],
                        intensity_scale_factor_has_max       = self.intensity_scale_factor_has_max[index],
                        intensity_scale_factor_max           = self.intensity_scale_factor_max[index],
                        intensity_scale_factor_function      = self.intensity_scale_factor_function[index],
                        intensity_scale_factor_function_value= self.intensity_scale_factor_function_value[index],
                        phase_name                           = self.phase_name[index])

    def get_empty_phase_box_instance(self, index, phase_tab):
        return PhaseBox(widget=self, parent=phase_tab, index=index)

    def check_congruence(self):
        pass

    def set_phases(self):
        self.fit_global_parameters.measured_dataset.set_phases([self.phases_box_array[index].get_phase() for index in range(len(self.phases_box_array))])

        measured_dataset = self.fit_global_parameters.measured_dataset
        incident_radiations = measured_dataset.incident_radiations

        for diffraction_pattern_index in range(measured_dataset.get_diffraction_patterns_number()):
            incident_radiation  = incident_radiations[0 if len(incident_radiations) == 1 else diffraction_pattern_index]
            diffraction_pattern = measured_dataset.diffraction_patterns[diffraction_pattern_index]
            line_profile = measured_dataset.line_profiles[diffraction_pattern_index]
            line_profile.generate_additional_parameters()

            for phase_index in range(self.fit_global_parameters.measured_dataset.get_phases_number()):
                gsasii_phase = measured_dataset.phases[phase_index]

                gsasii_reflections_list = gsasii_load_reflections(gsasii_phase.cif_file,
                                                                  incident_radiation.wavelength.value,
                                                                  diffraction_pattern.get_diffraction_point(0).twotheta,
                                                                  diffraction_pattern.get_diffraction_point(-1).twotheta)

                line_profile.set_additional_parameters_of_phase(phase_index=phase_index,
                                                                additional_parameters=gsasii_reflections_list)

                self.phases_box_array[phase_index].set_gsasii_result(gsasii_reflections_list)

class PhaseBox(ParameterBox):
    use_structure = 1

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
                 cif_file="",
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
                                       a_fixed=a_fixed,
                                       a_has_min=a_has_min,
                                       a_min=a_min,
                                       a_has_max=a_has_max,
                                       a_max=a_max,
                                       a_function=a_function,
                                       a_function_value=a_function_value,
                                       symmetry=symmetry,
                                       cif_file=cif_file,
                                       formula=formula,
                                       intensity_scale_factor=intensity_scale_factor,
                                       intensity_scale_factor_fixed=intensity_scale_factor_fixed,
                                       intensity_scale_factor_has_min=intensity_scale_factor_has_min,
                                       intensity_scale_factor_min=intensity_scale_factor_min,
                                       intensity_scale_factor_has_max=intensity_scale_factor_has_max,
                                       intensity_scale_factor_max=intensity_scale_factor_max,
                                       intensity_scale_factor_function=intensity_scale_factor_function,
                                       intensity_scale_factor_function_value=intensity_scale_factor_function_value,
                                       phase_name=phase_name)

    def get_height(self):
        return 470

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
        self.cif_file = kwargs["cif_file"]
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
        gui.lineEdit(container, self, "phase_name", "Phase Name (will appear in tabs and plots)", labelWidth=260, valueType=str, callback=self.widget.dump_phase_name)

        self.cb_symmetry = orangegui.comboBox(container, self, "symmetry", label="Symmetry", items=Symmetry.tuple(),
                                              callback=self.set_symmetry, orientation="horizontal")

        OWGenericWidget.create_box_in_widget(self, container, "a", "a [nm]", add_callback=True, min_value=0.0,
                                             min_accepted=False, trim=5)

        orangegui.separator(container)

        structure_box = gui.widgetBox(container,
                                      "", orientation="vertical",
                                      width=self.CONTROL_AREA_WIDTH)

        self.structure_box_1 = gui.widgetBox(structure_box,
                                             "", orientation="vertical",
                                             width=self.CONTROL_AREA_WIDTH - 5, height=90)

        file_box = gui.widgetBox(self.structure_box_1, "", orientation="horizontal", width=self.CONTROL_AREA_WIDTH-10)

        self.le_cif_file = gui.lineEdit(file_box, self, value="cif_file", valueType=str, label="CIF File", labelWidth=50, callback=self.widget.dump_cif_file)
        orangegui.button(file_box, self, "...", callback=self.open_folders)

        gui.lineEdit(self.structure_box_1, self, "formula", "Chemical Formula", labelWidth=110, valueType=str,
                     callback=self.widget.dump_formula)

        OWGenericWidget.create_box_in_widget(self, self.structure_box_1, "intensity_scale_factor", "I0",
                                             add_callback=True, min_value=0.0, min_accepted=False, trim=5)

        text_area_box = gui.widgetBox(structure_box, "Calculation Result", orientation="vertical", height=165, width=self.CONTROL_AREA_WIDTH - 10)

        self.text_area = gui.textArea(height=125, width=self.CONTROL_AREA_WIDTH - 30, readOnly=True)
        self.text_area.setText("")

        text_area_box.layout().addWidget(self.text_area)

        self.is_on_init = False

    def open_folders(self):
        self.cif_file=gui.selectFileFromDialog(self,
                                               self.cif_file,
                                               start_directory=self.widget.working_directory)

        self.le_cif_file.setText(self.cif_file)

    def set_symmetry(self):
        if not GSASIIPhase.is_cube(self.cb_symmetry.currentText()):
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
        return GSASIIPhase.get_parameters_prefix()

    def set_data(self, phase):
        OWGenericWidget.populate_fields_in_widget(self, "a", phase.a)
        OWGenericWidget.populate_fields_in_widget(self, "intensity_scale_factor", phase.intensity_scale_factor)
        self.cif_file = phase.cif_file
        self.formula = phase.formula

        simmetries = Symmetry.tuple()
        for index in range(0, len(simmetries)):
            if simmetries[index] == phase.symmetry:
                self.symmetry = index

        self.set_symmetry()

        self.phase_name = phase.name

    def get_phase(self):
        phase = GSASIIPhase.init_cube(a0=OWGenericWidget.populate_parameter_in_widget(self, "a", self.get_parameters_prefix()),
                                      symmetry=self.cb_symmetry.currentText(),
                                      cif_file=self.cif_file,
                                      formula=congruence.checkEmptyString(self.formula, "Chemical Formula"),
                                      intensity_scale_factor=OWGenericWidget.populate_parameter_in_widget(self, "intensity_scale_factor", self.get_parameters_prefix()),
                                      name=self.phase_name,
                                      progressive=self.get_parameter_progressive())

        return phase

    def set_gsasii_result(self, gsasii_reflection_list):
        self.text_area.clear()

        text = "h k l    2\u03b8    m     |F|^2         I\n" + \
               "-----------------------------------------------------\n"
        for reflection in gsasii_reflection_list.get_reflections():
            text += str(reflection) + "\n"

        self.text_area.setText(text)

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWGSASIIPhases()
    ow.show()
    a.exec_()
    ow.saveSettings()
