# standard library
import os
from dataclasses import dataclass, make_dataclass, asdict, field
import sys
import logging.config
# third-party site-packages
import pandas as pd
import numpy as np

from aiolos_commissioning_tools import __version__
import aiolos_fluid_dynamics
from aiolos_fluid_dynamics.physical_constants import  GAMMA

log = logging.getLogger(__name__)

# tunnel condition filetypes
RUNLOG = 0
FCS = 1
EXCEL = 2


@dataclass
class TunnelData:
    """
    data structure to hold fcs data loaded in from an excel file
    """
    run_id: int
    parameters: dict
    file_type: int = field(repr=False)  # do not show when strut is printed
    file_name: str = field(repr=False)  # do not show when strut is printed


def load_tunnel_data(data_file, file_type=RUNLOG, sheet_name=0, run_id=0, return_params={}):
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
    :param file_type:       <int> RUNLOG (i.e. excel) == 0, FCS (i.e. csv) == 1
    :param run_id:          <int> run number - useful if data are loaded for many runs in parallel
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
    elif file_type == EXCEL:
        try:
            data = pd.read_excel(data_file, sheet_name=sheet_name)
            data.dropna()
            
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

# ==================================================================================================================================================================================================== #
# PITOT-STATIC PROBE 
# ==================================================================================================================================================================================================== #
    
    """
    memo from H. Brocklehurst to D. Van Every (1991)

        the pitot-static probe will record a pressure difference of:

            DeltaP = 1/2 * C * rho * v**2

        where C is the non-dimensional correction of the pitot-static tube and departs from unity according to the degree of imperfection
        of the tube and to the conditions of it's use.

    the pitot-static probe correction is used to correct the static pressure measured by the probe.

        Pt - Ps  = 1 / C * ( p-pitot - p-static )
        Ps - ref = p-static + ( C - 1 ) * ( p-pitot - p-static )

    where ref is the reference pressure used in the measurement ()

    the functions in this section favour using the pitot-static probe pressure difference directly, rather than calculated test section conditions. This
    is done to minimize floating point errors when adding large reference pressures in kPa to small differential pressures in Pa. 

    """

@np.vectorize
def dynamic_pressure_from_pitot(pitot_port_pressure, static_port_pressure, reference_absolute_pressure, probe_correction):
    """

    :param pitot_port_pressure:         <float64 or np.ndarray<float64>> pitot port pressure relative to some reference          [Pa]
    :param static_port_pressure:        <float64 or np.ndarray<float64>> static port pressure relative to the same reference     [Pa]
    :param probe_correction:            <float64> pitot-static probe correction factor, c                                        []
    :param reference_absolute_pressure: <float64 or np.ndarray<float64>> asbolute (barometric) pressure at that reference point  [Pa]
    :return:
            dynamic_pressure_from_pitot <same type as input> Mach number                                                         [Pa]

    """
    delta_p_probe = pitot_port_pressure - static_port_pressure
    static_pressure = reference_absolute_pressure + static_port_pressure + ( probe_correction  - 1.0 ) * ( delta_p_probe )

    return GAMMA / (GAMMA-1.0) * static_pressure * ( ( (1.0/probe_correction)*(delta_p_probe/static_pressure) + 1.0 )**( (GAMMA-1.0)/GAMMA ) - 1.0)


@np.vectorize
def mach_number_from_pitot(pitot_port_pressure, static_port_pressure, reference_absolute_pressure, probe_correction):
    """

    :param pitot_port_pressure:         <float64 or np.ndarray<float64>> pitot port pressure relative to some reference          [Pa]
    :param static_port_pressure:        <float64 or np.ndarray<float64>> static port pressure relative to the same reference     [Pa]
    :param probe_correction:            <float64> pitot-static probe correction factor, c                                        []
    :param reference_absolute_pressure: <float64 or np.ndarray<float64>> asbolute (barometric) pressure at that reference point  [Pa]
    :return:
            mach_number_from_pitot      <same type as input> Mach number                                                         []

    """
    delta_p_probe = pitot_port_pressure - static_port_pressure
    static_pressure = reference_absolute_pressure + static_port_pressure + (probe_correction - 1.0 ) * ( delta_p_probe )

    return  2 / (GAMMA-1.0) * ( ( (1.0/probe_correction)*(delta_p_probe/static_pressure) + 1.0 )**( (GAMMA-1.0)/GAMMA ) - 1.0)


