# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 17:11
# @File    : general_test.py
# @User    : yangchuan
# @Desc    : 
from quant_trade_framwork.common import SystemConfig

def func_a(func_a_p1):
    print(func_a_p1)

def func_b(func_name,func_b_p1,**kwargs):
    func_name(**kwargs)
    print(func_b_p1)

if __name__ == '__main__':
    print(SystemConfig.LOG_FILE_PATH)
    # temp = context()
    # temp.get_price("M9999.XDCE")
    # result = temp.history("M9999.XDCE",["open","close"],10,"dataframe")
    # print(temp.current_datetime())
    # func_b(func_name = func_a,func_a_p1 = "123",func_b_p1='Hello Python')