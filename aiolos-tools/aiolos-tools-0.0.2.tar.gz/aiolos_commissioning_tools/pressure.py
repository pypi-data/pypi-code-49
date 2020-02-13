""" Module Pressure

    v0 :    c. sooriyakumaran 2019

This module is used to load pressure data from the different types of Scanivalve pressure scanners. It contains
functions to compute different pressure coefficients, calibrate probes, and

This module contains the following functions:

    *  - returns the
    *
"""
# standard library
import os
import sys
import logging
import time
from dataclasses import dataclass
from dataclasses import field

# third-party site packages
import numpy as np
import matplotlib.figure as mpl
import matplotlib.pyplot as plt

# Custome Package files
from aiolos_code_instrumentation.timer import timer

from aiolos_commissioning_tools import __version__
from aiolos_fluid_dynamics.physical_constants import INCHES_H2O
from aiolos_fluid_dynamics import fluid_dynamics_relationships as fluids

log = logging.getLogger(__name__)

# Pressure measurement equipment
ZOC334 = 334
ZOC335 = 335
ZOC732 = 732

pressure_scanner_names = {'ZOC334': ZOC334,
                          'ZOC335': ZOC335,
                          'ZOC732': ZOC732,
                          ZOC334: 'ZOC334',
                          ZOC335: 'ZOC335',
                          ZOC732: 'ZOC732'}

pressure_scanner_ranges = {ZOC334: 10 * INCHES_H2O, # 2488.4 Pa = 10 inches water
                           ZOC335: 10 * INCHES_H2O, # 2488.4 Pa = 10 inches water
                           ZOC732: 20 * INCHES_H2O} # 4976.8 Pa = 20 inches water

# pressure probes
AEROPROBE = 10
CEA = 20
UNITEDSENSOR = 30
AIRFLOW=40

pressure_probe_names = {'AEROPROBE': AEROPROBE,
                        'CEA': CEA,
                        'UNITEDSENSOR': UNITEDSENSOR,
                        'AIRFLOW': AIRFLOW,
                        AEROPROBE: 'AEROPROBE',
                        CEA: 'CEA',
                        UNITEDSENSOR: 'UNITEDSENSOR',
                        AIRFLOW: 'AIRFLOW'}

pressure_probe_coefficients = {AEROPROBE: {'kp': 0.0, 'kq' : 1.0},
                               CEA: {'kp': 0.0, 'kq' : 1.0},
                               UNITEDSENSOR : {'kp' : 0.0, 'kq' : 1.0},
                               AIRFLOW: {'kp' : 0.003, 'kq' : 0.997}
                               }


def add_scanner(scanner_id, scanner_name, scanner_range):
    pressure_scanner_names[scanner_id] = scanner_name
    pressure_scanner_names[scanner_name] = scanner_id
    pressure_scanner_ranges[scanner_id] = scanner_range


def add_probe(probe_id, probe_name):
    pressure_probe_names[probe_id] = probe_name
    pressure_probe_names[probe_name] = probe_id


@dataclass
class PneumaticProbe:
    id: int
    pitch: np.float64 = field(repr=False, default='')
    yaw: np.float64 = field(repr=False, default='')
    cal_file: str = field(repr=False, default='')
    kp: float = field(init=False)
    kq: float = field(init=False)
    name: str = field(init=False)

    def __post_init__(self):
        try:
            self.name = pressure_probe_names[self.id]
            self.kp = pressure_probe_coefficients[self.id]['kp']
            self.kq = pressure_probe_coefficients[self.id]['kq']
        except KeyError as err:
            log.error(err)


@dataclass
class PressureScanner:
    id: int
    ref: int
    name: str = field(init=False)
    range: float = field(init=False)

    def __post_init__(self):
        try:
            self.name = pressure_scanner_names[self.id]
            self.range = pressure_scanner_ranges[self.id]
        except KeyError as err:
            log.error(err)


@dataclass
class ScannerData:

    run_id: int
    scanner_id: int
    port_count: int
    frame_count: int
    ref: int
    scanner_name: str
    file_name: str = field(repr=False)
    pressure: np.ndarray = field(repr=False)
    port: np.ndarray = field(repr=False)
    frame: np.ndarray = field(repr=False)


