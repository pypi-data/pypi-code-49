import sys, copy

from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import Qt

from orangewidget.settings import Setting
from orangewidget import gui as orangegui
from orangewidget.widget import OWAction

from orangecontrib.wonder.widgets.gui.ow_generic_widget import OWGenericWidget
from orangecontrib.wonder.util.gui_utility import gui, ConfirmDialog
from orangecontrib.wonder.util import congruence

from orangecontrib.wonder.fit.parameters.thermal.thermal_parameters import ThermalParameters

class OWDebyeWaller(OWGenericWidget):
    name = "Debye-Waller Factor"
    description = "Define Debye-Waller Factor"
    icon = "icons/debye_waller.png"
    priority = 5

    want_main_area = False

    use_single_parameter_set = Setting(0)

    use_debye_waller_factors = Setting([[1]])

    debye_waller_factors = Setting([[0.1]])
    debye_waller_factors_fixed = Setting([[0]])
    debye_waller_factors_has_min = Setting([[0]])
    debye_waller_factors_min = Setting([[0.0]])
    debye_waller_factors_has_max = Setting([[0]])
    debye_waller_factors_max = Setting([[0.0]])
    debye_waller_factors_function = Setting([[0]])
    debye_waller_factors_function_value = Setting([[""]])

    def __init__(self):
        super().__init__(show_automatic_box=True)

        self.setFixedHeight(410)

        main_box = gui.widgetBox(self.controlArea,
                                 "Line Profiles", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 10, height=300)

        button_box = gui.widgetBox(main_box,
                                   "", orientation="horizontal",
                                   width=self.CONTROL_AREA_WIDTH - 25)

        gui.button(button_box, self, "Debye-Waller Parameters", height=40, callback=self.send_debye_waller)

        orangegui.comboBox(main_box, self, "use_single_parameter_set", label="Use single set of Parameters", labelWidth=350, orientation="horizontal",
                           items=["No", "Yes"], callback=self.set_use_single_parameter_set, sendSelectedValue=False)

        orangegui.separator(main_box)

        self.debye_wallers_tabs = gui.tabWidget(main_box)

        self.set_use_single_parameter_set(on_init=True)

        runaction = OWAction("Send Debye-Waller Parameters", self)
        runaction.triggered.connect(self.send_debye_waller)
        self.addAction(runaction)

        orangegui.rubber(self.controlArea)

    def get_max_height(self):
        return 700

    def set_use_single_parameter_set(self, on_init=False):
        self.debye_wallers_tabs.clear()
        self.debye_wallers_box_array = []

        dimension = len(self.debye_waller_factors) if self.fit_global_parameters is None else self.fit_global_parameters.measured_dataset.get_diffraction_patterns_number()
        phases_number = len(self.debye_waller_factors[0]) if self.fit_global_parameters is None else self.fit_global_parameters.measured_dataset.get_phases_number()

        for diffraction_pattern_index in range(1 if self.use_single_parameter_set == 1 else dimension):
            debye_waller_tab = gui.createTabPage(self.debye_wallers_tabs, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, diffraction_pattern_index, self.use_single_parameter_set == 1))

            # qui analisi delle fasi
            if diffraction_pattern_index < len(self.debye_waller_factors):  # keep the existing
                use_debye_waller_factors = []
                debye_waller_factors = []
                debye_waller_factors_fixed = []
                debye_waller_factors_has_min = []
                debye_waller_factors_min = []
                debye_waller_factors_has_max = []
                debye_waller_factors_max = []
                debye_waller_factors_function = []
                debye_waller_factors_function_value = []

                for phase_index in range(phases_number):
                    if phase_index < len(self.debye_waller_factors[diffraction_pattern_index]):
                        use_debye_waller_factors.append(self.use_debye_waller_factors[diffraction_pattern_index][phase_index])
                        debye_waller_factors.append(self.debye_waller_factors[diffraction_pattern_index][phase_index])
                        debye_waller_factors_fixed.append(self.debye_waller_factors_fixed[diffraction_pattern_index][phase_index])
                        debye_waller_factors_has_min.append(self.debye_waller_factors_has_min[diffraction_pattern_index][phase_index])
                        debye_waller_factors_min.append(self.debye_waller_factors_min[diffraction_pattern_index][phase_index])
                        debye_waller_factors_has_max.append(self.debye_waller_factors_has_max[diffraction_pattern_index][phase_index])
                        debye_waller_factors_max.append(self.debye_waller_factors_max[diffraction_pattern_index][phase_index])
                        debye_waller_factors_function.append(self.debye_waller_factors_function[diffraction_pattern_index][phase_index])
                        debye_waller_factors_function_value.append(self.debye_waller_factors_function_value[diffraction_pattern_index][phase_index])
                    else:
                        use_debye_waller_factors.append(1)
                        debye_waller_factors.append(0.1)
                        debye_waller_factors_fixed.append(0)
                        debye_waller_factors_has_min.append(0)
                        debye_waller_factors_min.append(0.0)
                        debye_waller_factors_has_max.append(0.0)
                        debye_waller_factors_max.append(0.0)
                        debye_waller_factors_function.append(0)
                        debye_waller_factors_function_value.append("")

                debye_waller_box = DebyeWallerBox(widget=self,
                                                  parent=debye_waller_tab,
                                                  diffraction_pattern_index=diffraction_pattern_index,
                                                  use_debye_waller_factors=use_debye_waller_factors,
                                                  debye_waller_factors=debye_waller_factors,
                                                  debye_waller_factors_fixed=debye_waller_factors_fixed,
                                                  debye_waller_factors_has_min=debye_waller_factors_has_min,
                                                  debye_waller_factors_min=debye_waller_factors_min,
                                                  debye_waller_factors_has_max=debye_waller_factors_has_max,
                                                  debye_waller_factors_max=debye_waller_factors_max,
                                                  debye_waller_factors_function=debye_waller_factors_function,
                                                  debye_waller_factors_function_value=debye_waller_factors_function_value)
            else:
                debye_waller_box = DebyeWallerBox(widget=self,
                                                  parent=debye_waller_tab,
                                                  diffraction_pattern_index=diffraction_pattern_index,
                                                  use_debye_waller_factors=[1] * phases_number,
                                                  debye_waller_factors=[0.1] * phases_number,
                                                  debye_waller_factors_fixed=[0] * phases_number,
                                                  debye_waller_factors_has_min=[0] * phases_number,
                                                  debye_waller_factors_min=[0.0] * phases_number,
                                                  debye_waller_factors_has_max=[0.0] * phases_number,
                                                  debye_waller_factors_max=[0.0] * phases_number,
                                                  debye_waller_factors_function=[0] * phases_number,
                                                  debye_waller_factors_function_value=[""] * phases_number)

            self.debye_wallers_box_array.append(debye_waller_box)

            if not on_init: self.dumpSettings()

    def send_debye_waller(self):
        try:
            if not self.fit_global_parameters is None:
                self.dumpSettings()

                thermal_parameters = self.fit_global_parameters.get_thermal_parameters(ThermalParameters.__name__)

                if thermal_parameters is None:
                    dimension = self.fit_global_parameters.measured_dataset.get_diffraction_patterns_number() if self.use_single_parameter_set == 0 else 1
                    thermal_parameters = [ThermalParameters(phases_number=self.fit_global_parameters.measured_dataset.get_phases_number())] * dimension
                else:
                    thermal_parameters = copy.deepcopy(thermal_parameters)

                for index in range(len(self.debye_wallers_box_array)):
                    self.debye_wallers_box_array[index].update_thermal_parameters_of_phases(thermal_parameters[index])

                use_debye_waller_factor = False
                debye_waller_factor_function = False
                send_data = True

                for thermal_parameters_of_phases in thermal_parameters:
                    for debye_waller_factor in thermal_parameters_of_phases.debye_waller_factors:
                        if not debye_waller_factor is None: use_debye_waller_factor = True
                        if debye_waller_factor.function: debye_waller_factor_function = True

                if use_debye_waller_factor and not debye_waller_factor_function:
                    if not self.fit_global_parameters.measured_dataset.get_phase(0).use_structure:
                        send_data = ConfirmDialog.confirmed(parent=self, message="Debye-Waller factor is better refined when the structural model is activated.\nProceed anyway?")

                if send_data:
                    self.fit_global_parameters.set_thermal_parameters(thermal_parameters)
                    self.fit_global_parameters.regenerate_parameters()
                    self.fit_global_parameters.evaluate_functions()

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

                phases = self.fit_global_parameters.measured_dataset.phases
                if phases is None: raise ValueError("Add Phase(s) before this widget")

                diffraction_patterns = self.fit_global_parameters.measured_dataset.diffraction_patterns
                if diffraction_patterns is None: raise ValueError("Add Diffraction Pattern(s) before this widget!")

                thermal_parameters = self.fit_global_parameters.get_instrumental_parameters(ThermalParameters.__name__)

                self.set_use_single_parameter_set(on_init=True)

                if self.use_single_parameter_set == 0:  # NO
                    if not thermal_parameters is None:
                        for diffraction_pattern_index in range(len(thermal_parameters)):
                            thermal_parameters_item = self.fit_global_parameters.get_instrumental_parameters_item(ThermalParameters.__name__, diffraction_pattern_index)

                            self.debye_wallers_tabs.setTabText(diffraction_pattern_index,
                                                               OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, diffraction_pattern_index, False))

                            debye_waller_box = self.debye_wallers_box_array[diffraction_pattern_index]

                            if not thermal_parameters_item is None: debye_waller_box.set_data(thermal_parameters_item)
                else:
                    if thermal_parameters is None:
                        self.set_use_single_parameter_set(True)
                    else:
                        self.__check_data_congruence(thermal_parameters)

                        thermal_parameters_item = self.fit_global_parameters.get_thermal_parameters_item(thermal_parameters.__name__, 0)

                        self.debye_wallers_tabs.setTabText(0, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, 0, True))

                        if not thermal_parameters_item is None: self.debye_wallers_box_array[0].set_data(thermal_parameters_item)

                self.dumpSettings()

                if self.is_automatic_run:
                    self.send_debye_waller()

            except Exception as e:
                QMessageBox.critical(self, "Error",
                                     str(e),
                                     QMessageBox.Ok)

                if self.IS_DEVELOP: raise e

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def get_parameter_box_array(self):
        return self.debye_wallers_box_array

    def dumpSettings(self):
        self.dump_use_debye_waller_factors()
        self.dump_debye_waller_factors()

    def dump_use_debye_waller_factors(self): self.dump_variable("use_debye_waller_factors")
    def dump_debye_waller_factors(self): self.dump_parameter("debye_waller_factors")

