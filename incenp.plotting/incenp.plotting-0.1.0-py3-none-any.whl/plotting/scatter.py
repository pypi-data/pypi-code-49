# -*- coding: utf-8 -*-
# Incenp.Plotting - Incenp.org's plotting helper library
# Copyright © 2020 Damien Goutte-Gattat
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Functions to create scatter plots.

The purpose of this module is to facilitate the creation of scatter
plots from multi-indexed Panda datasets.
"""

from .util import xdistr, get_stars


def scatterplot_subtrack(ax, data, n_track, n_subtrack, max_subtrack,
                         color, width=.7, min_sep=-.05):
    """Plot a single subtrack.
    
    :param ax: The matplotlib axis to draw on
    :param data: The data series from which the values to plot are taken
    :param n_track: Offset of the current track
    :param n_subtrack: Offset of the current subtrack
    :param max_subtrack: Number of subtracks
    :param color: A matplotlib color specification
    :param width: The width of a subtrack
    :param min_sep: If two values in the data series differ by less
        than this parameter, they will be considered to belong on the
        same rank and will be distributed along the X axis
    """

    offset = n_track * max_subtrack + n_subtrack
    xs = xdistr(data.values, width, center=True, min_sep=min_sep, offset=offset)
    ax.plot(xs, data.values, color + '.')
    ax.hlines(data.mean(), offset - .5, offset + .5, color)


def scatterplot(ax, data, columns, subtrackcolumns=False,
                tracks=[None], trackname=0,
                subtracks=[None], subtrackname=1,
                colors='rgb', width=.7, min_sep=-.05, testfunc=None):
    """Create a scatterplot from multi-indexed data.
    
    :param ax: The matplotlib axis to draw on
    :param data: The data frame from which the values to plot are taken
    :param columns: The name of the column(s) in the data frame
        containing the values to plot
    :param subtrackcolumns: If true and columns is a list of column
        names, the different columns will be plotted as subtracks;
        otherwise they will be plotted as tracks; this parameter is
        irrelevant when columns is a single column name
    :param tracks: Index values used to select the tracks
    :param trackname: Index level at which tracks are selected
    :param subtracks: Index values used to select the subtracks
    :param subtrackname: Index level at which subtracks are selected
    :param colors: A list of matplotlib color specifications (one for
        each subtrack)
    :param width: The width of a subtrack
    :param min_sep: If two values in a subtrack differ by less than this
        parameter, they will be considered to belong on the same rank
        and will be distributed along the X axis
    :param testfunc: A statistical test function (must accept two data
        series as arguments and return a pvalue); if set and there are
        exactly two subtracks, the function will be called for each
        track and the signficance will be displayed on top of the track
    """

    # Get number of subtracks and track labels
    if isinstance(columns, list):
        if subtrackcolumns:
            # Subtracks are taken from the columns,
            # use tracks as specified
            n = len(columns) + 1
            labels = tracks
        else:
            # Tracks are taken from the columns,
            # use subtracks as specified
            n = len(subtracks) + 1
            labels = columns
    else:
        # Use tracks and subtracks as specified
        n = len(subtracks) + 1
        labels = tracks

    i = 0

    if isinstance(columns, list) and not subtrackcolumns:
        # Columns as tracks
        for column in columns:
            j = 0
            testset = []

            for subtrack in subtracks:
                subset = _get_dataseries(data, column, subtrack, subtrackname)
                testset.append(subset)
                scatterplot_subtrack(ax, subset, i, j, n, colors[j % n], width, min_sep)
                j += 1

            if testfunc and len(subtracks) == 2:
                _do_test(ax, testset, testfunc, i, n)

            i += 1

    else:
        for track in tracks:
            j = 0
            testset = []

            if isinstance(columns, list) and subtrackcolumns:
                # Columns as subtracks
                for column in columns:
                    subset = _get_dataseries(data, column, track, trackname)
                    testset.append(subset)
                    scatterplot_subtrack(ax, subset, i, j, n, colors[j % n], width, min_sep)
                    j += 1
            else:
                for subtrack in subtracks:
                    indexer = [track, subtrack] if subtrack else [track]
                    level = [trackname, subtrackname] if subtrack else [trackname]

                    subset = _get_dataseries(data, columns, indexer, level=level)
                    testset.append(subset)
                    scatterplot_subtrack(ax, subset, i, j, n, colors[j % n], width, min_sep)
                    j += 1

            if testfunc and len(testset) == 2:
                _do_test(ax, testset, testfunc, i, n)

            i += 1

    ax.set_xticks([(.5 * (n - 2)) + n * i for i in range(len(labels))])
    ax.set_xticklabels(labels)


def _get_dataseries(data, column, indexer, level):
    if indexer:
        if data.index.nlevels == 1:
            level = None
        data = data.xs(indexer, level=level)
    return data.loc[:, column].dropna()


def _do_test(ax, testset, testfunc, n_track, max_subtrack):
    pvalue = testfunc(testset[0], testset[1])
    if pvalue:
        y = max(testset[0].max(), testset[1].max()) * 1.1
        offset = n_track * max_subtrack
        ax.hlines(y, offset - .5, offset + 1.5)
        ax.text(offset + .5, y, get_stars(pvalue), ha='center', va='bottom')

