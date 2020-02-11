import sys, numpy, copy

from PyQt5.QtWidgets import QMessageBox, QScrollArea, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

from orangewidget.settings import Setting
from orangewidget import gui as orangegui
from orangewidget.widget import OWAction

from orangecontrib.wonder.widgets.gui.ow_generic_widget import OWGenericWidget
from orangecontrib.wonder.util.gui_utility import gui, ConfirmDialog, ConfirmTextDialog

from orangecontrib.wonder.util.fit_utilities import Utilities, list_of_s_bragg
from orangecontrib.wonder.fit.parameters.fit_global_parameters import FitGlobalParameters
from orangecontrib.wonder.fit.parameters.fit_parameter import FitParameter, Boundary
from orangecontrib.wonder.fit.parameters.measured_data.reflection import Reflection
from orangecontrib.wonder.fit.parameters.measured_data.diffraction_pattern import DiffractionPattern

class OWLineProfile(OWGenericWidget):

    name = "Line Profile"
    description = "Define Visibile Reflections"
    icon = "icons/line_profile.png"
    priority = 1.3

    want_main_area = False

    reflections_of_phases = Setting([[""]])
    limits                = Setting([[0.0]])
    limit_types           = Setting([[0]])

    inputs = [("Fit Global Parameters", FitGlobalParameters, 'set_data')]
    outputs = [("Fit Global Parameters", FitGlobalParameters)]

    def __init__(self):
        super().__init__(show_automatic_box=True)
        
        line_profiles_box = gui.widgetBox(self.controlArea,
                                 "Line Profiles", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 10, height=600)


        button_box = gui.widgetBox(line_profiles_box,
                                   "", orientation="horizontal",
                                   width=self.CONTROL_AREA_WIDTH-25)

        gui.button(button_box, self, "Send Line Profiles", height=40, callback=self.send_line_profiles)

        self.line_profiles_tabs = gui.tabWidget(line_profiles_box)
        self.line_profiles_box_array = []

        for index in range(len(self.reflections_of_phases)):
            line_profiles_tab = gui.createTabPage(self.line_profiles_tabs, DiffractionPattern.get_default_name(index))

            line_profiles_box = LineProfileBox(widget=self,
                                               parent=line_profiles_tab,
                                               diffraction_pattern_index = index,
                                               reflections_of_phases = self.reflections_of_phases[index],
                                               limits                = self.limits[index],
                                               limit_types           = self.limit_types[index])

            self.line_profiles_box_array.append(line_profiles_box)

        runaction = OWAction("Send Line Profiles", self)
        runaction.triggered.connect(self.send_line_profiles)
        self.addAction(runaction)

        orangegui.rubber(self.controlArea)

    def get_max_height(self):
        return 700

    def send_line_profiles(self):
        try:
            if not self.fit_global_parameters is None:
                self.dumpSettings()

                for index in range(len(self.line_profiles_box_array)):
                    self.line_profiles_box_array[index].update_line_profile()

                self.fit_global_parameters.evaluate_functions()
                self.fit_global_parameters.regenerate_parameters()

                self.send("Fit Global Parameters", self.fit_global_parameters)

        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 str(e),
                                 QMessageBox.Ok)

            if self.IS_DEVELOP: raise e

    def set_data(self, data):
        if not data is None:
            try:
                self.fit_global_parameters = data.duplicate()

                diffraction_patterns = self.fit_global_parameters.measured_dataset.diffraction_patterns
                phases               = self.fit_global_parameters.measured_dataset.phases
                line_profiles        = self.fit_global_parameters.measured_dataset.line_profiles

                if diffraction_patterns is None: raise ValueError("No Diffraction Pattern in input data!")
                if phases is None:               raise ValueError("No Phases in input data!")

                different_phases   = len(phases) != len(self.reflections_of_phases[0])
                different_patterns = len(line_profiles) != len(self.reflections_of_phases)

                if different_patterns or different_phases:
                    self.line_profiles_tabs.clear()
                    self.line_profiles_box_array = []

                    for diffraction_pattern_index in range(len(diffraction_patterns)):
                        line_profile_tab = gui.createTabPage(self.line_profiles_tabs, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, diffraction_pattern_index))

                        if diffraction_pattern_index < len(self.reflections_of_phases): #keep the existing
                            reflections_of_phases = []
                            limits                = []
                            limit_types           = []

                            for phase_index in range(len(phases)):
                                if phase_index < len(self.reflections_of_phases[diffraction_pattern_index]):
                                    reflections_of_phases.append(self.reflections_of_phases[diffraction_pattern_index][phase_index])
                                    limits.append(self.limits[diffraction_pattern_index][phase_index])
                                    limit_types.append(self.limit_types[diffraction_pattern_index][phase_index])
                                else:
                                    reflections_of_phases.append("")
                                    limits.append(0.0)
                                    limit_types.append(0)

                            line_profile_box = LineProfileBox(widget=self,
                                                              parent=line_profile_tab,
                                                              diffraction_pattern_index = diffraction_pattern_index,
                                                              reflections_of_phases = reflections_of_phases,
                                                              limits         = limits,
                                                              limit_types    = limit_types)
                        else:
                            line_profile_box = LineProfileBox(widget=self,
                                                              parent=line_profile_tab,
                                                              diffraction_pattern_index = diffraction_pattern_index,
                                                              reflections_of_phases=[""]*len(phases),
                                                              limits=[0.0]*len(phases),
                                                              limit_types=[0]*len(phases))

                        self.line_profiles_box_array.append(line_profile_box)


                elif not line_profiles is None:
                    for diffraction_pattern_index in range(len(diffraction_patterns)):
                        self.line_profiles_tabs.setTabText(diffraction_pattern_index, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, diffraction_pattern_index))
                        self.line_profiles_box_array[diffraction_pattern_index].set_data(line_profiles[diffraction_pattern_index])

                self.dumpSettings()

                if self.is_automatic_run:
                    self.send_line_profiles()

            except Exception as e:
                QMessageBox.critical(self, "Error",
                                     str(e),
                                     QMessageBox.Ok)

                if self.IS_DEVELOP: raise e


    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def get_parameter_box_array(self):
        return self.line_profiles_box_array

    def dumpSettings(self):
        self.dump_reflections_of_phases()
        self.dump_limits()
        self.dump_limit_types()

    def dump_reflections_of_phases(self): self.dump_variable("reflections_of_phases")
    def dump_limits(self): self.dump_variable("limits")
    def dump_limit_types(self): self.dump_variable("limit_types")


