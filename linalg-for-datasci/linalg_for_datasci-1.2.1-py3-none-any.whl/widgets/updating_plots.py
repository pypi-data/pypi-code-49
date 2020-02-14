import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np


def init_updating_plot(title, xlabel, ylabel, xlim, ylim):
    output_widget = widgets.Output()
    figure = plt.figure()
    axis = figure.add_subplot(111)
    axis.set_title(title)
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    axis.set_xlim(xlim)
    axis.set_ylim(ylim)
    return output_widget, figure, axis


from ..utils import ball_to_box_ratio


def updating_ball_to_box_ratio_plot(
    callback, output_widget, figure, axis, trials=10000
):
    """
    callback is the dart_did_land_in_ball function students define in the notebook
    """
    xs = np.arange(1, 101)
    (line,) = axis.plot(0, 0)
    ratios = []

    with output_widget:
        for x in range(1, 101):
            output_widget.clear_output(wait=True)
            ratio = ball_to_box_ratio(trials, lambda: callback(x))
            ratios.append(ratio)
            line.set_xdata(xs[:x])
            line.set_ydata(ratios)
            figure.canvas.draw()
