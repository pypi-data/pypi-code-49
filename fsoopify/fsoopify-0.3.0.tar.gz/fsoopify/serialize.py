# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from abc import ABC, abstractmethod
from typing import Optional

EXT2FORMAT_MAP = {
    '.json' : 'json',
    '.json5': 'json5',
    '.yaml' : 'yaml',
    '.yml' : 'yaml',
    '.toml' : 'toml',
}

NAME2FORMAT_MAP = {
    'pipfile' : 'pipfile'
}

_REGISTERED_SERIALIZERS = {}


class FormatNotFoundError(Exception):
    pass


class SerializeError(Exception):
    pass


def _detect_format(file_info):
    ext = file_info.path.name.ext.lower()
    if ext in EXT2FORMAT_MAP:
        return EXT2FORMAT_MAP[ext]

    name = file_info.path.name.lower()
    if name in NAME2FORMAT_MAP:
        return NAME2FORMAT_MAP[name]

    raise FormatNotFoundError(f'Cannot detect format from file {file_info!r}')

def load(file_info, format=None, *, kwargs={}):
    serializer = get_serializer(file_info, format)
    with serctx():
        return serializer.loadf(file_info, kwargs)

def dump(file_info, obj, format=None, *, kwargs={}):
    serializer = get_serializer(file_info, format)
    with serctx():
        return serializer.dumpf(file_info, obj, kwargs)

class _SerializeContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            if exc_type in (NotImplementedError, SerializeError):
                raise exc_val from None
            raise SerializeError(exc_val)

def serctx():
    'catch serialize error in context'
    return _SerializeContext()

class ISerializer:
    format: str = '' # setted on `register_format`

    def is_overrided(self, name: str):
        return getattr(type(self), name, None) is not getattr(ISerializer, name, None)

    def loads(self, s: str, kwargs: dict):
        if self.is_overrided('loadb'):
            buffer = s.encode(kwargs.pop('encoding', 'utf-8'))
            return self.loadb(buffer, kwargs)

        raise NotImplementedError

    def loadb(self, s: bytes, kwargs: dict):
        if self.is_overrided('loads'):
            text = s.decode(kwargs.pop('encoding', 'utf-8'))
            return self.loads(text, kwargs)

        raise NotImplementedError

    def loadf(self, src, kwargs):
        if self.is_overrided('loadb'):
            return self.loadb(src.read_bytes(), kwargs)

        if self.is_overrided('loads'):
            return self.loads(src.read_text(), kwargs)

        raise NotImplementedError

    def dumps(self, obj, kwargs: dict) -> str:
        if self.is_overrided('dumpb'):
            return self.dumpb(obj, kwargs).decode(kwargs.pop('encoding', 'utf-8'))

        raise NotImplementedError

    def dumpb(self, obj, kwargs: dict) -> bytes:
        if self.is_overrided('dumps'):
            return self.dumps(obj, kwargs).encode(kwargs.pop('encoding', 'utf-8'))

        raise NotImplementedError

    def dumpf(self, src, obj, kwargs: dict) -> None:
        if self.is_overrided('dumpb'):
            src.write_bytes(self.dumpb(obj, kwargs), append=False)
            return

        if self.is_overrided('dumps'):
            src.write_text(self.dumps(obj, kwargs), append=False)
            return

        raise NotImplementedError


def register_format(name: str):
    '''
    register a serializer for load and dump.
    '''
    def decorator(cls):
        _REGISTERED_SERIALIZERS[name] = cls
        cls.format = name
        return cls
    return decorator

def _load_serializer(format_):
    if not isinstance(format_, str):
        raise TypeError(f'format must be str.')

    if format_ not in _REGISTERED_SERIALIZERS:
        raise FormatNotFoundError(f'unknown format: {format_}')

    cls = _REGISTERED_SERIALIZERS[format_]
    return cls()

def get_serializer(file_info, format: Optional[str]) -> ISerializer:
    if format is None:
        format = _detect_format(file_info)

    if not isinstance(format, str):
        raise TypeError(f'format must be str.')

    if format not in _REGISTERED_SERIALIZERS:
        raise FormatNotFoundError(f'unknown format: {format}')

    cls = _REGISTERED_SERIALIZERS[format]
    return cls()


@register_format('json')
class JsonSerializer(ISerializer):
    def __init__(self):
        super().__init__()
        import json
        self.json = json

    def loads(self, s: str, kwargs: dict):
        return self.json.loads(s, **kwargs)

    def dumps(self, obj, kwargs: dict) -> str:
        return self.json.dumps(obj, **kwargs)


@register_format('pickle')
class PickleSerializer(ISerializer):
    def __init__(self):
        super().__init__()
        import pickle
        self.pickle = pickle

    def loadb(self, s: bytes, kwargs: dict):
        return self.pickle.loads(s, **kwargs)

    def dumpb(self, obj, kwargs: dict) -> bytes:
        return self.pickle.dumps(obj, **kwargs)


@register_format('json5')
class Json5Serializer(ISerializer):
    def __init__(self):
        super().__init__()
        try:
            import json5
        except ModuleNotFoundError as err:
            raise ModuleNotFoundError(
                'You need install `json5` before use it.')
        self.json5 = json5

    def loads(self, s: str, kwargs: dict):
        return self.json5.loads(s, **kwargs)

    def dumps(self, obj, kwargs: dict) -> str:
        return self.json5.dumps(obj, **kwargs)


@register_format('toml')
class TomlSerializer(ISerializer):
    def __init__(self):
        super().__init__()
        try:
            import toml
        except ModuleNotFoundError as err:
            raise ModuleNotFoundError(
                'You need install `toml` before use it.')
        self.toml = toml

    def loads(self, s: str, kwargs: dict):
        return self.toml.loads(s, **kwargs)

    def dumps(self, obj, kwargs: dict) -> str:
        return self.toml.dumps(obj, **kwargs)


@register_format('yaml')
class YamlSerializer(ISerializer):
    def __init__(self):
        super().__init__()
        try:
            import yaml
        except ModuleNotFoundError as err:
            raise ModuleNotFoundError(
                'You need install `pyyaml` before use it.')
        self.yaml = yaml

    def loads(self, s: str, kwargs: dict):
        return self.yaml.safe_load(s, **kwargs)

    def dumps(self, obj, kwargs: dict) -> str:
        return self.yaml.dump(obj, **kwargs)


@register_format('pipfile')
class PipfileSerializer(ISerializer):
    def __init__(self):
        super().__init__()
        try:
            import pipfile
        except ModuleNotFoundError as err:
            raise ModuleNotFoundError(
                'You need install `pipfile` before use it.')
        self.pipfile = pipfile

    def loadf(self, src, kwargs):
        pipfile = self.pipfile.load(src.path)
        return pipfile.data

    def dumps(self, obj, kwargs: dict) -> str:
        raise NotImplementedError('dump `pipfile` is not supported.')
