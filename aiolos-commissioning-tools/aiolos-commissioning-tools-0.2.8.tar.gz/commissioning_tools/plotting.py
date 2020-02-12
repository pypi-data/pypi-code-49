import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy
#from matplotlib.mlab import griddata
from matplotlib import colors as mc

from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.interpolate import griddata


def add_to_plot(x, y, fig=plt.figure(),
                 label='', type='', color='',
                 markersize=1.0,  linewidth=1.0):
    plt.plot(x, y, color + type, label=label,  markersize=markersize, linewidth=linewidth)

def plotter(x, y, ax, label='', type='', color='',
                 markersize=1.0,  linewidth=1.0):
    ax = plt.plot(x, y, color + type, label=label,  markersize=markersize, linewidth=linewidth)
    return ax


def drawOnPlot(fig=plt.figure(),pts=[[0,0],[0,1],[1,0],[1,1]],color='k',type='',linewidth=1.0):
    """pts = [[x1,y1],[x2,y2]...,[xn,yn]] counterclockwise around perimeter"""
    x = zip(*pts)[0]
    y = zip(*pts)[1]
    for i in range(0,len(pts)):
        if i == len(pts) -1:  # last element so join first and last point
            plt.plot([x[0], x[-1]], [y[0], y[-1]],
                     color + type, linewidth=linewidth)
        else:
            plt.plot([x[i], x[i+1]], [y[i], y[i+1]],
                     color + type, linewidth=linewidth)


def contourFrom1D(x, y, z, ax=None,fig=None, npts=300, interp="cubic", crange=[[], [], []],
                  labels=["Title", "x-axis", "y-axis", "z-axis"], colmap="coolwarm", ncons=10, area=1.0, extend="both",
                  alpha=1.0, nlines=10, text='', xticks=11, yticks=6):
    if ax == None:
        fig, ax = plt.subplots(1,1)

    # plot size detals
    if crange[0] == []:
        # xmin, xmax = Xmin, Xmax
        xmin, xmax = np.nanmin(x), np.nanmax(x)
    else:
        xmin, xmax = crange[0]

    if crange[1] == []:
        # ymin, ymax = Ymin, Ymax
        ymin, ymax = np.nanmin(y), np.nanmax(y)
    else:
        ymin, ymax = crange[1]

    if crange[2] == []:
        # zmin, zmax = Zmin, Zmax
        zmin, zmax = np.nanmin(z), np.nanmax(z)
    else:
        zmin, zmax = crange[2]

    xi, yi = np.linspace(xmin, xmax, npts), np.linspace(ymin, ymax, npts)
    xi, yi = np.meshgrid(xi, yi)

    #zi = griddata(x, y, z, xi, yi, interp=interp)
    # triangles = mpl.tri.Triangulation(xi,yi)

    zi = scipy.interpolate.griddata((x,y), z, (xi,yi), method=interp,)
    # plt.imshow(zi, vmin=np.nanmin(z), vmax=np.nanmax(z), origin='lower',
    # extent=[np.nanmin(x), np.nanmax(x), np.nanmin(y), np.nanmax(y)])
    # plot color details
    cmap = plt.get_cmap(colmap)
    levels = np.linspace(zmin, zmax, ncons)
    lines = np.linspace(zmin, zmax, nlines)
    norm = mc.BoundaryNorm(levels, cmap.N)

    # axis details
    #ax = fig.add_subplot(111)
    ax.set_title(labels[0])
    ax.set_xlabel(labels[1])
    ax.set_ylabel(labels[2])
    ax.set_xlim(xmin, xmax, auto=False)
    ax.set_ylim(ymin, ymax, auto=False)
    ax.set_xticks(np.linspace(xmin, xmax, xticks))
    ax.set_yticks(np.linspace(ymin, ymax, yticks))

    ax.grid(b=True, which="major", linestyle='--', linewidth=0.5)
    ax.grid(b=True, which="minor", linestyle='--', linewidth=0.5)
    ax.set_aspect('equal')
    ax.tick_params(axis='both', which='both', direction='in')

    ax.text(0.05, 0.85, text, fontsize=8, transform=ax.transAxes)

    # create color flood
    cs = ax.contourf(xi, yi, zi, levels=levels, cmap=cmap, vmin=zmin, vmax=zmax, alpha=alpha)
    # cs = ax.imshow(zi, norm=norm, vmin=zmin, vmax=zmax)
    # cs = mpl.tri.tripcolor(ax, triangles, zi)
    # add legend
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size='5%', pad=0.05)
    cbar = plt.colorbar(cs, ticks=lines, cax=cax)
    cbar.ax.set_ylabel(labels[3])
    # add contour lines
    #cs2 = ax.contour(cs, linewidths=0.5, levels=cs.levels[0:-1:ncons//nlines], colors='k')
    cs2 = ax.contour(cs, linewidths=0.5, levels=lines, colors='k')
    # cs2 = ax.contour(cs, linewidths = 0.5, levels=levels, colors='k')
    cbar.add_lines(cs2)
    plt.clabel(cs2, fontsize=8, inline=1)
    # fig.colorbar()
    return fig, ax


def vector2D(x, y, u, v, ax=None,fig=None, npts=300,
             labels=["Title", "x-axis", "y-axis"],
             crange=[[],[]], interp='cubic',
             alpha=1.0, width=0.001, headwidth=10, headlength=15, scale=100,
             text='', xticks=11, yticks=6,
             textx=0.05, texty=0.85, keysize=0.1):
    if ax == None:
        fig, ax = plt.subplots(1,1)

    # plot size detals
    if crange[0] == []:
        # xmin, xmax = Xmin, Xmax
        xmin, xmax = np.nanmin(x), np.nanmax(x)
    else:
        xmin, xmax = crange[0]

    if crange[1] == []:
        # ymin, ymax = Ymin, Ymax
        ymin, ymax = np.nanmin(y), np.nanmax(y)
    else:
        ymin, ymax = crange[1]

    umin, umax = np.nanmin(u), np.nanmax(u)
    vmin, vmax = np.nanmin(v), np.nanmax(v)
    if interp != None:
        xi, yi = np.linspace(xmin, xmax, 2*npts-1), np.linspace(ymin, ymax, npts)
        xi, yi = np.meshgrid(xi, yi)

        ui = scipy.interpolate.griddata((x,y), u, (xi,yi), method=interp,)
        vi = scipy.interpolate.griddata((x,y), v, (xi,yi), method=interp,)
    else:
        xi, yi = x, y
        ui, vi = u, v
    # axis details
    ax.set_title(labels[0])
    ax.set_xlabel(labels[1])
    ax.set_ylabel(labels[2])
    ax.set_xlim(xmin, xmax, auto=False)
    ax.set_ylim(ymin, ymax, auto=False)
    ax.set_xticks(np.linspace(xmin, xmax, xticks))
    ax.set_yticks(np.linspace(ymin, ymax, yticks))

    ax.grid(b=True, which="major", linestyle='--', linewidth=0.5)
    ax.grid(b=True, which="minor", linestyle='--', linewidth=0.5)
    ax.set_aspect('equal')
    ax.tick_params(axis='both', which='both', direction='in')

    ax.text(textx, texty, text, fontsize=8, transform=ax.transAxes)

    # create vector plot
    q = ax.quiver(xi, yi, ui, vi, width=width, headwidth=headwidth, headlength=headlength, scale=scale)
    qk = ax.quiverkey(q, 0.9, 1.05, keysize, '%.2f' % keysize, labelpos='E')
    # add legend
    return fig, ax