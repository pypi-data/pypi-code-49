#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
intra_robustness_heu2.py: Script for generating intra robustness data, using the heuristic2 approach as in
Macedo & Gontijo, 2019.
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
    first_data_type = "enhancers"
    second_data_type = "promoters"
    ven_number = 20
    ven_size = 4

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
    celltype_list = primary_cell_list
    sample_types = "primary cells"
elif setup.celltype_type == "cancer":
    celltype_list = cancer_celltype_list
    sample_types = "cell lines"
else:
    raise AttributeError("Celltype_type - {} - currently not supported".format(setup.celltype_type))

results = {}
data = internals.DataTpm(file="parsed", sample_types=sample_types, data_type=setup.first_data_type)
data_second = internals.DataTpm(file="parsed", sample_types=sample_types, data_type=setup.second_data_type)

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

    # Launch VEnCode search:
    vencodes = internals.Vencodes(data, algorithm="heuristic", number_of_re=setup.ven_size, stop=3)
    vencodes.next_heuristic2_vencode(data_second, amount=setup.ven_number)

    # Determine e-values:
    if vencodes.vencodes:
        vencodes.determine_e_values()
        e_values = list(vencodes.e_values.values())
        if len(e_values) != setup.ven_number:
            for i in range(len(e_values), setup.ven_number):
                e_values.append("")
        results[celltype] = e_values
    else:
        results[celltype] = [""]*20

# create a directory to store results
results_directory = d_f_handling.check_if_and_makefile(os.path.join(
    "E-values analysis", "{} {} k{} {}".format(setup.celltype_type, "Heuristic2", setup.ven_size, algorithm)),
    path_type="parent3")

# Set up the important information to include in the file
info_list = [attr for attr in dir(setup) if not callable(getattr(setup, attr)) and not attr.startswith("__")]
info_dict = {}
for item in info_list:
    info_dict[item] = getattr(setup, item)

# write the information and results
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, info_dict, deprecated=False)
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, results, deprecated=False, method="a")
print("File saved in: {}".format(results_directory))
