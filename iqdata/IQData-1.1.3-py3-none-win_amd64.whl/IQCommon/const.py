# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：const.py
# 摘    要：const 模块
#
# 当前版本：V1.0.0
# 作    者：qianmx21829
# 完成日期：2018-10-08
# 备    注：常量定义
###############################################################################

from enum import Enum
import operator

import numpy as np

ENCODE_TYPE = 'UTF-8'
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
NEED_EXCEPTION_HANDLE = '_handle_iq_exception'
EXC_EXT_NAME = 'iq_exec'
DEFAULT_EXC_TYPE = 'NOTSET'
USER_STRATEGY_NAME = "strategy.py"
STOCK_TICK_BEGIN_TIME = 930

fq_enum = ['pre', 'post', 'dypre', None]
t0_symbol_set = {'510900.XSHG', '513030.XSHG', '513100.XSHG', '513500.XSHG'}


NULL_SET = {'None', None, '', 'null', 'NULL'}

# 市场别名字典
MARKET_ALIAS = {
    '.SS': '.XSHG',
    '.SZ': '.XSHE'
}

FREQUENCY_EXCHANGE = {
    'daily': '1d',
    'minute': '1m',
}

MARKET_ALIAS_REVERT = {
    v: k
    for k, v in MARKET_ALIAS.items()
}

# 系统动态释放进程间隔时间
SYSTEM_CHECK_CYCLE = 5

# 系统性能分析选项，配合add_profile装饰器使用
SYSTEM_PROFILE = True

# 默认插件优先级
DEFAULT_PRIORITY = 50

# fly计算除权的字段
CAL_EXRIGHTS_COLUMNS = [
    "open", "close", "high", "low"
]


class IQEnum(Enum):
    """
    自定义枚举类型，重写__repr__方法
    """

    def __repr__(self):
        """
        __repr__方法
        :return: 返回值字符串中删除对self._value_的显示
        """
        return "'%s'" % self.value


class ExcType(IQEnum):
    """
    运行类型，包括用户类型、系统类型、未设置类型
    """
    USER_EXC = "USER_EXC"
    SYSTEM_EXC = "SYSTEM_EXC"
    NOTSET = "NOTSET"


class ExitCode(IQEnum):
    EXIT_SUCCESS = "EXIT_SUCCESS"
    EXIT_USER_ERROR = "EXIT_USER_ERROR"
    EXIT_INTERNAL_ERROR = "EXIT_INTERNAL_ERROR"


class AssetType(IQEnum):
    STOCK = "STOCK"      # 股票
    FUTURE = "FUTURE"    # 期货
    INDEX = "INDEX"      # 指数
    ETF = "ETF"          # ETF
    OPTION = "OPTION"    # 期权


class Frequency(IQEnum):
    DAILY = '1d'
    MINUTE = '1m'
    TICK = 'tick'
    MINUTE5 = '5m'
    MINUTE15 = '15m'
    MINUTE30 = '30m'
    MINUTE60 = '60m'



class ExecutionPhase(IQEnum):
    """
    运行阶段枚举
    """
    GLOBAL = "[全局]"
    INITIALIZE = "[程序初始化]"
    BEFORE_TRADING_START = "[日内交易前]"
    ON_HANDLE_AUCTION = "[集合竞价]"
    ON_HANDLE_DATA = "[盘中 handle_data 函数]"
    ON_HANDLE_TICK = "[盘中 handle_tick 函数]"
    ON_ORDER_RSP = "[盘中 委托主推]"
    ON_TRADE_RSP = "[盘中 交易主推]"
    AFTER_TRADING_END = "[日内交易后]"
    FINALIZED = "[程序结束]"
    SCHEDULED = "[scheduler函数内]"


class EncryptType(IQEnum):
    """
    策略加密模式
    """
    AES = 'AES'
    DES = 'DES'


class RunType(IQEnum):
    """
    运行类型枚举类
    """
    # 回测
    BACKTEST = "BACKTEST"
    # 仿真
    SIMULATION = "SIMULATION"
    # 交易
    TRADING = 'TRADING'
    # 因子加工
    FACTOR = 'FACTOR'
    # 混合模式（因子加工与回测的混合模式）
    MIXING = 'MIXING'


