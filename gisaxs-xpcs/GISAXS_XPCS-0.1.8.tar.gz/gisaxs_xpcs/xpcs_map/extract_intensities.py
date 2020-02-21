# -*- coding: utf-8 -*-
import re
from typing import Union, Tuple
from pathlib import Path

from h5py import File, Group
import numpy as np
from numpy import ndarray

__all__ = ['get_intensities']


def get_intensities(h5file: Union[File, Group, Path, str],
                    mask: ndarray, group_key: str = None,
                    time_key: str = 'time_of_frame') -> Tuple[ndarray, ndarray]:
    if isinstance(h5file, (File, Group)):
        return _get_intensities_from_file(h5file, mask, group_key, time_key)
    elif isinstance(h5file, str):
        path = Path(h5file)
    elif isinstance(h5file, Path):
        path = h5file
    else:
        raise TypeError(f'h5file should be Union[File, Group, Path, str] type,'
                        f'provided {type(h5file)} instead.')
    if not path.is_file():
        raise FileNotFoundError(f'File {h5file} not found.')
    with File(path, 'r') as f:
        return _get_intensities_from_file(f, mask, group_key, time_key)


_DIGITS_PATTERN = r'^([\s\d]+)$'


def _get_intensities_from_file(f: File, mask: ndarray,
                               group_key: str = None,
                               time_key: str = 'time_of_frame') -> Tuple[ndarray, ndarray]:
    if group_key:
        f = f[group_key]
    if mask.dtype != bool:
        raise TypeError(f'Mask dtype should be bool, provided {mask.dtype}')

    dset_keys = [k for k in f.keys() if re.search(_DIGITS_PATTERN, k)]
    dset_sorted_keys = sorted(dset_keys, key=lambda x: int(x))
    time_size = len(dset_sorted_keys)
    intensity_array = np.empty((time_size, np.sum(mask)))
    t_array = np.empty(time_size)

    for dset_number, dset_name in enumerate(dset_sorted_keys):
        dataset = f[dset_name]
        # if dataset.shape != mask.shape:
        #     raise ValueError(f'Mask shape is wrong: {dataset.shape} != {mask.shape}.')
        intensity = dataset[mask]
        intensity_array[dset_number, :] = intensity
        t_array[dset_number] = dataset.attrs.get(time_key, dset_number)
    return intensity_array, t_array
