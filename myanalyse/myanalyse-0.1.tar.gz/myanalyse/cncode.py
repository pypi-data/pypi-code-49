# -*- coding: utf-8 -*-
'''
get and write shanghai and shengzheng code into database 
'''
import time,os,sys,datetime
import pandas as pd
from sqlalchemy import create_engine
from jqdatasdk import *
import jqdatasdk

mysql_pass = os.environ['mysql_pass']
mysql_ip = '127.0.0.1'
acc_jq = os.environ['acc_jq']
passwd_jq = os.environ['passwd_jq']
user = 'root'

sz_engine = create_engine("mysql+pymysql://{}:{}@{}:3306/szsec?charset=utf8".\
                           format(user,mysql_pass,mysql_ip))
sh_engine = create_engine("mysql+pymysql://{}:{}@{}:3306/shsec?charset=utf8".\
                           format(user,mysql_pass,mysql_ip))


def get_latest(target):
    ''' get_all_trade_days create all trades day in a year,\
        getlast get the latest trade day forword'''
    xday = get_all_trade_days()
    latest = target + datetime.timedelta(-1)
    while (latest not in xday):
        latest = latest + datetime.timedelta(-1)
    return latest


def get_code():
    '''get sz,sh code from jqdatasdk;get hk code from hkex'''
    try:
        auth(acc_jq, passwd_jq)
        today = datetime.date.today()
        latest = get_latest(today)
        tmp_stock = get_all_securities(types=['stock'],date=latest)
        sz_stock = pd.DataFrame(columns=['code','name'])
        sh_stock = pd.DataFrame(columns=['code','name'])
        for row in tmp_stock.iterrows():
            if(row[0][0] != '6'):
                sz_stock = sz_stock.append({'code':row[0][0:6] ,'name':row[1][0]},\
                           ignore_index=True)
            else:
                sh_stock = sh_stock.append({'code':row[0][0:6] ,'name':row[1][0]},\
                           ignore_index=True)
        #add 510050 both into szsec.code and shsec.code
        sz_stock = sz_stock.append({'code':'510050' ,'name':'50etf'},ignore_index=True)  
        sh_stock = sh_stock.append({'code':'510050' ,'name':'50etf'},ignore_index=True)      
    except:
        sz_stock = None
        sh_stock = None
    return  (sz_stock,sh_stock)


def write_code():
    '''
    write code into database , szsec and shsec
    '''
    sz_stock,sh_stock = get_code()
    if sz_stock is not None and sh_stock is not None:
        sz_stock.to_sql('code',sz_engine,if_exists='replace', index=False)
        sh_stock.to_sql('code',sh_engine,if_exists='replace', index=False)
        return (sz_stock['code'],sh_stock['code'])
    else:
        return None




