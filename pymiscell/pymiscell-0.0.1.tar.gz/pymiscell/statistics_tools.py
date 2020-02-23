"""Statistics related mathematical functions.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

import math

import numpy as np

from . import math_tools as mt


def calculate_empirical_cdf(variable_values):
    """Calculate numerical cumulative distribution function.

    Output tuple can be used to plot empirical cdf of input variable.

    Parameters
    ----------
    variable_values : numpy array
         Values of a given variable.

    Returns
    -------
    numpy array
        Ordered variable values.
    numpy array
        Accumulated percentages of relative variable values.
    """
    # Sort array and calculate accumulated percentages.
    values = np.sort(variable_values)
    accum_percentages = np.arange(1, len(values) + 1) / float(len(values))
    return values, accum_percentages


def code_variable_value(real_value, limits):
    """Transform a variable value to a scale between -1 and +1.

    Parameters
    ----------
    real_value : float
        Variable real value.
    limits : Tuple of 2 floats.
        Minimum and maximum real variable values.

    Returns
    -------
    float
        Coded variable value.
    """
    x_max, x_min = max(limits), min(limits)
    return (2 * (real_value - x_min) / (x_max - x_min)) - 1


def decode_variable_value(coded, limits):
    """Transform coded values between -1 and +1 into real scale values.

    Parameters
    ----------
    coded : float
        Coded variable value.
    limits : Tuple of 2 floats.
        Minimum and maximum real variable values.

    Returns
    -------
    float
        Variable real value.
    """
    x_max, x_min = max(limits), min(limits)
    return ((coded+1) * (x_max-x_min) * 0.5) + x_min


def generate_halton_sequence(dims_no, points_no):
    """Produce a Halton low discrepancy sequence.

    Output values are in the range 0, 1.

    Parameters
    ----------
    dims_no : int
         Number of dimensions (also called factors or variables).
    points_no : int
        Number of sample points to generate for each dimension.

    Returns
    -------
    numpy array
        Multidimensional array with generated points, in (0, 1) range.
    """
    # Initialize empty arrays and fill them with nan values.
    matrix = np.empty(points_no * dims_no)
    matrix.fill(np.nan)
    points_values = np.empty(points_no)
    points_values.fill(np.nan)

    # Run generator and fill output arrays
    primes = mt.generate_primes(dims_no)
    log_points = math.log(points_no + 1)
    for dim in range(dims_no):
        prime = primes[dim]
        limit = int(math.ceil(log_points / math.log(prime)))
        power = pow
        for _ in range(limit):
            points_values[_] = power(prime, -(_ + 1))
        for point in range(points_no):
            edge = point + 1
            sum_ = math.fmod(edge, prime) * points_values[0]
            for _ in range(1, limit):
                edge = math.floor(edge / prime)
                sum_ += math.fmod(edge, prime) * points_values[_]
            matrix[point * dims_no + dim] = sum_
    return matrix.reshape(points_no, dims_no)


def generate_monte_carlo_sequence(dims_no, points_no):
    """Produce a Monte Carlo random sequence.

    Output values are in the range -1, 1.

    Parameters
    ----------
    dims_no : int
         Number of dimensions (also called factors or variables).
    points_no : int
        Number of sample points to generate for each dimension.

    Returns
    -------
    numpy array
        Multidimensional array with generated points, in (-1, 1) range.
    """
    output = np.random.uniform(low=-1, high=1, size=(points_no, dims_no))
    return output