class FactorCalcMode(IQEnum):
    """
    因子计算模式，包括加工模式、生产模式
    """
    # 加工模式
    PROCESS_MODE = "PROCESS_MODE"
    # 生产模式
    PRODUCTION_MODE = "PRODUCTION_MODE"


class LevelType(IQEnum):
    """
    行情的level类
    """
    LEVEL1 = "LEVEL1"
    LEVEL2 = "LEVEL2"


class EntrustDirection(IQEnum):
    """
    委托方向枚举类
    """
    BUY = "BUY"      # 买
    SELL = "SELL"    # 卖


class FuturesDirection(IQEnum):
    """
    开平方向枚举类
    """
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    CLOSE_TODAY = "CLOSE_TODAY"


class HedgeType(IQEnum):
    """
    对冲类型
    """
    SPECULATION = "SPECULATION"    # 投机
    HEDGE = "HEDGE"                # 套保
    ARBITRAGE = "ARBITRAGE"        # 套利
    MARKETMAKER = "MARKETMAKER"    # 做市
    COVERED = "COVERED"            # 备兑


class OptionProperty(IQEnum):
    """
    期权合约属性
    """
    CALL = "CALL"    # 认购
    PUT = "PUT"      # 认沽


class PositionType(IQEnum):
    """
    持仓类型
    """
    RIGHT = "Right"    # 权利仓
    VOLUNTARY = "Voluntary"    # 义务仓
    COVERED = "Covered"        # 备兑仓


class AccountType(IQEnum):
    """
    账户类型
    """
    # TOTAL = 0
    BENCHMARK = "BENCHMARK"
    # 股票
    STOCK = "STOCK"
    # 期货
    FUTURE = "FUTURE"
    # 期权
    OPTION = "OPTION"


class DaysCount(IQEnum):
    DAYS_A_YEAR = 250
    TRADING_DAYS_A_YEAR = 252


class OrderType(IQEnum):
    MARKET = "MARKET"    # 市价
    LIMIT = "LIMIT"      # 现价
    GEAR = "GEAR"        # 档位


class OrderProperty(IQEnum):
    """
    订单属性
    """
    CURRENT = 0
    NEXT = 1     # 隔夜单


class OrderStatus(IQEnum):
    UNREPORTED = 0      # 未报
    TOBEREPORTED = 1    # 待报
    REPORTED = 2        # 已报
    CANCEL_REPORTED = 3  # 已报待撤
    CANCEL_PART_FILLED = 4  # 部成待撤
    PART_CANCEL = 5     # 部撤
    CANCELLED = 6       # 已撤
    PART_FILLED = 7     # 部成
    FILLED = 8          # 已成
    REJECTED = 9        # 废单


class CommissionType(IQEnum):
    """
    手续费计算类型
    """
    BY_MONEY = "BY_MONEY"
    BY_VOLUME = "BY_VOLUME"


class MarginType(IQEnum):
    """
    保证金类型
    """
    BY_MONEY = "BY_MONEY"
    BY_VOLUME = "BY_VOLUME"


class CompanyEnum(IQEnum):
    """
    公司/机构号枚举类，由代码动态生成
    """
    pass


class MatcherType(IQEnum):
    CURRENT_BAR_CLOSE = "CLOSE"
    CURRENT_BAR_OPEN = "OPEN"
    CURRENT_BAR_HIGH = "HIGH"
    CURRENT_BAR_LOW = "LOW"
    NEXT_BAR_OPEN = "NEXT_OPEN"
    NEXT_BAR_CLOSE = "NEXT_CLOSE"
    NEXT_BAR_HIGH = "NEXT_HIGH"
    NEXT_BAR_LOW = "NEXT_LOW"

    # NEXT_TICK_LAST = "NEXT_TICK_LAST"
    # NEXT_TICK_BEST_OWN = "NEXT_TICK_BEST_OWN"
    # NEXT_TICK_BEST_COUNTERPARTY = "NEXT_TICK_BEST_COUNTERPARTY"


class CompareEnum(IQEnum):
    LT = '<', operator.lt
    LE = '<=', operator.le
    GT = '>', operator.gt
    GE = '>=', operator.ge


