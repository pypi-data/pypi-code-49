# -*- coding: utf-8 -*-
"""
Created on Wednesday 12-February-2020 at 00:14

@author: Rastko Pajković
"""

import matplotlib.pyplot as plt


def dp_prep(x, ax, x_spacing_factor=0.05):
    """Prepare dynamic plot"""
    plt.ion()
    x_spacing = x_spacing_factor*(max(x)-min(x))
    ax.set(
        autoscaley_on=True,
        xlim=[min(x)-x_spacing, max(x)+x_spacing]
    )


def dp_update(line, x,y, fig, ax):
    """Update the plot data and rescale y axis"""
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    # We need to draw *and* flush
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)
