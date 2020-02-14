"""
MIT License

Copyright (c) 2020 Max Planck Institute of Molecular Physiology

Author: Luca Lusnig (luca.lusnig@mpi-dortmund.mpg.de)
Author: Thorsten Wagner (thorsten.wagner@mpi-dortmund.mpg.de)
Author: Markus Stabrin (markus.stabrin@mpi-dortmund.mpg.de)
Author: Fabian Schoenfeld (fabian.schoenfeld@mpi-dortmund.mpg.de)
Author: Tapu Shaikh (tapu.shaikh@mpi-dortmund.mpg.de)
Author: Adnan Ali (adnan.ali@mpi-dortmund.mpg.de)


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


"""
EXAMPLE CONFIGURATION FILE
{
    "path_to_file": "../example.tif",
	"mandatory_parameters": {
        "Sigma": 3.39,
        "Lower_Threshold": 0.34,
        "Upper_Threshold": 1.02,
        "Maximum_Line_Length": 0,
        "Minimum_Line_Length": 0,
        "Darkline": "LIGHT",
        "Overlap_resolution": "NONE"
    },

  	"optional_parameters": {
		"Line_width": 10.0,
        "High_contrast": 200,
        "Low_contrast": 80
	},

	"further_options": {
		"Correct_position": true,
		"Estimate_width": true,
        "doExtendLine": true,
		"Show_junction_points": true,
        "Show_IDs": false,
		"Display_results": true,
        "Preview": true,
        "Make_Binary": false,
        "save_on_disk": true
	}
}

