
"""
This file manages QA operations only on columns between 2 files.
"""
import pandas as pd
import numpy as np
from DST2.core_validations import replaceScore,bigdiff,build_index,search_columns
from DST2.SingleColumnValidation import general_column_report,categorical_column_report



def get_company_name(ID,df):
    """
    Get company name given ID.
    """
    result = df[df['Company ID']==ID]
    return result['Company Name']


def columns_comparison(dfOld, dfNew, cols, indexField):
    """
    Returns the length of Column differences and the column differences
    :param dfOld: Previous deliverable
    :param dfNew: Current deliverable
    :param cols: Columns of Interest
    :param indexField : Index columns
    :return: len(dfReport), dfReport , uniqueChanges
    """
    ##Getting indexes that intersects between both rows
    #concating cols with indexField
    #Fixing the index
    #idx = indexField
    dfOld1 = dfOld.copy()
    dfNew1 = dfNew.copy()

    #if

    #print(dfNew1.head())
    #print(dfOld1.head())
    #print(dfNew1)
    #If indexfield is made up of more than 1 color
    if type(indexField) is list:
        dfOld1,main_index =  build_index(dfOld1,indexField) #for Old if index is a list
        dfNew1,main_index =  build_index(dfNew1,indexField) #for New if index is a list


    else:
        main_index = indexField

    #print(dfNew1.columns)

    # Ensure the indexfield is a string
    dfNew1[main_index] = dfNew1[main_index].astype(str)
    dfOld1[main_index] = dfOld1[main_index].astype(str)

    #print(dfOld1.head())
    newcols = [main_index]+cols
    dfOld1 = dfOld1[newcols].astype(str)  # Taking specified cols
    dfNew1 = dfNew1[newcols].astype(str) # Taking specified cols

    #fill NA with No data
    dfOld1 = dfOld1.fillna('No data')
    dfNew1 = dfNew1.fillna('No data')

    # set index and collect intersections
    dfNew1.set_index(main_index,inplace=True)
    dfOld1.set_index(main_index, inplace=True)
    #print(dfNew1.head())
    #print(dfOld1.index)
    dfNew1 = dfNew1[dfNew1.index.isin(dfOld1.index)]
    dfOld1 = dfOld1[dfOld1.index.isin(dfNew1.index)]
    #print(dfNew1.head())
    #print(dfOld1.head())
    #Sort index
    dfNew1.sort_index(inplace=True)
    dfOld1.sort_index(inplace=True)

    #print(dfNew1.head())

    try: # Handling this ValueError: Can only compare identically-labeled DataFrame objects

        df = dfOld1 != dfNew1 #changes check
        #print(df)
        linii_mod_stacked = df.stack()  # Converts row to column
        changed = linii_mod_stacked[linii_mod_stacked]
        changed.index.names = [main_index, 'Column']  # Prepares new index
        #print(changed) for testing
        difference_locations = np.where(dfOld1 != dfNew1)
        changed_from = dfOld1.values[difference_locations]
        changed_to = dfNew1.values[difference_locations]
        data = pd.DataFrame({'Previous': changed_from, 'Current': changed_to}, index=changed.index)
        #
        data = data.reset_index()
        #print(data.head()) for testing
        data = data[~(data['Column'].isin([main_index]))]
        try:
            try:

                #Append company name
                name_col = search_columns('name',dfNew.columns.tolist())
                new_df = dfNew[[indexField, name_col[0]]].astype(str)
                # Perform a merge
                data = data.merge(new_df, how='left', on=indexField)
                #print(data.head())
                #Rearrange columns
                data = data[[indexField,name_col[0],'Column','Previous','Current']]
                return len(data), data,(len(data[main_index].unique())/len(dfNew1))*100,len(dfNew1)
            except:
                return len(data), data, (len(data[main_index].unique()) / len(dfNew1)) * 100, len(dfNew1)
        except ZeroDivisionError:
            error_message = {'ID': "Error Info", 'Reason 1': "Files could contain duplicate IDs or indexes",
                             'Reason 2': "Files are possibly same",'Reason 3': "ID column has different types"}
            data = pd.DataFrame(error_message, columns=['ID', 'Reason 1', 'Reason 2','Reason 3'],index=[0])
            return 0, data, 0, 0


    except ValueError:
        #Return empty dataframe
        error_message = {'ID':"Error Info",'Reason 1':"Files could contain duplicate IDs or indexes", 'Reason 2': "Files are possibly same",'Reason 3': "ID column has different types"}
        data = pd.DataFrame(error_message,columns=['ID','Reason 1','Reason 2','Reason 3'],index=[0])

        return 0,data,0,0





