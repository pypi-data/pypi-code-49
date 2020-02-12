import os, sys

from orangewidget.settings import Setting
from orangewidget import gui as orangegui

from orangecontrib.wonder.widgets.gui.ow_generic_parameter_widget import OWGenericWidget, OWGenericDiffractionPatternParametersWidget, ParameterBox
from orangecontrib.wonder.util.gui_utility import gui, ConfirmDialog
from orangecontrib.wonder.fit.parameters.measured_data.incident_radiation import IncidentRadiation
from orangecontrib.wonder.fit.parameters.fit_global_parameters import FitGlobalParameters
from orangecontrib.wonder.fit.parameters.fit_parameter import FitParameter

class Wavelenght:
    wavelength = 0.0
    weight = 0.0

    def __init__(self, wavelength, weight):
        self.wavelength = wavelength
        self.weight = weight
        self.is_principal = False

wavelengths_data = {}

def load_data_files():
    directory_files = os.path.join(os.path.dirname(__file__), "data")

    try:
        for path, dirs, files in os.walk(directory_files):

            for file_name in files:
                file = open(os.path.join(path, file_name), "r")

                rows = file.readlines()

                key = rows[0].strip()
                wavelengths = [None]*(len(rows)-1)
                highest_weight = 0.0
                for index in range(1, len(rows)):
                    data = rows[index].split()
                    wavelength = round(float(data[0].strip())/10, 8) # nm!
                    weight = round(float(data[1].strip()), 6)
                    highest_weight = highest_weight if weight <= highest_weight else weight

                    wavelengths[index-1] = Wavelenght(wavelength, weight)

                for wavelength in wavelengths:
                    if wavelength.weight == highest_weight:
                        wavelength.is_principal = True

                wavelengths_data[key] = wavelengths

    except Exception as err:
        raise Exception("Problems reading X-ray Tubes Wavelengths Configuration file: {0}".format(err))
    except:
        raise Exception("Unexpected error while reading X-ray Tubes Wavelengths Configuration file: ", sys.exc_info()[0])

load_data_files()

