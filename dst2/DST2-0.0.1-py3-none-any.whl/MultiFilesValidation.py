
""" 2files Checks
This File manages the differences between files. For example what was added to the new file
and what was deleted in the new file
"""

import pandas as pd
import numpy as np
from DST2.core_validations import build_index
from DST2.SingleColumnValidation import get_row_size,get_column_size

def files_comparison(dfsuper, dfsub, indexField):
    """
    dfsuper - dfsub : returns rows that exist in dfsuper and not in dfsub
    Returns rows that exist in dfsuper and not dfsub. This can be used for knowing the additions and deletions.
    :param df1: dataframe to make the subtract
    :param df2: dataframe to be subtracted.
    :param indexField: The index of the dataframe example company ID
    :return: len(dfReport),dfReport
    """
    dfsuper1 = dfsuper.copy()
    dfsub1 = dfsub.copy()
    if type(indexField) is list:
        dfsuper1, main_index = build_index(dfsuper1, indexField)  # for Old
        dfsub1, main_index = build_index(dfsub1, indexField)  # for New
    else:
        main_index = indexField

    dfsuper1=dfsuper1.set_index(main_index)
    dfsub1=dfsub1.set_index(main_index)
    dfReport = dfsuper1[~dfsuper1.index.isin(dfsub1.index)]
    return len(dfReport), dfReport,(len(dfReport)/len(dfsuper1))*100


def file_info(dfOld,dfNew):
    """
    Returns the number of rows in both the new and old file
    :param dfOld: Old file
    :param dfNew: Current file
    :return: dataframe of report
    """
    dfOld_report = get_row_size(dfOld)
    dfNew_report = get_row_size(dfNew)

    #Report
    dfReport = pd.concat([dfNew_report, dfOld_report], axis=1)
    dfReport.columns = ['Current File', 'Previous File']

    return dfReport

def file_columns(dfOld,dfNew):
    """
    Returns the number of rows in both the new and old file
    :param dfOld: Old file
    :param dfNew: Current file
    :return: dataframe of report
    """
    dfOld_report = get_column_size(dfOld)
    dfNew_report = get_column_size(dfNew)

    #Report
    dfReport = pd.concat([dfNew_report, dfOld_report], axis=1)
    dfReport.columns = ['Current File', 'Previous File']

    return dfReport







