#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Christian Heider Nielsen'
__doc__ = ''

import matplotlib
import numpy
from matplotlib import pyplot as plt


def plot_value_function(V, title="Value Function"):
  """
  Plots the value function as a surface plot.
  """
  min_x = min(k[0] for k in V.keys())
  max_x = max(k[0] for k in V.keys())
  min_y = min(k[1] for k in V.keys())
  max_y = max(k[1] for k in V.keys())

  x_range = numpy.arange(min_x, max_x + 1)
  y_range = numpy.arange(min_y, max_y + 1)
  X, Y = numpy.meshgrid(x_range, y_range)

  # Find value for all (x, y) coordinates
  Z_noace = numpy.apply_along_axis(lambda _:V[(_[0], _[1], False)], 2, numpy.dstack([X, Y]))
  Z_ace = numpy.apply_along_axis(lambda _:V[(_[0], _[1], True)], 2, numpy.dstack([X, Y]))

  def plot_surface(X, Y, Z, title):
    fig = pyplot.figure(figsize=(20, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                           cmap=matplotlib.cm.coolwarm, vmin=-1.0, vmax=1.0)
    ax.set_xlabel('Player Sum')
    ax.set_ylabel('Dealer Showing')
    ax.set_zlabel('Value')
    ax.set_title(title)
    ax.view_init(ax.elev, -120)
    fig.colorbar(surf)
    pyplot.show()

  plot_surface(X, Y, Z_noace, "{} (No Usable Ace)".format(title))
  plot_surface(X, Y, Z_ace, "{} (Usable Ace)".format(title))


if __name__ == '__main__':
  plot_value_function(
    {(0, 0, False):0, (0, 1, False):0, (1, 0, False):10, (1, 1, False):10, (0, 0, True):0, (0, 1, True):0,
     (1, 0, True): 10, (1, 1, True):10
     })
