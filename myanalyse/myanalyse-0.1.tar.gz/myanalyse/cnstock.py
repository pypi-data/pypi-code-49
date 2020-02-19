import os
import numpy as np
import pandas as pd
import datetime
from jqdatasdk import *
acc_jq = os.environ["acc_jq"]
passwd_jq = os.environ["passwd_jq"]
auth(acc_jq,passwd_jq)

def get_growth(code):
    q = query(finance.STK_COMPANY_INFO.industry_id).filter(finance.STK_COMPANY_INFO.code==code)
    industry = finance.run_query(q).iloc[0,0]
    financeIndustry = ["J66","J67","J68","J69"]
    if ( industry in  financeIndustry ) :
        q1 = query(finance.FINANCE_INCOME_STATEMENT.report_date,
                   finance.FINANCE_INCOME_STATEMENT.operating_revenue,
                   finance.FINANCE_INCOME_STATEMENT.net_profit,
                   finance.FINANCE_INCOME_STATEMENT.np_parent_company_owners
                   ).filter(finance.FINANCE_INCOME_STATEMENT.code == code,
                   finance.FINANCE_INCOME_STATEMENT.end_date.ilike('_____12-31'), 
                   finance.FINANCE_INCOME_STATEMENT.report_type==0)
        df1 = finance.run_query(q1)
        q2 = query(finance.FINANCE_INCOME_STATEMENT_PARENT.report_date,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.operating_revenue,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.net_profit,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.np_parent_company_owners
                   ).filter(finance.FINANCE_INCOME_STATEMENT_PARENT.code == code ,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.end_date.ilike('_____12-31'), 
                   finance.FINANCE_INCOME_STATEMENT_PARENT.report_type==0)
        df2 = finance.run_query(q2)
        df2.rename(columns={'operating_revenue':'operating_revenue_parent', 
               'np_parent_company_owners':'np_parent_company_owners_parent'}, inplace = True)
    else :
        q1 = query(finance.STK_INCOME_STATEMENT.report_date,
                   finance.STK_INCOME_STATEMENT.total_operating_revenue,
                   finance.STK_INCOME_STATEMENT.net_profit,
                   finance.STK_INCOME_STATEMENT.np_parent_company_owners
                   ).filter(finance.STK_INCOME_STATEMENT.code == code ,
                   finance.STK_INCOME_STATEMENT.end_date.ilike('_____12-31'), 
                   finance.STK_INCOME_STATEMENT.report_type==0)
        df1 = finance.run_query(q1)
        q2 = query(finance.STK_INCOME_STATEMENT_PARENT.report_date,
                   finance.STK_INCOME_STATEMENT_PARENT.total_operating_revenue,
                   finance.STK_INCOME_STATEMENT_PARENT.net_profit,
                   finance.STK_INCOME_STATEMENT_PARENT.np_parent_company_owners
                   ).filter(finance.STK_INCOME_STATEMENT_PARENT.code == code ,
                   finance.STK_INCOME_STATEMENT_PARENT.end_date.ilike('_____12-31'), 
                   finance.STK_INCOME_STATEMENT_PARENT.report_type==0)
        df2 = finance.run_query(q2)
        df2.rename(columns={'total_operating_revenue':'total_operating_revenue_parent', 
               'net_profit':'net_profit_parent',
               'np_parent_company_owners':'np_parent_company_owners_parent'}, inplace = True)
    df = df1.join(df2.set_index('report_date'),on='report_date',how='outer')
    back = df 
    df = pd.concat([df.iloc[:,0],df.iloc[:,1:].pct_change(fill_method=None)],axis=1)
    colnum = len(df.columns)
    rownum = len(df)
    for colid in range(1,colnum):
        for rowid in range(rownum):
            if not(pd.isna(df.iloc[rowid,colid])):
                df.iloc[rowid,colid] = str(round(df.iloc[rowid,colid]*100,0)) + "%"
    return  {"primitive":back,"growth":df}


