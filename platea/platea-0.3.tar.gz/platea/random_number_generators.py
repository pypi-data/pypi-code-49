"""
Random Number Generators
=====
This module contains random number generators (RNGs). These RNGs are operating
system (OS) agnostic.

Notes
----------
The docstring examples assume that `random_number_generators` has been imported as `rng`::
  >>> from platea import random_number_generators as rng
"""

import numpy as _np
from numpy import ndarray
from typing import Union, Tuple

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # when installed
    import platea._fortran.ran_num_gen.rng as _rng
except:
    # for local testing
    from . import _fortran
    _rng = _fortran.ran_num_gen.rng

################################################################################

class Ran0(object):
    """
    Random number generator (RNG).

    Notes
    ----------
    Numerical Recipes in Fortran77 Ch7.1 <ran0>
    Numerical Recipes in C 2Ed Ch7.1 <ran0>

    Attributes
    ----------
    state_size int
        The length of the state array of the rng

    Methods
    -------
    set_state(seed)
        Set the internal state of the rng.
    get_state()
        Get the current internal state of the rng.
    draw(n)
        Sample random number(s).

    Examples
    --------
    >>> random_number_generator = rng.Ran0()
    >>> state = random_number_generator.get_state()
    >>> random_number_generator.set_state(seed=state)
    >>> random_number = random_number_generator.draw(n=1)
    """

    def __init__(self, seed: Union[int, ndarray] = -99999999999) -> None:
        """
        Initialize the object.

        Parameters
        ----------
        seed : int, ndarray[int]
            Random seed to initialize the rng. Must be between [-99999999999, 0].

        Returns
        -------
        None
        """
        self.set_state(seed)
        self.state_size = 1

    def set_state(self, seed: Union[int, ndarray]) -> None:
        """
        Set the state of the rng.

        Parameters
        ----------
        seed : int, ndarray[int]
            If an integer valued [-99999999999, 0], the RNG will be rest using
            that seed. Any other value will set the state of the RNG. For
            example, you could set the state of RNG one to the state of RNG two
            rather than resetting RNG one with a new seed.

        Returns
        -------
        None
        """
        if isinstance(seed, ndarray):
            self._state = seed.copy()
        self._state = seed

    def get_state(self) -> ndarray:
        """
        Get the internal state of the rng.

        Parameters
        ----------
        None

        Returns
        -------
        ndarray[int]
            the current internal state of the RNG
        """
        return self._state.copy() # don't return the actually state array

    def draw(self, n: Union[int, Tuple[int, int]] = 1) -> ndarray:
        """
        Draw random numbers valued [0.0, 1.0].

        Parameters
        ----------
        n : int, tuple(int, int)
            The number of samples to draw. Can be one or two dimensional.

        Returns
        -------
        ndarray[float]
            samples from a uniform distribution [0.0, 1.0]
        """
        if isinstance(n, tuple):
            self._state, output = _rng.ran0v2(self._state, n[0], n[1])
            return output
        self._state, output = _rng.ran0v(self._state, n)
        return output

################################################################################

