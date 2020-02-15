# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：interface.py
# 摘    要：接口定义
#
# 当前版本：V0.0.1
# 作    者：lishuai14461
# 完成日期：2019-07-15
# 备    注：
###############################################################################

import abc
import six


class AbstractBasicsData(six.with_metaclass(abc.ABCMeta)):
    """
    基础数据接口类，需要扩展时，继承该类即可
    """

    @abc.abstractmethod
    def get_all_securities(self, types=None, date=None):
        """
        获取所有标的的基础信息

        :param types:  标的分类，值域范围：'stock', 'index', 'futures', 'options', 'etf'，可以任意组合，默认返回所有股票的基础信息
        :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型
        :return: list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_security_info(self, security):
        """
        获取指定标的的基础信息
        :param security:   标的代码
        :return:
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_all_stocks(self, types='A', date=None):
    #     """
    #     获取所有类型的市场成分股股票列表
    #     :param types:   标的分类，值域范围：'A': 所有A股, 'B': 所有B股, 默认返回所有A股的成分股
    #     :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
    #     :return: list
    #     """
    #     raise NotImplementedError

    @abc.abstractmethod
    def get_Ashares(self, date=None):
        """
        获取所有A股的成分列表
        :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
        :return: list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_Bshares(self, date=None):
        """
        获取所有A股的成分列表
        :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
        :return: list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_exrights_info(self, security, date=None):
        """
        获取标的的除权除息信息
        :param security:   标的代码
        :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
        :return: dict
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_dividend_df(self, security, date=None):
    #     """
    #     获取标的的除权除息信息
    #     :param security:   标的代码
    #     :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
    #     :return: pandas.DataFrame
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_st_stock_dates(self, security):
    #     """
    #     获取标的被ST的日期列表
    #     :param security:   标的代码
    #     :return: list
    #     """
    #     raise NotImplementedError
    #
    # @abc.abstractmethod
    # def get_suspended_dates(self, security):
    #     """
    #     获取标的停牌日期列表
    #     :param security:   标的代码
    #     :return: list
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_merger_info(self, security, date=None):
    #     """
    #     获取标的指定日期的合股信息
    #     :param security:   标的代码
    #     :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
    #     :return: dict
    #     """
    #     raise NotImplementedError

    @abc.abstractmethod
    def is_st(self, security, date=None):
        """
        检查标的是否ST股
        :param security:   标的代码
        :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
        :return: bool
        """
        raise NotImplementedError

    @abc.abstractmethod
    def is_suspended(self, security, date=None):
        """
        检查标的是否停牌
        :param security:   标的代码
        :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
        :return: bool
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_security_margin(self, security, date=None):
    #     """
    #     获取标的保证金信息
    #     :param security:   标的代码
    #     :param date:   查询日期，支持str|int|datetime.datetime|datetime.date多种数据类型, 默认取当天
    #     :return: dict
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_commission_info(self, trade_code):
    #     """
    #     获取标的佣金比率信息
    #     :param trade_code:  交易代码
    #     :return:
    #     """
    #     raise NotImplementedError


