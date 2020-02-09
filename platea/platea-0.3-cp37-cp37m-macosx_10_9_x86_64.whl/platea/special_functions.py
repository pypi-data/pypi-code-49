"""
Special Functions
=====
Special functions commonly used in numerical calculations.

Notes
----------
The docstring examples assume that `special_functions` has been imported as `sf`::
  >>> from platea import special_functions as sf
"""

from numpy import ndarray
from typing import Union, Tuple

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # when installed
    import platea._fortran.spcl_fnc as _spcl_fnc
except:
    # for local testing
    from . import _fortran
    _spcl_fnc = _fortran.spcl_fnc

################################################################################
# gamma function

def gamma(x: Union[float, ndarray]) -> ndarray:
    """
    The gamma function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/5.2#E1
    Numerical Recipes 3Ed 6.1

    Parameters
    ----------
    x : float, ndarray[float], ndarray[float, float]
        Real valued argument to the gamma function. Can be a single value or an
        array. Can be one or two dimensional.

    Returns
    -------
    ndarray
        gamma function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.gamma.gammv(x)
        if x.shape[0] == 1:
            return _spcl_fnc.gamma.gammv(x[0, :]).reshape(1,-1)
        return _spcl_fnc.gamma.gammv2(x)
    return _spcl_fnc.gamma.gamm(x)

def gammaln(x: Union[float, ndarray]) -> ndarray:
    """
    Log of the absolute value of the gamma function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/5
    Numerical Recipes 3Ed 6.1

    Parameters
    ----------
    x : float, ndarray[float], ndarray[float, float]
        Real valued argument to the gamma function. Can be a single value or an
        array. Can be one or two dimensional.

    Returns
    -------
    ndarray
        natural log of the gamma function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.gamma.gammlnv(x)
        if x.shape[0] == 1:
            return _spcl_fnc.gamma.gammlnv(x[0, :]).reshape(1,-1)
        return _spcl_fnc.gamma.gammlnv2(x)
    return _spcl_fnc.gamma.gammln(x)

def gammap(a: Union[float, ndarray], x: Union[float, ndarray]) -> ndarray:
    """
    Lower incomplete gamma function. CDF of the gamma distribution.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/8.2#E4
    Numerical Recipes 3Ed 6.2

    Parameters
    ----------
    a : float, ndarray[float], ndarray[float, float]
        Parametertizes the gamma distribution. Must be > 0.0 Can be a single
        value or an array. Can be one or two dimensional.
    x : float, ndarray[float], ndarray[float, float]
        Probability expressed as a value 0.0 to 1.0. Must be >= 0.0 Can be a
        single value or an array. Can be one or two dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.gamma.gammpv(a, x)
        if x.shape[0] == 1:
            return _spcl_fnc.gamma.gammpv(a[0, :], x[0, :]).reshape(1,-1)
        return _spcl_fnc.gamma.gammpv2(a, x)
    return _spcl_fnc.gamma.gammp(a, x)

def gammaq(a: Union[float, ndarray], x: Union[float, ndarray]) -> ndarray:
    """
    Upper incomplete gamma function. Survival function of the gamma distribution.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/8.2#E4
    Numerical Recipes 3Ed 6.2

    Parameters
    ----------
    a : float, ndarray[float], ndarray[float, float]
        Parametertizes the gamma distribution. Must be > 0.0 Can be a single
        value or an array. Can be one or two dimensional.
    x : float, ndarray[float], ndarray[float, float]
        Non-negative argument. Must be >= 0.0 Can be a single value or an array.
        Can be one or two dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.gamma.gammqv(a, x)
        if x.shape[0] == 1:
            return _spcl_fnc.gamma.gammqv(a[0, :], x[0, :]).reshape(1,-1)
        return _spcl_fnc.gamma.gammqv2(a, x)
    return _spcl_fnc.gamma.gammq(a, x)

################################################################################
# error function

def erf(x: Union[float, ndarray]) -> ndarray:
    """
    Error function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/7.2#i
    Numerical Recipes in C 2Ed 6.2

    Parameters
    ----------
    x: float, ndarray[float], ndarray[float, float]
        Real valued input. Can be a single value or an array. Can be one or two
        dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.error_function.erfv(x)
        if x.shape[0] == 1:
            return _spcl_fnc.error_function.erfv(x[0, :]).reshape(1,-1)
        return _spcl_fnc.error_function.erfv2(x)
    return _spcl_fnc.error_function.erf(x)

def erfc(x: Union[float, ndarray]) -> ndarray:
    """
    Complementary error function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/7.2#i
    Numerical Recipes in C 2Ed 6.2

    Parameters
    ----------
    x: float, ndarray[float], ndarray[float, float]
        Real valued input. Can be a single value or an array. Can be one or two
        dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.error_function.erfcv(x)
        if x.shape[0] == 1:
            return _spcl_fnc.error_function.erfcv(x[0, :]).reshape(1,-1)
        return _spcl_fnc.error_function.erfcv2(x)
    return _spcl_fnc.error_function.erfc(x)

def erfcc(x: Union[float, ndarray]) -> ndarray:
    """
    Chebyshev approximation of complementary error function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/7.2#i
    Numerical Recipes in C 2Ed 6.2

    Parameters
    ----------
    x: float, ndarray[float], ndarray[float, float]
        Real valued input. Can be a single value or an array. Can be one or two
        dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(x, ndarray):
        if len(x.shape) == 1:
            return _spcl_fnc.error_function.erfccv(x)
        if x.shape[0] == 1:
            return _spcl_fnc.error_function.erfccv(x[0, :]).reshape(1,-1)
        return _spcl_fnc.error_function.erfccv2(x)
    return _spcl_fnc.error_function.erfcc(x)

def inverfc(p: Union[float, ndarray]) -> ndarray:
    """
    Inverse of the complementary error function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/7.17
    Numerical Recipes 3Ed 6.2

    Parameters
    ----------
    p: float, ndarray[float], ndarray[float, float]
        Real valued input. A probability [0.0, 1.0]. Can be a single value or an
        array. Can be one or two dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(p, ndarray):
        if len(p.shape) == 1:
            return _spcl_fnc.error_function.inverfcv(p)
        if p.shape[0] == 1:
            return _spcl_fnc.error_function.inverfcv(p[0, :]).reshape(1,-1)
        return _spcl_fnc.error_function.inverfcv2(p)
    return _spcl_fnc.error_function.inverfc(p)

def inverf(p: Union[float, ndarray]) -> ndarray:
    """
    Inverse of the error function.

    Notes
    ----------
    NIST: https://dlmf.nist.gov/7.17
    Numerical Recipes 3Ed 6.2

    Parameters
    ----------
    p: float, ndarray[float], ndarray[float, float]
        Real valued input. A probability [0.0, 1.0]. Can be a single value or an
        array. Can be one or two dimensional.

    Returns
    -------
    ndarray
        function value
    """
    if isinstance(p, ndarray):
        if len(p.shape) == 1:
            return _spcl_fnc.error_function.inverfv(p)
        if p.shape[0] == 1:
            return _spcl_fnc.error_function.inverfv(p[0, :]).reshape(1,-1)
        return _spcl_fnc.error_function.inverfv2(p)
    return _spcl_fnc.error_function.inverf(p)

################################################################################
