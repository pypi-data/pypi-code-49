#
# Contributed by Rodrigo Tobar <rtobar@icrar.org>
#
# ICRAR - International Centre for Radio Astronomy Research
# (c) UWA - The University of Western Australia, 2016
# Copyright by UWA (in the framework of the ICRAR)
#
'''
Wrapper for _yajl2 C extension module
'''

from ijson import common, compat, utils
from . import _yajl2

@utils.coroutine
def basic_parse_basecoro(target, **kwargs):
    return _yajl2.basic_parse_basecoro(target.send, **kwargs)

def basic_parse(file, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = kwargs.pop('buf_size', 64 * 1024)
    return _yajl2.basic_parse(f, buf_size, **kwargs)

@utils.coroutine
def parse_basecoro(target, **kwargs):
    return _yajl2.parse_basecoro(target.send, **kwargs)

def parse(file, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = kwargs.pop('buf_size', 64 * 1024)
    return _yajl2.parse(f, buf_size, **kwargs)

@utils.coroutine
def kvitems_basecoro(target, prefix, map_type=None, **kwargs):
    return _yajl2.kvitems_basecoro(target.send, prefix, map_type, **kwargs)

def kvitems(file, prefix, map_type=None, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = kwargs.pop('buf_size', 64 * 1024)
    return _yajl2.kvitems(f, buf_size, prefix, map_type, **kwargs)

@utils.coroutine
def items_basecoro(target, prefix, map_type=None, **kwargs):
    return _yajl2.items_basecoro(target.send, prefix, map_type, **kwargs)

def items(file, prefix, map_type=None, **kwargs):
    f = compat.bytes_reader(file)
    buf_size = kwargs.pop('buf_size', 64 * 1024)
    return _yajl2.items(f, buf_size, prefix, map_type, **kwargs)

common.enrich_backend(globals())
