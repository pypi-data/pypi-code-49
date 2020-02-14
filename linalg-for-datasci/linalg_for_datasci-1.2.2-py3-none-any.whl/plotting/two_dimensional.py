import matplotlib.pyplot as plt
import numpy as np

from ..arrays import col_to_vec
from ..arrays import row_to_vec
from ..tests import typecheck_vector


def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, "--")


def timeseries_plot(discretized_function_vector, title="Time Series Plot", ylim=None):
    try:
        typecheck_vector(discretized_function_vector)
    except AssertionError:
        try:
            col_to_vec(discretized_function_vector)
        except AssertionError:
            row_to_vec(discretized_function_vector)

    xvalues = np.arange(len(discretized_function_vector))
    plt.plot(xvalues, discretized_function_vector)
    plt.title(title)
    plt.xlabel("Coordinate number")
    plt.ylabel("Value at coordinate")
    plt.xlim([-1, len(discretized_function_vector) + 1])
    if ylim:
        plt.ylim(ylim)
    else:
        plt.ylim(
            [
                np.min(discretized_function_vector) - 0.1,
                np.max(discretized_function_vector) + 0.1,
            ]
        )