class AbstractDataSource(six.with_metaclass(abc.ABCMeta)):
    """
    行情数据接口类，需要扩展时，继承该类即可
    """

    @abc.abstractmethod
    def get_trading_dates(self, start_date=None, end_date=None):
        """
        获取指定日期范围内的所有交易日信息
        :param start_date:  开始日期，默认1990年开始
        :param end_date:    结束日期，默认当天
        :return:  list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_previous_trading_date(self, date, offset=1):
        """
        获取指定日期前推N天的交易日信息
        :param date:     开始日期
        :param offset:   日期偏移量，默认一天
        :return:  datetime.date
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_trading_date(self, date, offset=1):
        """
        获取指定日期后推N天的交易日信息
        :param date:     开始日期
        :param offset:   日期偏移量，默认一天
        :return:  datetime.date
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_trading_days(self, date=None, offset=0):
    #     """
    #     获取指定日期推算N天的所有交易日信息
    #     :param date:     开始日期, 默认取当天
    #     :param offset:   日期偏移量，>1向后推算N天，<1向前推算N天，默认为0
    #     :return:  list
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def available_data_range(self, frequency='1d'):
    #     """
    #     获取指定周期频率的数据有效范围
    #     :param frequency:    周期频率，默认日线
    #     :return: tuple
    #     """
    #     raise NotImplementedError

    @abc.abstractmethod
    def get_history(self, security, count, frequency='1d', fields=None, end_date=None, fq=None, skip_suspended=False):
        """
        获取历史行情
        :param security:    标的代码或代码列表
        :param count:       查询条数
        :param frequency:   周期频率,支持'1d', '1m'，默认1d
        :param fields:      指明数据结果集中所支持输出字段，支持的值域范围：
        open  -- 开盘价；
        high  -- 最高价；
        low   -- 最低价；
        close -- 收盘价；
        volume-- 交易量；
        money -- 交易金额；
        price -- 最新价；
        :param end_date:    查询日期，默认当天
        :param fq:          复权选项，pre:前复权，post:后复权，dypre:动态前复权，None:不复权
        :param skip_suspended:    是否跳过停牌日, 默认False不跳过停牌日
        :return:    numpy.array
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_price(self, security, start_date, end_date=None, frequency='1d', fields=None,
                  fq=None, skip_suspended=False):
        """
        获取历史行情
        :param security:    标的代码或代码列表
        :param start_date:  开始日期
        :param end_date:    查询日期，默认当天
        :param frequency:   周期频率,支持'1d', '1m'，默认1d
        :param fields:      指明数据结果集中所支持输出字段，支持的值域范围：
        open  -- 开盘价；
        high  -- 最高价；
        low   -- 最低价；
        close -- 收盘价；
        volume-- 交易量；
        money -- 交易金额；
        price -- 最新价；
        :param fq:          复权选项，pre:前复权，post:后复权，dypre:动态前复权，None:不复权
        :param skip_suspended:    是否跳过停牌日, 默认False不跳过停牌日
        :return:    numpy.array
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_bar(self, security, date, frequency='1d', fields=None):
    #     """
    #     获取K线数据
    #     :param security:    标的代码
    #     :param date:        查询日期
    #     :param frequency:   周期频率,支持'1d', '1m'，默认1d
    #     :param fields:      指明数据结果集中所支持输出字段，支持的值域范围：
    #     open  -- 开盘价；
    #     high  -- 最高价；
    #     low   -- 最低价；
    #     close -- 收盘价；
    #     volume-- 交易量；
    #     money -- 交易金额；
    #     price -- 最新价；
    #     :return:    numpy.array
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_bars(self, security, start_date, end_date=None, frequency='1d', fields=None):
    #     """
    #     获取指定日期范围内的K线数据
    #     :param security:      标的代码
    #     :param start_date:    开始日期
    #     :param end_date:      结束日期，默认取当天
    #     :param frequency:     周期频率,支持'1d', '1m'，默认1d
    #     :param fields:        指明数据结果集中所支持输出字段，支持的值域范围：
    #     open  -- 开盘价；
    #     high  -- 最高价；
    #     low   -- 最低价；
    #     close -- 收盘价；
    #     volume-- 交易量；
    #     money -- 交易金额；
    #     price -- 最新价；
    #     :return:    numpy.array
    #     """
    #     raise NotImplementedError

    @abc.abstractmethod
    def get_future_contracts(self, security, date=None):
        """
        获取期货可交易合约列表
        :param security:    标的代码或代码列表
        :param date:  查询日期
        :return:    list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_dominant_future(self, security, date=None):
        """
        获取主力合约对应的标的
        :param security:    标的代码或代码列表
        :param date:  查询日期
        :return:    str
        """
        raise NotImplementedError


class AbstractIndustryComponents(six.with_metaclass(abc.ABCMeta)):
    """
    行业成分接口类，需要扩展时，继承该类即可
    """

    @abc.abstractmethod
    def get_index_stocks(self, index_code=None, date=None):
        """
        获取指数成分股
        :param index_code:  指数代码
        :param date:  查询日期
        :return:  list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_industry_stocks(self, industry_code=None, date=None):
        """
        获取行业成分股
        :param industry_code:  行业代码
        :param date:  查询日期
        :return:  list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_block_stocks(self, block_code=None, date=None):
        """
        获取板块成分股
        :param block_code:  板块代码
        :param date:  查询日期
        :return:  list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_stock_blocks(self, security=None, date=None):
        """
        获取标的所属板块
        :param security:  标的代码
        :param date:  查询日期
        :return:  str
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_industries(self, name=None, date=None):
        """
        获取所属行业分类
        :param name:  行业名称
        :param date:  查询日期
        :return:  list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_market_list(self):
        """
        获取市场列表
        :return:  numpy.ndarray
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_market_detail(self, finance_mic):
        """
        获取市场详情信息
        :param finance_mic:  市场代码
        :return:  numpy.ndarray
        """
        raise NotImplementedError


class AbstractFinancialData(six.with_metaclass(abc.ABCMeta)):
    """
    财务数据接口类，需要扩展时，继承该类即可
    """

    @abc.abstractmethod
    def get_fundamentals(self, security, table, fields=None, date=None, start_year=None,
                         end_year=None, report_types=None, date_type=None, merge_type=None):
        """
        获取财务数据，包括三大财报、六大成长指标、股本信息、估值数据
        :param security:  股票代码
        :param table:  表名
        :param fields:  字段名/字段列表
        :param date:  日期
        :param start_year:  开始年份
        :param end_year:  结束年份
        :param report_types:  报告周期
        :param date_type:  是否可以获取未来数据
        :param merge_type:  是否采用更正后的数据
        :return:  pandas.DataFrame, 默认返回字段包含secu_code, publ_date,end_date及请求字段
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_fundamentals_filled(self, security, fields, start_date=None, end_date=None,
                                report_types=None, adjust_type=None, count=None):
        """
        获取填充后财报信息，包括三大报表数据
        :param security:  股票代码
        :param fields:  字段名/字段列表
        :param start_date:  开始日期
        :param end_date:  结束日期
        :param report_types:  报告周期
        :param adjust_type:  数据调整类型
        :param count:  向前查询年数
        :return:  pandas.DataFrame， 默认返回DataFrame索引为trading_day,symbol,列字段包含report_type及请求字段
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_performance(self, security, fields, start_date=None, end_date=None,
                        extra_day='0'):
        """
        获取股票行情表现数据
        :param security:  股票代码
        :param fields:  字段名/字段列表
        :param start_date:  开始日期
        :param end_date:  结束日期
        :param extra_day:  额外获取天数
        :return:  pandas.DataFrame， 默认返回DataFrame索引为trading_day,symbol,列字段包含请求字段
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_valuation_info(self, security, count, date=None, filled=False):
        """
        获取填充后财报信息，包括三大报表数据
        :param security:  股票代码
        :param count:  向前查询天数
        :param date:  日期
        :param filled:  填充数据标志
        :return: dict, 其中dict中key为股票代码，value为DataFrame
        """
        raise NotImplementedError


