import os

import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog
import ast

from VEnCode import internals_extensions as iext
import VEnCode.utils.dir_and_file_handling as d_f_handling

def get_path():
    """ Gets path using a file dialog. """
    tk.Tk().withdraw()
    path = filedialog.askopenfilename()
    return path


path_evalues = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
               "3-Vencode/Fantom5/Validations/Single Cell/A549 200 SC VEn - samp/" \
               "A549_singlecell_evalues.csv"

path_out = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
               "3-Vencode/Fantom5/Validations/Single Cell"
filename = "Expression_SC_samp.csv"
path_out = os.path.join(path_out, filename)

if path_evalues is None:
    path_evalues = get_path()

cell_type = "lung adenocarcinoma cell line:A549"

df_evalues = pd.read_csv(path_evalues, sep=";", engine="python", header=None)
vencodes_tuple = df_evalues.iloc[:, 0].values
elements_set = set()
vencodes_list = list()
for vencode in vencodes_tuple:
    vencode = ast.literal_eval(vencode)
    vencodes_list.append(vencode)
    for element in vencode:
        elements_set.add(element)
elements_list = list(elements_set)
expression = iext.CheckElementExpression(element_list=elements_list,
                                         cell_type=cell_type,
                                         data_type="enhancers",
                                         parsed=False)
results = expression.export_expression_data(method="return")
expressions = dict()
for vencode in vencodes_list:
    expression_list = []
    for element in vencode:
        expression = results.loc[element]
        expression_list.append(expression[0])
    expressions[vencode] = expression_list
d_f_handling.write_dict_to_csv(path_out, expressions, deprecated=False)
