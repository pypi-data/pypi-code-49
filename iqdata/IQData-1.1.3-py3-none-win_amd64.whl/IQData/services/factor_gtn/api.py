#  -*- coding: utf-8 -*-
#  =====================================================================
#  Copyright (c)2019, 恒生电子股份有限公司
#  All rights reserved.
#
#  文件名称：api.py
#  摘    要：
#
#  当前版本：V1.0.0
#  作    者：qianmx21829
#  完成日期：2019-08-26
#  备    注：
#  =====================================================================
import datetime

import pandas as pd

from IQCommon.datetime_func import to_timestamp
from IQCommon.exception import ParamsError
from IQData.services.factor_gtn.factor_gtn import factor_gtn
from . import const


__all__ = [
    'init',
    'get_factor_list',
    'get_high_frequency_factor',
    'get_sentiment_factor',
    'get_fundamental_factor',
    'get_technical_factor',
    'get_event_factor',
    'get_multi_event_factor',
    'get_index_stocks',
    'get_Ashares'
]


def init(user_name=None, password=None, **kwargs):
    """
    初始化GTN的app_key和app_secret
    :param user_name: 用户名
    :param password: 密码
    :param kwargs: 其他预留参数
    :return:
    """
    if user_name is not None and not isinstance(user_name, str):
        raise ParamsError("请输入正确类型的user_name：用户名，字符串类型")
    if password is not None and not isinstance(password, str):
        raise ParamsError("请输入正确类型的password：密码，字符串类型")

    return factor_gtn.init(user_name, password, **kwargs)


def get_factor_list(factor_type='0', company_id='91000'):
    """
    获取指定分类因子列表
    :param factor_type:    因子类型，默认基本面类型
    :param company_id:     机构编码，默认'91000', 恒生电子
    :return:
    """
    if factor_type is not None and not isinstance(factor_type, str):
        raise ParamsError("请输入正确类型的因子类型（factor_type），str类型，如'0'- 基本面因子")
    if factor_type is not None and factor_type not in const.FACTOR_TYPE_NUM:
        raise ParamsError("请输入正确类型的因子类型（factor_type），str类型，现只支持{}".format(const.FACTOR_TYPE_NUM))
    if company_id is not None and not isinstance(company_id, str):
        raise ParamsError("请输入正确类型的机构编码（company_id），str类型， 如'91000'")

    return factor_gtn.get_factor_list(factor_type, company_id)


def get_index_stocks(index_code=None, date=None):
    """
       获取指定分类因子列表
       :param index_code: 指数代码, str类型
       :param date: 指定日期，int/str/datetime.date类型， 默认当前日期
       :return: list
       """

    if not isinstance(index_code, str):
        raise ParamsError("请输入正确类型的需要返回的字段（index_code），str类型")

    if index_code.split('.')[1] != 'XBHS':
        raise ParamsError("请输入正确类型的指数代码（index_code），后缀为'XBHS', 如'000300.XBHS'")
    index_code = index_code.split('.')[0]

    if date is not None and not isinstance(date, (int, str, datetime.date)):
        raise ParamsError("请输入正确类型的查询日期（date），int、str或datetime.date类型，如'20190105'")
    if date is not None:
        try:
            date = to_timestamp(date).strftime('%Y%m%d')
        except Exception as x:
            raise ParamsError("请输入正确类型的查询日期（date），int、str或datetime.date类型，如'20190105'")

    else:
        date = datetime.datetime.now().strftime("%Y%m%d")

    return factor_gtn.get_index_stocks(index_code, date)


def get_Ashares(date=None):
    """
       获取全部A股代码列表
       :param date: 指定日期，int/str/datetime.date类型， 默认当前日期
       :return: list
       """
    if date is not None and not isinstance(date, (int, str, datetime.date)):
        raise ParamsError("请输入正确类型的查询日期（date），int、str或datetime.date类型，如'20190105'")
    if date is not None:
        try:
            date = to_timestamp(date).strftime('%Y%m%d')
        except Exception as x:
            raise ParamsError("请输入正确类型的查询日期（date），int、str或datetime.date类型，如'20190105'")
    else:
        date = datetime.datetime.now().strftime("%Y%m%d")

    return factor_gtn.get_Ashares(date)


def get_high_frequency_factor(factor_list=None, stock_list=None,
                              start_date=None, end_date=None, company_id='91000'):
    """
    获取高频因子数据
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :return:
    """
    return get_factor_value(factor_list, stock_list,
                            start_date, end_date, company_id, "high_frequency")


def get_sentiment_factor(factor_list=None, stock_list=None,
                         start_date=None, end_date=None, company_id='91000'):
    """
    获取舆情因子数据
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :return:
    """
    return get_factor_value(factor_list, stock_list,
                            start_date, end_date, company_id, "sentiment")


def get_fundamental_factor(factor_list=None, stock_list=None,
                           start_date=None, end_date=None, company_id='91000'):
    """
    获取基本面因子数据
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :return:
    """
    return get_factor_value(factor_list, stock_list,
                            start_date, end_date, company_id, "fundamental")


