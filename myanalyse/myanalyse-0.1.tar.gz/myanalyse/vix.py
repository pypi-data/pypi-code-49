# -*- coding: utf-8 -*-
'''
求出波动性，并绘图,本地没有数据，就从yahoo上抓数据
dp means date and price
example:
    import analyse.data.vix as vis
    stock = ""
    vix.draw_vix(data=df,stock='somestock')
    vix.draw_vix(stock='',num=500)
    vix.draw_vix(stock,num,market='sz')  
    vix.draw_vix(stock,num,market='sh')

'''
import os,io
import re,time,datetime
import http.cookiejar
import urllib.request
import pymysql
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
from pylab import *
from sqlalchemy import create_engine

base_dir = '/tmp'
user = 'root'
mysql_ip = '127.0.0.1'
mysql_pass = os.environ['mysql_pass']

hkengine = create_engine('mysql+pymysql://root:{}@{}:3306/hksec?charset=utf8'.\
                          format(mysql_pass,mysql_ip))
szengine = create_engine('mysql+pymysql://root:{}@{}:3306/szsec?charset=utf8'.\
                          format(mysql_pass,mysql_ip))
shengine = create_engine('mysql+pymysql://root:{}@{}:3306/shsec?charset=utf8'.\
                          format(mysql_pass,mysql_ip))

mproperty = {'hk':{'engine':hkengine},
             'sz':{'engine':szengine},
             'sh':{'engine':shengine}}

def get_ohlc_yahoo(stock='^hsi',num=None):
    ''' get data in `open high low close` format ,reindex from 0
    normal stock : get_ohlc_yahoo(stock='msft',num=None)
    index        : get_ohlc_yahoo(stock='^dji',num=None)  
                   get_ohlc_yahoo(stock='^hsi',num=None)
    x=get_ohlc_yahoo(stock='^hsi',num=500)
    '''
    start=0
    end  = int(time.time())
    target1 = "https://finance.yahoo.com/quote/{}/history?p={}".format(stock,stock)
    fname_cookie = os.path.join(base_dir,'cookies.txt')
    cookie = http.cookiejar.MozillaCookieJar(fname_cookie)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response1 = opener.open(target1).read().decode('utf-8')
    cookie.save()
    crumb = re.findall('"CrumbStore":{"crumb":"(.+?)"}', response1)[0] 
    cookie.load(fname_cookie)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    time.sleep(3)
    target2 = "https://query1.finance.yahoo.com/v7/finance/download/\
               {0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}".\
               format(stock,start,end,crumb)
    response2 = opener.open(target2).read().decode('utf-8')
    df = pd.read_csv(io.StringIO(response2),sep=',')
    tmpdf = df.dropna(axis=0,how='any')
    tmpdf.columns = ['date','open','high','low','close','amount','volume']
    newdf = pd.DataFrame(columns = ['code','date','open','high','low',\
                                    'close','amount','volume'] )
    code = stock.replace('^','')
    for id in range(0,len(tmpdf)):
        newdf.loc[id] = [code,tmpdf.iloc[id]['date'],round(tmpdf.iloc[id]['open'],2),    \
                     round(tmpdf.iloc[id]['high'],2),round(tmpdf.iloc[id]['low'],2),     \
                     round(tmpdf.iloc[id]['close'],2),0,int(tmpdf.iloc[id]['volume'])]
    os.remove(fname_cookie)
    if num is None:
        newdf = newdf
    else:
        newdf = newdf.iloc[-num:,]
    newdf.index = range(len(newdf))
    return newdf



def get_dp_yahoo(stock='^hsi',num=500):
    '''get data in `date price` format from ohlc 
    normal stock : get_dp_yahoo(stock='msft',num=None)
    index        : get_dp_yahoo(stock='^dji',num=None)  
                   get_dp_yahoo(stock='^hsi',num=None)
    '''
    df = get_ohlc_yahoo(stock=stock,num=num)
    date = df['date']
    price = df['close']
    newdf = pd.DataFrame({'date':date,'price':price})
    return newdf

def get_ohlc_local(stock=None,num=None,market=None):
    stock = stock.replace('^','')
    if num is None:
        sql_code = 'SELECT date,open,high,low,close FROM quote where code="{}";'\
                    .format(stock)
    else:
        sql_code = 'select * from (select date,open,high,low,close from quote \
                    where code="{}" order by date desc limit {}) as tmp order \
                    by date asc;'.format(stock,num) 
    try:
        df = pd.read_sql(sql_code, con=mproperty[market]['engine']) 
    except:
        return None
    return  df   