class AbstractFactorData(six.with_metaclass(abc.ABCMeta)):
    """
    因子数据接口类，需要扩展时，继承该类即可
    """

    @abc.abstractmethod
    def get_factor_list(self, company=None):
        """
        获取因子列表
        :param company:  机构枚举类
        :return: list
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_factor_info(self, fields, company=None):
        """
        获取因子信息
        :param fields:  字段名/字段列表
        :param company:  机构枚举类
        :return: pandas.DataFrame
        因子信息，包含列为
            'factor_id': 因子id
            'factor_name': 因子名
            'factor_chi_name': 因子中文名
            'company_id': 机构id
            'company_name': 机构名称
            'start_date': 因子数据开始日期
            'end_date': 因子数据结束日期
            'factor_frequency': 因子频率
            '1st_level_category': 一级分类
            '2nd_level_category': 二级分类
            '3rd_level_category': 三级分类
            'data_belong': 数据所属
            'data_source': 数据来源
            'valuation_criteria': 评估标准
            'factor_scale': 因子规模
            'factor_status': 因子状态
            'factor_unit',: 因子单位
            'memo': 备注
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_factor_value(self, security, fields, start_date, end_date, count, company=None):
        """
        获取因子信息数据
        :param security:  股票代码
        :param fields:  字段名/字段列表
        :param start_date:  开始日期
        :param end_date:  结束日期
        :param count:  往end_date前推的天数
        :param company:  机构枚举类
        :return: pandas.DataFrame, 包含列为trading_day':交易日，'symbol':股票代码及请求字段
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_ibrain_factor_list(self):
    #     """
    #     获取ibrain因子列表
    #     :return: dict
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_ibrain_factor_info(self, user_id, security, factor_ids, start_date, end_date, cache=True):
    #     """
    #     获取ibrain因子数据
    #     :param user_id: 用户ID
    #     :param security:  股票代码
    #     :param factor_ids: 因子id或因子id列表
    #     :param start_date:  开始日期
    #     :param end_date:  结束日期
    #     :param cache: 是否从缓存中获取数据
    #     :return: dict
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_ibrain_factor_info_online(self, user_id, security, factor_ids, start_date, end_date):
    #     """
    #     获取ibrain因子数据
    #     :param user_id: 用户ID
    #     :param security:  股票代码
    #     :param factor_ids: 因子id或因子id列表
    #     :param start_date:  开始日期
    #     :param end_date:  结束日期
    #     :return: dict
    #     """
    #     raise NotImplementedError


