#!/usr/bin/env python3
#
# Copyright 2012-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This file is part of flyer-composer.
#
# flyer-composer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# flyer-composer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with flyer-composer. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2012-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Affero General Public License v3 or later (AGPLv3+)"

import pytest

from flyer_composer import (Box, papersizes, decide_num_cols_rows)


def __make_box(name, landscape):
    box = Box(**{
        'width': papersizes[name][0],
        'height': papersizes[name][1],
        'offset_x': 0,
        'offset_y': 0,
        'unit': name,
        'units_x': 1,
        'units_y': 1,
    })
    if landscape:
        box.rotate()
        box['unit'] += '_land'
    return box


A4port = __make_box('a4', False)
A4land = __make_box('a4', True)
A5port = __make_box('a5', False)
A5land = __make_box('a5', True)
A6port = __make_box('a6', False)
A6land = __make_box('a6', True)
A7port = __make_box('a7', False)
A7land = __make_box('a7', True)

# -----

@pytest.mark.parametrize("flyerbox", [A4land, A4port],
                         ids=["landscape", "portrait"])
def test_A4_on_A4(flyerbox):
    for mediabox in (A4port, A4land):
        flyer, cols, rows = decide_num_cols_rows(flyerbox, mediabox)
        # flyer has same orientation as sheet
        assert flyer.is_landscape == mediabox.is_landscape
        # output is a single flyer
        assert (cols, rows) == (1, 1)


@pytest.mark.parametrize("flyerbox", [A5land, A5port],
                         ids=["landscape", "portrait"])
def test_A5_on_A4(flyerbox):
    flyer, cols, rows = decide_num_cols_rows(flyerbox, A4port)
    assert flyer.is_landscape
    assert (cols, rows) == (1, 2)

    flyer, cols, rows = decide_num_cols_rows(flyerbox, A4land)
    assert not flyer.is_landscape
    assert (cols, rows) == (2, 1)


@pytest.mark.parametrize("flyerbox", [A6land, A6port],
                         ids=["landscape", "portrait"])
def test_A6_on_A4(flyerbox):
    flyer, cols, rows = decide_num_cols_rows(flyerbox, A4port)
    assert not flyer.is_landscape
    assert (cols, rows) == (2, 2)

    flyer, cols, rows = decide_num_cols_rows(flyerbox, A4land)
    assert flyer.is_landscape
    assert (cols, rows) == (2, 2)


@pytest.mark.parametrize("flyerbox", [A7land, A7port],
                         ids=["landscape", "portrait"])
def test_A7_on_A4(flyerbox):
    flyer, cols, rows = decide_num_cols_rows(flyerbox, A4port)
    assert flyer.is_landscape
    assert (cols, rows) == (2, 4)

    flyer, cols, rows = decide_num_cols_rows(flyerbox, A4land)
    assert not flyer.is_landscape
    assert (cols, rows) == (4, 2)
