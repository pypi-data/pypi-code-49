#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
table_vens.py: Script used to generate Supplementary Data S1 as in Macedo & Gontijo, 2019.
"""

import os
import sys

from tqdm import tqdm

import VEnCode.utils.dir_and_file_handling

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals
import VEnCode.utils.dir_and_file_handling as d_f_handling
from VEnCode.common_variables import three_donors_cell_list, cancer_three_donors_list


class SetUp:
    """ set up some variables: """
    celltype_type = "primary"
    first_data_type = "enhancers"
    second_data_type = "promoters"
    ven_number = 20

    # Next ones you may not need to change:
    target_celltype_activity = 0.1
    non_target_celltypes_inactivity = 0
    second_target_celltype_activity = 0.5
    second_non_target_celltypes_inactivity = 0
    reg_element_sparseness = 0
    second_reg_element_sparseness = 0


# Now you don't need to change anything else
setup = SetUp()

algorithm = "heuristic"

if setup.celltype_type == "primary":
    celltype_list = three_donors_cell_list
    sample_types = "primary cells"
elif setup.celltype_type == "cancer":
    celltype_list = cancer_three_donors_list
    sample_types = "cell lines"
else:
    raise AttributeError("Celltype_type - {} - currently not supported".format(setup.celltype_type))

results = {}
data = internals.DataTpm(file="parsed", sample_types=sample_types, data_type=setup.first_data_type)
data_second = internals.DataTpm(file="parsed", sample_types=sample_types, data_type=setup.second_data_type)

# create a directory to store results
results_directory = d_f_handling.check_if_and_makefile(os.path.join(
    "E-values table", "{} {}".format(setup.celltype_type, "Heuristic2")),
    path_type="parent3")

# Set up the important information to include in the file
info_list = [attr for attr in dir(setup) if not callable(getattr(setup, attr)) and not attr.startswith("__")]
info_dict = {}
for item in info_list:
    info_dict[item] = getattr(setup, item)

# write the information to a file
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, info_dict, deprecated=False)

# cycle your list of cell types:
for celltype in tqdm(celltype_list, desc="Completed: "):
    # prepare first data:
    data.make_data_celltype_specific(celltype)
    data.filter_by_target_celltype_activity(threshold=setup.target_celltype_activity)
    data.filter_by_reg_element_sparseness(threshold=setup.reg_element_sparseness)
    data.define_non_target_celltypes_inactivity(threshold=setup.non_target_celltypes_inactivity)
    data.sort_sparseness()
    # prepare second data:
    data_second.make_data_celltype_specific(celltype)
    data_second.filter_by_target_celltype_activity(threshold=setup.second_target_celltype_activity)
    data_second.filter_by_reg_element_sparseness(threshold=setup.second_reg_element_sparseness)
    data_second.define_non_target_celltypes_inactivity(threshold=setup.second_non_target_celltypes_inactivity)
    data_second.sort_sparseness()

    # Deal with possible dictionaries in celltype list:
    if isinstance(celltype, dict):
        celltype = list(celltype.keys())[0]
    data_second_original = data_second.copy()
    results[celltype] = []
    for k in range(1, 5):
        # Launch VEnCode search:
        vencodes = internals.Vencodes(data, algorithm="heuristic", number_of_re=k, stop=3)
        vencodes.next_heuristic2_vencode(data_second, amount=setup.ven_number)

        # Determine e-values:
        if vencodes.vencodes:
            vencodes.determine_e_values()
            best = []
            e_values = vencodes.e_values.copy()
            for i in range(5):
                try:
                    best_partial = max(e_values, key=lambda key: e_values[key])
                except ValueError:
                    break
                best.append(best_partial)
                try:
                    e_values.pop(best_partial)
                except KeyError:
                    print("Could not pop {} from dict e_values".format(best_partial))
            results[celltype].append([[i, vencodes.e_values[i]] for i in best])
            if len(results[celltype][k-1]) < 5:
                results[celltype].append([""]*(5 - len(results[celltype])))
        else:
            results[celltype].append([""]*5)
        data_second = data_second_original.copy()
    VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, results, deprecated=False, method="a")
    results = {}
print("File saved in: {}".format(results_directory))
