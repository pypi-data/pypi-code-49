#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import classes

from VEnCode.common_variables import file_name, primary_exclude_list, \
    primary_not_include_codes, primary_cells_supersets

# region Variables
case_studies = ["small cell lung carcinoma", "testicular germ cell embryonal carcinoma",
                "chronic myelo leukemia", "acute myeloid leukemia (FAB M2)", "teratocarcinoma"]
# endregion Variables

if __name__ == "__main__":
    initialize_promoters = classes.Promoters(file_name,
                                             case_studies[3],
                                             celltype_exclude=primary_exclude_list,
                                             not_include=primary_not_include_codes,
                                             partial_exclude=primary_cells_supersets,
                                             sample_types=["primary cells", "cell lines"],
                                             second_parser="primary cells")
    # get files for VEn diagram:
    initialize_promoters.ven_diagrams(50000, 4, threshold=50)

    # test if biologically (statistically) relevant:
    # initialize_promoters.statistics_ven_diagram(5000, 5, 22, threshold=50)
