# -*- coding: utf-8 -*-
'''
  To  analyse stock ,basic information
'''
import analyse
import os
import numpy as np
import pandas as pd
import datetime
from jqdatasdk import *
acc_jq = os.environ["acc_jq"]
passwd_jq = os.environ["passwd_jq"]

auth(acc_jq,passwd_jq)

def rounddf(df):
    df_print = df.copy(deep=True)
    collen = df.shape[1]
    for item in range(collen):
        if df.iloc[:,item].dtype == 'float64':
            df.iloc[:,item] = df.iloc[:,item].apply(lambda x : round(x,4) \
                    if np.isnan(x) == False  else x)
            df_print.iloc[:,item] = df_print.iloc[:,item].apply(lambda x : \
                    str(round(x*100,2)) + '%' if np.isnan(x) == False  else x)
    return {'raw':df,'print':df_print}


def get_growth(code=None,type=None):
    '''
    get_growth(code=None,type=None) code contain surfix,type :
       year,quarter(当期的数值，非累计)
    return a dictionary,  {'raw':data,'growth':df}
    '''
    if type == "year":
        data = analyse.info.get_info(code,"year")['peryear']
    elif type == "quarter":
        data = analyse.info.get_info(code,"quarter")['perquarter']
    df = pd.concat([data.iloc[:,0],data.iloc[:,1:].pct_change(fill_method=None)],\
                   axis=1)
    colnum = len(df.columns)
    rownum = len(df)
    for colid in range(1,colnum):
        for rowid in range(rownum):
            if not(pd.isna(df.iloc[rowid,colid])):
                df.iloc[rowid,colid] = str(round(df.iloc[rowid,colid]*100,0)) + "%"
    return {'raw':data,'growth':df}


def get_pe(code=None,type=None):
    '''
    get_pe(code=None,type=None) code contain surfix,
            type :year,quarter(当期的数值，非累计)
    return a dictionary,  {'raw':df,'pe':df_pe} 
    '''
    if  type == "static" :
        df_pe = pd.DataFrame(data=None,columns=['report_date','pe','pe_parent'],\
                             dtype=None)
        df  = analyse.info.get_info(code=code,type='year')['peryear']
        df_pe['report_date'] = df['report_date']
        df_pe["pe"] = df["market_cap"]*100000000/df["np_parent_company_owners"]
        df_pe['pe'] = df_pe["pe"].apply(lambda x:round(x,2))
        df_pe["pe_parent"] = df["market_cap"]*100000000/\
                             df["np_parent_company_owners_parent"]
        df_pe['pe_parent']  = df_pe['pe_parent'].apply(lambda x:round(x,2))
    elif  type == "ttm":
        df_pe = pd.DataFrame(data=None,\
                             columns=['report_date','pe_ttm','pe_ttm_parent'],\
                             dtype=None)
        df  = analyse.info.get_info(code=code,type='quarter')['perquarter']
        df_pe['report_date'] = df['report_date']
        earnings_list = list(df['np_parent_company_owners'])
        earnings_list_parent = list(df['np_parent_company_owners_parent'])
        market_cap_list = list(df['market_cap'])
        for ind in range(len(df)):
            if ind == 0 :
                earnings =  earnings_list[ind]*4
                earnings_parent =  earnings_list_parent[ind]*4
            elif ind == 1 :
                earnings =  sum(earnings_list[0:ind+1])*2
                earnings_parent =  sum(earnings_list_parent[0:ind+1])*2
            elif ind == 2 :
                earnings =  sum(earnings_list[0:ind+1])*4/3
                earnings_parent =  sum(earnings_list_parent[0:ind+1])*4/3
            else :
                earnings =  sum(earnings_list[ind-3:ind+1])
                earnings_parent =  sum(earnings_list_parent[ind-3:ind+1])
            pe_ttm = market_cap_list[ind]*100000000/earnings
            pe_ttm_parent = market_cap_list[ind]*100000000/earnings_parent
            df_pe['pe_ttm'][ind] = round(pe_ttm,2)
            df_pe['pe_ttm_parent'][ind] = round(pe_ttm_parent,2)
    return  {'raw':df,'pe':df_pe}