class BarDataEnum(IQEnum):
    DATETIME = "datetime"
    OPEN = "open"
    CLOSE = "close"
    HIGH = "high"
    LOW = "low"
    AMOUNT = "amount"
    BALANCE = "balance"
    SETTLEMENT = "settlement"
    PREV_SETTLEMENT = "prev_settlement"
    OPEN_INTEREST = "open_interest"
    LIMIT_UP = "limit_up"
    LIMIT_DOWN = "limit_down"

    TRADE_MINS = "trade_mins"
    TRADE_STATUS = "trade_status"
    PRECLOSE = "preclose"
    LAST = "last"
    AVG = "avg"
    WAVG = "wavg"
    BUSINESS_COUNT = "business_count"
    CURRENT_AMOUNT = "current_amount"
    BUSINESS_AMOUNT_IN = "business_amount_in"
    BUSINESS_AMOUNT_OUT = "business_amount_out"
    ISSUEDATE = "issueDate"
    TURNOVER_RATIO = "turnover_ratio"
    A1 = "a1"
    A2 = "a2"
    A3 = "a3"
    A4 = "a4"
    A5 = "a5"
    A1_V = "a1_v"
    A2_V = "a2_v"
    A3_V = "a3_v"
    A4_V = "a4_v"
    A5_V = "a5_v"
    B1 = "b1"
    B2 = "b2"
    B3 = "b3"
    B4 = "b4"
    B5 = "b5"
    B1_V = "b1_v"
    B2_V = "b2_v"
    B3_V = "b3_v"
    B4_V = "b4_v"
    B5_V = "b5_v"

    PROD_CODE = "prod_code"
    BID_GRP = "bid_grp"
    OFFER_GRP = "offer_grp"
    AMOUNT_POSITION = "amount_postion"  # 实时行情中的,非business_amount,应该是持仓量


class ExchangeType(IQEnum):
    CCFX = 'CCFX'    # 中金所
    XDCE = 'XDCE'    # 大商所
    XZCE = 'XZCE'    # 郑商所
    XSGE = 'XSGE'    # 上期所
    XSHG = 'XSHG'    # 上交所
    XSHE = 'XSHE'    # 深交所


class IQEStatus(IQEnum):
    UNINITIALISED = -1
    IDLE = 0
    INITIALISE = 1
    RUNNING = 5
    END = 10


class RunningMode(IQEnum):
    MULTI_PROCESS = 'process'
    MULTI_THREAD = 'thread'


class PositionFrequency(IQEnum):
    """
    调仓频率类型
    """
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    QUARTERLY = 3
    SEMIANNUALLY = 4
    ANNUALLY = 5


# 股票池类型，'ALL': 全市场股票, 'HS300': 沪深300, 'ZZ500': 中证500, 'SZ50': 上证50
UniverseType = ["ALL", "HS300", "ZZ500", "SZ50"]

ACCOUNT_FIELDS_MAP = {
    # AccountType.STOCK.value: ['dividend_receivable'],
    AccountType.FUTURE.value: ['holding_pnl', 'realized_pnl', 'daily_pnl', 'margin'],
}

POSITION_FIELDS_MAP = {
    AccountType.STOCK.value: [
        'amount', 'last_price', 'avg_price', 'market_value', 'sellable'
    ],
    AccountType.FUTURE.value: [
        'margin', 'margin_rate', 'contract_multiplier', 'last_price',
        'buy_pnl', 'buy_margin', 'buy_amount', 'buy_avg_open_price',
        'sell_pnl', 'sell_margin', 'sell_amount', 'sell_avg_open_price',
        'buy_today_amount', 'sell_today_amount'
    ],
    AccountType.OPTION.value: [
            'market_value', 'buy_market_value', 'sell_market_value', 'contract_multiplier',
            'buy_holding_pnl', 'sell_holding_pnl', 'buy_realized_pnl', 'sell_realized_pnl',
            'holding_pnl', 'realized_pnl', 'buy_daily_pnl', 'sell_daily_pnl', 'daily_pnl',
            'buy_pnl', 'sell_pnl', 'pnl', 'buy_open_order_amount', 'sell_open_order_amount',
            'buy_close_order_amount', 'sell_close_order_amount', 'buy_amount', 'sell_amount',
            'closable_buy_amount', 'closable_sell_amount', 'margin', 'premium', 'option_property',
            'buy_avg_holding_price', 'sell_avg_holding_price', 'buy_avg_open_price', 'last_price',
            'sell_avg_open_price', 'buy_transaction_cost', 'sell_transaction_cost',
        ],
}


