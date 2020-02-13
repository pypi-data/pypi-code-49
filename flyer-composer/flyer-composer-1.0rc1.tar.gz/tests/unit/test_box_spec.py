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
import re
import argparse

from flyer_composer import mm
from flyer_composer.cli import __parse_box as parse_box

ArgParserError = argparse.ArgumentTypeError


def test_papersize_abbreviation():
    box = parse_box('1x1let')
    assert box['unit'] == 'letter'
    box = parse_box('1x1envdin')
    assert box['unit'] == 'envdinlang'


def test_ambiguous_papersize_abbreviation_raises():
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('1x1a')
    assert re.search("papersize name .* is not unique", excinfo.value.args[0])


def test_unknown_papersize_raises():
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('1x2yyy')
    assert "I don't understand your papersize name" in excinfo.value.args[0]
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('1x2xxx')
    assert "I don't understand your papersize name" in excinfo.value.args[0]


def test_wrong_box_definition_raises():
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('2yyy')
    assert "I don't understand your box specification" in excinfo.value.args[0]
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('2xxx')
    assert "I don't understand your box specification" in excinfo.value.args[0]


def test_disallowed_offset_raises():
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('1x1+10,10a4')
    assert "Offset not allowed in box definition" in excinfo.value.args[0]
    # not even if zero
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('1x1+0,0a4')
    assert "Offset not allowed in box definition" in excinfo.value.args[0]


def test_missing_offset_raises():
    with pytest.raises(ArgParserError) as excinfo:
        parse_box('1x1+a4')
    assert "I don't understand your box specification" in excinfo.value.args[0]


def test_allowed_offset_does_not_raise():
    parse_box('1x1+10,10a4', allow_offset=True)
    parse_box('1x1+0,0a4', allow_offset=True)


def test_some_standard_papersizes():
    box = parse_box('1x1a4')
    for k, v in (
            ('width', 210*mm),
            ('height', 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v

    box = parse_box('a4')
    for k, v in (
            ('width', 210*mm),
            ('height', 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v

    box = parse_box('1x1tabloid')
    for k, v in (
            ('width', 792),
            ('height', 1224),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'tabloid'),
            ('units_x', 1),
            ('units_y', 1)):
        assert box[k] == v


def test_multiplier():
    box = parse_box('2x2a4')
    for k, v in (
            ('width', 2 * 210*mm),
            ('height', 2 * 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 2),
            ('units_y', 2)):
        assert box[k] == v

    box = parse_box('7.2x3.5a4')
    for k, v in (
            ('width', 7.2 * 210*mm),
            ('height', 3.5 * 297*mm),
            ('offset_x', 0),
            ('offset_y', 0),
            ('unit', 'a4'),
            ('units_x', 7.2),
            ('units_y', 3.5)):
        assert box[k] == v


def test_complex_box_specification():
    box = parse_box('7.3x3.7+1.5,0.3a4', allow_offset=True)
    for k, v in (
            ('width', 7.3 * 210*mm),
            ('height', 3.7 * 297*mm),
            ('offset_x', 1.5 * 210*mm),
            ('offset_y', 0.3 * 297*mm)):
        # accept a small precision error
        assert abs(box[k] - v) < 0.00001
    for k, v in (
            ('unit', 'a4'),
            ('units_x', 7.3),
            ('units_y', 3.7)):
        assert box[k] == v
