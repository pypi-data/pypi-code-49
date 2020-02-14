#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
sampling_vs_heuristic.py: Script to compare VEnCodes between the sampling and heuristic algorithms.
"""
import classes
import matplotlib.pyplot as plt
import utils.directory_handlers as dhs
import utils.input_handlers as ihs
import utils.writing_files as wfs
from tqdm import tqdm

from VEnCode.common_variables import promoter_file_name, primary_cell_list, \
    primary_exclude_list, \
    primary_not_include_codes, primary_cells_supersets

rows_number = ihs.input_integers("Number of rows from the file to open (put 'None' for full file): ")
vencodes_number = ihs.input_integers("Number of VEnCodes to get: ")
algorithm = ihs.input_string("Algorithm(s) to use (heuristic, sampling, both): ")

celltype_list = ["Lens Epithelial Cells"]


initialize_promoters = classes.Promoters(promoter_file_name, primary_cell_list,
                                         celltype_exclude=primary_exclude_list,
                                         not_include=primary_not_include_codes,
                                         partial_exclude=primary_cells_supersets,
                                         sample_types="primary cells", second_parser=None,
                                         conservative=True, log_level="info", nrows=rows_number)

for celltype in tqdm(celltype_list, desc="Celltypes"):
    vencodes = initialize_promoters.vencode_generator(celltype, algorithm=algorithm,
                                                      combinations_number=4,
                                                      threshold_activity=1, threshold_inactivity=0,
                                                      threshold_sparseness=90,
                                                      number_vencodes=vencodes_number)
    data = []
    labels = []
    for key, value in vencodes.items():
        results_directory = dhs.check_if_and_makefile(r"/sampling_vs_heuristic/{} {} method".format(celltype,
                                                                                                    key),
                                                      path_type="parent2")
        wfs.write_dict_to_csv(results_directory, value, deprecated=False)
        data.append(list(value.values()))
        labels.append(key)
    plt.boxplot(data)
    """
    xtickNames = plt.setp(ax1, xticklabels=np.repeat(randomDists, 2))
    plt.setp(xtickNames, rotation=45, fontsize=8)
    """
    plt.show()

    break
