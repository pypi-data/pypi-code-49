#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
generate_datasets_cancer.py: Script to generate pre-filtered cancer data sets files.
"""

import os
import sys

from tqdm import tqdm

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode.utils import dir_and_file_handling as dir_handlers
from VEnCode.utils import general_utils as gen_utils
from VEnCode import internals
from VEnCode.common_variables import cancer_celltype_list, promoter_file_name, enhancer_file_name


class SetUp:
    """set up some variables: """
    data_type = "promoters"
    if data_type == "enhancers":
        file_name = enhancer_file_name
    else:
        file_name = promoter_file_name


# Now you don't need to change anything else
setup = SetUp()

data = internals.DataTpm(file=setup.file_name, sample_types="primary cells", data_type=setup.data_type)
data.merge_donors_primary(exclude_target=False)
data_original = data.copy()
data_cancer = internals.DataTpm(file=setup.file_name, sample_types="cell lines", data_type=setup.data_type)

for celltype in tqdm(cancer_celltype_list, desc="Completed: "):
    data.add_celltype(celltype, file=data_cancer)
    data.make_data_celltype_specific(celltype)
    data.filter_by_target_celltype_activity(threshold=0.0001, binarize=False)

    if isinstance(celltype, dict):
        celltype = list(celltype.keys())[0]
    celltype = gen_utils.str_replace_multi(celltype, {":": "-", "/": "-"})  # those symbols can't be in file names
    directory = dir_handlers.check_if_and_makefile(os.path.join(
        "Files", "Dbs",
        "{}_tpm_{}-1".format(celltype, setup.data_type)), path_type="parent3")

    data.data.to_csv(directory, sep=";")
    data = data_original.copy()
