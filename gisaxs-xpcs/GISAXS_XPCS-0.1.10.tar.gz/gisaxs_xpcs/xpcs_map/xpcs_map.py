# -*- coding: utf-8 -*-

from typing import (Tuple, Iterable, Union,
                    List, Callable, Dict)

import numpy as np
from scipy.ndimage import zoom
from h5py import File
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from ..manage_h5_data import h5_manager
from ..extract_data import ExtractData

from .xpcs import XPCS
from .region_grid import (RegionGrid, RGridParams,
                          RListParams, RegionType, r_params_from_dict)

GeneratorType = Iterable[Tuple[np.ndarray, RegionType]]


class XPCSMap(object):
    @property
    def parameters(self) -> Union[RListParams, RGridParams]:
        return self.region_grid.parameters

    @staticmethod
    def _default_xpcs_map_h5_group_name(folder_num: int) -> str:
        return 'zaptime_%d' % folder_num

    @classmethod
    def init_from_file(cls, folder_num: int, name: str = 'xpcs_map'):
        return _init_xpcs_map_from_file(folder_num, name)

    def __init__(self, folder_num: int,
                 region_grid: RegionGrid,
                 mask: RegionType = None,
                 name: str = 'xpcs_map'):
        self.folder_num = folder_num
        self.region_grid = region_grid
        self.name = name
        self.xpcs = XPCS(folder_num, mask=mask)

    def get_time_axis(self):
        _, t_array = self.xpcs.get_intensities()
        return t_array

    def set_name(self, name: str) -> None:
        self.name = name

    def generate_2d_corr(self, mode: str = 'std') -> GeneratorType:
        for region in self.region_grid:
            self.xpcs.set_region(region)
            corr, _ = self.xpcs.get_two_time_corr_function(mode)
            yield corr, region

    def generate_1d_corr(self) -> GeneratorType:
        for region in self.region_grid:
            self.xpcs.set_region(region)
            corr, _ = self.xpcs.get_one_time_corr_function()
            yield corr, region

    def get_one_2d_corr_from_file(self, region: RegionType):
        res = _get_regions_from_h5(self.folder_num, self.name, [region])
        try:
            return res[region]
        except KeyError:
            raise ValueError(f'Region {region} not found in saved xpcs.')

    def save_2d_corr(self, mode: str = 'std') -> None:
        _save_to_h5(self.name, self.folder_num,
                    self.generate_2d_corr(mode), self.parameters)

    def generate_from_file(self) -> GeneratorType:
        return _read_from_h5(self.folder_num, self.name)

    def plot_grid(self, file_num: int = 0, **kwargs) -> None:
        extract_data = ExtractData()
        extract_data.get_images(
            self.folder_num, file_num, apply_log=True, plot=True,
            show=False, gp=self.xpcs.gp, x_range=(-10, 10), y_range=(-10, 10)
        )

        ax = plt.gca()
        for cut in self.region_grid:
            ax.add_patch(_get_rect(cut, **kwargs))

        plt.show()

    def plot_from_file(self, figname: str = None,
                       figsize: Tuple[int, int] = None,
                       reduce_factor: float = None,
                       reduce_mode: str = 'nearest') -> None:
        generator = self.generate_from_file()
        _plot_r(generator, self.parameters,
                reduce_factor, reduce_mode, figsize)
        if figname:
            plt.savefig(figname)
        else:
            plt.show()


def _plot_r(generator: GeneratorType, parameters: RGridParams or RListParams,
            reduce_factor: float = None,
            reduce_mode: str = 'nearest',
            figsize: Tuple[int, int] = None) -> None:
    if isinstance(parameters, RGridParams):
        return _plot_all_grid(generator, parameters, reduce_factor,
                              reduce_mode, figsize)
    elif isinstance(parameters, RListParams):
        return _plot_all_list(generator, parameters, reduce_factor,
                              reduce_mode, figsize)
    else:
        raise TypeError(f'Parameters have unexpected type {type(parameters)}.')


def _plot_all_grid(generator: GeneratorType, parameters: RGridParams,
                   reduce_factor: float = None,
                   reduce_mode: str = 'nearest',
                   figsize: Tuple[int, int] = None) -> None:
    ny, nx = parameters.xy_size

    figsize = figsize or (nx, ny)
    fig, axs = plt.subplots(nrows=ny, ncols=nx, sharex=True, figsize=figsize)
    axs = np.flip(axs, axis=0).flatten()

    for i, (ax, (res, cut)) in enumerate(tqdm(zip(axs, generator))):
        if reduce_factor:
            res = zoom(res, reduce_factor, mode=reduce_mode)
        _imshow(ax, res)
        if i % nx == 0:
            _set_y_label(ax, cut)
        if i < nx:
            _set_x_label(ax, cut)

    plt.subplots_adjust(wspace=0, hspace=0)