from PyQt5.QtWidgets import QVBoxLayout
from orangecontrib.wonder.util.gui_utility import InnerBox

class DebyeWallerBox(InnerBox):
    widget = None
    is_on_init = True

    parameter_functions = {}

    diffraction_pattern_index = 0

    def __init__(self,
                 widget=None,
                 parent=None,
                 diffraction_pattern_index=0,
                 use_debye_waller_factors=[],
                 debye_waller_factors=[],
                 debye_waller_factors_fixed=[],
                 debye_waller_factors_has_min=[],
                 debye_waller_factors_min=[],
                 debye_waller_factors_has_max=[],
                 debye_waller_factors_max=[],
                 debye_waller_factors_function=[],
                 debye_waller_factors_function_value=[]):
        super(DebyeWallerBox, self).__init__()

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedWidth(widget.CONTROL_AREA_WIDTH - 35)
        self.setFixedHeight(140)

        self.widget = widget
        self.diffraction_pattern_index = diffraction_pattern_index

        self.use_debye_waller_factors = use_debye_waller_factors
        self.debye_waller_factors = debye_waller_factors
        self.debye_waller_factors_fixed = debye_waller_factors_fixed
        self.debye_waller_factors_has_min = debye_waller_factors_has_min
        self.debye_waller_factors_min = debye_waller_factors_min
        self.debye_waller_factors_has_max = debye_waller_factors_has_max
        self.debye_waller_factors_max = debye_waller_factors_max
        self.debye_waller_factors_function = debye_waller_factors_function
        self.debye_waller_factors_function_value = debye_waller_factors_function_value

        self.CONTROL_AREA_WIDTH = widget.CONTROL_AREA_WIDTH - 45

        parent.layout().addWidget(self)
        container = self

        self.debye_waller_of_phases_tabs = gui.tabWidget(container)
        self.debye_waller_of_phases_box_array = []

        for phase_index in range(len(self.debye_waller_factors)):
            debye_waller_of_phase_tab = gui.createTabPage(self.debye_waller_of_phases_tabs, OWGenericWidget.phase_name(self.widget.fit_global_parameters, phase_index))

            debye_waller_of_phase_box = DebyeWallerOfPhaseBox(widget=widget,
                                                              widget_container=self,
                                                              parent=debye_waller_of_phase_tab,
                                                              diffraction_pattern_index=diffraction_pattern_index,
                                                              phase_index=phase_index,
                                                              use_debye_waller_factor=self.use_debye_waller_factors[phase_index],
                                                              debye_waller_factor=self.debye_waller_factors[phase_index],
                                                              debye_waller_factor_fixed=self.debye_waller_factors_fixed[phase_index],
                                                              debye_waller_factor_has_min=self.debye_waller_factors_has_min[phase_index],
                                                              debye_waller_factor_min=self.debye_waller_factors_min[phase_index],
                                                              debye_waller_factor_has_max=self.debye_waller_factors_has_max[phase_index],
                                                              debye_waller_factor_max=self.debye_waller_factors_max[phase_index],
                                                              debye_waller_factor_function=self.debye_waller_factors_function[phase_index],
                                                              debye_waller_factor_function_value=self.debye_waller_factors_function_value[phase_index])

            self.debye_waller_of_phases_box_array.append(debye_waller_of_phase_box)

    def update_thermal_parameters_of_phases(self, thermal_parameters_of_phases):
        for phase_index in range(len(self.debye_waller_factors)):
            self.debye_waller_of_phases_box_array[phase_index].update_debye_waller(thermal_parameters_of_phases)

    def set_data(self, thermal_parameters):
        for phase_index in range(len(self.debye_waller_of_phases_box_array)):
            debye_waller_of_phases_box = self.debye_waller_of_phases_box_array[phase_index]
            debye_waller_of_phases_box.set_data(thermal_parameters)
            self.debye_waller_of_phases_tabs.setTabText(phase_index, OWGenericWidget.phase_name(self.widget.fit_global_parameters, phase_index))

    def get_parameter_box_array(self):
        return self.debye_waller_of_phases_box_array

    def dumpSettings(self):
        self.dump_use_debye_waller_factors()
        self.dump_debye_waller_factors()

    def dump_use_debye_waller_factors(self):
        OWGenericWidget.dump_variable_in_widget(self, "use_debye_waller_factors", variable_name_in_box="use_debye_waller_factor")
        self.widget.dump_use_debye_waller_factors()

    def dump_debye_waller_factors(self):
        OWGenericWidget.dump_parameter_in_widget(self, "debye_waller_factors", parameter_name_in_box="debye_waller_factor")
        self.widget.dump_debye_waller_factors()

