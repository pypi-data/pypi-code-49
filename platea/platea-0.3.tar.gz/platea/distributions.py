"""
Distributions
=====
This mode includes functions and classes for working with probability
distributions.

Notes
----------
The docstring examples assume that `distributions` has been imported as `dist`::
  >>> from platea import distributions as dist
"""

from numpy import ndarray
from typing import Union, Tuple

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # when installed
    import platea._fortran.dist as _dist
except:
    # for local testing
    from . import _fortran
    _dist = _fortran.dist

from platea import random_number_generators as _rng

################################################################################

class Normal(object):
    """
    Normal (Gaussian) distribution.

    Notes
    ----------
    Numerical Recipes 3Ed 6.14.1

    Attributes
    ----------
    mu float
        The mean of the Gaussian distribution.
    sigma float
        The standard deviation of the Gaussian distribution.
        (square root of the variance)
    state_size int
        The length of the state array of the rng used in the draw method

    Methods
    -------
    pdf(x, mu, sigma)
        Evaluate the pdf of the distribution at x.
    cdf(x, mu, sigma)
        Evaluate the cdf of the distribution at x.
    invdcdf(p, mu, sigma)
        Evaluate the invcdf of the distribution at p.
    draw(n, mu, sigma)
        Sample random number(s).
    set_state(seed)
        Set the internal state of the rng.
    get_state()
        Get the current internal state of the rng.

    Examples
    --------
    >>> norm = dist.Normal(mu=0.0, sigma=1.0)
    >>> pdf_value = norm.pdf(0.57)
    >>> sample = norm.draw(n=1)
    """

    def __init__(self, mu: float = None, sigma: float = None) -> None:
        """
        Initialize the object.

        Parameters
        ----------
        mu : float
            The mean of the Gaussian distribution.
        sigma float
            The standard deviation of the Gaussian distribution.
            (square root of the variance)

        Returns
        -------
        None
        """
        self.mu = mu
        self.sigma = sigma
        self._state = _rng.Ran().get_state()
        self.state_size = _rng.Ran().state_size

    def _check_sufficient_statistics(self, mu: float, sigma: float) -> Tuple[float, float]:
        """
        Checks that sufficient statistics exist and are valid values.
        """
        if mu is None or sigma is None:
            if self.mu is None or self.sigma is None:
                raise Exception("Please specify mu and sigma.")
            mu = self.mu
            sigma = self.sigma
        assert sigma >= 0.0, "Sigma must be positive."
        return mu, sigma

    def pdf(self, x: Union[float, ndarray], mu: float = None,
            sigma: float = None) -> ndarray:
        """
        Probability density function.

        Parameters
        ----------
        x : float, ndarray[float], ndarray[float, float]]
            Real valued argument to the function. Can be a single value or
            an array. Can be one or two dimensional.
        mu: float
            The mean of the Gaussian distribution. If `None` then uses the class
            attribute value.
        sigma: float
            The standard deviation of the Gaussian distribution. (square root of
            the variance). If `None` then uses the class attribute value.

        Returns
        -------
        ndarray
            function value
        """
        mu, sigma = self._check_sufficient_statistics(mu, sigma)
        if isinstance(x, ndarray):
            if len(x.shape) == 1:
                return _dist.normal.pdfv(mu, sigma, x)
            if x.shape[0] == 1:
                return _dist.normal.pdfv(mu, sigma, x[0, :]).reshape(1,-1)
            return _dist.normal.pdfv2(mu, sigma, x)
        return _dist.normal.pdf(mu, sigma, x)

    def cdf(self, x: Union[float, ndarray], mu: float = None,
            sigma: float = None) -> ndarray:
        """
        Cummulative density function.

        Parameters
        ----------
        x : float, ndarray[float], ndarray[float, float]]
            Real valued argument to the function. Can be a single value or
            an array. Can be one or two dimensional.
        mu: float
            The mean of the Gaussian distribution. If `None` then uses the class
            attribute value.
        sigma: float
            The standard deviation of the Gaussian distribution. (square root of
            the variance). If `None` then uses the class attribute value.

        Returns
        -------
        ndarray
            function value
        """
        mu, sigma = self._check_sufficient_statistics(mu, sigma)
        if isinstance(x, ndarray):
            if len(x.shape) == 1:
                return _dist.normal.cdfv(mu, sigma, x)
            if x.shape[0] == 1:
                return _dist.normal.cdfv(mu, sigma, x[0, :]).reshape(1,-1)
            return _dist.normal.cdfv2(mu, sigma, x)
        return _dist.normal.cdf(mu, sigma, x)

    def invcdf(self, p: Union[float, ndarray], mu: float = None,
               sigma: float = None) -> ndarray:
        """
        Inverse cummulative density function.

        Parameters
        ----------
        p : float, ndarray[float], ndarray[float, float]]
            Real valued argument to the function. Can be a single value or
            an array. Can be one or two dimensional. Should be a probability
            [0.0, 1.0]
        mu: float
            The mean of the Gaussian distribution. If `None` then uses the class
            attribute value.
        sigma: float
            The standard deviation of the Gaussian distribution. (square root of
            the variance). If `None` then uses the class attribute value.

        Returns
        -------
        ndarray
            function value
        """
        mu, sigma = self._check_sufficient_statistics(mu, sigma)
        if isinstance(p, ndarray):
            if len(p.shape) == 1:
                return _dist.normal.invcdfv(mu, sigma, p)
            if x.shape[0] == 1:
                return _dist.normal.invcdfv(mu, sigma, p[0, :]).reshape(1,-1)
            return _dist.normal.invcdfv2(mu, sigma, p)
        return _dist.normal.invcdf(mu, sigma, p)

    def draw(self, n: int = 1, mu: float = None,
             sigma: float = None) -> ndarray:
        """
        Draw random numbers valued [0.0, 1.0].

        Parameters
        ----------
        n : int, tuple(int, int)
            The number of samples to draw. Can be one or two dimensional.
        mu: float
            The mean of the Gaussian distribution. If `None` then uses the class
            attribute value.
        sigma: float
            The standard deviation of the Gaussian distribution. (square root of
            the variance). If `None` then uses the class attribute value.

        Returns
        -------
        ndarray[float]
            samples from the distribution
        """
        mu, sigma = self._check_sufficient_statistics(mu, sigma)
        if isinstance(n, tuple):
            self._state, output = _dist.normal.drawv2(mu, sigma, self._state, n[0], n[1])
            return output
        self._state, output = _dist.normal.drawv(mu, sigma, self._state, n)
        return output

    def set_state(self, seed: Union[int, ndarray]) -> None:
        """
        Set the state of the rng.

        Parameters
        ----------
        seed : int, ndarray[int]
            The seed for the rng. See the docs for the platea default rng:
            help(pla.random_number_generators.ran)

        Returns
        -------
        None
        """
        if not isinstance(seed, ndarray):
            self._state[:] = 0.0
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

################################################################################