def get_pe_year(code):
    data_growth = get_growth(code)
    date = data_growth["primitive"]["report_date"]
    market_cap = pd.DataFrame(data=None,index=range(len(date)) ,columns=['report_date','market_cap'], dtype=None)
    for i in range(len(date)):
        q = query(valuation.market_cap).filter(valuation.code == code)
        y = get_fundamentals(q,date=date[i])
        if len(y) == 0 :
            market_cap.iloc[i,1] = np.nan
        else:
            market_cap.iloc[i,1] = y['market_cap'][0]
        market_cap.iloc[i,0] = date[i]
    raw = data_growth['primitive']
    df = raw.join(market_cap.set_index('report_date'),on='report_date',how='outer')
    df["pe"] = df["market_cap"]*100000000/df["np_parent_company_owners"]
    df["pe"] = df["pe"].apply(lambda x:round(x,2))
    df["pe_parent"] = df["market_cap"]*100000000/df["np_parent_company_owners_parent"]
    df["pe_parent"] = df["pe_parent"].apply(lambda x:round(x,2))
    return df


def get_pe_ttm(code):
    '''
       没有使用综合收益
    '''
    result = pd.DataFrame(data=None,index=range(1) ,columns=['report_date','pe_ttm','pe_ttm_parent'], dtype=None)
    today = datetime.date.today().strftime("%Y-%m-%d")    
    query_market_cap = query(valuation.market_cap).filter(valuation.code == code) 
    market_cap = get_fundamentals(query_market_cap)
    data = get_growth(code)['primitive']
    report_date = list(data['report_date'])[-1]

    query_ttm = query(valuation.pe_ratio).filter(valuation.code == code)
    pe_ttm = round(get_fundamentals(query_ttm).iloc[0,0],2)

    query_attr = query(finance.STK_COMPANY_INFO.industry_id).filter(finance.STK_COMPANY_INFO.code==code)
    industry = finance.run_query(query_attr).iloc[0,0]
    financeIndustry = ["J66","J67","J68","J69"]
    if ( industry in  financeIndustry ) :
        query_profit_parent = query(finance.FINANCE_INCOME_STATEMENT_PARENT.start_date,
                        finance.FINANCE_INCOME_STATEMENT_PARENT.end_date,
                        finance.FINANCE_INCOME_STATEMENT_PARENT.np_parent_company_owners).filter(
                        finance.FINANCE_INCOME_STATEMENT_PARENT.code == code,
                        finance.FINANCE_INCOME_STATEMENT_PARENT.report_date < today,
                        finance.FINANCE_INCOME_STATEMENT_PARENT.report_type== 0)
    else :
        query_profit_parent = query(finance.STK_INCOME_STATEMENT_PARENT.start_date,
                        finance.STK_INCOME_STATEMENT_PARENT.end_date,
                        finance.STK_INCOME_STATEMENT_PARENT.np_parent_company_owners).filter(
                        finance.STK_INCOME_STATEMENT_PARENT.code == code,
                        finance.STK_INCOME_STATEMENT_PARENT.report_date < today,
                        finance.STK_INCOME_STATEMENT_PARENT.report_type== 0)
    df = finance.run_query(query_profit_parent)
    if len(df) >= 7 :
        raw = df.iloc[-7:,]
        raw.index = range(0,7)
        flag = [0,0,0,0]
        date_list = raw['end_date'].apply(lambda x:x.strftime("%Y-%m-%d"))[-4:]
        earnings =  list(raw['np_parent_company_owners'])
        for id,item in enumerate(list(date_list)):
            if item[5:]  == '03-31':
                flag[id] = "q1"
            elif  item[5:]  == '06-30':
                flag[id] = "q2"
            elif  item[5:]  == '09-30':
                flag[id] = "q3"
            elif  item[5:]  == '12-31':
                flag[id] = "q4"
        if flag == ['q1','q2','q3','q4']:
            earning = earnings[-1]
        elif flag == ['q2','q3','q4','q1']:
           earning = earnings[-1] + earnings[-2] - earnings[-5]
        elif flag == ['q3','q4','q1','q2']:
           earning = earnings[-1] + earnings[-3] - earnings[-5]
        elif flag == ['q4','q1','q2','q3']:
           earning = earnings[-1] + earnings[-4] - earnings[-5]
        pe_ttm_parent = market_cap*100000000/earning
        result['pe_ttm_parent'] = round(pe_ttm_parent,2)
    else:
        result['pe_ttm_parent'] = np.nan 
    result['report_date'] = report_date
    result['pe_ttm'] = pe_ttm
    return result