class DebyeWallerOfPhaseBox(InnerBox):
    widget = None
    is_on_init = True

    parameter_functions = {}

    diffraction_pattern_index = 0
    phase_index = 0

    def __init__(self,
                 widget=None,
                 widget_container=None,
                 parent=None,
                 diffraction_pattern_index=0,
                 phase_index=0,
                 use_debye_waller_factor=1,
                 debye_waller_factor=0.1,
                 debye_waller_factor_fixed=0,
                 debye_waller_factor_has_min=0,
                 debye_waller_factor_min=0.0,
                 debye_waller_factor_has_max=0,
                 debye_waller_factor_max=0.0,
                 debye_waller_factor_function=0,
                 debye_waller_factor_function_value=""):
        super(DebyeWallerOfPhaseBox, self).__init__()

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.setFixedWidth(widget.CONTROL_AREA_WIDTH - 35)
        self.setFixedHeight(200)

        self.widget = widget
        self.widget_container = widget_container
        self.diffraction_pattern_index = diffraction_pattern_index
        self.phase_index = phase_index

        self.use_debye_waller_factor = use_debye_waller_factor
        self.debye_waller_factor = debye_waller_factor
        self.debye_waller_factor_fixed = debye_waller_factor_fixed
        self.debye_waller_factor_has_min = debye_waller_factor_has_min
        self.debye_waller_factor_min = debye_waller_factor_min
        self.debye_waller_factor_has_max = debye_waller_factor_has_max
        self.debye_waller_factor_max = debye_waller_factor_max
        self.debye_waller_factor_function = debye_waller_factor_function
        self.debye_waller_factor_function_value = debye_waller_factor_function_value

        self.CONTROL_AREA_WIDTH = widget.CONTROL_AREA_WIDTH - 65

        parent.layout().addWidget(self)
        container = self

        orangegui.comboBox(container, self, "use_debye_waller_factor", label="Calculate", items=["No", "Yes"], labelWidth=250, orientation="horizontal", callback=self.set_dw)

        self.box_dw = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 10, height=30)
        self.box_dw_empty = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 10, height=30)

        OWGenericWidget.create_box_in_widget(self, self.box_dw, "debye_waller_factor", label="B [Å-2]", min_value=0.0, max_value=1.0, min_accepted=True, max_accepted=True, add_callback=True, trim=25)

        self.is_on_init = False

    def set_dw(self):
        self.box_dw.setVisible(self.use_debye_waller_factor == 1)
        self.box_dw_empty.setVisible(self.use_debye_waller_factor == 0)

        self.widget_container.dump_use_debye_waller_factors()

    def callback_debye_waller_factor(self):
        if not self.is_on_init: self.widget_container.dump_debye_waller_factors()

    def get_parameters_prefix(self):
        return ThermalParameters.get_parameters_prefix() + self.get_parameter_progressive()

    def get_parameter_progressive(self):
        return str(self.diffraction_pattern_index + 1) + "_" + str(self.phase_index + 1) + "_"

    def set_data(self, thermal_parameters):
        debye_waller_factor = thermal_parameters.get_debye_waller_factor(phase_index=self.phase_index)

        if not debye_waller_factor is None:
            self.use_debye_waller_factor = 1

            debye_waller_factor = debye_waller_factor.duplicate()
            debye_waller_factor.rescale(100)  # CONVERSIONE from nm-2 to A-2

            OWGenericWidget.populate_fields_in_widget(self, "debye_waller_factor", debye_waller_factor, value_only=True)

    def update_debye_waller(self, thermal_parameters):
        if self.use_debye_waller_factor == 1 and not self.debye_waller_factor_function == 1:
            congruence.checkStrictlyPositiveNumber(self.debye_waller_factor, "B")

        debye_waller_factor = None if self.use_debye_waller_factor == 0 else OWGenericWidget.populate_parameter_in_widget(self, "debye_waller_factor", self.get_parameters_prefix())
        if not debye_waller_factor is None: debye_waller_factor.rescale(0.01)  # CONVERSIONE from A-2 to nm-2

        thermal_parameters.set_debye_waller_factor(self.phase_index, debye_waller_factor)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWDebyeWaller()
    ow.show()
    a.exec_()
    ow.saveSettings()
