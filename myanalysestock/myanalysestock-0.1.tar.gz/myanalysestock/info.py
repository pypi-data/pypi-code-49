# -*- coding: utf-8 -*-
'''
  To  analyse stock ,basic valuation information
  聚宽的季度数据是累计到报告期为止的数据，进行滚动分析时，使用的季度数据
  应当是当期发生的数据,从最近一期往前面计算，最后一期在最下面，因此是从最下面一行开始
      本期发生 = 累计到本期-累计到上期
      一季度数据不用扣减，其他季度如何正好排在第一行，这个季度的实际发生值，将无法计算。
'''
import os
import numpy as np
import pandas as pd
import datetime
from jqdatasdk import *
acc_jq = os.environ["acc_jq"]
passwd_jq = os.environ["passwd_jq"]

auth(acc_jq,passwd_jq)

def get_info(code=None,type=None):
    '''
    get basic info : market_cap,net_profit
    code company symbol in stock market
    type = year or quarter
    the order can't changed:report_date,total_assets,total_owners_equities,
    operating_revenue,net_profit,np_parent_company_owners,
    total_assets_parent,total_owners_equities_parent,
    operating_revenue_parent,net_profit_parent,np_parent_company_owners_parent,
    '''
    query_industry = query(finance.STK_COMPANY_INFO.industry_id).\
                           filter(finance.STK_COMPANY_INFO.code==code)
    industry = finance.run_query(query_industry).iloc[0,0]
    financeIndustry = ["J66","J67","J68","J69"]
    # fiance and other company has different type table
    if ( industry in  financeIndustry ) :
        query_balance = query(finance.FINANCE_BALANCE_SHEET.report_date,
                            finance.FINANCE_BALANCE_SHEET.total_assets,
                            finance.FINANCE_BALANCE_SHEET.total_owner_equities
                            ).filter(
                            finance.FINANCE_BALANCE_SHEET.code == code,
                            finance.FINANCE_BALANCE_SHEET.report_type== 0)
        df_balance = finance.run_query(query_balance)
        query_income = query(finance.FINANCE_INCOME_STATEMENT.report_date,
                   finance.FINANCE_INCOME_STATEMENT.operating_revenue,
                   finance.FINANCE_INCOME_STATEMENT.net_profit,
                   finance.FINANCE_INCOME_STATEMENT.np_parent_company_owners
                   ).filter(finance.FINANCE_INCOME_STATEMENT.code == code,
                   finance.FINANCE_INCOME_STATEMENT.report_type==0)
        df_income = finance.run_query(query_income)
        query_balance_parent = query(finance.FINANCE_BALANCE_SHEET_PARENT.report_date,
                            finance.FINANCE_BALANCE_SHEET_PARENT.total_assets,
                            finance.FINANCE_BALANCE_SHEET_PARENT.total_owner_equities
                            ).filter(
                            finance.FINANCE_BALANCE_SHEET_PARENT.code == code,
                            finance.FINANCE_BALANCE_SHEET_PARENT.report_type== 0)
        df_balance_parent = finance.run_query(query_balance_parent)
        query_income_parent = query(finance.FINANCE_INCOME_STATEMENT_PARENT.report_date,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.operating_revenue,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.net_profit,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.np_parent_company_owners
                   ).filter(finance.FINANCE_INCOME_STATEMENT_PARENT.code == code,
                   finance.FINANCE_INCOME_STATEMENT_PARENT.report_type==0)
        df_income_parent = finance.run_query(query_income)
        df = df_balance.join(df_income.set_index('report_date'),\
                             on='report_date',how='outer')
        df_parent = df_balance_parent.join(df_income_parent.set_index('report_date'),\
                                           on='report_date',how='outer')
        df_parent.rename(columns={'total_assets':'total_assets_parent',
                                  'total_owner_equities':'total_owner_equities_parent',
                                  'operating_revenue':'operating_revenue_parent',
                                  'net_profit':'net_profit_parent',
                                  'np_parent_company_owners':\
                                  'np_parent_company_owners_parent',
                                  },inplace=True)
    else :
        query_balance = query(finance.STK_BALANCE_SHEET.report_date,
                            finance.STK_BALANCE_SHEET.total_assets,
                            finance.STK_BALANCE_SHEET.total_owner_equities
                            ).filter(
                            finance.STK_BALANCE_SHEET.code == code,
                            finance.STK_BALANCE_SHEET.report_type== 0)
        df_balance = finance.run_query(query_balance)
        query_income = query(finance.STK_INCOME_STATEMENT.report_date,
                   finance.STK_INCOME_STATEMENT.total_operating_revenue,
                   finance.STK_INCOME_STATEMENT.net_profit,
                   finance.STK_INCOME_STATEMENT.np_parent_company_owners
                   ).filter(finance.STK_INCOME_STATEMENT.code == code,
                   finance.STK_INCOME_STATEMENT.report_type==0)
        df_income = finance.run_query(query_income)
        query_balance_parent = query(finance.STK_BALANCE_SHEET_PARENT.report_date,
                            finance.STK_BALANCE_SHEET_PARENT.total_assets,
                            finance.STK_BALANCE_SHEET_PARENT.total_owner_equities
                            ).filter(
                            finance.STK_BALANCE_SHEET_PARENT.code == code,
                            finance.STK_BALANCE_SHEET_PARENT.report_type== 0)
        df_balance_parent = finance.run_query(query_balance_parent)
        query_income_parent = query(finance.STK_INCOME_STATEMENT_PARENT.report_date,
                   finance.STK_INCOME_STATEMENT_PARENT.total_operating_revenue,
                   finance.STK_INCOME_STATEMENT_PARENT.net_profit,
                   finance.STK_INCOME_STATEMENT_PARENT.np_parent_company_owners
                   ).filter(finance.STK_INCOME_STATEMENT_PARENT.code == code,
                   finance.STK_INCOME_STATEMENT_PARENT.report_type==0)
        df_income_parent = finance.run_query(query_income_parent)
        df = df_balance.join(df_income.set_index('report_date'),\
                             on='report_date',how='outer')
        df_parent = df_balance_parent.join(df_income_parent.set_index('report_date'),\
                                           on='report_date',how='outer')
        df_parent.rename(columns=
                {'total_assets':'total_assets_parent',
                  'total_owner_equities':'total_owner_equities_parent',
                  'total_operating_revenue':'total_operating_revenue_parent',
                  'net_profit':'net_profit_parent',
                  'np_parent_company_owners':'np_parent_company_owners_parent',
                },inplace=True)
    df = df.join(df_parent.set_index('report_date'),on='report_date',how='outer')
    df = df.sort_values(by='report_date')
    df.reset_index(drop=True, inplace=True)
    all_cap = []
    query_market_cap = query(valuation.market_cap).filter(valuation.code == code) 
    for idate in df['report_date']:
        cap = get_fundamentals(query_market_cap,date=idate)['market_cap']
        if cap.empty:
            all_cap.append(np.nan)
        else:
            all_cap.append(cap[0])
    df['market_cap'] = all_cap
    df.index = df['report_date']
    #必须深度拷贝，后面的运算将修改df,不深度拷贝，raw_df也会变化
    raw_df = df.copy(deep=True)

    if type == "year" :
        df = df[df['report_date'].astype(str).str.contains('12-31')]
        return {"raw":raw_df,"peryear":df}
    elif type == "quarter" :
        row_num = df.shape[0]
        col_num = df.shape[1]
        #对这个df从最后一行往前面进行，因为后面的一行，根据上面一行修改
        #必须先改后面的每行，改完后，固定下来
        for row_id in range(row_num-1,-1,-1):
            if df.iloc[row_id,0].strftime('%Y-%m-%d')[5:]  != '03-31':
                if (row_id - 1 >= 0 and df.iloc[row_id-1,0].strftime('%Y') == \
                                  df.iloc[row_id,0].strftime('%Y')):
                    df.iloc[row_id,3] = df.iloc[row_id,3] - df.iloc[row_id-1,3]
                    df.iloc[row_id,4] = df.iloc[row_id,4] - df.iloc[row_id-1,4]
                    df.iloc[row_id,5] = df.iloc[row_id,5] - df.iloc[row_id-1,5]
                    df.iloc[row_id,8] = df.iloc[row_id,8] - df.iloc[row_id-1,8]
                    df.iloc[row_id,9] = df.iloc[row_id,9] - df.iloc[row_id-1,9]
                    df.iloc[row_id,10] = df.iloc[row_id,10] - df.iloc[row_id-1,10]
                elif row_id == 0:
                    if df.iloc[row_id,0].strftime('%m') == '06':
                        df.iloc[row_id,3] = df.iloc[row_id,3]/2 
                        df.iloc[row_id,4] = df.iloc[row_id,4]/2
                        df.iloc[row_id,5] = df.iloc[row_id,5]/2
                        df.iloc[row_id,8] = df.iloc[row_id,8]/2
                        df.iloc[row_id,9] = df.iloc[row_id,9]/2
                        df.iloc[row_id,10] = df.iloc[row_id,10]/2
                    if df.iloc[row_id,0].strftime('%m') == '09':
                        df.iloc[row_id,3] = df.iloc[row_id,3]/3
                        df.iloc[row_id,4] = df.iloc[row_id,4]/3
                        df.iloc[row_id,5] = df.iloc[row_id,5]/3
                        df.iloc[row_id,8] = df.iloc[row_id,8]/3
                        df.iloc[row_id,9] = df.iloc[row_id,9]/3
                        df.iloc[row_id,10] = df.iloc[row_id,10]/3
                    if df.iloc[row_id,0].strftime('%m') == '12':
                        df.iloc[row_id,3] = df.iloc[row_id,3]/4
                        df.iloc[row_id,4] = df.iloc[row_id,4]/4
                        df.iloc[row_id,5] = df.iloc[row_id,5]/4
                        df.iloc[row_id,8] = df.iloc[row_id,8]/4
                        df.iloc[row_id,9] = df.iloc[row_id,9]/4
                        df.iloc[row_id,10] = df.iloc[row_id,10]/4
        return {"raw":raw_df,"perquarter":df}