def scores_comparison(dfOld, dfNew, col, indexField, delta=5):
    """
    Returns the length of Column differences and the column differences
    :param dfOld: old score
    :param dfNew: new score
    :param col: score column
    :param indexField: index field
    :param delta: delta difference and default = 5
    :return: len(scores_data),data, percentage_change
    """

    _,scores_data,_ ,report_size= columns_comparison(dfOld, dfNew, col, indexField) #Gets the changes on that column

    # Obtain delta values
    if not scores_data.empty:

        scores_data['delta'] = np.nan
        #replace scores

        scores_data['Current'] = scores_data['Current'].map(replaceScore)
        scores_data['Previous'] = scores_data['Previous'].map(replaceScore)
        #Fillna
        scores_data.fillna(0,inplace=True)
        #Obtain delta values
        scores_data['delta'] = scores_data['Current'] - scores_data['Previous']


        #scores_data[''] = np.vectorize(bigdiff)(scores_data['delta'],delta) #Applying the function bigdiff
        scores_data['bigdiff'] = scores_data.apply(lambda x:bigdiff(x['delta'],delta),axis=1)

        #Get the scores with difference more than the delta threshold
        scores_data =  scores_data[scores_data['bigdiff'] == True]
        #print(scores_data.head())
        #Drop the bigdiff Column
        scores_data = scores_data.drop('bigdiff',axis=1)
        real_size = len(dfNew)*len(col)

        return len(scores_data), scores_data, (len(scores_data[indexField].unique())/report_size)*100 #return: len(scores_data),data, percentage_change
    else:
        scores_data['delta'] = np.nan
        return 0,scores_data,0



def summary_general_comparison(dfOld, dfNew):
    """
    Concats the report for column summary comparison
    :param dfOld: Old file
    :param dfNew: New file
    :return: dfReport
    """
    dfOld_report = general_column_report(dfOld) #Get Columns report old file
    dfNew_report = general_column_report(dfNew) #Get Columns report for new file

    #Report
    dfReport = pd.concat([dfNew_report,dfOld_report],sort=True, axis=1)
    dfReport.columns=['Current File', 'Previous File']

    return dfReport


def summary_categorical_comparison(dfOld, dfNew):
    """
    Concats the report for column summary comparison
    :param dfOld:
    :param dfNew:
    :return:
    """
    dfOld_report = categorical_column_report(dfOld) #Get Columns report old file
    dfNew_report = categorical_column_report(dfNew) #Get Columns report for new file

    #Report
    dfReport = pd.concat([dfNew_report,dfOld_report],sort=True,axis=1)
    #print(dfReport)
    dfReport.columns=['Current File', 'Previous File']


    return dfReport

def check_new_columns(dfOld,dfNew):
    """
    Returns differences in columns in the 2 reports
    :param dfOld: Old file
    :param dfNew: New file
    :return: A dataframe
    """
    old_cols = dfOld.columns.tolist()
    new_cols = dfNew.columns.tolist()

    #Get cols
    cols_in_old = list(set(old_cols) - set(new_cols))
    tag_list_old= ['Old']*len(cols_in_old) #Repeating old n times
    #Zip the values
    cols_in_old = list(zip(cols_in_old,tag_list_old))

    cols_in_new = list(set(new_cols) - set(old_cols))
    tag_list_new = ['New']*len(cols_in_new)
    cols_in_new = list(zip(cols_in_new,tag_list_new))

    all_cols = cols_in_new + cols_in_old
    #Convert to DataFrames
    if len(all_cols)>0:
        df_final = pd.DataFrame(all_cols,columns=['Column','File'])
        return df_final
    else:
        return None
























