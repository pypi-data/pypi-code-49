#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Different non-specific tools widely used along the project.
"""

import time
import os
from typing import Optional, List
import logging
from pathlib import Path

from gisaxs_xpcs.read_edf import read_header_from_file

_DEFAULT_MONETA_DIR = '/home/vladimir/remote_folder/OMBD/'


class MonetaDirNotSetError(ValueError):
    """Please, set the correct _path to OMBD folder on moneta server. """
    pass


class WrongOMBDDirError(ValueError):
    """Please, check that the provided _path to OMBD folder is correct. """
    pass


class MonetaDir(object):
    def __init__(self):
        self.path = None

    def set_path(self, path: str):
        path = Path(path)
        if not path.is_dir():
            raise WrongOMBDDirError()
        self.path = path / 'xray' / 'beamtimes' / '2018_ESRF_SC4813_coherence' / 'id10' / 'data'

    def __call__(self, *args, **kwargs):
        if not self.path:
            raise MonetaDirNotSetError()
        return str(self.path)

    def _set_default_dir(self):
        self.set_path(_DEFAULT_MONETA_DIR)


MONETA_DIR = MonetaDir()


def measure_speed(title: Optional[str] = None):
    """
    Decorator function that prints time in sec spent on a target function
    :param title: title to print before time
    """
    title = title or 'Time counting'

    def decorator(func):
        def wrapper(*args, **kwargs):
            print('\n', '*' * 30, '\n')
            print(title)
            start = time.perf_counter()
            res = func(*args, **kwargs)
            end = time.perf_counter()
            print()
            print('Performed in %.4f sec' % float(end - start))
            return res

        return wrapper

    return decorator


def get_zaptime_files(zaptime_number: int, info: Optional[bool] = False) -> List[str]:
    """
    Looks for f'zaptime_{zaptime_number}' folder in MONETA groupshare
    and returns the list of all /*.edf.gz file paths inside the folder, sorted by file number.

    :param zaptime_number: number of target folder
    :param info: if True, prints number of files found
    :return: list of file paths
    """
    pen_folders = get_listdir(MONETA_DIR(), start_filter='PEN')
    zaptime_name = '_'.join(['zaptime', str(zaptime_number)])
    for p_folder in pen_folders:
        if zaptime_name in os.listdir(p_folder):
            files = get_listdir(os.path.join(p_folder, zaptime_name), end_filer='.edf.gz')
            files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
            if info:
                logging.info('Found %d files in %s folder' % (len(files), zaptime_name))
            return files
    else:
        print('Folder %s is not found in %s' % (zaptime_name, MONETA_DIR()))
        return []


def get_pen_folder_number(zaptime_number: int) -> Optional[int]:
    if zaptime_number > 86:
        return 5
    pen_folders = get_listdir(MONETA_DIR(), start_filter='PEN')
    pen_folders.sort(key=lambda x: int(x.split('PEN')[-1]))
    zaptime_name = '_'.join(['zaptime', str(zaptime_number)])
    for i, p_folder in enumerate(pen_folders):
        if zaptime_name in os.listdir(p_folder):
            return i + 1
    else:
        print('Folder %s is not found in %s' % (zaptime_name, MONETA_DIR()))
        return


def get_zaptime_file(zaptime_number: int, file_num: int) -> Optional[str]:
    """
    Looks for f'zaptime_{zaptime_number}' folder in MONETA groupshare
    and returns the _path of /*.edf.gz file with the corresponding number.

    :param zaptime_number: number of target folder
    :param file_num: number of target file
    :return: list of file paths
    """
    files = get_zaptime_files(zaptime_number)
    try:
        return files[file_num]
    except IndexError:
        logging.error('File number %d not found' % file_num)
        return


def get_listdir(dir_, *, start_filter: str = None, end_filer: str = None):
    """
    Lists files and folders in a target directory with optional name filters.
    :param dir_: target directory
    :type dir_: str
    :param start_filter:
    :param end_filer:
    :return:
    """
    start_filter = start_filter or ''
    end_filer = end_filer or ''
    if os.path.isdir(dir_):
        return [os.path.join(dir_, file_) for file_ in os.listdir(dir_)
                if file_.startswith(start_filter) and
                file_.endswith(end_filer)]
    else:
        raise NotADirectoryError('No such a directory: %s' % dir_)


def save_create(parent, group):
    """
    Creates group if doesn't exist and returns it

    :param parent: h5py.Group
    :param group: str
    :return: h5py.Group
    """
    if group not in list(parent.keys()):
        return parent.create_group(group)
    else:
        return parent[group]


def itersubclasses(cls, _seen=None):
    """
    itersubclasses(cls)

    Generator over all subclasses of a given class, in depth first order.

    """

    if not isinstance(cls, type):
        raise TypeError('itersubclasses must be called with '
                        'new-style classes, not %.100r' % cls)
    if _seen is None: _seen = set()
    try:
        subs = cls.__subclasses__()
    except TypeError:  # fails only when cls is type
        subs = cls.__subclasses__(cls)
    for sub in subs:
        if sub not in _seen:
            _seen.add(sub)
            yield sub
            for sub in itersubclasses(sub, _seen):
                yield sub


def get_image_header(folder_num: int, file_num: int) -> dict:
    """
    Returns edf header as a dict.
    :param folder_num: folder number
    :param file_num: file number
    :return: header dict
    """
    filepath = get_zaptime_file(folder_num, file_num)
    if filepath is None:
        raise FileNotFoundError('No file %d or folder %d found' % (file_num, folder_num))
    return read_header_from_file(filepath)


def setup_plot_fontsize(fontsize: int = 20,
                        bold: bool = True,
                        usetex: bool = True):
    import matplotlib as mpl
    from matplotlib import rc
    if bold:
        mpl.rcParams['text.latex.preamble'] = [r'\boldmath']
    if usetex:
        rc('text', usetex=True)

    rc('xtick', labelsize=fontsize)
    rc('ytick', labelsize=fontsize)
    rc('axes', labelsize=fontsize)
    rc('axes', titlesize=fontsize)
    rc('axes', titlesize=fontsize)
    rc('legend', fontsize=fontsize)
