

import pandas as pd
import DST.SingleColumnValidation as occ
import MultiColumnsValidation as tcc
from DST.Reporting import Report,Sheet
from DST import DescriptiveReporting as ovs
import core_validations
#df = pd.read_excel('data_test/QA Test_10052017.xlsx', sheetname='Results')
#df2 = pd.read_excel('data_test/QA Test_29052017.xlsx', sheetname='Results')
#dfOld =  pd.read_csv( 'data_test/Breckinridge Report 2017_06_01_2.csv',encoding='latin-1')
#dfNew = pd.read_csv('data_test/Breckinridge Report 2017_06_15_2.csv',encoding='latin-1')

dfOld = pd.read_excel('data_test/august.xlsx', sheet_name='Results')
#dfNew = pd.read_excel('data_test\GS Wealth Master Screen July 2017.xlsx', sheetname='Results',skiprows=5)
dfNew = pd.read_excel('data_test/october.xlsx', sheet_name='Results')

#dfOld =  pd.read_excel('data_test\Sustainalytics Product Involvement - Full Report - 2017-August_work.xlsx',sheetname='Active',skiprows=1,encoding='latin-1')
#dfNew = pd.read_excel('data_test\Sustainalytics Product Involvement - Full Report - 2017-September_work.xlsx',sheetname='Active',skiprows=1,encoding='latin-1')

#print(dfOld.head())


#print(df.head())
indexField = 'Company ID'
#Meta settings
#indexField = ['ID','Product Involvement Indicator']

#indexField = 'ID'
selected_cols = ['Does the company meet your screening criteria?']
spec_cols = dfOld.columns.tolist()[11:]
#unwanted_cols = ['Company Type','Company Status','Bloomberg Global ID','Bloomberg Unique ID','Company Name'] + spec_cols +[indexField]
#pi_cols = ['Product Involvement Indicator','Category of Involvement ','Revenue Range','% Ownership']
#cols_of_interest =list(set(dfNew.columns.tolist()) - set(unwanted_cols))
#count,dfNew = occ.isin_check(df['ISIN'])

_,df1,_,_=tcc.columns_comparison(dfOld, dfNew, selected_cols,indexField)
#print(df1)

"""
df1 = pd.DataFrame({'A': ['A1', 'A1', 'A2', 'A3'],
                     'B': ['121', '345', '123', '146'],
                     'C': ['K0', 'K1', 'K0', 'K1']})

df2 = pd.DataFrame({'A': ['A1', 'A3'],
                      'BB': ['B0', 'B3'],
                      'CC': ['121', '345'],
                      'DD': ['D0', 'D1']})

print(tcc.check_new_columns(df1,df2))

#print(dfOld['Company ID'].head())
#print(dfNew['Company ID'].head())


_,df1,_,_=tcc.columns_comparison(dfOld, dfNew, pi_cols, indexField)
#d1=tcc.summary_general_comparison(df['Total ESG Score'],df2['Total ESG Score'])
#d2 = tcc.summary_categorical_comparison(df['Company type'],df2['Company type'])
print(df1)
#print(d1)

summary_report = ovs.SummaryReport()
summary_report.add_summary_report('T-ESG',d1)
summary_report.add_summary_report('Company Type',d2)
print(summary_report.get_summary_report())

#print(percent_score)
#print(df1)
#print(d1.append(d2))


df = pd.DataFrame(columns=['ID','in column','in new file','in old file'])
#df['In column'] = pd.np.nan
print(df)
"""
print(core_validations.search_columns('isin',['Social Score',
'Environment Score',
'Environment Score'
]))