@np.vectorize
def wind_speed_from_pitot(pitot_port_pressure, static_port_pressure, reference_absolute_pressure, probe_correction, total_temperature, dew_point):
    """

    :param pitot_port_pressure:         <float64 or np.ndarray<float64>> pitot port pressure relative to some reference          [Pa]
    :param static_port_pressure:        <float64 or np.ndarray<float64>> static port pressure relative to the same reference     [Pa]
    :param probe_correction:            <float64> pitot-static probe correction factor, c                                        []
    :param reference_absolute_pressure: <float64 or np.ndarray<float64>> asbolute (barometric) pressure at that reference point  [Pa]
    :param total_temperature:           <float64 or np.ndarray<float64>> reference total temperature                             [K]
    :param dew_point:                   <float64 or np.ndarray<float64>> reference dew-point temperature                         [K]
    :return:
            wind_speed_from_pitot       <same type as input> wind speed                                                          [m/s]

    """

    delta_p_probe   = pitot_port_pressure - static_port_pressure
    static_pressure = reference_absolute_pressure + static_port_pressure + (probe_correction - 1.0 ) * delta_p_probe

    dynamic_pressure    = dynamic_pressure_from_pitot(pitot_port_pressure=pitot_port_pressure, static_port_pressure=static_port_pressure, reference_absolute_pressure=reference_absolute_pressure, probe_correction=probe_correction)
    mach_number         = mach_number_from_pitot(pitot_port_pressure=pitot_port_pressure, static_port_pressure=static_port_pressure, reference_absolute_pressure=reference_absolute_pressure, probe_correction=probe_correction)
    
    static_temperature  = aiolos_fluid_dynamics.fluid_dynamics_relationships.static_temperature(To=total_temperature, M=mach_number)
    vapour_pressure     = aiolos_fluid_dynamics.fluid_dynamics_relationships.water_vapour_pressure(dew_point_temperature=dew_point, dry_bulb_temperature=static_temperature)
    density             = aiolos_fluid_dynamics.fluid_dynamics_relationships.density_air_water_vapour(p=static_pressure, p_h2o=vapour_pressure, T=static_temperature)
   
    return np.sqrt(2*dynamic_pressure/density)   # m/s


@np.vectorize
def rayleigh_pitot_correction(Po2, p, tolerance, MAXIT=1000):
    
    pass
    
    M = fluids.Mach_number(Po=Po2, p=p)
    return Po1, M
    

# ==================================================================================================================================================================================================== #
# AIOLOS WIND SPEED ALGORITHM  
# ==================================================================================================================================================================================================== #


@np.vectorize
def wind_speed_alogorithm(dp, absolute_pressure, total_temperature, dew_point, fkp, fkq):
    """
    this function takes in the Pitot and static pressures from a Pitot probe, as well as the thermodynamic properties
    and returns the wind speed in m/s

    :param dp:                  <float64 or np.ndarray<float64>> pitot port pressure relative to some reference          [Pa]
    :param absolute_pressure:   <float64 or np.ndarray<float64>> asbolute (barometric) pressure at that reference point  [Pa]
    :param total_temperature:   <float64 or np.ndarray<float64>> reference total temperature                             [K]
    :param dew_point:           <float64 or np.ndarray<float64>> reference dew-point temperature                         [K]
    :param fkp:                  <function> wind speed coefficient function fkp = kp(dp[Pa])  
    :param fkp:                  <function> wind speed coefficient function fkp = kp(dp[Pa])  
    :return:
        wind_speed_alogorithm   <same type as input> wind speed                                                          [m/s]

    """

    # use the wind tunnel calibration to determine the test section static pressure 
    static_pressure = fkp(dp)*dp + absolute_pressure

    # calculate the Mach number and dynamic pressure from the calibration functions 
    mach_number         = mach_number_from_ws_calibration(dp=dp, fkp=fkp, fkq=fkq, absolute_pressure=absolute_pressure)
    dynamic_pressure    = dynamic_pressure_from_ws_calibration(dp=dp, fkp=fkp, fkq=fkq, absolute_pressure=absolute_pressure)

    # calculate the density from the test section conditions
    static_temperature  = aiolos_fluid_dynamics.fluid_dynamics_relationships.static_temperature(To=total_temperature, M=mach_number)
    vapour_pressure     = aiolos_fluid_dynamics.fluid_dynamics_relationships.water_vapour_pressure(dew_point_temperature=dew_point, dry_bulb_temperature=static_temperature)
    density             = aiolos_fluid_dynamics.fluid_dynamics_relationships.density_air_water_vapour(p=static_pressure, p_h2o=vapour_pressure, T=static_temperature)

    return np.sqrt(2*dynamic_pressure/density)   # m/s