def load_scanner_data(data_file, scanner_id, reference_port=0, run_id=0):

    """

    :param data_file:   <str> path to data file containing pressure data
    :param scanner_id:  <int>
    :param reference_port:
    :return:
    """
    _ = timer.Timer()

    scanner = PressureScanner(id=scanner_id, ref=reference_port)
    log.debug('Loading data file %s from %s' % (os.path.basename(data_file), scanner.__repr__()) )

    if scanner.id == ZOC732 or scanner.id == ZOC334 or scanner.id == ZOC335:
        try:
            scanner_group, scanner_frame, scanner_module, scanner_port, scanner_data = np.loadtxt(data_file, unpack=True)
        except ValueError as err:
            log.warning(err)
            try:
                scanner_group, scanner_frame, scanner_module, scanner_port, scanner_data = np.loadtxt(data_file, delimiter=',', unpack=True)
            except (ValueError, IOError, FileNotFoundError) as err:
                log.error(err)
                log.error('could not load run %i [%s]' % (run_id, os.path.basename(data_file)))
                raise err
            else:
                log.warning('FIXED: Pressure data was "," delimited')
        finally:

            frame_count = int(np.max(scanner_frame)) # number of frames (i.e. number of data samples)
            port_count = len(scanner_data)//frame_count  # port number is not sequential - calculate total number of ports
            log.debug('no. of frames = %03i, no. of ports = %02i' % (frame_count, port_count))

            pressure_data = np.ndarray(shape=(frame_count, port_count), dtype=np.float64)
            frame_num = np.ndarray(shape=(frame_count, port_count), dtype=int)
            port_num = np.ndarray(shape=(port_count,), dtype=int)

            use_ref = 0
            ref = np.zeros(shape=(frame_count,), dtype=int)
            if not reference_port == 0:
                use_ref = 1
                # use reference_port to offset pressure data from other channels
                # ref is the index of reference_port
                ref = np.where(scanner_port == reference_port)[0]
            for f in range(frame_count):
                for p in range(port_count):
                    pressure_data[f, p] = scanner_data[p + f*port_count] - use_ref * scanner_data[ref[f]]
                    port_num[p] = scanner_port[p + f*port_count]
                    frame_num[f, p] = scanner_frame[p + f*port_count]

    else:
        err_msg = "%s not a valid pressure scanner type" % scanner.__repr__()
        log.error(err_msg)
        raise ValueError(err_msg)
    uncertainty = np.ndarray(shape=(port_count,))
    uncertainty_fs = np.ndarray(shape=(port_count,))
    average = np.ndarray(shape=(port_count,))

    for p in range(port_count):
        average[p] = np.mean(pressure_data[:, p], dtype=np.float64)
        uncertainty[p] = np.std(pressure_data[:, p]/average[p]) if np.abs(average[p]) > 0 else 0
        uncertainty_fs[p] = np.std(pressure_data[:, p]/scanner.range)
        log.debug('sigma(p) = %.4f %% (%.4f %% FS) on port %02i where mean(p) = %.4f Pa' % (uncertainty[p] * 100, uncertainty_fs[p] * 100, port_num[p], average[p]))


    max_uncertainty = np.max(uncertainty)
    max_fs = uncertainty_fs[np.where(uncertainty == max_uncertainty)[0]]
    max_port = port_num[np.where(uncertainty == max_uncertainty)[0]]
    max_avg = average[np.where(uncertainty == max_uncertainty)[0]]

    min_uncertainty = np.min(uncertainty[np.where(uncertainty > 0.0)])
    min_fs = uncertainty_fs[np.where(uncertainty == min_uncertainty)[0]]
    min_port = port_num[np.where(uncertainty == min_uncertainty)[0]]
    min_avg = average[np.where(uncertainty == min_uncertainty)[0]]

    mean_uncertainty = np.mean(uncertainty)

    log.debug('max sigma(p) = %.4f %% (%.4f %% FS) on port %02i where mean(p) = %.4f Pa' %  (max_uncertainty*100,max_fs*100, max_port, max_avg))
    log.debug('min sigma(p) = %.4f %% (%.4f %% FS) on port %02i where mean(p) = %.4f Pa' %  (min_uncertainty*100,min_fs*100, min_port, min_avg))
    log.debug('mean sigma(p) = %.4f %% ' % (mean_uncertainty*100))

    return ScannerData(
        run_id=run_id, scanner_id=scanner.id, scanner_name=scanner.name, port_count=port_count, frame_count=frame_count,
        pressure=pressure_data, port=port_num, frame=frame_num, ref=reference_port, file_name=data_file
    )

