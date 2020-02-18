#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Import libraries
# Python internal libraries
# future imports
from __future__ import print_function
from __future__ import unicode_literals
#from builtins import str
from builtins import range
from future import standard_library
standard_library.install_aliases()
import copy
import time
from datetime import datetime
import cProfile
import configparser
import logging
logging.getLogger().setLevel(20)
import math
from multiprocessing import Pool
import operator
import os
import pickle
import psutil
import re
import io
import shutil
import subprocess
import sys
import tarfile
import traceback
# External Python Libraries
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy
from Bio.PDB import *
#import pandas


# Our modules
try:
    import Bioinformatics
except ImportError:
    print("\n I couldn't import Bioinformatics\n")
    print(sys.exc_info()[1])
try:
    import ADT
except ImportError:
    print("\n I couldn't import ADT\n")
    print(sys.exc_info()[1])
try:
    import SELSLIB2
except ImportError:
    print("\n I couldn't import SELSLIB2\n")
    print(sys.exc_info()[1])
try:
    import unitCellTools
except ImportError:
    print("\n I couldn't import unitCellTools\n")
    print(sys.exc_info()[1])


"""
This module was originally developed to support the program ALIXE. It contains functions related to

It also contains a space group dictionary
"""

# Functions to help in optimization
def timing(f):
    """

    :param f:
    :type f:
    :return:
    :rtype:
    """

    def wrap(*args, **kwds):
        time1 = time.time()
        ret = f(*args, **kwds)
        time2 = time.time()
        print ('%s function took %0.8f s' % (f.__name__, (time2 - time1)))
        return ret

    return wrap


def profileit(func):
    """

    :param func:
    :type func:
    :return:
    :rtype:
    """

    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile"  # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval

    return wrapper

# DEFAULT CONFIGURATION FOR ALIXE
defaults_alixe = """
[ALIXE]
# Either a folder with solutions and data files 
# or a path to a bor file
input_info_1: none
# Only required if combination between two folder or runs is going to be performed
#input_info_2: none

# Output folder settings
# if another name is set, then it will generate a folder with that name
output_folder: CLUSTERING

# Can be monomer multimer cc_analysis fish
alixe_mode: monomer

# Path to the local executable for phase combination
path_chescat: 

# Core clustering algorithm settings
# wMPD tolerances for phase comparison
tolerance_first_round: 60
tolerance_second_round: 88
tolerance_merging: 90
# Resolution thresholds for phase comparison
resolution_comparison: 3.5
resolution_merging: 2.0
# Algorithm for origin shift computation. Can be sxos or sxosfft
origin_search: sxosfft
# Weight to apply to the reflections. Can be e (e-value) or f (amplitudes)
weight: e
# Flag to compute or not map correlation coefficient apart from wMPD
map_cc: True
# Flag to check the origin shift. If False, not checked after cycle 1
oricheck: True
# Number of cycles of iterative clustering
cycles = 3
# Minimal size of remaining list to process to move from parallel to sequential algorithm
# NOTE CM: We should change this to a dynamic parameterization 
minchunk: 100
max_non_clust_events: 20
# Seed argument to use in chescat jobs for sequential mode
seed=1
# Number of cores to exploit in parallel parts of the algorithm
# By default set to the number of physical CPUs - 1
number_cores_parallel: -1

# Solution limits and filtering
# The FOM Can be COMBINED, CC, LLG or ZSCORE
fom_sorting: COMBINED
# Hard limit on the number of solutions to be processed
# NOTE CM: Maybe I should limit per single chescat job, considering cores available
limit_sol_per_rotclu: 1000
# Integer in the range of the number of fragments (ens1_fragn, only ARCIMBOLDO_LITE)
fragment: 1
# For SHELXE runs inside ALIXE. If no line is provided, default values will be used
#shelxe_line_alixe: -m5 -a0
#shelxe_line_expansion: -m15 -a8

# path_reference_solution or folder_path Use this solution or solutions as references only
references: none

# Phase clusters posterior analysis
# If set to True, expansions from the merged phase sets and with SHELXE will be attempted in multiprocessing
expansions: True
# If set to True, output tables and files will not include the phase sets that did not cluster
filter_single: False
# Perform a wMPE assesment of the solutions
postmortem: False
# Generates in real space the equivalent merging of solutions
fusedcoord: False 
# Computes the initial CC of the combined phases with SHELXE
ccfromphi: False

# Graphical output
plots: True
"""

# CONDITIONS FOR CHECKING OF RUNS
CHESCAT_OUT_END_CONDITION_LOCAL = """cluster phases written to"""
CHESCAT_OUT_FAILURE_CONDITION_LOCAL = """Bad command line"""
CHESCAT_OUT_END_TEST = 1


# SPACE GROUP DICTIONARY

# These are used for polar space groups
x = 'x'
y = 'y'
z = 'z'

dictio_space_groups = {}

# Key is space group number, except for non standard settings
# Dictionary contains the following fields:
# symbol --> The space group symbol as a string, found in the CRYST card of the pdb
# symops --> A dictionary with the symmetry operations. Keys are numbers from 1 to n,
# being n the number of symmetry operations
#            Each symop is itself a dictionary, with a 'tra' and a 'rot' key, that contain the vectors/matrices (floats)
#            dictio_space_groups[1]['symbol'] --> 'P 1' # standard Hermann-Mauguin symbol
#            dictio_space_groups[1]['short_symbol'] --> 'P 1' # Reduced notation
#            dictio_space_groups[1]['xHM_symbol'] --> 'P 1' # extended Hermann-Mauguin symbol
#            dictio_space_groups[1]['hall_symbol'] --> 'P 1'
#            dictio_space_groups[1]['symops'][1]['tra'] --> [0.0, 0.0, 0.0]
#            dictio_space_groups[1]['symops'][1]['rot'] --> [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
#            dictio_space_groups[1]['origins_list'] --> [[x, y, z]]
#                                                       if space group is non polar then it will have the coordinates
#            dictio_space_groups[1]['polar'] --> True
#            dictio_space_groups[1]['latt'] --> 1 useful to generate ins files from here
#            dictio_space_groups[1]['symm_cards'] --> [] useful to generate ins files from here

# LATT instruction correspondence with centering of unit cells
# P -> 1 I -> 2 R on hexagonal axes -> 3 F -> 4 A -> 5 B -> 6 C -> 7

dictio_space_groups[1] = {'symbol': 'P 1', 'short_symbol': 'P1', 'xHM_symbol':'P 1' , 'hall_symbol':'P 1' ,'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}},
                          'point': 1, 'laue': '-1',
                          'origins_list': [[x, y, z]], 'polar': True, 'latt': 1, 'symm_cards': []}

# NOTE CM: A1 has not been tested. On the other hand, only 1 structure in the PDB
# dictio_space_groups['A1'] = {'symbol':'A 1' , 'short_symbol': 'A1', 'xHM_symbol': 'A 1' , 'hall_symbol': 'A 1',
#                              'symops': {
#     1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}},
#                           'point': 1, 'laue': '-1',
#                           'origins_list': None, 'polar': True, 'latt': 1, 'symm_cards': []}

# NOTE CM: Not tested, no structures in the PDB
# dictio_space_groups['B1'] = {'symbol':'B 1' , 'short_symbol':'B1' , 'xHM_symbol':'B 1' , 'hall_symbol':'B 1' ,
#                              'symops': {
#     1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}},
#                           'point': 1, 'laue': '-1',
#                           'origins_list': None, 'polar': True, 'latt': 1, 'symm_cards': []}

# NOTE CM: Not tested, no structures in the PDB
# dictio_space_groups['C1'] = {'symbol':'C 1' , 'short_symbol':'C1' , 'xHM_symbol':'C 1' , 'hall_symbol': 'C 1',
#                              'symops': {
#     1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}},
#                           'point': 1, 'laue': '-1',
#                           'origins_list': None, 'polar': True, 'latt': 1, 'symm_cards': []}

# NOTE CM: Not tested, no structures in the PDB
# dictio_space_groups['I1'] = {'symbol': 'I 1' , 'short_symbol': 'I1', 'xHM_symbol': 'I 1', 'hall_symbol':'I 1' ,'symops': {
#     1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}},
#                           'point': 1, 'laue': '-1',
#                           'origins_list': None, 'polar': True, 'latt': 1, 'symm_cards': []}

# NOTE CM: Not tested, no structures in the PDB
# dictio_space_groups['F1'] = {'symbol':'F 1' , 'short_symbol':'F1' , 'xHM_symbol':'F 1' , 'hall_symbol':'F 1' ,'symops': {
#     1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}},
#                           'point': 1, 'laue': '-1',
#                           'origins_list': [[x, y, z]], 'polar': True, 'latt': 1, 'symm_cards': []}

dictio_space_groups[3] = {'symbol': 'P 1 2 1', 'short_symbol': 'P2', 'xHM_symbol': 'P 1 2 1', 'hall_symbol':'P 2y',
                          'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}},
                          'point': 2, 'laue': '2/m',
                          'origins_list': [[0.0, y, 0.0], [0.0, y, 1 / 2.0], [1 / 2.0, y, 0.0], [1 / 2.0, y, 1 / 2.0]],
                          'polar': True, 'latt': 1, 'symm_cards': ['SYMM -x, y, -z\n']}

dictio_space_groups[4] = {'symbol': 'P 1 21 1', 'short_symbol': 'P21', 'xHM_symbol': 'P 1 21 1', 'hall_symbol':'P 2yb',
                          'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}},
                          'point': 2, 'laue': '2/m',
                          'origins_list': [[0.0, y, 0.0], [0.0, y, 1 / 2.0], [1 / 2.0, y, 0.0], [1 / 2.0, y, 1 / 2.0]],
                          'polar': True, 'latt': 1, 'symm_cards': ['SYMM -x, y+0.5, -z\n']}


dictio_space_groups[5] = {'symbol': 'C 1 2 1', 'short_symbol': 'C2', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    3: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}},
                          'point': 2, 'laue': '2/m',
                          'origins_list': [[0.0, y, 0.0], [0.0, y, 1 / 2.0]], 'polar': True, 'latt': 7,
                          'symm_cards': ['SYMM -x, y, -z\n']}

dictio_space_groups['I2'] = {'symbol': 'I 1 2 1', 'short_symbol': 'I2', 'xHM_symbol': 'I 1 2 1',
                             'hall_symbol': 'C 2y (x,y,-x+z)',
                             'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    3: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}},
                             'point': 2, 'laue': '2/m',
                             'origins_list': [[0.0, y, 0.0], [0.0, y, 1 / 2.0]], 'polar': True, 'latt': 2,
                             'symm_cards': ['SYMM -x, y, -z\n']}

dictio_space_groups[16] = {'symbol': 'P 2 2 2', 'short_symbol': 'P222', 'xHM_symbol': 'P 2 2 2',
                           'hall_symbol': 'P 2 2',
                           'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},     # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},   # x, -y, -z
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},   # -x, y, -z
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},  # -x, -y, z
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [0.0, 1 / 2.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0],
                                            [1 / 2.0, 1 / 2.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                           'latt': 1, 'symm_cards': ['SYMM -x, -y, z\n', 'SYMM x, -y, -z\n', 'SYMM -x, y, -z\n']}

dictio_space_groups[17] = {'symbol': 'P 2 2 21', 'short_symbol': 'P2221', 'xHM_symbol': 'P 2 2 21',
                           'hall_symbol': 'P 2c 2' ,'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x, -y, z+1/2
    3: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y, -z+1/2
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}}, # x, -y, -z
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [0.0, 1 / 2.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0],
                                            [1 / 2.0, 1 / 2.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                           'latt': 1,
                           'symm_cards': ['SYMM -x, -y, z+0.5\n','SYMM -x, y, -z+0.5\n', 'SYMM x, -y, -z\n']}

# NOTE CM: Not tested, only two proteins in the PDB
dictio_space_groups['P2122']= {'symbol': 'P 21 2 2', 'short_symbol': 'P2122', 'xHM_symbol': 'P 21 2 2',
                               'hall_symbol': 'P 2c 2 (z,x,y)', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},  # x, y, z
    2: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},  # x+1/2, -y, -z
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},  # -x, y, -z
    4: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},  # -x+1/2 , -y, z
                       'point': 222, 'laue': '2/mm',
                       'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],[0.0, 1 / 2.0, 1 / 2.0],
                       [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                       [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                               'symm_cards': ['SYMM x+0.5, -y, -z\n','SYMM -x+0.5, -y, z\n','SYMM -x, y, -z\n']}

# NOTE CM: Not tested, only three proteins in the PDB
dictio_space_groups['P2212']= {'symbol': 'P 2 21 2', 'short_symbol': 'P2212','xHM_symbol': 'P 2 21 2',
                               'hall_symbol': 'P 2c 2 (y,z,x)', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y+1/2, -z
    3: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y+1/2, -z
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}} # -x, -y, z
    ,
                       'point': 222, 'laue': '2/mm',
                       'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],[0.0, 1 / 2.0, 1 / 2.0],
                       [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                       [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                        'latt': 1,'symm_cards': ['SYMM -x, y+0.5, -z\n','SYMM x, -y+0.5, -z\n','SYMM -x, -y, z\n']}


dictio_space_groups[18] = {'symbol': 'P 21 21 2', 'short_symbol': 'P21212', 'xHM_symbol': 'P 21 21 2',
                               'hall_symbol': 'P 2 2ab' ,'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x, -y, z
    3: {'tra': [1/2.0, 1/2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x+1/2, y+1/2, -z
    4: {'tra': [1/2.0, 1/2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2, -y+1/2, -z
    },
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [0.0, 1 / 2.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0],
                                            [1 / 2.0, 1 / 2.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                           'latt': 1,
                           'symm_cards': ['SYMM -x, -y, z\n', 'SYMM -x+0.5, y+0.5, -z\n', 'SYMM x+0.5, -y+0.5, -z\n']}

dictio_space_groups['P22121'] = {'symbol': 'P 2 21 21', 'short_symbol': 'P22121', 'xHM_symbol': 'P 2 21 21',
                               'hall_symbol': 'P 2 2ab (z,x,y)' ,'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y, -z
    3: {'tra': [0.0, 1/2.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y+1/2, -z+1/2
    4: {'tra': [0.0, 1/2.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}}, # -x, -y+1/2, z+1/2
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [0.0, 1 / 2.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0],
                                            [1 / 2.0, 1 / 2.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                           'latt': 1,
                           'symm_cards': ['SYMM x, -y, -z\n', 'SYMM -x, y+0.5, -z+0.5\n', 'SYMM -x, -y+0.5, z+0.5\n']}

dictio_space_groups['P21221']={'symbol': 'P 21 2 21', 'short_symbol': 'P21221', 'xHM_symbol': 'P 21 2 21',
                               'hall_symbol': 'P 2 2ab (y,z,x)' ,'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [1/2.0, 0.0, 1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2, -y, -z+1/2
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y, -z
    4: {'tra': [1/2.0, 0.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}}, # -x+1/2, -y, z+1/2
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [0.0, 1 / 2.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0],
                                            [1 / 2.0, 1 / 2.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                           'latt': 1,
                           'symm_cards': ['SYMM -x, y, -z\n', 'SYMM -x+0.5, -y, z+0.5\n', 'SYMM x+0.5, -y, -z+0.5\n']}


dictio_space_groups[19] = {'symbol': 'P 21 21 21', 'short_symbol': 'P212121','xHM_symbol': 'P 21 21 21',
                            'hall_symbol': 'P 2ac 2ab','symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [1/2.0, 0.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x+1/2, -y, z+1/2
    3: {'tra': [0.0, 1/2.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y+1/2, -z+1/2
    4: {'tra': [1/2.0, 1/2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2, -y+1/2, -z
    },
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [0.0, 1 / 2.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0], [1 / 2.0, 0.0, 1 / 2.0],
                                            [1 / 2.0, 1 / 2.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                           'latt': 1, 'symm_cards': ['SYMM x+0.5, -y+0.5, -z\n', 'SYMM -x, y+0.5, -z+0.5\n',
                                                     'SYMM -x+0.5, -y, z+0.5\n']}

dictio_space_groups[20] = {'symbol': 'C 2 2 21', 'short_symbol': 'C2221', 'xHM_symbol': 'C 2 2 21',
                            'hall_symbol': 'C 2c 2' ,'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y, -z
    3: {'tra': [0.0, 0.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y, -z+1/2
    4: {'tra': [0.0, 0.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x, -y, z+1/2
    5: {'tra': [1/2.0, 1/2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x+1/2, y+1/2, z
    6: {'tra': [1/2.0, 1/2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2, -y+1/2, -z
    7: {'tra': [1/2.0, 1/2.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x+1/2, y+1/2, -z+1/2
    8: {'tra': [1/2.0, 1/2.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}}, # -x+1/2, -y+1/2, z+1/2
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0],
                                            [1 / 2.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 7,
                           'symm_cards': ['SYMM -x, y, -z+0.5\n', 'SYMM -x, -y, z+0.5\n', 'SYMM x, -y, -z\n']}

# NOTE CM: Not tested, only one structure in the pdb and it is DNA
dictio_space_groups['B2212'] = {'symbol': 'B 2 21 2', 'short_symbol': 'B2212', 'xHM_symbol':'B 2 21 2' ,
                            'hall_symbol': 'B 2 2b', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x,y,z

    2: {'tra': [0.0, 1/2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y+1/2, -z

    3: {'tra': [1/2.0, 1/2.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x+1/2, y+1/2, -z+1/2

    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x, -y, z

    5: {'tra': [1/2.0, 0.0, 1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x+1/2, y, z+1/2

    6: {'tra': [1/2.0, 1/2.0, 1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2,-y+1/2,-z+1/2

    7: {'tra': [0.0, 1/2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y+1/2, -z

    8: {'tra': [1/2.0, 0.0, 1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]} #  -x+1/2,-y,z+1/2
    },
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0],
                                            [1 / 2.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 6,
                           'symm_cards': ['SYMM x, -y+0.5, -z\n', 'SYMM -x, y+0.5, -z\n', 'SYMM -x, -y, z\n']}

# NOTE CM: Not tested, no structures deposited at the pdb
dictio_space_groups['A2122'] = {'symbol': 'A 21 2 2', 'short_symbol': 'A2122', 'xHM_symbol':'A 21 2 2' ,
                            'hall_symbol': 'A 2a 2a', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [1/2.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2,-y,-z
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y, -z
    4: {'tra': [1/2.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x+1/2, -y, z
    5: {'tra': [0.0,1/2.0,1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x,y+1/2,z+1/2
    6: {'tra': [1/2.0,1/2.0,1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2,-y+1/2,-z+1/2
    7: {'tra': [0.0,1/2.0,1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x,y+1/2,-z+1/2
    8: {'tra': [1/2.0,1/2.0,1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]} # -x+1/2,-y+1/2,z+1/2
},
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0],
                                            [1 / 2.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 5,
                           'symm_cards': None} # TODO: produce these symm cards


dictio_space_groups[21] = {'symbol': 'C 2 2 2', 'short_symbol': 'C222','xHM_symbol':'C 2 2 2' ,
                            'hall_symbol':'C 2 2', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0],
                                            [1 / 2.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 7,
                           'symm_cards': ['SYMM -x, -y, z\n', 'SYMM x, -y, -z\n', 'SYMM -x, y, -z\n']}

# NOTE CM: Not tested, there are not structures deposited at the PDB
dictio_space_groups['A222']={'symbol': 'A 2 2 2', 'short_symbol': 'A222','xHM_symbol':'A 2 2 2' ,
                            'hall_symbol':'A 2 2', 'symops': {
    1: {'tra': [0.0,0.0,0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0,0.0,0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y, -z
    3: {'tra': [0.0,0.0,0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y, -z
    4: {'tra': [0.0,0.0,0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x, -y, z
    5: {'tra': [0.0,1/2.0,1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y+1/2, z+1/2
    6: {'tra': [0.0,1/2.0,1/2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y+1/2, -z+1/2
    7: {'tra': [0.0,1/2.0,1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y+1/2, -z+1/2
    8: {'tra': [0.0,1/2.0,1/2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}}, # -x, -y+1/2, z+1/2
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0],
                                            [1 / 2.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 5,
                           'symm_cards': None} # TODO: produce these symm cards

# NOTE CM: Not tested, there are not structures deposited at the PDB
dictio_space_groups['B222'] = {'symbol': 'B 2 2 2', 'short_symbol': 'B222','xHM_symbol':'B 2 2 2' ,
                            'hall_symbol':'B 2 2', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x, -y, -z
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x, y, -z
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}, # -x, -y, z
    5: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]}, # x+1/2, y, z+1/2
    6: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2, -y, -z+1/2
    7: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x+1/2, y, -z+1/2
    8: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}}, # -x+1/2, -y, z+1/2
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 0.0, 0.0],
                                            [1 / 2.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 6,
                           'symm_cards': None} # TODO: produce these symm cards

dictio_space_groups[22] = {'symbol': 'F 2 2 2', 'short_symbol': 'F222', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    10: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    13: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    14: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    16: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [1 / 4.0, 1 / 4.0, 1 / 4.0], [1 / 2.0, 1 / 2.0, 1 / 2.0],
                                            [3 / 4.0, 3 / 4.0, 3 / 4.0]], 'polar': False, 'latt': 4,
                           'symm_cards': ['SYMM -x, -y, z\n', 'SYMM x, -y, -z\n', 'SYMM -x, y, -z\n']}

dictio_space_groups[23] = {'symbol': 'I 2 2 2', 'short_symbol': 'I222', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'point': 222, 'laue': '2/mm',
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 0.0, 0.0]], 'polar': False, 'latt': 2,
                           'symm_cards': ['SYMM -x, -y, z\n', 'SYMM x, -y, -z\n', 'SYMM -x, y, -z\n']}

dictio_space_groups[24] = {'symbol': 'I 21 21 21', 'short_symbol': 'I212121', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    3: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    4: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [0.0, 1 / 2.0, 0.0],
                            [1 / 2.0, 0.0, 0.0]],
                           'polar': False, 'latt': 2, 'point': 222, 'laue': '2/mm',
                           'symm_cards': ['SYMM x+0.5, -y+0.5, -z\n', 'SYMM -x, y+0.5, -z+0.5\n',
                                          'SYMM -x+0.5, -y, z+0.5\n']}

dictio_space_groups[75] = {'symbol': 'P 4', 'short_symbol': 'P4', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, z], [1 / 2.0, 1 / 2.0, z]], 'polar': True, 'latt': 1,
                           'symm_cards': ['SYMM -x, -y, z\n', 'SYMM -y, x, z\n', 'SYMM y, -x, z\n']}

dictio_space_groups[76] = {'symbol': 'P 41', 'short_symbol': 'P41', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, z], [1 / 2.0, 1 / 2.0, z]], 'polar': True, 'latt': 1,
                           'symm_cards': ['SYMM y, -x, z+0.75\n', 'SYMM -y, x, z+0.25\n', 'SYMM -x, -y, z+0.5\n']}

dictio_space_groups[77] = {'symbol': 'P 42', 'short_symbol': 'P42', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, z], [1 / 2.0, 1 / 2.0, z]], 'polar': True, 'latt': 1,
                           'symm_cards': ['SYMM -y, x, z+0.5\n', 'SYMM -x, -y, z\n',
                                          'SYMM y, -x, z+0.5\n']}

dictio_space_groups[78] = {'symbol': 'P 43', 'short_symbol': 'P43', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, z], [1 / 2.0, 1 / 2.0, z]], 'polar': True, 'latt': 1,
                           'symm_cards': ['SYMM -y, x, z+0.75\n', 'SYMM -x, -y, z+1.5\n', 'SYMM -x, -y, z+0.5\n',
                                          'SYMM y, -x, z+1.25\n', 'SYMM y, -x, z+2.25\n', '']}

dictio_space_groups[79] = {'symbol': 'I 4', 'short_symbol': 'I4', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 2,
                           'symm_cards': ['SYMM -x, -y, z\n', 'SYMM -y, x, z\n', 'SYMM y, -x, z\n']}

dictio_space_groups[80] = {'symbol': 'I 41', 'short_symbol': 'I41', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 2.0, 0.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [1 / 2.0, 0.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [1.0, 1 / 2.0, 0.625], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [1.0, 1 / 2.0, 0.625], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                           'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 2,
                           'symm_cards': ['SYMM -x+0.5, -y+0.5, z+0.5\n', 'SYMM y+0.5, -x, z+0.75\n',
                                          'SYMM -y, x+0.5, z+0.25\n']}

dictio_space_groups[89] = {'symbol': 'P 4 2 2', 'short_symbol': 'P422', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},      # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},     # -y, x, z
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},     # y, -x, z
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},    # x, -y, -z
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},    # -x, y, -z
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},    # -x, -y, z
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},     # y, x, -z
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},  # -y, -x, -z
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM -y, -x, -z\n', 'SYMM y, -x, z\n', 'SYMM y, x, -z\n', 'SYMM -x, -y, z\n',
                                          'SYMM x, -y, -z\n', 'SYMM -y, x, z\n', 'SYMM -x, y, -z\n']}

dictio_space_groups[90] = {'symbol': 'P 4 21 2', 'short_symbol': 'P4212', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM -y+0.5, x+0.5, z\n', 'SYMM -x, -y, z\n', 'SYMM -x, -y, z\n',
                                          'SYMM x+0.5, -y+0.5, -z\n', 'SYMM y, x, -z\n', 'SYMM y+0.5, -x+0.5, z\n',
                                          'SYMM -y, -x, -z\n', 'SYMM -x+0.5, y+0.5, -z\n']}

dictio_space_groups[91] = {'symbol': 'P 41 2 2', 'short_symbol': 'P4122', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},          # x, y, z
    2: {'tra': [0.0, 0.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},     # -y, x, z+1/4
    3: {'tra': [0.0, 0.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},     # y, -x, z+3/4
    4: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},    # x, -y, -z+1/2
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},        # -x, y, -z
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},    # -x, -y, z+1/2
    7: {'tra': [0.0, 0.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},     # y, x, -z+3/4
    8: {'tra': [0.0, 0.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},  # -y, -x, -z+1/4
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM -x, -y, z+0.5\n', 'SYMM -y, x, z+0.25\n', 'SYMM x, -y, -z+0.5\n',
                                          'SYMM -y, -x, -z+0.25\n', 'SYMM y, -x, z+0.75\n', 'SYMM -x, y, -z\n',
                                          'SYMM y, x, -z+0.75\n']}

dictio_space_groups[92] = {'symbol': 'P 41 21 2', 'short_symbol': 'P41212', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},               # x, y, z
    2: {'tra': [1/2.0, 1/2.0, 1/4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},        # -y+1/2, x+1/2, z+1/4
    3: {'tra': [1 / 2.0, 1 / 2.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},  # y+1/2, -x+1/2, z+3/4
    4: {'tra': [1 / 2.0, 1 / 2.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}, # x+1/2, -y+1/2, -z+3/4
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]}, # -x+1/2, y+1/2, -z+1/4
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},         # -x, -y, z+1/2
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},              # y, x, -z
    8: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},       # -y, -x, -z+1/2
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'point': 422, 'laue': '4/mm',
                           'symm_cards': ['SYMM -x, -y, z+0.5\n', 'SYMM -x+0.5, y+0.5, -z+0.25\n',
                                          'SYMM y+0.5, -x+0.5, z+0.75\n', 'SYMM x+0.5, -y+0.5, -z+0.75\n',
                                          'SYMM -y+0.5, x+0.5, z+0.25\n', 'SYMM -y, -x, -z+0.5\n', 'SYMM y, x, -z\n']}

dictio_space_groups[93] = {'symbol': 'P 42 2 2', 'short_symbol': 'P4222', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM y, -x, z+0.5\n', 'SYMM -x, -y, z\n', 'SYMM x, -y, -z\n',
                                          'SYMM -x, -y, z\n', 'SYMM -y, x, z+0.5\n', 'SYMM x, -y, -z\n',
                                          'SYMM -y, -x, -z+0.5\n', 'SYMM y, x, -z+0.5\n', 'SYMM -x, y, -z\n']}

dictio_space_groups[94] = {'symbol': 'P 42 21 2', 'short_symbol': 'P42212', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM x+0.5, -y+0.5, -z+0.5\n', 'SYMM -x, -y, z\n',
                                          'SYMM -y+0.5, x+0.5, z+0.5\n', 'SYMM -x+0.5, y+0.5, -z+0.5\n',
                                          'SYMM y, x, -z\n','SYMM -y, -x, -z\n', 'SYMM y+0.5, -x+0.5, z+0.5\n']}

dictio_space_groups[95] = {'symbol': 'P 43 2 2', 'short_symbol': 'P4322', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM -y, x, z+0.75\n', 'SYMM -x, -y, z+1.5\n', 'SYMM -x, -y, z+0.5\n',
                                          'SYMM y, x, -z+0.25\n', 'SYMM y, -x, z+1.25\n', 'SYMM x, -y, -z+0.5\n',
                                          'SYMM -x, y, -z\n', 'SYMM y, -x, z+2.25\n', 'SYMM -y, -x, -z+0.75\n']}

dictio_space_groups[96] = {'symbol': 'P 43 21 2', 'short_symbol': 'P43212', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 2.0, 1 / 2.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [1 / 2.0, 1 / 2.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 2.0, 1 / 2.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 2.0, 1 / 2.0, 0.0],
                                            [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                           'symm_cards': ['SYMM 0.5-y, 0.5+x, 0.75+z\n', 'SYMM -x, -y, 0.5+z\n',
                                          'SYMM 0.5+y, 0.5-x, 0.25+z\n', 'SYMM 0.5-x, 0.5+y, 0.75-z\n',
                                          'SYMM y, x, -z\n', 'SYMM 0.5+x, 0.5-y, 0.25-z\n', 'SYMM -y, -x, 0.5-z\n']}

dictio_space_groups[97] = {'symbol': 'I 4 2 2', 'short_symbol': 'I422', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    9: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    10: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    11: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    12: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    13: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    14: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    16: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 2,
                           'symm_cards': ['SYMM -y, -x, -z\n', 'SYMM y, -x, z\n', 'SYMM y, x, -z\n', 'SYMM -x, -y, z\n',
                                          'SYMM x, -y, -z\n', 'SYMM -y, x, z\n', 'SYMM -x, y, -z\n']}

dictio_space_groups[98] = {'symbol': 'I 41 2 2', 'short_symbol': 'I4122', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 2.0, 0.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [1 / 2.0, 0.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 2.0, 0.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [1 / 2.0, 0.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    9: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    10: {'tra': [1.0, 1 / 2.0, 0.625], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    11: {'tra': [1.0, 1 / 2.0, 0.625], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    12: {'tra': [1.0, 1 / 2.0, 0.625], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    13: {'tra': [1.0, 1 / 2.0, 0.625], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    14: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    16: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                           'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 2,
                           'symm_cards': ['SYMM -y, x+0.5, z+0.25\n', 'SYMM -x+0.5, -y+0.5, z+0.5\n',
                                          'SYMM y+0.5, -x, z+0.75\n', 'SYMM y+0.5, x+0.5, -z+0.5\n',
                                          'SYMM -x+0.5, y, -z+0.75\n', 'SYMM x, -y+0.5, -z+1.25\n', 'SYMM -y, -x, -z\n',
                                          'SYMM x, -y+0.5, -z+0.25\n']}

dictio_space_groups[143] = {'symbol': 'P 3', 'short_symbol': 'P3', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, z], [1 / 3.0, 2 / 3.0, z], [2 / 3.0, 1 / 3.0, z]],
                            'polar': True, 'latt': 1,
                            'symm_cards': ['SYMM -x+y, -x, z\n', 'SYMM -y, x-y, z\n']}

dictio_space_groups[144] = {'symbol': 'P 31', 'short_symbol': 'P31', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, z], [1 / 3.0, 2 / 3.0, z], [2 / 3.0, 1 / 3.0, z]],
                            'polar': True, 'latt': 1,
                            'symm_cards': ['SYMM -y, x-y, z+0.333333333333\n','SYMM -x+y, -x, z+0.666666666667\n']}

dictio_space_groups[145] = {'symbol': 'P 32', 'short_symbol': 'P32', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, z], [1 / 3.0, 2 / 3.0, z], [2 / 3.0, 1 / 3.0, z]],
                            'polar': True, 'latt': 1,
                            'symm_cards': ['SYMM -y, x-y, z+0.666666666667\n','SYMM -x+y, -x, z+0.333333333333\n']}

dictio_space_groups[146] = {'symbol': 'H 3', 'short_symbol': 'H3', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'point': 3, 'laue': '-3',
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 3,
                            'symm_cards': ['SYMM -x+y, -x, z\n', 'SYMM -y, x-y, z\n']}

dictio_space_groups['R 3'] = {'symbol': 'R 3', 'short_symbol': 'R3', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]}},
                              'origins_list': [[x, x, x]], 'polar': True, 'latt': 1,
                              'symm_cards': ['SYMM y, z, x\n', 'SYMM z, x, y\n']}

dictio_space_groups[149] = {'symbol': 'P 3 1 2', 'short_symbol': 'P312', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 3.0, 2 / 3.0, 0.0],
                                             [1 / 3.0, 2 / 3.0, 1 / 2.0], [2 / 3.0, 1 / 3.0, 0.0],
                                             [2 / 3.0, 1 / 3.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM x, x-y, -z\n','SYMM -y, -x, -z\n','SYMM -x+y, y, -z\n',
                                           'SYMM -x+y, -x, z\n','SYMM -y, x-y, z\n']}

dictio_space_groups[150] = {'symbol': 'P 3 2 1', 'short_symbol': 'P321', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards':['SYMM x-y, -y, -z\n', 'SYMM -x, -x+y, -z\n', 'SYMM y, x, -z\n',
                                          'SYMM -x+y, -x, z\n', 'SYMM -y, x-y, z\n']}


dictio_space_groups[151] = {'symbol': 'P 31 1 2', 'short_symbol': 'P3112', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 3.0, 2 / 3.0, 0.0],
                                             [1 / 3.0, 2 / 3.0, 1 / 2.0], [2 / 3.0, 1 / 3.0, 0.0],
                                             [2 / 3.0, 1 / 3.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards':['SYMM y, x, -z\n', 'SYMM -y, x-y, z+0.333333333333\n',
                                          'SYMM -x+y, -x, z+0.666666666667\n', 'SYMM x-y, -y, -z+0.666666666667\n',
                                          'SYMM -x, -x+y, -z+0.333333333333\n']}

dictio_space_groups[152] = {'symbol': 'P 31 2 1', 'short_symbol': 'P3121', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM y, x, -z\n', 'SYMM -y, x-y, z+0.333333333333\n',
                                           'SYMM -x+y, -x, z+0.666666666667\n', 'SYMM x-y, -y, -z+0.666666666667\n',
                                           'SYMM -x, -x+y, -z+0.333333333333\n']}

dictio_space_groups[153] = {'symbol': 'P 32 1 2', 'short_symbol': 'P3212', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0], [1 / 3.0, 2 / 3.0, 0.0],
                                             [1 / 3.0, 2 / 3.0, 1 / 2.0], [2 / 3.0, 1 / 3.0, 0.0],
                                             [2 / 3.0, 1 / 3.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM -y, x-y, z+0.666666666667\n', 'SYMM -x+y, -x, z+0.333333333333\n',
                                           'SYMM -y, -x, -z+0.333333333333\n', 'SYMM x, x-y, -z\n',
                                           'SYMM -x+y, y, -z+0.666666666667\n']}

dictio_space_groups[154] = {'symbol': 'P 32 2 1', 'short_symbol': 'P3221', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM -y, x-y, z+0.666666666667\n', 'SYMM -x+y, -x, z+0.333333333333\n',
                                           'SYMM y, x, -z\n', 'SYMM -x, -x+y, -z+0.666666666667\n',
                                           'SYMM x-y, -y, -z+0.333333333333\n']}

dictio_space_groups[155] = {'symbol': 'H 3 2', 'short_symbol': 'H32', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    10: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [1 / 3.0, 2 / 3.0, 2 / 3.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    13: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    14: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    15: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    16: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [2 / 3.0, 1 / 3.0, 1 / 3.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 3,
                            'symm_cards': ['SYMM x-y, -y, -z\n', 'SYMM -x, -x+y, -z\n', 'SYMM y, x, -z\n',
                                           'SYMM -x+y, -x, z\n', 'SYMM -y, x-y, z\n']}

dictio_space_groups['R 3 2'] = {'symbol': 'R 3 2', 'short_symbol': 'R32', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                                'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False,
                                'latt': 1, 'symm_cards': ['SYMM -z, -y, -x\n', 'SYMM -x, -z, -y\n', 'SYMM y, z, x\n',
                                                          'SYMM -y, -x, -z\n', 'SYMM z, x, y\n']}

dictio_space_groups[168] = {'symbol': 'P 6', 'short_symbol': 'P6', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},         # x, y, z
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},        # x-y, x, z
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},        # y, -x+y, z
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},       # -y, x-y, z
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},       # -x+y, -x, z
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},      # -x, -y, z
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 1, 'point': 6, 'laue': '6/m',
                            'symm_cards': ['SYMM x-y, x, z\n', 'SYMM -x, -y, z\n', 'SYMM -x+y, -x, z\n',
                                           'SYMM -y, x-y, z\n', 'SYMM y, -x+y, z\n']}

dictio_space_groups[169] = {'symbol': 'P 61', 'short_symbol': 'P61', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},         # x, y, z
    2: {'tra': [0.0, 0.0, 1 / 6.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},    # x-y, x, z+1/6
    3: {'tra': [0.0, 0.0, 5 / 6.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},    # y, -x+y, z+5/6
    4: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},   # -y, x-y, z+1/3
    5: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},   # -x+y, -x, z+2/3
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},  # -x, -y, z+1/2
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 1, 'point': 6, 'laue': '6/m',
                            'symm_cards': ['SYMM y, -x+y, z+0.833333333333\n', 'SYMM -x, -y, z+0.5\n',
                                           'SYMM -y, x-y, z+0.333333333333\n', 'SYMM x-y, x, z+0.166666666667\n',
                                           'SYMM -x+y, -x, z+0.666666666667\n']}

dictio_space_groups[170] = {'symbol': 'P 65', 'short_symbol': 'P65', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},         # x, y, z
    2: {'tra': [0.0, 0.0, 5 / 6.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},    # x-y, x, z+5/6
    3: {'tra': [0.0, 0.0, 1 / 6.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},    # y, -x+y, z+1/6
    4: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},   # -y, x-y, z+2/3
    5: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},   # -x+y, -x, z+1/3
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},  # -x, -y, z+1/2
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 1, 'point': 6, 'laue': '6/m',
                            'symm_cards': ['SYMM -y, x-y, z+0.666666666667\n', 'SYMM -x+y, -x, z+0.333333333333\n',
                                           'SYMM x-y, x, z+0.833333333333\n', 'SYMM -x, -y, z+0.5\n',
                                           'SYMM y, -x+y, z+0.166666666667\n']}

dictio_space_groups[171] = {'symbol': 'P 62', 'short_symbol': 'P62', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},        # x, y, z
    2: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},   # x-y, x, z+1/3
    3: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},   # y, -x+y, z+2/3
    4: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},  # -y, x-y, z+2/3
    5: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},  # -x+y, -x, z+1/3
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},     # -x, -y, z
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 1, 'point': 6, 'laue': '6/m',
                            'symm_cards': ['SYMM -y, x-y, z+0.666666666667\n', 'SYMM y, -x+y, z+0.666666666667\n',
                                           'SYMM -x, -y, z\n', 'SYMM -x+y, -x, z+0.333333333333\n',
                                           'SYMM x-y, x, z+0.333333333333\n']}

