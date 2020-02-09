"""
    Name: __init__.py
    Author: Charles Zhang <694556046@qq.com>
    Propose: __init__ for pygrading.general_test.
    Coding: UTF-8

    Change Log:
        **2020.02.09**
        Add import __version__.

        **2020.01.29**
        Add import html.

        **2020.01.27**
        Add import utils.

        **2020.01.26**
        Create this file!
"""
import pygrading.general_test.compiler
import pygrading.general_test.utils

from pygrading import version, __version__
from pygrading.general_test.configuration import load_config
from pygrading.general_test.testcase import TestCases, create_std_testcase, create_testcase
from pygrading.general_test.job import job
