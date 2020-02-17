from abc import ABCMeta, abstractmethod
from collections.abc import Collection, Iterator

from typing import Union

from .CajaFactory import CajaFactory
from .PathSplitter import PathSplitter
from . import __DEFAULT_PATH_SPLITTER__

__CAJA_AGGREGATED_TRAIT__ = Collection
__META__ = type('Meta', (CajaFactory, type(__CAJA_AGGREGATED_TRAIT__)), {})

class Caja(__CAJA_AGGREGATED_TRAIT__, metaclass=__META__):

    def __init__(self,
                 content: Union[type(None), __CAJA_AGGREGATED_TRAIT__]=None,
                 path_splitter: PathSplitter=__DEFAULT_PATH_SPLITTER__()):
        self.path_splitter = path_splitter
        self.content = content

    def __getattr__(self, attr):
        try:
            return self._content_.__getattribute__(attr)
        except AttributeError:
            return self.__getitem__(attr)

    def _split_key(self, key):
        return self.path_splitter(key)

    def _resolve_item(self, key):
        left, right = self._split_key(key)
        value = self._content_[left]
        # if retrieved value is collection, wrap it
        if isinstance(value, Collection) \
        and type(value) not in type(self.__class__).exceptions:
            value = Caja(value)
        # return item directly or recurse if not leaf
        return value if right is None else value[right]

    # only called by subclasses that support mutability
    def _assign_item(self, key, value):
        left, right = self._split_key(key)
        # if key does not exist, create it
        try: 
            _ = self._content_[left]
        except LookupError: 
            self._content_[left] = Caja(None)
        # if collection under key, wrap it
        if isinstance(self._content_[left], Collection) \
        and type(self._content_[left]) not in type(self.__class__).exceptions:
                self._content_[left] = Caja(self._content_[left])
        # assign
        if right:
            self._content_[left][right] = value
        else:
            self._content_[left] = value

    # resolve lookup exceptions to a fallback value
    def safe_get(self, key, fallback=None):
        try:
            return self[key]
        except LookupError:
            return fallback

    # only called by subclasses that support mutability
    def _del_item(self, key):
        left, right = self._split_key(key)
        # if leaf, just attempt delete
        if not right:
            del self._content_[left]
        else:
            # if collection under key, wrap it
            if isinstance(self._content_[left], Collection) \
            and type(self._content_[left]) not in type(self.__class__).exceptions:
                    self._content_[left] = Caja(self._content_[left])
            # then attempt
            del self._content_[left][right]

    # operators

    def __eq__(self, other):
        # TODO improve
        if isinstance(other, Caja):
            if self.path_splitter != other.path_splitter: 
                return False
            other = other.content
        return self.content == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self._content_.__repr__()

    def __str__(self):
        return self._content_.__str__()

    # abc interface

    def __getitem__(self, key):
        # TODO improve
        try: return self._resolve_item(key)
        except Exception as e: 
            raise LookupError(f'Failed to retrieve \'{key}\'') from e

    def __contains__(self, value) -> bool:
        return self._content_.__contains__(value)

    def __iter__(self) -> Iterator:
        return self._content_.__iter__()

    def __len__(self) -> int:
        return self._content_.__len__()

    # content

    @property
    def content(self):
        raise NotImplementedError
    
    @content.setter
    def content(self, content):
        if content is None:
            self._content_ = self._default_content()
        else:
            meta = type(self)
            content_traits = meta.trait_filters(type(content))
            self_traits = meta.trait_filters(self.__class__)
            if meta.trait_match(content_traits, self_traits) and type(content) not in meta.exceptions:
                self._content_ = content if not isinstance(content, Caja) else content._content_
            else: raise TypeError(f'{type(self)} cannot wrap content of type {type(content)}')

    @content.deleter
    def content(self):
        self._content_ = self._default_content()

    @classmethod
    @abstractmethod
    def _default_content(self):
        pass

    # path_splitter

    @property
    def path_splitter(self) -> PathSplitter:
        return self._path_splitter_

    @path_splitter.setter
    def path_splitter(self, path_splitter: PathSplitter) -> None:
        if not isinstance(path_splitter, PathSplitter):
            raise TypeError('path_splitter must be an instance of PathSplitter')
        self._path_splitter_ = path_splitter

    @path_splitter.deleter
    def path_splitter(self) -> None:
        raise AttributeError('path_splitter attribute cannot be deleted')
