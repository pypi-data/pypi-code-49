#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" get_validated_vencodes.py: file used to generate VEnCodes from cross-validated enhancer regions. """

import os
import sys

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals_extensions as iext
from VEnCode.utils import validation_utils as val


class SetUp:
    cell_type = "lung adenocarcinoma cell line:A549"
    type = "cell lines"
    data_type = "enhancers"
    algorithm = "heuristic"
    k = 4
    number_vencodes_to_get = 200

    data_set = "enhancer_atlas"  # default: None

    path_out_ven = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
                   "3-Vencode/Fantom5/VEnCodes/A549-atlas 200 val vencodes - heu"

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
        reg_element_sparseness = 90  # For some, you probably have to reduce sparseness to 0.
    else:
        raise AttributeError("Algorithm - {} - currently not supported".format(algorithm))


# Now you don't need to change anything else

class ValidatedVEnCodes:
    """
    Gets validated VEnCodes.
    """

    def __init__(self, set_up):
        self.set_up = set_up
        thresholds = (
            set_up.non_target_celltypes_inactivity, set_up.target_celltype_activity, set_up.reg_element_sparseness)
        self.data = iext.GetVencodeValidated(validate_with=val.get_data_to_validate(set_up.cell_type,
                                                                                    optional=set_up.data_set),
                                             cell_type=set_up.cell_type,
                                             data_type=set_up.data_type, algorithm=set_up.algorithm,
                                             n_regulatory_elements=set_up.k,
                                             number_vencodes=set_up.number_vencodes_to_get,
                                             parsed=val.status_parsed(set_up.cell_type),
                                             thresholds=thresholds, n_samples=10000, sample_type=set_up.type)

    def export(self):
        """
        Export the E values and VEnCode data to a file.
        """
        self.data.vencodes.export("e-values", path=self.set_up.path_out_ven)
        self.data.vencodes.get_vencode_data(method="write", path=self.set_up.path_out_ven)


if __name__ == "__main__":
    setup = SetUp()
    ven = ValidatedVEnCodes(setup)
    ven.export()
