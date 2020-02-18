"""
this file contains unit conversions to treat non-SI units

e.g.

when loading a data file containing pressures in PSI
 >>> import numpy as np
 >>> from aiolos_fluid_dynamics import units
 >>> data = np.loadtxt('data_file.dat') * units.PSI



"""
import numpy as np

# pressure: converts units to base units of Pascals
PASCALS     = 1.0               # Pascals               --> Pascals
KPA         = 1.0e3             # kilopascals           --> Pascals
BAR         = 1.0e5             # Bar                   --> Pascals
PSI         = 6894.76           # Pounds per sq. inch   --> Pascals
INCHES_H2O  = 248.84            # inches of water       --> Pascals
INCHES_Hg   = 3386.39           # inches of mercury     --> Pascals

# velocity: used to convert values to base units of m/s
METERS_PER_SECOND = 1.0         # meter per second      --> meters per second
KPH         = 1.0 / 3.6         # kilometer per hour    --> meters per second
MPH         = 4.44704e-1        # miles per hour        --> meters per second
KNOTS       = 1.0 / 1.9438445   # nautical miles per hour-> meters per second

# length: converts values to base units of meters
METERS      = 1.0               # meters                --> meters
MM          = 1.0e-3            # millimeters           --> meters
CM          = 1.0e-2            # centimeters           --> meters
KM          = 1.0e3             # kilometers            --> meters
INCHES      = 2.540e-2          # inches                --> meters
FEET        = 3.048e-1          # feet                  --> meters
NM          = 1852.0            # nautical miles        --> meters

# Temperature
RANKIN      = 5.0 / 9.0         # degrees Rankin        --> degrees Kelvin


@np.vectorize
def celcius_to_kelvin(T):
    return T + 273.15


@np.vectorize
def rankin_to_kelvin(T):
    return T * RANKIN


@np.vectorize
def farhenheit_to_kelvin(T):
    return (T + 459.67) * RANKIN
