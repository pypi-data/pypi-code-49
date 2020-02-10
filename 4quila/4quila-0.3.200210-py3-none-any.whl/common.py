#!/usr/bin/python3
# -*- coding: utf-8 -*-
import inspect
import logging
import sys
import traceback
import linecache
logger = logging.getLogger('_4quila')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

URL = 'https://4quila.ink'
EMAIL = 't10n@4quila.ink'


def format_frame(frame):
    for k, v in frame.f_locals.items():
        if k.startswith('__') or k.endswith('__'):
            continue
        if inspect.ismodule(v):
            continue
        if inspect.isfunction(v):
            continue
        if inspect.isclass(v):
            continue
        yield '%s->%s' % (k, v)


def format_stacks():
    exc_type, exc, exc_traceback = sys.exc_info()
    if not exc_type:
        return
    for tb in traceback.walk_tb(exc_traceback):
        tb_frame, tb_lineno = tb
        tb_filename = tb_frame.f_code.co_filename
        tb_name = tb_frame.f_code.co_name
        tb_line = linecache.getline(tb_frame.f_code.co_filename, tb_lineno).strip()
        yield '%s[%s] %s: %s' % (tb_filename, tb_lineno, tb_name, tb_line)
        for item in format_frame(tb_frame):
            yield '    %s' % item
    yield '%s %s' % (exc_type.__name__, exc)
