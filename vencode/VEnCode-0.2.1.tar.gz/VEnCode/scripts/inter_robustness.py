#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
inter_robustness.py: Script to find cell type z values for all cell types with 3 or more donors,
as in Macedo & Gontijo, 2019.
"""

import os
import sys
import random
import numpy as np
from tqdm import tqdm

import VEnCode.utils.dir_and_file_handling

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals
import VEnCode.utils.dir_and_file_handling as d_f_handling
from VEnCode.common_variables import cancer_three_donors_list, cancer_three_donors_bio_rep_list, \
    three_donors_cell_list, cancer_four_donors_list


class SetUp:
    """ Set up some variables: """
    celltype_type = "cancer"
    data_type = "enhancers"
    algorithm = "sampling"
    celltypes_list = cancer_three_donors_list
    ven_size = 4

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
    sample_types = "cell lines"
elif setup.celltype_type == "primary":
    sample_types = "primary cells"
else:
    raise AttributeError("Celltype_type - {} - currently not supported".format(setup.celltype_type))

results_final = {}
data = internals.DataTpm(file="parsed", sample_types=sample_types, data_type=setup.data_type)

# cycle your list of cell types:
for celltype in tqdm(setup.celltypes_list, desc="Completed: "):
    data.make_data_celltype_specific(celltype)
    data_copy = data.copy()

    # Deal with possible dictionaries in celltype list:
    if isinstance(celltype, dict):
        celltype = list(celltype.keys())[0]

    # cycle possible number of combinations of donors:
    donors_number = len(data.ctp_analyse_donors[celltype])
    for k in range(1, donors_number):
        results_celltype = []
        for n in range(50):
            choice = random.sample(range(donors_number), k=k)  # chooses a random int from 0 to 2, to later choose a donor.
            data.filter_by_target_celltype_activity(threshold=setup.target_celltype_activity, donors=choice)
            data.filter_by_reg_element_sparseness(threshold=setup.reg_element_sparseness)
            data.define_non_target_celltypes_inactivity(threshold=setup.non_target_celltypes_inactivity)
            if setup.algorithm != "sampling":
                data.sort_sparseness()

            # Launch VEnCode search:
            if setup.algorithm == "sampling":
                vencodes = internals.Vencodes(data, algorithm="sampling", number_of_re=setup.ven_size, n_samples=10000)
            elif setup.algorithm == "heuristic":
                vencodes = internals.Vencodes(data, algorithm="heuristic", number_of_re=setup.ven_size, stop=3)
            else:
                raise AttributeError("Algorithm '{}' not recognized".format(setup.algorithm))
            vencodes.next(amount=1)

            # Determine z-values
            if vencodes.vencodes:
                donors_vencode_data = vencodes.celltype_donors_data.loc[vencodes.vencodes[0]]
                assess_if_not_vencode = np.any(donors_vencode_data == 0, axis=0)
                result = any(assess_if_not_vencode)
                results_celltype.append(not result)
            else:
                results_celltype.append("")
            data = data_copy
        results_final["{}_{}".format(celltype, k)] = results_celltype

# create a directory to store results
results_directory = d_f_handling.check_if_and_makefile(os.path.join(
    "Z-values analysis", "{} {} {} {}".format(setup.celltype_type, "three donors", setup.data_type, setup.algorithm)),
    path_type="parent3")

# Set up the important information to include in the file
info_list = [attr for attr in dir(setup) if not callable(getattr(setup, attr)) and not attr.startswith("__")]
info_dict = {}
for item in info_list:
    info_dict[item] = getattr(setup, item)

# write the information and results
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, info_dict, deprecated=False)
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, results_final, deprecated=False, method="a")
print("File saved in: {}".format(results_directory))
