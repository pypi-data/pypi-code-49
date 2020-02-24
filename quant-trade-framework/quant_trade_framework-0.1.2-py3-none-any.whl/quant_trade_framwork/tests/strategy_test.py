# -*-coding:utf-8 -*-

# @Time    : 2020/2/9 14:59
# @File    : strategy_test.py
# @User    : yangchuan
# @Desc    : 
from quant_trade_framwork.btc import strategy
from quant_trade_framwork.common import Constant
from quant_trade_framwork.common import Logger
logger = Logger.module_logger("system")
def initialize(context):

    context.N = 20
    context.k = 2
    # context.account = context.get_account('account1')

def handle_data(context):
    context.get_price("BTCUSDT")

my_strategy = strategy()
my_strategy.create_account(
    "account1",
    "btc",
    "digital.spot",
    [{'asset': 'BTC', 'qty': 10},{'asset': 'USDT', 'qty': 50000}]
)

universe = my_strategy.create_universe(['BTC/USDT.binance'])
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
    start="2020-01-01",
    end="2020-02-01",
    commission={'taker': 0.0002, 'maker': 0.0002}
)