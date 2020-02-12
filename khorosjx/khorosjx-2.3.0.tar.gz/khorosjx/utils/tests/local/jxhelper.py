# -*- coding: utf-8 -*-
"""
:Module:         khorosjx.utils.tests.local.jxhelper
:Synopsis:       This module initiates API connections to facilitate local testing
:Usage:          ``from khorosjx.utils.tests.local import jxhelper``
:Example:        ``jxhelper.initialize()``
:Created By:     Jeff Shurtliff
:Last Modified:  Jeff Shurtliff
:Modified Date:  16 Dec 2019
:Version:        1.0.0
"""

from .... import __init__ as jxinit


# Define function to initialize the khorosjx library
def initialize_khorosjx(*modules):
    """This function initializes the ``khorosjx`` package and modules using the Helper utility.

    :param modules: The module(s) to leverage with the ``khorosjx`` package (Default: import all primary modules)
    :type modules: tuple
    :returns: None
    :raises: FileNotFoundError, CredentialsUnpackingError, InvalidHelperArgumentsError, HelperFunctionNotFoundError
    """
    yml_path = "C:\\Users\\shurtj\\Development\\python-local\\khorosjx\\khorosjx\\utils\\tests\\local\\"
    jxinit.init_helper(f'{yml_path}jxhelper.yml')
    if len(modules) > 0:
        jxinit.init_module(modules)
    return


# Define function to execute when the module is imported
def initialize(*modules):
    """This function initializes the ``khorosjx`` package and modules using the Helper utility.

    :param modules: The module(s) to leverage with the ``khorosjx`` package (Default: import all primary modules)
    :type modules: tuple
    :returns: None
    :raises: FileNotFoundError, CredentialsUnpackingError, InvalidHelperArgumentsError, HelperFunctionNotFoundError
    """
    # Initialize the package
    if len(modules) > 0:
        initialize_khorosjx(modules)
    else:
        all_modules = ('admin', 'content', 'groups', 'spaces', 'users')
        initialize_khorosjx(all_modules)
    return
