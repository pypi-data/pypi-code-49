#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    types.py: This python script implements util Classes and functions 
    for the type parameter in argparse arguments.
"""


# standard library(ies)
import argparse
import pathlib


class Path(object):

    def __init__(self, exists: bool = True, mode: str = 'folder', dash_ok: bool = False) -> None:
        '''
            exists:
                True: a path that does exist
                False: a path that does not exist, in a valid parent directory
                None: don't care
           type: file, folder, symlink, None, or a function returning True for
                    valid paths
                None: don't care
           dash_ok: whether to allow "-" as stdin/stdout
        '''
        assert exists in (True, False, None)
        assert mode in ('file', 'folder', 'symlink',
                        None) or hasattr(mode, '__call__')
        self._exists = exists
        self._mode = mode
        self._dash_ok = dash_ok


    def __call__(self, path: str) -> pathlib.Path:
        if path == '-':
            # the special argument "-" means sys.std{in,out}
            if self._mode == 'folder':
                msg = 'as directory path'
            elif self._mode == 'symlink':
                msg = 'as symlink path'
            elif not self._dash_ok:
                msg = ''
            raise argparse.ArgumentTypeError(
                'standard input/output (-) not allowed {msg}')
        path = pathlib.Path(path)
        if self._exists == True:
            if not path.exists():
                raise argparse.ArgumentTypeError(
                    f"path does not exist: '{path}'")
            if self._mode is None:
                pass
            elif self._mode == 'file':
                if not path.is_file():
                    raise argparse.ArgumentTypeError(
                        f"path is not a file: '{path}'")
            elif self._mode == 'symlink':
                if not path.is_symlink():
                    raise argparse.ArgumentTypeError(
                        f"path is not a symlink: '{path}'")
            elif self._mode == 'folder':
                if not path.is_dir():
                    raise argparse.ArgumentTypeError(
                        f"path is not a directory: '{path}'")
            elif not self._mode(path):
                raise argparse.ArgumentTypeError(
                    f"path not valid: '{path}'")
        else:
            if self._exists == False and path.exists():
                raise argparse.ArgumentTypeError(
                    f"path exists: '{path}'")
            if not path.parent.is_dir():
                raise argparse.ArgumentTypeError(
                    f"parent path is not a directory: '{path.parent}'")
            elif not path.parent.exists():
                raise argparse.ArgumentTypeError(
                    f"parent directory does not exist: '{path.parent}'")
        return path


def positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            f'{value} is not a positive integer value.')
    return ivalue


def non_negative_int(value: str) -> int:
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(
            f'{value} is a negative integer value.')
    return ivalue