def get_technical_factor(factor_list=None, stock_list=None,
                         start_date=None, end_date=None, company_id='91000'):
    """
    获取技术面因子数据
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :return:
    """
    return get_factor_value(factor_list, stock_list,
                            start_date, end_date, company_id, "technical")


def get_event_factor(factor_list=None, stock_list=None,
                     start_date=None, end_date=None, company_id='91000'):
    """
    获取事件因子数据
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :return:
    """
    return get_factor_value(factor_list, stock_list,
                            start_date, end_date, company_id, "event")


def get_multi_event_factor(factor_list=None, stock_list=None,
                           start_date=None, end_date=None, company_id='91000'):
    """
    获取合并事件因子数据
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :return:
    """
    if not isinstance(factor_list, (str, list)):
        raise ParamsError("请输入正确类型的因子列表（factor_list），str或list类型，至多10个")
    if isinstance(factor_list, list):
        if len(factor_list) > 10:
            raise ParamsError("请输入正确类型的因子列表（factor_list），str或list类型，至多10个")
        elif len(factor_list) == 0:
            return pd.DataFrame()

    if isinstance(factor_list, str):
        factor_list_tmp = [factor_list]
        event_data = get_factor_value(factor_list_tmp, stock_list,
                                      start_date, end_date, company_id, "event")
        if not event_data.empty:
            event_data.rename(columns={factor_list: 'event_factor'}, inplace=True)
        else:
            event_data = pd.DataFrame()
    else:
        event_data_tmp = get_factor_value(factor_list, stock_list,
                                          start_date, end_date, company_id, "event")
        try:
            event_data_tmp["event_factor"] = event_data_tmp.loc[
                event_data_tmp[factor_list].notnull().any(axis=1), factor_list].max(axis=1)
            columns_tmp = list(event_data_tmp.columns)
            columns = [x for x in columns_tmp if x not in factor_list]
            event_data = event_data_tmp[columns]
        except Exception as x:
            print(x)
            return pd.DataFrame()
    return event_data


def get_factor_value(factor_list=None, stock_list=None,
                     start_date=None, end_date=None, company_id='91000', factor_type=None):
    """
    因子数据获取通用接口
    :param factor_list:
    :param stock_list:
    :param start_date:
    :param end_date:
    :param company_id:
    :param factor_type:
    :return:
    """
    if not isinstance(factor_list, (str, list)):
        raise ParamsError("请输入正确类型的因子列表（factor_list），str或list类型，至多10个")
    if isinstance(factor_list, list):
        if len(factor_list) > 10:
            raise ParamsError("请输入正确类型的因子列表（factor_list），str或list类型，至多10个")
        elif len(factor_list) == 0:
            return pd.DataFrame()

    if stock_list is not None and not isinstance(stock_list, (str, list)):
        raise ParamsError("请输入正确类型的股票代码列表（stock_list），str或list类型，如['600570.XSHG', '000001.XSHE'] ")
    if stock_list is None:
        raise ParamsError("请输入股票代码列表(stock_list)")
    if start_date is not None and not isinstance(start_date, (int, str, datetime.date)):
        raise ParamsError("请输入正确类型的开始日期（start_date），int或str类型，如'20190105'")
    if end_date is not None and not isinstance(end_date, (int, str, datetime.date)):
        raise ParamsError("请输入正确类型的结束日期（end_date），int或str类型，如'20190105'")
    if company_id is not None and not isinstance(company_id, str):
        raise ParamsError("请输入正确类型的机构编码（company_id），str类型， 如'91000'")

    if start_date is not None:
        try:
            start_date = to_timestamp(start_date).strftime('%Y%m%d')
        except Exception as x:
            raise ParamsError("请输入正确类型的查询日期（date），int、str或datetime.date类型，如'20190105'")

        if start_date > datetime.datetime.now().strftime("%Y%m%d"):
            print("Warning: 输入开始日期超过当前日期，无法返回当前日期之后的因子数据")

    if end_date is not None:
        try:
            end_date = to_timestamp(end_date).strftime('%Y%m%d')
        except Exception as x:
            raise ParamsError("请输入正确类型的查询日期（date），int、str或datetime.date类型，如'20190105'")
        if end_date > datetime.datetime.now().strftime("%Y%m%d"):
            print("Warning: 结束日期超过当前日期，无法返回当前日期之后的因子数据")

    if start_date is not None and end_date is not None:
        if start_date > end_date:
            raise ParamsError("请传入正确的开始日期与结束日期，开始日期需小于等于结束日期，结束日期不超过当天")

    if factor_type not in const.FACTOR_TYPE.keys():
        raise ParamsError("请输入正确的因子数据类型（factor_type），str类型， 如'high_frequency'")

    return factor_gtn.get_factor_value(factor_list, stock_list,
                                       start_date, end_date, company_id, factor_type)
