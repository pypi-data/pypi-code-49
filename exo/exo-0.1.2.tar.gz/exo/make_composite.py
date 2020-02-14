#!/usr/bin/python
from __future__ import division

import math
import sys

import click

import matplotlib
import matplotlib.pyplot as plt

import numpy

import pandas as pd

matplotlib.use('Agg')


def findRelativeMaxPoint(data):
    """
    Function to find the max and min for the input data of CDT values
    """

    values = list(data.iloc[0])  # selecting the first row values as a list
    maxi = max(values)    # finding the maximum of the values
    # finding the index of the max value within the list of values
    max_index = values.index(maxi)
    # co-ordinate on the composite plot
    zero_relative = float(list(data.iloc[[], [max_index]])[0])

    return [zero_relative, maxi]


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.argument('sample', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.argument('control', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.option('-t', '--title', metavar="<string>", default=' ', prompt=True, show_default=' ', help='Plot Title')
@click.option('-sc', '--scolor', metavar="<string>", default='C70039', prompt=True, show_default='C70039', help='Sample data color in Hexcode')
@click.option('-cc', '--ccolor', metavar="<string>", default='dc7633', prompt=True, show_default='dc7633', help=' Control data color in Hexcode')
@click.option('-bc', '--bcolor', metavar="<string>", default='212f3d', prompt=True, show_default='212f3d', help='Background color in Hexcode')
@click.option('-lc', '--lcolor', metavar="<string>", default='28de0f', prompt=True, show_default='28de0f', help='Center line color in Hexcode')
@click.option('-d', '--dpi', metavar="<int>", type=int, default=100, prompt=True, show_default='100', help='Plot pixel density')
@click.option('-ym', '--ymax', metavar="<int>", type=int, default=10, prompt=True, show_default='10', help='Min-Max value to set the Y-axis upper limit')
@click.option('-o', '--out', metavar="<string>", default='Composite_plot.png', prompt=True, show_default='Composite_plot.png', help='output filename')
def cli(sample, control, title, scolor, ccolor, bcolor, lcolor, dpi, ymax, out):
    """
    Program to create the composite plots from signal and control tag pile up CDT data matrix.

    \b
    Colors are in Hexcode, no need to add '#' in front of the hexcode.
    Info: Hexcode is an alphanumeric value of length six.

    """
    click.echo('\n' + '.' * 50)

    # reading the CDT file.
    try:
        signalData = pd.read_csv(sample, sep='\t', index_col=0)
        controlData = pd.read_csv(control, sep='\t', index_col=0)
    except IOError:
        print("\nUnable to OPEN input files !\n")
        sys.exit(1)

    print("signalData shape : {}".format(signalData.shape))
    print("controlData shape : {}".format(controlData.shape))

    # prepare PlotData for sample
    signalData = signalData.round(decimals=3)

    # Calculating the peak value index with respect to origin.
    mPeak = findRelativeMaxPoint(signalData)
    print(mPeak)

    # retrieve the row index from the dataframe
    rowIndex = list(signalData.index)

    # retrieve data for signal dataset
    sx = list(signalData.loc[rowIndex[0]])

    # retrieve values for y axis and convert them to float
    sy = list(signalData.columns)
    sy = list(map(float, sy))

    # retrieve the row index from the controlData dataframe
    rowIndex = list(controlData.index)

    # retrieve data for control dataset
    cx = list(controlData.loc[rowIndex[0]])

    # retrieve values for y axis and convert them to float
    cy = list(controlData.columns)
    cy = list(map(float, cy))

    # setting the font
    # matplotlib.rcParams['font.family'] = "Arial"

    # generating the figure
    fig, ax = plt.subplots()

    # plotting the signal data
    plt.plot(sy, sx, color="#" + scolor, label="Signal")

    # adding the background color
    d = numpy.zeros(len(sx))
    plt.fill_between(sy, sx, where=sx >= d, interpolate=False,
                     color="#" + bcolor)

    # plotting the control data
    plt.plot(cy, cx, color="#" + ccolor, label="Control")

    # adding the vertical line at midpoint
    plt.axvline(x=0, color="#" + lcolor, linestyle='--', linewidth=2)

    # adding yticks and label
    plt.yticks([0, max(int(ymax), math.ceil(mPeak[1]))], fontsize=18)
    plt.ylabel('Tags', fontsize=18)

    # setting the padding space between the y-axis label and the y-axis
    if math.ceil(mPeak[1]) < 10:
        ax.yaxis.labelpad = -16
    else:
        ax.yaxis.labelpad = -25

    # adding text to the composite plot. (the peak location.)
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html

    # changing the co-ordinates to position the value to the top right corner
    left, width = 0.28, .7
    bottom, height = .28, .7
    right = left + width
    top = bottom + height

    # position of the peak relative to 0
    value = '(' + str(int(mPeak[0])) + ')'
    # plt.text(x=-480, y=(int(math.ceil(mPeak[1])-0.2)), s=value, fontsize=12)
    plt.text(right, top, value,
             horizontalalignment='right',
             verticalalignment='top',
             transform=ax.transAxes, fontsize=14)

    # setting the ylimits for yticks
    ax.set_ylim(0, max(int(ymax), math.ceil(mPeak[1])))

    # removing the x-axis ticks
    plt.xticks([])

    # adding the title and increase the spine width
    plt.title(title, fontsize=25)
    plt.setp(ax.spines.values(), linewidth=2)

    # referance for margins
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.margins.html#matplotlib.pyplot.margins

    plt.margins(0)
    plt.tick_params(length=8, width=2)

    plt.savefig(out, facecolor=None, dpi=int(
        dpi), pad_inches=0.05, bbox_inches='tight')
    click.echo('\n' + '.' * 50)
