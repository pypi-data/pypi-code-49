#!/usr/bin/python
# -*- coding: utf-8 -*
# #############################################################################
#
#  Copyright (c) Baidu.com,  Inc. All Rights Reserved
#
# #############################################################################

"""
:author:
    Guannan Ma @mythmgn
"""

import os

import cup
from cup import log
from cup import shell
from cup import platforms

__all__ = ['CSmsSender']
if platforms.is_windows():
    # windows does not support serializer and noah
    pass
else:
    from cup.bidu import serializer
    from cup.bidu import noah
    __all__.append('serializer')
    __all__.append('noah')


# pylint: disable=R0903
class CSmsSender(object):
    """
    depreciated, use from cup.bidu.cloud import sms
    """
    def __init__(self, path_smstool='/bin/gsmsend'):
        raise ImportError('depreciated, use from cup.bidu.cloud import sms')


# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
