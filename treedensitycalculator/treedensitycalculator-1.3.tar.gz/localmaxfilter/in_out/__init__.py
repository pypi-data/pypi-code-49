# -*- coding: utf-8 -*-
"""
| ----------------------------------------------------------------------------------------------------------------
| Date                : March 2019
| Copyright           : (C) 2018 by Tinne Cahy, Louis Put (Geo Solutions) and Ann Crabbé (KU Leuven)
| Email               : tinne.cahy@geosolutions.be, ann.crabbe@kuleuven.be
| Acknowledgements    : Translated from Local Maximum Filter [C++ software]
|                       Ghent University, Laboratory of Forest Management and Spatial Information Techniques
|                       Lieven P.C. Verbeke
|
| This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
| License as published by the Free Software Foundation; either version 3 of the License, or any later version.
| ----------------------------------------------------------------------------------------------------------------
"""
import os


def check_path(path):
    """ Check if path exists. Skipp path which are in memory

    :param path: the absolute path to the input file
    """
    if path == '':
        pass

    elif 'vsimem' in path:
        pass

    elif not os.path.exists(path):
        raise Exception("Cannot find file '" + path + "'.")
