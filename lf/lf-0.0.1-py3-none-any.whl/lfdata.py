""" Provides the LFData class and data_loader function

LFData holds all data reported by the LF AWESOME receiver and includes several
preprocessing operations.
data_loader provides a quick way of converting the .mat files provided by the
LF AWESOME receiver to a python dictionary.
"""

from datetime import datetime
from scipy.io import loadmat


def data_loader(mat_file, variables=None):
    """ Properly format an LF AWESOME receiver's output mat file

    Parameters
    ----------
    mat_file : string
        File path to a specific .mat file
    variables : list of strings (optional)
        List of variables to be extracted from the .mat file

    Returns
    -------
    dict
        dictionary containing formatted LF Data

    See Also
    --------
    LFData : Data management class
    """
    data = loadmat(mat_file, mat_dtype=True, variable_names=variables)
    for key in data:
        if key in [
            "start_year",
            "start_month",
            "start_day",
            "start_hour",
            "start_minute",
            "start_second",
            "Fs",
            "adc_channel_number",
        ]:
            # Should be integers, but aren't by default
            data[key] = int(data[key][0][0])
        elif key in [
            "latitude",
            "longitude",
            "altitude",
            "gps_quality",
            "adc_sn",
            "adc_type",
            "antenna_bearings",
            "cal_factor",
            "computer_sn",
            "gps_sn",
            "station_description",
        ]:
            # Correct type, but in array
            data[key] = data[key][0][0]
        elif key in ["is_amp", "is_msk"]:
            # Should be boolean
            data[key] = bool(data[key][0][0])
        elif key in [
            "hardware_description",
            "station_name",
            "call_sign",
            "VERSION",
        ]:
            # Should be strings, but are in array of ascii
            data[key] = "".join(chr(char) for char in data[key])
    time_vals = [
        "start_year",
        "start_month",
        "start_day",
        "start_hour",
        "start_minute",
        "start_second",
    ]
    # If all of the time data is loaded, create a datetime object
    if (variables is None) or all(elem in variables for elem in time_vals):
        data["start_time"] = datetime(
            data.pop("start_year"),
            data.pop("start_month"),
            data.pop("start_day"),
            data.pop("start_hour"),
            data.pop("start_minute"),
            data.pop("start_second"),
        )

    return data
