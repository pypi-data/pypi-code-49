#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""e_value_statistics.py: Functions for generating tables to use in statistic analyses for Macedo & Gontijo, 2019."""

import os
import numpy as np
import pandas as pd

from VEnCode import internals
from VEnCode.utils import dir_and_file_handling as dhs
from VEnCode.utils import general_utils as ghs

if __name__ == "__main__":
    celltype_number = [20, 80, 100, 154, 200, 250, 350, 450, 550, 650, 800, 1000]
    promoter_number = range(1, 11)  # number of promoters ranging from x to y
    e_values = pd.DataFrame(index=promoter_number, columns=celltype_number)
    for i in celltype_number:
        print("Starting number of cell types: {}".format(i))
        for z in promoter_number:
            print("Starting number of promoters: {}".format(z))
            data = pd.DataFrame(np.zeros(shape=(z, i)), dtype=np.int8)
            e_value_raw = internals.Vencodes.vencode_mc_simulation(data, reps=1000)
            e_value = ghs.e_value_normalizer(e_value_raw, z, i)  # use this line if we want normalized e-values
            e_values.loc[z, i] = e_value
    try:
        file_name = dhs.check_if_and_makefile(os.path.join("E-value statistics", "e_value statistics norm"),
                                              path_type="parent3")
    except:
        file_name = "e_value statistics norm.csv"
    with open(file_name, 'w') as f:
        e_values.to_csv(f, sep=";")