def _plot_all_list(generator: GeneratorType, parameters: RListParams,
                   reduce_factor: float = None,
                   reduce_mode: str = 'nearest',
                   figsize: Tuple[int, int] = None) -> None:
    n = parameters.number_of_cuts
    axis_ind = parameters.axis
    if axis_ind == 0:
        nx, ny = n, 1
    else:
        nx, ny = 1, n

    figsize = figsize or (nx, ny)
    fig, axs = plt.subplots(nrows=ny, ncols=nx, figsize=figsize)

    for i, (ax, (res, cut)) in enumerate(tqdm(zip(axs, generator))):
        if reduce_factor:
            res = zoom(res, reduce_factor, mode=reduce_mode)
        _imshow(ax, res)
        if i == 0 and axis_ind == 0:
            _set_y_label(ax, cut)
        if i == len(axs) - 1 and axis_ind == 1:
            _set_x_label(ax, cut)
        if axis_ind == 0:
            _set_x_label(ax, cut)
        else:
            _set_y_label(ax, cut)

    plt.subplots_adjust(wspace=0, hspace=0)


def _imshow(ax, res) -> None:
    ax.imshow(res, cmap='jet', origin=True)
    ax.set_xticks([], [])
    ax.set_yticks([], [])


def _set_x_label(ax: plt.Axes, cut: RegionType) -> None:
    ax.set_xlabel(str((cut[2] + cut[3]) / 2)[:5])


def _set_y_label(ax: plt.Axes, cut: RegionType) -> None:
    ax.set_ylabel(str((cut[0] + cut[1]) / 2)[:5])


def _get_rect(region: RegionType, **kwargs) -> patches.Rectangle:
    return patches.Rectangle((region[2], region[0]), region[3] - region[2], region[1] - region[0],
                             fill=False, color='red', **kwargs)


def _save_to_h5(name: str, folder_number: int,
                generator: GeneratorType,
                parameters: Union[RGridParams, RListParams],
                mask: RegionType = None) -> None:
    h5_path = h5_manager.xpcs_path
    if h5_path is None:
        raise ValueError('The path to xpcs h5 file is not set.')

    with File(h5_path, 'a') as f:
        if str(folder_number) not in f.keys():
            folder = f.create_group(str(folder_number))
        else:
            folder = f[str(folder_number)]
        if name in folder:
            del folder[name]
        group = folder.create_group(name)
        group.attrs.update(parameters.dict)
        if mask is not None:
            group.create_dataset('mask', data=mask)

    for i, (data, region) in enumerate(tqdm(generator)):
        with File(h5_path, 'a') as f:
            group = f[str(folder_number)][name]
            dset = group.create_dataset(str(i), data=data)
            dset.attrs['region'] = region


def _read_from_h5(folder_number: int, name: str) -> GeneratorType:
    h5_path = _get_xpcs_path()
    with File(h5_path, 'a') as f:
        group = _get_group(f, folder_number, name)
        group_keys = [k for k in group.keys() if k != 'mask']
        group_keys.sort(key=lambda x: int(x))

    def func(i: int) -> Tuple[np.ndarray, RegionType]:
        # open/close the file every time might seem a bad idea
        # however, usually it is even faster and definitely safer when using from generator
        with File(h5_path, 'a') as f_:
            group_ = f_[str(folder_number)][name]
            try:
                dset = group_[str(i)]
                region = dset.attrs.get('region', None)
                data = dset[()]
                return data, region
            except KeyError:
                raise KeyError(f'Index {i} not found.')

    yield from (func(k) for k in group_keys)


def _get_regions_from_h5(folder_number: int, name: str,
                         regions: List[RegionType]) -> Dict[RegionType, np.ndarray]:
    data_dict = dict()
    with File(_get_xpcs_path(), 'a') as f:
        group = _get_group(f, folder_number, name)
        for k in group.keys():
            if k == 'mask':
                continue
            dset = group[k]
            region = tuple(dset.attrs.get('region', None))
            if region in regions:
                data_dict[region] = dset[()]
            if len(data_dict) == len(regions):
                break
        return data_dict


def _init_xpcs_map_from_file(folder_number: int, name: str):
    with File(_get_xpcs_path(), 'a') as f:
        group = _get_group(f, folder_number, name)
        param_dict = group.attrs
        try:
            mask = tuple(group['mask'])
        except (KeyError, RuntimeError, TypeError):
            mask = None

        region_grid = RegionGrid.init_from_parameters_dict(param_dict)
        return XPCSMap(folder_number, region_grid, mask, name)


def _get_parameters_from_file(folder_number: int, name: str) -> Union[RGridParams, RListParams]:
    with File(_get_xpcs_path(), 'a') as f:
        group = _get_group(f, folder_number, name)
        param_dict = group.attrs
        return r_params_from_dict(param_dict)


def _get_group(f: File, folder_number: int, name: str):
    if str(folder_number) not in f.keys():
        raise ValueError(f'Folder number {folder_number} is not found.')
    folder = f[str(folder_number)]
    if name not in folder.keys():
        raise ValueError(f'Group {name} is not found.')
    return folder[name]


def _get_xpcs_path():
    h5_path = h5_manager.xpcs_path
    if h5_path is None:
        raise ValueError('The path to xpcs h5 file is not set.')
    return h5_path