class ExceptType(IQEnum):
    """
    异常类型
    """
    EXCEPT_USER = "EXCEPT_USER"
    EXCEPT_SYSTEM = "EXCEPT_SYSTEM"
    NOTSET = "NOTSET"


# 除权除息计算方式
DIVIDEND_CALC_TYPE = ['pre', 'post', 'dypre', None]

# 历史行情的字段
VALID_HISTORY_FIELDS = [
    'datetime', 'open', 'close', 'high', 'low', 'amount', 'balance'
]


# 后续需要添加其他合约类型，其他周期频率的枚举
DATA_INDEX = [
    (AssetType.STOCK.value, Frequency.DAILY.value),
    (AssetType.STOCK.value, Frequency.MINUTE.value),
    (AssetType.FUTURE.value, Frequency.DAILY.value),
    (AssetType.FUTURE.value, Frequency.MINUTE.value),
    (AssetType.INDEX.value, Frequency.DAILY.value),
    (AssetType.INDEX.value, Frequency.MINUTE.value),
    (AssetType.ETF.value, Frequency.DAILY.value),
    (AssetType.ETF.value, Frequency.MINUTE.value),
    (AssetType.OPTION.value, Frequency.DAILY.value),
    (AssetType.OPTION.value, Frequency.MINUTE.value),
    (AssetType.STOCK.value, Frequency.MINUTE5.value),
    (AssetType.STOCK.value, Frequency.MINUTE15.value),
    (AssetType.STOCK.value, Frequency.MINUTE30.value),
    (AssetType.STOCK.value, Frequency.MINUTE60.value),
    (AssetType.FUTURE.value, Frequency.MINUTE5.value),
    (AssetType.FUTURE.value, Frequency.MINUTE15.value),
    (AssetType.FUTURE.value, Frequency.MINUTE30.value),
    (AssetType.FUTURE.value, Frequency.MINUTE60.value),
    (AssetType.INDEX.value, Frequency.MINUTE5.value),
    (AssetType.INDEX.value, Frequency.MINUTE15.value),
    (AssetType.INDEX.value, Frequency.MINUTE30.value),
    (AssetType.INDEX.value, Frequency.MINUTE60.value),
    (AssetType.ETF.value, Frequency.MINUTE5.value),
    (AssetType.ETF.value, Frequency.MINUTE15.value),
    (AssetType.ETF.value, Frequency.MINUTE30.value),
    (AssetType.ETF.value, Frequency.MINUTE60.value),
    (AssetType.OPTION.value, Frequency.MINUTE5.value),
    (AssetType.OPTION.value, Frequency.MINUTE15.value),
    (AssetType.OPTION.value, Frequency.MINUTE30.value),
    (AssetType.OPTION.value, Frequency.MINUTE60.value)
]

