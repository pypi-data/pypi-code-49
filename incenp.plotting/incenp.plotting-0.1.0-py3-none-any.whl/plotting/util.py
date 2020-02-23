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

"""Miscellaneous utility functions for plotting tasks."""


def xdistr(values, width, offset=0, even_max=10, center=False, min_sep=-.05):
    """Distribute coordinates around an axis.
    
    Given a list of values, return an array of x coordinates so that
    the plotted values are equally distributed.
    
    :param values: The list of values to distribute
    :param width: The distance along which to distribute the values
    :param offset: An offset to apply to each returned coordinates
    :param even_max: If the number of values on a given rank exceeds
        this parameter, they will be put closer together
    :param center: Distribute coordinates on both sides of offset
    :param min_sep: If two values differ by less than this parameter,
        they will be considered to belong on the same rank; if negative,
        it is interpreted as a fraction of the span of values
    :return: An array of x coordinates
    """

    dist = {}
    spent = {}
    xcoords = []

    if min_sep < 0:
        min_sep = (max(values) - min(values)) * -min_sep
    values = [int(i / min_sep) for i in values]

    # Get the distribution of values
    for v in values:
        if v in dist:
            dist[v] += 1
        else:
            dist[v] = 1
        spent[v] = 0

    # Now proceeds
    for v in values:

        # Compute step to distribute the values on the specified width
        step = width / max(even_max, dist[v])

        if not center:
            x = offset + step * spent[v]
        elif spent[v] % 2 == 0:
            # If we've already drawn an even number of points,
            # draw the next one on the right of offset
            x = offset + (step / 2) * spent[v]
        else:
            # Draw the next point on the left of offset
            x = offset - (step / 2) * (spent[v] + 1)

        # If there is an even number of points in that rank,
        # shift all points by a half-step
        if dist[v] % 2 == 0:
            x += step / 2

        spent[v] += 1
        xcoords.append(x)

    return xcoords


def get_stars(pvalue):
    if pvalue < 0.001:
        return '***'
    elif pvalue < 0.01:
        return '**'
    elif pvalue < 0.05:
        return '*'
    else:
        return 'ns'
