#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import classes

from VEnCode.common_variables import file_name, primary_exclude_list, \
    primary_not_include_codes, primary_cells_supersets

if __name__ == "__main__":
    initialize_promoters = classes.Promoters(file_name,
                                             "acute myeloid leukemia",
                                             celltype_exclude=primary_exclude_list,
                                             not_include=primary_not_include_codes,
                                             partial_exclude=primary_cells_supersets,
                                             sample_types=["primary cells", "cell lines"],
                                             second_parser="primary cells")

    # get vencodes:
    initialize_promoters.get_vencodes(n=1, write_file=True)