"""
import logging
from json import load as json_load
from json import JSONDecodeError
from os import path
from math import sqrt,pi,exp
from ridge_detection.linesUtil import MODE_LIGHT,MODE_DARK
def load_json(config_path):
    """
    Check if the config file exist and has a valid json format
    :param config_path: path to the json config file
    :return: loaded json file
    """
    if path.isfile(config_path) is False:
        print("ERROR: file '"+config_path+"' not found!")
        logging.error("ERROR: file '" + config_path + "' not found!")
        exit(-1)
    try:
        with open(config_path) as json_file:
            return  json_load(json_file)
    except JSONDecodeError:
        print("\nYour configuration file seems to be corruped. Please check if it is valid.")
        logging.error("Your configuration file seems to be corruped. Please check if it is valid.")
        exit(-1)

class Params:
    """
    This class replaces the original class "Options.java".
    class containing the parameters got or estimated from the json config file.

    The lists of accepted parameters  are the following:
    mandatory_params= ["Sigma", "Lower_Threshold", "Upper_Threshold", "Darkline", "Overlap_resolution","Minmum_Line_Length","Maximum_Line_Length"]
    optional_params = ["Line_width", "High_contrast", "Low_contrast"]
    further_bool_options = ["Correct_position", "Estimate_width", "Show_junction_points", "Show_IDs",  "Display_results", "Add_to_Manager", "Preview"]

    The "Sigma", "Lower_Threshold" and "Upper_Threshold" mandatory's parameter can be estimated from the oprional_parameter,
    for more info see: https://imagej.net/Ridge_Detection#Mandatory_Parameters
    """
    _line_width = None
    _high_contrast = None
    _low_contrast = None

    _correct_position = False
    _estimate_width = False
    _show_junction_points = False
    _show_IDs = False
    _display_results = True
    _preview = False
    _doExtendLine = True
    _saveOnFile= True

    config_path_to_file = None
    _config = None
    _accepted_Overlap_resolution =["none","slope"]
    _accepted_Darkline = ["light", "dark"]
    _foundamental_params = ["Minimum_Line_Length", "Maximum_Line_Length", "Darkline", "Overlap_resolution"]

    def __init__(self, cfg):
        if isinstance(cfg, dict):
            self._config = cfg
            self.config_path_to_file = cfg["path_to_file"]
        else:
            self._config = load_json(cfg)
            self.config_path_to_file=self._config["path_to_file"]
        self._isValid()

        self._set_params()

    def _isValid(self):
        """
        Given the loaded json config file, it check if all the params are available. If not abort
        I inserted this function because we can estimate some mandatory params from the optional param
        :return: None
        """

        if "mandatory_parameters" not in self._config.keys():
            print("\nError: params 'mandatory_parameters' not found in the config file!")
            logging.error(" params 'mandatory_parameters' not found in the config file!")
            exit(-1)

        mandatory_k = self._config["mandatory_parameters"].keys()

        for foundamental_value in self._foundamental_params:
            if foundamental_value not in mandatory_k:
                print("\nError: param 'mandatory_parameters."+foundamental_value+"' not found in the config file!")
                logging.error(" param 'mandatory_parameters." + foundamental_value + "' not found in the config file!")
                exit(-1)


        if self._config["mandatory_parameters"]["Overlap_resolution"].lower() not in self._accepted_Overlap_resolution:
            print("\nError: param 'mandatory_parameters.Overlap_resolution' not valid. Has to be one of "+str(self._accepted_Overlap_resolution))
            logging.error(" param 'mandatory_parameters.Overlap_resolution' not valid. Has to be one of "+str(self._accepted_Overlap_resolution))
            exit(-1)

        if self._config["mandatory_parameters"]["Darkline"].lower() not in self._accepted_Darkline:
            print("\nError: param 'mandatory_parameters.Darkiline' not valid. Has to be one of " + str(self._accepted_Darkline))
            logging.error(" param 'mandatory_parameters.Darkiline' not valid. Has to be one of " + str(self._accepted_Darkline))
            exit(-1)

        if "optional_parameters" not in self._config.keys() and ("Sigma" not in mandatory_k or "Lower_Threshold" not in mandatory_k  or "Upper_Threshold" not in mandatory_k ):
            print("\nERROR: optional parameters are used to estimate the [Sigma, Lower_Threshold,Upper_Threshold] mandatory's parameter when they miss")
            logging.error("optional parameters are used to estimate the [Sigma, Lower_Threshold,Upper_Threshold] mandatory's parameter when they miss")
            exit(-1)

    def _get_mandatory_parameters(self):
        return {k:v for k,v in zip (self._config["mandatory_parameters"].keys(),self._config["mandatory_parameters"].values())}

    def _get_optional_parameters(self):
        return {k:v for k,v in zip (self._config["optional_parameters"].keys(),self._config["optional_parameters"].values())} if "optional_parameters" in self._config.keys() else None

    def _get_further_options(self):
        return {k:v for k,v in zip (self._config["further_options"].keys(),self._config["further_options"].values())} if "further_options" in self._config.keys() else None

    def __str__(self):
        """print the value used in the script the variables """
        output = "List of input params:\n"
        output += "\tLine_width = " + str(self._line_width) + "\n"
        output += "\tHigh_contrast = " + str(self._high_contrast) + "\n"
        output += "\tLow_contrast = " + str(self._low_contrast) + "\n"
        output += "\tSigma = " + str(self._sigma) + "\n"
        output += "\tLower_Threshold = " + str(self._lower_Threshold) + "\n"
        output += "\tUpper_Threshold = " + str(self._upper_Threshold) + "\n"
        output += "\tMaximum_Line_Length = " + str(self._maximum_Line_Length) + "\n"
        output += "\tMinimum_Line_Length = " + str(self._minimum_Line_Length) + "\n"
        output += "\tDarkline = " + str(self._darkline) + "\n"
        output += "\tOverlap_resolution = " + str(self._overlap_resolution) + "\n"
        output += "\tCorrect_position = " + str(self._correct_position) + "\n"
        output += "\tEstimate_width = " + str(self._estimate_width) + "\n"
        output += "\tShow_junction_points = " + str(self._show_junction_points) + "\n"
        output += "\tShow_IDs = " + str(self._show_IDs) + "\n"
        output += "\tDisplay_results = " + str(self._display_results) + "\n"
        output += "\tPreview = " + str(self._preview) + "\n"
        output += "\tdoExtendLine = " + str(self._doExtendLine) + "\n"
        output += "\tSaveOnfile = " + str(self._saveOnFile) + "\n"
        return output

    def _set_params(self):
        m = self._get_mandatory_parameters()
        f = self._get_further_options()
        o = self._get_optional_parameters()


        if isinstance(o,dict):
            if "Line_width" in o:
                self._line_width = o["Line_width"]
            if "High_contrast" in o:
                self._high_contrast = o["High_contrast"]
            if "Low_contrast" in o :
                self._low_contrast = o["Low_contrast"]

        if "Sigma" in m:
            self._sigma = m["Sigma"]
        else:
            self._sigma = 0.5 + (self._line_width/(2*sqrt(3)))
        val = pow(self._sigma,3)*sqrt(2*pi)

        if "Lower_Threshold" in m:
            self._lower_Threshold = m["Lower_Threshold"]
        else:
            ew = 0.17 * exp(- (pow(self._line_width / 2, 2) / pow(2 * self._sigma, 2)))
            self._lower_Threshold = ew*( (2 * self._low_contrast*(self._line_width / 2)) /val)
        if "Upper_Threshold" in m:
            self._upper_Threshold = m["Upper_Threshold"]
        else:
            ew = 0.17 * exp(- (pow(self._line_width / 2, 2) / pow(2 * self._sigma, 2)))
            self._upper_Threshold = ew * ((2 * self._high_contrast * (self._line_width / 2)) / val)

        self._maximum_Line_Length =  m["Maximum_Line_Length"]
        self._minimum_Line_Length = m["Minimum_Line_Length"]
        self._darkline = MODE_DARK if m["Darkline"].lower()=="dark" else MODE_LIGHT
        self._overlap_resolution = m["Overlap_resolution"].lower()

        if isinstance(f, dict):
            if "Correct_position" in f:
                self._correct_position = f["Correct_position"]
            if "Estimate_width" in f:
                self._estimate_width = f["Estimate_width"]
            if "Show_junction_points" in f:
                self._show_junction_points = f["Show_junction_points"]
            if "Show_IDs" in f:
                self._show_IDs = f["Show_IDs"]
            if "Display_results" in f:
                self._display_results = f["Display_results"]
            if "Preview" in f:
                self._preview = f["Preview"]
            if "save_on_disk" in f:
                self._saveOnFile = f["save_on_disk"]
            if "doExtendLine" in f:
                self._doExtendLine = f["doExtendLine"]


    def get_line_width(self):
        return self._line_width

    def get_high_contrast(self):
        return self._high_contrast

    def get_low_contrast(self):
        return self._low_contrast

    def get_correct_position(self):
        return self._correct_position

    def get_estimate_width(self):
        return self._estimate_width

    def get_show_junction_points(self):
        return self._show_junction_points

    def get_show_IDs (self):
        return self._show_IDs

    def get_display_results(self):
        return self._display_results

    def get_preview(self):
        return self._preview

    def get_saveOnFile(self):
        return self._saveOnFile

    def get_doExtendLine(self):
        return self._doExtendLine

    def get_sigma(self):
        return self._sigma

    def get_lower_Threshold(self):
        return self._lower_Threshold

    def get_upper_Threshold(self):
        return self._upper_Threshold

    def get_maximum_Line_Length(self):
        return self._maximum_Line_Length

    def get_minimum_Line_Length(self):
        return self._minimum_Line_Length

    def get_darkline(self):
        return self._darkline

    def get_overlap_resolution(self):
        return self._overlap_resolution
