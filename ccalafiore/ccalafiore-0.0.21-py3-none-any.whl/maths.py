from numbers import *
import numpy as np


def factors_of_x(x, y=1):
    type_x = type(x)
    type_y = type(y)

    x_is_integer = isinstance(x, Integral)

    # The Numeric abstract base classes:
    # numbers.Complex
    # numbers.Real
    # numbers.Integral
    # numbers.Number

    if not x_is_integer:
        raise Exception('x must be ab integer. Now, type_x = {}'.format(type_x))

    y_is_integer = isinstance(y, Integral)
    if not y_is_integer:
        raise Exception('y must be ab integer. Now, type_y = {}'.format(type_y))

    factors = np.empty(0, int)

    for i in range(y, x + 1):
        if x % i == 0:
            factors = np.append(factors, i)

    return factors