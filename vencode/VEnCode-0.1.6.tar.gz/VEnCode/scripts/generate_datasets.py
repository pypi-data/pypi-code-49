#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
generate_datasets.py: Script to generate pre-filtered data sets files.
"""
import os

import classes
import pandas as pd
from tqdm import tqdm

from VEnCode import internals
from VEnCode.common_variables import enhancer_file_name, enhancer_names_db, primary_cell_list, \
    primary_exclude_list, promoter_file_name, \
    primary_not_include_codes, primary_cells_supersets
from VEnCode.utils import dir_and_file_handling as dhs
from VEnCode.utils import util

# Promoters:
"""
init = classes.Promoters(promoter_file_name, complete_primary_cell_list,
                         celltype_exclude=complete_primary_exclude_list,
                         not_include=complete_primary_non_include_list,
                         partial_exclude=complete_primary_jit_exclude_list,
                         sample_types="primary cells", second_parser=None,
                         conservative=True, log_level="info", nrows=None)
"""
# Enhancers:

init = classes.Promoters(enhancer_file_name,
                         primary_cell_list,
                         celltype_exclude=primary_exclude_list,
                         not_include=primary_not_include_codes,
                         partial_exclude=primary_cells_supersets,
                         sample_types="primary cells", second_parser=None,
                         conservative=True, log_level="info", enhancers=enhancer_names_db,
                         skiprows=None, nrows=None)

data = internals.DataTpm(file=promoter_file_name, sample_types="primary cells", data_type="promoters")
data_copy = data.data.copy()
# data_copy = init.data.copy()
# init.data = init.merge_donors_into_celltypes()

for celltype in tqdm(primary_cell_list, desc="Completed: "):
    # file name:
    filename = "{}_tpm_enhancers".format(celltype)
    results_directory = dhs.check_if_and_makefile(os.path.join("Files", "Dbs", filename),
                                                  path_type="parent3")
    # Data
    data_celltype = init.data[celltype]
    init.data.drop(celltype, axis=1, inplace=True)
    init.data = pd.concat([init.data, data_copy[init.codes[celltype]]],
                          axis=1)
    data_set = util.df_filter_by_expression(init.data, init.codes[celltype], 0.0001)
    data_set.to_csv(results_directory, sep=";")

    init.data.drop(data_copy[init.codes[celltype]], axis=1, inplace=True)
    init.data = pd.concat([init.data, data_celltype], axis=1)
