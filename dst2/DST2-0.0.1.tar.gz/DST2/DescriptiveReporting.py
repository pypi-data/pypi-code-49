"""
Responsible for measuring the changes and more
"""

import pandas as pd
import numpy as np





class SummaryReport(object):
    """
    This class handles the summary reports.
    """
    def __init__(self):
        """
        Summary report Constructor
        """
        self.df = pd.DataFrame()

    def add_summary_report(self,summary_info,summary_report):
        """
        Appends summary report
        :return:
        """
        df_temp = summary_report
        df_temp=df_temp.reset_index()
        df_temp.columns = ['Summary Info','Current File','Previous File']
        #Append a string to the summary info column
        df_temp['Summary Info'] =  df_temp['Summary Info'].astype(str)
        df_temp = df_temp.fillna(0)
        #print(df_temp)
        self.df=self.df.append(df_temp)
        #print(self.df)

    def get_summary_report(self):
        """
        Returns the Summary Report.
        :return: self.df
        """
        return self.df





class PercentageReport(object):
    """
    This class handles the percentage report.
    """
    def __init__(self):
        """
        Percentage Change Constructor.
        """
        self.df = pd.DataFrame()

    def add_percentage_report(self,value_name,counts_or_threshold,percent_value):
        """

        :param value_name: name of the percentage change
        :param percent_value: the percent value
        :return:
        """
        self.df = self.df.append({'Change Type': value_name, 'Counts/Threshold': counts_or_threshold,'Percentage Value': str(round(percent_value,3))+ "%"}, ignore_index=True)


    def get_percentage_report(self):
        """
        Returns the percentage report dataFrame
        :return: self.df
        """
        return self.df

class ErrorReport(object):
    """
    This class handles Error report
    """
    def __init__(self):
        """
        Constructor for error reporting
        """
        self.df = pd.DataFrame()


    def add_error_report(self,error_name,error_count):
        """
        Adds error value to the error report
        :param error_name: # OF ISINS ERROR
        :param error_value:
        :return:
        """
        self.df = self.df.append({'Counts': error_count,'Error Check': error_name}, ignore_index=True)



    def get_error_report(self):
        """
        Returns the error report dataFrame
        :return: self.df
        """
        try:

            cols = ['Error Check','Counts']
            return self.df[cols]
        except:
            cols = ['Error Check', 'Counts']
            self.df = pd.DataFrame(columns=cols)


