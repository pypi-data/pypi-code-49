import collections.abc

import numpy as np
import matplotlib.pyplot as plt

from ._distribution import Discrete, Continuous
from .utils import ecdf

__all__ = ["plot_ecdf", "plot_hist", "plot_pmf", "plot_pdf", "plot_cdf"]


def plot_ecdf(samples, show=False):
    """Plot the empirical cumulative distribution function
    of the samples. This can be used to estimate the centeral
    tendency of sampled data.

    Parameters
    -----
    samples: array_like
             Observed data.
    
    Examples
    -----
    >>> import swissroll.distributions as srd
    >>> from swissroll import plotter
    >>> samples = srd.Binomial(20, 0.7)
    >>> plotter.plot_ecdf(samples)
    """
    x_ecdf, y_ecdf = ecdf(samples)
    plt.plot(x_ecdf, y_ecdf, marker=".", linestyle="none")
    if show:
        plt.show()


def plot_hist(samples, show=False):
    """Plot the histogram of the observed data.

    Parameters
    -----
    samples: array_like
             Observed data.
    
    Examples
    -----
    >>> import swissroll.distributions as srd
    >>> from swissroll import plotter
    >>> samples = srd.Binomial(20, 0.7)
    >>> plotter.plot_hist(samples)
    """
    plt.hist(samples, bins=10, density=True)
    if show:
        plt.show()


def plot_pmf(distributions, support, show=False):
    """Plot the Probability Mass Function of multiple
    distributions.

    Parameters
    -----
    distributions: list, tuple
                   distributions whose pmf is to be evaluated.
    
    support: list, array_like
             values at which pmf is to be evaluated. It can be
             different or common for all the distributions.
    
    Examples
    -----
    >>> import swissroll.distributions as srd
    >>> from swissroll import plotter
    >>> dist = srd.Binomial(20, 0.7)
    >>> support = np.arange(0, 20, dtype=np.float32)
    >>> plotter.plot_pmf(dist, support)
    """
    if isinstance(support, np.ndarray) or not isinstance(
        support, collections.abc.Collection
    ):
        plot_pmf(distributions, [support] * len(distributions))
        return

    if len(distributions) != len(support):
        raise ValueError("length of support must be equal" " to distributions!")

    for distribution, y in zip(distributions, support):
        if isinstance(distribution, Continuous):
            raise ValueError(
                "Continuous distributions don't have"
                " a mass function! Try swissroll.plotter.plot_pdf"
            )
        plt.plot(y, distribution.pmf(y), label=distribution._short_str)
    plt.legend()
    if show:
        plt.show()


def plot_pdf(distributions, support, show=False):
    """Plot the Probability Density Function of multiple
    or single distributions.

    Parameters
    -----
    distributions: list, tuple, array_like
                   distributions whose pdf is to be evaluated.
    
    support: list, tuple, array_like
             values at which pdf is to be evaluated. It can be
             different or common for all the distributions.
    
    Examples
    -----
    >>> import swissroll.distributions as srd
    >>> from swissroll import plotter
    >>> dist = srd.Binomial(20, 0.7)
    >>> support = np.arange(0, 20, dtype=np.float32)
    >>> plotter.plot_pdf(dist, support)
    """
    if isinstance(support, np.ndarray) or not isinstance(
        support, collections.abc.Collection
    ):
        plot_pdf(distributions, [support] * len(distributions))
        return

    if len(distributions) != len(support):
        raise ValueError("length of support must be equal" " to distributions!")

    for distribution, y in zip(distributions, support):
        if isinstance(distribution, Discrete):
            raise ValueError(
                "Discrete distributions don't have"
                " a density function!"
                " Try `swissroll.plotter.plot_pmf`"
            )
        plt.plot(y, distribution.pdf(y), label=distribution._short_str)
    plt.legend()
    if show:
        plt.show()


def plot_cdf(distributions, support, show=False):
    """Plot the Cumulative Distribution Function of multiple
    distributions.

    Parameters
    -----
    distributions: list, tuple
                   distributions whose cdf is to be evaluated.
    
    support: list, array_like
             values at which cdf is to be evaluated. It can be
             different for all the distributions or common.
    
    Examples
    -----
    >>> import swissroll.distributions as srd
    >>> from swissroll import plotter
    >>> dist = srd.Binomial(20, 0.7)
    >>> support = np.arange(0, 20, dtype=np.float32)
    >>> plotter.plot_cdf(dist, support)
    """
    if isinstance(support, np.ndarray) or not isinstance(
        support, collections.abc.Collection
    ):
        plot_cdf(distributions, [support] * len(distributions))
        return

    if len(distributions) != len(support):
        raise ValueError("length of support must be equal" " to distributions!")

    for distribution, y in zip(distributions, support):
        plt.plot(y, distribution.cdf(y), label=distribution._short_str)
    plt.legend()
    if show:
        plt.show()


def say_what(just_for_fun=True):
    # undocumented easter egg!
    print("What!!!")
