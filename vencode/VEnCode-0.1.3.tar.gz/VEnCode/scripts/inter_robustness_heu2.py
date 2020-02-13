#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
inter_robustness_heu2.py: Script to find cell type z-values, using the hybrid vencode strategy,
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
from VEnCode.common_variables import three_donors_cell_list
import VEnCode.utils.dir_and_file_handling as d_f_handling


class SetUp:
    """ set up some variables: """
    celltype_list = three_donors_cell_list
    first_data_type = "enhancers"
    second_data_type = "promoters"
    algorithm = "heuristic"

    target_celltype_activity = 0.1
    reg_element_sparseness = 0
    non_target_celltypes_inactivity = 0

    second_target_celltype_activity = 0.5
    second_reg_element_sparseness = 0
    second_non_target_celltypes_inactivity = 0


# Now you don't need to change anything else
setup = SetUp()
results_final = {}
data = internals.DataTpm(file="parsed", sample_types="primary cells", data_type=setup.data_type)

for celltype in tqdm(setup.re_list, desc="Completed: "):
    data.make_data_celltype_specific(celltype)
    data_copy = data.copy()
    for k in [1, 2]:
        results_celltype = []
        for n in range(50):
            choice = random.sample(range(3), k=k)  # chooses a random int from 0 to 2, to later choose a donor.
            data.filter_by_target_celltype_activity(threshold=setup.target_celltype_activity, donors=choice)
            data.filter_by_reg_element_sparseness(threshold=setup.reg_element_sparseness)
            data.define_non_target_celltypes_inactivity(threshold=setup.non_target_celltypes_inactivity)
            if setup.algorithm != "sampling":
                data.sort_sparseness()

            if setup.algorithm == "sampling":
                vencodes = internals.Vencodes(data, algorithm="sampling", number_of_re=setup.ven_size, n_samples=10000)
            elif setup.algorithm == "heuristic":
                vencodes = internals.Vencodes(data, algorithm="heuristic", number_of_re=setup.ven_size, stop=3)
            else:
                raise AttributeError("Algorithm '{}' not recognized".format(setup.algorithm))
            vencodes.next(amount=1)
            if vencodes.vencodes:
                donors_vencode_data = vencodes.celltype_donors_data.loc[vencodes.vencodes[0]]
                assess_if_not_vencode = np.any(donors_vencode_data == 0, axis=0)
                result = any(assess_if_not_vencode)
                results_celltype.append(not result)
            else:
                results_celltype.append("")
            data = data_copy
        results_final[celltype + str(k)] = results_celltype

# create a directory to store results
results_directory = d_f_handling.check_if_and_makefile(os.path.join(
    "Z-values analysis", "{} primary {} {}".format("Three donors", setup.data_type, setup.algorithm)),
    path_type="parent3")

# Set up the important information to include in the file
info_list = [attr for attr in dir(setup) if not callable(getattr(setup, attr)) and not attr.startswith("__")]
info_dict = {}
for item in info_list:
    info_dict[item] = getattr(setup, item)

# write the information and results
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, info_dict, deprecated=False)
VEnCode.utils.dir_and_file_handling.write_dict_to_csv(results_directory, results_final, deprecated=False, method="a")