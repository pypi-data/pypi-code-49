import sys

from PyQt5.QtWidgets import QMessageBox

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericPhaseParameterWidget, ParameterActivableBox
from orangecontrib.wonder.util.gui_utility import gui
from oasys.widgets import congruence
from orangecontrib.wonder.fit.parameters.microstructure.size import SizeParameters
from wonder.fit.functions.wppm_functions import Distribution, Normalization, Shape, WulffCubeFace

class OWSize(OWGenericPhaseParameterWidget):
    name = "Size"
    description = "Define Size"
    icon = "icons/size.png"
    priority = 16

    active = Setting([1])

    shape = Setting([1])
    distribution = Setting([1])
    mu = Setting([4.0])
    mu_fixed = Setting([0])
    mu_has_min = Setting([1])
    mu_min = Setting([0.01])
    mu_has_max = Setting([0])
    mu_max = Setting([0.0])
    mu_function = Setting([0])
    mu_function_value = Setting([""])
    sigma = Setting([0.5])
    sigma_fixed = Setting([0])
    sigma_has_min = Setting([1])
    sigma_min = Setting([0.01])
    sigma_has_max = Setting([1])
    sigma_max = Setting([1.0])
    sigma_function = Setting([0])
    sigma_function_value = Setting([""])
    truncation = Setting([0.5])
    truncation_fixed = Setting([0])
    truncation_has_min = Setting([1])
    truncation_min = Setting([0.01])
    truncation_has_max = Setting([1])
    truncation_max = Setting([1.0])
    truncation_function = Setting([0])
    truncation_function_value = Setting([""])
    cube_face = Setting([1])
    add_saxs = Setting([False])
    normalize_to = Setting([0])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 500

    def get_parameter_name(self):
        return "Size"

    def get_current_dimension(self):
        return len(self.shape)

    def get_parameter_box_instance(self, parameter_tab, index):
        return SizeBox(widget=self,
                       parent=parameter_tab,
                       index = index,
                       active = self.active[index],
                       shape=self.shape[index],
                       distribution = self.distribution[index],
                       mu = self.mu[index],
                       mu_fixed = self.mu_fixed[index],
                       mu_has_min = self.mu_has_min[index],
                       mu_min = self.mu_min[index],
                       mu_has_max = self.mu_has_max[index],
                       mu_max = self.mu_max[index],
                       mu_function = self.mu_function[index],
                       mu_function_value = self.mu_function_value[index],
                       sigma = self.sigma[index],
                       sigma_fixed = self.sigma_fixed[index],
                       sigma_has_min = self.sigma_has_min[index],
                       sigma_min = self.sigma_min[index],
                       sigma_has_max = self.sigma_has_max[index],
                       sigma_max = self.sigma_max[index],
                       sigma_function = self.sigma_function[index],
                       sigma_function_value = self.sigma_function_value[index],
                       truncation = self.truncation[index],
                       truncation_fixed = self.truncation_fixed[index],
                       truncation_has_min = self.truncation_has_min[index],
                       truncation_min = self.truncation_min[index],
                       truncation_has_max = self.truncation_has_max[index],
                       truncation_max = self.truncation_max[index],
                       truncation_function = self.truncation_function[index],
                       truncation_function_value = self.truncation_function_value[index],
                       cube_face = self.cube_face[index],
                       add_saxs = self.add_saxs[index],
                       normalize_to = self.normalize_to[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return SizeBox(widget=self, parent=parameter_tab, index=index, active=0)

    def get_parameter_array(self):
        return self.fit_global_parameters.size_parameters

    def get_parameter_item(self, phase_index):
        return self.fit_global_parameters.get_size_parameters(phase_index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_size_parameters([self.get_parameter_box(index).get_size_parameters() for index in range(self.get_current_dimension())])

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpOtherSettings(self):
        self.dump_shape()
        self.dump_distribution()
        self.dump_mu()
        self.dump_sigma()
        self.dump_truncation()
        self.dump_cube_face()
        self.dump_add_saxs()
        self.dump_normalize_to()

    def dump_shape(self): self.dump_variable("shape")
    def dump_distribution(self): self.dump_variable("distribution")
    def dump_mu(self): self.dump_parameter("mu")
    def dump_sigma(self): self.dump_parameter("sigma")
    def dump_truncation(self): self.dump_parameter("truncation")
    def dump_cube_face(self): self.dump_variable("cube_face")
    def dump_add_saxs(self): self.dump_variable("add_saxs")
    def dump_normalize_to(self): self.dump_variable("normalize_to")

class SizeBox(ParameterActivableBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 active=1,
                 shape=1,
                 distribution=1,
                 mu=4.0,
                 mu_fixed=0,
                 mu_has_min=1,
                 mu_min=0.01,
                 mu_has_max=0,
                 mu_max=0.0,
                 mu_function=0,
                 mu_function_value="",
                 sigma=0.5,
                 sigma_fixed=0,
                 sigma_has_min=1,
                 sigma_min=0.01,
                 sigma_has_max=1,
                 sigma_max=1.0,
                 sigma_function=0,
                 sigma_function_value="",
                 truncation=0.5,
                 truncation_fixed=0,
                 truncation_has_min=1,
                 truncation_min=0.01,
                 truncation_has_max=1,
                 truncation_max=1.0,
                 truncation_function=0,
                 truncation_function_value="",
                 cube_face=1,
                 add_saxs=False,
                 normalize_to=0):
        super(SizeBox, self).__init__(widget=widget,
                                      parent=parent,
                                      index=index,
                                      active=active,
                                      shape=shape,
                                      distribution=distribution,
                                      mu=mu,
                                      mu_fixed=mu_fixed,
                                      mu_has_min=mu_has_min,
                                      mu_min=mu_min,
                                      mu_has_max=mu_has_max,
                                      mu_max=mu_max,
                                      mu_function=mu_function,
                                      mu_function_value=mu_function_value,
                                      sigma=sigma,
                                      sigma_fixed=sigma_fixed,
                                      sigma_has_min=sigma_has_min,
                                      sigma_min=sigma_min,
                                      sigma_has_max=sigma_has_max,
                                      sigma_max=sigma_max,
                                      sigma_function=sigma_function,
                                      sigma_function_value=sigma_function_value,
                                      truncation=truncation,
                                      truncation_fixed=truncation_fixed,
                                      truncation_has_min=truncation_has_min,
                                      truncation_min=truncation_min,
                                      truncation_has_max=truncation_has_max,
                                      truncation_max=truncation_max,
                                      truncation_function=truncation_function,
                                      truncation_function_value=truncation_function_value,
                                      cube_face=cube_face,
                                      add_saxs=add_saxs,
                                      normalize_to=normalize_to)

    def init_fields(self, **kwargs):
        self.shape                     = kwargs["shape"]
        self.distribution              = kwargs["distribution"]
        self.mu                        = kwargs["mu"]
        self.mu_fixed                  = kwargs["mu_fixed"]
        self.mu_has_min                = kwargs["mu_has_min"]
        self.mu_min                    = kwargs["mu_min"]
        self.mu_has_max                = kwargs["mu_has_max"]
        self.mu_max                    = kwargs["mu_max"]
        self.mu_function               = kwargs["mu_function"]
        self.mu_function_value         = kwargs["mu_function_value"]
        self.sigma                     = kwargs["sigma"]
        self.sigma_fixed               = kwargs["sigma_fixed"]
        self.sigma_has_min             = kwargs["sigma_has_min"]
        self.sigma_min                 = kwargs["sigma_min"]
        self.sigma_has_max             = kwargs["sigma_has_max"]
        self.sigma_max                 = kwargs["sigma_max"]
        self.sigma_function            = kwargs["sigma_function"]
        self.sigma_function_value      = kwargs["sigma_function_value"]
        self.truncation                = kwargs["truncation"]
        self.truncation_fixed          = kwargs["truncation_fixed"]
        self.truncation_has_min        = kwargs["truncation_has_min"]
        self.truncation_min            = kwargs["truncation_min"]
        self.truncation_has_max        = kwargs["truncation_has_max"]
        self.truncation_max            = kwargs["truncation_max"]
        self.truncation_function       = kwargs["truncation_function"]
        self.truncation_function_value = kwargs["truncation_function_value"]
        self.cube_face                 = kwargs["cube_face"]
        self.add_saxs                  = kwargs["add_saxs"]
        self.normalize_to              = kwargs["normalize_to"]

    def init_main_box(self):
        self.cb_shape = orangegui.comboBox(self.main_box, self, "shape", label="Shape", items=Shape.tuple(), callback=self.set_shape, orientation="horizontal")
        self.cb_distribution = orangegui.comboBox(self.main_box, self, "distribution", label="Distribution", items=Distribution.tuple(), callback=self.set_distribution, orientation="horizontal")

        orangegui.separator(self.main_box)

        size_box = gui.widgetBox(self.main_box, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH-10)

        self.sigma_box = gui.widgetBox(size_box, "", orientation="vertical")

        OWGenericWidget.create_box_in_widget(self, self.sigma_box, "mu", label="\u03bc or D", add_callback=True, min_value=0.0, min_accepted=False, trim=25)
        OWGenericWidget.create_box_in_widget(self, self.sigma_box,  "sigma", label="\u03c3", add_callback=True, min_value=0.0, min_accepted=False, trim=25)

        self.truncation_box = gui.widgetBox(size_box, "", orientation="vertical")

        OWGenericWidget.create_box_in_widget(self, self.truncation_box, "truncation", label="trunc.", add_callback=True, min_value=0.0, max_value=1.0, min_accepted=True, trim=25)

        self.cb_cube_face = orangegui.comboBox(self.truncation_box, self, "cube_face", label="Cube Face", items=WulffCubeFace.tuple(), 
                                               callback=self.callback_cube_face, labelWidth=300, orientation="horizontal")

        self.saxs_box = gui.widgetBox(size_box, "", orientation="vertical")

        orangegui.comboBox(self.saxs_box, self, "add_saxs", label="Add SAXS", items=["No", "Yes"], labelWidth=300, orientation="horizontal",
                           callback=self.set_add_saxs)

        self.normalize_box = gui.widgetBox(self.saxs_box, "", orientation="vertical")

        orangegui.comboBox(self.normalize_box, self, "normalize_to", label="Normalize to", items=Normalization.tuple(), 
                           callback=self.callback_normalize_to, labelWidth=300, orientation="horizontal")

        self.set_shape()
        
    def set_shape(self):
        if self.cb_distribution.currentText() == Distribution.LOGNORMAL:
            if not (self.cb_shape.currentText() == Shape.SPHERE or self.cb_shape.currentText() == Shape.WULFF):
                if not self.is_on_init:
                    QMessageBox.critical(self, "Error",
                                         "Only Sphere/Wulff Solid shape is supported",
                                         QMessageBox.Ok)
    
                    self.shape = 1
        elif not self.cb_shape.currentText() == Shape.SPHERE:
            if not self.is_on_init:
                QMessageBox.critical(self, "Error",
                                     "Only Sphere shape is supported",
                                     QMessageBox.Ok)

                self.shape = 1
            
        if not self.is_on_init: self.widget.dump_shape()
        
        self.set_distribution()

    def set_add_saxs(self):
        self.normalize_box.setVisible(self.add_saxs==1)
        
        if not self.is_on_init: self.widget.dump_add_saxs()

    def set_distribution(self, is_init=False):
        if not (self.cb_distribution.currentText() == Distribution.LOGNORMAL or \
                #self.cb_distribution.currentText() == Distribution.GAMMA or \
                self.cb_distribution.currentText() == Distribution.DELTA):
            if not is_init:
                QMessageBox.critical(self, "Error",
                                     #"Only Lognormal, Gamma and Delta distributions are supported",
                                     "Only Lognormal and Delta distributions are supported",
                                     QMessageBox.Ok)

                self.distribution = 1
        else:
            self.sigma_box.setVisible(self.cb_distribution.currentText() != Distribution.DELTA)
            self.saxs_box.setVisible(self.cb_distribution.currentText() == Distribution.DELTA)
            if self.cb_distribution.currentText() == Distribution.DELTA: self.set_add_saxs()
            self.truncation_box.setVisible(self.cb_distribution.currentText() == Distribution.LOGNORMAL and self.cb_shape.currentText() == Shape.WULFF)

        if not self.is_on_init: self.widget.dump_distribution()

    def callback_mu(self):
        if not self.is_on_init: self.widget.dump_mu()

    def callback_sigma(self):
        if not self.is_on_init: self.widget.dump_sigma()
        
    def callback_truncation(self):
        if not self.is_on_init: self.widget.dump_truncation()

    def callback_cube_face(self):
        if not self.is_on_init: self.widget.dump_cube_face()

    def callback_normalize_to(self):
        if not self.is_on_init: self.widget.dump_normalize_to()

    def get_basic_parameter_prefix(self):
        return SizeParameters.get_parameters_prefix()
    
    def set_data(self, size_parameters):
        OWGenericWidget.populate_fields_in_widget(self, "mu",    size_parameters.mu)
        OWGenericWidget.populate_fields_in_widget(self, "sigma", size_parameters.sigma)

        if size_parameters.shape == Shape.WULFF:
            OWGenericWidget.populate_fields_in_widget(self, "truncation", size_parameters.truncation)
            self.cb_cube_face.setCurrentText(size_parameters.cube_face)

        self.add_saxs = size_parameters.add_saxs

        if size_parameters.add_saxs:
            self.normalize_to = size_parameters.normalize_to

        self.set_shape()
        self.set_distribution()

    def get_size_parameters(self):
        if self.active == 0: return None
        else:
            if not self.mu_function == 1: congruence.checkStrictlyPositiveNumber(self.mu, "\u03bc or D")
            if self.cb_distribution.currentText() != Distribution.DELTA and not self.sigma_function == 1: congruence.checkStrictlyPositiveNumber(self.sigma, "\u03c3")
            if self.cb_distribution.currentText() == Distribution.DELTA and not self.fit_global_parameters.measured_dataset.phases[self.index].use_structure:
                raise Exception("Delta Distribution cannot be used when the structural model is not activated")

            return SizeParameters(shape=self.cb_shape.currentText(),
                                  distribution=self.cb_distribution.currentText(),
                                  mu=OWGenericWidget.populate_parameter_in_widget(self, "mu", self.get_parameters_prefix()),
                                  sigma=None if self.cb_distribution.currentText() == Distribution.DELTA else OWGenericWidget.populate_parameter_in_widget(self, "sigma", self.get_parameters_prefix()),
                                  truncation=OWGenericWidget.populate_parameter_in_widget(self, "truncation",self.get_parameters_prefix()) if (self.cb_distribution.currentText() == Distribution.LOGNORMAL and self.cb_shape.currentText() == Shape.WULFF) else None,
                                  cube_face=self.cb_cube_face.currentText() if (self.cb_distribution.currentText() == Distribution.LOGNORMAL and self.cb_shape.currentText() == Shape.WULFF) else None,
                                  add_saxs=self.add_saxs if self.cb_distribution.currentText() == Distribution.DELTA else False,
                                  normalize_to=self.normalize_to if self.cb_distribution.currentText() == Distribution.DELTA else None)

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a =  QApplication(sys.argv)
    ow = OWSize()
    ow.show()
    a.exec_()
    ow.saveSettings()