dictio_space_groups[172] = {'symbol': 'P 64', 'short_symbol': 'P64', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},        # x, y, z
    2: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},   # x-y, x, z+2/3
    3: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},   # y, -x+y, z+1/3
    4: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},  # -y, x-y, z+1/3
    5: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},  # -x+y, -x, z+2/3
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},     # -x, -y, z
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 1, 'point': 6, 'laue': '6/m',
                            'symm_cards': ['SYMM y, -x+y, z+0.333333333333\n','SYMM -x, -y, z\n',
                                           'SYMM -y, x-y, z+0.333333333333\n','SYMM x-y, x, z+0.666666666667\n',
                                           'SYMM -x+y, -x, z+0.666666666667\n']}

dictio_space_groups[173] = {'symbol': 'P 63', 'short_symbol': 'P63', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},         # x, y, z
    2: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},    # x-y , x, z+1/2
    3: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},    # y, -x+y, z+1/2
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},       # -y, x-y, z
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},       # -x+y, -x, z
    6: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},  # -x, -y, z+1/2
                            'origins_list': [[0.0, 0.0, z]], 'polar': True, 'latt': 1, 'point': 6, 'laue': '6/m',
                            'symm_cards': ['SYMM -x, -y, z+0.5\n','SYMM -x+y, -x, z\n','SYMM -y, x-y, z\n',
                                           'SYMM x-y, x, z+0.5\n','SYMM y, -x+y, z+0.5\n']}

dictio_space_groups[177] = {'symbol': 'P 6 2 2', 'short_symbol': 'P622', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point':'622','laue':'6/mmm',
                            'symm_cards': ['SYMM x, x-y, -z\n','SYMM -y, -x, -z\n','SYMM x-y, x, z\n',
                                           'SYMM -x, -x+y, -z\n','SYMM y, x, -z\n','SYMM -x, -y, z\n',
                                           'SYMM -x+y, -x, z\n','SYMM x-y, -y, -z\n','SYMM -x+y, y, -z\n',
                                           'SYMM -y, x-y, z\n','SYMM y, -x+y, z\n']}

dictio_space_groups[178] = {'symbol': 'P 61 2 2', 'short_symbol': 'P6122', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 6.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 5 / 6.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    10: {'tra': [0.0, 0.0, 5 / 6.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 1 / 6.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point': '622', 'laue': '6/mmm',
                            'symm_cards':['SYMM -Y, X-Y, 1/3+Z\n','SYMM -X+Y, -X, 2/3+Z\n','SYMM -X, -Y, 1/2+Z\n',
                                          'SYMM Y, -X+Y, 5/6+Z\n','SYMM X-Y, X, 1/6+Z\n','SYMM Y, X, 1/3-Z\n',
                                          'SYMM X-Y, -Y, -Z\n','SYMM -X, -X+Y, 2/3-Z\n','SYMM -Y, -X, 5/6-Z\n',
                                          'SYMM -X+Y, Y, 1/2-Z\n','SYMM X, X-Y, 1/6-Z\n']}

dictio_space_groups[179] = {'symbol': 'P 65 2 2', 'short_symbol': 'P6522', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 5 / 6.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 6.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    10: {'tra': [0.0, 0.0, 1 / 6.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 5 / 6.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point':'622','laue':'6/mmm',
                            'symm_cards': ['SYMM -Y, X-Y, 2/3+Z\n','SYMM -X+Y, -X, 1/3+Z\n','SYMM -X, -Y, 1/2+Z\n',
                                           'SYMM Y, -X+Y, 1/6+Z\n','SYMM X-Y, X, 5/6+Z\n','SYMM Y, X, 2/3-Z\n',
                                           'SYMM X-Y, -Y, -Z\n','SYMM -X, -X+Y, 1/3-Z\n','SYMM -Y, -X, 1/6-Z\n',
                                           'SYMM -X+Y, Y, 1/2-Z\n','SYMM X, X-Y, 5/6-Z\n']}


dictio_space_groups[180] = {'symbol': 'P 62 2 2', 'short_symbol': 'P6222', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    10: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point':'622','laue':'6/mmm',
                            'symm_cards': ['SYMM -Y, X-Y, 2/3+Z\n','SYMM -X+Y, -X, 1/3+Z\n','SYMM -X, -Y, Z\n',
                                           'SYMM Y, -X+Y, 2/3+Z\n','SYMM X-Y, X, 1/3+Z\n','SYMM Y, X, 2/3-Z\n',
                                           'SYMM X-Y, -Y, -Z\n','SYMM -X, -X+Y, 1/3-Z\n','SYMM -Y, -X, 2/3-Z\n',
                                           'SYMM -X+Y, Y, -Z\n','SYMM X, X-Y, 1/3-Z\n']}

dictio_space_groups[181] = {'symbol': 'P 64 2 2', 'short_symbol': 'P6422', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    10: {'tra': [0.0, 0.0, 1 / 3.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 2 / 3.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point':'622','laue':'6/mmm',
                            'symm_cards': ['SYMM y, x, -z+0.333333333333\n','SYMM y, -x+y, z+0.333333333333\n',
                                           'SYMM -x+y, y, -z\n','SYMM -x, -y, z\n','SYMM -y, x-y, z+0.333333333333\n',
                                           'SYMM x-y, -y, -z\n','SYMM x-y, x, z+0.666666666667\n',
                                           'SYMM -x+y, -x, z+0.666666666667\n','SYMM -y, -x, -z+0.333333333333\n',
                                           'SYMM -x, -x+y, -z+0.666666666667\n','SYMM x, x-y, -z+0.666666666667\n']}

dictio_space_groups[182] = {'symbol': 'P 63 2 2', 'short_symbol': 'P6322', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    3: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, -1.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    8: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    10: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [1.0, -1.0, 0.0], [0.0, 0.0, -1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [0.0, 0.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point':'622','laue':'6/mmm',
                            'symm_cards': ['SYMM x-y, -y, -z\n','SYMM -x, -y, z+0.5\n','SYMM -x, -x+y, -z\n',
                                           'SYMM y, x, -z\n','SYMM -x+y, -x, z\n','SYMM x, x-y, -z+0.5\n',
                                           'SYMM -x+y, y, -z+0.5\n','SYMM -y, x-y, z\n','SYMM x-y, x, z+0.5\n',
                                           'SYMM -y, -x, -z+0.5\n','SYMM y, -x+y, z+0.5\n',]}

dictio_space_groups[195] = {'symbol': 'P 2 3', 'short_symbol': 'P23', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM z, x, y\n', 'SYMM x, -y, -z\n', 'SYMM -x, -y, z\n', 'SYMM z, -x, -y\n',
                                           'SYMM -y, z, -x\n', 'SYMM -y, -z, x\n', 'SYMM y, z, x\n', 'SYMM -z, x, -y\n',
                                           'SYMM -x, y, -z\n', 'SYMM -z, -x, y\n']}

dictio_space_groups[196] = {'symbol': 'F 2 3', 'short_symbol': 'F23', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    13: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    14: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    15: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    17: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    18: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    19: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    20: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    21: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    22: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    23: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    24: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    25: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    26: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    27: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    28: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    29: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    30: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    31: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    32: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    33: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    34: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    35: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    36: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    37: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    38: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    39: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    40: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    41: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    42: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    43: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    44: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    45: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    46: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    47: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    48: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 4.0, 1 / 4.0, 1 / 4.0], [1 / 2.0, 1 / 2.0, 1 / 2.0],
                                             [3 / 4.0, 3 / 4.0, 3 / 4.0]], 'polar': False, 'latt': 4,
                            'symm_cards': ['SYMM z, x, y\n','SYMM x, -y, -z\n','SYMM -x, -y, z\n','SYMM y, -z, -x\n',
                                           'SYMM z, -x, -y\n','SYMM -y, z, -x\n','SYMM -y, -z, x\n','SYMM y, z, x\n',
                                           'SYMM -z, x, -y\n','SYMM -x, y, -z\n','SYMM -z, -x, y\n']}




dictio_space_groups[197] = {'symbol': 'I 2 3', 'short_symbol': 'I23', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    13: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    14: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    16: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    17: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    18: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    19: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    20: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    21: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    22: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    23: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    24: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0]], 'polar': False, 'latt': 2,
                            'symm_cards': ['SYMM z, x, y\n', 'SYMM x, -y, -z\n', 'SYMM -x, -y, z\n', 'SYMM z, -x, -y\n',
                                           'SYMM -y, z, -x\n', 'SYMM -y, -z, x\n', 'SYMM y, z, x\n', 'SYMM -z, x, -y\n',
                                           'SYMM -x, y, -z\n', 'SYMM -z, -x, y\n']}

dictio_space_groups[198] = {'symbol': 'P 21 3', 'short_symbol': 'P213', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    4: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    6: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    7: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    8: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    9: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    10: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM -z, x+0.5, -y+0.5\n', 'SYMM z, x, y\n', 'SYMM -x, y+0.5, -z+0.5\n',
                                           'SYMM z+0.5, -x+0.5, -y\n', 'SYMM y+0.5, -z+0.5, -x\n',
                                           'SYMM -z+0.5, -x, y+0.5\n', 'SYMM x+0.5, -y+0.5, -z\n',
                                           'SYMM -y, z+0.5, -x+0.5\n','SYMM y, z, x\n', 'SYMM -y+0.5, -z, x+0.5\n',
                                           'SYMM -x+0.5, -y, z+0.5\n']}



dictio_space_groups[199] = {'symbol': 'I 21 3', 'short_symbol': 'I213', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    4: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    6: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    7: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    8: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    11: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    12: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    13: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    14: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    16: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    17: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    18: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    19: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    20: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    21: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    22: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    23: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    24: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0]], 'polar': False, 'latt': 2,
                            'symm_cards': ['SYMM -y, -z, x+0.5\n', 'SYMM -x, -y, z+0.5\n', 'SYMM -x, y+0.5, -z\n',
                                           'SYMM -y, z+0.5, -x\n', 'SYMM z, x, y\n', 'SYMM -z, x+0.5, -y\n',
                                           'SYMM x, -y+0.5, -z+0.5\n', 'SYMM -z, -x, y+0.5\n', 'SYMM y, z, x\n',
                                           'SYMM z+0.5, -x, -y\n']}

dictio_space_groups[207] = {'symbol': 'P 4 3 2', 'short_symbol': 'P432', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM y, z, x\n', 'SYMM -y, x, z\n', 'SYMM y, -x, z\n',
                                           'SYMM -x, -y, z+0.5\n', 'SYMM -y, -z, x+0.5\n', 'SYMM y, x, -z\n',
                                           'SYMM z, x, y\n', 'SYMM x, z, -y\n', 'SYMM x, -y, -z+0.5\n',
                                           'SYMM -z, y, x\n', 'SYMM -z, -x, y+0.5\n', 'SYMM -x, y, -z\n',
                                           'SYMM -y, z, -x\n', 'SYMM z, y, -x\n', 'SYMM -y, -x, -z+0.5\n',
                                           'SYMM z+0.5, -x, -y\n', 'SYMM -z, x, -y\n', 'SYMM -z, -x, y\n']}

dictio_space_groups[208] = {'symbol': 'P 42 3 2', 'short_symbol': 'P4232', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'symm_cards': ['SYMM -z+0.5, y+0.5, x+0.5\n', 'SYMM -y, -z, x+0.5\n',
                                           'SYMM -x, -y, z+0.5\n', 'SYMM -y+0.5, -x+0.5, -z\n',
                                           'SYMM y+0.5, x+0.5, -z+0.5\n', 'SYMM z, x, y\n',
                                           'SYMM x+0.5, z+0.5, -y+0.5\n', 'SYMM x, -y, -z+0.5\n',
                                           'SYMM -z, -x, y+0.5\n', 'SYMM -x, y, -z\n', 'SYMM -y, z, -x\n',
                                           'SYMM -y+0.5, x+0.5, z+0.5\n', 'SYMM y, z, x\n', 'SYMM z+0.5, -x, -y\n',
                                           'SYMM -z, x, -y\n', 'SYMM z+0.5, y+0.5, -x+0.5\n',
                                           'SYMM y+0.5, -x+0.5, z+0.5\n', 'SYMM -z, -x, y\n']}

dictio_space_groups[209] = {'symbol': 'F 4 3 2', 'short_symbol': 'F432', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    25: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    26: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    27: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    28: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    29: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    30: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    31: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    32: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    33: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    34: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    35: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    36: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    37: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    38: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    39: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    40: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    41: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    42: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    43: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    44: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    45: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    46: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    47: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    48: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    49: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    50: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    51: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    52: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    53: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    54: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    55: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    56: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    57: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    58: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    59: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    60: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    61: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    62: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    63: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    64: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    65: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    66: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    67: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    68: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    69: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    70: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    71: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    72: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    73: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    74: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    75: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    76: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    77: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    78: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    79: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    80: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    81: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    82: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    83: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    84: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    85: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    86: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    87: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    88: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    89: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    90: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    91: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    92: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    93: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    94: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    95: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    96: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 4,
                            'symm_cards': ['SYMM y, z, x\n', 'SYMM -y, x, z\n', 'SYMM y, -x, z\n',
                                           'SYMM -x, -y, z+0.5\n', 'SYMM -y, -z, x+0.5\n', 'SYMM y, x, -z\n',
                                           'SYMM z, x, y\n', 'SYMM x, z, -y\n', 'SYMM x, -y, -z+0.5\n',
                                           'SYMM -z, y, x\n', 'SYMM -z, -x, y+0.5\n', 'SYMM -x, y, -z\n',
                                           'SYMM -y, z, -x\n', 'SYMM z, y, -x\n', 'SYMM -y, -x, -z+0.5\n',
                                           'SYMM z+0.5, -x, -y\n', 'SYMM -z, x, -y\n', 'SYMM -z, -x, y\n']}

dictio_space_groups[210] = {'symbol': 'F 41 3 2', 'short_symbol': 'F4132', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    25: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    26: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    27: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    28: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    29: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    30: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    31: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    32: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    33: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    34: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    35: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    36: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    37: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    38: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    39: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    40: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    41: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    42: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    43: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    44: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    45: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    46: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    47: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    48: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    49: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    50: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    51: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    52: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    53: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    54: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    55: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    56: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    57: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    58: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    59: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    60: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    61: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    62: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    63: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    64: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    65: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    66: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    67: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    68: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    69: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    70: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    71: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    72: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    73: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    74: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    75: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    76: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    77: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    78: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    79: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    80: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    81: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    82: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    83: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    84: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    85: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    86: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    87: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    88: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    89: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    90: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    91: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    92: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    93: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    94: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    95: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    96: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 4,
                            'symm_cards': ['SYMM -y+0.25, -x+0.25, -z+1.25\n', 'SYMM -z+0.75, y+0.75, x+0.25\n',
                                           'SYMM -x, -y+0.5, z+0.5\n', 'SYMM x+0.5, -y, -z+0.5\n',
                                           'SYMM -y+1.25, -x+0.25, -z+0.25\n', 'SYMM -z, -x+0.5, y+0.5\n',
                                           'SYMM z, x, y\n', 'SYMM z+0.75, y+0.25, -x+0.75\n',
                                           'SYMM -y+0.75, x+0.75, z+0.25\n', 'SYMM y+1.25, -x+0.75, z+0.75\n',
                                           'SYMM -z+0.5, x+0.5, -y\n', 'SYMM -y, -z+0.5, x+0.5\n',
                                           'SYMM y+0.75, x+0.25, -z+0.75\n', 'SYMM -x+0.5, y+0.5, -z\n',
                                           'SYMM y, z, x\n', 'SYMM -y+0.5, z+0.5, -x\n',
                                           'SYMM x+0.75, z+0.25, -y+0.75\n', 'SYMM z+0.5, -x, -y+0.5\n']}

