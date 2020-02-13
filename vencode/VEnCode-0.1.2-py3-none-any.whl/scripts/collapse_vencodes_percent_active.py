import os
import sys

file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_dir)

from VEnCode.utils import dir_and_file_handling as d_f_handling
from VEnCode.utils import pandas_utils as pd_u

files_path = "D:/Utilizador HDD/OneDrive - Nova Medical School Faculdade de Ciências Médicas da UNL/1-Research/" \
             "3-Vencode/Fantom5/VEnCodes/prostate cancer cell average 200"

# Append all files in directory to one big Pandas DataFrame
vencodes_all = d_f_handling.read_append_multiple_files(files_path, "*vencode*")
# Clean the DataFrame: remove genomic coordinates and extra target cell type donors
vencodes_all.drop(vencodes_all.columns[[-1, 0]], axis=1, inplace=True)
# Change target cell type values to 1 (active). Files may have been generated with TPM values.
vencodes_all[vencodes_all.columns[-1]] = vencodes_all[vencodes_all.columns[-1]].map(lambda x: 1)
# Calculate percentage of active RE for each column (each cell type)
vencode_collapsed = vencodes_all.apply(pd_u.series_frequency, axis=0, value=1)
# Write to file
vencode_collapsed.to_csv(os.path.join(files_path, "Collapsed REs-prostCancer.csv"), sep=";")
