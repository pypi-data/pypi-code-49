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
import math

from flyer_composer import (Box, papersizes, decide_scale)


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
    for inbox in (A4port, A4land):
        scale, rotate = decide_scale(inbox, flyerbox)
        assert scale == 1
        assert rotate == (inbox.is_landscape != flyerbox.is_landscape)


@pytest.mark.parametrize("flyerbox", [A5land, A5port],
                         ids=["landscape", "portrait"])
def test_A5_on_A4(flyerbox):
    # Ax formats are rounded to milimeters, thus scaling is not exactly
    # 1/sqrt(2) for each step
    expected_scale = 1 / math.sqrt(2)

    scale, rotate = decide_scale(A4port, flyerbox)
    assert rotate == flyerbox.is_landscape
    assert abs(scale - expected_scale) < 0.01

    scale, rotate = decide_scale(A4land, flyerbox)
    assert rotate == (not flyerbox.is_landscape)
    assert abs(scale - expected_scale) < 0.01


@pytest.mark.parametrize("flyerbox", [A6land, A6port],
                         ids=["landscape", "portrait"])
def test_A6_on_A4(flyerbox):
    expected_scale = 1 / math.sqrt(2) / math.sqrt(2)

    scale, rotate = decide_scale(A4port, flyerbox)
    assert rotate == flyerbox.is_landscape
    assert abs(scale - expected_scale) < 0.01

    scale, rotate = decide_scale(A4land, flyerbox)
    assert rotate == (not flyerbox.is_landscape)
    assert abs(scale - expected_scale) < 0.01


@pytest.mark.parametrize("flyerbox", [A7land, A7port],
                         ids=["landscape", "portrait"])
def test_A7_on_A4(flyerbox):
    expected_scale = 1 / math.sqrt(2) / math.sqrt(2) / math.sqrt(2)

    scale, rotate = decide_scale(A4port, flyerbox)
    assert rotate == flyerbox.is_landscape
    assert abs(scale - expected_scale) < 0.01

    scale, rotate = decide_scale(A4land, flyerbox)
    assert rotate == (not flyerbox.is_landscape)
    assert abs(scale - expected_scale) < 0.01
