# copy from https://github.com/open-mmlab/mmcv

import ast
import os
import os.path as osp
import sys
from argparse import ArgumentParser
from importlib import import_module
from typing import Iterable

import astunparse

from .addict import Dict


class ConfigDict(Dict):

    def __missing__(self, name):
        raise KeyError(name)

    def __getattr__(self, name):
        try:
            value = super(ConfigDict, self).__getattr__(name)
        except KeyError:
            ex = AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, name))
        except Exception as e:
            ex = e
        else:
            return value
        raise ex


def import_from_python(path, default_setting=None):
    astree = ast.parse(open(path).read())
    statements = [astunparse.unparse(e) for e in astree.body]
    cfg = {}
    for expr in statements:
        t = cfg.copy()
        exec(expr, t)
        if  '__builtins__' in t:
            del t['__builtins__']
        if default_setting is not None:
            key = (t.keys() - cfg.keys()).pop() 
            if key in default_setting:
                t = {key: default_setting.pop(key)}
        cfg.update(t)
    return cfg


def add_args(parser, cfg, prefix=''):
    for k, v in cfg.items():
        if isinstance(v, str):
            parser.add_argument('--' + prefix + k)
        elif isinstance(v, bool):
            if v:
                parser.add_argument('--' + prefix + k, action='store_false')
            else:
                parser.add_argument('--' + prefix + k, action='store_true')
        elif isinstance(v, int):
            parser.add_argument('--' + prefix + k, type=int)
        elif isinstance(v, float):
            parser.add_argument('--' + prefix + k, type=float)
        elif isinstance(v, dict):
            add_args(parser, v, prefix + k + '.')
        elif isinstance(v, Iterable):
            parser.add_argument('--' + prefix + k, type=type(v[0]), nargs='+')
        else:
            print('cannot parse key {} of type {}'.format(prefix + k, type(v)))
    return parser


class Config(object):
    """A facility for config and config files.

    It supports common file formats as configs: python/json/yaml. The interface
    is the same as a dict object and also allows access config values as
    attributes.

    Example:
        >>> cfg = Config(dict(a=1, b=dict(b1=[0, 1])))
        >>> cfg.a
        1
        >>> cfg.b
        {'b1': [0, 1]}
        >>> cfg.b.b1
        [0, 1]
        >>> cfg = Config.fromfile('tests/data/config/a.py')
        >>> cfg.filename
        "/home/kchen/projects/mmcv/tests/data/config/a.py"
        >>> cfg.item4
        'test'
        >>> cfg
        "Config [path: /home/kchen/projects/mmcv/tests/data/config/a.py]: "
        "{'item1': [1, 2], 'item2': {'a': 0}, 'item3': True, 'item4': 'test'}"

    """

    @staticmethod
    def fromfile(filename, default_setting=None):
        filename = osp.abspath(osp.expanduser(filename))
        if not osp.isfile(filename):
            raise FileNotFoundError(
                'file "{}" does not exist'.format(filename))

        if filename.endswith('.py'):
            cfg_dict = import_from_python(filename, default_setting)
        elif filename.endswith(('.yml', '.yaml')):
            import yaml
            cfg_dict = yaml.load(open(filename))
        elif filename.endswith('.json'):
            import json
            cfg_dict = json.load(open(filename))
        else:
            raise IOError('Only py/yml/yaml/json type are supported now!')
        return Config(cfg_dict, filename=filename)

    @staticmethod
    def auto_argparser(description=None):
        """Generate argparser from config file automatically (experimental)
        """
        partial_parser = ArgumentParser(description=description)
        partial_parser.add_argument('config', help='config file path')
        cfg_file = partial_parser.parse_known_args()[0].config
        cfg = Config.fromfile(cfg_file)
        parser = ArgumentParser(description=description)
        parser.add_argument('config', help='config file path')
        add_args(parser, cfg)
        return parser, cfg

    def __init__(self, cfg_dict=None, filename=None):
        if cfg_dict is None:
            cfg_dict = dict()
        elif not isinstance(cfg_dict, dict):
            raise TypeError('cfg_dict must be a dict, but got {}'.format(
                type(cfg_dict)))

        super(Config, self).__setattr__('_cfg_dict', ConfigDict(cfg_dict))
        super(Config, self).__setattr__('_filename', filename)
        if filename:
            with open(filename, 'r') as f:
                super(Config, self).__setattr__('_text', f.read())
        else:
            super(Config, self).__setattr__('_text', '')

    @property
    def filename(self):
        return self._filename

    @property
    def text(self):
        return self._text

    def merge_from_dict(self, cfg_dict):
        for k, v in cfg_dict.items():
            setattr(self, k, v)

    def merge_from_args(self, opt, lazy=False):
        args = [v[2:] for v in sys.argv if v.startswith('--')]
        opt = {k: v for k, v in opt.__dict__.items() if k in args}
        if lazy is True:
            self.fromfile(self.filename, opt)
        else:
            self.merge_from_dict(opt)

    def merge_from_file(self):
        raise NotImplementedError

    def merge_from_list(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Config (path: {}): {}'.format(self.filename,
                                              self._cfg_dict.__repr__())

    def __len__(self):
        return len(self._cfg_dict)

    def __getattr__(self, name):
        return getattr(self._cfg_dict, name)

    def __getitem__(self, name):
        return self._cfg_dict.__getitem__(name)

    def __setattr__(self, name, value):
        if isinstance(value, dict):
            value = ConfigDict(value)
        self._cfg_dict.__setattr__(name, value)

    def __setitem__(self, name, value):
        if isinstance(value, dict):
            value = ConfigDict(value)
        self._cfg_dict.__setitem__(name, value)

    def __iter__(self):
        return iter(self._cfg_dict)
