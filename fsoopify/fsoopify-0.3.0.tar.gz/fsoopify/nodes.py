#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import os
from typing import Iterable, List, Any
from abc import abstractmethod, ABC
from enum import Enum

from .paths import Path
from .size import Size
from .serialize import load, dump, get_serializer, serctx

class NodeType(Enum):
    file = 1
    dir = 2


class NodeInfo(ABC):
    ''' the abstract base class for file system node. '''

    def __init__(self, path):
        # path alwasys be abs
        self._path: Path = Path(path).get_abspath()

    def __str__(self):
        return str(self._path)

    def __repr__(self):
        return '{}(\'{}\')'.format(type(self).__name__, self._path)

    @property
    def path(self) -> Path:
        '''
        return a Path object.
        '''
        return self._path

    def rename(self, dest_path: str):
        '''
        use `os.rename()` to move the node.
        '''
        if not isinstance(dest_path, str):
            raise TypeError
        os.rename(self._path, dest_path)
        self._path = Path(dest_path).get_abspath()

    def get_parent(self, level=1):
        '''
        get parent dir as a `DirectoryInfo`.

        return `None` if self is top.
        '''
        try:
            parent_path = self.path.get_parent(level)
        except ValueError: # abspath cannot get parent
            return None
        assert parent_path
        return DirectoryInfo(parent_path)

    @staticmethod
    def from_path(path):
        '''
        create from path.

        return `None` if path is not exists.
        '''
        if os.path.isdir(path):
            return DirectoryInfo(path)

        if os.path.isfile(path):
            return FileInfo(path)

        return None

    @staticmethod
    def from_cwd():
        '''
        get a `DirectoryInfo` by `os.getcwd()`
        '''
        return DirectoryInfo(os.getcwd())

    @staticmethod
    def from_argv0():
        '''
        get a `FileInfo` by `sys.argv[0]`
        '''
        return FileInfo(sys.argv[0])

    # common methods

    @property
    @abstractmethod
    def node_type(self):
        raise NotImplementedError

    def is_exists(self):
        '''
        get whether the node is exists on disk.
        '''
        return os.path.exists(self._path)

    def is_directory(self):
        '''
        get whether the node is a exists directory.
        '''
        return False

    def is_file(self):
        '''
        get whether the node is a exists file.
        '''
        return False

    # abstract methods

    @abstractmethod
    def delete(self):
        ''' remove the node from disk. '''
        raise NotImplementedError

    @abstractmethod
    def create_hardlink(self, dest_path: str):
        ''' create hardlink for the node. '''
        raise NotImplementedError