@np.vectorize
def wind_speed_alogorithm_with_density(dp, absolute_pressure, density, fkp, fkq):
    """
    this function takes in the Pitot and static pressures from a Pitot probe, as well as the thermodynamic properties
    and returns the wind speed in m/s

    :param dp:                  <float64 or np.ndarray<float64>> pitot port pressure relative to some reference          [Pa]
    :param absolute_pressure:   <float64 or np.ndarray<float64>> asbolute (barometric) pressure at that reference point  [Pa]
    :param total_temperature:   <float64 or np.ndarray<float64>> reference total temperature                             [K]
    :param dew_point:           <float64 or np.ndarray<float64>> reference dew-point temperature                         [K]
    :param fkp:                  <function> wind speed coefficient function fkp = kp(dp[Pa])  
    :param fkp:                  <function> wind speed coefficient function fkp = kp(dp[Pa])  
    :return:
        wind_speed_alogorithm   <same type as input> wind speed                                                          [m/s]

    """

    # use the wind tunnel calibration to determine the test section static pressure 
    static_pressure = fkp(dp)*dp + absolute_pressure

    # calculate the Mach number and dynamic pressure from the calibration functions
    mach_number         = mach_number_from_ws_calibration(dp=dp, fkp=fkp, fkq=fkq, absolute_pressure=absolute_pressure)
    dynamic_pressure    = dynamic_pressure_from_ws_calibration(dp=dp, fkp=fkp, fkq=fkq, absolute_pressure=absolute_pressure)
   
    return np.sqrt(2*dynamic_pressure/density)   # m/s


@np.vectorize
def mach_number_from_ws_calibration(dp, fkp, fkq, absolute_pressure):
    """
    returns the mach number based on the wind tunnel calibration
    :param dp:      <> contraction pressure drop (e.g. Pc1-Pc2 or Pc1-Pc3) in Pascals
    :param kp:      <function>
    :param kq:      <function>
    :param absolute_pressure: <> absolute pressure in Pascals
    :return:
        mach_number in the test section
    """
    return np.sqrt(2./(GAMMA-1.) * ((fkq(dp)*dp/(fkp(dp)*dp+absolute_pressure) + 1.)**((GAMMA-1)/GAMMA) - 1.))


def dynamic_pressure_from_ws_calibration(dp, fkp, fkq, absolute_pressure):

    return GAMMA/2. * ( absolute_pressure + fkp(dp)*dp ) * mach_number_from_ws_calibration(dp, fkp, fkq, absolute_pressure)**2

# ==================================================================================================================================================================================================== #
# WIND SPEED CALIBRATION COEFFICIENTS 
# ==================================================================================================================================================================================================== #

def generate_tunnel_calibration_coefficients(dp, kp, kq, deg_kp, deg_kq):
    """
        this function returns the polynomial coefficients ckp[:], ckq[:] for the wind speed calibration coefficient curve fits kp, kq = f(dp)
    """

    ckp = np.flip(np.polyfit(np.log(dp), kp, deg=deg_kp))        
    ckq = np.flip(np.polyfit(np.log(dp), kq, deg=deg_kq))

    log.debug("kp coefficients: " + (deg_kp+1)*"%.2e " % tuple(ckp[:]))
    log.debug("kq coefficients: " + (deg_kq+1)*"%.2e " % tuple(ckq[:]))    

    return ckp, ckq


def generate_tunnel_calibration_funcs(ckp, ckq):
    """
    this functions returns two functions for the wind speed calibration. The polynomial coefficients should be arranged according to
    increasing order. i.e. c0, c1, c2, ... which is the opposite the default numpy.polyfit output. 

        fkp(dp) = sum ( kp[i] * ln(dp)**i )
        fkq(dp) = sum ( kq[i] * ln(dp)**i )
    
    :param ckp:              <np.ndarray<np.float64>> static pressure coefficient curve fitting coefficients where kp = sum ( ckp[i]*ln(dp)**i) for i = 0 ... deg_kp
    :param ckq:              <np.ndarray<np.float64>> dynamic pressure coefficient curve fitting coefficients where kq = sum ( ckq[i]*ln(dp)**i) for i = 0 ... deg_kq
    
    """
    
    def fkp(dp):
        return np.sum(ckp[i]*np.log(dp)**i for i in range(len(ckp)))

    def fkq(dp):
        return np.sum(ckq[i]*np.log(dp)**i for i in range(len(ckq)))

    log.debug("generating wind speed calbration coefficient functions, kp(dp) and kq(dp)")

    return fkp, fkq


