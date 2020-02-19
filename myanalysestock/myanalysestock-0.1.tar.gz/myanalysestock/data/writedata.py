#!/usr/bin/python3  
'''
从通达信下载数据
example:
    python3 writedata.py
    or
    import analyse.data
    analyse.data.writedata.main()
'''
from jqdatasdk import *
import jqdatasdk
from  os import listdir as ldir
import os ,shutil ,io
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import struct
import re,time,datetime
import http.cookiejar
import urllib.request
import logging
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import  analyse.cncode as cncode
import  analyse.hkcode as hkcode
import subprocess


base_dir = '/tmp' 
logging_file = os.path.join(base_dir,'writedata.log')
logging.basicConfig(filename=logging_file,level=logging.INFO)

user = 'root'
mysql_ip = '127.0.0.1'
mysql_pass = os.environ['mysql_pass']
acc_jq = os.environ['acc_jq']
passwd_jq = os.environ['passwd_jq']
email126 = os.environ['email126']
pass126 = os.environ['pass126']

hkengine = create_engine("mysql+pymysql://{}:{}@{}:3306/hksec?charset=utf8".\
                         format(user,mysql_pass,mysql_ip))
szengine = create_engine("mysql+pymysql://{}:{}@{}:3306/szsec?charset=utf8".\
                         format(user,mysql_pass,mysql_ip))
shengine = create_engine("mysql+pymysql://{}:{}@{}:3306/shsec?charset=utf8".\
                         format(user,mysql_pass,mysql_ip))
hkdir = os.path.join(base_dir,'hklday')
szdir = os.path.join(base_dir,'szlday')
shdir = os.path.join(base_dir,'shlday')
hkfile = os.path.join(base_dir,'hklday.zip')
szfile = os.path.join(base_dir,'szlday.zip')
shfile = os.path.join(base_dir,'shlday.zip')

mproperty = {'hk':{'engine':hkengine,'mdir':hkdir},
             'sz':{'engine':szengine,'mdir':szdir},
             'sh':{'engine':shengine,'mdir':shdir}}

unpack_rule = {'hk':'ifffffii','sz':'iiiiifii','sh':'iiiiifii'}

def get_latest(target):
    ''' get_all_trade_days create all trades day in a year,getlast get the 
    latest trade day forword'''
    xday = get_all_trade_days()
    latest = target + datetime.timedelta(-1)
    while (latest not in xday):
        latest = latest + datetime.timedelta(-1)
    return latest


