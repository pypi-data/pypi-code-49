#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
exceptions.py: handling custom exceptions.
"""


class NoVencodeError(Exception):
    """Raised when no VEnCode was found"""
    pass


class SampleTypeNotSupported(Exception):
    def __init__(self, sample_type, cell_type, msg=None):
        if msg is None:
            msg = "sample_type - {} - currently not supported for cell type {}".format(sample_type, cell_type)
        super().__init__(msg)