dictio_space_groups[211] = {'symbol': 'I 4 3 2', 'short_symbol': 'I432', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [0.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    25: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    26: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    27: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    28: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    29: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    30: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    31: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    32: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    33: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    34: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    35: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    36: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    37: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    38: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    39: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    40: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    41: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    42: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    43: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    44: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    45: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    46: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    47: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    48: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 2,
                            'symm_cards': ['SYMM y, z, x\n', 'SYMM -y, x, z\n', 'SYMM y, -x, z\n',
                                           'SYMM -x, -y, z+0.5\n', 'SYMM -y, -z, x+0.5\n', 'SYMM y, x, -z\n',
                                           'SYMM z, x, y\n', 'SYMM x, z, -y\n', 'SYMM x, -y, -z+0.5\n',
                                           'SYMM -z, y, x\n', 'SYMM -z, -x, y+0.5\n', 'SYMM -x, y, -z\n',
                                           'SYMM -y, z, -x\n', 'SYMM z, y, -x\n', 'SYMM -y, -x, -z+0.5\n',
                                           'SYMM z+0.5, -x, -y\n', 'SYMM -z, x, -y\n', 'SYMM -z, -x, y\n']}

dictio_space_groups[212] = {'symbol': 'P 43 3 2', 'short_symbol': 'P4332', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [3 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [3 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point': '432', 'laue': 'm-3m',
                            'symm_cards': ['SYMM x+0.75, z+0.25, -y+0.75\n', 'SYMM -y+0.75, -x+0.75, -z+1.25\n',
                                           'SYMM -y+0.25, x+0.75, z+0.75\n', 'SYMM y-0.25, x+0.25, -z+0.75\n',
                                           'SYMM -z, x+0.5, -y+0.5\n', 'SYMM -y+0.75, -x+0.75, -z+0.25\n',
                                           'SYMM z, x, y\n', 'SYMM z+0.75, y+0.25, -x+0.75\n',
                                           'SYMM z+0.5, -x+0.5, -y\n', 'SYMM -x, y+0.5, -z+0.5\n',
                                           'SYMM -z+0.5, -x, y+0.5\n', 'SYMM x+0.5, -y+0.5, -z\n',
                                           'SYMM -y, z+0.5, -x+0.5\n', 'SYMM y, z, x\n',
                                           'SYMM -z+0.75, y+0.75, x+0.25\n', 'SYMM y+0.25, -x+0.25, z+0.25\n',
                                           'SYMM -y+0.5, -z, x+0.5\n', 'SYMM -x+0.5, -y, z+0.5\n']}

dictio_space_groups[213] = {'symbol': 'P 41 3 2', 'short_symbol': 'P4132', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [3 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [3 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [1 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [1 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [1 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [1 / 2.0, 1 / 2.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [0.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [1 / 2.0, 0.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [3 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [3 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [1 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [3 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [1 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [3 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0], [1 / 2.0, 1 / 2.0, 1 / 2.0]], 'polar': False, 'latt': 1,
                            'point': '432', 'laue': 'm-3m',
                            'symm_cards': ['SYMM x+0.25, z+0.75, -y+0.25\n', 'SYMM y, z, x\n',
                                           'SYMM z+0.25, y+0.75, -x+0.25\n', 'SYMM -z, x+0.5, -y+0.5\n',
                                           'SYMM z, x, y\n', 'SYMM z+0.5, -x+0.5, -y\n', 'SYMM -x, y+0.5, -z+0.5\n',
                                           'SYMM y+0.75, -x+0.75, z+0.75\n', 'SYMM -z+0.5, -x, y+0.5\n',
                                           'SYMM x+0.5, -y+0.5, -z\n', 'SYMM -y, z+0.5, -x+0.5\n',
                                           'SYMM -y+0.25, -x+0.25, -z+0.75\n', 'SYMM -z+0.25, y+0.25, x+0.75\n',
                                           'SYMM -y+0.5, -z, x+0.5\n', 'SYMM -y+0.75, x+0.25, z+0.25\n',
                                           'SYMM y+0.25, x-0.25, -z+0.25\n', 'SYMM -x+0.5, -y, z+0.5\n']}

dictio_space_groups[214] = {'symbol': 'I 41 3 2', 'short_symbol': 'I4132', 'symops': {
    1: {'tra': [0.0, 0.0, 0.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    2: {'tra': [1 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    3: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    4: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    5: {'tra': [1 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    6: {'tra': [1 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    7: {'tra': [1 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    8: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    9: {'tra': [0.0, 0.0, 0.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    10: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    11: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    12: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    13: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    14: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    15: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    16: {'tra': [0.0, 0.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    17: {'tra': [1 / 2.0, 0.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    18: {'tra': [0.0, 1 / 2.0, 0.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    19: {'tra': [1 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    20: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    21: {'tra': [1 / 4.0, 1 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    22: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    23: {'tra': [1 / 4.0, 3 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    24: {'tra': [1 / 4.0, 1 / 4.0, 1 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]},
    25: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]},
    26: {'tra': [3 / 4.0, 3 / 4.0, 0.625], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, 0.0]]},
    27: {'tra': [3 / 4.0, 0.625, 0.625], 'rot': [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]},
    28: {'tra': [3 / 4.0, 0.625, 0.625], 'rot': [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0]]},
    29: {'tra': [3 / 4.0, 0.625, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]},
    30: {'tra': [3 / 4.0, 0.625, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    31: {'tra': [3 / 4.0, 3 / 4.0, 0.625], 'rot': [[0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]},
    32: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    33: {'tra': [1 / 2.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]},
    34: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, 0.0]]},
    35: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[0.0, 0.0, 1.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    36: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]]},
    37: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]},
    38: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[0.0, 0.0, -1.0], [1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]},
    39: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, 0.0]]},
    40: {'tra': [1 / 2.0, 1 / 2.0, 1.0], 'rot': [[1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, -1.0]]},
    41: {'tra': [1.0, 1 / 2.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]]},
    42: {'tra': [1 / 2.0, 1.0, 1 / 2.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, 0.0, 1.0]]},
    43: {'tra': [3 / 4.0, 0.625, 0.625], 'rot': [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    44: {'tra': [3 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, -1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]},
    45: {'tra': [3 / 4.0, 3 / 4.0, 0.625], 'rot': [[0.0, 0.0, 1.0], [0.0, -1.0, 0.0], [1.0, 0.0, 0.0]]},
    46: {'tra': [3 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]]},
    47: {'tra': [3 / 4.0, 0.625, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]},
    48: {'tra': [3 / 4.0, 3 / 4.0, 3 / 4.0], 'rot': [[-1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, 0.0]]}},
                            'origins_list': [[0.0, 0.0, 0.0]], 'polar': False, 'latt': 2,
                            'point': '432', 'laue': 'm-3m',
                            'symm_cards': ['SYMM x+0.25, z+0.75, -y+0.25\n', 'SYMM y, z, x\n',
                                           'SYMM z+0.25, y+0.75, -x+0.25\n', 'SYMM -z, x+0.5, -y+0.5\n',
                                           'SYMM z, x, y\n', 'SYMM z+0.5, -x+0.5, -y\n', 'SYMM -x, y+0.5, -z+0.5\n',
                                           'SYMM y+0.75, -x+0.75, z+0.75\n', 'SYMM -z+0.5, -x, y+0.5\n',
                                           'SYMM x+0.5, -y+0.5, -z\n', 'SYMM -y, z+0.5, -x+0.5\n',
                                           'SYMM -y+0.25, -x+0.25, -z+0.75\n', 'SYMM -z+0.25, y+0.25, x+0.75\n',
                                           'SYMM -y+0.5, -z, x+0.5\n', 'SYMM -y+0.75, x+0.25, z+0.25\n',
                                           'SYMM y+0.25, x-0.25, -z+0.25\n', 'SYMM -x+0.5, -y, z+0.5\n']}

#############
# Functions #
#############

##########################################
# Pandas dataframe and plotting related  #
##########################################


def read_info_frag(infofrag):
    dfirst = pd.read_csv(infofrag,delim_whitespace=True)
    dfirst['Name'] = dfirst['Name'].astype(str) + '.phs'
    return dfirst


def color_plot_cmap(dfirst, x, y, zcolor):
    fig, ax = plt.subplots()
    cmap = mpl.cm.get_cmap('RdYlGn_r')
    plotx = dfirst.plot.scatter(x, y, c=zcolor, cmap=cmap, ax=ax)
    return plotx

def color_plot_discrete(dfirst, x, y, zcolor):
    fig, ax = plt.subplots()
    colours = ['b', 'g', 'y', 'm', 'c', 'r']
    col = [colours[i] for i,_ in enumerate(set(dfirst[zcolor]))]
    plotx = dfirst.plot.scatter(x, y, c=col, ax=ax)
    return plotx


def correct(dfirst):
    total = len(dfirst)
    corr = dfirst.loc[dfirst['wMPE'] < 80]
    print('\n\n Post-mortem INFO: ')
    print('There are ', len(corr), ' correct solutions out of ',total)
    print('Ratio is ', float(len(corr))/total)
    print("Max value of wMPE is ", dfirst['wMPE'].max())
    print("Min value of wMPE is ", dfirst['wMPE'].min(),'\n\n')


def plots_info_clust(path_info_clust, ali_confdict, folder_mode=False):
    # We will do different plots depending on whether we have final wMPE of solutions or not
    list_path = os.path.split(path_info_clust)
    path_clustering = list_path[0]
    keyname = list_path[1][:-17]
    dalixe = pd.read_csv(path_info_clust, delim_whitespace=True)
    total = len(dalixe)
    if not folder_mode:
        if ali_confdict['filter_single']:
            #                 no_single = dalixe.loc[dalixe['n_phs']>1]
            #                 total_no_single = len(no_single)
            print('\n Pending to implement')
        else:
            if ali_confdict['postmortem'] and 'ent_file' in ali_confdict:
                # Aside from plotting, it also finds out how many clusters have also a wMPE that is less than 80
                correct_clu = dalixe.loc[dalixe['phi_wmpe']<80]
                print('\n There are ', len(correct_clu), ' correct phase clusters out of ',total)
                print('Ratio is ',float(len(correct_clu))/total)
                print("Max value of phiwMPE is ",dalixe['phi_wmpe'].max())
                print("Min value of phiwMPE is ",dalixe['phi_wmpe'].min())
                cmap = mpl.cm.get_cmap('RdYlGn_r')
                plot1 = dalixe.plot.scatter('topzscore','topllg',s=dalixe['n_phs']*15,c=dalixe['phi_wmpe'],cmap=cmap)
                plt.savefig(os.path.join(path_clustering, keyname+'_info_allclust_LLG_vs_Zscore_by_wMPE.pdf'))
                # If fusedcoord also do it with the fused_cc
                if ali_confdict['fusedcoord']:
                    plot2 = dalixe.plot.scatter('fused_cc','topllg', s=dalixe['n_phs'] * 15, c=dalixe['phi_wmpe'],
                                                cmap=cmap)
                    plt.savefig(os.path.join(path_clustering,keyname+'_info_allclust_LLG_vs_FusedCC_by_wMPE.pdf'))

            else: # no postmortem
                plot2 = dalixe.plot.scatter('topzscore','topllg', s=dalixe['n_phs'] * 15)
                plt.savefig(os.path.join(path_clustering, keyname+'_info_allclust_LLG_vs_Zscore.pdf'))
                if ali_confdict['fusedcoord']:
                    plot2 = dalixe.plot.scatter('fused_cc','topllg',s=dalixe['n_phs']*15)
                    plt.savefig(os.path.join(path_clustering,keyname+'_info_allclust_LLG_vs_FusedCC.pdf'))
    # else:
        # HISTOGRAMA del numero de phs por cluster


def plots_info_frag(path_files, ali_confdict, folder_mode=False):
    """

    :param path_files:
    :param ali_confdict:
    :param folder_mode:
    :return:
    """
    # We will do different plots depending on whether we have final wMPE of solutions or not
    keyname = os.path.basename(path_files)
    path_info_frag = os.path.join(path_files, keyname+"_info_frag")
    dfirst = read_info_frag(path_info_frag)
    if not folder_mode:
        if 'LLGgimbLLG' in dfirst.columns:  # gimble performed and we should use latest LLG for plots and do the multiplot
            key_llg = 'LLGgimbLLG'
            # extra_plot_llgs = dfirst.plot(x="X", y=["A", "B", "C"], kind="bar")
            extra_plot_llgs = dfirst.plot(y=["LLGrbr", "LLGgimb", "LLGgimbLLG"], kind="bar")
            plt.savefig(os.path.join(path_files, keyname + '_LLGs_comparison.pdf'))
        else:
            key_llg = 'LLGrbr'
        if ali_confdict['postmortem']:
            correct(dfirst)
            plot1 = dfirst.plot.scatter('wMPE', key_llg)
            plt.savefig(os.path.join(path_files,keyname+'_single_sol_wMPE_LLG.pdf'))
            plot2 = color_plot_cmap(dfirst, 'InitCC', key_llg, 'wMPE')
            plt.savefig(os.path.join(path_files,keyname+'_single_sol_InitCC_LLG_color_by_wMPE.pdf'))
            plot3 = dfirst.plot.scatter('InitCC', key_llg)
            plt.savefig(os.path.join(path_files,keyname+'_single_sol_InitCC_LLG.pdf'))
            plot4 = dfirst.plot.scatter('Z-score', key_llg)
            plt.savefig(os.path.join(path_files,keyname+'_single_sol_Z-score_LLG.pdf'))
            plot5 = color_plot_cmap(dfirst, 'Z-score', key_llg, 'wMPE')
            plt.savefig(os.path.join(path_files,keyname+'_single_sol_InitCC_LLG_color_by_wMPE.pdf'))
        else:
            plot6 = dfirst.plot.scatter('InitCC', key_llg)
            plt.savefig(os.path.join(path_files, keyname + '_single_sol_InitCC_LLG.pdf'))

            plot7 = dfirst.plot.scatter('Z-score', key_llg)
            plt.savefig(os.path.join(path_files, keyname + '_single_sol_Z-score_LLG.pdf'))
    else:
        if ali_confdict[path_files]['compute_phs']:
            if ali_confdict['postmortem']:
                plot1 = dfirst.plot.scatter('wMPE', 'InitCC')
                plt.savefig(os.path.join(path_files, keyname + '_single_sol_wMPE_InitCC.pdf'))





#@timing
def add_cryst_card(cryst_card, path_pdb): #NOTE: Maybe should be moved to Bioinformatics3.py
    """ Add a cryst1 record to a pdb file

    :param cryst_card: cryst1 record
    :type cryst_card: str
    :param path_pdb: ath to the pdb file to modify. Note that it will be overwritten
    :type path_pdb: str
    :return: True for success, False otherwise
    :rtype: bool
    """
    try:
        file_pdb = open(path_pdb, 'r')
        content_pdb = file_pdb.read()
        file_pdb.close()
        new_file = open(path_pdb, 'w')  # Overwrite and put CRYST card
        new_file.write(cryst_card + "\n")
        new_file.write(content_pdb)
        new_file.close()
        return True
    except:
        print('\nSomething went wrong adding the CRYST1 record to the pdb at',path_pdb)
        return False


def check_cryst_cards_folder_mode(list_files_pdb, tolerance):
    list_cryst_cards = []
    for filepdbpath in list_files_pdb:
        file_sym = open(filepdbpath, 'r')
        cryst_card = extract_cryst_card_pdb(file_sym.read())
        del file_sym
        list_cryst_cards.append(cryst_card)
    # First naive check just if they are identical
    setcheck = set(list_cryst_cards)
    if len(setcheck) == 1:
        return True
    else:  # Second check with the tolerance
        list_checks = []
        reference_cryst = list_cryst_cards[0]
        list_val = reference_cryst.split()
        ref_unit_cell = [float(list_val[1]), float(list_val[2]), float(list_val[3])]
        ref_sg = list_val[7]
        for i in range(1, len(list_cryst_cards)):  # we skip first because it is the reference
            crysti = list_cryst_cards[i]
            list_val = crysti.split()
            unit_cell = [float(list_val[1]), float(list_val[2]), float(list_val[3])]
            sg = list_val[7]
            if (sg == ref_sg) and check_cell_range(unit_cell, ref_unit_cell, tolerance):
                # SG and cell checks passed
                list_checks.append(True)
            else:
                # SG and cell checks NOT passed
                list_checks.append(False)
        if len(set(list_checks)) == 1:
            print('\n *Info* All cells in CRYST1 records were within the accepted tolerance')
            return True
        else:
            print('\n *Info* The cells in CRYST1 records were NOT within the accepted tolerance')
            return False


def check_cell_range(test_cell, ref_unit_cell, tolerance):
    upper_lim_cell = [side + tolerance for side in ref_unit_cell]
    down_lim_cell = [side - tolerance for side in ref_unit_cell]
    if (down_lim_cell[0] <= test_cell[0] <= upper_lim_cell[0]) and \
            (down_lim_cell[1] <= test_cell[1] <= upper_lim_cell[1]) and \
            (down_lim_cell[2] <= test_cell[2] <= upper_lim_cell[2]):
        return True
    else:
        return False


def check_if_gimble(type_run,wd):
    if type_run=='BORGES':
        if os.path.exists(os.path.join(wd,'8_GIMBLE')):
           gimble=True
        else:
           gimble=False
    else:
        gimble=False
    return gimble


def check_dir_or_make_it(path_dir,remove=True):
    try:
        os.mkdir(path_dir)
        return False
    except OSError:
        exctype, value = sys.exc_info()[:2]
        print(value)
        if str(value).startswith("[Errno 17] File exists:") and remove:  # Then the folder exists
            print("\n ",path_dir," folder existed. Files will be removed to recreate the folder")
            shutil.rmtree(path_dir, ignore_errors=True)
            os.mkdir(path_dir)
            return False
        else:
            print("\n ", path_dir, " folder was already present, we will not remove it or create it")
            return True


def check_path_chescat(path_chescat):
    # Testing the fortran executable for the phase combination
    print('\nThe given path for CHESCAT is '+path_chescat)
    if not os.path.exists(path_chescat):
        print('\nThe path given to the CHESCAT executable does not exist')
        return False
    else:
        # Check anyway that the program works
        try:
            p = subprocess.Popen(path_chescat, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            complete_output, errors = p.communicate()
            if len(complete_output) > 0:
                print('\nCHESCAT test was run succesfully')
                return True
            else:
                print('\nSorry, there is some error with the path given as chescat_executable')
                return False
        except:
            print('\nSorry, there is some error with the path given as chescat_executable')
            return False



def call_chescat_for_clustering_global(args):

    name_phstat, wd, path_phstat, resolution, seed, tolerance, n_cycles, orisub, weight, oricheck, mapcc, wait = args

    # Check if the correct files are there
    ls_filename = name_phstat + ".ls"
    pda_filename = name_phstat + ".pda"
    if not (((os.path.exists(os.path.join(wd, ls_filename))) and (os.path.exists(os.path.join(wd, pda_filename))))):
        sys.exit("\nAn error has occurred. Please make sure that you have provide a .ls and a .pda file")

    # If everything is OK, we continue and prepare the command line
    command_line = []
    command_line.append(path_phstat)
    full_name_phstat = os.path.join(wd,name_phstat)
    #name_phstat = os.path.split(name_phstat)[1]
    command_line.append(name_phstat)
    arguments = ["-r" + str(resolution), "-s" + str(seed), "-t" + str(tolerance), "-c" + str(n_cycles)]
    if weight=='e':
        arguments.append('-e')
    if orisub=='sxosfft':
        arguments.append('-o')
    if not oricheck:
        arguments.append('-q')
    if mapcc:
        arguments.append('-k')
    for i in range(len(arguments)):
        command_line.append(arguments[i])

    # Try to run CHESCAT with the given command line
    out_file = open(full_name_phstat + '.out', 'w')  # we need to write the out file
    try:
        print("\nCommand line used in CHESCAT --> ", ' '.join(command_line))
        if wait:
            p = subprocess.Popen(command_line, stdin=subprocess.PIPE, stdout=out_file, stderr=subprocess.PIPE,
                                 cwd=wd)
            complete_output, errors = p.communicate()
            return complete_output,errors
        else:
            p = subprocess.Popen(command_line, stdin=subprocess.PIPE, stdout=out_file, stderr=subprocess.PIPE,
                                 cwd=wd)
            return p
    except Exception:
        exctype, value = sys.exc_info()[:2]
        print("\n An error has occurred:\n" + str(exctype) + "\n" + str(value))
        return None,None


def validate_CPUs(n_cores_read):
    n_cores = (psutil.cpu_count(logical=True) - 1)  # default is the number of logical cores -1
    if n_cores_read == -1:
        # Adding a maximum value to limit the number of cores, as speedup over this value is not significant
        if n_cores >= 10:
            return 10
        else:
            return n_cores
    elif n_cores_read > n_cores:
        print('\n Warning: This run is not going to be executed as set ',
              'because you inputted a larger number of cores ',n_cores_read,
              ' than logical cores in the machine, ',n_cores)
        return n_cores
    else:
        print('\n Warning: This run is going to be executed on ',n_cores_read,' CPUs')
        return n_cores_read


# Check correctness of options or change accordingly
def validate_confdict_alixe(ali_confdict):
    folder_mode = False
    ali_confdict['output_folder'] = os.path.abspath(ali_confdict['output_folder'])
    print('\n *Info* Output folder will be ',ali_confdict['output_folder'])
    if ali_confdict['alixe_mode'] not in ('fish','cc_analysis','monomer','multimer'):
        print('Sorry, you need to provide a valid mode for autoalixe')
        print("Available options are monomer, multimer, fish, cc_analysis")
        sys.exit(1)
    if not os.path.exists(ali_confdict['references']) and ali_confdict['references'] != 'none':
        print('Sorry, you need to provide a valid folder or reference for ALIXE')
        sys.exit(1)
    if not check_path_chescat(ali_confdict['path_chescat']):
        sys.exit(1)
    if ali_confdict['fom_sorting'] not in ('CC','LLG','ZSCORE','COMBINED'):
        print('\nSorry, only CC, LLG, ZSCORE or COMBINED can be used for sorting')
    # Check input_info folders
    for i in range(ali_confdict['n_pools']):
        keyinputinfo = 'input_info_'+str(i+1)
        if not os.path.exists(ali_confdict[keyinputinfo]):
            print('Sorry, you need to provide a valid input_info for ALIXE')
            sys.exit(1)
        else:
            if os.path.isdir(ali_confdict[keyinputinfo]):
                folder_mode = True
    ali_confdict['number_cores_parallel'] = validate_CPUs(ali_confdict['number_cores_parallel'])
    return folder_mode, ali_confdict


def startALIXEforARCIMBOLDO_TwoSteps(ali_confdict, clust_fold_root):
    # Check if alixe has been already performed and act accordingly
    clust_fold_second = os.path.join(clust_fold_root,'R2')
    print('\n Starting ALIXE second round on folder ' + clust_fold_second)
    if check_dir_or_make_it(clust_fold_second, remove=False):
        # check whether it existed because it was unfinished or because it was already done:
        # R2_dictio_clustering_alixe.pkl
        path_pickle = os.path.join(clust_fold_second,'R2'+'_dictio_clustering_alixe.pkl')
        if os.path.exists(path_pickle):
            dictio_results = get_dictio_results_from_pickle_clustering_alixe(path_pickle)
            print("\n ALIXE first round has run succesfully already on this folder. Returning! ")
            # Return tuple for expansion (filtering single)
            print('\n You are in two steps mode, returning the required tuple for expansion')
            rotcluster_id = list(dictio_results.keys())[0]  # there is only one key, as one step is performed on a rotclu
            filtered_list = [os.path.join(clust_fold_second, key) for key in dictio_results[rotcluster_id].keys()
                             if dictio_results[rotcluster_id][key]['n_phs'] > 1]
            ins_file_path = os.path.join(clust_fold_second,'symmetry.ins')
            tuple_phi = (ins_file_path, filtered_list)
            return tuple_phi
        else:
            print('\n ALIXE was not completed in this folder ', clust_fold_second)
            print('\n Starting a new ALIXE run')
            check_dir_or_make_it(clust_fold_second, remove=True)
            ali_confdict[clust_fold_second] = {}
    else:
        print('\n Clustering folder did not exist and has been created now')
        ali_confdict[clust_fold_second] = {}

    ali_confdict[clust_fold_second]['compute_phs'] = False

    # First we need to read all the clusters from the other folders and link the files
    dict_clust_by_rotclu={}
    for fichiname in os.listdir(clust_fold_root):
        if fichiname != 'R2':
            path_rotclu = os.path.join(clust_fold_root, fichiname)
            path_pickle = os.path.join(path_rotclu, fichiname + '_dictio_clustering_alixe.pkl')
            if os.path.exists(path_pickle):
                dictio_results = get_dictio_results_from_pickle_clustering_alixe(path_pickle)
                dict_clust_by_rotclu = merge_dicts(dict_clust_by_rotclu,dictio_results)
                for phasecluster in dictio_results[fichiname].keys():
                    path_file_to_link = os.path.join(path_rotclu,phasecluster)
                    link_file(clust_fold_second, path_file_to_link, os.path.basename(path_file_to_link))

    # Take a file for the symmetry (last one for example)
    pathi_sym = path_file_to_link[:-4]+'.pda'
    ali_confdict['path_sym'] = pathi_sym
    if 'ins_file' not in ali_confdict: # This will happen if first rounds were already performed in a previous run
        # Then take the ins file from the latest processed rotation cluster
        ali_confdict['ins_file'] = os.path.join(path_rotclu,'symmetry.ins')

    # Now we can run the second step
    # Make sure input is sorted in a sensible way
    # list_chosen = []
    # list_phi = list_files_by_extension(clust_fold_second, 'phi', fullpath=True)
    # list_phs = list_files_by_extension(clust_fold_second, 'phs', fullpath=True)
    # list_chosen.extend(list_phi)
    # list_chosen.extend(list_phs)
    # del list_phi
    # del list_phs
    dict_clust_second = {}
    # I will need to use the same function than in ALIXE, al.get_clusters_from_dict_clust_by_rotclu(dict_clust_by_rotclu)
    list_chosen = get_clusters_from_dict_clust_by_rotclu(dict_clust_by_rotclu)
    # NOTE CM: list_chosen does not have full paths, should it?
    dict_clust_second = ALIXE_clustering_on_a_set(ali_confdict=ali_confdict, dict_clust_by_rotclu=dict_clust_second,
                                                  rotclu='R2', list_phs_rotclu=list_chosen,
                                                  sub_clust_path=clust_fold_second, tolerance ='second')

    prepare_output_tables_clustering_alixe_second_round(dict_clust_by_rotclu=dict_clust_second,
                                                        ali_confdict=ali_confdict, sub_clust_path=clust_fold_second,
                                                        keypool='R2', folder_mode=False, filter_single=False)

    # write the output in pkl format to retrieve it later on
    prepare_pickle_clustering_alixe(dict_clust_second, clust_fold_second, 'R2')

    # If plotting option is active, prepare plots describing the clustering
    # Need to check this is not yet prepared
    # if ali_confdict['plots']:
    #     path_info_clust = os.path.join(path_rotclu, 'R2' + "_info_clust_table")
    #     plots_info_clust(path_info_clust, ali_confdict, folder_mode=False)

    # Now prepare to return
    # We will filter the clusters that have less than one file
    filtered_list = [os.path.join(clust_fold_second, key) for key in dict_clust_second['R2'].keys()
                     if dict_clust_second['R2'][key]['n_phs'] > 1]
    tuple_phi = (ali_confdict['ins_file'], filtered_list)
    return tuple_phi, ali_confdict


def ALIXE_clustering_on_a_set(ali_confdict, dict_clust_by_rotclu, rotclu, list_phs_rotclu, sub_clust_path,
                              tolerance='first'):
    """

    :param ali_confdict:
    :param dict_clust_by_rotclu:
    :param rotclu:
    :param list_phs_rotclu:
    :param sub_clust_path:
    :param tolerance:
    :return:
    """
    key_tol = 'tolerance_' +tolerance+ '_round'  # I need to check which tolerance to use
    dict_rotclu = {rotclu: {}}  # working dictionary to save intermediate results
    starting_input_size = len(list_phs_rotclu)
    if starting_input_size <= 1:
        print('\n This cluster has only one solution, no clustering will be performed')
        return
    elif starting_input_size <= ali_confdict['minchunk']:
        # NOTE CM: this is a hard limit, apart from this we can have something dynamic
        list_non_processed_files = list_phs_rotclu
    else:  # only then we proceed to the parallel section
        if 'n_references' not in ali_confdict.keys():
            ali_confdict["n_references"] = starting_input_size  # then we use all the solutions
        list_non_processed_files, \
        dict_global_results, \
        single_clust_count = parallel_chescat_clustering(path_chescat=ali_confdict["path_chescat"],
                                                            list_of_input_files=list_phs_rotclu,
                                                            n_references=ali_confdict["n_references"],
                                                            n_cores=ali_confdict["number_cores_parallel"],
                                                            min_size_list=ali_confdict["minchunk"],
                                                            max_non_clust_events=ali_confdict["max_non_clust_events"],
                                                            clust_fold=sub_clust_path,
                                                            resolution=ali_confdict["resolution_comparison"],
                                                            tolerance=ali_confdict[key_tol],
                                                            cycles=ali_confdict["cycles"],
                                                            orisub=ali_confdict["origin_search"],
                                                            weight=ali_confdict["weight"],
                                                            oricheck=ali_confdict["oricheck"],
                                                            cc_calc=ali_confdict["map_cc"],
                                                            path_sym=ali_confdict['path_sym'])

        if not dict_global_results.keys():
            print("There was not any clustering performed in the parallel section, continuing with the sequential")
        else:
            print("There was clustering performed in the parallel section, but now we will continue sequentially")
            # Save the results of the parallel part sorted by rotclu
            dict_rotclu[rotclu]['parallel'] = dict_global_results

    # Now we will call the sequential part with the resolution for comparison
    if len(list_non_processed_files) > 0:
        prepare_chescat_input_from_data(list_phase_sets=list_non_processed_files, directory=sub_clust_path,
                                        name_chescat='sequential', path_sym=ali_confdict['path_sym'])

        dict_global_results = sequential_clustering_chescat(name_chescat='sequential',
                                                               wd=sub_clust_path,
                                                               path_chescat=ali_confdict["path_chescat"],
                                                               tolerance=ali_confdict[key_tol],
                                                               resolution=ali_confdict["resolution_comparison"],
                                                               seed=ali_confdict["seed"],
                                                               n_cycles=ali_confdict["cycles"],
                                                               orisub=ali_confdict["origin_search"],
                                                               weight=ali_confdict["weight"],
                                                               idrotclu=rotclu,
                                                               oricheck=ali_confdict["oricheck"],
                                                               mapcc=ali_confdict["map_cc"])

        # Save the results of the sequential part sorted by rotclu
        dict_rotclu[rotclu]['sequential'] = dict_global_results

    # Finally, we will recompute the clusters we need at full resolution
    # And to save the results in a single dictionary that we can use for:
    # # # Writing the output in a human-readable table
    # # # Writing a pickle file that we can read for further clustering
    if 'parallel' in dict_rotclu[rotclu]:
        list_to_recalculate_parallel, \
        list_single_parallel = process_dictioset_alixe(dict_rotclu[rotclu]['parallel'])

        if len(list_to_recalculate_parallel) > 0:
            dict_results_par = produce_merged_clusters(list_to_recalculate_parallel, sub_clust_path,
                                                          ali_confdict)
            dict_clust_by_rotclu = add_clusters_to_dictionary(rotclu, dict_clust_by_rotclu, dict_results_par)
            if len(list_single_parallel) > 0:
                dict_clust_by_rotclu = add_clusters_to_dictionary(rotclu, dict_clust_by_rotclu,
                                                                     list_single_parallel)
        else:  # In this case we need to save the single clusters
            dict_clust_by_rotclu = add_clusters_to_dictionary(rotclu, dict_clust_by_rotclu, list_single_parallel)
    if 'sequential' in dict_rotclu[rotclu]:
        list_to_recalculate_sequential, \
        list_single_sequential = process_dictioset_alixe(dict_rotclu[rotclu]['sequential'])
        if len(list_to_recalculate_sequential) > 0:
            dict_results_seq = produce_merged_clusters(list_to_recalculate_sequential, sub_clust_path,
                                                          ali_confdict)
            dict_clust_by_rotclu = add_clusters_to_dictionary(rotclu, dict_clust_by_rotclu, dict_results_seq)
            if len(list_single_sequential) > 0:
                dict_clust_by_rotclu = add_clusters_to_dictionary(rotclu, dict_clust_by_rotclu,
                                                                     list_single_sequential)
        else:
            dict_clust_by_rotclu = add_clusters_to_dictionary(rotclu, dict_clust_by_rotclu, list_single_sequential)
    return dict_clust_by_rotclu



def startALIXEforARCIMBOLDO_OneStep(ali_confdict, input_mode, wd, path_rotclu, type_run):
    """

    :param ali_confdict:
    :param input_mode:
    :param wd:
    :param path_rotclu:
    :param type_run:
    :return:
    """

    # Check if alixe has been already performed on that folder and act accordingly depending on mode
    print('\n Starting ALIXE on folder ' + path_rotclu)
    rotcluster_id = os.path.basename(path_rotclu)
    if check_dir_or_make_it(path_rotclu, remove=False):
        # check whether it existed because it was unfinished or because it was already done:
        # 0_dictio_clustering_alixe.pkl
        path_pickle = os.path.join(path_rotclu,rotcluster_id+'_dictio_clustering_alixe.pkl')
        if os.path.exists(path_pickle):
            dictio_results = get_dictio_results_from_pickle_clustering_alixe(path_pickle)
            print("\n ALIXE first round has run succesfully already on this folder. Returning! ")
            # As is one step, we filter the single ones and leave the ones for expansion
            print('\n You are in one step mode, returning the required tuple for expansion')
            rotcluster_id = list(dictio_results.keys())[0]  # there is only one key, as one step is performed on a rotclu
            filtered_list = [os.path.join(path_rotclu, key) for key in dictio_results[rotcluster_id].keys()
                             if dictio_results[rotcluster_id][key]['n_phs'] > 1]
            ins_file_path = os.path.join(path_rotclu,'symmetry.ins')
            tuple_phi = (ins_file_path, filtered_list)
            return tuple_phi, ali_confdict
        else:
            print('\n ALIXE was not completed in this folder ', path_rotclu)
            print('\n Starting a new ALIXE run')
            check_dir_or_make_it(path_rotclu, remove=True)
            ali_confdict[path_rotclu] = {}
    else:
        print('\n Clustering folder did not exist and has been created now')
        ali_confdict[path_rotclu] = {}

    ali_confdict[path_rotclu]['compute_phs'] = False  # It is from an ARCIMBOLDO run so we do have already them

    # Obtain the files and put them in the folder
    if type_run == 'SHREDDER' or type_run == 'BORGES':
        list_chosen = get_files_from_9_EXP_BORGES(wd=wd, clust_fold=path_rotclu, cluster_id=rotcluster_id,
                                                  mode=input_mode, hard_limit_phs=ali_confdict['limit_sol_per_rotclu'])
        ali_confdict[path_rotclu]['type_run'] = 'BORGES'
        ali_confdict[path_rotclu]['wd_run'] = wd

    # # Read the FOMs of the phs files in the phaser and shelxe steps
    phs_files = list_files_by_extension(path_rotclu, 'phs')
    dictio_fragments = {}

    list_pdbs = list_files_by_extension(path_rotclu, 'pda')
    dictio_fragments = fill_dictio_fragments(dictio_fragments, rotcluster_id, path_rotclu, list_pdbs, ali_confdict)

    # Take a file for the symmetry (first one for example)
    pathi_sym = list_pdbs[0]
    ali_confdict['path_sym'] = pathi_sym
    ali_confdict = generate_sym_data(ali_confdict['path_sym'], ali_confdict, path_rotclu)

    # Now is time to call the actual clustering
    dict_clust_by_rotclu = {}
    dict_clust_by_rotclu[rotcluster_id] = {}
    # Make sure input is sorted sensibly
    list_chosen = sort_list_phs_rotclu_by_FOM(list_phs_full=list_chosen,
                                   fom_sorting=ali_confdict['fom_sorting'],
                                   dictio_fragments=dictio_fragments,
                                   keypool=rotcluster_id)
    dict_clust_by_rotclu = ALIXE_clustering_on_a_set(ali_confdict=ali_confdict,
                                                     dict_clust_by_rotclu=dict_clust_by_rotclu, rotclu=rotcluster_id,
                                                     list_phs_rotclu=list_chosen,sub_clust_path=path_rotclu,
                                                     tolerance='first')

    # write the output in table format
    prepare_output_tables_clustering_alixe(dict_clust_by_rotclu, ali_confdict, path_rotclu, rotcluster_id,
                                              dictio_fragments, False)
    # write the output in pkl format to retrieve it later on
    prepare_pickle_clustering_alixe(dict_clust_by_rotclu, path_rotclu, rotcluster_id)

    # If plotting option is active, prepare plots describing the clustering
    if ali_confdict['plots']:
        path_info_clust = os.path.join(path_rotclu, rotcluster_id + "_info_clust_table")
        plots_info_clust(path_info_clust, ali_confdict, folder_mode=False)

    # Now prepare to return
    # As this is a one_step, we will filter the clusters that have less than one file
    filtered_list = [os.path.join(path_rotclu,key) for key in dict_clust_by_rotclu[rotcluster_id].keys()
                      if dict_clust_by_rotclu[rotcluster_id][key]['n_phs']>1]
    tuple_phi = (ali_confdict['ins_file'],filtered_list)
    return tuple_phi, ali_confdict


def split_alixe_clusters(dictio_result):
    list_dictio_results = []
    for keyp in dictio_result.keys():
        if dictio_result[keyp]['ref_no_cluster'] == True:
            new_dictio_result = {}
            new_dictio_result[keyp] = copy.deepcopy(dictio_result[keyp])
            dictio_result = removeKeyDict(dictio_result, keyp)
            list_dictio_results.append(new_dictio_result)
    # Whatever left now, it should be the cluster
    if dictio_result:
        list_dictio_results.append(dictio_result)
    return list_dictio_results


def sequential_clustering_chescat(name_chescat, wd, path_chescat, tolerance=75, resolution=2.0, seed=0, n_cycles=3,
                                  orisub='sxos', weight='f', idrotclu='0', oricheck=True, mapcc=False):
    """ This function calls the fortran CHESCAT that Isabel modified
     for clustering, and sequentially process the complete ls file.

    Requires both the .ls file and a .pdb file called like name_phstat.

    orisub can be 'sxos' or 'sxosfft' (apply or not flag -o to phstat. -o means fft
    weight can be 'f' or 'e'

    IMPORTANT: the phi files will be named as name_phstat.phi (not the old name_phstat_0.phi)

    Returns the clusters obtained under the given tolerance in the form of a dictionary

    """

    # Start variables
    ls_not_empty = True
    count = 0
    items_to_remove = []

    path_ls = os.path.join(wd, name_chescat + ".ls")
    ls = open(path_ls, "r")
    lineas_fichero_ls = ls.readlines()
    numero_phs = len(lineas_fichero_ls)
    del ls
    print("\nThere are " + str(numero_phs) + "  phase set files in the ls file ", path_ls)
    content_lines = lineas_fichero_ls

    # NOTE CM: For exploration: Prepare a file to analyse how the clusters are being formed
    # path_formation = os.path.join(wd, "clustering_sequence_"+str(idrotclu))
    # file_form = open(path_formation, "w")
    # counter_single=0

    dict_global_results = {}

    while ls_not_empty:
        if (len(content_lines) - len(items_to_remove)) > 0:
            # Read the ls to see what did you have before clustering
            ls = open(path_ls, "r")
            content_lines = ls.readlines()
            del ls
            print('\n There are ', str(len(content_lines)), ' files remaining to cluster')
            if len(content_lines) == 1:
                the_file = os.path.basename(content_lines[0])
                faketuli = generate_fake_list_tuple_single_clust(the_file, 1)
                dict_global_results[the_file] = faketuli
                return dict_global_results
            print('\n Attempting sequential clustering with this set ')
            argumentsclust = (name_chescat, wd, path_chescat, resolution, seed, tolerance, n_cycles, orisub, weight,
                              oricheck, mapcc, True)
            call_chescat_for_clustering_global(argumentsclust)

            # Retrieve the results
            list_dictio_results = process_chescat_output_multiseed(path_output=path_ls[:-3]+'.out', cycles=n_cycles,
                                                                   size_ls=len(content_lines), seed=seed)

            dict_global_results, items_to_remove, clubool = process_list_dictio_results_to_global(list_dictio_results,
                                                                                                  dict_global_results,
                                                                                                  items_to_remove,
                                                                                                   name_chescat,
                                                                                                   wd,False)

            # if len(items_to_remove) != len(content_lines):
            #     print('check ',path_ls[:-3]+'.out')
            #     print(' items_to_remove', items_to_remove)
            #     print(' len(items_to_remove)', len(items_to_remove))
            #     print('len(content_lines)', len(content_lines))
            #     quit()

            # Overwrite the ls so that you write now just the things that didn't cluster
            ls2 = open(path_ls, 'w')
            del ls2
            for phs in content_lines:
                phs = phs.strip()
                if phs not in items_to_remove:
                    ls3 = open(path_ls, 'a')
                    ls3.write(phs + "\n")
                    del ls3
                count = count + 1
        else:
            ls_not_empty = False

    # # Do some cleaning now
    # try:
    #     os.remove(path_ls)
    #     os.remove(path_ls[:-3] + ".out")
    #     os.remove(path_ls[:-3] + ".pda")
    #     os.remove(path_ls[:-3] + ".phi")
    # except:
    #     pass
    return dict_global_results


def load_pickle(pickle_file):
    try:
        with open(pickle_file, 'rb') as f:
            pickle_data = pickle.load(f)
    except UnicodeDecodeError as e:
        with open(pickle_file, 'rb') as f:
            pickle_data = pickle.load(f, encoding='latin1')
    except Exception as e:
        print('Unable to load data ', pickle_file, ':', e)
        raise
    return pickle_data


def prepare_pickle_clustering_alixe(dictio_results_clustering, path_clustering, keypool):
        # Write a pkl file to avoid recomputation if it is not required
        save_dictio = open(os.path.join(path_clustering, keypool+'_dictio_clustering_alixe.pkl'), 'wb')
        pickle.dump(dictio_results_clustering, save_dictio, protocol=2)
        save_dictio.close()


def get_clusters_from_dict_clust_by_rotclu(dict_clust_by_rotclu, sort=True):
    list_tuple_clusters = []
    for rotclu in dict_clust_by_rotclu.keys():
        for keyclu in dict_clust_by_rotclu[rotclu].keys():
            list_tuple_clusters.append((keyclu,
                                        dict_clust_by_rotclu[rotclu][keyclu]["n_phs"],
                                        dict_clust_by_rotclu[rotclu][keyclu]["dict_FOMs"]['llg'],
                                        dict_clust_by_rotclu[rotclu][keyclu]["dict_FOMs"]['zscore']))
    if sort:
        list_tuple_clusters.sort(key=operator.itemgetter(1,2,3), reverse=True)
        list_clusters = [ele[0] for ele in list_tuple_clusters]
    else:
        list_clusters = [ele[0] for ele in list_tuple_clusters]
    return list_clusters


def get_dictio_results_from_pickle_clustering_alixe(path_pickle):
    #back_dictio = open(path_pickle, 'rb')
    dictio_result = load_pickle(path_pickle)
    #back_dictio.close()
    return dictio_result


def get_best_rotclu_order_to_start_exp(dict_clust_by_rotclu):
    list_tuple_sort = []
    for clu in dict_clust_by_rotclu.keys():
        print('\n ****** Rotation cluster ',clu)
        for phaseclu in dict_clust_by_rotclu[clu].keys():
            if dict_clust_by_rotclu[clu][phaseclu]['n_phs'] > 1:
                # Possible keys in dict_FOMs are 'efom_fused', 'pseudocc_fused', 'CC_fused',
                # 'final_MPEs_fused', 'final_MPEs_phi', 'efom_phi', 'pseudocc_phi',
                # 'CC_phi', 'llg', 'zscore'
                # LLG and ZSCORE only at the moment, but with new shelxe cc from phi would be an option
                list_tuple_sort.append((clu, dict_clust_by_rotclu[clu][phaseclu]['dict_FOMs']['llg'],
                                       dict_clust_by_rotclu[clu][phaseclu]['dict_FOMs']['zscore']))
                                       #dict_clust_by_rotclu[clu][phaseclu]['dict_FOMs']['CC_phi'],
                                       #dict_clust_by_rotclu[clu][phaseclu]['dict_FOMs']['CC_fused']))
    list_tuple_sort.sort(key=operator.itemgetter(1, 2), reverse=True)
    list_rotclu_exp = [ ele[0] for ele in list_tuple_sort ]
    return list_rotclu_exp


def perform_SHELXE_expansions_from_dictio_cluster(dict_clust_by_rotclu, ali_confdict, sub_clust_path, sort=True):
    print('\nStarting the expansions of the ALIXE phase clusters')
    expansions_folder_base = os.path.join(sub_clust_path, 'EXPANSIONS')
    check_dir_or_make_it(expansions_folder_base, remove=True)
    if sort:
        sorted_list_rotclu = get_best_rotclu_order_to_start_exp(dict_clust_by_rotclu)
    else:
        sorted_list_rotclu = dict_clust_by_rotclu.keys()
    for clu in sorted_list_rotclu:
        print('\n ****** Rotation cluster ',clu)
        expansions_folder = os.path.join(expansions_folder_base,clu)
        print('\n Processing expansions_folder',expansions_folder)
        check_dir_or_make_it(expansions_folder, remove=True)
        for phaseclu in dict_clust_by_rotclu[clu].keys():
            # print('\n phaseclu', phaseclu)
            if dict_clust_by_rotclu[clu][phaseclu]['n_phs'] > 1:
                print("\nThis cluster ", phaseclu, "contains more then one file, we will expand it")
                os.link(os.path.join(sub_clust_path, phaseclu), os.path.join(expansions_folder, phaseclu))
        # We need to do the linking first
        get_links_for_all(expansions_folder, ali_confdict['hkl_file'][:-4], 'phi', 'hkl')
        get_links_for_all(expansions_folder, ali_confdict['ins_file'][:-4], 'phi', 'ins')
        if 'ent_file' in ali_confdict.keys():
            get_links_for_all(expansions_folder, ali_confdict['ent_file'][:-4], 'phi', 'ent')
        (bool_check,fichi,cc) = phase_all_in_folder_with_SHELXE(linea_arg=ali_confdict['shelxe_line_expansion'],
                                                                dirname=expansions_folder,
                                                                shelxe_path=ali_confdict['shelxe_path'],
                                                                n_cores=ali_confdict['number_cores_parallel'],
                                                                check_if_solved=True, subset=[])
        if bool_check:  # We solved!
            break

#def prepare_references_ALIXE():
        # if option.startswith("-ref"):
        #     reference_to_fish = option[5:]
        #     if not os.path.exists(reference_to_fish):
        #         print("Sorry, you need to provide a valid path for the reference or references")
        #         sys.exit(1)
        #     else:
        #         if os.path.isfile(reference_to_fish):
        #             print("\nFile ", reference_to_fish, "is going to be used for fishing")
        #             list_references_fish=[reference_to_fish]
        #             if reference_to_fish.endswith('.phs'):
        #                 phs_ref=True
        #             else:
        #                 phs_ref=False
        #         elif os.path.isdir(reference_to_fish):
        #             print('\n Checking the files to use as references ')
        #             # NOTE: check whether we have the phase files or just coordinates
        #             list_references_fish=al.list_files_by_extension(reference_to_fish, 'phs')
        #             phs_ref=True
        #             if list_references_fish==None:
        #                 list_references_fish=al.list_files_by_extension(reference_to_fish, 'pdb')
        #                 if list_references_fish==None:
        #                     list_references_fish=al.list_files_by_extension(reference_to_fish, 'pda')
        #                     if list_references_fish==None:
        #                         print("Sorry, you need to provide a folder with either phs, pda or pdb references")
        #                         sys.exit(1)
        #                 phs_ref=False


def process_dictioset_alixe(dictio_set):
    """

    :param dictio_set:
    :return:
    """
    # NOTE CM: introducing sorting for reproducibility
    list_to_recalculate = []
    list_single = []
    list_keys = list(dictio_set.keys())
    list_keys.sort()
    for keyclu in list_keys:
        listsets = dictio_set[keyclu]
        settis = [ele[1] for ele in listsets]
        united = set.union(*settis)
        united_list = list(united)
        united_list.sort()
        if len(united) != 0:
            list_to_recalculate.append((keyclu, united_list))
        else:
            list_single.append(keyclu)
    list_single.sort()
    return list_to_recalculate, list_single


def produce_merged_clusters(list_to_recalculate, clust_fold, ali_confdict):
    """

    :param list_to_recalculate:
    :param clust_fold:
    :param ali_confdict:
    :return:
    """
    print('\n\n Now we will perform the reclustering step\n')
    dict_global_results = {}
    for ref, files in list_to_recalculate:
        name_ref = os.path.basename(ref)[:-4]
        # if filekeep[-8:] != '_ref_ref':
        #     name_ref_phs = os.path.basename(ref)[:-8] + '.phs'
        # else:
        #     name_ref_phs = os.path.basename(ref)[:-8] + '.phi'
        path_ls = os.path.join(clust_fold, name_ref + '_ref.ls')
        lsrotfile = open(path_ls, 'w')
        lsrotfile.write(ref + '\n')
        for xi in range(len(files)):
            if files[xi] != ref:
                lsrotfile.write(files[xi] + '\n')
        lsrotfile.close()
        if not os.path.exists(os.path.join(clust_fold, name_ref + "_ref.pda")):
            shutil.copy(ali_confdict['path_sym'], os.path.join(clust_fold, name_ref + "_ref.pda"))
        complete_output, errors = call_chescat_for_clustering_global((name_ref + "_ref",
                                                                      clust_fold,
                                                                      ali_confdict['path_chescat'],
                                                                      ali_confdict['resolution_merging'],
                                                                      0,
                                                                      ali_confdict["tolerance_merging"],
                                                                      ali_confdict["cycles"],
                                                                      ali_confdict["origin_search"],
                                                                      ali_confdict["weight"],
                                                                      ali_confdict["oricheck"],
                                                                      ali_confdict["map_cc"],
                                                                      True))

        list_dictio_results = process_chescat_output_multiseed(path_output=os.path.join(clust_fold, name_ref + "_ref.out"),
                                                               cycles=ali_confdict["cycles"], size_ls=len(files),
                                                               seed=0)


        list_remove = []
        dict_global_results, list_remove, clubool = process_list_dictio_results_to_global(list_dictio_results,
                                                                                             dict_global_results,
                                                                                             list_remove,
                                                                                             name_ref + "_ref",
                                                                                             clust_fold, True)

        # NOTE CM: here list_remove in principle should have the same than input, so if it does not we know sth
        # and is that something we expected to cluster, even if using a super high tolerance, 90, was not included
        # if len(list_remove) != len(files):
        #     print('os.path.join(clust_fold, name_ref + "_ref.out")',os.path.join(clust_fold, name_ref + "_ref.out"))
        #     print('list_remove', list_remove)
        #     print('files', files)
        #     print('len(list_remove)', len(list_remove))
        #     print('len(files)', len(files))
        #     quit()

    return dict_global_results


def add_clusters_to_dictionary(keyro, dict_clust_by_rotclu, data_cluster):
    # First we check whether data_cluster is a dictionary or a list
    if isinstance(data_cluster, list):
        # list of single clusters
        for _, ele in enumerate(data_cluster):
            if keyro in dict_clust_by_rotclu.keys():
                dict_clust_by_rotclu[keyro][ele] = {'n_phs': 1}
            else:
                dict_clust_by_rotclu[keyro] = {}
                dict_clust_by_rotclu[keyro][ele] = {'n_phs': 1}
    elif isinstance(data_cluster, dict):
        for key in data_cluster.keys():
            dictio_result = data_cluster[key][0][2]
            if keyro in dict_clust_by_rotclu.keys():
                dict_clust_by_rotclu[keyro][key] = {'n_phs': len(dictio_result.keys()),
                                                    'dictio_result': dictio_result}
            else:
                dict_clust_by_rotclu[keyro] = {}
                dict_clust_by_rotclu[keyro][key] = {'n_phs': len(dictio_result.keys()),
                                                    'dictio_result': dictio_result}

    return dict_clust_by_rotclu


def prepare_output_tables_clustering_alixe_second_round(dict_clust_by_rotclu, ali_confdict, sub_clust_path, keypool,
                                                        folder_mode, filter_single):
    # In the second round there are many things we cannot know!
    path_infoclust_table_second = os.path.join(sub_clust_path, keypool+"_info_clust_table_second_round")
    path_infoclust_raw_second = os.path.join(sub_clust_path , keypool+"_info_clust_raw")
    # Nice output table file
    table_clust_second_round = open(path_infoclust_table_second,'w')
    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
        if ali_confdict['ccfromphi']:
            table_clust_second_round.write(
                '%-40s %-5s %-10s %-10s\n' %
                ('Cluster', 'n_phs', 'phi_cc', 'phi_wmpe'))
        else:
            table_clust_second_round.write(
                '%-40s %-5s %-10s\n' %
                ('Cluster', 'n_phs', 'phi_wmpe'))
    else:
        if ali_confdict['ccfromphi']:
            table_clust_second_round.write(
                '%-40s %-5s %-10s \n' %
                ('Cluster', 'n_phs', 'phi_cc'))
        else:
            table_clust_second_round.write(
                '%-40s %-5s\n' %
                ('Cluster', 'n_phs'))
    # Raw output from the clustering
    raw_clust_first_round = open(path_infoclust_raw_second, 'w')
    del raw_clust_first_round
    # Get the information for the table
    for rotclu in dict_clust_by_rotclu.keys():
        print('We are evaluating rotation cluster', rotclu)
        for cluster in (dict_clust_by_rotclu[rotclu]).keys():
            print("\n\tEvaluating cluster ", cluster)
            n_phs = dict_clust_by_rotclu[rotclu][cluster]['n_phs']
            dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs'] = {}
            if dict_clust_by_rotclu[rotclu][cluster]['n_phs'] > 1:
                print("\n\t This cluster contains more than one phs")
                raw_clust_first_round = open(path_infoclust_raw_second, 'a')
                raw_clust_first_round.write(
                    "**********************************************************************************\n")
                raw_clust_first_round.write(str(cluster) + str(dict_clust_by_rotclu[rotclu][cluster]) + "\n")
                del raw_clust_first_round
                for phs in dict_clust_by_rotclu[rotclu][cluster]['dictio_result'].keys():  # For each phs in the cluster
                    print("\t Processing file ", phs)
                    shift = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phs]['shift_first']
                    if shift == [-1, -1, -1]:  # Then this phs entered in the third cycle and I need to catch that
                        shift = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phs]['shift_last']
                if ali_confdict['ccfromphi'] or ('ent_file' in ali_confdict.keys() and ali_confdict['postmortem']):
                    name_shelxe = ((os.path.split(cluster))[1])[:-4]
                    path_name_shelxe = os.path.join(sub_clust_path, name_shelxe)
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                        shutil.copy(ali_confdict['ent_file'], path_name_shelxe + ".ent")
                    shutil.copy(ali_confdict['hkl_file'], path_name_shelxe + ".hkl")
                    shutil.copy(ali_confdict['ins_file'], path_name_shelxe + ".ins")
                    phase_fragment_with_shelxe((ali_confdict['shelxe_line_alixe'], name_shelxe, sub_clust_path,
                                                        ali_confdict['shelxe_path'],'phi', True))
                    path_lst = os.path.join(sub_clust_path,name_shelxe + '.lst')
                    lst_file = open(path_lst, 'r')
                    lst_content = lst_file.read()
                    list_fom = extract_EFOM_and_pseudoCC_shelxe(lst_content)
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:  # Retrieve final MPE and save them too
                        list_mpe = extract_wMPE_shelxe(path_lst)
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_phi'] = list_mpe
                        wmpefinal_phi = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_phi'][2]
                    phicc = extract_INITCC_shelxe(lst_content, map=True)
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['efom_phi'] = list_fom[0]
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['pseudocc_phi'] = list_fom[1]
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC_phi'] = phicc
                name_cluster = os.path.split(cluster)[1].strip()
                name_cluster = os.path.basename(name_cluster)
                table_clust_second_round = open(path_infoclust_table_second, 'a')
                if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                    if ali_confdict['ccfromphi']:
                        table_clust_second_round.write(
                            '%-40s %-5i %-10.2f %-10.2f\n' %
                            (name_cluster, n_phs, phicc, wmpefinal_phi))
                    else:
                        table_clust_second_round.write(
                            '%-40s %-5i %-10.2f\n' %
                            (name_cluster, n_phs, wmpefinal_phi))
                else:
                    if ali_confdict['ccfromphi']:
                        table_clust_second_round.write(
                            '%-40s %-5i %-10.2f \n' %
                            (name_cluster, n_phs, phicc,))
                    else:
                        table_clust_second_round.write(
                            '%-40s %-5i\n' %
                            (name_cluster, n_phs))
                del table_clust_second_round
            else:
                if not filter_single:
                    name_file = cluster[:-4]  # The key is in itself the only file in the cluster
                    # NOTE CM: COMMENTING, NOT SURE WHY LIKE THIS AND IT IS GIVING A PROBLEM
                    #name_file = os.path.join(sub_clust_path, os.path.split(name_file)[1])
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                        # NOTE CM: quick and dirty. If we have phs then shall we do a PM?
                        if ali_confdict[sub_clust_path]['compute_phs'] == False and folder_mode:
                            dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'] = [-1,-1,-1,-1]
                        else:
                            # Unless I have a general dictio_fragments that I can pass to this function, I can't be sure
                            # I will be accessing this information! Leave it like this now and see if there is the need
                            if name_file.endswith('ref'):
                                dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'] = [-1,-1,-1,-1]
                                #dictio_fragments[keypool][name_file[:-4]]['list_MPE']
                            else:
                                dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'] = [-1,-1,-1,-1]
                                #    dictio_fragments[keypool][name_file]['list_MPE']
                            # # Get the shift and apply it to better see in Coot to what solutions they correspond
                            # lst_file = open(name_file + '.lst')
                            # lst_content = lst_file.read()
                            # shift_to_apply = extract_shift_from_shelxe(lst_content)
                            # if not shift_to_apply == [0.0, 0.0, 0.0]:
                            #     print("Moving pda ", name_file + ".pda",
                            #           ".pda with this shift respect to the ent ", shift_to_apply)
                            #     shifting_coordinates_inverse(shift_to_apply, name_file + '.pda')
                            #     add_cryst_card(ali_confdict['cryst_card'], name_file + "_shifted.pda")
                            #     os.rename(name_file + "_shifted.pda", name_file + "_shifted_to_final.pda")
                    # NOTE CM maybe this block should be under the check of compute_phs in case only phs were given
                    if name_file.endswith('ref'):
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC'] = -1
                            #dictio_fragments[keypool][name_file[:-4]]['initcc']
                    else:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC'] = -1
                        #dictio_fragments[keypool][name_file]['initcc']
                    singlecc = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC']
                    # NOTE CM maybe this block should be under the check of compute_phs in case only phs were given
                    raw_clust_first_round = open(path_infoclust_raw_second, 'a')
                    raw_clust_first_round.write(
                        "**********************************************************************************\n")
                    raw_clust_first_round.write(str(cluster) + str(dict_clust_by_rotclu[rotclu][cluster]) + "\n")
                    del raw_clust_first_round
                    table_clust_second_round = open(path_infoclust_table_second, 'a')
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                        wmpefinal = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'][2]
                        name_file = os.path.basename(name_file)
                        if ali_confdict['ccfromphi']:
                            table_clust_second_round.write(
                                '%-40s %-5i %-10.2f %-10.2f\n' %
                                (name_file, n_phs, singlecc, wmpefinal))
                        else:
                            table_clust_second_round.write(
                                '%-40s %-5i %-10.2f\n' %
                                (name_file, n_phs, wmpefinal))
                    else:
                        if ali_confdict['ccfromphi']:
                            table_clust_second_round.write(
                                '%-40s %-5i %-10.2f \n' %
                                (name_file, n_phs, singlecc,))
                        else:
                            table_clust_second_round.write(
                                '%-40s %-5i\n' %
                                (name_file, n_phs))

                    del table_clust_second_round
    # For each cluster write a summary table file with the information of its contents
    for cluster in dict_clust_by_rotclu[rotclu].keys():
        # Do this only if we have more than one phs
        if dict_clust_by_rotclu[rotclu][cluster]['n_phs'] > 1:
            path_clu = os.path.join(sub_clust_path, os.path.basename(cluster)[:-4] + '.sum')
            fileforclu = open(path_clu, 'w')
            fileforclu.write(
                '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (
                    'Name', 'wMPD_first', 'wMPD_last', 'diff_wMPD', 'mapcc_first',
                    'mapcc_last', 'shift_first_x', 'shift_first_y', 'shift_first_z', 'shift_last_x', 'shift_last_y',
                    'shift_last_z'))
            for phaseset in dict_clust_by_rotclu[rotclu][cluster]['dictio_result'].keys():
                name = os.path.basename(phaseset)
                wmpe_first = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['wMPE_first'], 2)
                wmpe_last = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['wMPE_last'], 2)
                if dict_clust_by_rotclu[rotclu][cluster]['n_phs'] > 1 and 'diff_wMPE' in \
                        dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]:
                    diffwmpe = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['diff_wMPE'],
                                     2)
                else:
                    diffwmpe = -1
                if dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_first'] != None:
                    mapcc_first = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_first'],
                                        2)
                else:
                    mapcc_first = -1
                if dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_last'] != None:
                    mapcc_last = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_last'],
                                       2)
                else:
                    mapcc_last = -1
                shift_first = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['shift_first']
                shift_last = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['shift_last']
                fileforclu.write(
                    '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (
                        name, wmpe_first, wmpe_last,
                        diffwmpe, mapcc_first,
                        mapcc_last,
                        shift_first[0],
                        shift_first[1],
                        shift_first[2],
                        shift_last[0],
                        shift_last[1],
                        shift_last[2]))
            del (fileforclu)



def prepare_output_tables_clustering_alixe(dict_clust_by_rotclu, ali_confdict, sub_clust_path, keypool,
                                           dictio_fragments, folder_mode):
    """

    :param dict_clust_by_rotclu:
    :param ali_confdict:
    :param sub_clust_path:
    :param keypool:
    :param dictio_fragments:
    :param folder_mode:
    :return:
    """
    # Nice output table file
    table_clust_first_round = open(os.path.join(sub_clust_path, keypool+"_info_clust_table"), 'w')
    # NOTE CM: All these conditions are not considering that if we have folder mode
    # we will not have topLLG and topZscore
    # This is handled at the moment at the plotting stage, and being written as -1 in the table.
    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
        if ali_confdict['fusedcoord']:
            if ali_confdict['ccfromphi']:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s %-10s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'fused_cc', 'fused_wmpe', 'phi_cc', 'phi_wmpe'))
            else:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s %-10s \n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'fused_cc', 'fused_wmpe'))
        else:
            if ali_confdict['ccfromphi']:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'phi_cc', 'phi_wmpe'))
            else:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'phi_wmpe'))
        del table_clust_first_round
    else:
        if ali_confdict['fusedcoord']:
            if ali_confdict['ccfromphi']:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'fused_cc', 'phi_cc'))
            else:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'fused_cc'))
        else:
            if ali_confdict['ccfromphi']:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg', 'phi_cc'))
            else:
                table_clust_first_round.write(
                    '%-40s %-5s %-10s %-10s\n' %
                    ('Cluster', 'n_phs', 'topzscore', 'topllg'))
        del table_clust_first_round

    # Raw output from the clustering
    raw_clust_first_round = open(os.path.join(sub_clust_path , keypool+"_info_clust_raw"), 'w')
    del raw_clust_first_round

    # Read clusters from results and process them
    count_cluster = 0
    for rotclu in dict_clust_by_rotclu.keys():
        print('We are evaluating rotation cluster', rotclu)
        for cluster in (dict_clust_by_rotclu[rotclu]).keys():
            print("\n\tEvaluating cluster ", cluster)
            n_phs = dict_clust_by_rotclu[rotclu][cluster]['n_phs']
            count_cluster = count_cluster + 1
            dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']={}
            if dict_clust_by_rotclu[rotclu][cluster]['n_phs'] > 1:
                print("\t This cluster contains more than one phs")
                raw_clust_first_round = open(os.path.join(sub_clust_path , keypool + "_info_clust_raw"), 'a')
                raw_clust_first_round.write(
                    "**********************************************************************************\n")
                raw_clust_first_round.write(str(cluster) + str(dict_clust_by_rotclu[rotclu][cluster]) + "\n")
                del raw_clust_first_round
                list_llg = []
                list_zscore = []
                list_of_filepaths = []  # list of files to join
                dict_clust_by_rotclu[rotclu][cluster][
                    'rot_clust_list'] = []  # Generate new key to save original rotation_cluster
                for phs in dict_clust_by_rotclu[rotclu][cluster]['dictio_result'].keys():  # For each phs in the cluster
                    print("\t Processing file ", phs)
                    keydictiofrag = os.path.join(sub_clust_path, phs[:-4])
                    if not folder_mode:
                        if 'llg_gimble_llg' in dictio_fragments[keypool][keydictiofrag].keys():
                            list_llg.append(dictio_fragments[keypool][keydictiofrag]['llg_gimble_llg'])
                        else:
                            list_llg.append(dictio_fragments[keypool][keydictiofrag]['llg_rbr'])
                        list_zscore.append(dictio_fragments[keypool][keydictiofrag]['zscore'])
                        if dictio_fragments[keypool][keydictiofrag]['rot_cluster'] not in dict_clust_by_rotclu[rotclu][cluster][
                            'rot_clust_list']:
                            # If more than 1 rot cluster elongated together you will have a list with len >1
                            dict_clust_by_rotclu[rotclu][cluster]['rot_clust_list'].append(
                                dictio_fragments[keypool][keydictiofrag]['rot_cluster'])
                    shift = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phs]['shift_first']
                    if shift == [-1, -1, -1]:  # Then this phs entered in the third cycle and I need to catch that
                        shift = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phs]['shift_last']
                    if ali_confdict['fusedcoord']:
                        if not (shift == [0.0, 0.0, 0.0]):  # Make sure it is not the reference
                            shifting_coordinates(
                                dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phs]['shift_first'],
                                keydictiofrag + '.pda')
                            list_of_filepaths.append(keydictiofrag + '_shifted.pda')  # Write pda with its shift
                        else:
                            list_of_filepaths.append(keydictiofrag + '.pda')

                if ali_confdict['fusedcoord']:
                    # Fuse the files in a single pdb
                    path_fused = os.path.join(sub_clust_path,cluster[:-4] + "_fused.pda")
                    fuse_pdbs(list_of_filepaths, path_fused)
                    add_cryst_card(ali_confdict['cryst_card'], path_fused)
                    # Check FOMs Starting from from the fused pda
                    name_shelxe = ((os.path.split(cluster))[1])[:-4] + "_fused"
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                        link_file(sub_clust_path, ali_confdict['ent_file'], name_shelxe + '.ent')
                    link_file(sub_clust_path, ali_confdict['hkl_file'], name_shelxe + ".hkl")
                    output, errors = phase_fragment_with_shelxe((ali_confdict['shelxe_line_alixe'], name_shelxe, sub_clust_path,
                                                        ali_confdict['shelxe_path'],'pda',True))
                    lst_file = open(os.path.join(sub_clust_path, name_shelxe + '.lst'), 'r')
                    lst_content = lst_file.read()
                    list_fom = extract_EFOM_and_pseudoCC_shelxe(lst_content)
                    initcc = extract_INITCC_shelxe(lst_content)
                    try:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['efom_fused'] = list_fom[0]
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['pseudocc_fused'] = list_fom[1]
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC_fused'] = initcc
                    except:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['efom_fused'] = -1
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['pseudocc_fused'] = -1
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC_fused'] = -1
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                        try:
                            path_lst = os.path.join(sub_clust_path, name_shelxe + '.lst')
                            list_mpe = extract_wMPE_shelxe(path_lst)
                            dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_fused'] = list_mpe
                            # Get the shift to final and apply it to better see in Coot to what solutions they correspond
                            lst_file = open(path_lst,'r')
                            lst_content = lst_file.read()
                            shift_to_apply = extract_shift_from_shelxe(lst_content)
                            if not shift_to_apply == [0.0, 0.0, 0.0]:
                                print("Moving pda ", name_shelxe, ".pda with this shift respect to the ent "
                                      , shift_to_apply)
                                shifting_coordinates_inverse(shift_to_apply,
                                                             os.path.join(sub_clust_path, name_shelxe + '.pda'))
                                add_cryst_card(ali_confdict['cryst_card'],
                                               os.path.join(sub_clust_path,  name_shelxe + "_shifted.pda"))
                                os.rename(os.path.join(sub_clust_path,  name_shelxe + "_shifted.pda"),
                                          os.path.join(sub_clust_path,  name_shelxe + "_shifted_to_final.pda"))
                        except:
                            print(sys.exc_info())
                            traceback.print_exc(file=sys.stdout)
                            dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_fused'] = [-1, -1, -1, -1]
                    fusedcc = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC_fused']
                if ali_confdict['ccfromphi'] or ('ent_file' in ali_confdict.keys() and ali_confdict['postmortem']):
                    # 2) Starting from from the phi file
                    name_shelxe = ((os.path.split(cluster))[1])[:-4]
                    path_name_shelxe = os.path.join(sub_clust_path, name_shelxe)
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                        shutil.copy(ali_confdict['ent_file'], path_name_shelxe + ".ent")
                    shutil.copy(ali_confdict['hkl_file'], path_name_shelxe + ".hkl")
                    shutil.copy(ali_confdict['ins_file'], path_name_shelxe + ".ins")
                    phase_fragment_with_shelxe((ali_confdict['shelxe_line_alixe'], name_shelxe, sub_clust_path,
                                                        ali_confdict['shelxe_path'],'phi', True))
                    path_lst = os.path.join(sub_clust_path,name_shelxe + '.lst')
                    lst_file = open(path_lst, 'r')
                    lst_content = lst_file.read()
                    list_fom = extract_EFOM_and_pseudoCC_shelxe(lst_content)
                    if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:  # Retrieve final MPE and save them too
                        list_mpe = extract_wMPE_shelxe(path_lst)
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_phi'] = list_mpe
                    phicc = extract_INITCC_shelxe(lst_content, map=True)
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['efom_phi'] = list_fom[0]
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['pseudocc_phi'] = list_fom[1]
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC_phi'] = phicc

                # We add the top LLG or ZSCORE as representative of the cluster
                if not folder_mode:
                    if 'dict_FOMs' not in dict_clust_by_rotclu[rotclu][cluster]:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']={}
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['llg'] = (sorted(list_llg, reverse=True))[0]
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['zscore'] = (sorted(list_zscore, reverse=True))[0]

                # Prepare to save info from clusters in this file
                name_cluster = os.path.split(cluster)[1]
                if not folder_mode:
                    topzscore = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['zscore']
                    topllg = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['llg']
                else:
                    topzscore = -1.0
                    topllg = -1.0

                if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                    if ali_confdict['fusedcoord']:
                        wmpefinal_fused = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_fused'][2]
                    # If there is postmortem, then we have computed the phi wMPE
                    wmpefinal_phi = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs_phi'][2]
                    table_clust_first_round = open(os.path.join(sub_clust_path, keypool+"_info_clust_table"), 'a')
                    if ali_confdict['fusedcoord']:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write('%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f %-10.2f %-10.2f\n' % (
                                    name_cluster, n_phs, topzscore, topllg, fusedcc, wmpefinal_fused, phicc,
                                    wmpefinal_phi))
                        else:
                            table_clust_first_round.write('%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f\n' % (
                                name_cluster, n_phs, topzscore, topllg, fusedcc, wmpefinal_fused))
                    else:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write('%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f\n' % (
                                name_cluster, n_phs, topzscore, topllg, phicc, wmpefinal_phi))
                        else:
                            table_clust_first_round.write('%-40s %-5i %-10.2f %-10.2f %-10.2f\n' % (
                                name_cluster, n_phs, topzscore, topllg, wmpefinal_phi))
                    del table_clust_first_round
                else:
                    table_clust_first_round = open(os.path.join(sub_clust_path,keypool+ "_info_clust_table"), 'a')
                    if ali_confdict['fusedcoord']:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc, phicc))
                        else:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc))
                    else:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f\n' % (
                                name_cluster, n_phs, topzscore, topllg, phicc))
                        else:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f\n' % (name_cluster, n_phs, topzscore, topllg))

                    del table_clust_first_round
            else:
                name_file = cluster[:-4] # The key is in itself the only file in the cluster
                name_file = os.path.join(sub_clust_path, os.path.split(name_file)[1])
                if not folder_mode:
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs'] = {}
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC'] = dictio_fragments[keypool][name_file]['initcc']
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['pseudocc'] = dictio_fragments[keypool][name_file][
                        'pseudocc']
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['efom'] = dictio_fragments[keypool][name_file]['efom']
                    # Save also the phaser FOMs
                    if 'llg_gimble_llg' in dictio_fragments[keypool][name_file].keys():
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['llg'] = dictio_fragments[keypool][name_file]['llg_gimble_llg']
                    else:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['llg']=dictio_fragments[keypool][name_file]['llg_rbr']
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['zscore'] = dictio_fragments[keypool][name_file]['zscore']
                    list_rot = []
                    list_rot.append(dictio_fragments[keypool][name_file]['rot_cluster'])
                    dict_clust_by_rotclu[rotclu][cluster]['rot_clust_list'] = list_rot
                else:
                    dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs'] = {}
                if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                    # NOTE CM: quick and dirty. If we have phs then shall we do a PM?
                    if ali_confdict[sub_clust_path]['compute_phs'] == False and folder_mode:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'] = [-1,-1,-1,-1]
                    else:
                        dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'] = dictio_fragments[keypool][name_file]['list_MPE']
                        # NOTE CM: this postmortem would require the lst files to be there and this is causing
                        # problems with chescat
                        # # Get the shift and apply it to better see in Coot to what solutions they correspond
                        # lst_file = open(name_file + '.lst')
                        # lst_content = lst_file.read()
                        # shift_to_apply = extract_shift_from_shelxe(lst_content)
                        # if not shift_to_apply == [0.0, 0.0, 0.0]:
                        #     print("Moving pda ", name_file + ".pda",
                        #           ".pda with this shift respect to the ent ", shift_to_apply)
                        #     shifting_coordinates_inverse(shift_to_apply, name_file + '.pda')
                        #     add_cryst_card(ali_confdict['cryst_card'], name_file + "_shifted.pda")
                        #     os.rename(name_file + "_shifted.pda", name_file + "_shifted_to_final.pda")
                # Write the information about the cluster in the files
                raw_clust_first_round = open(os.path.join(sub_clust_path , keypool+"_info_clust_raw"), 'a')
                raw_clust_first_round.write(
                    "**********************************************************************************\n")
                raw_clust_first_round.write(str(cluster) + str(dict_clust_by_rotclu[rotclu][cluster]) + "\n")
                del raw_clust_first_round
                name_cluster = os.path.split(cluster)[1].strip()
                if not folder_mode:
                    topzscore = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['zscore']
                    topllg = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['llg']
                    fusedcc = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['CC']
                else:  # TODO: This is quick and dirty to get the mode to work
                    topzscore = -1.0
                    topllg = -1.0
                    if ali_confdict[sub_clust_path]['compute_phs']:
                        fusedcc = dictio_fragments[keypool][name_file]['initcc']
                    else:
                        fusedcc = -1
                if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                    if not folder_mode:
                        wmpefinal = dict_clust_by_rotclu[rotclu][cluster]['dict_FOMs']['final_MPEs'][2]
                    else:
                        if ali_confdict[sub_clust_path]['compute_phs']: # again, this we would have if we have or produce the lst ourselves
                            wmpefinal = dictio_fragments[keypool][name_file]['list_MPE'][2]
                        else:
                            wmpefinal = -1.0
                    table_clust_first_round = open(os.path.join(sub_clust_path,keypool+"_info_clust_table"), 'a')
                    if ali_confdict['fusedcoord']:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write('%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc, wmpefinal, fusedcc, wmpefinal))
                        else:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc, wmpefinal))
                    else:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc, wmpefinal))
                        else:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg,  wmpefinal))
                    del table_clust_first_round
                else:
                    table_clust_first_round = open(os.path.join(sub_clust_path,keypool+"_info_clust_table"), 'a')
                    if ali_confdict['fusedcoord']:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc, fusedcc))

                        else:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg, fusedcc))
                    else:
                        if ali_confdict['ccfromphi']:
                            table_clust_first_round.write(
                                    '%-40s %-5i %-10.2f %-10.2f %-10.2f\n' %
                                    (name_cluster, n_phs, topzscore, topllg, fusedcc))
                        else:
                            table_clust_first_round.write(
                                '%-40s %-5i %-10.2f %-10.2f\n' %
                                (name_cluster, n_phs, topzscore, topllg))
                    del table_clust_first_round
        # For each cluster write a summary table file with the information of its contents
        for cluster in dict_clust_by_rotclu[rotclu].keys():
            # Do this only if we have more than one phs
            if dict_clust_by_rotclu[rotclu][cluster]['n_phs']>1:
                path_clu = os.path.join(sub_clust_path, os.path.basename(cluster)[:-4] + '.sum')
                fileforclu = open(path_clu, 'w')
                fileforclu.write(
                    '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (
                        'Name', 'wMPD_first', 'wMPD_last', 'diff_wMPD', 'mapcc_first',
                        'mapcc_last', 'shift_first_x', 'shift_first_y', 'shift_first_z', 'shift_last_x', 'shift_last_y',
                        'shift_last_z'))
                for phaseset in dict_clust_by_rotclu[rotclu][cluster]['dictio_result'].keys():
                    name = os.path.basename(phaseset)
                    wmpe_first = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['wMPE_first'], 2)
                    wmpe_last = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['wMPE_last'], 2)
                    if dict_clust_by_rotclu[rotclu][cluster]['n_phs'] > 1 and 'diff_wMPE' in dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]:
                        diffwmpe = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['diff_wMPE'],
                                         2)
                    else:
                        diffwmpe = -1
                    if dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_first'] != None:
                        mapcc_first = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_first'],
                                            2)
                    else:
                        mapcc_first = -1
                    if dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_last'] != None:
                        mapcc_last = round(dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['mapcc_last'],
                                           2)
                    else:
                        mapcc_last = -1
                    shift_first = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['shift_first']
                    shift_last = dict_clust_by_rotclu[rotclu][cluster]['dictio_result'][phaseset]['shift_last']
                    fileforclu.write(
                        '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (
                            name, wmpe_first, wmpe_last,
                            diffwmpe, mapcc_first,
                            mapcc_last,
                            shift_first[0],
                            shift_first[1],
                            shift_first[2],
                            shift_last[0],
                            shift_last[1],
                            shift_last[2]))
                del (fileforclu)


