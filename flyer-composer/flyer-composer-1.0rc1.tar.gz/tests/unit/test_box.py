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

from flyer_composer import Box, mm
from flyer_composer.cli import __parse_box as parse_box


def test_box_init():
    box = Box(parse_box('a4'))
    for k, v in (
            ('width', 210*mm),
            ('height', 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v

    box = Box(parse_box('tabloid'))
    for k, v in (
            ('width', 792),
            ('height', 1224),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'tabloid'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v


def test_box_from_papersize():
    box = Box.from_papersize('a4')
    for k, v in (
            ('width', 210*mm),
            ('height', 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v

    box = Box.from_papersize('tabloid')
    for k, v in (
            ('width', 792),
            ('height', 1224),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'tabloid'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v


def test_box_copy():
    box1 = Box(parse_box('a4'))
    assert isinstance(box1, Box)
    box2 = box1.copy()
    assert isinstance(box2, Box)
    assert box1 == box2


def test_rotate():
    box = Box(parse_box('a4'))
    box.rotate()
    for k, v in (
            ('width', 297*mm),
            ('height', 210*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v
    box.rotate()
    for k, v in (
            ('width', 210*mm),
            ('height', 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v


def test_is_landscape():
    box = Box(parse_box('a4'))
    assert not box.is_landscape
    box.rotate()
    assert box.is_landscape
    box.rotate()
    assert not box.is_landscape


def test_ensure_portrait():
    box = Box(parse_box('a4'))
    box.rotate()
    assert box.is_landscape
    box.ensure_portrait()
    assert not box.is_landscape