def send_email(subject="title",content="info"):
    '''call 126 mail and send mail to 126 itself'''
    port = 465
    smtp_server = 'smtp.126.com'
    sender_email = email126
    receiver_email = email126
    password = pass126
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email
    text = content
    part = MIMEText(text, 'plain')
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.126.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def write_quote_table(code,dfile,market):
    '''parse data from file and write into table quote
    return quote data from every stock in dataframe form
    '''
    try:
        data = open(dfile,'rb')
        dayline = data.read(32)
        alldayline = []
        while  dayline:
            tmpdata = list(struct.unpack(unpack_rule[market],dayline))
            dataday = [code]
            if( code == '510050' and market == 'sz'):
                dataday.append(str(tmpdata[0]))
                dataday.append(tmpdata[1]/1000)
                dataday.append(tmpdata[2]/1000)
                dataday.append(tmpdata[3]/1000)
                dataday.append(tmpdata[4]/1000)
                dataday.append(round(tmpdata[5],2))
                dataday.append(tmpdata[6])
                alldayline.append(dataday)
            elif( code == '510050' and market == 'sh'):
                dataday.append(str(tmpdata[0]))
                dataday.append(tmpdata[1]/1000)
                dataday.append(tmpdata[2]/1000)
                dataday.append(tmpdata[3]/1000)
                dataday.append(tmpdata[4]/1000)
                dataday.append(round(tmpdata[5],2))
                dataday.append(tmpdata[6])
                alldayline.append(dataday)
            elif( len( str(tmpdata[0]) )  == 8 and market == 'hk'):
                dataday.append(str(tmpdata[0]))
                dataday.append(round(tmpdata[1],2))
                dataday.append(round(tmpdata[2],2))
                dataday.append(round(tmpdata[3],2))
                dataday.append(round(tmpdata[4],2))
                dataday.append(round(tmpdata[5],2))
                dataday.append(tmpdata[6]*100)
                alldayline.append(dataday)
            elif( len( str(tmpdata[0]) )  == 8 and (market == 'sz' ) ):
                dataday.append(str(tmpdata[0]))
                dataday.append(tmpdata[1]/100)
                dataday.append(tmpdata[2]/100)
                dataday.append(tmpdata[3]/100)
                dataday.append(tmpdata[4]/100)
                dataday.append(round(tmpdata[5],2))
                dataday.append(tmpdata[6])
                alldayline.append(dataday)
            elif( len( str(tmpdata[0]) )  == 8 and (market == 'sh') ):
                dataday.append(str(tmpdata[0]))
                dataday.append(tmpdata[1]/100)
                dataday.append(tmpdata[2]/100)
                dataday.append(tmpdata[3]/100)
                dataday.append(tmpdata[4]/100)
                dataday.append(round(tmpdata[5],2))
                dataday.append(tmpdata[6])
                alldayline.append(dataday)
            else:
                logging.info('parse stock file {} , failure , \
                              contain some 00 as date'.format(dfile))
                return None
            dayline = data.read(32)
    except:
        logging.info('parse error unknown for  {} '.format(dfile))
        return None
    fields = ['code','date','open','high','low','close','amount','volume']
    df = pd.DataFrame(alldayline, columns= fields)
    df.to_sql(name = 'quote', con = mproperty[market]['engine'], \
              if_exists='append', index=False)
    return df


def get_cur_vix(code,data,market):
    '''get the current vix for every stock from recent trend
    and write it into curvix table 
    return stock's current vix in array 
    
    '''
    price = data['close']
    date = data['date'].map(lambda x:str(x))
    number = len(data)
    lmax_min = []
    if number<21 :
        logging.info("the stock {}  's data is too small  ".format(code))
        return None
    end_id = number - 1
    id=10
    while id<= end_id-11:
        flag1 = max(price[id-10:id])
        flag2 = min(price[id+1:id+11])
        flag3 = min(price[id-10:id])
        flag4 = max(price[id+1:id+11])
        if ( price[id] >= flag1 and price[id] >= flag4 ):
            lmax_min.append([date[id],price[id],'lmax'])
            id = id +10
        elif( price[id] <= flag2 and price[id] <= flag3 ):
            lmax_min.append([date[id],price[id],'lmin'])
            id = id +10
        else:
            id = id +1
    end_index = len(data) - 1
    if lmax_min:
        if  lmax_min[-1][1] >0:
            start_index = data[data['date'] == lmax_min[-1][0]].index.values[0]
            cur_time_scope = end_index - start_index + 1
            if(lmax_min[-1][1] >= list(price)[-1]):
                vix_range = -round( 1- list(price)[-1] / lmax_min[-1][1] , 4)
            else:
                vix_range = round( list(price)[-1]/lmax_min[-1][1] -1 , 4)
        else:
            logging.info("max or min value is zero,can't calculate the vix for  {}  "\
                          .format(code))
            return None
    else:
        logging.info("no max or min value for {}  because of short time period "\
                      .format(code))
        return None
    maxdate = list(date)[-1]
    mdata = [code,cur_time_scope,vix_range,maxdate]
    return  mdata