class AbstractRealDataSource(six.with_metaclass(abc.ABCMeta)):
    """
    实时行情数据接口类，需要扩展时，继承该类即可
    """
    @abc.abstractmethod
    def get_snapshot(self, security):
        """
        获取实时行情快照
        :param security:  股票代码
        :return: dict
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_real_minute_kline(self, security, include_now=True, fq=None, ex_info=None):
        """
        获取实时分钟行情快照
        :param security:  股票代码
        :param include_now:  是否包含最新的一条K线
        :param fq:  复权类型
        :param ex_info:  除权信息
        :return: pandas.DataFrame
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_real_daily_kline(self, security, fq=None, ex_info=None):
        """
        获取实时日线行情快照
        :param security:  股票代码
        :param fq:  复权类型
        :param ex_info:  除权信息
        :return: pandas.DataFrame
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_gear_price(self, security):
        """
        获取买卖档位数据
        :param security:  股票代码
        :return: pandas.DataFrame
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def subscribe(self, security):
    #     """
    #     订阅行情
    #     :param security:  标的代码
    #     :return: 无
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def unsubscribe(self, security):
    #     """
    #     取消订阅行情
    #     :param security:  标的代码
    #     :return: 无
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_individual_entrust(self, security, count=50, offset=0, direction=1):
    #     """
    #     获取逐笔委托行情
    #     :param security:  标的代码
    #     :param count:  数据条数
    #     :param offset:  起始位置
    #     :param direction:  搜索方向
    #     :return: pandas.Panel
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get_individual_transcation(self, security, count=50, offset=0, direction=1):
    #     """
    #     获取逐笔委托行情
    #     :param security:  标的代码
    #     :param count:  数据条数
    #     :param offset:  起始位置
    #     :param direction:  搜索方向
    #     :return: pandas.Panel
    #     """
    #     raise NotImplementedError


class AbstractFactor(six.with_metaclass(abc.ABCMeta)):
    """
    因子数据获取，从GTN获取接口类，需要扩展时，继承该类即可
    """

    @abc.abstractmethod
    def init(self, user_name=None, password=None, **kwargs):
        """
        初始化GTN的app_key和app_secret
        :param user_name: 用户名
        :param password: 密码
        :param kwargs: 其他预留参数
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_factor_list(self, factor_type='0', company_id='91000'):
        """
        获取指定分类因子列表
        :param factor_type:    因子类型，默认基本面类型
        :param company_id:     机构编码，默认'91000', 恒生电子
        :return:
        """
        raise NotImplementedError