def get_return(code=None,mtype=None):
    '''
    return a dictionary,  {'raw':df,'pe':df_pe} 
    '''
    #import numpy as np
    if mtype == 'static':
        result = pd.DataFrame(data=None,\
                        columns=['report_date','roa','roa_parent','roe','roe_parent'],\
                        dtype=None)
        df = analyse.info.get_info(code,type='year')['peryear']
        result['report_date'] = df['report_date']
        result['roa'] = df['np_parent_company_owners'] / df['total_assets']
        result['roa_parent'] = df['np_parent_company_owners_parent'] / \
                               df['total_assets_parent']
        result['roe'] = df['np_parent_company_owners'] / df['total_owner_equities']
        result['roe_parent'] = df['np_parent_company_owners_parent'] / \
                               df['total_owner_equities_parent']
    elif mtype == 'ttm':
        df = analyse.info.get_info(code,type='quarter')['perquarter']
        result = pd.DataFrame(data=None,\
                 columns=\
                 ['report_date','roa_ttm','roa_ttm_parent','roe_ttm','roe_ttm_parent'],\
                 dtype='object')
        result['report_date'] = df['report_date']
        for ind in range(len(df)):
            if ind == 0 :
                net_p = df['np_parent_company_owners'][ind]*4
                np_parent = df['np_parent_company_owners_parent'][ind]*4
                assets = df['total_assets'][ind]
                assets_parent = df['total_assets_parent'][ind]
                equities = df['total_owner_equities'][ind]
                equities_parent = df['total_owner_equities_parent'][ind]
            elif ind == 1 :
                net_p = df['np_parent_company_owners'][0:2].sum()*2
                np_parent = df['np_parent_company_owners_parent'][0:2].sum()*2
                assets = df['total_assets'][0:2].mean()
                assets_parent = df['total_assets_parent'][0:2].mean()
                equities = df['total_owner_equities'][0:2].mean()
                equities_parent = df['total_owner_equities_parent'][0:2].mean()
            elif ind == 2 :
                net_p = df['np_parent_company_owners'][0:3].sum()*4/3
                np_parent = df['np_parent_company_owners_parent'][0:3].sum()*4/3
                assets = df['total_assets'][0:3].mean()
                assets_parent = df['total_assets_parent'][0:3].mean()
                equities = df['total_owner_equities'][0:3].mean()
                equities_parent = df['total_owner_equities_parent'][0:3].mean()
            else :
                net_p = df['np_parent_company_owners'][ind-3:ind+1].sum()
                np_parent = df['np_parent_company_owners_parent'][ind-3:ind+1].sum()
                assets = df['total_assets'][ind-3:ind+1].mean()
                assets_parent = df['total_assets_parent'][ind-3:ind+1].mean()
                equities = df['total_owner_equities'][ind-3:ind+1].mean()
                equities_parent = df['total_owner_equities_parent'][ind-3:ind+1].mean()
            result['roa_ttm'][ind] = net_p/assets
            result['roa_ttm_parent'][ind] = np_parent/assets_parent
            result['roe_ttm'][ind] = net_p/equities
            result['roe_ttm_parent'][ind] = np_parent/equities_parent
        #result.iloc[:,1] = result.iloc[:,1].astype('float')
        #result.iloc[:,2] = result.iloc[:,2].astype('float')
        #result.iloc[:,3] = result.iloc[:,3].astype('float')
        #result.iloc[:,4] = result.iloc[:,4].astype('float')
    return_raw = rounddf(result)['raw']
    return_print = rounddf(result)['print']
    return  {'raw':df,'return_raw':return_raw,'return_print':return_print}
        