def change_key_dictio_clust_dict(dict_clust_by_rotclu,clust_fold):
    # NOTE: Because of the relative paths, I need to modify the dictionary now to contain the full paths
    for rotclu in dict_clust_by_rotclu.keys():
        for key1 in dict_clust_by_rotclu[rotclu].keys():
            new_key1 = os.path.join(clust_fold, os.path.split(key1)[1])
            dict_clust_by_rotclu[rotclu][new_key1] = copy.deepcopy(dict_clust_by_rotclu[rotclu][key1])
            del dict_clust_by_rotclu[rotclu][key1]
            for key2 in dict_clust_by_rotclu[rotclu][new_key1]['dictio_result'].keys():
                new_key2 = os.path.join(clust_fold, os.path.split(key2)[1])
                dict_clust_by_rotclu[rotclu][new_key1]['dictio_result'][new_key2] = copy.deepcopy(
                    dict_clust_by_rotclu[rotclu][new_key1]['dictio_result'][key2])
                del dict_clust_by_rotclu[rotclu][new_key1]['dictio_result'][key2]
    return dict_clust_by_rotclu


def change_shelxe_line_for_alixe(shelxe_line):
    '''Modifies a given shelxe line to adapt it to the necessary parameterization for alixe.

    Args:
        shelxe_line (str): command line for shelxe

    Returns:
        shelxe_line (str): modified command line for shelxe

    '''
    list_arg = shelxe_line.split()
    new_shelxe_line = ""
    for arg in list_arg:
        if arg.startswith("-a"):
            new_shelxe_line += "-a0 " # 0 autotracing cycles
        elif arg.startswith("-m"):
            new_shelxe_line += "-m5 " # 5 cycles of density modification
        elif arg.startswith("-v"):
            new_shelxe_line += "-v0 " # no density sharpening
        elif arg.startswith("-y"):
            new_shelxe_line += "-y1.0 " # use all available resolution to compute phases
        elif arg.startswith("-e"): # leave whathever free lunch was in the original shelxe line
            pass
        elif arg.startswith("-o"): # leave the trimming optimization if it was present in the original shelxe line
            pass
        else:
            new_shelxe_line += arg + " " # every other argument can be the same
    return new_shelxe_line


