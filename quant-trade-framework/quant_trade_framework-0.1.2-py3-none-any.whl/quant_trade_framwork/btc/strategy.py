# -*-coding:utf-8 -*-

# @Time    : 2020/2/8 14:29
# @File    : strategy.py
# @User    : yangchuan
# @Desc    : quant trade strategy information
from quant_trade_framwork.btc import context
from quant_trade_framwork.common.constant import Constant,Symbol
from datetime import timedelta
from quant_trade_framwork.common.logConfig import Logger
from quant_trade_framwork.model.Indicators import *
import math
from pytz import timezone
from quant_trade_framwork.btc.account import account
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

logger = Logger.module_logger("system")
cst_tz = timezone('Asia/Shanghai')
utc_tz = timezone('UTC')

class strategy:
    """
    class strategy define:
    (1) account: exchange,type,position
    (2) universe
    (3) strategy
    (4) strategy run
    """

    def __init__(self):
        self.context = context()
        self.daily_value = []
        self.daily_return = []
        self.benchmark_daily_return = []
        self.run_datetimes = []
        self.strategy_annualized_returns = None
        self.annualised_benchmark_return = None
        self.cumulative_portfolio_return = None
        self.cumulative_benchmark_return = None
        self.algorithm_volatility = 0
        self.benchmark_volatility = 0
        self.alpha = 0
        self.sharpe_ratio = 0
        self.information_ratio = 0
        self.beta = 0
        self.annualized_portfolio_volatility = 0
        self.max_drawdown = 0
        self.start_daily_value = None
        self.total_return = None
        self.run_duration_in_days = 1
        self.start_benchmark_index = 0
        self.last_benchmark_index = 0
        self.start_protfolio_value = 0
        self.sortino_ratio = 0
        self.risk_free_ratio = 0.01
        self.average_change = 0
        self.downside_risk = 0
        self.RF = 0.04

    def create_account(self,name:str,exchange:str,
                       account_type:str,position_base:dict):
        """

        :param name:
        :param exchange:
        :param account_type:
        :param position_base:
        :return:
        """
        new_account = account(name,exchange,account_type,position_base)
        context.set_account(new_account)
        context.exchange = exchange

    def create_universe(self,universe:list):
        """

        :param universe:
        :return:
        """
        self.universe = universe
        return universe

    def create_strategy(self,initialize, handle_data, universe,
                        benchmark:str, frequency:str, refresh_rate:int):
        """

        :param initialize:
        :param handle_data:
        :param universe:
        :param benchmark:
        :param frequency:
        :param refresh_rate:
        :return:
        """
        self.initialize = initialize
        self.handle_data = handle_data
        self.universe = universe
        self.benchmark = benchmark
        self.frequency = frequency
        self.refresh_rate = refresh_rate

        if self.frequency == Constant.RUN_FREQ_DAY:
            context.run_freq = Constant.KLINE_INTERVAL_1DAY
        elif self.frequency == Constant.RUN_FREQ_HOUR:
            context.run_freq = Constant.KLINE_INTERVAL_1HOUR
        elif self.frequency == Constant.RUN_FREQ_MINUTE:
            context.run_freq = Constant.KLINE_INTERVAL_1MINUTE

    def backtest(self,strategy,start:str,end:str,commission:dict):
        """

        :param strategy:
        :param start:
        :param end:
        :param commission:
        :return:
        """
        self.strategy = strategy
        self.start = datetime.strptime(start,"%Y-%m-%d")
        self.end = datetime.strptime(end,"%Y-%m-%d")
        self.comission = commission
        diff = self.end - self.start
        self.run_times = diff.days + 1
        self.run_duration_in_days = diff.days
        self.run_backtest()


    def run_backtest(self):
        """
        run backtest logical in every cycle
        :return: None
        """
        self.initialize(self.context)
        self.context.set_current_datetime(self.start)
        self.before_start_operation()
        if self.frequency == Constant.RUN_FREQ_DAY:
            for item in range(1,self.run_times):
                temp = self.start + timedelta(days=item)
                self.context.set_current_datetime(temp)
                self.handle_data(context)
                self.indicator_cal()
        self.after_end_operation()

    def indicator_cal(self):
        logger.info(context.current_datetime().strftime('%Y-%m-%d %H:%H:%S'))

        self.run_datetimes.append(context.current_datetime())

        #caculate daily value
        temp_value = 0
        for name,account in context.accounts.items():
            for name1,position in account.position.items():
                if position.asset != Symbol.USDT:
                    usdt_price = context.get_price("BTCUSDT")
                    t1 = position.available * usdt_price
                    temp_value = temp_value + (position.available * usdt_price)
                else:
                    temp_value = temp_value + position.available

        current_daily_value= round(temp_value, 5)
        logger.info("daily value:" + str(current_daily_value))
        self.daily_value.append(current_daily_value)

        # caculate daily return
        if len(self.daily_value) >= 2:
            last_daily_value = self.daily_value[-2]
            temp = (current_daily_value/
                                 last_daily_value) - 1
            temp = round(temp, 5)
            current_daily_return = temp
            logger.info("daily return:" + str(current_daily_return))
            self.daily_return.append(current_daily_return)

        #caculate benchmark daily return
        if len(self.daily_value) >= 2:
            temp_current_benchmark_index = context.get_benchmark_price()
            temp = (temp_current_benchmark_index/
                                             self.last_benchmark_index) -1
            current_benchmark_return = round(temp, 5)
            logger.info("daily benchmark return:" + str(current_benchmark_return))
            self.benchmark_daily_return.append(current_benchmark_return)


    def before_start_operation(self):
        #caculate start daily value
        temp_value = 0
        for name, account in context.accounts.items():
            for name1, position in account.position.items():
                if position.asset != Symbol.USDT:
                    usdt_price = context.get_price("BTCUSDT")
                    t1 = position.available * usdt_price
                    temp_value = temp_value + t1
                else:
                    temp_value = temp_value + position.available

        self.start_daily_value = round(temp_value, 5)
        logger.info("start daily value:" + str(self.start_daily_value))
        self.daily_value.append(self.start_daily_value)

        #get benchmark index
        self.start_benchmark_index = context.get_benchmark_price()
        self.last_benchmark_index = self.start_benchmark_index
        logger.info("start benchmark index:" + str(self.start_daily_value))

        #get the start prorfolio value equal to start daily value in usdt
        self.start_protfolio_value = self.start_daily_value
        logger.info("start prorfolio value:" + str(self.start_protfolio_value))

    def after_end_operation(self):
        #caculate total return
        if len(self.daily_value) >= 2 and self.start_daily_value:
            last_daily_value = self.daily_value[-1]
            temp = (last_daily_value /
                    self.start_daily_value) - 1
            temp = round(temp, 5)
            self.total_return = temp
        else:
            self.total_return = 0
        logger.info("total return:" + str(self.total_return))

        #caculate Total Annualized Returns
        if len(self.daily_value) >= 2 and self.start_daily_value:
            temp = pow((1 + self.total_return),365.0/self.run_duration_in_days) - 1
            temp = round(temp, 5)
            self.strategy_annualized_returns = temp
        else:
            self.strategy_annualized_returns = 0
        logger.info("Annualised Strategy Return:" + str(self.strategy_annualized_returns))

        #caculate Benchmark Annualized Returns
        if len(self.daily_value) >= 2 and self.start_daily_value:
            last_benchmart_value = context.get_benchmark_price()
            temp = (last_benchmart_value /
                    self.start_benchmark_index) - 1
            temp = round(temp, 5)
            self.annualised_benchmark_return = temp
        else:
            self.annualised_benchmark_return = 0
        logger.info("benchmark annualized return:" + str(self.annualised_benchmark_return))

        #caculate Algorithm Volatility
        df = pd.DataFrame({'date':self.run_datetimes,'rtn':self.daily_return})
        self.algorithm_volatility = df['rtn'].std() * math.sqrt(365)
        logger.info("Algorithm Volatility:" + str(self.algorithm_volatility))

        #caculate Benchmark Volatility
        df = pd.DataFrame({'date': self.run_datetimes, 'rtn': self.benchmark_daily_return})
        self.benchmark_volatility = df['rtn'].std() * math.sqrt(365)
        logger.info("Benchmark Volatility:" + str(self.benchmark_volatility))

        # caculate information ratio
        df = pd.DataFrame({'date': self.run_datetimes, 'rtn': self.daily_return,
                           'benchmark_rtn':self.benchmark_daily_return})
        df['diff'] = df['rtn'] - df['benchmark_rtn']
        aunual_mean = df['diff'].mean() * 365
        aunual_std = df['diff'].std() * math.sqrt(365)
        self.information_ratio = aunual_mean / aunual_std
        logger.info("Information Ratio:" + str(self.information_ratio))

        #caculate sharp ratio
        self.sharpe_ratio = (self.strategy_annualized_returns -
                             self.RF) / self.algorithm_volatility
        logger.info("Sharp Ratio:" + str(self.sharpe_ratio))

        #caculate beta
        df = pd.DataFrame({'date': self.run_datetimes, 'rtn': self.daily_return,
                           'benchmark_rtn': self.benchmark_daily_return})
        self.beta = df['rtn'].cov(df['benchmark_rtn']) / df['benchmark_rtn'].var()
        logger.info("Beta:" + str(self.beta))

        #caculate alpha
        self.alpha = self.strategy_annualized_returns - (self.RF + self.beta * (self.annualised_benchmark_return- self.RF))
        logger.info("Alpha:" + str(self.alpha))

        #caculate max drawdown
        df = pd.DataFrame({'date': self.run_datetimes, 'capital': self.daily_value[1:]})
        df.sort_values(by='date',inplace=True)
        df.reset_index(drop=True,inplace=True)

        df['max2here'] = df['capital'].cummax()
        df['dd2here'] = df['capital'] / df['max2here'] -1
        temp = df.sort_values(by='dd2here').iloc[0][['date','dd2here']]
        max_dd = temp['dd2here']
        end_date = temp['date']
        df = df[df['date'] <= end_date]
        start_date = df.sort_values(by='capital',ascending=False).iloc[0]['date']

        logger.info("Max Draw Down: " +str(max_dd)
                    + " start datetime:" + str(start_date)
                    + " end datetime:" + str(end_date))

        #caculate average change
        df = pd.DataFrame({'date': self.run_datetimes, 'rtn': self.daily_return})
        self.average_change = df['rtn'].mean()
        logger.info("average change:" + str(self.average_change))

        #caculate downside risk
        temp_strategy_return_length = len(self.daily_return)
        temp_value = 0
        for item_index in range(1,temp_strategy_return_length):
            temp_ave = np.mean(self.daily_return[0:item_index])
            if self.daily_return[item_index] <temp_ave:
                temp_value = temp_value + pow((self.daily_return[item_index] - temp_ave),2)
        self.downside_risk = math.sqrt(temp_value * 365 / temp_strategy_return_length)
        logger.info("downside risk:" + str(self.downside_risk))

        #caculate Sortino Ratio
        self.sortino_ratio = (self.strategy_annualized_returns - self.RF) / self.downside_risk
        logger.info("sortino ratio:" + str(self.downside_risk))

        df = pd.DataFrame({'date': self.run_datetimes, 'rtn': self.daily_return,
                           'benchmark_rtn': self.benchmark_daily_return})
        df['stock_cumret'] = (df['rtn'] + 1).cumprod()
        df['benchmark_cumret'] = (df['benchmark_rtn'] + 1).cumprod()

        df['stock_cumret'].plot(style='k-',figsize=(12,5))
        df['benchmark_cumret'].plot(style='k-', figsize=(12, 5))
        plt.show()