class FileInfo(NodeInfo):

    def open(self, mode='r', *, buffering=-1, encoding=None, newline=None, closefd=True):
        ''' open the file. '''
        return open(self._path,
                    mode=mode,
                    buffering=buffering,
                    encoding=encoding,
                    newline=newline,
                    closefd=closefd)

    @property
    def size(self):
        ''' get file size. '''
        return Size(os.path.getsize(self.path))

    def write(self, data, *, mode=None, buffering=-1, encoding=None, newline=None):
        ''' write data into the file. '''
        if mode is None:
            mode = 'w' if isinstance(data, str) else 'wb'
        with self.open(mode=mode, buffering=buffering, encoding=encoding, newline=newline) as fp:
            return fp.write(data)

    def read(self, mode='r', *, buffering=-1, encoding=None, newline=None):
        ''' read data from the file. '''
        with self.open(mode=mode, buffering=buffering, encoding=encoding, newline=newline) as fp:
            return fp.read()

    def write_text(self, text: str, *, encoding='utf-8', append=True):
        ''' write text into the file. '''
        mode = 'a' if append else 'w'
        return self.write(text, mode=mode, encoding=encoding)

    def write_bytes(self, data: bytes, *, append=True):
        ''' write bytes into the file. '''
        mode = 'ab' if append else 'wb'
        return self.write(data, mode=mode)

    def copy_to(self, dest, buffering: int = -1):
        '''
        copy the file to dest path.

        `dest` canbe `str`, `FileInfo` or `DirectoryInfo`.

        if `dest` is `DirectoryInfo`, that mean copy into the dir with same name.
        '''
        if isinstance(dest, str):
            dest_path = dest
        elif isinstance(dest, FileInfo):
            dest_path = dest.path
        elif isinstance(dest, DirectoryInfo):
            dest_path = dest.path / self.path.name
        else:
            raise TypeError('dest is not one of `str`, `FileInfo`, `DirectoryInfo`')

        with open(self._path, 'rb', buffering=buffering) as source:
            # use x mode to ensure dest does not exists.
            with open(dest_path, 'xb') as dest_file:
                for buffer in source:
                    dest_file.write(buffer)

    def read_text(self, encoding='utf-8') -> str:
        ''' read all text into memory. '''
        with self.open('r', encoding=encoding) as fp:
            return fp.read()

    def read_bytes(self) -> bytes:
        ''' read all bytes into memory. '''
        with self.open('rb') as fp:
            return fp.read()

    # override common methods

    @property
    def node_type(self):
        return NodeType.file

    def is_exists(self) -> bool:
        return self.is_file()

    def is_file(self) -> bool:
        ''' check if this is a exists file. '''
        return os.path.isfile(self._path)

    # override @abstractmethod

    def delete(self):
        ''' remove the file from disk. '''
        os.remove(self._path)

    def create_hardlink(self, dest_path: str):
        ''' create hardlink for the file. '''
        os.link(self._path, dest_path)

    # load/dump system.

    def load(self, format=None, *, kwargs={}):
        '''
        deserialize object from the file.

        auto detect format by file extension name if `format` is None.
        for example, `.json` will detect as `json`.

        * raise `FormatNotFoundError` on unknown format.
        * raise `SerializeError` on any serialize exceptions.
        '''
        return load(self, format=format, kwargs=kwargs)

    def dump(self, obj, format=None, *, kwargs={}):
        '''
        serialize the `obj` into file.

        * raise `FormatNotFoundError` on unknown format.
        * raise `SerializeError` on any serialize exceptions.
        '''
        return dump(self, obj, format=format, kwargs=kwargs)

    def load_context(self, format=None, *, load_kwargs={}, dump_kwargs={}, lock=False):
        '''
        load the file in a context, auto dump `context.data` into file when context exit.

        - if the file does not exists, `context.data` will be `None`.
        - set `context.data` to `None` will remove the file from disk.
        - by default, `context.save_on_exit` is `True`.
        - if `lock` is `True`, lock the file until the context exit. (`lock` require install package `portalocker`)

        usage:

        ``` py
        with file.load_context() as context:
            # read or edit context.data
            ...
        ```
        '''
        if lock:
            context = _LockedDataContext(self, format, load_kwargs, dump_kwargs)
        else:
            context = _DataContext(self, format, load_kwargs, dump_kwargs)
        return context

    # hash system

    def get_file_hash(self, *algorithms: str):
        '''
        get lower case hash of file.

        return value is a tuple, you may need to unpack it.

        for example: `get_file_hash('md5', 'sha1')` return `('XXXX1', 'XXXX2')`
        '''
        from .hashs import hashfile_hexdigest
        return hashfile_hexdigest(self._path, algorithms)


