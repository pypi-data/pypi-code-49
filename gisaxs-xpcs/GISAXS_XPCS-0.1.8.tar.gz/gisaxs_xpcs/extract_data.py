#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contains ExtractData class which allows to extract and process data
from the remote server and .h5 files
(images data, plots, movies, metadata)
"""

from typing import List, Tuple, Union, Optional
import warnings

import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

from gisaxs_xpcs.common_tools import get_zaptime_files, get_pen_folder_number
from gisaxs_xpcs.read_edf import read_edf_gz
from gisaxs_xpcs.gisaxs_parameters import GisaxsParameters
from gisaxs_xpcs.metadata_obj import MetaData

rc('text', usetex=True)
rc('xtick', labelsize=12)
rc('ytick', labelsize=12)
rc('axes', labelsize=14)


class ExtractData(object):
    def __init__(self, *,
                 default_background: float = 0.01,
                 metadata: MetaData = None):

        self.default_background = default_background
        self.metadata = metadata or MetaData()

    @staticmethod
    def zaptime_info(folder_num: int):
        return 'Number of files = %d' % len(get_zaptime_files(folder_num))

    # @measure_speed('Getting images ... ')
    def get_images(self, folder_num: int, num: Optional[Union[int, list]] = None, *,
                   plot: bool = False,
                   apply_log: bool = False,
                   background: float = None,
                   x_range: tuple = (-0.1, 0.1),
                   y_range: tuple = (0., 0.4),
                   gp: GisaxsParameters = None,
                   vmin: float = None,
                   vmax: float = None,
                   get_properties: bool = False,
                   save: bool = False,
                   title: Optional[str] = None,
                   show: bool = True) -> DataFrame or List[DataFrame]:

        background = background or self.default_background
        gp = gp or GisaxsParameters.init_from_folder_number(folder_num)
        files = get_zaptime_files(folder_num)
        if num is None:
            num = list(range(len(files)))
        if isinstance(num, list):
            x_angles, y_angles = gp.get_angle_vectors(units='deg', flip=False)
            res = []
            for n in num:
                df = self.get_df_from_data(read_edf_gz(files[n])[0], self.get_name(folder_num, n),
                                           apply_log,
                                           background, x_range, y_range, gp,
                                           x_angles, y_angles)
                if get_properties:
                    df.attrs.update(self.metadata.get_image_properties(folder_num, n, return_dict=True))
                if plot or save:
                    self._plot_image(df, vmin, vmax, show=show, save=save, title=title, folder_num=folder_num, num=n)
                res.append(df)
            return res
        else:
            file_ = files[num] if files and len(files) > num + 1 else None
            if not file_:
                raise ValueError('num = %d is bigger than number of files = %d' % (num, len(files)))
            data, header_dict = read_edf_gz(files[num])
            df = self.get_df_from_data(data, self.get_name(folder_num, num),
                                       apply_log, background, x_range, y_range, gp)
            if plot or save:
                self._plot_image(df, vmin, vmax, show=show, save=save, title=title,
                                 folder_num=folder_num, num=num)
            if get_properties:
                df.attrs.update(self.metadata.get_image_properties(folder_num, num))
            return df

    @staticmethod
    def get_name(folder_num: int, num: int) -> str:
        return 'image_%d_%d' % (folder_num, num)

    @staticmethod
    def get_df_from_data(data, name: str, apply_log: bool, background: float,
                         x_range: tuple, y_range: tuple, gp: GisaxsParameters,
                         x_angles: np.array = None, y_angles: np.array = None) -> DataFrame:
        if x_angles is None or y_angles is None:
            x_angles, y_angles = gp.get_angle_vectors(units='deg', flip=False)
            x_angles = np.flip(x_angles, axis=0)
        df = DataFrame(np.flip(np.clip(data, background, np.amax(data)), axis=1),
                       columns=x_angles, index=y_angles)
        df = df.iloc[(df.index >= y_range[0]) * (df.index <= y_range[1]),
                     (df.columns >= x_range[0]) * (df.columns <= x_range[1])]
        if apply_log:
            df = np.log(df)
        df.name = name
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            df.attrs = dict()
        return df

    # def _str_from_attrs(self, attrs: dict) -> str:
    #     def _chech_class(value) -> float:
    #         if not isinstance(value, float):
    #             return value.value
    #         else:
    #             return value
    #     props = 0

    def _plot_image(self, df: DataFrame, vmin: float = None, vmax: float = None,
                    save: bool = False, path: str = None, title: str = None,
                    folder_num: int = None, num: int = None, extent_: tuple = None,
                    show: bool = True):

        fig, ax = plt.subplots()
        extent_ = extent_ or self.get_extent(df)
        p = ax.imshow(df, extent=extent_,
                      vmin=vmin,
                      vmax=vmax,
                      cmap='jet')
        if folder_num and num:
            if title is None:
                title = 'Pentacene sample %d' % get_pen_folder_number(folder_num)
            try:
                title = '%s%s(folder %d, image %d)' % (
                    title,
                    self.metadata.get_latex_title(folder_num, num),
                    folder_num, num)
            except Exception as err:
                print(err)
            plt.title(title)
        ax.set_xlabel(r'$2 \theta$, deg')
        ax.set_ylabel(r'$\alpha$, deg')
        plt.colorbar(p, ax=ax)
        if save:
            path = path or '%s.png' % df.name
            plt.savefig(path)
        elif show:
            plt.show()
        return p

    @staticmethod
    def get_extent(df, numbers: int = 2):
        return (round(df.columns.min(), numbers),
                round(df.columns.max(), numbers),
                round(df.index.min(), numbers),
                round(df.index.max(), numbers),)

    def make_video(self, folder_num: int, *, background: float = 0.1,
                   x_range: tuple = (-0.1, 0.1), y_range: tuple = (0., 0.4),
                   vmin: float = None, vmax: float = None, apply_log=True,
                   number_of_frames: int = 100,
                   interval: int = 200, title: str = None) -> None:

        files = get_zaptime_files(folder_num)

        def df_list(num: int) -> DataFrame:
            return self.get_images(folder_num, num, apply_log=apply_log, background=background,
                                   x_range=x_range, y_range=y_range)

        print('%d frames found ' % len(files))
        if len(files) == 0:
            return

        number_of_frames = number_of_frames or len(files)
        number_of_frames = min([number_of_frames, len(files)])

        delta_frame = int(len(files) / number_of_frames)

        extent_ = self.get_extent(df_list(0))

        fig = plt.figure()
        if title is None:
            title = 'Pentacene sample %d' % get_pen_folder_number(folder_num)

        def update_imshow(num):
            num = num * delta_frame if num * delta_frame < len(files) else len(files) - 1
            print(num)
            p = plt.imshow(df_list(num), vmin=vmin, vmax=vmax, extent=extent_)
            ax = plt.gca()
            ax.set_xlabel(r'$2 \theta$, deg')
            ax.set_ylabel(r'$\alpha$, deg')
            if not update_imshow.colorbar_is_set:
                plt.colorbar()
                update_imshow.colorbar_is_set = True
            plt.title('%s%s(folder %d, image %d)' % (
                title,
                self.metadata.get_latex_title(folder_num, num),
                folder_num, num))
            return p,

        update_imshow.colorbar_is_set = False
        ani = animation.FuncAnimation(fig, update_imshow, number_of_frames,
                                      interval=interval, blit=True)

        ani.save('movie_%d.mp4' % folder_num)


def get_time_axis(files: List[Tuple[int, int]]):
    def func(n):
        try:
            return MetaData().get_image_properties(*n)['abs_time']
        except KeyError as err:
            print('Folder, file : ', n)
            raise KeyError(err)

    start = func(files[0])
    return [func(n) - start for n in files]


def get_temp_axis(files: List[Tuple[int, int]], key='temp_sample'):
    def func(n):
        try:
            return MetaData().get_image_properties(*n)[key].value
        except KeyError as err:
            print('Folder, file : ', n)
            raise KeyError(err)

    return [func(n) for n in files]


if __name__ == '__main__':
    from pprint import pprint

    extract_data = ExtractData()
    folder_number = 99
    print(extract_data.zaptime_info(folder_number))
    ims = extract_data.get_images(folder_number, [1], background=1,
                                  apply_log=True, plot=True, get_properties=True,
                                  save=False)
    for im in ims:
        pprint(im.attrs)

    # extract_data.make_video(97, number_of_frames=100, title='Pentacene sample 5, annealing')