def generate_tunnel_calibration_funcs_from_coefficient_file(coef_file):
    """
    Called when the wind tunnel kp and kq = f(dp) curve fit coefficients are already known and in coef_file
    :param coef_file:
    :return:
    """
    try:
        ckp, ckq = np.loadtxt(coef_file, unpack=True, dtype=np.float64)
    
    except (ValueError, IOError, FileNotFoundError) as err:
        log.error(err)
        log.error('Cannont read %s' % os.path.basename(coef_file))
        raise
    
    log.debug("calibration file %s loaded successfully" % os.path.basename(coef_file))

    return generate_tunnel_calibration_funcs(ckp, ckq)


def generate_tunnel_calibration_funcs_from_data_file(data_file, deg_kp=5, deg_kq=5):
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
        dp, kp, kq = np.loadtxt(data_file, unpack=True, dtype=np.float64)

    except (ValueError, IOError, FileNotFoundError) as err:
        log.error(err)
        log.error('Cannont read %s' % os.path.basename(data_file))
        raise

    if not dp.size == kp.size and dp.size == kq.size:
        msg = "Array dimensions do not match: dp(%i), kp(%i), kq(%i)" % (dp.size, kp.size, kq.size)
        # log error message
        log.error(msg)
        # halt execution with Traceback
        raise ValueError(msg)

    log.debug("calibration file %s loaded successfully" % os.path.basename(data_file))
    
    # np.polyfit returns coefficient with highest order first
    ckp, ckq = generate_tunnel_calibration_coefficients(dp=dp, kp=kp, kq=kq, deg_kp=deg_kp, deg_kq=deg_kq)

    return generate_tunnel_calibration_funcs(ckp, ckq)


def write_tunnel_calibration_data_to_file(cal_file, dp, kp, kq):
    """
        writes calibration data to a file in column format. This file can be read by generate_tunnel_calibration_funs_from_data

    :param cal_file:        <filename> path to file to be written to 
    :param dp:              <np.ndarray<np.float64>> tunnel contraction pressure drop (i.e. Pc1 - Pc2 or Pc1 - Pc3) [Pa]
    :param kp:              <np.ndarray<np.float64>> static pressure coefficient cacluated from measurements kp = p - ref / dp
    :param kq:              <np.ndarray<np.float64>> dynamic pressure coefficient cacluated from measurements kq = pt - p / dp

    :return:
        None
    """
    try:
        np.savetxt(cal_file, np.transpose(np.array([dp, kp, kq])))
    except (ValueError, IOError, FileNotFoundError) as err:
        log.error(err)
        log.error('Cannont write %s' % os.path.basename(cal_file))
        raise

    log.debug("calibration data written to %s" % cal_file)
    return 


def write_tunnel_calibration_coefficients_to_file(coef_file, ckp, ckq):
    """
        writes calibration coefficients to a file in column format. This file can be read by generate_tunnel_calibration_funs_from_coefficients.

        the polynomial coefficients should be arranged according to increasing order. i.e. c0, c1, c2, ... which is the opposite the default numpy.polyfit output. 

        calibration coefficient curve fits take the form

                k = c0 + c1*ln(dp)**1 + c2*ln(dp)**2 + ...

    :param coef_file:        <filename> path to file to be written to 
    :param ckp:              <np.ndarray<np.float64>> static pressure coefficient curve fitting coefficients where kp = sum ( ckp[i]*ln(dp)**i) for i = 0 ... deg_kp
    :param ckq:              <np.ndarray<np.float64>> dynamic pressure coefficient curve fitting coefficients where kq = sum ( ckq[i]*ln(dp)**i) for i = 0 ... deg_kq
    
    :return:
        None
    """
    # need to pad both with zeros until they are the same size

    if len(ckp) > len(ckq): # ckp is of higher order - pad ckq
        for _ in range(len(ckp) - len(ckq)):
            ckq = np.append(ckq, 0.0)
    
    if len(ckq) > len(ckp): # ckq is of higher order - pad ckp
        for _ in range(len(ckq) - len(ckp)):
            ckp = np.append(ckp, 0.0)
    
    try:
        np.savetxt(coef_file, np.transpose(np.array([ckp, ckq])))
    except (ValueError, IOError, FileNotFoundError) as err:
        log.error(err)
        log.error('Cannont write %s' % os.path.basename(coef_file))
        raise
    
    log.debug("calibration coefficients written to %s" % coef_file)
    return


