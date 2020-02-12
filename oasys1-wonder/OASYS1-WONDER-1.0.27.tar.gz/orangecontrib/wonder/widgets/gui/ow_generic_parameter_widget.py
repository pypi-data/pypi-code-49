from PyQt5.QtWidgets import QMessageBox

from orangewidget.settings import Setting
from orangewidget import gui as orangegui
from orangewidget.widget import OWAction

from orangecontrib.wonder.widgets.gui.ow_generic_widget import OWGenericWidget
from orangecontrib.wonder.util.gui_utility import gui


class OWGenericParametersWidget(OWGenericWidget):
    want_main_area = False

    def __init__(self):
        super().__init__(show_automatic_box=True)

        self.main_box = gui.widgetBox(self.controlArea, self.get_parameter_name(), orientation="vertical", width=self.CONTROL_AREA_WIDTH - 10, height=self.get_height())

        self.button_box = gui.widgetBox(self.main_box, "", orientation="horizontal", width=self.CONTROL_AREA_WIDTH - 25)

        gui.button(self.button_box, self, "Send " + self.get_parameter_name(), height=40, callback=self.send_parameter)

        self.build_main_box()

        orangegui.separator(self.main_box)

        self.parameter_tabs = gui.tabWidget(self.main_box)
        self.parameter_box_array = []

        self.build_parameter_box_array()

        runaction = OWAction("Send " + self.get_parameter_name(), self)
        runaction.triggered.connect(self.send_parameter)
        self.addAction(runaction)

        orangegui.rubber(self.controlArea)

    def get_height(self):
        return self.get_max_height() - 100

    def build_main_box(self):
        raise NotImplementedError()

    def build_parameter_box_array(self):
        raise NotImplementedError()

    def set_data(self, data):
        raise NotImplementedError()

    def send_parameter(self):
        try:
            if not self.fit_global_parameters is None:
                self.dumpSettings()

                self.set_parameter_data()

                self.fit_global_parameters.evaluate_functions()
                self.fit_global_parameters.regenerate_parameters()

                self.send("Fit Global Parameters", self.fit_global_parameters)

        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 str(e),
                                 QMessageBox.Ok)

            if self.IS_DEVELOP: raise e

    def get_parameter_box_array(self):
        return self.parameter_box_array

    def get_parameter_box(self, index):
        return self.parameter_box_array[index]

    def get_parameter_name(self):
        raise NotImplementedError()

    def get_current_dimension(self):
        raise NotImplementedError()

    def get_parameter_box_instance(self, parameter_tab, index):
        raise NotImplementedError()

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        raise NotImplementedError()

    def set_parameter_data(self):
        raise NotImplementedError()

    def get_parameter_array(self):
        raise NotImplementedError()

    def get_parameter_item(self, diffraction_pattern_index):
        raise NotImplementedError()

    def dumpSettings(self):
        raise NotImplementedError()

# -----------------------------------------------------------------
# Widget with Parameters related to Diffraction Pattern(s)
# -----------------------------------------------------------------

