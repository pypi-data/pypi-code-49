
"""
This file helps in creating the excel reports
"""

import pandas as pd
import numpy as np
from datetime import datetime
from DST2.core_validations import get_today_date



class Report(object):
    """
    Prepares files for reporting
    """
    def __init__(self,excel_file_name):
        """
        Constructor files
        :param file_name: XXX_comparison
        """
        self.report_name = str(excel_file_name)+'_'+get_today_date()+'.xlsx'
        self.writer = pd.ExcelWriter(self.report_name,engine='xlsxwriter') #Writer
        self.sheets = []
        self.insame_sheet = []

    def add_to_report(self,sheet):
        """
        Adds Sheet to report.
        :param report:
        :return:
        """
        self.sheets.append(sheet)

    def save_report(self):
        """
        Concats and writes all report to an excel file.
        :return: Excel file and notification
        """
        if len(self.sheets)>0:
            for sheet in self.sheets:
                sheet.default_df.to_excel(self.writer,index=sheet.keep_index, sheet_name=sheet.sheet_name, na_rep='N/A',startrow=sheet.start_row,startcol=sheet.start_col)

            self.writer.save()
        else:
            pass


class Sheet(object):
    """
    Prepares Sheet to be added to the Report.
    """
    def __init__(self,sheet_name,df,keep_index=False,start_row=1,start_col=1):
        """
        Sheet Constructor files
        :return:
        """
        self.sheet_name = sheet_name
        self.default_df = df
        self.keep_index = keep_index
        self.start_row = start_row - 1 #To obey zero indexing
        self.start_col = start_col - 1 #To obey zero indexing



    def concat_to_sheet(self,df):
        """
        Appends dataframe
        :param df:
        :return:
        """

        self.default_df.append(df)