@np.vectorize
def kp_measured(pitot_port_pressure, static_port_pressure, probe_correction, delta_p_tunnel):

    # ps - ref
    relative_static_pressure = static_port_pressure + (probe_correction - 1.0) * ( pitot_port_pressure - static_port_pressure )

    return relative_static_pressure / delta_p_tunnel


@np.vectorize
def kq_measured(pitot_port_pressure, static_port_pressure, probe_correction, delta_p_tunnel):

    # pt - ps
    pseudo_dynamic_pressure = probe_correction * ( pitot_port_pressure - static_port_pressure )
    
    return pseudo_dynamic_pressure / delta_p_tunnel


# ==================================================================================================================================================================================================== #
# WIND SPEED CALIBRATION  
# ==================================================================================================================================================================================================== #

def wind_speed_calibration(dp, kp, kq, deg_kp, deg_kq, name):

    
    # fit kp and kq data vs np.log(dp)
    ckp, ckq = generate_tunnel_calibration_coefficients(dp=dp, kp=kp, kq=kq, deg_kp=deg_kp, deg_kq=deg_kq)
    fkp, fkq = generate_tunnel_calibration_funcs(ckp=ckp, ckq=ckq)
    r2kp = coefficient_of_determination(f=fkp, x=dp, y=kp)
    r2kq = coefficient_of_determination(f=fkq, x=dp, y=kq)

    log.debug("coefficient of regression for kp = f(dp) of order %i = %.4f" % (deg_kp, r2kp) )
    log.debug("coefficient of regression for kq = f(dp) of order %i = %.4f" % (deg_kq, r2kq) )
   
    # write calibration  data to file
    write_tunnel_calibration_data_to_file(cal_file="%s-calibration-data.dat" % name, dp=dp, kp=kp, kq=kq)
    # write calibration coefficients to fil
    write_tunnel_calibration_coefficients_to_file(coef_file="%s-calibration-coefficients.dat" % name, ckp=ckp, ckq=ckq)
    # return functions

    return fkp, fkq


def wind_speed_feed_forward(true_wind_speed, main_fan_speed_rpm, name):
    """
        this function fits a curve to the empty tunnel feed-forward relationship between wind speed
        and main fan rpm

    """

    wind_speed_kph = true_wind_speed / aiolos_fluid_dynamics.units.KPH
    # fit data
    cffw = np.polyfit(wind_speed_kph, main_fan_speed_rpm, deg=1)
    
    log.debug("wind speed feed-forward: fanspeed [rpm] = %.4f*ws[kph] + %.4f " % (cffw[0], cffw[1]))
    ffw = np.poly1d(cffw)
    
    r2ffw = coefficient_of_determination(f=ffw, x=wind_speed_kph, y=main_fan_speed_rpm)
    log.debug("coefficient of regression for rpm(ws [kph]) = %.4f" % r2ffw) 
   
    # output data
    np.savetxt("%s-feedforward-data.dat" % name, np.transpose(np.array([wind_speed_kph, main_fan_speed_rpm])))
    # output coefficients 
    np.savetxt("%s-feedforward-coefficients.dat" % name, np.transpose(cffw))

    return ffw


# ==================================================================================================================================================================================================== #
# WIND SPEED CALIBRATION PROCEDURE 
# ==================================================================================================================================================================================================== #

def coefficient_of_determination(f, x, y):
    """
        r-squared (i.e. coefficient of regression)

    :param f:       <function> the curve fited function of the data x, y
    :param x:       <np.array<np.float64>> array of independent curve fit data
    :param y:       <np.array<np.float64>> array of dependent curve fit data

    :return:
        R-squared   <np.float64> coefficient of determination for the curve fit function f
    """

    yhat = f(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum( (yhat - ybar)**2.0 )
    ssres = np.sum( (y - yhat)**2.0 )
    sstot = np.sum( (y - ybar)**2.0)

    return 1.0 - ssres/sstot