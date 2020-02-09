#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
generate_datasets_old.py: Script to generate files with parsed data sets.
"""
import os

import classes
import pandas as pd
from tqdm import tqdm
from utils import util

from VEnCode.common_variables import enhancer_file_name, enhancer_names_db, primary_cell_list, \
    primary_exclude_list, \
    primary_not_include_codes, primary_cells_supersets
from VEnCode.utils import dir_and_file_handling as dhs

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

data_copy = init.data.copy()
init.data = init.merge_donors_into_celltypes()
for celltype in tqdm(primary_cell_list):
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
