from matplotlib.pyplot import colorbar
from matplotlib.colors import LogNorm
from numpy import random, meshgrid

def PlotVapor2D(ax, cax, vapor, x2, x1, cloud = None, vlevel = None, clevel = None):
  X, Y = meshgrid(x2, x1)
  #alevel = arange(0., 3.75, 0.25)
  h = ax.contourf(X, Y, vapor.T, levels = vlevel, cmap = 'inferno', extend = 'both')
  if cloud is not None:
    ax.contourf(X, Y, cloud.T, levels = clevel, cmap = 'Greys_r',
      norm = LogNorm(), alpha = 0.8)
  colorbar(h, cax = cax)

  ax.set_xlim([min(x2), max(x2)])
  ax.set_ylim([min(x1), max(x1)])
  ax.set_ylabel('Height (km)', fontsize = 15)
  ax.set_xlabel('Distance (km)', fontsize = 15)

def PlotPrecipitation2D(ax, precip, x2, x1, vmin = 0., scale = 5.E4):
  dx = (x2[-1] - x2[0])/(len(x2) - 1)
  dy = (x1[-1] - x1[0])/(len(x1) - 1)
  X, Y = meshgrid(x2, x1)

  # find places with precipitation
  ip = precip > vmin
  xp = (X.T)[ip]
  yp = (Y.T)[ip]

  # randomize the position of precipitation in the cell
  xp += dx*(random.rand(len(xp)) - 0.5)
  yp += dy*(random.rand(len(yp)) - 0.5)

  ax.scatter(xp, yp, marker = 'o', color = 'b', s = precip[ip]*scale)
