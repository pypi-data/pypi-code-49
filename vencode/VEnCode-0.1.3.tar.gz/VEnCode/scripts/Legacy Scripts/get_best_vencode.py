#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""get_best_vencode.py: Script to get the best VEnCodes possible """

import classes
from utils import input_handlers as ih

from VEnCode.common_variables import promoter_file_name, primary_cell_list, \
    primary_exclude_list, \
    primary_not_include_codes, primary_cells_supersets

vencodes_number = ih.input_integers("Number of VEnCodes to get: ")
rows_number = ih.input_integers("Number of rows from the file to open (put 'None' for full file): ")

# Promoters
initialize_promoters = classes.Promoters(promoter_file_name, primary_cell_list,
                                         celltype_exclude=primary_exclude_list,
                                         not_include=primary_not_include_codes,
                                         partial_exclude=primary_cells_supersets,
                                         sample_types="primary cells", second_parser=None,
                                         conservative=True, log_level="info", skip_raw_data=True,
                                         nrows=rows_number)
initialize_promoters.best_vencode_generator("Hepatocyte", number_vencodes=vencodes_number)


# Enhancers
"""
initialize_enhancers = Classes.Promoters(enhancer_file_name,
                                         complete_primary_cell_list,
                                         celltype_exclude=complete_primary_exclude_list,
                                         not_include=complete_primary_non_include_list,
                                         partial_exclude=complete_primary_jit_exclude_list,
                                         sample_types="primary cells", second_parser=None,
                                         conservative=True, log_level="info", enhancers=enhancer_names_db,
                                         skiprows=None, nrows=24000)
initialize_enhancers.best_vencode_generator("Hepatocyte", number_vencodes=4)
"""
# To create an ill patient:
"""
complete_primary_cell_list.append("testicular germ cell embryonal carcinoma")
initialize_promoters = Classes.Promoters(promoter_file_name,
                                         complete_primary_cell_list,
                                         celltype_exclude=complete_primary_exclude_list,
                                         not_include=complete_primary_non_include_list,
                                         partial_exclude=complete_primary_jit_exclude_list,
                                         sample_types=["primary cells", "cell lines"],
                                         second_parser="primary cells", conservative=True,
                                         log_level="info", nrows=40000)
initialize_promoters.best_vencode_generator("testicular germ cell embryonal carcinoma", number_vencodes=4)
"""

# some tests:
"""
initialize_promoters.test_vencode_data(rows=('chr10:114581583..114581600,-', 'chr10:101841398..101841415,-'),
                                       file_name="test_hepatocyte_vencode.csv")

initialize_promoters.test_vencode_data(('chr10:114581583..114581600,-', 'chr10:101841398..101841415,-'),
                                       (initialize_promoters.codes["Hepatocyte"]))
"""