class OWGenericDiffractionPatternParametersWidget(OWGenericParametersWidget):
    want_main_area = False

    use_single_parameter_set = Setting(0)

    def __init__(self):
        super().__init__()

    def build_main_box(self):
        orangegui.comboBox(self.main_box, self, "use_single_parameter_set", label="Use single set of Parameters", labelWidth=350, orientation="horizontal",
                           items=["No", "Yes"], callback=self.set_use_single_parameter_set, sendSelectedValue=False)

    def build_parameter_box_array(self):
        self.set_use_single_parameter_set(on_init=True)

    def set_use_single_parameter_set(self, on_init=False):
        self.parameter_tabs.clear()
        self.parameter_box_array.clear()

        dimension = self.get_current_dimension() if self.fit_global_parameters is None else self.fit_global_parameters.measured_dataset.get_diffraction_patterns_number()

        for index in range(1 if self.use_single_parameter_set == 1 else dimension):
            parameter_tab = gui.createTabPage(self.parameter_tabs, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, index, self.use_single_parameter_set == 1))

            if index < self.get_current_dimension():  # keep the existing
                parameter_box = self.get_parameter_box_instance(parameter_tab, index)
            else:
                parameter_box = self.get_empty_parameter_box_instance(parameter_tab, index)

            self.parameter_box_array.append(parameter_box)

            if not on_init: self.dumpSettings()

    def set_data(self, data):
        if not data is None:
            try:
                self.fit_global_parameters = data.duplicate()

                diffraction_patterns = self.fit_global_parameters.measured_dataset.diffraction_patterns
                if diffraction_patterns is None: raise ValueError("No Diffraction Pattern in input data!")

                parameters = self.get_parameter_array()

                if parameters is None:
                    self.set_use_single_parameter_set(on_init=True)
                else:
                    if self.use_single_parameter_set == 0:  # NO
                        tabs_to_remove = self.get_current_dimension() - len(parameters)

                        if tabs_to_remove > 0:
                            for index in range(tabs_to_remove):
                                self.parameter_tabs.removeTab(-1)
                                self.parameter_box_array.pop()

                        for diffraction_pattern_index in range(len(parameters)):
                            parameters_item = self.get_parameter_item(diffraction_pattern_index)

                            if diffraction_pattern_index < self.get_current_dimension():
                                parameter_box = self.parameter_box_array[diffraction_pattern_index]
                                self.parameter_tabs.setTabText(diffraction_pattern_index, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, diffraction_pattern_index, False))
                            else:
                                parameter_box = self.get_empty_parameter_box_instance(parameter_tab=gui.createTabPage(self.parameter_tabs, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, diffraction_pattern_index, False)),
                                                                                      index=diffraction_pattern_index)
                                self.parameter_box_array.append(parameter_box)

                            if not parameters_item is None: parameter_box.set_data(parameters_item)
                    else:
                        self.__check_data_congruence(parameters)

                        parameters_item = self.get_parameter_item(0)

                        self.parameter_tabs.setTabText(0, OWGenericWidget.diffraction_pattern_name(self.fit_global_parameters, 0, True))
                        if not parameters_item is None: self.parameter_box_array[0].set_data(parameters_item)

                self.dumpSettings()

                if self.is_automatic_run:
                    self.send_parameter()

            except Exception as e:
                QMessageBox.critical(self, "Error",
                                     str(e),
                                     QMessageBox.Ok)

                if self.IS_DEVELOP: raise e

    def __check_data_congruence(self, parameters):
        if (len(parameters) == 1 and self.use_single_parameter_set == 0) or (len(parameters) > 1 and self.use_single_parameter_set == 1):
            raise ValueError("Previous " + self.get_parameter_name() + " parameters are incongruent with the current choice of using a single set")



# -----------------------------------------------------------------
# Widget with Parameters related to Phase(s)
# -----------------------------------------------------------------
from orangecontrib.wonder.fit.parameters.measured_data.phase import Phase

