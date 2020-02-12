"""
Manages  core functions the module
"""

#import modules to be used
import pandas as pd
import numpy as np
from datetime import datetime
import re
import math


#nalist = ['No data', 'N/A'] #Blank list..
#valid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' #alpha-numeric

def valid_characters():
    """
    Returns values the valid characters accepted by Identifiers
    :return: string character
    """
    valid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@*'  # alpha-numeric
    return valid


def get_default_column_strings():
    """
    Returns a list of all expected default strings in the GA
    :return: list of default strings
    """
    default_strings = ['No data','Research in progress','Framework not applicable','No Access','N/A',np.nan]
    return default_strings

def is_isin(isin_value):
    """
    Validates that ISIN Column is in the right format.
    12 digits for ISIN – apply this rule on the file.
    :param isin_value: df['ISIN']
    :return: validation flag
    """
    if type(isin_value) != str:
        return True
    elif type(isin_value) == str and len(isin_value) == 12:
        if (all([(i in valid_characters()) for i in isin_value])):
            if (any([(i in valid_characters()) for i in isin_value])):
                return False
    if isin_value in get_default_column_strings():
        return True
    else:
        return True




def is_cusip(cusip_value):
    """
    Validates that CUSIP Column is in the right format.
    9 digits for CUSIP – apply this rule on the file
    :param df: df['CUSIP']
    :return: validation flag
    """
    if type(cusip_value) == int:
        if 5 < len(str(cusip_value)) < 10: #previously len(str(x)) == 9:
            return False
        else:
            return True
    elif type(cusip_value) == str and len(cusip_value) == 9:
                if(all([(i in valid_characters()) for i in cusip_value])):
                    if(any([(i in valid_characters()) for i in cusip_value])):
                        return False
    if cusip_value in get_default_column_strings():
        return True
    else:
        return True


def is_sedol(sedol_value):
    """
    Validates that Sedol Column is in the right format
    :param df: df['Sedol']
    :return: validation flag
    """
    if type(sedol_value) == int:
        if len(str(sedol_value)) == 7:
            return False
        else:
            return True
    elif type(sedol_value) == str and len(sedol_value) == 7:
                if(all([(i in valid_characters()) for i in sedol_value])):
                    if(any([(i in valid_characters()) for i in sedol_value])):
                        return False
    if sedol_value in get_default_column_strings():
        return True
    else:
        return True

def replaceScore(x):
    """
    Replace score to 0 if the type is string.
    """
    try:
        new_x = float(x) #Cast value to float
    except:
        new_x = str(x) #Else recognize a string

    if type(new_x) == str:
        return 0
    else:
        return new_x

def bigdiff(x,delta):
    """
    Return True is absolute score difference is greater than delta
    """
    if np.abs(x) > delta:
        return True
    elif np.abs(x) < delta:
        return False
    else:
        return True

def get_today_date():
    """
    Returns the date as a string
    :return: string(date)
    """
    today = datetime.today()
    today = today.strftime('%d-%m-%y')
    return str(today)

def build_index(df,index_list):
    """
    Build a new Index for the DataFrame
    :param df: dfOld or New
    :return: a new dataframe
    """
    df1 = df.copy()
    #Convert Columns to string type
    df1['General ID'] = ""
    for x in index_list:
        df1['General ID'] = df1['General ID'].map(str)+df1[x].map(str)+"-"

    #apply rstrip to the combined index column
    df1['General ID'] = df1['General ID'].str.rstrip('-')
    #print(df1.head())
    return df1,'General ID'

def search_columns(search_query,all_columns):
    """
    Return column names
    :param search_query: isins, cusip, sedol
    :param columns: list of all columns in a file
    :return: column or columns
    """
    #Check if search query instance is a list
    if isinstance(search_query,list):
        search_result = [col for sq in search_query for col in all_columns if str(sq).lower() in str(col).lower()]
        return search_result
    else:
        search_result = [col for col in all_columns if str(search_query).lower() in str(col).lower()]
        return search_result



def list_intersection(lst1, lst2):
    """
    Returns the intersection between 2 lists
    :param lst1: List 1
    :param lst2: List 2
    :return: List of intersection
    """
    return list(set(lst1) & set(lst2))

def keyword_remove(search_query,all_columns):
    """
    Remove all columns containing the list of keywords
    :param search_query: List1 or keyword
    :param all_columns: List2
    :return: list
    """
    final_result = []
    if isinstance(search_query,list):

        for e in all_columns:
            eligible_flag = True
            for q in search_query:
                if str(q).lower() in str(e).lower():
                    eligible_flag=False
                else:
                    pass
            if eligible_flag is True:
                final_result.append(e)
            else:
                pass
        return final_result
    else:
        final_result = [col for col in all_columns if str(search_query).lower() not in str(col).lower()]
        return final_result




