class OWRadiation(OWGenericDiffractionPatternParametersWidget):

    name = "Incident Radiation"
    description = "Incident Radiation"
    icon = "icons/lambda.png"
    priority = 1.1

    is_multiple_wavelength = Setting([0])
    
    wavelength = Setting([0.0826])
    wavelength_fixed = Setting([0])
    wavelength_has_min = Setting([0])
    wavelength_min = Setting([0.0])
    wavelength_has_max = Setting([0])
    wavelength_max = Setting([0.0])
    wavelength_function = Setting([0])
    wavelength_function_value = Setting([""])
    
    xray_tube_key = Setting(["CuKa2"])

    wavelength_2 = Setting([0])
    wavelength_2_fixed = Setting([1])
    wavelength_2_has_min = Setting([0])
    wavelength_2_min = Setting([0.0])
    wavelength_2_has_max = Setting([0])
    wavelength_2_max = Setting([0.0])
    wavelength_2_function = Setting([0])
    wavelength_2_function_value = Setting([""])

    wavelength_3 = Setting([0])
    wavelength_3_fixed = Setting([1])
    wavelength_3_has_min = Setting([0])
    wavelength_3_min = Setting([0.0])
    wavelength_3_has_max = Setting([0])
    wavelength_3_max = Setting([0.0])
    wavelength_3_function = Setting([0])
    wavelength_3_function_value = Setting([""])

    wavelength_4 = Setting([0])
    wavelength_4_fixed = Setting([1])
    wavelength_4_has_min = Setting([0])
    wavelength_4_min = Setting([0.0])
    wavelength_4_has_max = Setting([0])
    wavelength_4_max = Setting([0.0])
    wavelength_4_function = Setting([0])
    wavelength_4_function_value = Setting([""])

    wavelength_5 = Setting([0])
    wavelength_5_fixed = Setting([1])
    wavelength_5_has_min = Setting([0])
    wavelength_5_min = Setting([0.0])
    wavelength_5_has_max = Setting([0])
    wavelength_5_max = Setting([0.0])
    wavelength_5_function = Setting([0])
    wavelength_5_function_value = Setting([""])

    weight_2 = Setting([0])
    weight_2_fixed = Setting([1])
    weight_2_has_min = Setting([0])
    weight_2_min = Setting([0.0])
    weight_2_has_max = Setting([0])
    weight_2_max = Setting([0.0])
    weight_2_function = Setting([0])
    weight_2_function_value = Setting([""])

    weight_3 = Setting([0])
    weight_3_fixed = Setting([1])
    weight_3_has_min = Setting([0])
    weight_3_min = Setting([0.0])
    weight_3_has_max = Setting([0])
    weight_3_max = Setting([0.0])
    weight_3_function = Setting([0])
    weight_3_function_value = Setting([""])

    weight_4 = Setting([0])
    weight_4_fixed = Setting([1])
    weight_4_has_min = Setting([0])
    weight_4_min = Setting([0.0])
    weight_4_has_max = Setting([0])
    weight_4_max = Setting([0.0])
    weight_4_function = Setting([0])
    weight_4_function_value = Setting([""])

    weight_5 = Setting([0])
    weight_5_fixed = Setting([1])
    weight_5_has_min = Setting([0])
    weight_5_min = Setting([0.0])
    weight_5_has_max = Setting([0])
    weight_5_max = Setting([0.0])
    weight_5_function = Setting([0])
    weight_5_function_value = Setting([""])

    def __init__(self):
        super().__init__()

    def get_parameter_name(self):
        return "Radiation"

    def get_current_dimension(self):
        return len(self.is_multiple_wavelength)

    def get_parameter_box_instance(self, parameter_tab, index):
        return RadiationBox(widget=self,
                            parent=parameter_tab,
                            index = index,
                            is_multiple_wavelength      = self.is_multiple_wavelength[index],
                            wavelength                  = self.wavelength[index],
                            wavelength_fixed            = self.wavelength_fixed[index],
                            wavelength_has_min          = self.wavelength_has_min[index],
                            wavelength_min              = self.wavelength_min[index],
                            wavelength_has_max          = self.wavelength_has_max[index],
                            wavelength_max              = self.wavelength_max[index],
                            wavelength_function         = self.wavelength_function[index],
                            wavelength_function_value   = self.wavelength_function_value[index],
                            xray_tube_key               = self.xray_tube_key[index],
                            wavelength_2                = self.wavelength_2[index],
                            wavelength_2_fixed          = self.wavelength_2_fixed[index],
                            wavelength_2_has_min        = self.wavelength_2_has_min[index],
                            wavelength_2_min            = self.wavelength_2_min[index],
                            wavelength_2_has_max        = self.wavelength_2_has_max[index],
                            wavelength_2_max            = self.wavelength_2_max[index],
                            wavelength_2_function       = self.wavelength_2_function[index],
                            wavelength_2_function_value = self.wavelength_2_function_value[index],
                            wavelength_3                = self.wavelength_3[index],
                            wavelength_3_fixed          = self.wavelength_3_fixed[index],
                            wavelength_3_has_min        = self.wavelength_3_has_min[index],
                            wavelength_3_min            = self.wavelength_3_min[index],
                            wavelength_3_has_max        = self.wavelength_3_has_max[index],
                            wavelength_3_max            = self.wavelength_3_max[index],
                            wavelength_3_function       = self.wavelength_3_function[index],
                            wavelength_3_function_value = self.wavelength_3_function_value[index],
                            wavelength_4                = self.wavelength_4[index],
                            wavelength_4_fixed          = self.wavelength_4_fixed[index],
                            wavelength_4_has_min        = self.wavelength_4_has_min[index],
                            wavelength_4_min            = self.wavelength_4_min[index],
                            wavelength_4_has_max        = self.wavelength_4_has_max[index],
                            wavelength_4_max            = self.wavelength_4_max[index],
                            wavelength_4_function       = self.wavelength_4_function[index],
                            wavelength_4_function_value = self.wavelength_4_function_value[index],
                            wavelength_5                = self.wavelength_5[index],
                            wavelength_5_fixed          = self.wavelength_5_fixed[index],
                            wavelength_5_has_min        = self.wavelength_5_has_min[index],
                            wavelength_5_min            = self.wavelength_5_min[index],
                            wavelength_5_has_max        = self.wavelength_5_has_max[index],
                            wavelength_5_max            = self.wavelength_5_max[index],
                            wavelength_5_function       = self.wavelength_5_function[index],
                            wavelength_5_function_value = self.wavelength_5_function_value[index],
                            weight_2                    = self.weight_2[index],
                            weight_2_fixed              = self.weight_2_fixed[index],
                            weight_2_has_min            = self.weight_2_has_min[index],
                            weight_2_min                = self.weight_2_min[index],
                            weight_2_has_max            = self.weight_2_has_max[index],
                            weight_2_max                = self.weight_2_max[index],
                            weight_2_function           = self.weight_2_function[index],
                            weight_2_function_value     = self.weight_2_function_value[index],
                            weight_3                    = self.weight_3[index],
                            weight_3_fixed              = self.weight_3_fixed[index],
                            weight_3_has_min            = self.weight_3_has_min[index],
                            weight_3_min                = self.weight_3_min[index],
                            weight_3_has_max            = self.weight_3_has_max[index],
                            weight_3_max                = self.weight_3_max[index],
                            weight_3_function           = self.weight_3_function[index],
                            weight_3_function_value     = self.weight_3_function_value[index],
                            weight_4                    = self.weight_4[index],
                            weight_4_fixed              = self.weight_4_fixed[index],
                            weight_4_has_min            = self.weight_4_has_min[index],
                            weight_4_min                = self.weight_4_min[index],
                            weight_4_has_max            = self.weight_4_has_max[index],
                            weight_4_max                = self.weight_4_max[index],
                            weight_4_function           = self.weight_4_function[index],
                            weight_4_function_value     = self.weight_4_function_value[index],
                            weight_5                    = self.weight_5[index],
                            weight_5_fixed              = self.weight_5_fixed[index],
                            weight_5_has_min            = self.weight_5_has_min[index],
                            weight_5_min                = self.weight_5_min[index],
                            weight_5_has_max            = self.weight_5_has_max[index],
                            weight_5_max                = self.weight_5_max[index],
                            weight_5_function           = self.weight_5_function[index],
                            weight_5_function_value     = self.weight_5_function_value[index])

    def get_empty_parameter_box_instance(self, parameter_tab, index):
        return RadiationBox(widget=self, parent=parameter_tab, index=index)

    def set_parameter_data(self):
        incident_radiations = []
    
        if self.use_single_parameter_set == 1:
            incident_radiation = self.get_parameter_box(0).get_incident_radiation()
            incident_radiations.append(incident_radiation)
    
            for diffraction_pattern in self.fit_global_parameters.measured_dataset.diffraction_patterns:
                diffraction_pattern.apply_wavelength(incident_radiation.wavelength)
        else:
            for index in range(self.get_current_dimension()):
                incident_radiation = self.get_parameter_box(index).get_incident_radiation()
                incident_radiations.append(incident_radiation)
    
                self.fit_global_parameters.measured_dataset.diffraction_patterns[index].apply_wavelength(incident_radiation.wavelength)
    
        self.fit_global_parameters.measured_dataset.incident_radiations = incident_radiations

    def get_parameter_array(self):
        return self.fit_global_parameters.measured_dataset.incident_radiations

    def get_parameter_item(self, diffraction_pattern_index):
        return self.fit_global_parameters.measured_dataset.incident_radiations[diffraction_pattern_index]

    ##############################
    # SINGLE FIELDS SIGNALS
    ##############################

    def dumpSettings(self):
        self.dump_is_multiple_wavelength()
        self.dump_wavelength()
        self.dump_xray_tube_key()
        self.dump_wavelength_2()
        self.dump_wavelength_3()
        self.dump_wavelength_4()
        self.dump_wavelength_5()
        self.dump_weight_2()
        self.dump_weight_3()
        self.dump_weight_4()
        self.dump_weight_5()

    def dump_is_multiple_wavelength(self): self.dump_variable("is_multiple_wavelength")
    def dump_xray_tube_key(self): self.dump_variable("xray_tube_key")
    def dump_wavelength(self): self.dump_parameter("wavelength")
    def dump_wavelength_2(self): self.dump_parameter("wavelength_2")
    def dump_wavelength_3(self): self.dump_parameter("wavelength_3")
    def dump_wavelength_4(self): self.dump_parameter("wavelength_4")
    def dump_wavelength_5(self): self.dump_parameter("wavelength_5")
    def dump_weight_2(self): self.dump_parameter("weight_2")
    def dump_weight_3(self): self.dump_parameter("weight_3")
    def dump_weight_4(self): self.dump_parameter("weight_4")
    def dump_weight_5(self): self.dump_parameter("weight_5")

