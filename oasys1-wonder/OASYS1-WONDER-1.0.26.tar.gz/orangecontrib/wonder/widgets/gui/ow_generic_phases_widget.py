import sys

from PyQt5.QtWidgets import QMessageBox

from orangewidget.settings import Setting
from orangewidget import gui as orangegui
from orangewidget.widget import OWAction

from orangecontrib.wonder.widgets.gui.ow_generic_widget import OWGenericWidget
from orangecontrib.wonder.util.gui_utility import gui, ConfirmDialog

from orangecontrib.wonder.fit.parameters.measured_data.phase import Phase

class OWGenericPhases(OWGenericWidget):
    want_main_area = False

    a = Setting([0.0])
    a_fixed = Setting([0])
    a_has_min = Setting([0])
    a_min = Setting([0.0])
    a_has_max = Setting([0])
    a_max = Setting([0.0])
    a_function = Setting([0])
    a_function_value = Setting([""])
    symmetry = Setting([2])
    use_structure = Setting([0])
    cif_file = Setting([""])
    formula = Setting([""])
    intensity_scale_factor = Setting([1.0])
    intensity_scale_factor_fixed = Setting([0])
    intensity_scale_factor_has_min = Setting([0])
    intensity_scale_factor_min = Setting([0.0])
    intensity_scale_factor_has_max = Setting([0])
    intensity_scale_factor_max = Setting([0.0])
    intensity_scale_factor_function = Setting([0])
    intensity_scale_factor_function_value = Setting([""])
    phase_name = Setting([""])

    def __init__(self):
        super().__init__(show_automatic_box=True)

        main_box = gui.widgetBox(self.controlArea,
                                 "Phases", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 5, height=self.get_height())

        button_box = gui.widgetBox(main_box,
                                   "", orientation="horizontal",
                                   width=self.CONTROL_AREA_WIDTH - 25)

        gui.button(button_box, self, "Send Phases", height=50, callback=self.send_phases)

        tabs_button_box = gui.widgetBox(main_box, "", addSpace=False, orientation="horizontal")

        btns = [gui.button(tabs_button_box, self, "Insert Phase Before", callback=self.insert_before),
                gui.button(tabs_button_box, self, "Insert Phase After", callback=self.insert_after),
                gui.button(tabs_button_box, self, "Remove Phase", callback=self.remove)]

        for btn in btns:
            btn.setFixedHeight(35)

        self.phases_tabs = gui.tabWidget(main_box)
        self.phases_box_array = []

        for index in range(len(self.a)):
            phase_tab = gui.createTabPage(self.phases_tabs, "Phase " + str(index + 1))

            phase_box = self.get_phase_box_instance(index, phase_tab)

            self.phases_box_array.append(phase_box)

        runaction = OWAction("Send Phases", self)
        runaction.triggered.connect(self.send_phases)
        self.addAction(runaction)

        orangegui.rubber(self.controlArea)

    def get_phase_box_instance(self, index, phase_tab):
        raise NotImplementedError()

    def get_empty_phase_box_instance(self, index, phase_tab):
        raise NotImplementedError()

    def get_max_height(self):
        return 480

    def get_height(self):
        return self.get_max_height() - 100

    def insert_before(self):
        current_index = self.phases_tabs.currentIndex()

        if ConfirmDialog.confirmed(parent=self,
                                   message="Confirm Insertion of a new element before " + self.phases_tabs.tabText(
                                       current_index) + "?"):
            phase_tab = gui.widgetBox(self.phases_tabs, addToLayout=0, margin=4)
            phase_box = self.get_empty_phase_box_instance(current_index, phase_tab)
            phase_box.after_change_workspace_units()

            self.phases_tabs.insertTab(current_index, phase_tab, "TEMP")
            self.phases_box_array.insert(current_index, phase_box)

            for index in range(current_index, self.phases_tabs.count()):
                self.phases_tabs.setTabText(index, Phase.get_default_name(index))
                self.phases_box_array[index].index = index

            self.dumpSettings()
            self.phases_tabs.setCurrentIndex(current_index)

    def insert_after(self):
        current_index = self.phases_tabs.currentIndex()

        if ConfirmDialog.confirmed(parent=self,
                                   message="Confirm Insertion of a new element after " + self.phases_tabs.tabText(
                                       current_index) + "?"):
            phase_tab = gui.widgetBox(self.phases_tabs, addToLayout=0, margin=4)
            phase_box = self.get_empty_phase_box_instance(current_index + 1, phase_tab)
            phase_box.after_change_workspace_units()

            if current_index == self.phases_tabs.count() - 1:  # LAST
                self.phases_tabs.addTab(phase_tab, "TEMP")
                self.phases_box_array.append(phase_box)
            else:
                self.phases_tabs.insertTab(current_index + 1, phase_tab, "TEMP")
                self.phases_box_array.insert(current_index + 1, phase_box)

            for index in range(current_index, self.phases_tabs.count()):
                self.phases_tabs.setTabText(index, Phase.get_default_name(index))
                self.phases_box_array[index].index = index

            self.dumpSettings()
            self.phases_tabs.setCurrentIndex(current_index + 1)

    def remove(self):
        if self.phases_tabs.count() <= 1:
            QMessageBox.critical(self, "Error",
                                 "Remove not possible, Fit process needs at least 1 element",
                                 QMessageBox.Ok)
        else:
            current_index = self.phases_tabs.currentIndex()

            if ConfirmDialog.confirmed(parent=self,
                                       message="Confirm Removal of " + self.phases_tabs.tabText(
                                           current_index) + "?"):
                self.phases_tabs.removeTab(current_index)
                self.phases_box_array.pop(current_index)

                for index in range(current_index, self.phases_tabs.count()):
                    self.phases_tabs.setTabText(index, Phase.get_default_name(index))
                    self.phases_box_array[index].index = index

                self.dumpSettings()
                self.phases_tabs.setCurrentIndex(current_index)

    def send_phases(self):
        try:
            if not self.fit_global_parameters is None:
                self.dumpSettings()

                self.check_congruence()

                self.set_phases()

                self.fit_global_parameters.evaluate_functions()
                self.fit_global_parameters.regenerate_parameters()

                self.send("Fit Global Parameters", self.fit_global_parameters)

        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 str(e),
                                 QMessageBox.Ok)

            if self.IS_DEVELOP: raise e

    def check_congruence(self):
        raise NotImplementedError()

    def set_data(self, data):
        if not data is None:
            try:
                self.fit_global_parameters = data.duplicate()

                diffraction_patterns = self.fit_global_parameters.measured_dataset.diffraction_patterns
                phases = self.fit_global_parameters.measured_dataset.phases

                if diffraction_patterns is None: raise ValueError("No Diffraction Pattern in input data!")

                if not phases is None:
                    if (len(phases) != len(self.phases_box_array)):
                        self.phases_tabs.clear()
                        self.phases_box_array = []

                        for index in range(len(phases)):
                            phase_tab = gui.createTabPage(self.phases_tabs, OWGenericWidget.phase_name(self.fit_global_parameters, index))

                            if index < len(self.a):  # keep the existing
                                phase_box = self.get_phase_box_instance(index, phase_tab)
                            else:
                                phase_box = self.get_empty_phase_box_instance(index, phase_tab)

                            self.phases_box_array.append(phase_box)
                    else:
                        for index in range(len(phases)):
                            self.phases_box_array[index].set_data(phases[index])

                self.dumpSettings()

                if self.is_automatic_run:
                    self.send_phases()

            except Exception as e:
                QMessageBox.critical(self, "Error",
                                     str(e),
                                     QMessageBox.Ok)

                if self.IS_DEVELOP: raise e

    def set_phases(self):
        raise NotImplementedError()

    def get_parameter_box_array(self):
        return self.phases_box_array

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpSettings(self):
        self.dump_a()
        self.dump_symmetry()
        self.dump_use_structure()
        self.dump_cif_file()
        self.dump_formula()
        self.dump_intensity_scale_factor()
        self.dump_phase_name()

    def dump_a(self): self.dump_parameter("a")
    def dump_use_structure(self): self.dump_variable("use_structure")
    def dump_symmetry(self): self.dump_variable("symmetry")
    def dump_cif_file(self): self.dump_variable("cif_file")
    def dump_formula(self): self.dump_variable("formula")
    def dump_intensity_scale_factor(self): self.dump_parameter("intensity_scale_factor")
    def dump_phase_name(self): self.dump_variable("phase_name")