def write_hsi():
    '''get hsi data from yahoo and write it into mysql'''
    code = 'hsi'
    start=0
    end=int(time.time())
    symbol='^hsi'
    target1 = "https://finance.yahoo.com/quote/{}/?p={}".format(symbol,symbol)
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
    target2 = "https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}\
               &period2={2}&interval=1d&events=history&crumb={3}".\
               format(symbol,start,end,crumb)
    response2 = opener.open(target2).read().decode('utf-8')
    df = pd.read_csv(io.StringIO(response2),sep=',')
    tmpdf = df.dropna(axis=0,how='any')
    tmpdf.columns = ['date','open','high','low','close','amount','volume']
    newdf = pd.DataFrame(columns = ['code','date','open','high','low',\
                                    'close','amount','volume'] )
    for id in range(0,len(tmpdf)):
        newdf.loc[id] = [code,tmpdf.iloc[id]['date'],round(tmpdf.iloc[id]['open'],2),  \
                     round(tmpdf.iloc[id]['high'],2),round(tmpdf.iloc[id]['low'],2),   \
                     round(tmpdf.iloc[id]['close'],2),0,int(tmpdf.iloc[id]['volume'])]
    newdf.to_sql('quote', con=hkengine, index=False, if_exists='append')
    os.remove(fname_cookie)
    return newdf


def parse_code(dfile,market):
    '''parse code from dfile'''
    if market == 'hk' :
        code = re.search('\d{5}',dfile).group()
    else:
        code = re.search('\d{6}',dfile).group()
    return  code

def prework():
    '''
    download raw data from tdx and create database table
    '''
    cmd = "mysqldump  -uroot -pi{} --all-databases > {}/alldatabaseback.sql".\
                 format(mysql_pass,os.environ['HOME'])
    os.system(cmd)
    if(not ( os.path.exists(hkfile) and os.path.exists(szfile) and \
             os.path.exists(shfile))):
        downloadfile = os.path.join(os.path.dirname(__file__),'download.sh')
        os.system("/bin/bash {}".format(downloadfile))
    try:
        sqlfile = os.path.join(os.path.dirname(__file__),'init.sql')
        os.system("mysql -h localhost -uroot -p{} < {}".format(mysql_pass,sqlfile))
    except:
        send_email(subject='database',content='something wrong \
                   with your database setting')
        exit()


def write_code_table():
    '''
    write code into hksec,szsec,shsec 
    return stocks code 
    '''
    sz_stock,sh_stock = cncode.write_code()
    hk_stock = hkcode.write_code('all')
    stocks = {'hk':hk_stock,'sz':sz_stock,'sh':sh_stock}
    return stocks

def main():
    starttime = datetime.datetime.now()
    prework()
    stocks = write_code_table()
    for market in mproperty:
        dfns = ldir(mproperty[market]["mdir"])
        vix_data = []
        for dfn in dfns:
            #增加判断，如果dfn在代码表内，请执行解析
            dfile = os.path.join(mproperty[market]["mdir"],dfn)
            try:
                code = parse_code(dfile,market)
            except:
                logging.info("can't get code ,fail {}".format(dfile))
                continue
            if(code in list(stocks[market])):
                data = write_quote_table(code,dfile,market)
                if data is not None :
                    tmp_vix_data = get_cur_vix(code,data,market)
                    if tmp_vix_data is not None:
                        vix_data.append(tmp_vix_data)
        df_vix = pd.DataFrame(vix_data,columns = ['code','timescope','vix','maxdate'])
        df_vix.to_sql('curvix',con= mproperty[market]['engine'],if_exists='append',\
                      index=False)        
    time.sleep(10)
    content_hsi = ''
    try:
        write_hsi()
    except:
        logging.info('can not download hsi ')
        content_hsi = "something wrong with hsi data,can't download it\n"
    #remove all temp data
    shutil.rmtree(hkdir)
    shutil.rmtree(szdir)
    shutil.rmtree(shdir)
    os.remove(hkfile)
    os.remove(szfile)
    os.remove(shfile)
    os.remove(os.path.join(os.environ['HOME'] , 'alldatabaseback.sql'))
    send_email(subject = 'get data',content= content_hsi + 'all data downloaded ,\
               write into database and get curvix ')
    endtime = datetime.datetime.now()
    mytime = round((endtime -starttime).seconds/60,2)
    logging.info("the used  time for the whole process:download and write into \
                  database and get current vix table  is {} minutes.".format(mytime))

if  __name__ == "__main__":
    main()