class RadiationBox(ParameterBox):

    def __init__(self,
                 widget=None,
                 parent=None,
                 index = 0,
                 is_multiple_wavelength = 0,
                 wavelength = 0.0826,
                 wavelength_fixed = 0,
                 wavelength_has_min = 0,
                 wavelength_min = 0.0,
                 wavelength_has_max = 0,
                 wavelength_max = 0.0,
                 wavelength_function = 0,
                 wavelength_function_value = "",
                 xray_tube_key = "CuKa2",
                 wavelength_2 = 0,
                 wavelength_2_fixed = 1,
                 wavelength_2_has_min = 0,
                 wavelength_2_min = 0.0,
                 wavelength_2_has_max = 0,
                 wavelength_2_max = 0.0,
                 wavelength_2_function = 0,
                 wavelength_2_function_value = "",
                 wavelength_3 = 0,
                 wavelength_3_fixed = 1,
                 wavelength_3_has_min = 0,
                 wavelength_3_min = 0.0,
                 wavelength_3_has_max = 0,
                 wavelength_3_max = 0.0,
                 wavelength_3_function = 0,
                 wavelength_3_function_value = "",
                 wavelength_4 = 0,
                 wavelength_4_fixed = 1,
                 wavelength_4_has_min = 0,
                 wavelength_4_min = 0.0,
                 wavelength_4_has_max = 0,
                 wavelength_4_max = 0.0,
                 wavelength_4_function = 0,
                 wavelength_4_function_value = "",
                 wavelength_5 = 0,
                 wavelength_5_fixed = 1,
                 wavelength_5_has_min = 0,
                 wavelength_5_min = 0.0,
                 wavelength_5_has_max = 0,
                 wavelength_5_max = 0.0,
                 wavelength_5_function = 0,
                 wavelength_5_function_value = "",
                 weight_2 = 0,
                 weight_2_fixed = 1,
                 weight_2_has_min = 0,
                 weight_2_min = 0.0,
                 weight_2_has_max = 0,
                 weight_2_max = 0.0,
                 weight_2_function = 0,
                 weight_2_function_value = "",
                 weight_3 = 0,
                 weight_3_fixed = 1,
                 weight_3_has_min = 0,
                 weight_3_min = 0.0,
                 weight_3_has_max = 0,
                 weight_3_max = 0.0,
                 weight_3_function = 0,
                 weight_3_function_value = "",
                 weight_4 = 0,
                 weight_4_fixed = 1,
                 weight_4_has_min = 0,
                 weight_4_min = 0.0,
                 weight_4_has_max = 0,
                 weight_4_max = 0.0,
                 weight_4_function = 0,
                 weight_4_function_value = "",
                 weight_5 = 0,
                 weight_5_fixed = 1,
                 weight_5_has_min = 0,
                 weight_5_min = 0.0,
                 weight_5_has_max = 0,
                 weight_5_max = 0.0,
                 weight_5_function = 0,
                 weight_5_function_value = ""):
        super(RadiationBox, self).__init__(widget=widget,
                                           parent=parent,
                                           index=index,
                                           is_multiple_wavelength=is_multiple_wavelength,
                                           wavelength = wavelength,
                                           wavelength_fixed = wavelength_fixed,
                                           wavelength_has_min = wavelength_has_min,
                                           wavelength_min = wavelength_min,
                                           wavelength_has_max = wavelength_has_max,
                                           wavelength_max = wavelength_max,
                                           wavelength_function = wavelength_function,
                                           wavelength_function_value = wavelength_function_value,
                                           xray_tube_key = xray_tube_key,
                                           wavelength_2 = wavelength_2,
                                           wavelength_2_fixed = wavelength_2_fixed,
                                           wavelength_2_has_min = wavelength_2_has_min,
                                           wavelength_2_min = wavelength_2_min,
                                           wavelength_2_has_max = wavelength_2_has_max,
                                           wavelength_2_max = wavelength_2_max,
                                           wavelength_2_function = wavelength_2_function,
                                           wavelength_2_function_value = wavelength_2_function_value,
                                           wavelength_3 = wavelength_3,
                                           wavelength_3_fixed = wavelength_3_fixed,
                                           wavelength_3_has_min = wavelength_3_has_min,
                                           wavelength_3_min = wavelength_3_min,
                                           wavelength_3_has_max = wavelength_3_has_max,
                                           wavelength_3_max = wavelength_3_max,
                                           wavelength_3_function = wavelength_3_function,
                                           wavelength_3_function_value = wavelength_3_function_value,
                                           wavelength_4 = wavelength_4,
                                           wavelength_4_fixed = wavelength_4_fixed,
                                           wavelength_4_has_min = wavelength_4_has_min,
                                           wavelength_4_min = wavelength_4_min,
                                           wavelength_4_has_max = wavelength_4_has_max,
                                           wavelength_4_max = wavelength_4_max,
                                           wavelength_4_function = wavelength_4_function,
                                           wavelength_4_function_value = wavelength_4_function_value,
                                           wavelength_5 = wavelength_5,
                                           wavelength_5_fixed = wavelength_5_fixed,
                                           wavelength_5_has_min = wavelength_5_has_min,
                                           wavelength_5_min = wavelength_5_min,
                                           wavelength_5_has_max = wavelength_5_has_max,
                                           wavelength_5_max = wavelength_5_max,
                                           wavelength_5_function = wavelength_5_function,
                                           wavelength_5_function_value = wavelength_5_function_value,
                                           weight_2 = weight_2,
                                           weight_2_fixed = weight_2_fixed,
                                           weight_2_has_min = weight_2_has_min,
                                           weight_2_min = weight_2_min,
                                           weight_2_has_max = weight_2_has_max,
                                           weight_2_max = weight_2_max,
                                           weight_2_function = weight_2_function,
                                           weight_2_function_value = weight_2_function_value,
                                           weight_3 = weight_3,
                                           weight_3_fixed = weight_3_fixed,
                                           weight_3_has_min = weight_3_has_min,
                                           weight_3_min = weight_3_min,
                                           weight_3_has_max = weight_3_has_max,
                                           weight_3_max = weight_3_max,
                                           weight_3_function = weight_3_function,
                                           weight_3_function_value = weight_3_function_value,
                                           weight_4 = weight_4,
                                           weight_4_fixed = weight_4_fixed,
                                           weight_4_has_min = weight_4_has_min,
                                           weight_4_min = weight_4_min,
                                           weight_4_has_max = weight_4_has_max,
                                           weight_4_max = weight_4_max,
                                           weight_4_function = weight_4_function,
                                           weight_4_function_value = weight_4_function_value,
                                           weight_5 = weight_5,
                                           weight_5_fixed = weight_5_fixed,
                                           weight_5_has_min = weight_5_has_min,
                                           weight_5_min = weight_5_min,
                                           weight_5_has_max = weight_5_has_max,
                                           weight_5_max = weight_5_max,
                                           weight_5_function = weight_5_function,
                                           weight_5_function_value = weight_5_function_value)

    def init_fields(self, **kwargs):
        self.is_multiple_wavelength      = kwargs["is_multiple_wavelength"]
        self.wavelength                  = kwargs["wavelength"]
        self.wavelength_fixed            = kwargs["wavelength_fixed"]
        self.wavelength_has_min          = kwargs["wavelength_has_min"]
        self.wavelength_min              = kwargs["wavelength_min"]
        self.wavelength_has_max          = kwargs["wavelength_has_max"]
        self.wavelength_max              = kwargs["wavelength_max"]
        self.wavelength_function         = kwargs["wavelength_function"]
        self.wavelength_function_value   = kwargs["wavelength_function_value"]
        self.xray_tube_key               = kwargs["xray_tube_key"]
        self.wavelength_2                = kwargs["wavelength_2"]
        self.wavelength_2_fixed          = kwargs["wavelength_2_fixed"]
        self.wavelength_2_has_min        = kwargs["wavelength_2_has_min"]
        self.wavelength_2_min            = kwargs["wavelength_2_min"]
        self.wavelength_2_has_max        = kwargs["wavelength_2_has_max"]
        self.wavelength_2_max            = kwargs["wavelength_2_max"]
        self.wavelength_2_function       = kwargs["wavelength_2_function"]
        self.wavelength_2_function_value = kwargs["wavelength_2_function_value"]
        self.wavelength_3                = kwargs["wavelength_3"]
        self.wavelength_3_fixed          = kwargs["wavelength_3_fixed"]
        self.wavelength_3_has_min        = kwargs["wavelength_3_has_min"]
        self.wavelength_3_min            = kwargs["wavelength_3_min"]
        self.wavelength_3_has_max        = kwargs["wavelength_3_has_max"]
        self.wavelength_3_max            = kwargs["wavelength_3_max"]
        self.wavelength_3_function       = kwargs["wavelength_3_function"]
        self.wavelength_3_function_value = kwargs["wavelength_3_function_value"]
        self.wavelength_4                = kwargs["wavelength_4"]
        self.wavelength_4_fixed          = kwargs["wavelength_4_fixed"]
        self.wavelength_4_has_min        = kwargs["wavelength_4_has_min"]
        self.wavelength_4_min            = kwargs["wavelength_4_min"]
        self.wavelength_4_has_max        = kwargs["wavelength_4_has_max"]
        self.wavelength_4_max            = kwargs["wavelength_4_max"]
        self.wavelength_4_function       = kwargs["wavelength_4_function"]
        self.wavelength_4_function_value = kwargs["wavelength_4_function_value"]
        self.wavelength_5                = kwargs["wavelength_5"]
        self.wavelength_5_fixed          = kwargs["wavelength_5_fixed"]
        self.wavelength_5_has_min        = kwargs["wavelength_5_has_min"]
        self.wavelength_5_min            = kwargs["wavelength_5_min"]
        self.wavelength_5_has_max        = kwargs["wavelength_5_has_max"]
        self.wavelength_5_max            = kwargs["wavelength_5_max"]
        self.wavelength_5_function       = kwargs["wavelength_5_function"]
        self.wavelength_5_function_value = kwargs["wavelength_5_function_value"]
        self.weight_2                    = kwargs["weight_2"]
        self.weight_2_fixed              = kwargs["weight_2_fixed"]
        self.weight_2_has_min            = kwargs["weight_2_has_min"]
        self.weight_2_min                = kwargs["weight_2_min"]
        self.weight_2_has_max            = kwargs["weight_2_has_max"]
        self.weight_2_max                = kwargs["weight_2_max"]
        self.weight_2_function           = kwargs["weight_2_function"]
        self.weight_2_function_value     = kwargs["weight_2_function_value"]
        self.weight_3                    = kwargs["weight_3"]
        self.weight_3_fixed              = kwargs["weight_3_fixed"]
        self.weight_3_has_min            = kwargs["weight_3_has_min"]
        self.weight_3_min                = kwargs["weight_3_min"]
        self.weight_3_has_max            = kwargs["weight_3_has_max"]
        self.weight_3_max                = kwargs["weight_3_max"]
        self.weight_3_function           = kwargs["weight_3_function"]
        self.weight_3_function_value     = kwargs["weight_3_function_value"]
        self.weight_4                    = kwargs["weight_4"]
        self.weight_4_fixed              = kwargs["weight_4_fixed"]
        self.weight_4_has_min            = kwargs["weight_4_has_min"]
        self.weight_4_min                = kwargs["weight_4_min"]
        self.weight_4_has_max            = kwargs["weight_4_has_max"]
        self.weight_4_max                = kwargs["weight_4_max"]
        self.weight_4_function           = kwargs["weight_4_function"]
        self.weight_4_function_value     = kwargs["weight_4_function_value"]
        self.weight_5                    = kwargs["weight_5"]
        self.weight_5_fixed              = kwargs["weight_5_fixed"]
        self.weight_5_has_min            = kwargs["weight_5_has_min"]
        self.weight_5_min                = kwargs["weight_5_min"]
        self.weight_5_has_max            = kwargs["weight_5_has_max"]
        self.weight_5_max                = kwargs["weight_5_max"]
        self.weight_5_function           = kwargs["weight_5_function"]
        self.weight_5_function_value     = kwargs["weight_5_function_value"]

    def init_gui(self, container):
        box = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH-5, spacing=0)

        orangegui.comboBox(box, self, "is_multiple_wavelength", label="Incident Radiation", items=["Single Wavelenght", "X-ray Tube"], orientation="horizontal", callback=self.set_is_multiple_wavelength)

        self.secondary_box = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH-5, spacing=0)

        orangegui.comboBox(self.secondary_box, self, "xray_tube_key", label="X-ray Tube Dataset", items=self.get_xray_tube_keys(),
                           sendSelectedValue=True, orientation="horizontal", callback=self.set_xray_tube_key)

        self.secondary_box_empty = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH-5, spacing=0)

        OWGenericWidget.create_box_in_widget(self, container,  "wavelength", label="\u03BB  [nm]", disable_function=True, add_callback=True, min_value=0.0, min_accepted=False, trim=25)

        self.secondary_box_2 = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH)
        self.secondary_box_2_empty = gui.widgetBox(container, "", orientation="vertical", width=self.CONTROL_AREA_WIDTH)

        self.create_wavelength_boxes()

        self.set_is_multiple_wavelength()

    def get_xray_tube_keys(self):
        items = []

        for key in wavelengths_data.keys():
            items.append(key)

        return items

    def create_wavelength_boxes(self):
        self.secondary_wavelengths_boxes = {}

        for key in wavelengths_data.keys():
            self.secondary_wavelengths_boxes[key] = gui.widgetBox(self.secondary_box_2, key + " Secondary Wavelengths", orientation="vertical", width=self.CONTROL_AREA_WIDTH - 5, height=240)

            secondary_index = 2
            for wavelenght in wavelengths_data[key]:
                if not wavelenght.is_principal:
                    var_wl = "wavelength_" + str(secondary_index)
                    var_we = "weight_" + str(secondary_index)
                    label_wl = "\u03BB" + " " + str(secondary_index) + "  [nm]"
                    label_we = "weight " + str(secondary_index)

                    OWGenericWidget.create_box_in_widget(self, self.secondary_wavelengths_boxes[key],  var_wl, label=label_wl, label_width=50, add_callback=True, min_value=0.0, min_accepted=False, trim=25)
                    OWGenericWidget.create_box_in_widget(self, self.secondary_wavelengths_boxes[key],  var_we, label=label_we, label_width=50, add_callback=True, min_value=0.0, min_accepted=True, trim=25)

                    secondary_index += 1

            self.secondary_wavelengths_boxes[key].setVisible(False)

    def set_xray_tube_key(self):
        if not self.is_on_init and self.xray_tube_key in wavelengths_data.keys():
            secondary_index = 2
            for wavelength in wavelengths_data[self.xray_tube_key]:
                if not wavelength.is_principal:
                    var_wl = "wavelength_" + str(secondary_index)
                    var_we = "weight_" + str(secondary_index)

                    OWGenericWidget.populate_fields_in_widget(self, var_wl, FitParameter(value=wavelength.wavelength, fixed=True), value_only=False)
                    OWGenericWidget.populate_fields_in_widget(self, var_we, FitParameter(value=wavelength.weight, fixed=True), value_only=False)

                    secondary_index += 1
                else:
                    OWGenericWidget.populate_fields_in_widget(self, "wavelength", FitParameter(value=wavelength.wavelength, fixed=True), value_only=False)

        for key in self.secondary_wavelengths_boxes.keys():
            if key==self.xray_tube_key:
                self.secondary_box_2.layout().removeWidget(self.secondary_wavelengths_boxes[key])
                self.secondary_box_2.layout().insertWidget(0, self.secondary_wavelengths_boxes[key])
                self.secondary_wavelengths_boxes[key].setVisible(True)
            else:
                self.secondary_wavelengths_boxes[key].setVisible(False)

        if not self.is_on_init:
            self.widget.dump_xray_tube_key()
            self.widget.dump_wavelength_2()
            self.widget.dump_wavelength_3()
            self.widget.dump_wavelength_4()
            self.widget.dump_wavelength_5()
            self.widget.dump_weight_2()
            self.widget.dump_weight_3()
            self.widget.dump_weight_4()
            self.widget.dump_weight_5()

    def set_is_multiple_wavelength(self, switch_tube=True):
        if self.is_multiple_wavelength == 0:
            self.secondary_box.setVisible(False)
            self.secondary_box_2.setVisible(False)
            self.secondary_box_empty.setVisible(True)
            self.secondary_box_2_empty.setVisible(True)
            OWGenericWidget.populate_fields_in_widget(self, "wavelength_2", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "weight_2", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "wavelength_3", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "weight_3", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "wavelength_4", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "weight_4", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "wavelength_5", FitParameter(value=0.0, fixed=True), value_only=False)
            OWGenericWidget.populate_fields_in_widget(self, "weight_5", FitParameter(value=0.0, fixed=True), value_only=False)
        else:
            self.secondary_box.setVisible(True)
            self.secondary_box_empty.setVisible(False)
            self.secondary_box_2.setVisible(True)
            self.secondary_box_2_empty.setVisible(False)

            if switch_tube: self.set_xray_tube_key()

        if not self.is_on_init:
            self.widget.dump_is_multiple_wavelength()
            self.widget.dump_xray_tube_key()
            self.widget.dump_wavelength_2()
            self.widget.dump_wavelength_3()
            self.widget.dump_wavelength_4()
            self.widget.dump_wavelength_5()
            self.widget.dump_weight_2()
            self.widget.dump_weight_3()
            self.widget.dump_weight_4()
            self.widget.dump_weight_5()

    def callback_wavelength(self):
        if not self.is_on_init: self.widget.dump_wavelength()
        
    def callback_wavelength_2(self):
        if not self.is_on_init: self.widget.dump_wavelength_2()
        
    def callback_wavelength_3(self):
        if not self.is_on_init: self.widget.dump_wavelength_3()
        
    def callback_wavelength_4(self):
        if not self.is_on_init: self.widget.dump_wavelength_4()
        
    def callback_wavelength_5(self):
        if not self.is_on_init: self.widget.dump_wavelength_5()
        
    def callback_weight_2(self):
        if not self.is_on_init: self.widget.dump_weight_2()
        
    def callback_weight_3(self):
        if not self.is_on_init: self.widget.dump_weight_3()
        
    def callback_weight_4(self):
        if not self.is_on_init: self.widget.dump_weight_4()
        
    def callback_weight_5(self):
        if not self.is_on_init: self.widget.dump_weight_5()

    def set_data(self, incident_radiation):
        if (self.is_multiple_wavelength==0 and not incident_radiation.is_single_wavelength) or \
           (self.is_multiple_wavelength==1 and incident_radiation.is_single_wavelength):
            raise ValueError("Incident Radiation is incompatible with previous setup: multiple/single wavelength")

        if not incident_radiation.is_single_wavelength:
            if self.xray_tube_key != incident_radiation.xray_tube_key:
                raise ValueError("Incident Radiation is incompatible with previous setup: different xray-tube")

        # ---------------------------------------

        OWGenericWidget.populate_fields_in_widget(self, "wavelength", incident_radiation.wavelength, value_only=True)
        self.is_multiple_wavelength = 0 if incident_radiation.is_single_wavelength else 1

        if not incident_radiation.is_single_wavelength:
            self.xray_tube_key=incident_radiation.xray_tube_key

            for index in range(0, len(incident_radiation.secondary_wavelengths)):
                OWGenericWidget.populate_fields_in_widget(self, "wavelength_" + str(2 + index), incident_radiation.secondary_wavelengths[index]        , value_only=True)
                OWGenericWidget.populate_fields_in_widget(self, "weight_" + str(2 + index)    , incident_radiation.secondary_wavelengths_weights[index], value_only=True)

        self.set_is_multiple_wavelength(switch_tube=False)

    def get_basic_parameter_prefix(self):
        return IncidentRadiation.get_parameters_prefix()

    def get_incident_radiation(self):
        incident_radiation = IncidentRadiation(wavelength=OWGenericWidget.populate_parameter_in_widget(self, "wavelength", self.get_parameters_prefix()))

        if self.is_multiple_wavelength == 1:
            secondary_wavelengths = []
            secondary_wavelengths_weights = []

            for index in range(0, 4):
                var_wl = "wavelength_" + str(2 + index)
                var_we = "weight_" + str(2 + index)

                secondary_wavelength        = OWGenericWidget.populate_parameter_in_widget(self, var_wl, self.get_parameters_prefix())
                secondary_wavelength_weight = OWGenericWidget.populate_parameter_in_widget(self, var_we, self.get_parameters_prefix())

                if secondary_wavelength.value > 0.0:
                    secondary_wavelengths.append(secondary_wavelength)
                    secondary_wavelengths_weights.append(secondary_wavelength_weight)

            incident_radiation.set_multiple_wavelengths(self.xray_tube_key, secondary_wavelengths, secondary_wavelengths_weights, recalculate=True)

        return incident_radiation

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWRadiation()
    ow.show()
    a.exec_()
    ow.saveSettings()
