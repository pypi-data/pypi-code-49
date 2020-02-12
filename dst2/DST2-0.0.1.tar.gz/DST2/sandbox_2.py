import DST2.QA as q
import pandas as pd


#dfOld =  pd.read_excel('data_test/Sustainalytics Product Involvement - Full Report - 2017-August_work.xlsx',sheet_name='Active',skiprows=1,encoding='latin-1')
#dfNew = pd.read_excel('data_test/Sustainalytics Product Involvement - Full Report - 2017-September_work.xlsx',sheet_name='Active',skiprows=1,encoding='latin-1')
#dfOld = pd.read_excel('data_test/august.xlsx',sheet_name='Results')
#dfNew = pd.read_excel('data_test/october_1.xlsx',sheet_name='Results')

#dfOld = pd.read_csv('data_test/Blackrock_ESG_CWR_20180123.csv',encoding='latin-1')
#dfNew = pd.read_csv('data_test/Blackrock_ESG_CWR_20190214.csv',encoding='latin-1')

dfOld = pd.read_excel('data_test/Tool MAY.xlsx',sheet_name='MAY',skiprows=[0,2])
dfNew = pd.read_excel('data_test/Tool JUN.xlsx',sheet_name='JUNE',skiprows=[0,2])


indexField = ['CompanyID','CATEGORY OF INVOLVEMENT','PRODUCT INVOLVEMENT AREA']

qa = q.QA_Report("Test_colWespth",dfOld,dfNew,indexField)
#print(dfOld['Company ID'].head())
#print(dfNew['Company ID'].head())
#corp_cols = ['Company Name','Country','Peer Group','Cusip','Exchange','Business Description']

#cols = ['Total ESG Score','Percentile']
#col2 = ['Total ESG Score']
#col3 = ['Percentile']
#qa.perform_qa(all_cols=True)
spec_cols = ['REVENUE RANGE','Company Type','Entity Type','CATEGORY OF INVOLVEMENT','PRODUCT INVOLVEMENT AREA']
qa.perform_qa(columns=spec_cols)
#qa.perform_qa(columns=col2,type='score',delta=10)
#qa.perform_qa(columns=col3,type='score',delta=2)
#qa.perform_qa(type='column',keywords=['level of involvement','standard analysis'])
#Test scores
#qa.perform_column_qa('Does the company meet your screening criteria?')
qa.create_report()