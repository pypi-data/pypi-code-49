#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

"""Various weather related formulas and utilities."""

import math


def CtoF(x):
    return x * 1.8 + 32.0


def FtoC(x):
    return (x - 32.0) * 5.0 / 9.0


def dewpointF(T, R):
    """Calculate dew point."""

    if T is None or R is None:
        return None

    TdC = dewpointC(FtoC(T), R)

    return CtoF(TdC) if TdC is not None else None


def dewpointC(T, R):
    """Calculate dew point."""

    if T is None or R is None:
        return None
    R = R / 100.0
    try:
        _gamma = 17.27 * T / (237.7 + T) + math.log(R)
        TdC = 237.7 * _gamma / (17.27 - _gamma)
    except (ValueError, OverflowError):
        TdC = None
    return TdC