def extract_INITCC_shelxe(complete_output,map=False):
    """Given the contents of an lst file (output from shelxe),
    it will parse it initial correlation coefficient and return it"""
    lines = complete_output.split("\n")
    for i in range(len(lines)):
        if lines[i].startswith(" Overall CC between native Eobs and Ecalc (from fragment)") and not map:
            initcc = float((lines[i].split()[10])[:-1])
            return initcc
        if lines[i].startswith("Overall CC between native Eobs and Ecalc (from map)") and map:
            initcc = float((lines[i].split()[10])[:-1])
            return initcc
    return -1.0

def extract_EFOM_and_pseudoCC_shelxe(complete_output):
    """Given the contents of an lst file (output from shelxe), it will look for the value of the mean FOM and Pseudo-Free CC and return them"""
    # Example format: Estimated mean FOM = 0.485   Pseudo-free CC = 49.91 %
    lines = complete_output.split("\n")
    regexFOM = re.compile('Estimated mean FOM = ')
    regexCC = re.compile('Pseudo-free CC =')
    for i in range(len(lines)):
        if bool(regexFOM.findall(lines[i])) and bool(regexCC.findall(lines[i])):
            list_val=lines[i].split()
            if len(list_val)==10: #all OK size is normal
                fom = float(list_val[4])
                pseudocc = float(list_val[8])
            elif len(list_val)==9: # one of the two values is negative
                if list_val[3].startswith('=') and len(list_val[3])>1: # fom is negative
                    fom = float(list_val[3][1:])
                    pseudocc = float(list_val[8])
                else:
                    fom = float(list_val[4])
                    pseudocc = float(list_val[7][1:])
            elif len(list_val)==8: # the two values are negative
                    fom = float(list_val[3][1:])
                    pseudocc = float(list_val[7][1:])
            return fom, pseudocc


def extract_best_CC_shelxe(complete_output):
    """Given the contents of an lst file (output from shelxe), it will look for the value of the final best value of CC"""
    # Example format:  Best trace (cycle   1 with CC  8.64%) was saved as all_phs_0_92.pdb
    lines = complete_output.split("\n")
    regexCC = re.compile('Best trace')
    for i in range(len(lines)):
        if bool(regexCC.findall(lines[i])):
            cut_first = lines[i].split("%")[0]
            CC = float(cut_first.split()[6])
            #print("\nFinal CC " + str(CC) + " %")
            return CC


def extract_shift_from_shelxe(complete_output):
    # Example format: Origin shift relative to model in .ent:  dx= 0.000  dy= 0.375  dz= 0.500
    regexshift = re.compile(' Shift from model in .ent')
    lines = complete_output.split("\n")
    shift = []
    for i in range(len(lines)):
        if bool(regexshift.findall(lines[i])):
            values = lines[i].split("=")
            for x in range(len(values)):
                if x in [1, 2, 3]:
                    shift.append(float(values[x].split()[0]))
    for index in range(len(shift)):
        shift[index] = float(shift[index])
    return shift


