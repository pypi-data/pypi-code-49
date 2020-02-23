"""Functions that automatize plotting mathematical data.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

import numpy as np


def calculate_golden_fig_size(width, fraction=1):
    """Set aesthetic figure dimensions to avoid scaling in Latex.

    Parameters
    ----------
    width : float
        Width of output plot in points unit measure.
    fraction : float
        Multiplier factor of `width`.

    Returns
    -------
    float
        Plot width in inches.
    float
        Plot height in inches.
    """
    # Set conversion factor from pt to inches and golden ratio.
    inches_per_pt = 1 / 72.27
    golden_ratio = (5**.5 - 1) / 2

    # Calculate figure width and height in inches
    fig_width_pt = width * fraction
    fig_width_in = fig_width_pt * inches_per_pt
    fig_height_in = fig_width_in * golden_ratio
    return fig_width_in, fig_height_in


def calculate_plot_ticks(input_axes, ticks_no=4, decimals_no=2,
                         identical_axes=False):
    """Calculate ticks positions for matplotlib 2D plots.

    Parameters
    ----------
    input_axes : matplotlib axes
        Axes to calculate the ticks for.
    ticks_no : int
        Amount of ticks for the axes.
    decimals_no : int
        Amount of decimals to print in the plot.
    identical_axes : bool, optional
        If True, both axis ticks will be identical. Default is False.

    Returns
    -------
    tuple
        Ticks for x and y axis, respectively.
    """
    # Extract axis limits and round them.
    x_min, x_max, y_min, y_max = input_axes()
    x_min, x_max = round(x_min, decimals_no), round(x_max, decimals_no)
    y_min, y_max = round(y_min, decimals_no), round(y_max, decimals_no)

    # Generate ticks positions
    x_ticks = np.round(np.linspace(x_min, x_max, ticks_no), decimals_no)
    y_ticks = np.round(np.linspace(y_min, y_max, ticks_no), decimals_no)

    # Optionally Use same ticks for both axes
    if identical_axes:
        y_ticks = x_ticks
    return x_ticks, y_ticks
