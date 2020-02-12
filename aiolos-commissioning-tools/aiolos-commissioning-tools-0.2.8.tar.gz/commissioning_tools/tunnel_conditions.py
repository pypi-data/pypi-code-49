# standard library
import os
from dataclasses import dataclass, make_dataclass, asdict, field
import sys
import logging.config
# third-party site-packages
import pandas as pd
import numpy as np

from commissioning_tools import __version__

log = logging.getLogger(__name__)

# tunnel condition filetypes
RUNLOG = 0
FCS = 1


@dataclass
class TunnelData:
    """
    data structure to hold fcs data loaded in from an excel file
    """
    run_id: int
    parameters: dict
    file_type: int = field(repr=False)  # do not show when strut is printed
    file_name: str = field(repr=False)  # do not show when strut is printed


def load_tunnel_data(data_file, file_type=RUNLOG, run_id=0, return_params={}):
    """
    Since the wind tunnel parameter names are not known a priori, we need to specify the parameter names as the values
    in the dictionay 'return_params'. The keys associated with these values will be the attribute names in the results
    struct. These can be called by result.x where x is the key.

    eg.

    >> return_params = { 'temperature' : 'Pane1-AirTemperature', 'wind_speed' : 'Pane1-WindSpeedKph'}
    >> t = results.temperature
    >> u = results.wind_speed
    or if only the mean is desired
    >> mean_temperature = np.mean(results.temperature)

    results.temperature will return the temperature data stored in the Pane1-AirTemperature column of the FCS file.

    :param data_file:       <path> path to either fcs data file or runlog
    :param file_type:       <int> RUNLOG == 0, FCS == 1
    :param run_id:          <int>
    :param return_params:   <dict> key: value pairs where key = desired variable name and value = fsc variable name
    :return:
            result          <TunnelData> data struct which holds results
    """

    # create results struct with initial parameters for this run case
    result = TunnelData(run_id=run_id, file_type=file_type, file_name=data_file, parameters=return_params)

    # Todo add additional files types for FSC data logger, FCS
    if file_type == FCS:  # load data from fcs output - this typically comes from the trends app in the tunnel FCS
        try:
            data = pd.read_csv(data_file)
            # the FCS data recorders can include missing data so we drop rows if they include 'nan'
            data = data.dropna()
        except (ValueError, IOError, FileNotFoundError) as err:
            log.error(err)
            log.error('Cannont read %s' % os.path.basename(data_file))
            raise
    elif file_type == RUNLOG:
        try:
            data = pd.read_excel(data_file)
            # only read the row for this run
            data = data[data['RUN NO.'] == run_id]
        except (ValueError, IOError, FileNotFoundError) as err:
            log.error(err)
            log.error('Cannont read %s' % os.path.basename(data_file))
            raise

    data = data.reset_index(drop=True)

    # add fields to TunnelData class dynamically to suit the users need
    # each field is defined by the key in the return_params dictionary
    result.__class__ = make_dataclass(
        'TunnelData',
        fields=[(key, np.float64, field(default=data[return_params[key]].to_numpy(), repr=False)) for key in return_params],
        bases=(TunnelData,))

    log.debug("%i parameter(s) read in from file %s successfully" % (len(return_params), os.path.basename(data_file)))
    log.debug(len(return_params)*"%s, "% tuple(return_params))
    return result


def write_tunnel_calibration_data_to_file(coef_file):
    pass


def write_tunnel_calibration_coefs_to_file(cal_file):
    pass


def generate_tunnel_calibration_funcs_from_coefs(coef_file):  # todo add this as optional flag and have one function
    """
    Called when the wind tunnel kp and kq = f(dp) curve fit coefficients are already known and in coef_file
    :param coef_file:
    :return:
    """
    ckp, ckq = np.loadtxt(coef_file, unpack=True, dtype=np.float64)

    def kp(dp):
        return np.sum(ckp[i]*np.log(dp)**i for i in range(len(ckp)))

    def kq(dp):
        return np.sum(ckq[i]*np.log(dp)**i for i in range(len(ckq)))

    return kp, kq


def generate_tunnel_calibration_funcs_from_data(data_file, deg_kp=5, deg_kq=5):
    """
    call if the kp, kq data is stored in data_file and fit a polynomial of degree deg_kp or deg_kq

    :param data_file:   <str> path to file containing whitespace seperated column data of dp, kp, kp(dp), kq, kq(dp), group
    :param deg_kp:      <int> degree of polynomial fit for kp data
    :param deg_kq:      <int> degree of polynomial fit for kp data
    :return:
        kp, kq          <func> functions which take in a pressure diference in Pa and use the curve fit coefficientskp
                               to return the wind speed coefficients kp = kp(dp) and kq = kq(dp)
    """
    try:
        DP, kp, _, kq, _, grp = np.loadtxt(data_file, unpack=True, dtype=np.float64)
        grp = grp[np.where(grp != 0)]
    except (ValueError, IOError, FileNotFoundError) as err:
        log.error(err)
        log.error('Cannont read %s' % os.path.basename(data_file))
        raise

    if not DP.size == kp.size and DP.size == kq.size:
        msg = "Array dimensions do not match: DP(%i), kp(%i), kq(%i)" % (DP.size, kp.size, kq.size)
        # log error message
        log.error(msg)
        # halt execution with Traceback
        raise ValueError(msg)

    # np.polyfit returns coefficient with highest order first
    kp_coef = np.polyfit(np.log(DP), kp, deg_kp)
    kq_coef = np.polyfit(np.log(DP), kq, deg_kq)

    log.debug("calibration file %s loaded successfully" % os.path.basename(data_file))
    log.debug("kp coefficients: " + (deg_kp+1)*"%.2e " % tuple(kp_coef[-1::-1]))
    log.debug("kq coefficients: " + (deg_kq+1)*"%.2e " % tuple(kq_coef[-1::-1]))

    def func_kp(dp):
        return np.sum(kp_coef[i]*np.log(dp)**(deg_kp-i) for i in range(len(kp_coef)))

    def func_kq(dp):
        return np.sum(kq_coef[i]*np.log(dp)**(deg_kq-i) for i in range(len(kq_coef)))

    return func_kp, func_kq
