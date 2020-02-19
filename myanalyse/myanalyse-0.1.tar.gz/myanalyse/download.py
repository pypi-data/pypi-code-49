# -*- coding: utf-8 -*-
'''
get and write hkcode into database
'''
import time,os,sys
import pandas as pd
import re 
from sqlalchemy import create_engine
import argparse

mysql_pass = os.environ['mysql_pass']
mysql_ip = '127.0.0.1'
table_all = 'allsec'
table_anchor = 'anchorsec'
table_other = 'othersec'

def get_time():
    '''
    get time for retrieve url ,minusNumber

    '''
    today = time.localtime()
    dayOfWeek = time.strftime('%u',today)
    if(dayOfWeek == '1'):
        minusNumber = 3
    elif(dayOfWeek == '7'):
        minusNumber = 2
    else:
        minusNumber = 1
    stamptime_getData = int(time.strftime('%s',today)) - minusNumber * 24 * 60 *60
    iday = time.strftime('%d',time.localtime(stamptime_getData))
    if(iday[0] == '0'): iday = iday[1]
    imon = time.strftime('%b',time.localtime(stamptime_getData))
    iyear = time.strftime('%y',time.localtime(stamptime_getData))
    return [iday,imon,iyear]


def con5code(code):
    '''
    hkcode contain 5 digitals
    series converter ,map function
    '''
    if(code[0] != '8'):
        code = '0' + code[0:4]
    else:
        code = code[0:5]
    return code

def get_code(type):
    '''
    all:all securities in hk,table name allsec
    anchor:indexed and stock option,table name anchorsec
    other: customized,table name othersec
    '''
    if (type == 'all'):
        url_all1 = 'https://sc.hkex.com.hk/TuniS/www.hkex.com.hk/chi/services'
        url_all2 = '/trading/securities/securitieslists/ListOfSecurities_c.xlsx'
        url_all = url_all1 + url_all2
        os.system("wget  --user-agent='Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.' {} -O  /tmp/all.xlsx ".format(url_all))
        data_all = pd.read_excel(io="/tmp/all.xlsx",skiprows=2,dtype=str)
        df_all = pd.DataFrame(data_all['股份代號'])
        df_all.columns = ['code']
        return df_all
    elif(type == 'anchor'):
        codes_anchor = set()
        #filter 
        itime=get_time()
        #hsi 50
        url_hsi = "https://www.hsi.com.hk/static/uploads/contents/en/indexes/\
                   report/hsi/con_{0}{1}{2}.csv".format(itime[0],itime[1],itime[2])
        os.system("wget {} -O /tmp/anchor.csv".format(url_hsi))
        data_hsi =  pd.read_csv(io='/tmp/anchor.csv',dtype=str,encoding = 'UTF-16',\
                                skiprows=1,sep='\t')
        codes_hsi = data_hsi['Stock Code']
        #hsi中型指数
        url_hsci = "https://www.hsi.com.hk/static/uploads/contents/en/indexes/\
                    report/hsci/con_{0}{1}{2}.csv".format(itime[0],itime[1],itime[2])
        os.system("wget {} -O /tmp/hsci.csv".format(url_hsci))
        data_hsci =  pd.read_csv(io='/tmp/hsci.csv',dtype=str,encoding = 'UTF-16',\
                                 skiprows=1,sep='\t')
        filter = data_hsci['Index'] == 'Hang Seng Composite MidCap Index \
                                        恒生綜合中型股指數' 
        codes_hsci = data_hsci[filter]['Stock Code']
        codes_anchor = codes_hsi.append(codes_hsci)
        codes_anchor = codes_anchor.map(con5code)
        frame = {'code':codes_anchor}
        # serires to dictionary to dataframe 
        df_anchor = pd.DataFrame(frame)
        df_anchor.index = range(len(df_anchor))
        return df_anchor
    elif(type == 'other'):
        codes_other = []
        while True:
            try:
                code = input('please input what stock you want with five digital,\
                              enter ctrl+d to finish the input: ')
                if len(code) == 5:
                    codes_other.append(code)
                else:
                    print('please input what stock you want with five digital')
                    continue
            except EOFError:
                break
        df = pd.DataFrame(codes_other,columns = ['code'])
        return  df

def convert_unit(value):
    tmpvalue = value.replace(',','')
    tmpvalue = int(tmpvalue)
    return tmpvalue 


def write_code(type):
    '''
    write codes into database,all allsec;anchor anchorsec;other othersec
    write_code('all')  write_code('anchor')  write_code('other')
    '''
    conn = create_engine("mysql+pymysql://root:{}@{}:3306/hksec?charset=utf8".\
                          format(mysql_pass,mysql_ip))
    if(type == 'all'):
        url_all = 'https://sc.hkex.com.hk/TuniS/www.hkex.com.hk/chi/services/\
                   trading/securities/securitieslists/ListOfSecurities_c.xlsx'
        data_all = pd.read_excel(url_all,skiprows=2,dtype=str)
        fields = ['code','name','type','unit']
        data = data_all[['股份代號','股份名稱','分類','買賣單位']]
        data.columns = fields
        xdata = data.copy()
        xdata['unit'] = xdata['unit'].map(convert_unit)
        table = eval("table_{}".format(type))
        xdata.to_sql(table, conn,if_exists='replace', index=False)
        return  xdata['code']
    elif(type == 'anchor' or type == 'other'):
        data = get_code(type)
        table = eval('table_{}'.format(type))
        if (type == 'anchor'):
            data.to_sql(table, conn,if_exists='replace', index=False)
        else:
            data.to_sql(table, conn,if_exists='append', index=False)
        return  data['code']
