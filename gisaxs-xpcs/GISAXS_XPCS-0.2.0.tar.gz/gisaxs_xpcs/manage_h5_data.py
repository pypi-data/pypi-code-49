#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from pathlib import Path

import numpy as np
import h5py
from tqdm import tqdm

from .common_tools import get_zaptime_files, save_create, measure_speed
from .read_edf import read_edf_gz
from .gisaxs_parameters import GisaxsParameters

__all__ = ['h5_manager']


class H5PathNotProvidedError(ValueError):
    """
    Please, set h5 _path first.
    """
    pass


class H5PathIsNotAFileError(ValueError):
    """
    Please, check the h5 file _path you provided.
    """
    pass


class ParentDirNotExistsError(ValueError):
    """
    The path is invalid. Please, provide a path to an existing folder.
    """


class H5Manager(object):
    @property
    def path(self):
        return self._path

    @property
    def xpcs_path(self):
        return self._xpcs_path

    def __init__(self, path: str = None, xpcs_path: str = None):
        self._path = path
        self._xpcs_path = xpcs_path

    def add_files(self, zaptime_number: List[int] or int):
        if not self._path:
            raise H5PathNotProvidedError()
        with h5py.File(self._path, 'a') as h5file:
            add_raw_data_to_h5(h5file, zaptime_number,
                               save_axes=True)

    def delete_files(self, zaptime_number: List[int] or int):
        if not self._path:
            raise H5PathNotProvidedError()
        with h5py.File(self._path, 'a') as h5file:
            delete_data_from_h5(h5file, zaptime_number)

    def set_path(self, path: str or Path):
        if isinstance(path, str):
            path = Path(path)
        if not path.is_file():
            raise H5PathIsNotAFileError()
        self._path = path

    def set_xpcs_path(self, xpcs_path: str or Path):
        if isinstance(xpcs_path, str):
            xpcs_path = Path(xpcs_path)
        if not xpcs_path.is_file():
            if xpcs_path.parent.is_dir():
                with h5py.File(xpcs_path, 'w'):
                    pass
            else:
                raise ParentDirNotExistsError()
        self._xpcs_path = xpcs_path


@measure_speed('Adding raw data to h5 file')
def add_raw_data_to_h5(h5file: h5py.File, zaptime_number: List[int] or int, *,
                       save_axes: bool = True, rewrite: bool = False) -> None:
    """
    Adds raw data from zaptime folder on groupshare with chosen number to the target h5 file.
    If save_axes is True, it adds axes as datasets and creates reference in attrs dict.

    :param h5file: target h5 file
    :param zaptime_number: target zaptime folder number
    :param save_axes: (optional) if True, saves axes as datasets to h5 file.
    :param rewrite: (optional) if True, allows to rewrite existing groups in h5file.
    :return: None
    """
    if isinstance(zaptime_number, list):
        for num in zaptime_number:
            add_raw_data_to_h5(h5file, num, save_axes=save_axes, rewrite=rewrite)
    else:
        print('Folder number ', zaptime_number)
        gp = GisaxsParameters.init_from_folder_number(zaptime_number)
        if save_axes:
            x_axis, y_axis = gp.get_angle_vectors(units='deg', flip=False)
        else:
            x_axis = y_axis = None
        zaptime_files = get_zaptime_files(zaptime_number)
        if zaptime_files:
            raw_data_group = save_create(h5file, 'Raw data')
            current_group_name = '_'.join(['zaptime', str(zaptime_number).zfill(2)])
            if current_group_name in list(raw_data_group.keys()) and not rewrite:
                print('Current folder already exists')
                return
            current_group = save_create(raw_data_group, current_group_name)
            if x_axis is not None and y_axis is not None:
                x_axis_dset = current_group.create_dataset('x_axis', data=x_axis)
                y_axis_dset = current_group.create_dataset('y_axis', data=y_axis)
            else:
                x_axis_dset = y_axis_dset = None
            for i, gz_file in enumerate(tqdm(zaptime_files)):
                try:
                    data, header_dict = read_edf_gz(gz_file)
                    data = np.flip(data, axis=1)
                    dset = current_group.create_dataset(str(i).zfill(len(str(len(zaptime_files)))), data=data)
                    dset.attrs.update(header_dict)
                    if x_axis_dset is not None and y_axis_dset is not None:
                        dset.attrs.update({'x_axis': x_axis_dset.ref, 'y_axis': y_axis_dset.ref})
                except Exception as err:
                    print(err)


@measure_speed('Delete data from h5')
def delete_data_from_h5(h5file: h5py.File, zaptime_number: List[int] or int):
    if isinstance(zaptime_number, list):
        for num in zaptime_number:
            delete_data_from_h5(h5file, num)
    else:
        if 'Raw data' not in h5file.keys():
            print('Raw data not found!')
            return
        else:
            group = h5file['Raw data']
            current_group_name = '_'.join(['zaptime', str(zaptime_number).zfill(2)])
            if current_group_name not in group.keys():
                print(f'Zaptime folder {zaptime_number} not found.')
                return
            else:
                del group[current_group_name]


h5_manager = H5Manager()

if __name__ == '__main__':
    folder_number = 76
    path = '/media/vladimir/data/GISAXS_DATA/test_raw_data.h5'
    with h5py.File(path, 'a') as h5file:
        add_raw_data_to_h5(h5file, folder_number)
        # delete_data_from_h5(h5file, list(range(76)))
