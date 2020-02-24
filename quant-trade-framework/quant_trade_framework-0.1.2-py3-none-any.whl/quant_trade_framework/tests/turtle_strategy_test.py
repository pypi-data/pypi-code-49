# -*-coding:utf-8 -*-

# @Time    : 2020/2/16 15:49
# @File    : strategy_test_stock.py
# @User    : yangchuan
# @Desc    : 

from quant_trade_framework.stock.strategy import Strategy
from quant_trade_framework.common.constant import Constant
from quant_trade_framework.common.logConfig import Logger
from quant_trade_framework.gateway.jointquant.jqdata import JqDataCore
from quant_trade_framework.stock.parameters import OrderCost,SlipPage
from quant_trade_framework.stock.context import Context
import talib as ta
from quant_trade_framework.common.array_manager import ArrayManager
from quant_trade_framework.core.utility import DataFormater

logger = Logger.module_logger("system")
N20 = 20
N55 = 55
total_cash = 1000000
entryWindow = 20
exitWindow = 10
atrWindow = 20
def initialize(Context):
    Context.set_auth('admin','123456')
    Context.set_order_cost(
        cost=OrderCost(open_tax=0.001,
                  close_tax=0.001,
                  open_commission=0.0003,
                  close_commission=0.0003,
                  close_today_commission=0,
                  min_commission=5),
        type='all')

    Context.set_slippage(
        slippage=SlipPage(type=Constant.PRICE_RELATED_SLIPPAGE,
                 value=0.001),
        type='all'
    )
    Context.N = 20
    Context.N20 = 20
    Context.atrWindow = 10
    Context.ORIGINAL_CASH = 1000000
    close_data = JqDataCore.get_bars("000001.XSHE", Context.N, Context.current_datetime(), Constant.KLINE_INTERVAL_1DAY,
                                     fields=['close'])
    new_bar = Context.get_price("000001.XSHE", Context.run_freq)
    close_data = DataFormater.data_list_2_data_frame(close_data)
    temp_N = ta.SMA(close_data['close'], Context.N)
    temp_N = round(float(temp_N.tail(1)),2)
    # Context.UNIT= int(((Context.ORIGINAL_CASH * 0.1) / temp_N)/new_bar.close_price)
    Context.CURRENT_UNIT = 0
    Context.UNIT = 0

    Context.longEntry1 = 0
    Context.longEntry2 = 0
    Context.longEntry3 = 0
    Context.longEntry4 = 0

    Context.shortEntry1 = 0
    Context.shortEntry2 = 0
    Context.shortEntry3 = 0
    Context.shortEntry4 = 0

    Context.entryUp = 0
    Context.entryDown = 0
    Context.exitUp = 0
    Context.exitDown = 0
    Context.set_bar_cache_size(Context.N)




def handle_data(Context):
    if Context.UNIT == 0:
        new_bar = Context.get_price("000001.XSHE", Context.run_freq)
        temp_N = Context.bars.sma(20)
        Context.UNIT = int(((Context.ORIGINAL_CASH * 0.1) / temp_N) / new_bar.close_price)
    generateSignal(Context)
    indicator_cal(Context)


