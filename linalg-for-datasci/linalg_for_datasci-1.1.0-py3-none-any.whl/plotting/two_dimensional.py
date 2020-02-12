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


def plot_vector(ax, vector, scale=1, color="k", label="", origin=np.array([0, 0])):
    typecheck_vector(origin)
    assert len(origin) == 2
    typecheck_vector(vector)
    assert len(vector) == 2

    shifted_and_scaled_vector = (vector + origin) * scale
    scaled_vector = vector * scale

    if label:
        halign = "left" if vector[0] >= 0 else "right"
        valign = "bottom" if vector[1] >= 0 else "top"
        text_options = {
            "horizontalalignment": halign,
            "verticalalignment": valign,
            "color": color,
            "size": 22,
        }
        ax.text(*shifted_and_scaled_vector, label, **text_options)

    arrow_options = {
        "width": 0.3 * scale,
        "head_width": 0.4 * scale,
        "head_length": 0.3 * scale,
        "length_includes_head": True,
        "color": color,
    }
    return ax.arrow(*origin, *scaled_vector, **arrow_options)


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
