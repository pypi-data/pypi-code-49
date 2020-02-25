#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import logging
from typing import Tuple

import numpy as np
import h5py

from ..gisaxs_parameters import GisaxsParameters
from ..manage_h5_data import h5_manager

from .calculate_xpcs import calculate_1d_corr, calculate_2d_corr, XPCSModes
from .extract_intensities import get_intensities
from .region_grid import RegionType

logger = logging.getLogger(__name__)


class XPCS(object):
    """
        Class provides the basic functionality to calculate
        two-time correlation functions for
        GISAXS images stored to .h5 file.
    """

    @staticmethod
    def _default_h5_path(folder_num: int):
        return '/'.join(['Raw data', 'zaptime_%s' % str(folder_num).zfill(2)])

    def __init__(self, folder_num: int = None,
                 cut_region: RegionType = None,
                 gp: GisaxsParameters = None,
                 h5_filepath: str = None,
                 h5_path: str = None,
                 mask: RegionType = None):
        """

        :param folder_num: number of the zaptime folder to analyse
        :param cut_region: tuple(x_min, x_max, y_min, y_max) in [deg]
        :param gp: gisaxs parameters object (necessary to extract angles)
        :param h5_filepath: _path to the data source
        :param h5_path: _path to zaptime folder in h5 file
        """
        if not folder_num and not h5_filepath:
            raise ValueError('Either folder_num or h5_filename should be provided')
        self.folder_num = folder_num
        self._index_x = self._index_y = None
        self._mask_x = self._mask_y = None
        self._bool_mask = None
        if not gp and folder_num:
            self.gp = GisaxsParameters.init_from_folder_number(folder_num)
        else:
            self.gp = gp or GisaxsParameters()
        self._cut_region = cut_region
        self._mask = mask
        self.h5_filepath = h5_filepath or h5_manager.path
        self.h5_path = h5_path or self._default_h5_path(self.folder_num)
        if not self._setup_h5():
            raise NotImplementedError('Reading from remote folder is not'
                                      ' implemented yet.')

        self.xx, self.yy = self._init_mask_coords()

        self._update_mask()

    @property
    def mask(self):
        return self._bool_mask

    @property
    def region(self):
        return self._cut_region

    @property
    def status(self) -> bool:
        return self.mask is not None

    def set_region(self, cut_region: RegionType):
        self._cut_region = cut_region
        self._update_mask()

    def set_mask(self, mask: RegionType):
        self._mask = mask
        self._update_mask()

    def get_two_time_corr_function(self, mode: str = 'std') -> Tuple[np.ndarray, np.ndarray]:
        if not self.status:
            raise ValueError('Cut region should be provided.')
        if mode == 'mean':
            mode = XPCSModes.mean
        elif mode == 'std':
            mode = XPCSModes.std
        else:
            raise ValueError(f'Mode should be "std" or "mean", {mode} provided.')
        intensity, time_array = self.get_intensities()
        return calculate_2d_corr(intensity, mode), time_array

    def get_one_time_corr_function(self) -> Tuple[np.ndarray, np.ndarray]:
        if not self.status:
            raise ValueError('Cut region should be provided.')
        intensity, time_array = self.get_intensities()
        return calculate_1d_corr(intensity), time_array

    def get_intensities(self) -> Tuple[np.ndarray, np.ndarray]:
        return get_intensities(self.h5_filepath, self.mask, self.h5_path)

    def _setup_h5(self) -> bool:
        """
        Checks .h5 file. If it exists and contains the provided _path to the dataset,
        returns True, otherwise False.
        """
        if not os.path.isfile(self.h5_filepath):
            logger.error('File %s doesn\'t exist.' % self.h5_filepath)
            return False
        try:
            with h5py.File(self.h5_filepath, 'r') as f:
                if f.get(self.h5_path, None) is None:
                    logger.error('File does not contain _path %s' % self.h5_path)
                    return False
                # data = f[self.h5_path][list(f[self.h5_path].keys())[0]][()]
                # print(data.shape)
        except Exception as err:
            logger.exception(err)
            return False
        return True

    def _init_mask_coords(self):
        x_angles, y_angles = self.gp.get_angle_vectors(units='deg',
                                                       flip=False)
        x, y = np.sort(x_angles), np.flip(np.sort(y_angles), axis=0)
        return np.meshgrid(x, y)

    def _update_mask(self) -> None:
        if not self._cut_region:
            mask = np.ones_like(self.xx, dtype=bool)
        else:
            mask = self._get_mask(self._cut_region)
        if self._mask is not None:
            mask = mask & self.beam_stop_mask
        self._bool_mask = mask

    @property
    def beam_stop_mask(self):
        if self._mask is not None:
            return np.logical_not(self._get_mask(self._mask))
        else:
            return np.ones_like(self.xx, dtype=bool)

    def _get_mask(self, region: RegionType):
        return (self.xx > region[2]) & (self.xx < region[3]) & (self.yy > region[0]) * (self.yy < region[1])
