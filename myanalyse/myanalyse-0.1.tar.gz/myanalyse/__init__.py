__all__ = ['cncode','hkcode','data','info','vix','ana','cbond']
from analyse  import  *
import analyse
#import os
#import numpy as np
#import pandas as pd
#import datetime
#from jqdatasdk import *



#acc_jq = os.environ["acc_jq"]
#passwd_jq = os.environ["passwd_jq"]

#auth(acc_jq,passwd_jq)

__doc__ ='''
analyse文件夹放置/usr/local/lib/python3.5/dist-packages
聚宽使用后缀 .XSHG .XSHE ,其他地方的数据不用后缀；
通达信没有后缀，香港使用5位数字。
本地完成的数据库szsec,shsec,hksec都不使用后缀，
本地数据库和聚宽混合使用时，需要调整股票代码。
金融类公司和非金融类公司的财务不同，调用时，需要进行专门处理。
财务报表分别是合并报表（不含后缀），母公司报表（含后缀parent）。
cncode,hkcode的返回值，不包含后缀；pehkipo(code)参数中的code,不包含后缀；
其他函数中的code 需要使用聚宽的后缀。
info.get_info(code,type),这里的type取值year, quarter；
返回值，peryear,perquarter,收益是当季的收益，不是累计收益。
ana包中的函数输出结果分别有合并公司计算值（不包含后缀），母公司计算值（含后缀parent)。
ana.get_pe(code,type),这里的type取值static,ttm,分别对应info.get_info中的year,quarter；
ana.get_growth(code,type),这里的type取值static,ttm,分别对应info.get_info中的year,quarter；
ana.get_return(code,type),这里的type取值static,ttm,分别对应info.get_info中的year,quarter；

获得转债数据
$HOME/cbond.csv文件不可以删除
import analyse
df = analyse.cbond.info()
转债数据更新
df = analyse.cbond.update()
'''