def get_dp_local(stock=None,num=None,market=None):
    '''
        get_dp_local(stock,market='sz')  get_dp_local(stock,market='sh')
    '''
    stock = stock.replace('^','')
    if num is None:
        sql_code = 'SELECT date,close as price FROM quote where code="{}";'\
                    .format(stock)
    else:
        sql_code = 'select * from (select date,close as price from quote \
                    where code="{}" order by date desc limit {}) as tmp  \
                    order by date asc;'.format(stock,num) 
    try:
        df = pd.read_sql(sql_code, con=mproperty[market]['engine']) 
    except:
        return None
    return  df   


def get_local_max_min(data=None,stock=None,num=None,market=None):
    '''data is None ,get_local_max_min from stcok and num;
       list to reindex from 0 and get data for using   
    normal stock : get_local_max_min(stock='msft',num=None)
    index        : get_local_max_min(stock='^dji',num=None)  
                   get_local_max_min(stock='^hsi',num=None)
                   get_local_max_min(data,stock,market='sz')  
                   get_local_max_min(data,stock,market='sh')

    '''
    if(data is None):
        code = stock.replace('^','')
        result = get_dp_local(stock=code,num=num,market=market)
        if result is not None:
            df = result
        else:
            df = get_dp_yahoo(stock=stock,num=num)
    else:
        df = data
    price = list(df['price'])
    date = list(df['date'])
    number = len(df)
    local_max_min = []
    if number<21 :
        print("the stock {}  's data is too small  ")
        return
    end_id = number - 1
    id=10
    while id<= end_id-11:
        flag1 = max(price[id-10:id])
        flag2 = min(price[id+1:id+11])
        flag3 = min(price[id-10:id])
        flag4 = max(price[id+1:id+11])
        if ( price[id] >= flag1 and price[id] >= flag4 ):
            local_max_min.append([date[id],price[id],'lmax'])
            id = id +10
        elif( price[id] <= flag2 and price[id] <= flag3 ):
            local_max_min.append([date[id],price[id],'lmin'])
            id = id +10
        else:
            id = id +1
    if local_max_min :
        return local_max_min
    else:
        print('no local max or min in the period')
        return None


def draw_vix(data=None,stock=None,num=None,market=None):
    '''draw vix ,when no local max or min ,return None ,draw nothing
       input data contains date and price to draw
       when data is not None,you have to input code='' in function 
       as the following two formats:
       draw_vix(data=df,stock='somestock')
       draw_vix(stock='',num=500)
       draw_vix(stock,num,market='sz')  
       draw_vix(stock,num,market='sh')
    normal stock : draw_vix(stock='msft',num=None)
    index        : draw_vix(stock='^dji',num=None)  draw_vix(stock='^hsi',num=None)      
    '''
    if data is None :
        code = stock.replace('^','')
        result = get_dp_local(stock=code,num=num,market=market)
        if result is not None:
            df = result 
        else:
            df = get_dp_yahoo(stock=stock,num=num)
            code = stock
    else:
        #recombine it as new df,change index from 0
        #changed index in getdata,how about if accept data 
        #with index not beginning from 0 ?
        newdate = list(data['date'])
        newprice = list(data['price'])
        df = pd.DataFrame({'date':newdate,'price':newprice})
    local_max_min = get_local_max_min(data=df,stock=stock,num=num)
    if local_max_min is not None:
        plt.ion()
        date = df['date']
        price = df['price']
        figure, ax = plt.subplots()
        xticks = list(range(0,len(date),10))
        if( xticks[-1] != len(date) ): xticks.append(len(date)-1)
        xlabels = date[xticks]
        ax.set_xticks(xticks)
        ax.set_xticklabels(xlabels,rotation=90)
        ax.plot(date,price)
        for item in local_max_min:
            ax.plot(item[0],item[1],'x',color='red')
        ax.set_title("{}'s vix in {} days".format(code,len(df)),fontsize=12,color='r')
        plt.draw()
        return  {'data':df,'local_max_min':local_max_min}
    else:
        print("no local max and min in the period,can't draw")
        return None
