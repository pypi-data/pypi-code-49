# -*- coding: utf-8 -*-
import pytest
import numpy as np

from gisaxs_xpcs import XPCS


def test_get_intensities(folder, region):
    xpcs = XPCS(folder, region)
    intensity, t_array = xpcs.get_intensities()
    assert intensity.shape[0] == t_array.size


def test_mask(folder):
    region = (-10, 10, -10, 10)
    xpcs = XPCS(folder, region)
    mask_size = xpcs.mask.shape[0] * xpcs.mask.shape[1]
    assert np.sum(xpcs.mask) == mask_size


def test_2d_corr(folder, region):
    xpcs = XPCS(folder, region)
    corr, t_array = xpcs.get_two_time_corr_function()
    assert corr.shape == (t_array.size, t_array.size)