class OWGenericPhaseParameterWidget(OWGenericParametersWidget):
    want_main_area =  False

    def __init__(self):
        super().__init__()

        try:
            getattr(self, "active")
        except:
            raise NotImplementedError("attribute 'active' is missing")

    def build_main_box(self):
        pass

    def build_parameter_box_array(self):
        if self.active is None or len(self.active) != self.get_current_dimension():
            self.active = [1]*self.get_current_dimension()

        for index in range(self.get_current_dimension()):
            parameter_box = self.get_parameter_box_instance(gui.createTabPage(self.parameter_tabs, Phase.get_default_name(index)), index)

            self.parameter_box_array.append(parameter_box)

    def set_data(self, data):
        if not data is None:
            try:
                if data.measured_dataset is None:
                    raise ValueError("Measured Dataset is missing")

                if data.measured_dataset.phases is None:
                    raise ValueError("Phases are missing")

                self.check_input_global_parameters(data)

                self.fit_global_parameters = data.duplicate()

                phases = self.fit_global_parameters.measured_dataset.phases

                tabs_to_remove = self.get_current_dimension()-len(phases)

                if tabs_to_remove > 0:
                    for index in range(tabs_to_remove):
                        self.parameter_tabs.removeTab(-1)
                        self.parameter_box_array.pop()

                for phase_index in range(len(phases)):
                    parameters = self.get_parameter_of_phase_item(phase_index)

                    if phase_index < self.get_current_dimension():
                        self.parameter_tabs.setTabText(phase_index, OWGenericWidget.phase_name(self.fit_global_parameters, phase_index))

                        parameter_box = self.get_parameter_box(phase_index)

                        if not parameters is None: parameter_box.set_data(parameters)
                    else:
                        parameter_box = self.get_empty_parameter_box_instance(gui.createTabPage(self.parameter_tabs, OWGenericWidget.phase_name(self.fit_global_parameters, phase_index)),
                                                                              phase_index)

                        if not parameters is None: parameter_box.set_data(parameters)

                        self.parameter_box_array.append(parameter_box)

                self.dumpSettings()

                if self.is_automatic_run:
                    self.send_parameter()

            except Exception as e:
                QMessageBox.critical(self, "Error",
                                     str(e),
                                     QMessageBox.Ok)

                if self.IS_DEVELOP: raise e

    def check_input_global_parameters(self, data):
        pass

    def get_parameter_of_phase_item(self, phase_index):
        if not self.get_parameter_array() is None:
            return self.get_parameter_item(phase_index)
        else:
            return None

    def dumpSettings(self):
        self.dump_active()
        self.dumpOtherSettings()

    def dump_active(self): self.dump_variable("active")

    def dumpOtherSettings(self):
        raise NotImplementedError

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from orangecontrib.wonder.util.gui_utility import InnerBox

class ParameterBox(InnerBox):
    widget = None
    is_on_init = True

    parameter_functions = {}

    index = 0

    def __init__(self, widget=None, parent=None, index=0, **kwargs):
        super(ParameterBox, self).__init__()

        self.widget = widget
        self.index = index

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)

        self.setFixedWidth(self.get_width())
        self.setFixedHeight(self.get_height())

        self.init_fields(**kwargs)

        self.CONTROL_AREA_WIDTH = widget.CONTROL_AREA_WIDTH - 45

        parent.layout().addWidget(self)
        container = self

        self.init_gui(container)

        self.is_on_init = False

    def get_width(self):
        return self.widget.CONTROL_AREA_WIDTH - 35

    def get_height(self):
        return 500

    def init_fields(self, **kwargs):
        raise NotImplementedError()

    def init_gui(self, container):
        raise NotImplementedError()

    def after_change_workspace_units(self):
        pass

    def get_parameters_prefix(self):
        return self.get_basic_parameter_prefix() + self.get_parameter_progressive()

    def get_basic_parameter_prefix(self):
        raise NotImplementedError()

    def get_parameter_progressive(self):
        return str(self.index + 1) + "_"

    def set_data(self, parameters):
        raise NotImplementedError()


class ParameterActivableBox(ParameterBox):

    active=1

    def __init__(self, widget=None, parent=None, index=0, active=1, **kwargs):
        super(ParameterActivableBox, self).__init__(widget, parent, index, **kwargs)

        self.active=active

        self.set_active()

    def init_gui(self, container):
        self.cb_active = orangegui.comboBox(container, self, "active", label="Active", items=["No", "Yes"], callback=self.set_active, orientation="horizontal")

        orangegui.separator(container)

        self.main_box = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH-10)

        self.init_main_box()

    def init_main_box(self):
        raise NotImplementedError()

    def set_active(self):
        self.main_box.setEnabled(self.active==1)

        if not self.is_on_init: self.widget.dump_active()
