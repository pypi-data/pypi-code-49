#!/usr/bin python36
# -*- coding: utf-8 -*
"""
Summary
-------
"""

__author__ = ['fzhao']

import os

scriptpath = os.path.dirname(os.path.abspath(__file__))
print("Script path is : " + scriptpath)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