# 后续需要添加其他合约类型，其他周期频率的枚举
DATA_INDEX_STR = [
    "('%s','%s')" % (AssetType.STOCK.value, Frequency.DAILY.value),
    "('%s','%s')" % (AssetType.STOCK.value, Frequency.MINUTE.value),
    "('%s','%s')" % (AssetType.FUTURE.value, Frequency.DAILY.value),
    "('%s','%s')" % (AssetType.FUTURE.value, Frequency.MINUTE.value),
    "('%s','%s')" % (AssetType.INDEX.value, Frequency.DAILY.value),
    "('%s','%s')" % (AssetType.INDEX.value, Frequency.MINUTE.value),
    "('%s','%s')" % (AssetType.ETF.value, Frequency.DAILY.value),
    "('%s','%s')" % (AssetType.ETF.value, Frequency.MINUTE.value),
    "('%s','%s')" % (AssetType.OPTION.value, Frequency.DAILY.value),
    "('%s','%s')" % (AssetType.OPTION.value, Frequency.MINUTE.value),
    "('%s','%s')" % (AssetType.STOCK.value, Frequency.MINUTE5.value),
    "('%s','%s')" % (AssetType.STOCK.value, Frequency.MINUTE15.value),
    "('%s','%s')" % (AssetType.STOCK.value, Frequency.MINUTE30.value),
    "('%s','%s')" % (AssetType.STOCK.value, Frequency.MINUTE60.value),
    "('%s','%s')" % (AssetType.FUTURE.value, Frequency.MINUTE5.value),
    "('%s','%s')" % (AssetType.FUTURE.value, Frequency.MINUTE15.value),
    "('%s','%s')" % (AssetType.FUTURE.value, Frequency.MINUTE30.value),
    "('%s','%s')" % (AssetType.FUTURE.value, Frequency.MINUTE60.value),
    "('%s','%s')" % (AssetType.INDEX.value, Frequency.MINUTE5.value),
    "('%s','%s')" % (AssetType.INDEX.value, Frequency.MINUTE15.value),
    "('%s','%s')" % (AssetType.INDEX.value, Frequency.MINUTE30.value),
    "('%s','%s')" % (AssetType.INDEX.value, Frequency.MINUTE60.value),
    "('%s','%s')" % (AssetType.ETF.value, Frequency.MINUTE5.value),
    "('%s','%s')" % (AssetType.ETF.value, Frequency.MINUTE15.value),
    "('%s','%s')" % (AssetType.ETF.value, Frequency.MINUTE30.value),
    "('%s','%s')" % (AssetType.ETF.value, Frequency.MINUTE60.value),
    "('%s','%s')" % (AssetType.OPTION.value, Frequency.MINUTE5.value),
    "('%s','%s')" % (AssetType.OPTION.value, Frequency.MINUTE15.value),
    "('%s','%s')" % (AssetType.OPTION.value, Frequency.MINUTE30.value),
    "('%s','%s')" % (AssetType.OPTION.value, Frequency.MINUTE60.value)
]

# 后续需要添加其他合约类型，其他周期频率的枚举
DATA_INDEX_DICT = {
    (AssetType.STOCK.value, Frequency.DAILY.value): 0,
    (AssetType.STOCK.value, Frequency.MINUTE.value): 1,
    (AssetType.FUTURE.value, Frequency.DAILY.value): 2,
    (AssetType.FUTURE.value, Frequency.MINUTE.value): 3,
    (AssetType.INDEX.value, Frequency.DAILY.value): 4,
    (AssetType.INDEX.value, Frequency.MINUTE.value): 5,
    (AssetType.ETF.value, Frequency.DAILY.value): 6,
    (AssetType.ETF.value, Frequency.MINUTE.value): 7,
    (AssetType.OPTION.value, Frequency.DAILY.value): 8,
    (AssetType.OPTION.value, Frequency.MINUTE.value): 9,
    (AssetType.STOCK.value, Frequency.MINUTE5.value): 10,
    (AssetType.STOCK.value, Frequency.MINUTE15.value): 11,
    (AssetType.STOCK.value, Frequency.MINUTE30.value): 12,
    (AssetType.STOCK.value, Frequency.MINUTE60.value): 13,
    (AssetType.FUTURE.value, Frequency.MINUTE5.value): 14,
    (AssetType.FUTURE.value, Frequency.MINUTE15.value): 15,
    (AssetType.FUTURE.value, Frequency.MINUTE30.value): 16,
    (AssetType.FUTURE.value, Frequency.MINUTE60.value): 17,
    (AssetType.INDEX.value, Frequency.MINUTE5.value): 18,
    (AssetType.INDEX.value, Frequency.MINUTE15.value): 19,
    (AssetType.INDEX.value, Frequency.MINUTE30.value): 20,
    (AssetType.INDEX.value, Frequency.MINUTE60.value): 21,
    (AssetType.ETF.value, Frequency.MINUTE5.value): 22,
    (AssetType.ETF.value, Frequency.MINUTE15.value): 23,
    (AssetType.ETF.value, Frequency.MINUTE30.value): 24,
    (AssetType.ETF.value, Frequency.MINUTE60.value): 25,
    (AssetType.OPTION.value, Frequency.MINUTE5.value): 26,
    (AssetType.OPTION.value, Frequency.MINUTE15.value): 27,
    (AssetType.OPTION.value, Frequency.MINUTE30.value): 28,
    (AssetType.OPTION.value, Frequency.MINUTE60.value): 29
}

