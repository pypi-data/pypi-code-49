# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 17:01
# @File    : common_var.py
# @User    : yangchuan
# @Desc    :
import sys
import os

class Constant:
    SUFFIX_DAILY= "-d"
    SUFFIX_MINUTE = "-m"
    SUFFIX_HOUR = "-60m"
    DB_NAME = 'quant'
    RUN_FREQ_DAY = 'day'
    RUN_FREQ_HOUR = 'hour'
    RUN_FREQ_MINUTE = 'minute'
    KLINE_INTERVAL_1MINUTE = '1m'
    KLINE_INTERVAL_3MINUTE = '3m'
    KLINE_INTERVAL_5MINUTE = '5m'
    KLINE_INTERVAL_15MINUTE = '15m'
    KLINE_INTERVAL_30MINUTE = '30m'
    KLINE_INTERVAL_1HOUR = '1h'
    KLINE_INTERVAL_2HOUR = '2h'
    KLINE_INTERVAL_4HOUR = '4h'
    KLINE_INTERVAL_6HOUR = '6h'
    KLINE_INTERVAL_8HOUR = '8h'
    KLINE_INTERVAL_12HOUR = '12h'
    KLINE_INTERVAL_1DAY = '1d'
    KLINE_INTERVAL_3DAY = '3d'
    KLINE_INTERVAL_1WEEK = '1w'
    KLINE_INTERVAL_1MONTH = '1M'
    FIXED_SLIPPAGE = 'fixedslippage'
    PRICE_RELATED_SLIPPAGE = 'pricerelatedslippage'
    STEP_RELATED_SLIPPAGE = 'steprelatedslippage'
    ORDER_OPEN = 'open'
    ORDER_CLOSE = 'close'


class Symbol:
    M9999 = "M9999.XDCE"
    BTC = "BTC"
    USDT = "USDT"



class SystemConfig:
    LOG_FILE_FOLDER = os.path.join(os.path.expanduser('~'),'general_quant')
    LOG_FILE_PATH = os.path.join(os.path.expanduser('~'),'general_quant','logs')
    MONGODB_HOST = "182.151.7.177"
    MONGODB_PORT = 27017
    MONGODB_USER = "admin"
    MONGODB_PWD = "admin"
    MONGODB_DB_ADMIN = "system_admin"
    MONGODB_COL_USERS = "users"
    WORKING_MODE_NORMAL = "normal"
    WORKING_MODE_SUPERVISOR = "supervisor"
    WORKING_MODE = WORKING_MODE_NORMAL
