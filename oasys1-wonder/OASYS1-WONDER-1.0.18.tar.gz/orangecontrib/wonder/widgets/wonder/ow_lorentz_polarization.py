import sys

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui
from orangecontrib.wonder.util import congruence
from orangecontrib.wonder.fit.parameters.instrument.polarization_parameters import PolarizationParameters, Beampath, LorentzFormula

class OWLorentzPolarization(OWGenericDiffractionPatternParametersWidget):
    name = "Lorentz-Polarization Factors"
    description = "Define Lorentz-Polarization Factor"
    icon = "icons/lorentz_polarization.png"
    priority = 9

    use_lorentz_factor      = Setting([1])
    lorentz_formula         = Setting([LorentzFormula.Shkl_Shkl])
    use_polarization_factor = Setting([0])
    degree_of_polarization  = Setting([0.0])
    beampath                = Setting([Beampath.PRIMARY])
    use_twotheta_mono       = Setting([1])
    twotheta_mono           = Setting([28.443])

    def __init__(self):
        super().__init__()

    def get_max_height(self):
        return 500

    def get_parameter_name(self):
        return "Lorentz-Polarization"

    def get_current_dimension(self):
        return len(self.use_lorentz_factor)

    def get_parameter_box_instance(self, parameter_tab, index):
        return PolarizationParametersBox(widget=self,
                                         parent=parameter_tab,
                                         index=index,
                                         use_lorentz_factor=self.use_lorentz_factor[index],
                                         lorentz_formula=self.lorentz_formula[index],
                                         use_polarization_factor=self.use_polarization_factor[index],
                                         degree_of_polarization=self.degree_of_polarization[index],
                                         beampath=self.beampath[index],
                                         use_twotheta_mono=self.use_twotheta_mono[index],
                                         twotheta_mono=self.twotheta_mono[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return PolarizationParametersBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        self.fit_global_parameters.set_instrumental_parameters([self.get_parameter_box(index).get_lorentz_polarization() for index in range(self.get_current_dimension())])

    def get_parameter_array(self):
        return self.fit_global_parameters.get_instrumental_parameters(PolarizationParameters.__name__)

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.get_instrumental_parameters_item(PolarizationParameters.__name__, diffraction_pattern_index)

    def dumpSettings(self):
        self.dump_use_lorentz_factor()
        self.dump_lorentz_formula()
        self.dump_use_polarization_factor()
        self.dump_degree_of_polarization()
        self.dump_beampath()
        self.dump_use_twotheta_mono()
        self.dump_twotheta_mono()

    def dump_use_lorentz_factor(self): self.dump_variable("use_lorentz_factor")
    def dump_lorentz_formula(self): self.dump_variable("lorentz_formula")
    def dump_use_polarization_factor(self): self.dump_variable("use_polarization_factor")
    def dump_degree_of_polarization(self): self.dump_variable("degree_of_polarization")
    def dump_beampath(self): self.dump_variable("beampath")
    def dump_use_twotheta_mono(self): self.dump_variable("use_twotheta_mono")
    def dump_twotheta_mono(self): self.dump_variable("twotheta_mono")

class PolarizationParametersBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index=0,
                 use_lorentz_factor=1,
                 lorentz_formula=LorentzFormula.Shkl_Shkl,
                 use_polarization_factor=0,
                 degree_of_polarization=0.0,
                 beampath=Beampath.PRIMARY,
                 use_twotheta_mono=1,
                 twotheta_mono=28.443):
        super(PolarizationParametersBox, self).__init__(widget=widget,
                                                        parent=parent,
                                                        index=index,
                                                        use_lorentz_factor=use_lorentz_factor,
                                                        lorentz_formula = lorentz_formula,
                                                        use_polarization_factor = use_polarization_factor,
                                                        degree_of_polarization = degree_of_polarization,
                                                        beampath = beampath,
                                                        use_twotheta_mono = use_twotheta_mono,
                                                        twotheta_mono = twotheta_mono)

    def init_fields(self, **kwargs):
        self.use_lorentz_factor      = kwargs["use_lorentz_factor"]
        self.lorentz_formula         = kwargs["lorentz_formula"]
        self.use_polarization_factor = kwargs["use_polarization_factor"]
        self.degree_of_polarization  = kwargs["degree_of_polarization"]
        self.beampath                = kwargs["beampath"]
        self.use_twotheta_mono       = kwargs["use_twotheta_mono"]
        self.twotheta_mono           = kwargs["twotheta_mono"]

    def init_gui(self, container):
        orangegui.comboBox(container, self, "use_lorentz_factor", label="Add Lorentz Factor", items=["No", "Yes"], labelWidth=300, orientation="horizontal", callback=self.set_LorentzFactor)

        self.lorentz_box = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20, height=30)
        self.lorentz_box_empty = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20, height=30)

        orangegui.comboBox(self.lorentz_box, self, "lorentz_formula", label="Formula", items=LorentzFormula.tuple(), labelWidth=300, orientation="horizontal", callback=self.widget.dump_lorentz_formula)

        self.set_LorentzFactor()

        orangegui.separator(container)

        orangegui.comboBox(container, self, "use_polarization_factor", label="Add Polarization Factor", items=["No", "Yes"], labelWidth=300,
                           orientation="horizontal", callback=self.set_Polarization)

        self.polarization_box = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20, height=200)
        self.polarization_box_empty = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20, height=200)

        gui.lineEdit(self.polarization_box, self, "degree_of_polarization", "Deg. Pol. (0\u2264Q\u22641)", labelWidth=300, valueType=float, callback=self.widget.dump_degree_of_polarization)

        orangegui.comboBox(self.polarization_box, self, "use_twotheta_mono", label="Use Monochromator", items=["No", "Yes"], labelWidth=300,
                           orientation="horizontal", callback=self.set_Monochromator)

        self.monochromator_box = gui.widgetBox(self.polarization_box, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20, height=95)
        self.monochromator_box_empty = gui.widgetBox(self.polarization_box, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 20, height=95)

        orangegui.comboBox(self.monochromator_box, self, "beampath", label="Beampath", items=Beampath.tuple(), labelWidth=300,
                           orientation="horizontal", callback=self.widget.dump_beampath)

        gui.lineEdit(self.monochromator_box, self, "twotheta_mono", "2\u03B8 Monochromator [deg]", labelWidth=300, valueType=float, callback=self.widget.dump_twotheta_mono)

        self.set_Polarization()

    def set_LorentzFactor(self):
        self.lorentz_box.setVisible(self.use_lorentz_factor==1)
        self.lorentz_box_empty.setVisible(self.use_lorentz_factor==0)
        
        if not self.is_on_init: self.widget.dump_use_lorentz_factor()

    def set_Monochromator(self):
        self.monochromator_box.setVisible(self.use_twotheta_mono==1)
        self.monochromator_box_empty.setVisible(self.use_twotheta_mono==0)
        
        if not self.is_on_init: self.widget.dump_use_twotheta_mono()

    def set_Polarization(self):
        self.polarization_box.setVisible(self.use_polarization_factor==1)
        self.polarization_box_empty.setVisible(self.use_polarization_factor==0)
        if self.use_polarization_factor==1: self.set_Monochromator()
        
        if not self.is_on_init: self.widget.dump_use_polarization_factor()

    def get_basic_parameter_prefix(self):
        return PolarizationParameters.get_parameters_prefix()

    def get_lorentz_polarization(self):
        if self.use_polarization_factor == 1:
            congruence.checkPositiveNumber(self.degree_of_polarization, "Deg. Pol.")
            congruence.checkLessOrEqualThan(self.degree_of_polarization, 1.0, "Deg. Pol.", "1.0")

        if self.use_polarization_factor == 1 and self.use_twotheta_mono==1:
            congruence.checkStrictlyPositiveAngle(self.twotheta_mono, "2\u03B8 Monochromator")

        return PolarizationParameters(use_lorentz_factor=self.use_lorentz_factor == 1,
                                      lorentz_formula=self.lorentz_formula,
                                      use_polarization_factor=self.use_polarization_factor,
                                      twotheta_mono=None if (self.use_polarization_factor == 0 or self.use_twotheta_mono == 0) else self.twotheta_mono,
                                      beampath=self.beampath,
                                      degree_of_polarization=self.degree_of_polarization)
    
    def set_data(self, polarization_parameters):
        self.use_lorentz_factor = 1 if polarization_parameters.use_lorentz_factor else self.use_lorentz_factor
        self.lorentz_formula = polarization_parameters.lorentz_formula
        self.use_polarization_factor = 1 if polarization_parameters.use_polarization_factor else self.use_polarization_factor
        if self.use_polarization_factor == 1:
            self.degree_of_polarization = polarization_parameters.degree_of_polarization
            twotheta_mono = polarization_parameters.twotheta_mono
            if not twotheta_mono is None:
                self.use_twotheta_mono = 1
                self.twotheta_mono = twotheta_mono
                self.beampath = polarization_parameters.beampath
            else:
                self.use_twotheta_mono = 0

        self.set_LorentzFactor()
        self.set_Polarization()

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWLorentzPolarization()
    ow.show()
    a.exec_()
    ow.saveSettings()
