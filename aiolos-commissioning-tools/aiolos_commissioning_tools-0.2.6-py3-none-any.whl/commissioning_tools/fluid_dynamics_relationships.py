# standard library
import logging
# third party site-packages
import numpy as np
from numba import vectorize

# this package
from commissioning_tools import __version__
from commissioning_tools.physical_constants import GAMMA, R_AIR, R_H2O


log = logging.getLogger(__name__)

# ====================================================================================================================================================================================================#
# FLUID PROPERTIES
# ====================================================================================================================================================================================================#

@np.vectorize
def ideal_gas_law(p=None, rho=None, T=None):
    """
    Solve the ideal gas law based on two thermodynamic parameters
    :param p:   <float> or <np.ndarray<float>> pressure in Pa
    :param rho: <float> or <np.ndarray<float>> density in kg/m**3
    :param T:   <float> or <np.ndarray<float>> temperature in Kelvin
    :return:
        returns the missing paramter
    """
    if p != None and rho != None and  T != None:
        errmsg = "ideal gas law over constrained: provide two of three parameters (P, rho T)"
        log.error(errmsg)
        raise ValueError(errmsg)

    if rho != None and  T != None:
        log.debug("calculating pressure from ideal gas law with density (%.2f kg/m**3) and temperature (%.2f K)" % (rho, T))
        return rho*R_AIR*T
    if p != None and T != None:
        log.debug("calculating density from ideal gas law with pressure (%.2f kPa) and temperature (%.2f K)" % (p/1000, T))
        return p/R_AIR/T
    if p != None and rho != None:
        log.debug("calculating temperature from ideal gas law with pressure (%.2f kPa) and density (%.2f kg/m**3)" % (p/1000, rho))
        return p/R_AIR/rho
    else:
        errmsg  = "ideal gas law requires at least two of three paramters (P, rho, T)"
        log.error(errmsg)
        raise ValueError(errmsg)

@np.vectorize
def density_air_water_vapour(p, p_h2o, T):
    return (1 / T) * (p_h2o/R_H2O + (p - p_h2o)/R_AIR)

@np.vectorize
def water_vapour_pressure(dew_point_temperature, dry_bulb_temperature):
    """
        Hyland and Wexler relationship for water vapour pressure, Ph2o
    :param dew_point_temperature:
    :return:
    """

    tb = dry_bulb_temperature
    tdp = dew_point_temperature

    C1 = np.array([
        -5.6745359e3,
        6.3925247,
        -9.677843e-3,
        6.22115701e-7,
        2.0747825e-9,
        -9.484024e-13,
        4.1635019
    ])
    C2 = np.array([
        -5.8002206e3,
        1.3914993,
        -4.8640239e-2,
        4.1764768e-5,
        -1.4452093e-8,
        6.5459673
    ])

    if tdp < 173.15:
        errmsg = "Dry Bulb Temperature Out of Range: Too low "
        log.error(errmsg)
        raise ValueError(errmsg)

    if tdp > 473.15:
        errmsg = "Dry Bulb Temperature Out of Range: Too high"
        log.error(errmsg)
        raise ValueError(errmsg)

    if tdp <= 273.15:
        C = C1

    if 273.15 < tdp <= 473.15:
        C = C2

    return np.exp(np.sum(C[i]*tdp**(i-1) for i in range(len(C)-1))+C[-1]*np.log(tdp))


@np.vectorize
def sutherland(T):
    """

    # =======================================================================#
    #
    #       FUNCTION:           sutherland(T)
    #
    #       DESCRIPTION:        Computes the dynamic viscosity (mu) from the absolute
    #                           temperautre (T) using the relationship established
    #                           by William Sutherland (1893)
    #                           
    #
    #
    #       ARGUMENTS
    #
    #           :param T:       <np.ndarray<np.float64> of size mx1> array or scalar    
    #                           of Temperature
    #
    #       OUTPUTS
    #
    #           :result x:      <np.ndarray<np.float64> of size T.size> results vector
    #
    # =======================================================================#

    """
    mu_o    = 1.716e-5      # kg/ms
    T_o     = 273.15        # Kelvin
    S       = 110.40        # Kelvin
    
    
    return mu_o * ( T / T_o )**(3./2.) * ( T_o + S) / ( T + S) 


# ====================================================================================================================================================================================================#
# ISENTROPIC RELATIONS
# ====================================================================================================================================================================================================#

@np.vectorize
def static_temperature(To, M):
    return To * (1 + (GAMMA - 1)/2.0*M**2)**(-1)


@np.vectorize
def static_pressure(Po, M):
    return Po * (1 + (GAMMA-1.)/2. * M**2)**(-GAMMA/(GAMMA-1))


@np.vectorize
def Mach_number(Po=None, p=None, dp=None, p_abs=None, kp=None, kq=None):
    if Po != None and p != None: #  use isentropic relation M = f(Po/p)
        log.debug("Using isentrop relation M = f(Po/p)")
        return np.sqrt(2./(GAMMA-1.) * ((Po/p)**((GAMMA-1)/GAMMA) - 1))
    else:  # use wind speed coefficients to calculate M from contraction pressure drop
        log.debug("Using wind tunnel calibration M = f(P, kp, kq)")
        return np.sqrt(2./(GAMMA-1.) * ((kq*dp/(kp*dp+p_abs) + 1.)**((GAMMA-1)/GAMMA) - 1))


@np.vectorize
def dynamic_pressure(p, M):
    return GAMMA/2.0*p*M**2
