#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: zhangkai
Email: kai.zhang1@nio.com
Last modified: 2019-09-04 13:32:01
'''
import asyncio
import inspect
import sys
from functools import partial

from .config_utils import Config
from .log_utils import Logger


def Fire(component=None):
    opt = Config()
    logger = Logger()
    if inspect.isclass(component):
        module = component(**opt)
        func = getattr(module, sys.argv[1])
        params = sys.argv[2:]
    elif inspect.isfunction(component):
        func = partial(component, **opt)
        params = sys.argv[1:]
    elif component is None:
        modules = inspect.stack()[1].frame.f_globals
        module = modules[sys.argv[1]]
        if isinstance(module, type):
            func = getattr(module(), sys.argv[2])
            params = sys.argv[3:]
        else:
            func = module
            params = sys.argv[2:]
    else:
        func = getattr(component, sys.argv[1])
        params = sys.argv[2:]

    ret = func(*params)
    if inspect.isawaitable(ret):
        loop = asyncio.get_event_loop()
        ret = loop.run_until_complete(ret)
    if ret is not None:
        logger.info(ret)