# 除权除息信息中的字段
DIVIDEND_COLUMNS = [
    'allotted_ps', 'rationed_px', 'rationed_ps', 'bonus_ps',
    'exer_forward_a', 'exer_forward_b', 'exer_backward_a', 'exer_backward_b'
]

# 空的行情bar
EMPTY_BAR_NP_ARRAY = np.array([], dtype=np.dtype([
    ('datetime', np.int64),
    ('open', float),
    ('close', float),
    ('high', float),
    ('low', float),
    ('amount', float),
    ('balance', float),
    ('is_open', np.int64),
    ('price', float),
    ('last', float)]))

EMPTY_BAR_NP_BAR = np.array([(0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0, np.nan, np.nan)] , dtype=np.dtype([
    ('datetime', np.int64),
    ('open', float),
    ('close', float),
    ('high', float),
    ('low', float),
    ('amount', float),
    ('balance', float),
    ('is_open', np.int64),
    ('price', float),
    ('last', float)]))[0]

# H5空的行情ndarray
H5_EMPTY_BAR_NP_ARRAY = np.array([], dtype=np.dtype([
    ('datetime', np.int64),
    ('open', float),
    ('close', float),
    ('high', float),
    ('low', float),
    ('amount', np.int64),
    ('balance', np.int64),
    ('price', float),
    ('last', float),
    ('high_limit', float),
    ('low_limit', float),
    ('open_interest', np.int64),  # 持仓量
    ('basis_spread', float),
    ('settlement', float),
    ('prev_settlement', float)]))


class StoreType(IQEnum):
    """
    存储格式
    """
    BCOLZ = 10    # bcolz格式数据
    PICKLE = 20   # pickle格式数据


class DataType(IQEnum):
    """
    数据类别
    """
    QUOTE = 100    # 行情数据
    FACTOR = 200   # 因子数据
    BASE = 300     # 基础数据


class EngineEnum(IQEnum):

    IQENGINE = 0
    RQALPHA = 1


class MethodType(IQEnum):
    """
    对接数据服务method定义
    """

    # 事件URL定义
    EVENT_TYPE = "get_event_type"
    EVENT_DATE = "get_event_by_date"
    EVENT_PEROID = "get_event_by_date"
    EVENT_COUNT = "get_event_by_num"
    EVENT_SECURITY = "get_eventstock_by_period"
    EVENT_TOP = "get_hotissue_top3_by_ date"
    EVENT_POEVENT = "get_poeventnum_by_period"
    EVENT_NGEVENT = "get_ngeventnum_by_period"

    # 图谱URL定义
    KG_INDUSTRY_CHAIN = "getCompanyIndustryChain"
    KG_PRODUCT_INDUSTRY_CHAIN = "getCompanyProductIndustryChain"
    KG_COMPANY_SHARE = "queryCompanyShareHold"


def format_engine(engine):
    try:
        return int(engine)
    except (ValueError, TypeError):
        try:
            return EngineEnum[engine.upper()].value
        except (TypeError, KeyError):
            return 0


class IQLogType(IQEnum):
    IQLOG_SYSTEM = 'system'
    IQLOG_USER = 'user'
    IQLOG_ERROR = 'error'


class IQEventResultType(IQEnum):
    IQEVENT_RESULT_LOGSYS = 'log_sys'
    IQEVENT_RESULT_LOGUSER = 'log_user'
    IQEVENT_RESULT_LOGERROR = 'log_error'
    IQEvent_RESULT_DATA = 'data'
    IQEVENT_RESULT_PROGRESS = 'progress'
    IQEVENT_RESULT_RISK = 'risk_result'
    IQEVENT_RESULT_SUMMARY = 'summary'
    IQEVENT_RESULT_BPORTFOLIO = 'benchmark_portfolio'
    IQEVENT_RESULT_PROFIT = 'profit_result'


WORK_PATH = './'


CONFIG_FILE_NAME = (
    DEFAULT_BACKTEST_CONFIG,
    DEFAULT_SIMULATION_CONFIG,
    DEFAULT_TRADING_CONFIG,
    DEFAULT_FACTOR_CONFIG,
    DEFAULT_MIXING_CONFIG,
) = (
    'backtest.yml',
    None,
    None,
    'factor.yml',
    None,
)