def extract_wMPE_shelxe(lst_path):
    """Given the contents of an lst file (output from shelxe), it will look for the wMPEs values and return them"""
    # Example format:  <cos> 0.002 / 0.013  <fom> 0.261 / 0.430  MPE  89.8 / 89.2  wMPE 88.9 / 87.4
    # Or worse: <cos> 0.020 /-0.109  <fom> 0.293 / 0.584  MPE  88.6 / 99.8  wMPE 88.6 /102.7
    p = subprocess.Popen('grep  wMPE ' + lst_path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    pout, perr = p.communicate()
    pout = pout.strip()
    regexwMPE = re.compile('wMPE')
    file_lst = open(lst_path, 'r')
    list_lines_wMPE = []
    lines_lst = file_lst.readlines()
    for i in range(len(lines_lst)):
        if bool(regexwMPE.findall(lines_lst[i])):
            list_lines_wMPE.append((lines_lst[i].strip("\n")))
    list_first = list_lines_wMPE[0].split("/")
    list_second = list_lines_wMPE[-1].split("/")
    wMPEa = float((list_first[3].split())[2])
    wMPEb = float(list_first[4])
    wMPEc = float((list_second[3].split())[2])
    wMPEd = float(list_second[4])
    return [wMPEa, wMPEb, wMPEc, wMPEd]


def extract_table_resolution_shelxe(complete_output):
    """Given the contents of an lst file (output from shelxe), it will look for the table of mean FOM and mapCC
    as a function of resolution and
    return it in the form of a dictionary where keys are d, FOM, mapCC and N"""
    dictio_result = {}
    lines = complete_output.split("\n")
    regex_table = re.compile('Estimated mean FOM and mapCC as a function of resolution')
    for i in range(len(lines)):
        if bool(regex_table.findall(lines[i])):
            line_res_shell = lines[
                i + 1]  # d    inf - 4.41 - 3.47 - 3.03 - 2.74 - 2.54 - 2.39 - 2.27 - 2.17 - 2.08 - 2.00
            list_res = line_res_shell.split("-")
            dictio_result["d"] = list_res[1:]
            line_FOM = lines[i + 2]  # <FOM>
            list_FOM = line_FOM.split()
            dictio_result["<FOM>"] = list_FOM[1:]
            line_mapCC = lines[i + 3]  # <mapCC>
            list_mapCC = line_mapCC.split()
            dictio_result["<mapCC>"] = list_mapCC[1:]
            line_N = lines[i + 4]  # N
            list_N = line_N.split()
            dictio_result["N"] = list_N[1:]
    return dictio_result


def extract_remark_cluster_pdb(pdb_content):
    pdb_lines = pdb_content.split("\n")
    for line in pdb_lines:
        if line.startswith("REMARK CLUSTER"):  # E.G. REMARK CLUSTER 7
            rotclu = (line.split())[2]
            return rotclu


def extract_cryst_card_pdb(pdb_content):
    pdb_lines = pdb_content.split("\n")
    for linea in pdb_lines:
        if linea.startswith("CRYST1"):  # E.G. CRYST1   30.279   91.989   32.864  90.00 112.60  90.00 P 1 21 1      2
            cryst_card = linea
            return cryst_card
    return None


def fill_dictio_fragments(dictio_fragments, sub_clust_key, sub_clust_path, list_pdbs, ali_confdict):
    # Checking the figures of merit of the single solutions
    # Just add the key of the pool
    dictio_fragments[sub_clust_key] = {}
    for pdb in list_pdbs:
        dictio_fragments[sub_clust_key][pdb[:-4]] = {'rot_cluster': None, 'llg': None, 'zscore': None,
                                                     'initcc': None, 'efom': None, 'pseudocc': None,
                                                     'list_MPE': None}
    n_single_solutions = len(list_pdbs)

    print("\nThere are ", n_single_solutions, " single solutions in ", sub_clust_path)

    # FOMs from lst files
    dictio_fragments = get_FOMs_from_lst_files_in_folder(dictio_fragments=dictio_fragments,
                                                        ali_confdict=ali_confdict,remove_after=True)

    # From SUMs
    gimble = check_if_gimble(ali_confdict[sub_clust_path]['type_run'],
                                ali_confdict[sub_clust_path]['wd_run'])
    # This is for a single fragment
    dictio_fragments = get_FOMs_from_sum_files_in_folder(wd=ali_confdict[sub_clust_path]['wd_run'],
                                                            clust_fold=sub_clust_path,
                                                            dictio_fragments=dictio_fragments,
                                                            keypool=sub_clust_key,
                                                            gimble=gimble,
                                                            program=ali_confdict[sub_clust_path]['type_run'],
                                                            fragment=ali_confdict['fragment'])
    return dictio_fragments

def fill_ali_confdict_with_defaults(ali_confdict, current_directory, program):
    # NOTE CM: pending to implement if there will be different defaults or other changes
    # depending on the program (shredder, borges, lite
    # if program == 'BORGES':
    # else: # then it is ARCIMBOLDO
    # Defaults are found in al.defaults_alixe
    Config = configparser.ConfigParser()
    # Read the defaults and write a configuration file
    Config.readfp(io.StringIO(defaults_alixe))
    path_alixe_bor = os.path.join(current_directory, 'alixe_conf.bor')
    file_alixe_bor = open(path_alixe_bor, 'w')
    Config.write(file_alixe_bor)
    del file_alixe_bor
    ali_confdict_defaults = read_confibor_alixe(path_alixe_bor)
    for key in ali_confdict_defaults.keys():
        if key not in ali_confdict:
            ali_confdict[key] = ali_confdict_defaults[key]  # put the default one
        else:
            # then we want to keep the value we had
            continue
    # Now we can decide if we want to modify something
    # Commenting the ones I had first
    # ali_confdict['minchunk'] = 100
    # ali_confdict['limit_sol_per_rotclu'] = 1000  # hard limit solutions to take from each rotclu
    # ali_confdict['max_non_clust_events'] = 20 * ali_confdict['number_cores_parallel']
    # if ent:
    #     ali_confdict['ent_file'] = ent
    #     ali_confdict['postmortem'] = True
    # else:
    #     ali_confdict['postmortem'] = False
    # ali_confdict['hkl_file'] = hkl
    # ali_confdict['shelxe_line_alixe'] = shlxLinea0
    # ali_confdict['shelxe_path'] = SELSLIB2.PATH_NEW_SHELXE
    # # These ones are related with the analysis of the phase clusters
    # ali_confdict['fusedcoord'] = False
    # ali_confdict['ccfromphi'] = False
    # ali_confdict[clust_fold_rotclu] = {'compute_phs': False}
    # ali_confdict['plots'] = True
    # # These are for setting chescat runs
    # ali_confdict["tolerance_first_round"] = 60
    # ali_confdict["tolerance_merging"] = 90
    # ali_confdict["resolution_comparison"] = 4.0
    # ali_confdict["seed"] = 1  # this is only for the sequential part
    # ali_confdict["cycles"] = 3
    # ali_confdict["origin_search"] = 'sxosfft'
    # ali_confdict["weight"] = 'e'
    # ali_confdict["oricheck"] = True
    # ali_confdict["map_cc"] = True
    # ali_confdict['resolution_merging'] = 2.0
    # ali_confdict['filter_single'] = False
    return ali_confdict


def fuse_pdbs(list_of_filepaths, path_pdb):
    """
    :param list_of_filepaths:
    :type list_of_filepaths:
    :param path_pdb:
    :type path_pdb:
    :return:
    :rtype:
    """
    list_of_structures = []
    parser = PDBParser()
    for pdb_file in list_of_filepaths:
        structure = parser.get_structure(pdb_file[:-4], pdb_file)
        list_of_structures.append(structure)
    main_structure = list_of_structures[0]
    for x, structure in enumerate(list_of_structures):
        model = structure[0]
        if x != 0:
            model.id = x
            model.serial_num = x
            main_structure.add(model)
    io = PDBIO()
    io.set_structure(main_structure)
    io.save(path_pdb, write_end=False)


def get_general_paths_for_alixe(Config, ali_confdict):
    """ Read the bor file and get info about the filepaths, save to dictio

    :param Config:
    :param ali_confdict:
    :return: ali_confdict
    """

    hkl_filename = Config.get("GENERAL", "hkl_path")
    if Config.has_option("GENERAL", "ent_path"):
        ent_filename = Config.get("GENERAL", "ent_path")
        ali_confdict['ent_file'] = os.path.abspath(ent_filename)
    else:
        ent_filename = None
    ali_confdict['hkl_file'] = os.path.abspath(hkl_filename)
    return ali_confdict

def get_arcirun_info_for_alixe(Config, ali_confdict, sub_clust_path):
    """ Retrieve shelxe line and info about type of run

    :param Config:
    :param ali_confdict:
    :return: ali_confdict
    """

    sections = Config.sections()
    wd_run = Config.get("GENERAL", "working_directory")
    for section in sections:
        if section in ('ARCIMBOLDO', 'ARCIMBOLDO-BORGES','ARCIMBOLDO-SHREDDER'):
            name_job = Config.get(section, "name_job")
            shelxe_line = get_shelxe_line_from_html_output(name_job, wd_run)
            if 'ent_file' in ali_confdict.keys() and ali_confdict['postmortem']:
                shelxe_line = shelxe_line + " -x"
            shelxe_line_alixe = change_shelxe_line_for_alixe(shelxe_line)
            ali_confdict['shelxe_line_expansion'] = shelxe_line
            ali_confdict['shelxe_line_alixe'] = shelxe_line_alixe
            # TODO CM: use the topexp information to decide attempts for clustering/expanding
            # topexp = get_topexp_from_html_output(name_job, wd_run)
            # NOTE CM: Now we should link what each folder is in terms of ARCIMBOLDO runs
            if section == 'ARCIMBOLDO':
                fragment = Config.get("ARCIMBOLDO", "fragment_to_search")
                type_run = 'ARCIMBOLDO'
            elif section == "ARCIMBOLDO-BORGES":
                fragment = 1 # single copy search
                type_run = 'BORGES'
            elif section == "ARCIMBOLDO-SHREDDER":
                # Read the method used to know if it is launching ARCIMBOLDO_BORGES or ARCIMBOLDO_LITEs
                shred_method = Config.get('ARCIMBOLDO-SHREDDER', 'SHRED_METHOD')
                if shred_method == 'spherical' or shred_method == 'secondary_structure':
                    # Then inside the working directory an ARCIMBOLDO_BORGES folder should have been written
                    fragment = 1 # single copy search
                    type_run = 'BORGES'
                    wd_run = os.path.join(wd_run, 'ARCIMBOLDO_BORGES')
                elif shred_method == 'sequential':
                    print("Currently this mode is not supported ", shred_method)
                    sys.exit(1)
    # I need to know the wd_run and the other things to retrieve the files later on
    ali_confdict[sub_clust_path] = {}
    ali_confdict[sub_clust_path]['wd_run'] = wd_run
    ali_confdict[sub_clust_path]['fragment_search'] = fragment
    ali_confdict[sub_clust_path]['type_run'] = type_run
    return ali_confdict

def get_computing_info_for_alixe(Config, ali_confdict):
    """ Read the bor obj and get information about the computing setup, saving it to the dictionary

    :param Config:
    :param ali_confdict:
    :return:
    """
    multiproc = False
    if not Config.has_section("CONNECTION"):
        multiproc = True
    else:
        computing = Config.get("CONNECTION", "distribute_computing")
        if computing!='multiprocessing':
            # NOTE: The operations related with reading the setup bor and the like are OK only for OUR setup
            # In condor we can read the local one from the setup.bor
            path_setup = Config.get("CONNECTION", "setup_bor_path")
            Config2 = configparser.ConfigParser()
            Config2.read(path_setup)
            try:
                shelxe_path = Config2.get("LOCAL", "path_local_shelxe")
            except:
                print("\nThe bor file did not contain a LOCAL section, assuming shelxe is in the path")
                shelxe_path = 'shelxe'
        else:
            multiproc=True

    if multiproc == True:
        try:
            shelxe_path = Config.get("LOCAL", "path_local_shelxe")
        except:
            print("\nThe bor file did not contain a LOCAL section, assuming shelxe is in the path")
            shelxe_path = 'shelxe'
    ali_confdict['shelxe_path'] = shelxe_path
    return ali_confdict


def get_list_rotation_clusters_from_dictio_fragments(dictio_fragments, keypool):
    """

    :param dictio_fragments:
    :param keypool:
    :return:
    """
    list_rot_cluster = []
    for frag in dictio_fragments[keypool].keys():
        rotclu = dictio_fragments[keypool][frag]['rot_cluster']
        if rotclu not in list_rot_cluster:
            list_rot_cluster.append(rotclu)
    return list_rot_cluster

def get_spacegroup_dictionary():
    return copy.deepcopy(dictio_space_groups)


def get_FOMs_from_lst_files_in_folder(dictio_fragments, ali_confdict, remove_after=False):
    """ Get the figures of merit form the shelxe output files .lst

    :param dictio_fragments:
    :param ali_confdict:
    :param remove_after:
    :return:
    """
    for pooli in dictio_fragments.keys():
        print("\nAnalysing FOMs from lst files from ",pooli)
        for pdb_name in dictio_fragments[pooli].keys():
            lst_file = open(pdb_name + '.lst', 'r')
            lst_content = lst_file.read()
            list_fom = extract_EFOM_and_pseudoCC_shelxe(lst_content)
            dictio_fragments[pooli][pdb_name]['efom'] = list_fom[0]
            dictio_fragments[pooli][pdb_name]['pseudocc'] = list_fom[1]
            dictio_fragments[pooli][pdb_name]['initcc'] = extract_INITCC_shelxe(lst_content)
            if ali_confdict['postmortem'] and ('ent_file' in ali_confdict) :  # Only if post-mortem has been performed in shelxe
                list_MPE = extract_wMPE_shelxe(pdb_name + '.lst')
                dictio_fragments[pooli][pdb_name]['list_MPE'] = list_MPE
            if remove_after:
                os.remove(pdb_name + '.lst')
    return dictio_fragments


def get_FOMs_from_sum_files_in_folder(wd, clust_fold, dictio_fragments, keypool, gimble=True, program='BORGES',
                                      fragment=1):
    """ Get the LLGs and ZSCOREs for individual solutions from the SUM folder of either BORGES or LITE run.

    :param wd: working directory of the ARCIMBOLDO, BORGES OR SHREDDER run
    :type wd: str
    :param clust_fold: folder where the files for clustering or their links are located
    :type clust_fold: str
    :param dictio_fragments:
    :type dictio_fragments: dict
    :param keypool:
    :type keypool: str
    :param ent_present:
    :type ent_present: bool
    :param program: ARCIMBOLDO or BORGES
    :type program: str
    :param fragment:
    :type fragment: int
    :return:
    :rtype:
    """
    inverted = False
    if program == 'ARCIMBOLDO':
        fragfold = 'ens1_frag'+str(fragment)
        sum_path_LLG = os.path.join(wd, fragfold+"/5_RNP_LIBRARY/clusters.sum")
        if os.path.exists(os.path.join(wd, fragfold+"/4_PACK_LIBRARY/clusters.sum")):
            sum_path_ZSCORE_1 = os.path.join(wd, fragfold+"/4_PACK_LIBRARY/clusters.sum")
            if os.path.exists(os.path.join(wd, fragfold+"/4.5_INVERTED_LIBRARY/clusters.sum")):
                sum_path_ZSCORE_2 = os.path.join(wd, fragfold+"/4.5_INVERTED_LIBRARY/clusters.sum")
                inverted = True
        else:  # Take the FOMS from the translation folder if no packing set
            sum_path_ZSCORE_1 = os.path.join(wd, fragfold+"/3_FTF_LIBRARY/clusters.sum")
        sol_refined, conv_names_refined = SELSLIB2.readClustersFromSUM(sum_path_LLG)
        sol_pack1, conv_names_pack1 = SELSLIB2.readClustersFromSUM(sum_path_ZSCORE_1)
        if inverted:
            sol_pack2, conv_names_pack2 = SELSLIB2.readClustersFromSUM(sum_path_ZSCORE_2)
        for clu in sol_refined:
            for item in clu["heapSolutions"].asList():
                prio, solu = item
                ensemble = solu['name']
                name = conv_names_refined[ensemble]
                id_frag = os.path.abspath(os.path.join(clust_fold, ((name.split("/"))[-1])[:-4]))
                if id_frag in dictio_fragments[keypool].keys():
                    dictio_fragments[keypool][id_frag]['llg'] = solu['llg']
                    dictio_fragments[keypool][id_frag]['rot_cluster'] = solu['original_rotcluster']
        for clu in sol_pack1:
            for item in clu["heapSolutions"].asList():
                prio, solu = item
                ensemble = solu['name']
                if ensemble in conv_names_refined.keys():
                    name = conv_names_refined[ensemble]
                    id_frag = os.path.abspath(os.path.join(clust_fold, ((name.split("/"))[-1])[:-4]))
                    if id_frag in dictio_fragments[keypool].keys():
                        dictio_fragments[keypool][id_frag]['zscore'] = solu['zscore']
        if inverted:
            for clu in sol_pack2:
                for item in clu["heapSolutions"].asList():
                    prio, solu = item
                    ensemble = solu['name']
                    if ensemble in conv_names_refined.keys():
                        name = conv_names_refined[ensemble]
                        id_frag = os.path.abspath(os.path.join(clust_fold, ((name.split("/"))[-1])[:-4]))
                        if id_frag in dictio_fragments[keypool].keys():
                            dictio_fragments[keypool][id_frag]['zscore'] = solu['zscore']
    elif program == 'BORGES':
        path_pack = os.path.join(wd, "7.5_PACK_Library")
        for rotclu in os.listdir(path_pack):
            sum_path_rottra = os.path.join(wd, "7.5_PACK_Library", rotclu, "clustersRed.sum")
            if os.path.exists(sum_path_rottra):
                clusters_rottra, conv_names_rottra = SELSLIB2.readClustersFromSUM(sum_path_rottra)
            else:
                continue
            for clu in clusters_rottra:
                for item in clu["heapSolutions"].asList():
                    prio, solu = item
                    ensemble = solu['name']
                    name = conv_names_rottra[ensemble]
                    pdb_frag = ((name.split("/"))[-1])[:-4]
                    if len(ensemble.split('-')) > 1:
                        position = (((ensemble.split('.'))[0]).split('-'))[1]
                        id_frag1 = os.path.abspath(os.path.join(clust_fold, pdb_frag + '-' + position + "_rottra_" + rotclu))
                        id_frag2 = os.path.abspath(os.path.join(clust_fold, pdb_frag + '-' + position + "_rbr_" + rotclu))
                    elif len(ensemble.split('-')) == 1:
                        id_frag1 = os.path.abspath(os.path.join(clust_fold, pdb_frag + "_rottra_" + rotclu))
                        id_frag2 = os.path.abspath(os.path.join(clust_fold, pdb_frag + "_rbr_" + rotclu))
                    if id_frag1 in dictio_fragments[keypool].keys():
                        dictio_fragments[keypool][id_frag1]['llg'] = solu['llg']
                        dictio_fragments[keypool][id_frag1]['rot_cluster'] = solu['original_rotcluster']
                        dictio_fragments[keypool][id_frag1]['zscore'] = solu['zscore']
                    if id_frag2 in dictio_fragments[keypool].keys():
                        dictio_fragments[keypool][id_frag2]['rot_cluster'] = solu['original_rotcluster']
                        dictio_fragments[keypool][id_frag2]['zscore'] = solu['zscore']
            # NOTE CM: changing to get all LLGs from the different refinement steps
            def fill_LLGs_refinement(clusters_ref,conv_names,dictio_fragments,keypool,key_llg):
                for clu in clusters_ref:
                    for item in clu["heapSolutions"].asList():
                        prio, solu = item
                        ensemble = solu['name']
                        name = conv_names[ensemble]
                        pdb_frag = ((name.split("/"))[-1])[:-4]
                        if len(ensemble.split('-')) > 1:
                            position = (((ensemble.split('.'))[0]).split('-'))[1]
                            id_frag = os.path.abspath(os.path.join(clust_fold, pdb_frag + '-' + position + "_rbr_" + rotclu))
                        elif len(ensemble.split('-')) == 1:
                            id_frag = os.path.abspath(os.path.join(clust_fold, pdb_frag + "_rbr_" + rotclu))
                        if id_frag in dictio_fragments[keypool].keys():
                            dictio_fragments[keypool][id_frag][key_llg] = solu['llg']
                return dictio_fragments
            if gimble:
                sum_path_gimble_llg = os.path.join(wd, "8_GIMBLE_LLG", rotclu, "clustersNoRed.sum")
                clusters_gimble_llg, conv_names_gimble_llg = SELSLIB2.readClustersFromSUM(sum_path_gimble_llg)
                dictio_fragments = fill_LLGs_refinement(clusters_ref=clusters_gimble_llg,
                                                        conv_names=conv_names_gimble_llg,
                                                        dictio_fragments=dictio_fragments,
                                                        keypool=keypool, key_llg='llg_gimble_llg')
                sum_path_gimble = os.path.join(wd, "8_GIMBLE", rotclu, "clustersNoRed.sum")
                clusters_gimble, conv_names_gimble = SELSLIB2.readClustersFromSUM(sum_path_gimble)
                dictio_fragments = fill_LLGs_refinement(clusters_ref=clusters_gimble,
                                                        conv_names=conv_names_gimble,
                                                        dictio_fragments=dictio_fragments,
                                                        keypool=keypool, key_llg='llg_gimble')
            sum_path_rbr = os.path.join(wd, "8_RBR", rotclu, "clustersNoRed.sum")
            clusters_rbr, conv_names_rnp = SELSLIB2.readClustersFromSUM(sum_path_rbr)
            dictio_fragments = fill_LLGs_refinement(clusters_ref=clusters_rbr,
                                                    conv_names=conv_names_rnp,
                                                    dictio_fragments=dictio_fragments,
                                                    keypool=keypool, key_llg='llg_rbr')

    return dictio_fragments


def get_symops_from_sg_dictionary(space_group_key):
    """

    :param space_group_key:
    :type space_group_key:
    :return:
    :rtype:
    """
    if isinstance(space_group_key, int):
        symops = dictio_space_groups[space_group_key]['symops']
    elif isinstance(space_group_key, str):
        try: # This will work if it is the sg number already and it is a standard setting
            space_group_key = int(space_group_key)
            symops = dictio_space_groups[space_group_key]['symops']
        except:
            symops = dictio_space_groups[space_group_key]['symops']
    else:
        print("Space group key is not valid")
        sys.exit()
    return symops


def get_origins_from_sg_dictionary(space_group_key):
    """

    :param space_group_key:
    :type space_group_key:
    :return:
    :rtype:
    """
    # EXAMPLE: 'origins_list': [[0.0, 0.0, 0.0], [1/2.0, 1/2.0, 1/2.0]],'polar': False
    if isinstance(space_group_key, int):
        origins = dictio_space_groups[space_group_key]['origins_list']
        polar_bool = dictio_space_groups[space_group_key]['polar']
    elif isinstance(space_group_key, str):
        try: # This will work if it is the sg number already and it is a standard setting
            space_group_key = int(space_group_key)
            origins = dictio_space_groups[space_group_key]['origins_list']
            polar_bool = dictio_space_groups[space_group_key]['polar']
        except: # This is for non standard settings
            origins = dictio_space_groups[space_group_key]['origins_list']
            polar_bool = dictio_space_groups[space_group_key]['polar']
    else:
        print("Space group key is not valid")
        sys.exit()
    return polar_bool, origins


def get_latt_from_sg_dictionary(space_group_key):
    """

    :param space_group_key:
    :type space_group_key:
    :return:
    :rtype:
    """
    if isinstance(space_group_key, int):
        latt = dictio_space_groups[space_group_key]['latt']
    elif isinstance(space_group_key, str):
        space_group_key = int(space_group_key)
        latt = dictio_space_groups[space_group_key]['latt']
    else:
        print("Space group key is not valid")
        sys.exit()
    return latt


def get_space_group_number_from_symbol(space_group_string):
    """

    :param space_group_string:
    :type space_group_string: str
    :return: either space group number (for standard ones) or the symbol, but always the key for the dictionary
    :rtype: int or str
    """
    for _, key in enumerate(list(dictio_space_groups.keys())):
        search_string = ''.join(space_group_string.split())
        current_string = ''.join(dictio_space_groups[key]["symbol"].split())
        if search_string == current_string:
            print("\n Space group string given: ", space_group_string, "has been found in the dictionary", key)
            return key
    # Only if we didn't return any value
    print("Space group string was not found")
    return None


def get_files_from_ARCIMBOLDO_for_ALIXE(wd, clust_fold, fragment=1,hard_limit_phs=1000):
    """ Links the files from the 6_EXP_VAL folder of a given ens1_fragN folder in an ARCIMBOLDO_LITE run

    :param wd: the working directory, where the ARCIMBOLDO_LITE job was launched
    :type wd: str
    :param clust_fold: the folder where to put the links and do the clustering
    :type clust_fold: str
    :param fragment: to decide which ens1_fragN folder to use
    :type fragment: int
    :param hard_limit_phs: maximum number of phs files to retrieve
    :type hard_limit_phs: int
    :return:
    :rtype:
    """
    list_phs = []
    dict_sorted_input = {}
    list_chosen = []
    fragfolder='ens1_frag'+str(fragment)
    path_expval = os.path.join(wd, fragfolder+ '/6_EXPVAL_LIBRARY')
    path_sum = os.path.join(path_expval, 'solCC.sum')
    ccval, convnames = SELSLIB2.readCCValFromSUM(path_sum)
    if hard_limit_phs == 0:
        print('\n No hard limit set for the number of phs files to get, ' \
              'setting it to the total number of solutions')
        hard_limit_phs = len(ccval)
    for i in range(len(ccval)):
        if i != hard_limit_phs:
            fullpath = ccval[i]['corresp']
            name_file = (os.path.split(fullpath)[1])[:-4]
            list_chosen.append(name_file)
            rot_cluster = ccval[i]['cluster']
            if rot_cluster not in dict_sorted_input.keys():
                dict_sorted_input[rot_cluster] = []  # You create it first
                dict_sorted_input[rot_cluster].append(
                    os.path.join(clust_fold, name_file + ".phs"))  # And then save the solution
            else:
                dict_sorted_input[rot_cluster].append(os.path.join(clust_fold, name_file + ".phs"))
        else:
            break
    dirs1 = [d for d in os.listdir(path_expval) if os.path.isdir(os.path.join(path_expval, d))]
    for dir1 in dirs1:
        next_step = os.path.join(path_expval, dir1)
        for file in os.listdir(next_step):
            if file.endswith('.tar.gz') and (file[:-7] in list_chosen):
                tar_file = tarfile.open(os.path.join(next_step, file))
                tar_file.extractall(path=clust_fold)
                members = tar_file.getmembers()
                for member in members:
                    name_file = member.name[2:]
            elif file[-3:] == "pdb" and (file[:-4] in list_chosen):
                os.link(os.path.join(next_step, file), os.path.join(clust_fold, file[:-4] + '.pda'))
                list_phs.append(os.path.join(clust_fold, file[:-4] + ".phs"))

    if len(list_phs) <= 1:
        print("\nThere aren't enough files to cluster them within ALIXE")

    return dict_sorted_input


def get_files_from_9_EXP_BORGES(wd, clust_fold, cluster_id, mode=9, hard_limit_phs=10000):
    """ This function links the phs, lst and pdb (as pda) files from the 9*EXP in the clustering folder.

    :param wd:
    :type wd:
    :param clust_fold:
    :type clust_fold:
    :param cluster_id:
    :type cluster_id:
    :param mode: mode argument can be 9,9.5, or 9.6, corresponding to refined, rototranslated, and NMA analyzed solutions
    :type mode: str
    :param hard_limit_phs:
    :type hard_limit_phs:
    :return:
    :rtype:
    """
    folder_initcc = None
    list_chosen = []
    list_phs = []
    for folder in os.listdir(wd):
        if folder == "9.5_EXP" and mode == 9.5:
            mod = "rottra"
            folder_initcc = os.path.join(wd, folder)
        elif folder == "9_EXP" and mode == 9:
            mod = "rbr"
            folder_initcc = os.path.join(wd, folder)
        elif folder == "9.6_EXP" and mode == 9.6:
            mod = "nma"
            folder_initcc = os.path.join(wd, folder)
    cluster_folder = os.path.join(wd, folder_initcc, str(cluster_id))
    n_cluster = str(cluster_id)
    path_sum = os.path.join(cluster_folder, 'solCC.sum')
    ccval, convnames = SELSLIB2.readCCValFromSUM(path_sum)
    if hard_limit_phs == 0:
        print('No hard limit set, setting it to the total number of solutions, ',len(ccval))
        hard_limit_phs = len(ccval)
    for i in range(len(ccval)):
        if i <= hard_limit_phs:
            fullpath = ccval[i]['corresp']
            name_file = (os.path.split(fullpath)[1])[:-4]
            list_chosen.append(name_file)
            list_phs.append(os.path.join(clust_fold, name_file + "_" + mod + "_" + n_cluster + ".phs"))
        else:
            print('\n Hitting the hard limit for the number of phs files to consider, which is',hard_limit_phs)
            print('\n We will use ',i,' files out of ',len(ccval))
            break
    dirs = [d for d in os.listdir(cluster_folder) if
            os.path.isdir(os.path.join(cluster_folder, d))]  # Need to check how many subfolders are for that cluster
    for i in range(len(dirs)):
        next_step = os.path.join(wd, folder_initcc, n_cluster, str(i))  # 0, 1, etc cada uno 1000 sol
        for file in os.listdir(next_step):
            if file.endswith('.tar.gz') and (file[:-7] in list_chosen):
                tar_file = tarfile.open(os.path.join(next_step, file))
                tar_file.extractall(path=clust_fold)
                members = tar_file.getmembers()
                for member in members:
                    model_fullname = member.name  # Example case with not filtering solutions: frag136A_0_0-21.pdb
                    model_name = model_fullname[:-4]
                    if model_fullname[-4:] == ".phs":
                        os.rename(os.path.join(clust_fold, model_fullname),
                                  clust_fold + "/" + model_name + "_" + mod + "_" + n_cluster + ".phs")
                    if model_fullname[-4:] == ".lst":
                        os.rename(os.path.join(clust_fold, model_fullname),
                                  clust_fold + "/" + model_name + "_" + mod + "_" + n_cluster + ".lst")
            if file[-3:] == "pdb" and (file[:-4] in list_chosen):
                model_name = file[:-4]
                os.link(os.path.join(next_step, file),
                        clust_fold + "/" + model_name + "_" + mod + "_" + n_cluster + ".pda")
    return list_phs


def get_link_to_name_shelxe(name_shelxe, name_file_to_link, extension):
    """Links a file with a certain extension to a new one suitable for shelxe (name_shelxe) They should be on the same folder)"""
    try:
        size_extension = len(extension)
        os.link(name_file_to_link + "." + extension, name_shelxe[:-(size_extension + 1)] + "." + extension)
    except Exception:
        exctype, value = sys.exc_info()[:2]
        print("\n EXCEPTION IN GET LINK TO NAME SHELXE An error has occurred:\n" + str(exctype) + "\n" + str(value))


#@timing
def get_pdas_for_all_pdbs(path_name):
    pdb_files = list_files_by_extension(path_name,'.pdb',True)
    for fich in pdb_files:
        os.link(fich,fich[:-4]+'.pda')


def get_links_for_all(dirname, name_file_to_link, extension_link, extension):
    """Calls get_link_to_name_shelxe recursively to get the links to a certain file for all the pdas present in the directory"""
    list_files = list_files_by_extension(dirname, extension_link)
    for file in list_files:
        get_link_to_name_shelxe(os.path.join(dirname, file), os.path.join(dirname, name_file_to_link), extension)


def get_shelxe_line_from_html_output(name_job, wd):
    '''Shelxe line is to be read from the html called as the name_job given as argument.
    This is done because if the shelxe line is the default one it will not appear in the bor file'''
    name_html = name_job + ".html"
    path_html = os.path.join(wd, name_html)
    file_html = open(path_html, 'r')
    lines_html = file_html.readlines()
    regexline = re.compile('^shelxe_line')
    for i in range(len(lines_html)):
        if bool(regexline.findall(lines_html[i])):
            shelxe_line = ((lines_html[i].split("="))[1]).strip()
            break
    return shelxe_line

def get_topexp_from_html_output(name_job, wd):
    '''topexp is to be read from the html called as the name_job given as argument'''
    name_html = name_job + ".html"
    path_html = os.path.join(wd, name_html)
    file_html = open(path_html, 'r')
    lines_html = file_html.readlines()
    regexline = re.compile('^topexp')
    for i in range(len(lines_html)):
        if bool(regexline.findall(lines_html[i])):
            topexp = ((lines_html[i].split("="))[1]).strip()
            if (lines_html[i].split("="))[0].startswith('topexp_1'):
                return topexp
            elif (lines_html[i].split("="))[0].startswith('topexp_n'):
                pass
            elif (lines_html[i].split("="))[0].startswith('topexp'):
                return topexp
    return topexp


def generate_fake_ins_for_shelxe(path_ins, cell, sg_number):
    symm_cards = dictio_space_groups[sg_number]['symm_cards']
    file_ins = open(path_ins, 'w')
    file_ins.write('CELL  1.54178  %6.3f  %6.3f  %6.3f  %6.2f%  6.2f%  6.2f\n' % (
    cell[0], cell[1], cell[2], cell[3], cell[4], cell[5]))
    latt = dictio_space_groups[sg_number]['latt']
    file_ins.write('LATT -' + str(latt) + '\n')
    for card in symm_cards:
        file_ins.write(card)
    file_ins.write('SFAC  C  H  N  O\n')  # SHELXE will not use it so it can be the same
    file_ins.write('UNIT  576 1152 192 192\n')
    del file_ins


def generate_fake_pda_for_phstat(path_pda, cell, sg_number):
    # CRYST1   58.630   60.360  113.880  90.00  90.00  90.00 P 21 21 21
    symbol=dictio_space_groups[sg_number]["symbol"]
    file_pda= open(path_pda, 'w')
    file_pda.write(unitCellTools.writeCRYSTCARDintoPDB(cell[0], cell[1], cell[2], cell[3], cell[4], cell[5],sgsymbol=symbol,znum=1))
    del file_pda


def generate_input_lists_for_ALIXE_by_rotclu(dictio_fragments):
    dictio_input = {}
    list_rot_cluster = get_list_rotation_clusters_from_dictio_fragments(dictio_fragments)
    for rotclu in list_rot_cluster:
        dictio_input[rotclu] = []
        for frag in dictio_fragments.keys():
            if dictio_fragments[frag]['rot_cluster'] == rotclu:
                (dictio_input[rotclu]).append(frag + ".phs")
    return dictio_input


def generate_input_dictio_for_ALIXE_by_references(list_phs, list_references):
    dictio_ref = {}
    for phs in list_phs:
        if phs in list_references:
            dictio_ref[phs] = True
        else:
            dictio_ref[phs] = False
    return dictio_ref


def link_file(folder_for_link,path_orifile,name_link):
    """ Simple function to link a file

    :param folder_for_link: path for the linked file (only path, no name, that is name_link)
    :type folder_for_link: str
    :param path_orifile: full path to the file to be linked
    :type path_orifile: str
    :param name_link: basename for the linked file
    :type name_link: str
    :return:
    :rtype:
    """
    path_destination=os.path.join(folder_for_link, name_link)
    if not os.path.exists(path_destination):
        try:
            os.link(path_orifile, path_destination)
        except:
            print('Some error happened during linking')
            sys.exc_info()
            traceback.print_exc(file=sys.stdout)


def list_files_by_extension(path, extension,fullpath=True):
    """ Searches over all the files and in a directory, and if their extension is the one given, saves it

    :param path: path where to search for the files
    :param extension: extension searched for
    :param fullpath: boolean indicating whether to return the fullpath or the basename
    :return:
    """

    def listdir_fullpath(d):
        return [os.path.join(d, f) for f in os.listdir(d)]

    list_files = []
    wd = os.getcwd()
    for f in listdir_fullpath(os.path.join(wd, path)):
        if f.endswith(extension):
            if fullpath:
                list_files.append(os.path.abspath(f))
            else:
                list_files.append(os.path.basename(f))
    if len(list_files) >= 1:
        #print("\nI found "+str(len(list_files))+" "+extension+" files")
        return list_files
    else:
        #print("\nI didn't found any files with the extension ",extension)
        return None

def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def prepare_chescat_input_from_data(list_phase_sets, directory, name_chescat, path_sym):
    # NOTE: we are assuming the list is already sorted in the preferred way
    # 1) Write an ls file with the list of phs
    ref_phs = list_phase_sets[0]
    path_ls = os.path.join(directory, name_chescat+".ls")
    lsrotfile = open(path_ls, 'w')
    for i in range(len(list_phase_sets)):
        phs_namefile = (os.path.split(list_phase_sets[i]))[1]
        lsrotfile.write(phs_namefile + '\n')
    lsrotfile.close()
    # 2) Link the pda file
    link_file(directory, path_sym, name_chescat+".pda")


def process_list_dictio_results_to_global(list_dictio_results, dict_global_results, list_remove,
                                          name_chunk, clust_fold, keep_phi_key):
    """

    :param list_dictio_results:
    :param dict_global_results:
    :param list_remove:
    :param name_chunk:
    :param clust_fold:
    :return:
    """
    list_clustered = []
    for iclu, superclu in enumerate(list_dictio_results):
        dictio_result = superclu
        phs_in_cluster = len(dictio_result)
        # Obtain the name of the reference used
        if phs_in_cluster > 1:  # Then I need to rename the original phi file
            for fichi in dictio_result.keys():
                if dictio_result[fichi]['ref_no_cluster'] != 'cluster':
                    name_phi = fichi[:-4] + '_ref.phi'
                    key_phs_ori = fichi
            os.rename(os.path.join(clust_fold, name_chunk + '.phi'), os.path.join(clust_fold, name_phi))
            if keep_phi_key:
                name_key = name_phi
            else:
                name_key = key_phs_ori
        else:
            name_key = list(dictio_result.keys())[0]
        clustered = True if len(dictio_result.keys()) > 1 else False
        list_clustered.append(clustered)
        keys_global = dict_global_results.keys()
        if name_key in keys_global:  # Add this info
            if not clustered:
                dict_global_results[name_key].append((name_chunk, set(), dictio_result))
            else:
                dict_global_results[name_key].append((name_chunk, set(dictio_result.keys()), dictio_result))
        else:  # Create the key and add the info then
            if not clustered:
                dict_global_results[name_key] = []
                dict_global_results[name_key].append((name_chunk, set(), dictio_result))
            else:
                dict_global_results[name_key] = []
                dict_global_results[name_key].append((name_chunk, set(dictio_result.keys()), dictio_result))
        #list_remove.extend([os.path.join(clust_fold, ele) for ele in dictio_result.keys()])
        list_remove.extend([ele for ele in dictio_result.keys()])
    cluster_bool = False
    for ele in list_clustered:
        if ele == True:
            cluster_bool = True
    return dict_global_results, list_remove, cluster_bool


#@timing
def parallel_chescat_clustering(path_chescat, list_of_input_files, n_references, n_cores, min_size_list,
                                max_non_clust_events, clust_fold, resolution, tolerance, cycles, orisub, weight,
                                oricheck, cc_calc, path_sym):
    """

    :param path_chescat:
    :param list_of_input_files:
    :param n_references:
    :param n_cores:
    :param min_size_list:
    :param max_non_clust_events:
    :param clust_fold:
    :param resolution:
    :param tolerance:
    :param cycles:
    :param orisub:
    :param weight:
    :param oricheck:
    :param cc_calc:
    :param path_sym:
    :return:
    """
    # Function that given a list of input files and a number of cores, performs clustering in parallel
    # Assumes the solution files are already ordered in the list as desired
    print('\n*****************************************************************************************')
    print('\n The number of cores used in the parallel mode will be ', n_cores)
    print('\n*****************************************************************************************\n\n')

    # All this block is what I will need to iterate over and change every time a round is completed
    dict_global_results = {}
    iterations_performed = 0
    single_clust_count = 0  # to keep track of unsuccessful clustering events
    starting_input_size = len(list_of_input_files)
    list_non_processed_files = []
    while len(list_of_input_files) > 1 and iterations_performed <= n_references:
        iterations_performed = iterations_performed + 1
        total_files = len(list_of_input_files)
        if single_clust_count > max_non_clust_events:
            print('Single_clust_count is over the value set for the number of non clustering events, returning')
            break
        if (total_files - 1) <= min_size_list:
            print('There are less input files than the minchunk value, returning now')
            if iterations_performed == 1: # At the beginning, we need to redefine the list of non-processed files
                list_non_processed_files == list_of_input_files  # then it is the same as input
            break
        else:
            print('\n*****************************************************************************************')
            print('\n It remains to process ', total_files, ' phs files out of a total of ', starting_input_size)
            print('\n*****************************************************************************************\n\n')
        list_args = []
        jobs_to_check = []
        start_ref_name = os.path.basename(list_of_input_files[0])
        size_chunk_float = (total_files - 1) / float(n_cores)  # we do not count the common reference
        size_chunk = int(math.ceil(size_chunk_float))
        list_fish = list_of_input_files[1:]
        size_chunk = int(math.ceil((len(list_fish) / float(n_cores))))
        list_to_eval = [list_fish[i:i + size_chunk] for i in range(0, len(list_fish), size_chunk)]
        for ind, ele in enumerate(list_to_eval):
            size_ls = len(ele) + 1  # we need to take into account the reference
            path_ls = os.path.join(clust_fold, 'chunk_' + str(ind) + '.ls')
            lsrotfile = open(path_ls, 'w')
            lsrotfile.write(start_ref_name + '\n')
            for i in range(len(ele)):
                phs_namefile = (os.path.split(ele[i]))[1]
                lsrotfile.write(phs_namefile + '\n')
            lsrotfile.close()
            if not os.path.exists(os.path.join(clust_fold, 'chunk_' + str(ind) + ".pda")):
                shutil.copy(path_sym, os.path.join(clust_fold, 'chunk_' + str(ind) + ".pda"))
            list_args.append(('chunk_' + str(ind), clust_fold, path_chescat, resolution,
                              0, tolerance, cycles, orisub, weight, oricheck, cc_calc,
                              False))  # this False will make that the chescat job does not wait to be finished
            jobs_to_check.append((os.path.join(clust_fold, 'chunk_' + str(ind) + '.out'), size_ls))
        # Now run all the trials in parallel
        list_childs = []
        for argumlist in list_args:
            child = call_chescat_for_clustering_global(argumlist)
            list_childs.append(child)
        while 1:  # Loop until the processes have finished
            list_returns = [child.poll() for child in list_childs]
            none_list = [None for child in list_childs]
            if list_returns != none_list:
                print("\nNow all chescat jobs have finished")
                break

        # Now I am sure they have finished, I can evaluate them
        list_remove = []
        for output_path, size_ls in jobs_to_check:
            print('\nChecking ', output_path)
            name_chunk = os.path.basename(output_path)[:-4]
            if os.path.exists(output_path):
                # Check also that it is finished
                # checkYOURoutput(myfile, conditioEND, testEND, sleep_ifnot_ready=True, failure_test=None)
                SELSLIB2.checkYOURoutput(output_path, CHESCAT_OUT_END_CONDITION_LOCAL,
                                         CHESCAT_OUT_END_TEST, sleep_ifnot_ready=True,
                                         failure_test=CHESCAT_OUT_FAILURE_CONDITION_LOCAL)
                # Now process the output
                list_dictio_results = process_chescat_output_multiseed(path_output=output_path, cycles=cycles,
                                                                       size_ls=size_ls, seed=0)

                dict_global_results, list_remove, clubool = process_list_dictio_results_to_global(list_dictio_results,
                                                                                                  dict_global_results,
                                                                                                  list_remove,
                                                                                                  name_chunk,
                                                                                                  clust_fold,
                                                                                                  False)

                if clubool == False:
                    single_clust_count = single_clust_count + 1
                else:
                    single_clust_count = 0  # we reset it


        # Now remove the files already used and go back to iterate
        set1 = set([os.path.basename(ele) for ele in list_of_input_files])
        set2 = set(list_remove)
        new_input = list(set1 - set2)
        list_of_input_files = [os.path.join(clust_fold,e) for e in new_input]
        list_non_processed_files = copy.deepcopy(list_of_input_files)
        if len(list_non_processed_files) == 1:
            list_non_processed_files = []
            single_clust_count = single_clust_count + 1
            the_file = os.path.basename(list_of_input_files[0])
            faketuli = generate_fake_list_tuple_single_clust(the_file, n_cores)
            dict_global_results[the_file] = faketuli

    # If we broke we will be here
    # Do some cleaning now
    list_files_to_delete = [ fichi for fichi in os.listdir(clust_fold) if fichi.startswith('chunk')]
    for fichi in list_files_to_delete:
        try:
            os.remove(fichi)
        except:
            pass
    del list_files_to_delete
    return list_non_processed_files, dict_global_results, single_clust_count


def generate_fake_list_tuple_single_clust(name_file,n_chunks):
    # ('chunk_2', set([]), {'frag61_0_0_rbr_0.phs': {'wMPE_last': 0.0, 'diff_wMPE_first': 90.0,
    # 'wMPE_first': 0.0, 'mapcc_first': 100.0, 'shift_first': [0.0, 0.0, 0.0], 'shift_last': [0.0, 0.0, 0.0],
    # 'diff_wMPE_last': 90.0, 'mapcc_last': 100.0}})
    faketuli = []
    for n in range(n_chunks):
        name_chunk='chunk_'+str(n)
        faketuli.append((name_chunk,set([]),{name_file: {'wMPE_last': 0.0, 'diff_wMPE_first': 90.0,
                                                                      'wMPE_first': 0.0, 'mapcc_first': 100.0,
                                                                      'shift_first': [0.0, 0.0, 0.0],
                                                                      'shift_last': [0.0, 0.0, 0.0],
                                                                      'diff_wMPE_last': 90.0, 'mapcc_last': 100.0}}))

    return faketuli


def process_chescat_output_multiseed(path_output, cycles, size_ls, seed):
    """

    :param path_output:
    :param cycles:
    :param size_ls:
    :param seed:
    :return:
    """
    name_chunk = os.path.basename(path_output)[:-4]
    root_path_out = os.path.split(path_output)[0]
    output_file = open(path_output, 'r')
    output_content = output_file.read()
    output_content = output_content.decode("utf-8") if isinstance(output_content,bytes) else output_content
    dictio_result, total_runtime, seed_tested = read_chescat_output(output_content, cycles, size_ls)
    if seed_tested:
        list_dictio_results = split_alixe_clusters(dictio_result)
        name_superphi = name_chunk + "_" + str(len(list_dictio_results)) + ".phi"
    else:
        if seed == 1:
            list_dictio_results = [dictio_result]
            name_superphi = name_chunk + "_1.phi"
        elif seed == 0:
            list_dictio_results = [dictio_result]
            name_superphi = name_chunk + "_0.phi"
    path_superphi = os.path.join(root_path_out, name_superphi)
    #  Move the file to change its name and make it consistent with the convention
    os.rename(path_superphi, os.path.join(root_path_out, name_chunk + '.phi'))
    return list_dictio_results


# Next function uses shelxe to generate a map file (.phs) using the arguments given as command line.
# It needs the argument line and the name for the file that shelxe will read
# Can work for pda and for phis
# It can be called either waiting or not for the output, to be able to use it in parallel
def phase_fragment_with_shelxe(args):
    """Uses shelxe to obtain the .phs file with the phases of the fragments"""
    linea_arg, name_shelxe, wd, shelxe_path, extt, wait = args
    command_line = []
    command_line.append(shelxe_path)
    command_line.append(name_shelxe+'.'+extt)
    arguments = linea_arg.split()
    for i in range(len(arguments)):
        command_line.append(arguments[i])
    print("\nCommand line for this call", ' '.join(command_line))
    try:
        if wait:
            p = subprocess.Popen(command_line, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 cwd=wd)
            complete_output, errors = p.communicate()
            return complete_output, errors
        else:
            p = subprocess.Popen(command_line, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 cwd=wd)
            return p
    except Exception:
        exctype, value = sys.exc_info()[:2]
        print("\n An error has occurred:\n" + str(exctype) + "\n" + str(value))


def phase_all_in_folder_with_SHELXE(linea_arg, dirname, shelxe_path, n_cores, check_if_solved, subset=[]):
    """

    :param linea_arg:
    :param dirname:
    :param shelxe_path:
    :param n_cores:
    :return:
    """

    # Check if this is a call for expansions
    number_cycles = 0
    for ele in linea_arg.split():
        if ele.startswith('-a'):
            number_cycles = int(ele[2:])
    if number_cycles>0:
        new_linea_arg = ''
        for ele in linea_arg.split():
            if ele.startswith('-a'):
                new_linea_arg=new_linea_arg+' -a1'
            else:
                new_linea_arg = new_linea_arg + ' '+ ele

    if number_cycles == 0:
        list_args = []
        for f in os.listdir(dirname):
            if f[-3:] not in ["pda","phi"]:
                continue
            if os.path.isfile(os.path.join(dirname, f)):
                if subset == []:
                    name_shelxe = f[:-4]
                    list_args.append((linea_arg, name_shelxe, dirname, shelxe_path, f[-3:], True))
                else:
                    if f not in subset:
                        continue
                    else:
                        name_shelxe = f[:-4]
                        list_args.append((linea_arg, name_shelxe, dirname, shelxe_path, f[-3:], True))
        # Prepare the input for running in parallel
        pool = Pool(int(n_cores))
        # execute a computation(s) in parallel
        pool.map(phase_fragment_with_shelxe, list_args)
        # turn off your parallel workers at the end of your script
        pool.close()
    else:
        list_tuple_bests = []
        for cycle in range(number_cycles):
            print('\n Expansions cycle ',cycle)
            # NOTE CM: maybe in the future we can do it in separate folders
            # dir_cycle = os.path.join(dirname,cycle)
            # check_dir_or_make_it(dir_cycle, remove=True)
            list_args = []
            for f in os.listdir(dirname):
                if cycle == 0:
                    if f[-3:]!="phi":
                        continue
                else:
                    if f[-3:]!="pda":
                        continue
                if os.path.isfile(os.path.join(dirname, f)):
                    name_shelxe = f[:-4]
                    list_args.append((new_linea_arg, name_shelxe, dirname, shelxe_path, f[-3:], True))
            # Prepare the input for running in parallel
            pool = Pool(int(n_cores))
            # execute a computation(s) in parallel
            pool.map(phase_fragment_with_shelxe, list_args)
            # turn off your parallel workers at the end of your script
            pool.close()
            # Check if any of them has solved
            if check_if_solved:
                for f in os.listdir(dirname):
                    if f[-3:] != 'lst':
                        continue
                    else:
                        fichioutput = open(os.path.join(dirname, f), 'r')
                        complete_output = fichioutput.read()
                        del fichioutput
                        CCfin = extract_best_CC_shelxe(complete_output)
                        print('\n ',f,' has a CC after autotracing of ',CCfin)
                        if CCfin > 30:
                            print('\n Achieved a CC of ',CCfin,'%')
                            print('\n The structure was possibly solved, check ',f)
                            return (True,f,CCfin)
                        else:
                            list_tuple_bests.append((f,CCfin,cycle))
            # If we have not returned, we need to go for the following cycle
            # Then we should rename the pdbs as the new pdas before restarting the process
            list_traces = list_files_by_extension(dirname, 'pdb', fullpath=True)
            for pdb_trace in list_traces:
                print("\nMoving ",pdb_trace,' to ',pdb_trace[:-4]+'.pda')
                shutil.move(pdb_trace, pdb_trace[:-4]+'.pda')


def generate_minimal_ali_confdict_from_mode_and_input(alixe_mode,input_info,path_chescat,hkl_filepath, path_sym):
    # Read the defaults from alixe_library
    ConfigAli = configparser.ConfigParser()
    ConfigAli.read_file(io.StringIO(defaults_alixe))
    ali_config_dict = {s: dict(ConfigAli.items(s)) for s in ConfigAli.sections()}
    ali_confdict = ali_config_dict['ALIXE']
    for keyali in ali_confdict.keys():
        try:
            if keyali in ['cycles','seed','fragment']: # these must be integers
                ali_confdict[keyali] = int(ali_confdict[keyali])
            else:
                ali_confdict[keyali] = float(ali_confdict[keyali])
        except:
            # traceback.print_exc()
            # Check if boolean
            if ali_confdict[keyali] in ['True', 'TRUE', 'true']:
                ali_confdict[keyali] = True
            if ali_confdict[keyali] in ['False', 'FALSE', 'false']:
                ali_confdict[keyali] = False
            # Otherwhise we leave them as strings
    # Assign the input values
    ali_confdict['alixe_mode']= alixe_mode
    ali_confdict['input_info_1'] = input_info
    ali_confdict['path_chescat'] = path_chescat
    ali_confdict['n_pools'] = 1
    ali_confdict['hkl_file'] = os.path.abspath(hkl_filepath)
    ali_confdict['path_sym'] = path_sym
    # NOTE CM: I AM NOT SURE THIS IS A GOOD IDEA. I THINK IT SHOULD BE BETTER TROUGH CONFIGURATION
    # or at least have defaults related to resolution
    ali_confdict['shelxe_line_alixe'] = '-m5 -a0'
    # not sure whether to just deactivate expansions in this case...
    #ali_confdict['shelxe_line_expansion'] = '-a8'
    ali_confdict['expansions'] = False
    ali_confdict['shelxe_path'] = 'shelxe'
    return ali_confdict



def read_confibor_alixe(path_alibor):
    # Read the defaults from alixe_library
    ConfigAli = configparser.ConfigParser()
    ConfigAli.read_file(io.StringIO(defaults_alixe))
    count_inputs = 0
    if os.path.exists(path_alibor):
        ConfigAli.read(path_alibor)
        ali_config_dict = {s:dict(ConfigAli.items(s)) for s in ConfigAli.sections()}
        ali_confdict = ali_config_dict['ALIXE']
        del ali_config_dict
        for keyali in ali_confdict.keys():
            try:
                ali_confdict[keyali] = float(ali_confdict[keyali])
            except:
                #traceback.print_exc()
                # Check if boolean
                if ali_confdict[keyali] in ['True','TRUE','true']:
                    ali_confdict[keyali] = True
                if ali_confdict[keyali] in ['False','FALSE','false']:
                    ali_confdict[keyali] = False
                else: # Otherwhise leave it as a string
                    if keyali.startswith('input_info'):
                        count_inputs = count_inputs+1
                    if keyali.endswith('file') or keyali=='path_sym':
                        ali_confdict[keyali] = os.path.abspath(ali_confdict[keyali])
        # Before returning also set keyword with number of input folders/bors
        ali_confdict['n_pools'] = count_inputs
        # NOTE CM: some variables must be an integer, otherwise they will produce an error
        ali_confdict['cycles']=int(ali_confdict['cycles'])
        ali_confdict['seed'] = int(ali_confdict['seed'])
        ali_confdict['fragment'] = int(ali_confdict['fragment'])

        return ali_confdict
    else:
        print('Please provide a path to an existing configuration file for ALIXE')
        sys.exit()


def generate_sym_data(path_sym, ali_confdict, sub_clust_path):
    file_sym = open(path_sym, 'r')
    cryst_card = extract_cryst_card_pdb(file_sym.read())
    ali_confdict['cryst_card'] = cryst_card
    cell, sg_symbol = read_cell_and_sg_from_pdb(path_sym)  # Cell is a list of floats
    sg_number = get_space_group_number_from_symbol(sg_symbol)
    polar, origins = get_origins_from_sg_dictionary(sg_number)
    path_ins = os.path.join(sub_clust_path, 'symmetry.ins')
    generate_fake_ins_for_shelxe(path_ins, cell, sg_number)
    ali_confdict['ins_file'] = path_ins
    return ali_confdict


def read_cell_from_ins(path_ins):
    """
    Reads the unit cell parameters from a shelxe instruction file

    Keyword arguments:
    path_ins -- path to the shelxe ins file

    Returns:
    float_cell -- list with six floats, a, b, c, alpha, beta, gamma
    wavelength -- float, not always present in ins file so not always returned
    """
    wavelength = None
    file_ins = open(path_ins, 'r')
    lines_ins = file_ins.readlines()
    for line in lines_ins:
        if line.startswith("CELL"):
            items = line.split()
            if len(items) == 8:  # If there are seven items, the first is assumed to be the wavelength
                wavelength = float(items[1])
                cell = [items[2], items[3], items[4], items[5], items[6], items[7]]
                float_cell = [float(i) for i in cell]
            elif len(items) == 7:
                cell = [items[1], items[2], items[3], items[4], items[5], items[6]]
                float_cell = [float(i) for i in cell]
            break
    return float_cell, wavelength


def read_cell_and_sg_from_pdb(path_pdb):
    """


    Keyword arguments:
    path_pdb --


    Returns:

    """
    pdb_file = open(path_pdb, 'r')
    pdb_content = pdb_file.read()
    del pdb_file
    pdb_lines = pdb_content.split("\n")
    for linea in pdb_lines:
        if linea.startswith("CRYST1"):
            cryst_card = linea
            space_group = (cryst_card[55:67]).strip()  # SG in characters 56 - 66
            list_values = cryst_card.split()  # Cell elements
            cell = [list_values[1], list_values[2], list_values[3], list_values[4], list_values[5], list_values[6]]
            float_cell = [float(i) for i in cell]
            return float_cell, space_group


def read_chescat_output(complete_output, cycles, n_files):
    """ Reads and returns the information from both the first and the last cycle of a CHESCAT run

    :param complete_output: string that contains the complete CHESCAT output
    :type complete_output: str
    :param cycles: number of cycles CHESCAT run
    :type cycles: int
    :param n_files: number of input files CHESCAT run
    :type n_files: int
    :return: dictionary with the results and float with total running time
    :rtype:
    """

    regex_start = re.compile('Cluster analysis cycle\s*1(?![0-9])')
    regex_end = re.compile('Cluster analysis cycle\s*%s' % (str(cycles)))
    regex_time = re.compile('Total time')
    regex_files = re.compile('phase files found in')
    lines_output = complete_output.split("\n")
    any_cluster = True
    total_time = None

    # NOTE CM: for the multiseed, we need to find how many instances of the cycle 1 are
    ncycle_one = len(re.findall(regex_start, complete_output))
    ncycle_three = len(re.findall(regex_end, complete_output))
    arg_seed = (re.findall(r"(^.*?%s.*?$)" % 'clusterphases -s', complete_output, re.MULTILINE))[0].split()
    seed_tested = True if int(arg_seed[-1][-1])==1 else False
    if ncycle_one == n_files-1 and ncycle_three == 0:
        any_cluster = False
        not_clustered_refs = ncycle_one + 1
    else:
        any_cluster = True
        if ncycle_one>1:
            not_clustered_refs = ncycle_one - 1
        else: # Then there was a cluster with the first reference
            not_clustered_refs=0
    count_no_clu=0


    dictio_result = {}
    sorted_input_files = []

    for i in range(len(lines_output)):

        # Reading how many phs were read by chescat
        if bool(regex_files.findall(lines_output[i])):
            for pepi in range(i+2,i+n_files+2,1):
                sorted_input_files.append(lines_output[pepi].strip())
            assert len(sorted_input_files) == n_files

        if bool(regex_time.findall(lines_output[i])):
            total_time=float(lines_output[i].split()[0])

        if bool(regex_start.findall((lines_output[i - 3]).strip())):
            if lines_output[i + 1] == "":
                no_cluster = True
                list_elements = lines_output[i].split()
                count_no_clu=count_no_clu+1
                if len(list_elements) == 9:
                    namefile = list_elements[8]
                    shiftx = float(list_elements[5])
                    shifty = float(list_elements[6])
                    shiftz = float(list_elements[7])
                    shift = [shiftx, shifty, shiftz]
                    mapcc = float(list_elements[4])
                    if list_elements[2]!='********':
                        wmpd = float(list_elements[2])
                        diff_wmpd = float(list_elements[3])
                        dictio_result[namefile] = {"wMPE_first": wmpd,
                                                           "shift_first": shift,'mapcc_first':mapcc,
                                                           'diff_wMPE_first': diff_wmpd,
                                                           "wMPE_last": wmpd,
                                                           "shift_last": shift,'mapcc_last':mapcc,
                                                           'diff_wMPE_last': diff_wmpd}
                    else:
                        dictio_result[namefile] = {"wMPE_first": -1.0,
                                                            "shift_first": shift,
                                                            'mapcc_first': mapcc,
                                                            'diff_wMPE_first': -1.0,
                                                            "wMPE_last": -1.0,
                                                            "shift_last": shift,
                                                            'mapcc_last': mapcc,
                                                            'diff_wMPE_last': -1.0}
                # NOTE CM: only if this is not the last cycle 1 we have, save that this was a not clustered reference
                if count_no_clu <= not_clustered_refs:
                    dictio_result[namefile]['ref_no_cluster']=True

            elif lines_output[i + 1] != "":
                # something has clustered and I need to save this information from first cycle somehow
                no_cluster = False
                for k in range(0,n_files):
                    line_MPE_to_ref = lines_output[i + k]
                    list_elements = line_MPE_to_ref.split()
                    if len(list_elements) == 9:
                        namefile = list_elements[8]
                        shiftx = float(list_elements[5])
                        shifty = float(list_elements[6])
                        shiftz = float(list_elements[7])
                        shift = [shiftx, shifty, shiftz]
                        mapcc = float(list_elements[4])
                        if list_elements[2] != '********':
                            wmpd = float(list_elements[2])
                            diff_wmpd = float(list_elements[3])
                            dictio_result[namefile] = {"wMPE_first": wmpd, "shift_first": shift,
                                                               'mapcc_first': mapcc, 'diff_wMPE_first':diff_wmpd}
                        else:
                            dictio_result[namefile] = {"wMPE_first": -1.0, "shift_first": shift,
                                                               'mapcc_first': mapcc, 'diff_wMPE_first': -1.0}
                        if wmpd == 0.0:
                            dictio_result[namefile]['ref_no_cluster'] = False
                        else:
                            dictio_result[namefile]['ref_no_cluster'] = 'cluster'
                    if line_MPE_to_ref == "":
                        break

        if bool(regex_end.findall((lines_output[i - 3]).strip())):
            for l in range(0, n_files):
                line_MPE_to_ref = lines_output[i + l]
                list_elements = line_MPE_to_ref.split()
                if len(list_elements) == 9:
                    namefile=list_elements[8]
                    shiftx = float(list_elements[5])
                    shifty = float(list_elements[6])
                    shiftz = float(list_elements[7])
                    shift = [shiftx, shifty, shiftz]
                    mapcc = float(list_elements[4])
                    if list_elements[2] != '********':
                        if list_elements[8] in dictio_result:
                            wmpd = float(list_elements[2])
                            diff_wmpd = float(list_elements[3])
                            dictio_result[namefile]["wMPE_last"]=wmpd
                            dictio_result[namefile]["diff_wMPE_last"] = diff_wmpd
                            dictio_result[namefile]["shift_last"]=shift
                            dictio_result[namefile]['mapcc_last']=mapcc
                        else:
                            #print 'There are more files in the last cycle than in the first, handling now'
                            dictio_result[namefile]={"wMPE_first":-1.0,"shift_first":[-1.0,-1.0,-1.0],
                                                     'mapcc_first':-1.0,'diff_wMPE_first': -1.0,
                                                     "wMPE_last":wmpd,"shift_last":shift,
                                                     'mapcc_last':mapcc,"diff_wMPE_last":diff_wmpd}
                    else:
                        if namefile in dictio_result:
                            dictio_result[namefile]["wMPE_last"]=-1.0
                            dictio_result[namefile]["shift_last"]=shift
                            dictio_result[namefile]['mapcc_last']=mapcc
                        else:
                            #print 'There are more files in the last cycle than in the first, handling now'
                            wmpd = float(list_elements[2])
                            diff_wmpd = float(list_elements[3])
                            dictio_result[namefile]={"wMPE_first":-1.0,"shift_first":[-1.0,-1.0,-1.0],
                                                     'mapcc_first':-1.0,'diff_wMPE_first': -1.0,
                                                     'wMPE_last':wmpd,"shift_last":shift,
                                                     'mapcc_last':mapcc,"diff_wMPE_last":diff_wmpd}

                    if 'ref_no_cluster' not in dictio_result[namefile].keys():
                        dictio_result[namefile]['ref_no_cluster']='cluster'
                if line_MPE_to_ref == "":
                    break

    for j in range(i,len(lines_output)):
        if bool(regex_time.findall(lines_output[j])):
            total_time=float(lines_output[j].split()[0])

    for key in dictio_result.keys():
        if 'wMPE_last' not in dictio_result[key]:
            dictio_result[key]["wMPE_last"] = -1.0
            dictio_result[key]["shift_last"] = [-1.0, -1.0, -1.0]
            dictio_result[key]["mapcc_last"] = -1.0
            dictio_result[key]['diff_wMPE_last']= -1.0

    if not any_cluster:
        for fichi in sorted_input_files:
            if fichi not in dictio_result.keys():
                dictio_result[fichi]={'wMPE_last': 0.0, 'diff_wMPE_first': 0.0,
                                                       'ref_no_cluster': True, 'wMPE_first': 0.0,
                                                       'mapcc_first': -1.0, 'shift_first': [0.0, 0.0, 0.0],
                                                       'shift_last': [0.0, 0.0, 0.0], 'diff_wMPE_last': 0.0,
                                                       'mapcc_last': -1.0}
    return dictio_result,total_time,seed_tested


def rename_models_simple(name_model, list_models):
    f = open("traceback_names_solutions", 'w')
    del f
    for i in range(len(list_models)):
        os.rename(list_models[i] + ".pda", "m_" + name_model + "_sol_" + str(i) + ".pda")
        os.rename(list_models[i] + ".lst", "m_" + name_model + "_sol_" + str(i) + ".lst")
        os.rename(list_models[i] + ".phs", "m_" + name_model + "_sol_" + str(i) + ".phs")
        f = open("traceback_names_solutions", 'a')
        f.write(list_models[i] + " ------> m" + name_model + "sol" + str(i) + "\n")
        del f


def removeKeyDict(d, key):
    r = dict(d)
    del r[key]
    return r


def sort_list_phs_rotclu_by_FOM(list_phs_full, fom_sorting, dictio_fragments, keypool):
    """

    :param list_phs_full:
    :param fom_sorting:
    :param dictio_fragments:
    :param keypool:
    :return:
    """
    # Sort the phase sets according to established FOM
    # VERSION 1, ITERATION
    #list_tuple_sort = []
    # for phs in list_phs_full:
    #     phs_key = phs[:-4]
    #     list_tuple_sort.append((phs, dictio_fragments[keypool][phs_key]['zscore'],
    #                             dictio_fragments[keypool][phs_key]['llg'],
    #                             dictio_fragments[keypool][phs_key]['initcc']))

    # VERSION 2, LIST COMPREHENSION
    list_tuple_sort = [ (phs,
                         dictio_fragments[keypool][phs[:-4]]['zscore'],
                         dictio_fragments[keypool][phs[:-4]]['llg'],
                         dictio_fragments[keypool][phs[:-4]]['initcc'])
                        for _,phs in enumerate(list_phs_full) ]
    if fom_sorting == 'CC':
        list_tuple_sort.sort(key=lambda x: x[3], reverse=True)
    elif fom_sorting == 'LLG':
        list_tuple_sort.sort(key=lambda x: x[2], reverse=True)
    elif fom_sorting == 'ZSCORE':
        list_tuple_sort.sort(key=lambda x: x[1], reverse=True)
    # New: a combined one with LLG, ZSCORE, CC
    elif fom_sorting == 'COMBINED':
       list_tuple_sort.sort(key=operator.itemgetter(2, 0, 1),reverse=True)
    list_phs_rotclu = [list_tuple_sort[i][0] for i in range(len(list_tuple_sort))]
    return list_phs_rotclu

#@timing
def sort_ls_file_by_CC(name_ls):
    """ This function reorders a given .ls file according to the CC of the phase files it contains. For that, it need to have on the same directory the .lst files output from
    SHELXE when obtaining the phases. It will overwrite the previous file """
    # Leer el ls para ver cuantos .phs hay
    fichero_ls = open(name_ls, "r")
    lineas_fichero_ls = fichero_ls.readlines()
    del fichero_ls
    numero_phs = len(lineas_fichero_ls)
    dictio_CC = {}
    for j in range(numero_phs):
        name_file = (lineas_fichero_ls[j].split())[0]
        # Guardar el dato del CC con su nombre de fichero en un diccionario declarado fuera del bucle
        # Leer correspondiente fichero lst y tomar el CC
        # TODO: Check all lst files are there and if not, print an error message and exit
        lst = open(name_file[:-4] + ".lst", 'r')
        lineas_lst = lst.readlines()
        for k in range(len(lineas_lst)):
            if lineas_lst[k].startswith(" Overall CC between native Eobs and Ecalc (from fragment) = "):
                CC = float(((lineas_lst[k].split())[10])[:-1])
                dictio_CC[name_file] = CC
                break
    # Obtener una lista ordenada con los ficheros y sus CC
    sorted_dict_CC = sorted(list(dictio_CC.items()), key=operator.itemgetter(1), reverse=True)
    # Escribir un nuevo ls
    ls = open(name_ls, "w")
    del ls
    for index in range(len(sorted_dict_CC)):
        ls = open(name_ls, "a")
        ls.write(sorted_dict_CC[index][0] + "\n")
        del ls

#@timing
def sort_reflections_phs(array_refle):
    '''Sorts an array of reflections in ascending order of first h, then k, and then l'''
    array_refle.sort(key=operator.itemgetter(2, 1, 0))
    return array_refle

#@timing
def sort_reflections_phs_numpy(array_refle):
    '''Sorts an array of reflections in ascending order of first h, then k, and then l'''
    #array_refle.sort(key=operator.itemgetter(2, 1, 0))
    array_refle = array_refle[array_refle[:, 2].argsort()]  # First sort doesn't need to be stable.
    array_refle = array_refle[array_refle[:, 1].argsort(kind='mergesort')]
    array_refle = array_refle[array_refle[:, 0].argsort(kind='mergesort')]
    return array_refle



# TODO: test that it actually works and applies the shift as expected (for example, test in coot)
# TODO: do it using the BioPython.PDB to work with the files
# TODO: either change this function or create a new one in which instead of converting twice, what you do
# is changing the vector for the shift from crystalline to orthogonal, and apply it directly to the pdb
# ATOM_FORMAT_STRING="%s%6i %-4s%c%3s %c%4i%c   %8.3f%8.3f%8.3f%6.2f%6.2f      %4s%2s%2s\n"
# parser=PDBParser()
# structure=parser.get_structure(pdb_model[:-4],pdb_model)
def shifting_coordinates(shift, pdbfile):
    """Applies a shift to the x,y,z coordinates of a given pdb.
    IT NEEDS TO HAVE THE CRYST CARD
    IT IS USED FOR PHSTAT SHIFTS"""
    # We need the CRYST card
    print("Reading ", pdbfile[:-4] + ".pda", " in order to apply a shift")
    pda = open(pdbfile[:-4] + ".pda")
    lineaspda = pda.readlines()
    pda.close()
    cell_dim = [0, 0, 0, 0, 0, 0]
    parameters = {}
    for i in range(len(lineaspda)):
        if lineaspda[i].startswith("CRYST1"):
            cryst_card = lineaspda[i]
            cell_dim[0] = float((lineaspda[i].split())[1])
            cell_dim[1] = float((lineaspda[i].split())[2])
            cell_dim[2] = float((lineaspda[i].split())[3])
            cell_dim[3] = float((lineaspda[i].split())[4])
            cell_dim[4] = float((lineaspda[i].split())[5])
            cell_dim[5] = float((lineaspda[i].split())[6])
    parser = PDBParser()
    structure = parser.get_structure(pdbfile[:-4], pdbfile)
    list_all_atoms = Selection.unfold_entities(structure, 'A')  # lista con todos los átomos de ese pdb
    for atom in list_all_atoms:
        ##        print "Before:",atom.get_coord()
        coord_before = atom.get_coord()
        x = coord_before[0]
        y = coord_before[1]
        z = coord_before[2]
        x, y, z, parameters = SELSLIB2.convertFromOrthToFrac(x, y, z, cell_dim, parameters)
        crist_coord = [x, y, z]
        new_coord = [0, 0, 0]
        # Luego aplicamos el shift
        new_coord[0] = crist_coord[0] + float(shift[0])
        new_coord[1] = crist_coord[1] + float(shift[1])
        new_coord[2] = crist_coord[2] + float(shift[2])
        # Reconvertimos a ortogonales para escribirlas
        ort_x, ort_y, ort_z, parameters = SELSLIB2.convertFromFracToOrth(new_coord[0], new_coord[1], new_coord[2], cell_dim,
                                                                parameters)
        atom.set_coord([ort_x, ort_y, ort_z])
    ##        print "After: ",atom.get_coord()
    io = PDBIO()
    io.set_structure(structure)
    io.save(pdbfile[:-4] + "_shifted.pda")
    pdb_file = open(pdbfile[:-4] + "_shifted.pda", "r")
    pdb_lines = pdb_file.readlines()
    del pdb_file
    pdb_file = open(pdbfile[:-4] + "_shifted.pda", "w")
    pdb_file.write(cryst_card + "\n")
    for i in range(len(pdb_lines)):
        pdb_file.write(pdb_lines[i])
    del pdb_file


def shifting_coordinates_inverse(shift, pdbfile, outputfile=""):
    """Applies the inverse shift to one given to all the x,y,z coordinates of a given pdb.
    IT NEEDS TO HAVE THE CRYST CARD
    IT IS USED FOR SHELXE SHIFTS"""
    # We need the CRYST card
    print("Reading ", pdbfile[:-4] + ".pda", " in order to apply a shift")
    # NOTE: Here I changed the following line for using the original extension of the pdbfile
    # pda=open(pdbfile[:-4]+".pda")
    pda = open(pdbfile, "r")

    lineaspda = pda.readlines()
    pda.close()
    cell_dim = [0, 0, 0, 0, 0, 0]
    parameters = {}
    for i in range(len(lineaspda)):
        if lineaspda[i].startswith("CRYST1"):
            cryst_card = lineaspda[i]
            cell_dim[0] = float((lineaspda[i].split())[1])
            cell_dim[1] = float((lineaspda[i].split())[2])
            cell_dim[2] = float((lineaspda[i].split())[3])
            cell_dim[3] = float((lineaspda[i].split())[4])
            cell_dim[4] = float((lineaspda[i].split())[5])
            cell_dim[5] = float((lineaspda[i].split())[6])
    parser = PDBParser()
    structure = parser.get_structure(pdbfile[:-4], pdbfile)
    list_all_atoms = Selection.unfold_entities(structure, 'A')  # lista con todos los átomos de ese pdb
    for atom in list_all_atoms:
        ##        print "Before:",atom.get_coord()
        coord_before = atom.get_coord()
        x = coord_before[0]
        y = coord_before[1]
        z = coord_before[2]
        x, y, z, parameters = SELSLIB2.convertFromOrthToFrac(x, y, z, cell_dim, parameters)
        crist_coord = [x, y, z]
        new_coord = [0, 0, 0]
        ##        print "crist_coord before",crist_coord
        # Luego aplicamos el shift, pero restando en vez de sumando
        new_coord[0] = crist_coord[0] - float(shift[0])
        new_coord[1] = crist_coord[1] - float(shift[1])
        new_coord[2] = crist_coord[2] - float(shift[2])
        # Reconvertimos a ortogonales para escribirlas
        ##        print "shift",shift
        ##        print "crist_coord after",new_coord
        ort_x, ort_y, ort_z, parameters = SELSLIB2.convertFromFracToOrth(new_coord[0], new_coord[1], new_coord[2], cell_dim,
                                                                parameters)
        atom.set_coord([ort_x, ort_y, ort_z])
    ##        print "After: ",atom.get_coord()
    io = PDBIO()
    io.set_structure(structure)
    if outputfile == "":
        outputfile = pdbfile[:-4] + "_shifted.pda"
    io.save(outputfile)
    pdb_file = open(outputfile, "r")
    pdb_lines = pdb_file.readlines()
    del pdb_file
    pdb_file = open(outputfile, "w")
    pdb_file.write(cryst_card + "\n")
    for i in range(len(pdb_lines)):
        pdb_file.write(pdb_lines[i])
    del pdb_file
    return outputfile

#@timing
def trimByContinuityLimit(pdb_file, min_size):
    """

    :param pdb_file:
    :type pdb_file:
    :param min_size:
    :type min_size:
    :return:
    :rtype:
    """
    parser = PDBParser()
    structure = parser.get_structure(pdb_file[:-4], pdb_file)
    residues = Selection.unfold_entities(structure, 'R')
    list_id = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    dictio_chainid = {}
    residues_to_remove = []
    current_listres = []
    index = 0
    for i in range(len(residues) - 1):
        res1 = residues[i]
        res2 = residues[i + 1]
        id1 = res1.id
        id2 = res2.id
        # print 'id1',id1
        check = Bioinformatics.checkContinuity(res1, res2)
        # print 'check',check
        # print 'list_id[index]',list_id[index]
        if check == True:
            # print "These two residues are consecutive",res1,res2
            if id1 not in current_listres:
                current_listres.append(id1)
            dictio_chainid[id1] = list_id[index]
            if id2 not in current_listres:
                current_listres.append(id2)
            dictio_chainid[id2] = list_id[index]
            # print 'list_id[index]',list_id[index]
            # print 'id1,dictio_chainid[id1]',dictio_chainid[id1],id1
            # print 'id2,dictio_chainid[id2]',dictio_chainid[id2],id2
        elif check == False:
            # print "current_listres beginning check",current_listres
            # print "These two residues are not consecutive",id1,id2
            if id1 not in current_listres:
                current_listres.append(id1)
                dictio_chainid[id1] = list_id[index]
            if len(current_listres) < min_size:
                # print "      The removal condition is fullfilled"
                # print "      residues_to_remove before",residues_to_remove
                residues_to_remove.extend(copy.deepcopy(current_listres))
                # print "      residues_to_remove after",residues_to_remove
            if i == len(
                    residues) - 2 and min_size > 1:  # If we reach this point, then the last residue is not continuos so it is single
                residues_to_remove.append(id2)
            else:
                current_listres = []
                current_listres.append(id2)
                index = index + 1
                dictio_chainid[id2] = list_id[index]
    # Remove the residues and write the pdb
    for model in list(structure):
        for chain in list(model):
            for residue in list(chain):
                id_res = residue.id
                if id_res in residues_to_remove:
                    chain.detach_child(id_res)
    io = PDBIO()
    io.set_structure(structure)
    io.save(pdb_file[:-4] + '_trimmed.pdb', write_end=False)


def write_info_frag_from_dictio_frag(dictio_fragments, clust_fold, keypool, ali_confdict):
    """

    :param dictio_fragments:
    :param clust_fold:
    :param keypool:
    :param ali_confdict:
    :return:
    """
    path_infofrag = os.path.join(clust_fold,keypool+"_info_frag")
    file_fragments = open(path_infofrag, 'w')
    if ali_confdict['postmortem'] and 'ent_file' in ali_confdict:
        file_fragments.write( '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' %
                              ('Name','LLGrbr','LLGgimb','LLGgimbLLG','Z-score','Rotcluster','InitCC','Efom','PseudoCC','wMPE'))
        for key in dictio_fragments[keypool].keys():
            file_fragments.write( '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (os.path.basename(key),
                                                                                                     dictio_fragments[keypool][key]['llg_rbr'],
                                                                                                     dictio_fragments[keypool][key]['llg_gimble'],
                                                                                                     dictio_fragments[keypool][key]['llg_gimble_llg'],
                                                                                                     dictio_fragments[keypool][key]['zscore'],
                                                                                                     dictio_fragments[keypool][key]['rot_cluster'],
                                                                                                     dictio_fragments[keypool][key]['initcc'],
                                                                                                     dictio_fragments[keypool][key]['efom'],
                                                                                                     dictio_fragments[keypool][key]['pseudocc'],
                                                                                                     dictio_fragments[keypool][key]['list_MPE'][2]))
    else:
        file_fragments.write( '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s \n' % ('Name','LLGrbr','LLGgimb',
                                                                                            'LLGgimbLLG','Z-score',
                                                                                            'Rotcluster','InitCC',
                                                                                            'Efom','PseudoCC'))
        for key in dictio_fragments[keypool].keys():
            file_fragments.write( '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s \n' % (os.path.basename(key),
                                                                                                dictio_fragments[
                                                                                                    keypool][key][
                                                                                                    'llg_rbr'],
                                                                                                dictio_fragments[
                                                                                                    keypool][key][
                                                                                                    'llg_gimble'],
                                                                                                dictio_fragments[
                                                                                                    keypool][key][
                                                                                                    'llg_gimble_llg'],
                                                                                       dictio_fragments[keypool][key]['zscore'],
                                                                                       dictio_fragments[keypool][key]['rot_cluster'],
                                                                                       dictio_fragments[keypool][key]['initcc'],
                                                                                       dictio_fragments[keypool][key]['efom'],
                                                                                       dictio_fragments[keypool][key]['pseudocc']))
    file_fragments.close()


