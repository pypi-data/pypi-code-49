"""Functions that operate with math data, numpy arrays and Sympy.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from IPython.display import display
from scipy.interpolate import Akima1DInterpolator
from sympy.solvers.solveset import nonlinsolve, linsolve


SI_CONSTANTS = {'gravity': 9.80665,  # in m/s2
                }
CONVERT_FACTORS = {'N-kgf': SI_CONSTANTS['gravity'],
                   'MPa-kgf/cm2':
                       100 / SI_CONSTANTS['gravity'],
                   'kg/m3-kg/cm3': (1 / 1000000),
                   }


def check_array_consecutiveness(array_like):
    """Check consecutiveness of elements values in a array.

    Parameters
    ----------
    array_like : numpy array or similar convertible to it
        Input array to be flattened and check for elements values
        consecutiveness.

    Returns
    -------
    Boolean
        True if all elements values are consecutive, False otherwise.
    numpy array
        Positions of not consecutive elements

    Raises
    ------
    AssertionError
        Not numeric data in `array_like`.
    """
    # Normalize input to numpy array object and flatten it.
    array = np.asarray(array_like)
    array = array.flatten()
    assert array.dtype.kind not in {'U', 'S'}, \
        'Array should contain numeric data only'

    # Check for not consecutive values and gather their positions.
    array_diff = np.diff(sorted(array))
    bool_consecutiveness = sum(array_diff == 1) >= len(array) - 1
    fail_positions = np.argwhere(np.diff(sorted(array)) > 1) + 2
    return bool_consecutiveness, fail_positions


def convert_units(quantity, conversion, inverse=False):
    """Convert float from a physical unit to another.

    Parameters
    ----------
    quantity : float
        Physical magnitude value to be converted.
    conversion : string from `CONVERT_FACTORS` dictionary
        Determines from and to which measurement unit to convert.
    inverse : Boolean
        If True, perform the inverse conversion. Default is False.

    Returns
    -------
    float
        Physical quantity in new measure unit.

    Raises
    ------
    AssertionError
        Conversion factor not established `CONVERT_FACTORS` dictionary.
    """
    assert conversion in CONVERT_FACTORS.keys(),\
        'Conversion factor not defined'

    if not inverse:
        converted = quantity * CONVERT_FACTORS[conversion]
    else:
        converted = quantity * (1 / CONVERT_FACTORS[conversion])
    return converted


def eval_sympy(expression, substitute_dict):
    """Substitute numeric values into sympy expressions recursively.

    Parameters
    ----------
    expression : sympy object
        Algebraic expression.
    substitute_dict: dict
        Variable name:value pairs to substitute from.

    Returns
    -------
    sympy object
        Evaluated algebraic expression.
    """
    # Attempt a symbolic eval, check for expression changes, return when
    # no more changes occur.
    for _ in range(0, len(substitute_dict) + 1):
        new_expr = expression.subs(substitute_dict)
        if new_expr == expression:
            break
    return new_expr


def extract_unique_sub_arrays(array_like):
    """Filter out repeated sub-arrays in multidimensional array.

    Parameters
    ----------
    array_like : numpy array or similar convertible to it
        Input array to be filtered.

    Returns
    -------
    numpy array
        Input array with unique sub-arrays.

    Raises
    ------
    AssertionError
        Input `array_like` does not contain any sub-arrays.
    """
    # Normalize input to numpy array object.
    array = np.asarray(array_like)
    assert array.ndim >= 2, 'Array should be mulidimensional'

    # Deal with data types, store array efficiently and filter unique.
    types = np.dtype((np.void, array.dtype.itemsize *
                      np.prod(array.shape[1:])))
    contiguous = np.ascontiguousarray(array.reshape(array.shape[0],
                                                    -1)).view(types)
    return array[np.unique(contiguous, return_index=True)[1]]


def generate_primes(amount):
    """Generate first n primes.

    Parameters
    ----------
    amount : int
        Amount of prime numbers to generate.

    Returns
    -------
    list
        Prime numbers.
    """
    # Set first prime and first candidate for generator.
    output_list = [2]
    number = 3

    # Generate candidates, test primeness and append them if positive.
    while len(output_list) < amount:
        primeness = True
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                primeness = False
                break
        if primeness:
            output_list.append(number)
        number += 1
    return output_list


def generate_primes_to(limit):
    """Generate all prime numbers, up to a given number.

    Parameters
    ----------
    limit : int
        Upper limit of generated primes.

    Returns
    -------
    list
        Prime numbers.
    """
    # Move up python limit for generator.
    limit = limit + 1

    # Generate candidates, try for and mark composites numbers.
    prime = [True] * limit
    for number in range(2, limit):
        if prime[number]:
            yield number
            for _ in range(number * number, limit, number):
                prime[_] = False


def generate_white_noise(mean, std, num_samples):
    """Generate normalized random values.

    Parameters
    ----------
    mean : float
        Mean of output samples.
    std : float
        Standard deviation of output samples.
    num_samples : int
        Amount of output samples.

    Returns
    -------
    numpy array
        Numeric samples.
    """
    return np.random.normal(mean, std, size=num_samples)


def integrate_num_2d(independent, dependent, verbose=False):
    """Calculate and plot numerical integral of a one variable function.

    Plot the curve corresponding to the function. Limits of the integral
    are given by `independent` domain.

    Parameters
    ----------
    independent : numpy array
        Independent variable values.
    dependent : numpy array
        Dependent variable values.
    verbose : bool, optional
        If True, print integral value. Default is False.

    Returns
    -------
    float
        Value of numeric integral.

    Raises
    ------
    AssertionError
        `independent` and `dependent` arrays have different dimensions.
    """
    assert independent.shape == dependent.shape,\
        'Independent and dependent variables arrays should be consistent'
    integral = np.trapz(independent, dependent)
    plt.plot(independent, dependent, markersize=5, marker='o')
    plt.show()
    if verbose:
        print('Integral value:', round(integral, 2))
    return integral


def interpolate_2d(independent, dependent, plot=True):
    """Interpolate a one variable function with the Akima algorithm.

    Parameters
    ----------
    independent : numpy array
        Independent variable values.
    dependent : numpy array
        Dependent variable values.
    plot : bool, optional
        If True, plot original vs interpolated curves. Default is False.

    Returns
    -------
    numpy array
        Interpolated independent values.
    numpy array
        Interpolated dependent values.

    Raises
    ------
    AssertionError
        `x` and `y` arrays have different dimensions.
    """
    assert independent.shape == dependent.shape,\
        'Independent and dependent variables arrays should be consistent'

    # Start interpolator, re-sample independent values, calculate
    # interpolated dependent values.
    interpolator = Akima1DInterpolator(independent, dependent)
    new_independent = np.linspace(np.amin(independent),
                                  np.amax(np.asarray(independent)),
                                  10000)
    new_dependent = interpolator(new_independent)
    if plot:
        fig = plt.figure(figsize=(10, 8))
        axes = fig.add_subplot(111)
        axes.plot(independent, dependent, marker='o')
        axes.plot(new_independent, new_dependent)
        plt.show()
    return new_independent, new_dependent


def ishigami_eq(x_1, x_2, x_3):
    """Mathematical Ishigami function of three variables.

    Parameters
    ----------
    x_1, x_2, x_3 : numpy arrays
        Input independent variables.

    Returns
    -------
    numpy array
        Dependent variable.

    Notes
    -----
    The Ishigami function of Ishigami & Homma (1990) is used as a test
    for uncertainty and sensitivity analysis methods, because it
    exhibits strong non-linearity and no-monotonicity.
    It also has a peculiar dependence on x_3, as described by Sobol
    & Levitan (1999).
    """
    return np.sin(x_1) + 7 * np.sin(x_2) ** 2 + 0.1 * x_3 ** 4 * np.sin(x_1)


def round_down_n(input_f, base=5):
    """Round down a float to a multiple of a given number.

    Parameters
    ----------
    input_f : float
        Value to be rounded.
    base: int
        Multiple of which to round down to.

    Returns
    -------
    int
        Rounded number.
    """
    return int(math.floor(input_f / base)) * base


def round_up_n(input_f, base=5):
    """Round up a float to a multiple of a given number.

    Parameters
    ----------
    input_f : float
        Value to be rounded.
    base: int
        Multiple of which to round up to.

    Returns
    -------
    int
        Rounded number.
    """
    return int(math.ceil(input_f / base)) * base


def solve_equations_system(variables, equations, replace_values=None):
    """Solve linear and non linear equations system using Sympy library.

    Parameters
    ----------
    variables : list of str
        Name of independent variable to solve for.
    equations : list of sympy equations objects
        Conform the equations system.
    replace_values : dict, optional
        If given, substitute variables for numeric values established
        in dict, as variable name:value pairs. Default is None.

    Returns
    -------
    dict
        Variable name: Solution value pairs.
    """
    # If a Matrix is present in the system, use linear solver;
    # otherwise, load a non linear solver.
    solver = nonlinsolve
    for equation in equations:
        if isinstance(equation, sp.Matrix):
            solver = linsolve
            break

    # Solve equations and extract solutions.
    solution = solver(equations, *variables)
    solution = {variable: list(solution)[0][pos] for
                pos, variable in enumerate(variables)}

    # Replace constants and extract values.
    if replace_values is not None:
        solution = {key: sp.simplify(eval_sympy(val, replace_values)) for
                    key, val in solution.items()}

    # Try to show solution with Latex, use ascii if not possible.
    try:
        sp.init_printing(use_latex=True, forecolor='White')
        display(solution)
    except ImportError:
        print(solution)
    return solution