def calibrate_4_hole(pressure, alpha, beta, probe_id=1):
    """

    :param pressure:    <2D array<float>> size(numruns, 6) pressure data for each port + po $ ps
    :param alpha:       <1D array<float>> flow pitch angle data
    :param beta:        <1D array<float>> flow yaw angle data
    :param probe_id:    <int> probe ID
    :return:
            f
    """
    pass

def generate_probe_calibration_func(calibration_file, file_units='rad'):
    """

    :param calibration_file:    <str> path to file containing the calibration data
    :param file_units:          <str> == deg or degrees : specifies that the calibration file is in units of degrees
    :return:
        alpha:      <func> returns pitch angle of the flow relative to the probe axis
        beta:       <func> returns yaw angle of the flow relative to the probe axis

    notes:
        ws : wind speed [m/s]
        ao : probe picth offset angle during calibration
        ma : probe sensitivity in pitch
        bo : probe yaw offset angle during calibration
        mb : probe sensitivity in yaw

    calibratin file format
        whitespace separated columns of ws  ao  ma  bo  mb
        one row for each wind speed calibrated
    """
    ws, ao, ma, bo, mb = np.loadtxt(calibration_file, unpack=True)

    if file_units == 'deg' or file_units == 'degrees':
        bo = np.deg2rad(bo)  # bo [rad] => bo [°] * pi [rad] / 180 [°]
        ao = np.deg2rad(ao)  # ao [rad] => ao [°] * pi [rad] / 180 [°]

        ma = np.rad2deg(ma)  # ma [/rad]=> ma [/°] * 180 [°] / pi [rad]
        mb = np.rad2deg(mb)  # mb [/rad]=> mb [/°] * 180 [°] / pi [rad]

    def alpha(cp, u):
        m = np.interp(u, ws, ma)  # linear interpolation between wind speeds in calibration
        b = np.interp(u, ws, ao)  # linear interpolation between wind speeds in calibration
        return cp / m - b  # returns alpha in [rad]

    def beta(cp, u):
        m = np.interp(u, ws, mb) # linear interpolation between wind speeds in calibration
        b = np.interp(u, ws, bo) # linear interpolation between wind speeds in calibration
        return cp / m - b  # retuns beta in [rad]

    return alpha, beta


def main():
    """ Main function to call when this module is executed directly on a list of input data files"""
    log.setLevel(logging.DEBUG)

    fmt = logging.Formatter('%(asctime)s <%(levelname)s> [%(module)s.%(funcName)s]: %(message)s')
    strm_handler = logging.StreamHandler()
    strm_handler.setLevel(logging.DEBUG)
    strm_handler.setFormatter(fmt)

    log.addHandler(strm_handler)

    log.debug("%s -v%i.%i.%i module %s -v%s with test case(s) %s" %
              (sys.executable, sys.version_info[0], sys.version_info[1], sys.version_info[2],
               os.path.basename(sys.argv[0]), __version__, ', '.join(sys.argv[1:])))

    add_scanner(99, "DSA", 2500.)

    probe = PneumaticProbe(id=AEROPROBE)
    scanner = PressureScanner(id=ZOC334, ref=0)

    log.debug('Default %s ' % probe.__repr__())
    log.debug('Default %s ' % scanner.__repr__())

    for arg in sys.argv[1:]:
        data = load_scanner_data(arg, scanner.id, reference_port=scanner.ref)
        p_average = np.ndarray(shape=(len(data.pressure[0]),))
        if data.port_count < 100:  # TODO add functionality to print 10 at a time
            for p in range(data.port_count):
                if p % 8 == 0:
                    # show only 8 traces per figure
                    fig, ax = plt.subplots(8, 1, figsize=(10,5))
                p_average[p] = np.mean(data.pressure[:,p])
                ax[p%8].plot(data.pressure[:, p], linewidth=0.5, color='C0')
                ax[p%8].axhline(p_average[p]+np.std(data.pressure[:,p]), linestyle='--', color='C1', linewidth=0.5)
                ax[p%8].axhline(p_average[p]-np.std(data.pressure[:,p]), linestyle='--', color='C1', linewidth=0.5)
                ax[p%8].set_ylabel('%02i' % data.port[p])
            plt.show()
        else:
            log.debug('Too many ports to plot')


if __name__ == "__main__":
    start_time = time.time()
    main()
    print('[completed in %.2f seconds]' % (time.time() - start_time))
    input('Press <Enter> to exit')