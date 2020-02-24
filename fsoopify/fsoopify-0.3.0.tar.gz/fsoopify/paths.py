#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import os
import sys

from .utils import gettercache

NT = sys.platform == 'win32'

if NT:
    def _is_abspath(path: str):
        if os.path.isabs(path):
            return True
        rp = path.rpartition(':')
        if rp[0]:
            # path like 'c:' should be abspath
            return True
        return False

    def _get_normpath(path: str):
        val = str(path) # avoid recursion
        if val.endswith(':'):
            val += os.path.sep
        return os.path.normpath(os.path.normcase(val))

    def _join(path, *others):
        if not isinstance(path, str):
            raise TypeError
        if path.endswith(':'):
            path += os.path.sep
        return os.path.join(path, *others)

else:
    def _is_abspath(path: str):
        return os.path.isabs(path)

    def _get_normpath(path: str):
        val = str(path) # avoid recursion
        return os.path.normpath(os.path.normcase(val))

    def _join(path, *others):
        return os.path.join(path, *others)


class PathComponent(str):
    def __init__(self, *args):
        self._norm: str = None

    def __repr__(self):
        return '{}(\'{}\')'.format(type(self).__name__, self)

    def __eq__(self, other):
        if isinstance(other, PathComponent):
            return self.normalcase == other.normalcase
        if isinstance(other, str):
            return self.normalcase == _get_normpath(other)
        return False

    def __hash__(self):
        return hash(self.normalcase)

    @property
    @gettercache
    def normalcase(self):
        '''
        get normcase path which create by `os.path.normcase()`.
        '''
        return _get_normpath(self)


class Name(PathComponent):
    '''
    the name part of path.
    '''

    def __init__(self, val):
        super().__init__(val)
        self._pure_name = None
        self._ext = None

    def __ensure_pure_name(self):
        if self._pure_name is None:
            pn, ext = os.path.splitext(self)
            self._pure_name = PathComponent(pn)
            self._ext = PathComponent(ext)

    @property
    def pure_name(self) -> PathComponent:
        ''' get name without ext from path. '''
        self.__ensure_pure_name()
        return self._pure_name

    @property
    def ext(self) -> PathComponent:
        ''' get ext from path. '''
        self.__ensure_pure_name()
        return self._ext

    def replace_pure_name(self, val):
        if not isinstance(val, str):
            raise TypeError
        return Name(val + self.ext)

    def replace_ext(self, val):
        if not isinstance(val, str):
            raise TypeError
        return Name(self.pure_name + val)


class Path(PathComponent):
    join = staticmethod(_join)

    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError
        if cls is Path:
            if _is_abspath(value):
                cls = _AbsPath
            else:
                cls = _RelPath
        path = str.__new__(cls, value)
        return path

    def __init__(self, val):
        super().__init__(val)
        # sub attrs
        self._dirname = None
        self._name = None

    @staticmethod
    def from_cwd():
        ''' get `Path` from `os.getcwd()` '''
        return Path(os.getcwd())

    @staticmethod
    def from_home():
        ''' get `Path` from `os.path.expanduser("~")` '''
        return Path(os.path.expanduser("~"))

    @staticmethod
    def from_argv(index=0):
        ''' get `Path` from `sys.argv` by index '''
        return Path(sys.argv[index])

    @staticmethod
    def from_main_file():
        ''' get `Path` from the path of __main__ file '''
        try:
            module = sys.modules['__main__']
        except KeyError:
            raise RuntimeError('unable to find `__main__` module')
        return Path(module.__file__)

    @staticmethod
    def from_caller_file():
        ''' get `Path` from the path of caller file '''
        import inspect
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        filename = calframe[1].filename
        if not os.path.isfile(filename):
            raise RuntimeError('caller is not a file')
        return Path(filename)

    @staticmethod
    def from_caller_module_root():
        ''' get `Path` from module root which include the caller '''
        import inspect
        all_stack = list(inspect.stack())
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        module = inspect.getmodule(calframe[1].frame)
        if not module:
            raise RuntimeError('caller is not a module')
        root_module_name = module.__name__.partition('.')[0]
        fullpath = sys.modules[root_module_name].__file__
        return Path(fullpath)

    def __repr__(self):
        return 'Path(\'{}\')'.format(self)

    def __truediv__(self, right: str):
        if not isinstance(right, str):
            raise TypeError

        path = type(self)(self.join(self, right))
        dn, fn = os.path.split(right)
        if not dn:
            # if right did not contains sep,
            # fill attr on path to avoid make new one
            path._dirname = self
            path._name = Name(right)
        return path

    @property
    def dirname(self):
        '''
        get directory component from path.
        return `None` if no parent.
        '''
        self._init_dirname_attr()
        return self._dirname

    @property
    def name(self) -> Name:
        ''' get name component from path. '''
        self._init_dirname_attr()
        return self._name

    @property
    def pure_name(self) -> PathComponent:
        ''' get name without ext from path. '''
        return self.name.pure_name

    @property
    def ext(self) -> PathComponent:
        ''' get ext from path. '''
        return self.name.ext

    def replace_dirname(self, val):
        if not isinstance(val, str):
            raise TypeError
        return Path(os.path.join(val, self.name))

    def replace_name(self, val):
        if not isinstance(val, str):
            raise TypeError
        return Path(os.path.join(self.dirname, val))

    def replace_pure_name(self, val):
        return Path(os.path.join(self.dirname, self.name.replace_pure_name(val)))

    def replace_ext(self, val):
        return Path(os.path.join(self.dirname, self.name.replace_ext(val)))

    def as_file(self):
        from .nodes import FileInfo
        return FileInfo(self)

    def as_dir(self):
        from .nodes import DirectoryInfo
        return DirectoryInfo(self)

    def get_parent(self, level: int = 1):
        if not isinstance(level, int):
            raise TypeError
        if level < 1:
            raise ValueError('level must large then 1')
        return self._get_parent(level)

    def _get_parent(self, level: int):
        raise NotImplementedError

    def _init_dirname_attr(self):
        raise NotImplementedError

    def is_abspath(self):
        raise NotImplementedError

    def get_abspath(self):
        raise NotImplementedError


