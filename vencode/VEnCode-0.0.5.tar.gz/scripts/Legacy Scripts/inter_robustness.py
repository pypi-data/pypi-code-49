#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""inter_robustness.py: Functions for generating inter robustness data """

import classes

from VEnCode.common_variables import promoter_file_name, primary_cell_list, \
    primary_exclude_list, primary_not_include_codes, primary_cells_supersets, \
    three_donors_cell_list

lines_3donors = ['acute myeloid leukemia (FAB M2) cell line', 'acute myeloid leukemia (FAB M6) cell line',
                 'B lymphoblastoid cell line: GM12878 ENCODE', 'carcinoid cell line', 'choriocarcinoma cell line',
                 'epitheloid carcinoma cell line: HelaS3 ENCODE', 'Hep-2 cells mock treated',
                 'hepatocellular carcinoma cell line: HepG2 ENCODE', 'leiomyoma cell line',
                 'neuroectodermal tumor cell line']


def healthy_lines():
    initialize_promoters = classes.Promoters(promoter_file_name,
                                             three_donors_cell_list,
                                             celltype_exclude=primary_exclude_list,
                                             not_include=primary_not_include_codes,
                                             partial_exclude=primary_cells_supersets,
                                             sample_types="primary cells",
                                             second_parser=None)
    """ get the percentage of VEnCodes taken for 1 donor that work for all donors: """
    initialize_promoters.ven_diagram_interception(2000, 5, 3, combinations_number=4, threshold=90)

    """ get the percentage of VEnCodes taken for 1, 2, 3, etc donors that work for all and com """
    # initialize_promoters.inter_donor_percentage_difference(2000, 3, 4, combinations_number=4, threshold=90)


def cancer_lines():
    for line in lines_3donors:
        primary_cell_list.append(line)
        initialize = classes.Promoters(promoter_file_name,
                                       primary_cell_list,
                                       celltype_exclude=primary_exclude_list,
                                       not_include=primary_not_include_codes,
                                       partial_exclude=primary_cells_supersets,
                                       sample_types=["primary cells", "cell lines"],
                                       second_parser="primary cells")
        initialize.ven_diagram_interception(2000, 5, 3, combinations_number=4, threshold=90, custom_celltypes=[line])
        primary_cell_list.remove(line)
        break


if __name__ == "__main__":
    cancer_lines()
