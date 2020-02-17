# -*- coding: utf-8 -*-
"""

    Тесты инструментов запуска

"""
import os
import sys


def test_test():
    print()
    print('sys.argv', sys.argv)
    print('os.getcwd()', os.getcwd())
    print('sys.executable', sys.executable)