def get_roe(code):
    result = pd.DataFrame(data=None,index=range(1) ,columns=['report_date','pe_ttm','pe_ttm_parent'], dtype=None)
    today = datetime.date.today().strftime("%Y-%m-%d")    
    query_attr = query(finance.STK_COMPANY_INFO.industry_id).filter(finance.STK_COMPANY_INFO.code == code)
    industry = finance.run_query(query_attr).iloc[0,0]
    financeIndustry = ["J66","J67","J68","J69"]
    if ( industry in  financeIndustry ) :
        query_profit = query(finance.FINANCE_INCOME_STATEMENT.report_date,
                      finance.FINANCE_INCOME_STATEMENT.np_parent_company_owners,
                      ).filter(
                      finance.FINANCE_INCOME_STATEMENT.code == code,
                      finance.FINANCE_INCOME_STATEMENT.report_type== 0)
        query_asset = query(finance.FINANCE_BALANCE_SHEET.report_date,
                            finance.FINANCE_BALANCE_SHEET.total_assets,
                            finance.FINANCE_BALANCE_SHEET.total_owner_equities
                            ).filter(
                            finance.FINANCE_BALANCE_SHEET.code == code,
                            finance.FINANCE_BALANCE_SHEET.report_type== 0)
        query_profit_parent = query(finance.FINANCE_INCOME_STATEMENT_PARENT.report_date,
                             finance.FINANCE_INCOME_STATEMENT_PARENT.np_parent_company_owners,
                             ).filter(
                             finance.FINANCE_INCOME_STATEMENT_PARENT.code == code,
                             finance.FINANCE_INCOME_STATEMENT_PARENT.report_type== 0)
        query_asset_parent = query(finance.FINANCE_BALANCE_SHEET_PARENT.report_date,
                                   finance.FINANCE_BALANCE_SHEET_PARENT.total_assets,
                                   finance.FINANCE_BALANCE_SHEET_PARENT.total_owner_equities
                                   ).filter(
                                   finance.FINANCE_BALANCE_SHEET_PARENT.code == code,
                                   finance.FINANCE_BALANCE_SHEET_PARENT.report_type== 0)
    else :
        query_profit = query(finance.STK_INCOME_STATEMENT.report_date,
                      finance.STK_INCOME_STATEMENT.np_parent_company_owners,
                      ).filter(
                      finance.STK_INCOME_STATEMENT.code == code,
                      finance.STK_INCOME_STATEMENT.report_type== 0)
        query_asset = query(finance.STK_BALANCE_SHEET.report_date,
                      finance.STK_BALANCE_SHEET.total_assets,
                      finance.STK_BALANCE_SHEET.total_owner_equities
                      ).filter(
                      finance.STK_BALANCE_SHEET.code == code,
                      finance.STK_BALANCE_SHEET.report_type== 0)
        query_profit_parent = query(finance.STK_INCOME_STATEMENT_PARENT.report_date,
                             finance.STK_INCOME_STATEMENT_PARENT.np_parent_company_owners,
                             ).filter(
                             finance.STK_INCOME_STATEMENT_PARENT.code == code,
                             finance.STK_INCOME_STATEMENT_PARENT.report_type== 0)
        query_asset_parent = query(finance.STK_BALANCE_SHEET_PARENT.report_date,
                                   finance.STK_BALANCE_SHEET_PARENT.total_assets,
                                   finance.STK_BALANCE_SHEET_PARENT.total_owner_equities
                                   ).filter(
                                   finance.STK_BALANCE_SHEET_PARENT.code == code,
                                   finance.STK_BALANCE_SHEET_PARENT.report_type== 0)
    df1 = finance.run_query(query_profit)
    df2 = finance.run_query(query_asset)
    df3 = finance.run_query(query_profit_parent)
    df4 = finance.run_query(query_asset_parent)
    df = df1.join(df2.set_index('report_date'),on='report_date',how='outer')
    df['roa'] = df['np_parent_company_owners'] / df['total_assets']
    df['roa'] = df['roa'].apply(lambda x: str(round(x*100,2))+'%' if np.isnan(x) == False else x)
    df['roe'] = df['np_parent_company_owners'] / df['total_owner_equities']
    df['roe'] = df['roe'].apply(lambda x: str(round(x*100,2))+'%' if np.isnan(x) == False else x)
    return df  
