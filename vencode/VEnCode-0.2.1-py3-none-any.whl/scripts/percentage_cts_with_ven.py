#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
percentage_cts_with_ven.py: Script to find which cell types have at least one VEnCode, as in Macedo & Gontijo, 2019.
"""

import os
import sys

from tqdm import tqdm

import VEnCode.utils.dir_and_file_handling

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals
import VEnCode.utils.dir_and_file_handling as d_f_handling
from VEnCode.common_variables import primary_cell_list, cancer_celltype_list


class SetUp:
    """ set up some variables: """
    celltype_type = "cancer"
    data_type = "enhancers"
    algorithm = "sampling"

    # Next ones you may not need to change:
    non_target_celltypes_inactivity = 0
    if data_type == "enhancers":
        target_celltype_activity = 0.1
    elif data_type == "promoters":
        target_celltype_activity = 0.5
    else:
        raise AttributeError("data_type - {} - currently not supported".format(data_type))
    if algorithm == "heuristic":
        reg_element_sparseness = 0
    elif algorithm == "sampling":
        reg_element_sparseness = 90
    else:
        raise AttributeError("Algorithm - {} - currently not supported".format(algorithm))


# Now you don't need to change anything else
setup = SetUp()

if setup.celltype_type == "cancer":
    celltype_list = cancer_celltype_list
    sample_types = "cell lines"
elif setup.celltype_type == "primary":
    celltype_list = primary_cell_list
    sample_types = "primary cells"
else:
    raise AttributeError("Celltype_type - {} - currently not supported".format(setup.celltype_type))

results = {}
data = internals.DataTpm(file="parsed", sample_types=sample_types, data_type=setup.data_type)

# cycle your list of cell types:
for celltype in tqdm(celltype_list, desc="Completed: "):
    # prepare data:
    data.make_data_celltype_specific(celltype)
    data.filter_by_target_celltype_activity(threshold=setup.target_celltype_activity)
    data.filter_by_reg_element_sparseness(threshold=setup.reg_element_sparseness)
    data.define_non_target_celltypes_inactivity(threshold=setup.non_target_celltypes_inactivity)
    if setup.algorithm != "sampling":
        data.sort_sparseness()

    try:
        results[celltype] = []
    except TypeError:
        celltype = list(celltype.keys())[0]
        results[celltype] = []

    # cycle the k numbers to search if there's a VEnCode.
    for k in range(1, 11):  # you can redefine the range of k here
        # Launch VEnCode search:
        if setup.algorithm == "sampling":
            vencodes = internals.Vencodes(data, algorithm="sampling", number_of_re=k, n_samples=10000)
        elif setup.algorithm == "heuristic":
            vencodes = internals.Vencodes(data, algorithm="heuristic", number_of_re=k, stop=3)
        else:
            raise AttributeError("Algorithm '{}' not recognized".format(setup.algorithm))
        vencodes.next(amount=1)

        # Determine if a VEnCode was found:
        if vencodes.vencodes:
            for v in range(k, 11):
                results[celltype].append(1)
            break
        else:
            results[celltype].append(0)

# create a directory to store results
results_directory = d_f_handling.check_if_and_makefile(os.path.join(
    "VEnCode Search",
    "{} {} {} sp{} act{} inact{}".format(setup.celltype_type, setup.data_type, setup.algorithm,
                                         setup.reg_element_sparseness,
                                         setup.target_celltype_activity,
                                         setup.non_target_celltypes_inactivity)), path_type="parent3")

# Set up the important information to include in the file
info_list = [attr for attr in dir(setup) if not callable(getattr(setup, attr)) and not attr.startswith("__")]
info_dict = {}
for item in info_list:
    info_dict[item] = getattr(setup, item)

# write the information and results
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, info_dict, deprecated=False)
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, results, deprecated=False, method="a")
print("File saved in: {}".format(results_directory))