from PyQt5.QtWidgets import QVBoxLayout
from orangecontrib.wonder.util.gui_utility import InnerBox

class LineProfileBox(InnerBox):
    widget = None
    is_on_init = True

    parameter_functions = {}

    diffraction_pattern_index = 0

    def __init__(self,
                 widget=None,
                 parent=None,
                 diffraction_pattern_index=0,
                 reflections_of_phases=[],
                 limits=[],
                 limit_types=[]):

        super(LineProfileBox, self).__init__()

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedWidth(widget.CONTROL_AREA_WIDTH - 35)
        self.setFixedHeight(480)

        self.widget = widget
        self.diffraction_pattern_index = diffraction_pattern_index

        self.reflections_of_phases = reflections_of_phases
        self.limits = limits
        self.limit_types = limit_types

        self.CONTROL_AREA_WIDTH = widget.CONTROL_AREA_WIDTH-45

        parent.layout().addWidget(self)
        container = self

        self.reflections_of_phases_tabs = gui.tabWidget(container)
        self.reflections_of_phases_box_array = []

        for phase_index in range(len(self.reflections_of_phases)):
            reflections_of_phase_tab = gui.createTabPage(self.reflections_of_phases_tabs, OWGenericWidget.phase_name(self.widget.fit_global_parameters, phase_index))

            reflections_of_phase_box = ReflectionsOfPhaseBox(widget=widget,
                                                             widget_container=self,
                                                             parent=reflections_of_phase_tab,
                                                             diffraction_pattern_index = diffraction_pattern_index,
                                                             phase_index=phase_index,
                                                             reflections_of_phase = self.reflections_of_phases[phase_index],
                                                             limit                = self.limits[phase_index],
                                                             limit_type           = self.limit_types[phase_index])

            self.reflections_of_phases_box_array.append(reflections_of_phase_box)

    def set_data(self, line_profile):
        for phase_index in range(len(self.reflections_of_phases_box_array)):
            reflections_of_phases_box = self.reflections_of_phases_box_array[phase_index]
            reflections_of_phases_box.set_data(line_profile)
            self.reflections_of_phases_tabs.setTabText(phase_index, OWGenericWidget.phase_name(self.widget.fit_global_parameters, phase_index))

    def update_line_profile(self):
        for reflections_of_phases_box in self.reflections_of_phases_box_array:
            reflections_of_phases_box.update_reflections_of_phase()


    def get_parameter_box_array(self):
        return self.reflections_of_phases_box_array

    def dumpSettings(self):
        self.dump_reflections_of_phases()
        self.dump_limits()
        self.dump_limit_types()

    def dump_reflections_of_phases(self):
        OWGenericWidget.dump_variable_in_widget(self, "reflections_of_phases", variable_name_in_box="reflections_of_phase")
        self.widget.dump_reflections_of_phases()

    def dump_limits(self):
        OWGenericWidget.dump_variable_in_widget(self, "limits", variable_name_in_box="limit")
        self.widget.dump_limits()

    def dump_limit_types(self):
        OWGenericWidget.dump_variable_in_widget(self, "limit_types", variable_name_in_box="limit_type")
        self.widget.dump_limit_types()