def write_sum_file_from_dictio_result(path_sum,dictio_result):
    fileforclu = open(path_sum, 'w')
    fileforclu.write(
        '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (
        'Name', 'wMPD_first', 'wMPD_last', 'diff_wMPD', 'mapcc_first',
        'mapcc_last', 'shift_first_x', 'shift_first_y', 'shift_first_z', 'shift_last_x', 'shift_last_y',
        'shift_last_z'))
    for phaseset in dictio_result.keys():
        name = os.path.basename(phaseset)
        wmpe_first = round(dictio_result[phaseset]['wMPE_first'], 2)
        wmpe_last = round(dictio_result[phaseset]['wMPE_last'], 2)
        diffwmpe = -1
        if dictio_result[phaseset]['mapcc_first'] != None:
            mapcc_first = round(dictio_result[phaseset]['mapcc_first'], 2)
        else:
            mapcc_first = -1
        if dictio_result[phaseset]['mapcc_last'] != None:
            mapcc_last = round(dictio_result[phaseset]['mapcc_last'], 2)
        else:
            mapcc_last = -1
        shift_first = dictio_result[phaseset]['shift_first']
        shift_last = dictio_result[phaseset]['shift_last']
        fileforclu.write(
            '%-40s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s %-10s\n' % (name, wmpe_first, wmpe_last,
                                                                                           diffwmpe, mapcc_first,
                                                                                           mapcc_last,
                                                                                           shift_first[0],
                                                                                           shift_first[1],
                                                                                           shift_first[2],
                                                                                           shift_last[0],
                                                                                           shift_last[1],
                                                                                           shift_last[2]))
    del (fileforclu)


if __name__ == "__main__":  # A set of tests to check everything works as expected

    print("Run to check syntax errors")

    # Test new function
    # name_job=sys.argv[1]
    # print get_topexp_from_html_output(name_job,os.getcwd())