def generateSignal(Context):
    if not Context.longEntry1:
        return
    print(Context.current_datetime())
    new_bar = Context.get_price("000001.XSHE", Context.run_freq)
    print(new_bar.datetime)
    current_positon = Context.accounts["account1"].get_position("000001.XSHE")
    # 优先检查平仓
    if Context.CURRENT_UNIT > 0:
        longExit = max(Context.longStop, Context.exitDown)
        if new_bar.low_price <= longExit:
            Context.CURRENT_UNIT = 0
            Context.accounts["account1"].order_target("000001.XSHE",0)
            return
    elif current_positon['available'] < 0:
        shortExit = min(Context.shortStop, Context.exitUp)
        if new_bar.high_price >= shortExit:
            Context.CURRENT_UNIT = 0
            Context.accounts["account1"].order_target("000001.XSHE",0)
            return

    # 没有仓位或者持有多头仓位的时候，可以做多（加仓）
    if current_positon['available'] >= 0:
        trade = False
        print("high price:"+str(new_bar.high_price))
        print("longEntry1 price:" + str( Context.longEntry1))
        print("longEntry2 price:" + str(Context.longEntry2))
        print("longEntry3 price:" + str(Context.longEntry3))
        print("longEntry4 price:" + str(Context.longEntry4))
        print("current postion:" + str(current_positon['available']))
        print("Unit:" + str(Context.UNIT))
        if new_bar.high_price >= Context.longEntry1 and current_positon['available'] <= Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", Context.UNIT)
            trade = True

        if new_bar.high_price >= Context.longEntry2 and current_positon['available'] <= 2 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", Context.UNIT)
            trade = True

        if new_bar.high_price >= Context.longEntry3 and current_positon['available'] <= 3 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", Context.UNIT)
            trade = True

        if new_bar.high_price >= Context.longEntry3 and current_positon['available'] <= 4 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", Context.UNIT)
            trade = True

        if trade:
            return

    # 没有仓位或者持有空头仓位的时候，可以做空（加仓）
    if current_positon['available'] <= 0:
        if new_bar.low_price <= Context.shortEntry1 and current_positon['available'] > - 1 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", - Context.UNIT)

        if new_bar.low_price <= Context.shortEntry2 and current_positon['available'] > - 2 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", - Context.UNIT)

        if new_bar.low_price <= Context.shortEntry3 and current_positon['available'] > - 3 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", - Context.UNIT)

        if new_bar.low_price <= Context.shortEntry4 and current_positon['available'] > - 4 * Context.UNIT:
            Context.accounts["account1"].order_target("000001.XSHE", - Context.UNIT)

def indicator_cal(Context):
    current_positon = Context.accounts["account1"].get_position("000001.XSHE")
    # if current_positon["available"] == 0:
    Context.entryUp, Context.entryDown = Context.bars.donchian(Context.N)
    Context.entryMiddle = (Context.entryUp + Context.entryDown) / 2
    Context.exitUp, Context.exitDown = Context.bars.donchian(15)

    Context.atrVolatility = Context.bars.atr(Context.atrWindow)

    Context.longEntry1 = Context.entryUp
    Context.longEntry2 = Context.entryUp + Context.atrVolatility * 0.5
    Context.longEntry3 = Context.entryUp + Context.atrVolatility * 1
    Context.longEntry4 = Context.entryUp + Context.atrVolatility * 1.5
    Context.longStop = 0

    Context.shortEntry1 = Context.entryDown
    Context.shortEntry2 = Context.entryDown - Context.atrVolatility * 0.5
    Context.shortEntry3 = Context.entryDown - Context.atrVolatility * 1
    Context.shortEntry4 = Context.entryDown - Context.atrVolatility * 1.5
    Context.shortStop = 0

    logger.info("atrVolatility:" + str(Context.atrVolatility))
    logger.info("longEntry1:" + str(Context.longEntry1))
    logger.info("longEntry2:" + str(Context.longEntry2))
    logger.info("longEntry3:" + str(Context.longEntry3))
    logger.info("longEntry4:" + str(Context.longEntry4))
    logger.info("shortEntry1:" + str(Context.shortEntry1))
    logger.info("shortEntry2:" + str(Context.shortEntry2))
    logger.info("shortEntry3:" + str(Context.shortEntry3))
    logger.info("shortEntry4:" + str(Context.shortEntry4))


my_strategy = Strategy()
my_strategy.create_account(
    "account1",
    10000000.0,
    "stock"
)

universe = my_strategy.create_universe(['000001.XSHE'])

my_strategy.create_strategy(
    initialize,
    handle_data,
    universe=universe,
    benchmark='csi5',
    frequency=Constant.RUN_FREQ_DAY,
    refresh_rate=1
)
my_strategy.backtest(
    strategy=my_strategy,
    start="2019-11-04",
    end="2020-02-01",
    commission={'taker': 0.0002, 'maker': 0.0002},
    run_at_time="15:15:00"
)