class _AbsPath(Path):

    def _get_parent(self, level: int):
        parts = self.replace('\\', '/').rstrip('/').split('/')
        if len(parts) <= level:
            raise ValueError(f'for path <{self}>, max level is {len(parts) - 1}')
        new_parts = parts[:-level]
        if not NT and new_parts[0] == '':
            new_parts[0] = '/'
        parent_path = self.join(*new_parts)
        return type(self)(parent_path)

    def _init_dirname_attr(self):
        if self._name is not None:
            return

        dn, fn = os.path.split(str(self))

        # `os.path.split('c:')` => `('c:', '')`
        if dn and fn:
            self._dirname = Path(dn)
            self._name = Name(fn)
        else:
            self._dirname = None
            self._name = Name(dn)

    def is_abspath(self):
        return True

    def get_abspath(self):
        return self


class _RelPath(Path):

    def _get_parent(self, level: int):
        path_cls = type(self)
        parts = self.replace('\\', '/').split('/')
        if len(parts) > level:
            new_parts = parts[:-level]
            parent_path = self.join(*new_parts)
            return path_cls(parent_path)
        level -= len(parts)
        if parts[0] == os.path.curdir:
            return path_cls(self.join(*([os.path.pardir] * (level+1))))
        elif parts[0] == os.path.pardir:
            return path_cls(self.join(*([os.path.pardir] * (level+2))))
        else:
            if level == 0:
                return path_cls(os.path.curdir)
            else:
                return path_cls(self.join(*([os.path.pardir] * level)))


    def _init_dirname_attr(self):
        if self._name is not None:
            return

        path_cls = type(self)
        dn, fn = os.path.split(str(self))

        if dn and fn:
            if dn == os.path.curdir:
                self._dirname = path_cls(dn)
            elif fn == os.path.pardir:
                # '..\\..' => ('..', '..')
                self._dirname = path_cls(os.path.join(os.path.pardir, str(self)))
            else:
                self._dirname = path_cls(dn)
            self._name = Name(fn)

        elif fn:
            if str(fn) == os.path.curdir:
                # '.' => ('', '.')
                self._dirname = path_cls(os.path.pardir)

            elif str(fn) == os.path.pardir:
                # '..' => ('', '..')
                self._dirname = path_cls(os.path.join(os.path.pardir, os.path.pardir))

            else:
                # `os.path.split('c')`  => `('', 'c')`
                self._dirname = path_cls(os.path.curdir)

            self._name = Name(fn)

        else:
            self._dirname = None
            self._name = Name(dn)

    def is_abspath(self):
        return False

    def get_abspath(self):
        return _AbsPath(os.path.abspath(self))
