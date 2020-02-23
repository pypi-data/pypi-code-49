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

"""Functions to create bar plots.

The purpose of this module is to facilitate the creation of bar
plots from multi-indexed Panda datasets.
"""

from numpy import arange as _arange


def get_subtrack_offset(n_subtrack, max_subtrack, width):
    """Get the X offset to center a subtrack around an origin.
    
    :param n_subtrack: The 0-based subtrack index
    :param max_subtrack: The number of subtracks
    :param The width of a single subtrack
    :return: The offset to apply
    """

    total_width = max_subtrack * width
    base_offset = -total_width / 2
    subtrack_offset = width * n_subtrack
    center_offset = width / 2
    return base_offset + subtrack_offset + center_offset


def barplot(ax, data, column, tracks, subtracks=[None], subtrackname=1,
            ncolumn=None, nformat="n={}", colors='rgb', width=.25):
    """Create a barplot from multi-indexed data.
    
    :param ax: The matplotlib axis to draw on
    :param data: The data from which the values to plot are taken
    :param column: The name of the column in the data frame containing
        the values to plot
    :param tracks: Index values used to select the tracks
    :param subtracks: Index values used to select the subtracks
    :param subtrackname: Index level at which subtracks are selected
    :param ncolumn: The name of the column containing the number of
        samples to be written on top of the bars (optional; no number
        will be written if set to 'None')
    :param nformat: Format string for the number of samples
    :param colors: A list of matplotlib color specifications (one for
        each subtrack)
    :param width: The width of a single subtrack:
    """

    for s, subtrack in enumerate(subtracks):
        if subtrack is not None:
            level = subtrackname if data.index.nlevels > 1 else None
            subset = data.xs(subtrack, level=level).loc[tracks, :]
        else:
            subset = data.loc[tracks, :]

        x = _arange(len(subset))
        ax.set_xticks(x)
        xoff = x + get_subtrack_offset(s, len(subtracks), width)
        rects = ax.bar(xoff, subset[column], width, color=colors[s])

        if ncolumn:
            for i, rect in enumerate(rects):
                height = rect.get_height()
                n = subset.loc[tracks, ncolumn][i]
                ax.annotate(nformat.format(n),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 5),
                            textcoords='offset points',
                            ha='center', va='center',
                            fontsize='xx-small')

    ax.set_xticklabels(tracks)

