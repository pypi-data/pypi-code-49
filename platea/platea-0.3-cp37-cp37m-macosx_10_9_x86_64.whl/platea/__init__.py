"""
Platea
=====
A package for simple numerical methods.

How to use the documentation
----------------------------
The docstring examples assume that `platea` has been imported as `pla`::
  >>> import platea as pla
Code snippets are indicated by three greater-than signs::
  >>> x = 42
  >>> x = x + 1
Use the built-in ``help`` function to view a function's docstring::
  >>> help(pla)
 or ``dir``::
  >>> dir(pla)
You can check the annotations of a function to see type hints::
  >>> pla.spcl_fnc.gamma.__annotations__
By conventions, look to modeule docstrings for source references and definitions
of important terms / acronyms.
  >>> help(pla.rng)

Available subpackages
---------------------
rng
    random number generators
dist
    tools for working with statistical distribution
spcl_fnc
    special mathematical functions like the `error function`
"""

import numpy as _np

try:
    # for local testing
    from . import _fortran
    from . import utilities
    from . import random_number_generators
    from . import distributions
    from . import special_functions
except:
    # when installed
    import platea._fortran
    import platea.utilities
    import platea.random_number_generators
    import platea.distributions
    import platea.special_functions

# TODO: add versioneer

def _get_precision():
    """
    Get precision.

    Will print the precision of numeric types in numpy.

    Notes
    ----------
    See these functions below for the fortran precision statistics
    stats._fortran.get_integer_precision()
    stats._fortran.get_real_precision()

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    print("Max Integer 32")
    print(_np.iinfo(_np.int32).max)
    print("Max Integer 64")
    print(_np.iinfo(_np.int64).max)

    print("Min Integer 32")
    print(_np.iinfo(_np.int32).min)
    print("Min Integer 64")
    print(_np.iinfo(_np.int64).min)

    print("Max Float 32")
    print(_np.finfo(_np.float32).max)
    print("Max Float 64")
    print(_np.finfo(_np.float64).max)

    print("Min Float 32")
    print(_np.finfo(_np.float32).min)
    print("Min Float 64")
    print(_np.finfo(_np.float64).min)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
