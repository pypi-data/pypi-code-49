#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDccLib
"""

from __future__ import print_function, division, absolute_import

import os
import inspect
import logging.config

from tpDcc import register
from tpDcc.abstract import dcc as abstract_dcc, shelf as abstract_shelf, menu as abstract_menu

main = __import__('__main__')


class DccCallbacks(object):
    Shutdown = ('Shutdown', {'type': 'simple'})
    Tick = ('Tick', {'type': 'simple'})
    ScenePreCreated = ('ScenePreCreated', {'type': 'simple'})
    ScenePostCreated = ('ScenePreCreated', {'type': 'simple'})
    SceneNewRequested = ('SceneNewRequested', {'type': 'simple'})
    SceneNewFinished = ('SceneNewFinished', {'type': 'simple'})
    SceneSaveRequested = ('SceneSaveRequested', {'type': 'simple'})
    SceneSaveFinished = ('SceneSaveFinished', {'type': 'simple'})
    SceneOpenRequested = ('SceneOpenRequested', {'type': 'simple'})
    SceneOpenFinished = ('SceneOpenFinished', {'type': 'simple'})
    UserPropertyPreChanged = ('UserPropertyPreChanged', {'type': 'filter'})
    UserPropertyPostChanged = ('UserPropertyPostChanged', {'type': 'filter'})
    NodeSelect = ('NodeSelect', {'type': 'filter'})
    NodeAdded = ('NodeAdded', {'type': 'filter'})
    NodeDeleted = ('NodeDeleted', {'type': 'filter'})


# =================================================================================


class Dccs(object):
    Unknown = 'unknown'
    Houdini = 'houdini'
    Maya = 'maya'
    Max = 'max'
    Nuke = 'nuke'

# =================================================================================


def init(do_reload=False, dev=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    :param dev: bool, Whether artellapipe is initialized in dev mode or not
    """

    from tpDcc.libs.python import importer

    create_logger()

    class tpDccLib(importer.Importer, object):
        def __init__(self, *args, **kwargs):
            super(tpDccLib, self).__init__(module_name='tpDcc', *args, **kwargs)

        def get_module_path(self):
            """
            Returns path where tpDccLib module is stored
            :return: str
            """

            try:
                mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
            except Exception:
                try:
                    mod_dir = os.path.dirname(__file__)
                except Exception:
                    try:
                        import tpDccLib
                        mod_dir = tpDccLib.__path__[0]
                    except Exception:
                        return None

            return mod_dir

    def init_dcc(do_reload=False):
        """
        Checks DCC we are working on an initializes proper variables
        """

        if 'cmds' in main.__dict__:
            from tpDcc.dccs.maya import loader
            loader.init_dcc(do_reload=do_reload)
        elif 'MaxPlus' in main.__dict__:
            from tpDcc.dccs.max import loader
            loader.init_dcc(do_reload=do_reload)
        elif 'hou' in main.__dict__:
            from tpDcc.dccs.houdini import loader
            loader.init_dcc(do_reload=do_reload)
        elif 'nuke' in main.__dict__:
            from tpDcc.dccs.nuke import loader
            loader.init_dcc(do_reload=do_reload)
        else:
            global Dcc
            from tpDcc.core import dcc
            Dcc = dcc.UnknownDCC

    dcclib_importer = importer.init_importer(importer_class=tpDccLib, do_reload=False)
    dcclib_importer.import_modules()
    dcclib_importer.import_packages(only_packages=True, order=['tpDcc.core'])
    if do_reload:
        dcclib_importer.reload_all()

    init_dcc(do_reload=do_reload)

    from tpDcc.managers import callbackmanager
    callbackmanager.CallbacksManager.initialize()


def create_logger():
    """
    Returns logger of current modue
    """

    logging.config.fileConfig(get_logging_config(), disable_existing_loggers=False)
    logger = logging.getLogger('tpDcc-core')

    return logger


def create_logger_directory():
    """
    Creates artellapipe logger directory
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)


def get_logging_config():
    """
    Returns logging configuration file path
    :return: str
    """

    create_logger_directory()

    return os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))


def is_nuke():
    """
    Checks if Nuke is available or not
    :return: bool
    """

    import tpDcc

    return tpDcc.Dcc.get_name() == Dccs.Nuke


def is_maya():
    """
    Checks if Maya is available or not
    :return: bool
    """

    import tpDcc

    return tpDcc.Dcc.get_name() == Dccs.Maya


def is_max():
    """
    Checks if Max is available or not
    :return: bool
    """

    import tpDcc

    return tpDcc.Dcc.get_name() == Dccs.Max


def is_houdini():
    """
    Checks if Houdini is available or not
    :return: bool
    """

    import tpDcc

    return tpDcc.Dcc.get_name() == Dccs.Houdini


def callbacks():
    """
    Return a full list of callbacks based on DccCallbacks dictionary
    :return: list<str>
    """

    new_list = list()
    for k, v in DccCallbacks.__dict__.items():
        if k.startswith('__') or k.endswith('__'):
            continue
        new_list.append(v[0])

    return new_list


register.register_class('Dcc', abstract_dcc.AbstractDCC())
register.register_class('Menu', abstract_menu.AbstractMenu)
register.register_class('Shelf', abstract_shelf.AbstractShelf)
register.register_class('Dccs', Dccs)
register.register_class('DccCallbacks', DccCallbacks)
register.register_class('callbacks', callbacks)
register.register_class('is_maya', is_maya)
register.register_class('is_max', is_max)
register.register_class('is_houdini', is_houdini)
register.register_class('is_nuke', is_nuke)
