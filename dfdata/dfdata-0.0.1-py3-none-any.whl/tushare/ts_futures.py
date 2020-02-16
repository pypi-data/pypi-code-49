#!/usr/bin/env python
# coding: utf-8

import datetime
import time
import sqlite3
import pandas as pd
import tushare as ts
pro = ts.pro_api()

# 初始化
#Tushare中定义交易所代码如：交易所名称：郑州商品交易所，代码：CZCE，后缀：.ZCE
exchange_name_ts = {
    'CZCE':'郑州商品交易所',
    'SHFE':'上海期货交易所',
    'DCE':'大连商品交易所',
    'CFFEX':'中国金融期货交易所',
    'INE':'上海国际能源交易所'
}

#期货数据库
FUTURES_TS_DB = '../data/futures_ts.db'


# # 下载Tushare期货数据
# 期货数据接口：https://tushare.pro/document/2?doc_id=134  
# 期货数据库futures_ts.db  


# ## 期货合约表 fut_basic
# 期货合约表fut_basic，全部历史合约
# * 表头 ts_code	symbol	exchange	name	fut_code	multiplier	trade_unit	per_unit	quote_unit	quote_unit_desc	d_mode_desc	list_date	delist_date	d_month	last_ddate
# * 表头
def save_ts_fut_basic():
    conn = sqlite3.connect(FUTURES_TS_DB)  #连接数据库，如果存在就会自动新建
    count = 0  #表的行数
    print("数据库futures_ts连接成功")
    c = conn.cursor()
    c.execute('drop table fut_basic') #删除数据库以前的fut_basic表
    print("删除之前fut_basic表")
    
    search_exchanges = ['CZCE','SHFE','DCE','CFFEX','INE']  #定义一个交易所列表，要获取最近数据的交易所
    for exchange in search_exchanges:
        df = pro.fut_basic(exchange=exchange) 
        print("获取到{}的{}行合约数据".format(exchange_name_ts[exchange], len(df)))
        df.to_sql("fut_basic", conn, if_exists="append")
        print("{}的合约数据，已保存到数据库！".format(exchange_name_ts[exchange]))
    
    
    conn.close()   #关闭数据库连接
    print("合约数据已全部保存！")

#读取期货合约表 fut_basic
#
def read_ts_fut_basic():
    


# ## 期货日线行情表 fut_daily
# 期货日线行情表fut_daily，数据开始月1996年1月，每日盘后更新  
# tushare当前限制：每分钟最多调用120次，单次最大2000条，总量不限制。
# 
# * 表头
# 通过交易日历获取所有要下载交易日
# 参数：
# db_name 设置数据库名称，
def save_ts_fut_daily(db_name='data/futures_ts.db',table_name='fut_daily', start_date='19960101', end_date='today', exchanges = ['DCE','SHFE','CFFEX','CZCE','INE']):
    exchanges = exchanges
    end_date = end_date
    if end_date == 'today':        
        today = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)) #获取现在北京时间，通过utc时间+8小时
        today_str = today.strftime('%Y%m%d') #转化为字符串
    start_date = start_date  #下载开始时间
    end_date = today_str   # 下载结束时间  
    print("开始下载日期："+start_date)
    print("结束下载日期："+end_date)
    
    try:
        conn = sqlite3.connect(db_name)
        print("数据库{}连接成功".format(db_name))
    except:
        print("数据库地址或名称错误！可能由于文件夹权限不够！")
        print("可以尝试如如下：db_name='../data/futures_ts.db'表示父文件夹下data文件夹里futures_ts.db文件")
        return
    #c = conn.cursor()
    #c.execute('drop table fut_daily') #删除数据库以前的fut_basic表
    #print("删除之前fut_daily表")

    #数据库已有日期集合
    try:
        sql = "select trade_date from {} ;".format(table_name)
        #默认：select trade_date from fut_daily
        df_trade_data = pd.read_sql_query(sql, conn) #获取数据库中trade_date列
        trade_date_in_db = set(df_trade_data['trade_date'])  #数据库中已有日期集合
    except:
        trade_date_in_db = set()  #如果数据表不存在，就设置已有日期为空集合
    print("数据库中已有交易日数量："+str(len(trade_date_in_db)))
     
    #要下载的交易日集合
    trade_date_all = set()  
    for exchange in exchanges:
        df = pro.trade_cal(exchange=exchange, start_date=start_date, end_date=today_str)
        df_set = set(df[df.is_open > 0 ]['cal_date'])
        trade_date_all = trade_date_all | df_set
        print('该时段内，{}共有{}个交易日'.format(exchange_name_ts[exchange], len(df_set)))
    print("要下载交易日数量："+str(len(trade_date_all)))
    #print(trade_date_all)
    
    #未完成的下载交易日
    trade_date_unfinished = trade_date_all - trade_date_in_db      
    print("未完成的下载交易日："+str(len(trade_date_unfinished)))
    
    for trade_date in trade_date_unfinished:
        df = pro.fut_daily(trade_date=trade_date)
        print(trade_date+'当天获取到行数：'+str(len(df)))
        
        df.to_sql("fut_daily", conn, if_exists="append")
        print(trade_date+"当天数据，已保存到数据库！")
        
        time.sleep(0.51) #休息0.5s，因为限制1分钟120次
    
    conn.close()
    print("数据保存完成")


    
def save_ts_fut_holding():
    print("下载fut_holding")

if __name__ == '__main__':