class ReflectionsOfPhaseBox(InnerBox):
    widget = None
    is_on_init = True

    parameter_functions = {}

    diffraction_pattern_index = 0
    phase_index = 0

    def __init__(self,
                 widget=None,
                 widget_container=None,
                 parent=None,
                 diffraction_pattern_index = 0,
                 phase_index = 0,
                 reflections_of_phase = "",
                 limit                = 0.0,
                 limit_type           = 0):
        super(ReflectionsOfPhaseBox, self).__init__()

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedWidth(widget.CONTROL_AREA_WIDTH - 55)
        self.setFixedHeight(430)

        self.widget = widget
        self.diffraction_pattern_index = diffraction_pattern_index
        self.phase_index = phase_index
        
        self.reflections_of_phase = reflections_of_phase
        self.limit                = limit
        self.limit_type           = limit_type

        self.CONTROL_AREA_WIDTH = widget.CONTROL_AREA_WIDTH-65

        parent.layout().addWidget(self)
        container = self

        gen_box = gui.widgetBox(container, "Generate Reflections", orientation="horizontal")

        le_limit = gui.lineEdit(gen_box, self, "limit", "Limit", labelWidth=90, valueType=float, validator=QDoubleValidator(), callback=widget_container.dump_limits)
        cb_limit = orangegui.comboBox(gen_box, self, "limit_type", label="Kind", items=["None", "Nr. Peaks", "2Theta Max"], orientation="horizontal")

        def set_limit(limit_type):
            if limit_type == 0:
                le_limit.setText("-1")
                le_limit.setEnabled(False)
            else:
                le_limit.setEnabled(True)

            if not self.is_on_init:
                widget_container.dump_limits()
                widget_container.dump_limit_types()

        cb_limit.currentIndexChanged.connect(set_limit)
        set_limit(self.limit_type)

        gui.button(gen_box, self, "Generate Reflections", callback=self.generate_reflections)

        reflection_box = gui.widgetBox(container,
                                       "Reflections", orientation="vertical",
                                       width=self.CONTROL_AREA_WIDTH - 10)

        orangegui.label(reflection_box, self, "h, k, l, <intensity_name> int <, min value, max value>")

        scrollarea = QScrollArea(reflection_box)
        scrollarea.setMaximumWidth(self.CONTROL_AREA_WIDTH - 40)
        scrollarea.setMinimumWidth(self.CONTROL_AREA_WIDTH - 40)

        def write_text():
            self.reflections_of_phase = self.text_area.toPlainText()
            if not self.is_on_init: widget_container.dump_reflections_of_phases()

        self.text_area = gui.textArea(height=500, width=1000, readOnly=False)
        self.text_area.setText(self.reflections_of_phase)
        self.text_area.textChanged.connect(write_text)

        scrollarea.setWidget(self.text_area)
        scrollarea.setWidgetResizable(1)

        reflection_box.layout().addWidget(scrollarea, alignment=Qt.AlignHCenter)

        self.is_on_init = False

    def after_change_workspace_units(self):
        pass

    def set_phase_index(self, phase_index):
        self.phase_index = phase_index

    def generate_reflections(self):
        a0 = self.widget.fit_global_parameters.measured_dataset.phases[self.phase_index].a
        symmetry = self.widget.fit_global_parameters.measured_dataset.phases[self.phase_index].symmetry

        if a0.function:
            QMessageBox.critical(self,
                                 "Error",
                                 "a0 value of this phase is a function, generation is not possibile",
                                 QMessageBox.Ok)
            return

        if not self.reflections_of_phase is None and not self.reflections_of_phase.strip() == "":
            if not ConfirmDialog.confirmed(self, "Confirm overwriting of exisiting reflections?"):
                return

        if self.limit_type == 0:
            list = list_of_s_bragg(a0.value, symmetry=symmetry)
        elif self.limit_type == 1:
            list = list_of_s_bragg(a0.value, symmetry=symmetry, n_peaks=int(self.limit))
        elif self.limit_type == 2:
            if not self.widget.fit_global_parameters is None \
               and not self.widget.fit_global_parameters.measured_dataset is None \
               and not self.widget.fit_global_parameters.measured_dataset.incident_radiations is None:
                incident_radiation = self.widget.fit_global_parameters.measured_dataset.get_incident_radiations_item(self.diffraction_pattern_index)

                if not incident_radiation.wavelength.function:
                    wavelength = incident_radiation.wavelength.value

                    list = list_of_s_bragg(a0.value,
                                           symmetry=symmetry,
                                           s_max=Utilities.s(numpy.radians(self.limit/2), wavelength))
            else:
                QMessageBox.critical(self,
                                     "Error",
                                     "No wavelenght is available, 2theta limit is not possibile",
                                     QMessageBox.Ok)
                return

        text = ""

        for index in range(0, len(list)):
            h = list[index][0][0]
            k = list[index][0][1]
            l = list[index][0][2]

            text += Reflection(h, k, l, FitParameter(parameter_name="I" + str(h) + str(k) + str(l), value=1000, boundary=Boundary(min_value=0.0))).to_text() + "\n"

        self.text_area.setText(text)

    def set_data(self, line_profile):
        existing_line_profile = line_profile.duplicate()

        if not self.text_area.toPlainText().strip() == "":
            existing_line_profile.parse_reflections(self.text_area.toPlainText(), phase_index=self.phase_index, diffraction_pattern_index=self.diffraction_pattern_index)

        for reflection in line_profile.get_reflections(self.phase_index):
            existing_reflection = existing_line_profile.existing_reflection(self.phase_index, reflection.h, reflection.k, reflection.l)

            if existing_reflection is None:
                existing_line_profile.add_reflection(self.phase_index, reflection)
            else:
                existing_reflection.intensity.value = reflection.intensity.value

        text = ""

        for reflection in existing_line_profile.get_reflections(self.phase_index):
            text += reflection.to_row() + "\n"

        self.text_area.setText(text)

    def update_reflections_of_phase(self):
        line_profile        = self.widget.fit_global_parameters.measured_dataset.line_profiles[self.diffraction_pattern_index].duplicate()
        use_structure       = self.widget.fit_global_parameters.measured_dataset.phases[self.phase_index].use_structure

        line_profile.parse_reflections(self.reflections_of_phase, phase_index=self.phase_index, diffraction_pattern_index=self.diffraction_pattern_index)

        if use_structure == 1:
            for reflection in line_profile.get_reflections(self.phase_index):
                reflection.intensity.fixed = True

        if not self.widget.fit_global_parameters is None \
                and not self.widget.fit_global_parameters.measured_dataset is None \
                and not self.widget.fit_global_parameters.measured_dataset.incident_radiations is None:
            incident_radiation = self.widget.fit_global_parameters.measured_dataset.get_incident_radiations_item(self.diffraction_pattern_index)

            if not incident_radiation.wavelength.function:
                diffraction_pattern = self.widget.fit_global_parameters.measured_dataset.diffraction_patterns[self.diffraction_pattern_index]

                wavelength = incident_radiation.wavelength.value
                s_min      = diffraction_pattern.get_diffraction_point(0).s
                s_max      = diffraction_pattern.get_diffraction_point(-1).s

                excluded_reflections = line_profile.get_congruence_check(phase_index=self.phase_index,
                                                                         wavelength=wavelength,
                                                                         min_value=s_min,
                                                                         max_value=s_max)

                if not excluded_reflections is None:
                    text_before = "The following reflections lie outside the diffraction pattern nr " + str(self.diffraction_pattern_index + 1) + ", phase nr " + str(self.phase_index + 1) + ":"

                    text = ""

                    for reflection in excluded_reflections:
                        text += "[" + str(reflection.h) + ", " + str(reflection.k) + ", " + str(reflection.l) +"]\n"

                    text_after = "Proceed anyway?"

                    if not ConfirmTextDialog.confirm_text("Confirm Structure", text,
                                                          text_after=text_after, text_before=text_before,
                                                          width=350, parent=self): return

        self.widget.fit_global_parameters.measured_dataset.line_profiles[self.diffraction_pattern_index] = line_profile

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWLineProfile()
    ow.show()
    a.exec_()
    ow.saveSettings()
