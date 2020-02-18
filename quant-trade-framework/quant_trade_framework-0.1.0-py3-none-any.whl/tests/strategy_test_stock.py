# -*-coding:utf-8 -*-

# @Time    : 2020/2/16 15:49
# @File    : strategy_test_stock.py
# @User    : yangchuan
# @Desc    : 

from quant_trade_framwork.stock.strategy import strategy
from quant_trade_framwork.common.constant import Constant
from quant_trade_framwork.common.logConfig import Logger
from quant_trade_framwork.gateway.jointquant.jqdata import JqDataCore
from quant_trade_framwork.stock.parameters import OrderCost,SlipPage

logger = Logger.module_logger("system")
def initialize(context):
    context.set_auth('admin','123456')
    context.N = 20
    context.k = 2
    context.set_order_cost(
        cost=OrderCost(open_tax=0.001,
                  close_tax=0.001,
                  open_commission=0.0003,
                  close_commission=0.0003,
                  close_today_commission=0,
                  min_commission=5),
        type='all')

    context.set_slippage(
        slippage=SlipPage(type=Constant.PRICE_RELATED_SLIPPAGE,
                 value=0.001),
        type='all'
    )

def handle_data(context):
    close_data = JqDataCore.get_bars("000001.XSHE",10,context.current_datetime(),Constant.KLINE_INTERVAL_1DAY,fields=['close'])
    temp_price = close_data['close'].mean()
    # 取得过去五天的平均价格
    MA10 = close_data['close'].mean()
    current_price = close_data['close'].iloc[-1]
    current_account = context.get_account('account1')
    cash = current_account.balance
    # 如果上一时间点价格高出五天平均价1%, 则全仓买入
    if (current_price > 1.01 * MA10) and (cash > 0):
        print("buy")
        current_account.order_value("000001.XSHE", cash/2)
    elif current_price < MA10 and \
            "000001.XSHE" in current_account.position \
            and current_account.position["000001.XSHE"].count > 0:
        print("sell")
        current_account.order_target("000001.XSHE", 0)

my_strategy = strategy()
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
    start="2019-10-01",
    end="2020-02-01",
    commission={'taker': 0.0002, 'maker': 0.0002},
    run_at_time="15:15:00"
)