class DirectoryInfo(NodeInfo):

    def create(self):
        ''' create directory. '''
        os.mkdir(self.path)

    def ensure_created(self):
        ''' ensure the directory was created. '''
        if not self.is_directory():
            os.makedirs(self.path)

    def iter_items(self, depth: int = 1) -> Iterable[NodeInfo]:
        '''
        get items from directory.
        '''
        if depth is not None and not isinstance(depth, int):
            raise TypeError
        def itor(root, d):
            if d is not None:
                d -= 1
                if d < 0:
                    return
            for name in os.listdir(root):
                path = os.path.join(root, name)
                node = NodeInfo.from_path(path)
                yield node
                if isinstance(node, DirectoryInfo):
                    yield from itor(path, d)
        yield from itor(self._path, depth)

    def list_items(self, depth: int = 1) -> List[NodeInfo]:
        '''
        get items from directory.
        '''
        return list(self.iter_items(depth))

    def has_file(self, name: str):
        '''
        check whether this directory contains the file.
        '''
        return os.path.isfile(self._path / name)

    def has_directory(self, name: str):
        '''
        check whether this directory contains the directory.
        '''
        return os.path.isdir(self._path / name)

    def get_fileinfo(self, name: str):
        '''
        get a `FileInfo` for a file (without create actual file).
        '''
        return FileInfo(os.path.join(self._path, name))

    def get_dirinfo(self, name: str):
        '''
        get a `DirectoryInfo` for a directory (without create actual directory).
        '''
        return DirectoryInfo(os.path.join(self._path, name))

    def get_unique_name(self, name: str, ext: str=''):
        '''
        generate a unique name for new item from the directory.
        '''
        def iter_name():
            yield f'{name}{ext}'
            index = 0
            while True:
                index += 1
                yield f'{name} ({index}){ext}'

        for unique_name in iter_name():
            if not os.path.exists(self._path / unique_name):
                return unique_name

    # tree api

    def get_tree(self) -> dict:
        '''
        Get structure tree from current directory.
        '''
        tree = {}
        for item in self.list_items():
            name = str(item.path.name)
            if item.node_type == NodeType.file:
                tree[name] = item.read(mode='rb')
            else:
                tree[name] = item.get_tree()
        return tree

    def make_tree(self, tree: dict, mode: int=0):
        '''
        make directory structure with tree.

        for each items in `tree`,

        - if value is `str` or `bytes`, use the key as filename to create a file, write the value as content;
        - if value is a `dict`, use the key as dirname to create a dir, then use the value to make sub tree.

        `mode` is a const `int` value:

        - `0` mean ignore all `FileExistsError`;
        - `1` mean raise `FileExistsError` when any file exists;
        - `2` mean overwrite all exists files;
        '''
        if mode not in (0, 1, 2):
            raise ValueError(mode)

        for key, value in tree.items():
            if not isinstance(key, str):
                raise TypeError(key)

            if isinstance(value, (str, bytes)):
                subfile = self.get_fileinfo(key)
                if subfile.is_file():
                    if mode == 0:
                        continue
                    elif mode == 1:
                        raise FileExistsError(subfile.path)
                    elif mode == 2:
                        subfile.delete()
                if isinstance(value, str):
                    subfile.write_text(value)
                else:
                    subfile.write_bytes(value)

            elif isinstance(value, dict):
                subdir = self.get_dirinfo(key)
                subdir.ensure_created()
                subdir.make_tree(value, mode=mode)

            else:
                raise TypeError((key, value))

    # override common methods

    @property
    def node_type(self):
        return NodeType.dir

    def is_exists(self) -> bool:
        return self.is_directory()

    def is_directory(self) -> bool:
        ''' check if this is a exists directory. '''
        return os.path.isdir(self._path)

    # override @abstractmethod

    def delete(self):
        ''' remove the directory from disk. '''
        os.rmdir(self._path)

    def create_hardlink(self, dest_path: str):
        ''' create hardlink for the directory (includes childs). '''

        # self
        dirinfo = DirectoryInfo(dest_path)
        dirinfo.ensure_created()

        # child
        for item in self.list_items():
            item.create_hardlink(os.path.join(dest_path, item.path.name))


class _DataContext:
    def __init__(self, file: FileInfo, format, load_kwargs: dict, dump_kwargs: dict):
        self._data = None
        self.save_on_exit = True
        self._file = file
        self._format = format
        self._serializer = get_serializer(file, format)
        self._load_kwargs = load_kwargs
        self._dump_kwargs = dump_kwargs

        self._on_load()

    def _loadb(self, s: bytes):
        with serctx():
            return self._serializer.loadb(s, self._load_kwargs)

    def _dumpb(self) -> bytes:
        with serctx():
            return self._serializer.dumpb(self.data, kwargs=self._dump_kwargs)

    def _on_load(self):
        if self._file.is_file():
            self._data = self._loadb(self._file.read_bytes())
        else:
            self._data = None

    def _on_dump(self):
        if self.data is None:
            if self._file.is_file():
                self._file.delete()
        else:
            self._file.dump(self.data, self._format, kwargs=self._dump_kwargs)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self.save_on_exit:
            self.save()

    def save(self):
        self._on_dump()


class _LockedDataContext(_DataContext):
    def __init__(self, file, format, load_kwargs, dump_kwargs):
        import portalocker
        self.portalocker = portalocker
        self._fp = None
        super().__init__(file, format, load_kwargs, dump_kwargs)

    def _on_load(self):
        is_exists = self._file.is_file()
        if is_exists:
            mode = 'r+b'
        else:
            mode = 'wb'
        self._fp = self._file.open(mode)
        self.portalocker.lock(self._fp, self.portalocker.LOCK_EX)
        if is_exists:
            self._data = self._loadb(self._fp.read())

    def _on_dump(self):
        if self.data is not None:
            buf = self._dumpb()
            self._fp.seek(0)
            self._fp.write(buf)
            self._fp.truncate()
            self._fp.close()

        else:
            self._fp.close()
            if self._file.is_file():
                self._file.delete()
