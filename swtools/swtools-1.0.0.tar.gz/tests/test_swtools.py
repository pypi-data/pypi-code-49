#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `swtools` package."""

import pytest
import re

from swtools import swlookup

# regexes to test
frequency_regex = re.compile(r'^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$')
utc_regex = re.compile('^(0[0-9]|1[0-9]|2[0-3])[0-5][0-9]$')

# test the frequency regex with multiple values
@pytest.mark.parametrize('frequencies', [
    pytest.param('Abc', marks=pytest.mark.xfail),
    '26.5',
    '7335',
    '15770',
    '0',
])
def test_frequency_regex(frequencies):
    assert frequency_regex.match(frequencies) is not None

# test the UTC regex with multiple values
@pytest.mark.parametrize('utc', [
    pytest.param('0', marks=pytest.mark.xfail),
    pytest.param('00', marks=pytest.mark.xfail),
    pytest.param('000', marks=pytest.mark.xfail),
    '0000',
    pytest.param('010', marks=pytest.mark.xfail),
    pytest.param('2459', marks=pytest.mark.xfail),
    '2359',
])
def test_utc_regex(utc):
    assert utc_regex.match(utc) is not None