class Ran1(object):
    """
    Random number generator (RNG).

    Notes
    ----------
    Numerical Recipes in Fortran77 Ch7.1 <ran1>
    Numerical Recipes in C 2Ed Ch7.1 <ran1>

    Attributes
    ----------
    state_size int
        The length of the state array of the rng

    Methods
    -------
    set_state(seed)
        Set the internal state of the rng.
    get_state()
        Get the current internal state of the rng.
    draw(n)
        Sample random number(s).

    Examples
    --------
    >>> random_number_generator = rng.Ran1()
    >>> state = random_number_generator.get_state()
    >>> random_number_generator.set_state(seed=state)
    >>> random_number = random_number_generator.draw(n=1)
    """

    def __init__(self, seed: Union[int, ndarray] = -99999999999) -> None:
        """
        Initialize the object.

        Parameters
        ----------
        seed : int
            Random seed to initialize the rng. Must be between [-99999999999, 0].

        Returns
        -------
        None
        """
        self.set_state(seed)
        self.state_size = 34

    def set_state(self, seed: Union[int, ndarray]) -> None:
        """
        Set the state of the rng.

        Parameters
        ----------
        seed : int, ndarray[int]
            If an integer valued [-99999999999, 0], the RNG will be rest using
            that seed. Any other value will set the state of the RNG. For
            example, you could set the state of RNG one to the state of RNG two
            rather than resetting RNG one with a new seed.

        Returns
        -------
        None
        """
        if not isinstance(seed, ndarray):
            self._state = _np.zeros(34)
            self._state[0] = seed
        else:
            self._state = seed.copy()

    def get_state(self) -> ndarray:
        """
        Get the internal state of the rng.

        Parameters
        ----------
        None

        Returns
        -------
        ndarray[int]
            the current internal state of the RNG
        """
        return self._state.copy() # don't return the actually state array

    def draw(self, n: Union[int, Tuple[int, int]] = 1) -> ndarray:
        """
        Draw random numbers valued [0.0, 1.0].

        Parameters
        ----------
        n : int, tuple(int, int)
            The number of samples to draw. Can be one or two dimensional.

        Returns
        -------
        ndarray[float]
            samples from a uniform distribution [0.0, 1.0]
        """
        if isinstance(n, tuple):
            self._state, output = _rng.ran1v2(self._state, n[0], n[1])
            return output
        self._state, output = _rng.ran1v(self._state, n)
        return output

################################################################################

class Ran2(object):
    """
    Random number generator (RNG).

    Notes
    ----------
    Numerical Recipes in Fortran77 Ch7.1 <ran2>
    Numerical Recipes in C 2Ed Ch7.1 <ran2>

    Attributes
    ----------
    state_size int
        The length of the state array of the rng

    Methods
    -------
    set_state(seed)
        Set the internal state of the rng.
    get_state()
        Get the current internal state of the rng.
    draw(n)
        Sample random number(s).

    Examples
    --------
    >>> random_number_generator = rng.Ran2()
    >>> state = random_number_generator.get_state()
    >>> random_number_generator.set_state(seed=state)
    >>> random_number = random_number_generator.draw(n=1)
    """

    def __init__(self, seed: Union[int, ndarray] = -99999999999) -> None:
        """
        Initialize the object.

        Parameters
        ----------
        seed : int
            Random seed to initialize the rng. Must be between [-99999999999, 0].

        Returns
        -------
        None
        """
        self.state_size = 35
        self.set_state(seed)

    def set_state(self, seed: Union[int, ndarray]) -> None:
        """
        Set the state of the rng.

        Parameters
        ----------
        seed : int, ndarray[int]
            If an integer valued [-99999999999, 0], the RNG will be rest using
            that seed. Any other value will set the state of the RNG. For
            example, you could set the state of RNG one to the state of RNG two
            rather than resetting RNG one with a new seed.

        Returns
        -------
        None
        """
        if not isinstance(seed, ndarray):
            self._state = _np.zeros(35)
            self._state[0] = seed
        else:
            self._state = seed.copy()

    def get_state(self) -> ndarray:
        """
        Get the internal state of the rng.

        Parameters
        ----------
        None

        Returns
        -------
        ndarray[int]
            the current internal state of the RNG
        """
        return self._state.copy() # don't return the actually state array

    def draw(self, n: Union[int, Tuple[int, int]] = 1) -> ndarray:
        """
        Draw random numbers valued [0.0, 1.0].

        Parameters
        ----------
        n : int, tuple(int, int)
            The number of samples to draw. Can be one or two dimensional.

        Returns
        -------
        ndarray[float]
            samples from a uniform distribution [0.0, 1.0]
        """
        if isinstance(n, tuple):
            self._state, output = _rng.ran2v2(self._state, n[0], n[1])
            return output
        self._state, output = _rng.ran2v(self._state, n)
        return output

################################################################################

# set the defualt random number generator
# MUST match line 15 in stats/_fortran/random_number_generators.f90
Ran = Ran2

################################################################################
