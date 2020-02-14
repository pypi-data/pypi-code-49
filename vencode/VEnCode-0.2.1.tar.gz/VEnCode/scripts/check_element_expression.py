#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
check_element_expression.py: file used to check expression levels of certain promoter and enhancer regions
in specific cell types of the FANTOM5 data.
"""

import os
import sys

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode import internals_extensions as iext

element_list = ('chr6:94545083-94545465', 'chr11:94480491-94481212', 'chr2:86922220-86922584', 'chr12:20975224-20975562')

cell_type = "embryonic kidney cell line: HEK293/SLAM untreated"
path_out = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
           "3-Vencode/Fantom5/Expression Levels/"

path_out = path_out + cell_type.replace(":", "-").replace("/", "-") + ".csv"

if __name__ == "__main__":
    expression = iext.CheckElementExpression(element_list=element_list,
                                             cell_type=cell_type,
                                             data_type="enhancers",
                                             parsed=False)
    expression.export_expression_data(path=path_out)
