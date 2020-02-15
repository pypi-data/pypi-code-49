# -*- coding: utf-8 -*-

#  -*- coding: utf-8 -*-
#  =====================================================================
#  Copyright (c)2019, 恒生电子股份有限公司
#  All rights reserved.
#
#  文件名称：arg_checker.py
#  摘    要：
#
#  当前版本：V1.0.0
#  作    者：qianmx21829
#  完成日期：2019-08-14
#  备    注：
#  =====================================================================

##############################################################################
#
# 文件名称：arg_checker.py
# 摘    要：arg_checker模块
#
# 当前版本：V1.0.0
# 作    者：qianmx21829
# 完成日期：2018-10-15
# 备    注：参数校验模块
###############################################################################

import sys
import inspect
import datetime
import six
import pandas as pd
from functools import wraps

from dateutil.parser import parse as parse_date

from IQCommon import exception, const, utils
from IQCommon.i18n import get_local_text as _

main_contract_warning_flag = True
index_contract_warning_flag = True


class ArgumentChecker(object):
    """
    用于参数校验的类
    """
    def __init__(self, arg_name):
        """
        :param arg_name: str 参数的名称， 主要用于日志打印
        """
        self._arg_name = arg_name
        self._rules = []  # 校验的规则数组

    def verify(self, func_name, value):
        for r in self._rules:
            r(func_name, value)

    @property
    def arg_name(self):
        return self._arg_name

    # -------------------------------- 错误检查方法 --------------------------------

    def is_instance(self, types):
        """
        校验参数类型
        :param types: tuple, isinstance参数，type类型元组
        :return: self
        """
        def check_is_instance(func_name, value):
            if not isinstance(value, types):
                raise exception.IQInvalidArgument(
                    _(u"function {}: invalid {} argument, expect a value of type {},"
                      u" got {} (type: {})").format(
                        func_name, self._arg_name, types, value, type(value)
                    ))

        self._rules.append(check_is_instance)
        return self

    def is_valid_asset(self):
        """
        校验是否为Asset
        :return: self
        """
        self._rules.append(self._is_valid_asset)
        return self

    def is_valid_stock(self):
        """
        校验是否为StockAsset
        :return: self
        """
        self._rules.append(self._is_valid_stock)
        return self

    def is_valid_future(self):
        """
        校验是否为FutureAsset
        :return: self
        """
        self._rules.append(self._is_valid_future)
        return self

    def is_number(self):
        """
        校验是否为数字
        :return: self
        """
        self._rules.append(self._is_number)
        return self

    def is_in(self, valid_values, ignore_none=True):
        """
        校验是否为在对象中
        :param valid_values: 含有 __contains__ 方法的对象
        :param ignore_none: bool 如果 value 为 None 则跳过
        :return: self
        """
        def check_is_in(func_name, value):
            if ignore_none and value is None:
                return

            if value not in valid_values:
                raise exception.IQInvalidArgument(
                    _(u"function {}: invalid {} argument,"
                      u" valid: {}, got {} (type: {})").format(
                        func_name, self._arg_name, repr(valid_values), value, type(value))
                )

        self._rules.append(check_is_in)
        return self

    def are_valid_fields(self, valid_fields, ignore_none=True):
        """
        校验 fields 参数合法性
        :param valid_fields: Iterable object 合法的field取值
        :param ignore_none: bool 如果 value 为 None 则跳过
        :return: self
        """
        valid_fields = set(valid_fields)

        def check_are_valid_fields(func_name, fields):
            if isinstance(fields, six.string_types):
                if fields not in valid_fields:
                    raise exception.IQInvalidArgument(
                        _(u"function {}: invalid {} argument, "
                          u"valid fields are {}, got {} (type: {})").format(
                            func_name, self._arg_name, repr(valid_fields), fields, type(fields)
                        ))
                return

            if fields is None and ignore_none:
                return

            if isinstance(fields, list):
                invalid_fields = [field for field in fields if field not in valid_fields]
                if invalid_fields:
                    raise exception.IQInvalidArgument(
                        _(u"function {}: invalid field {}, "
                          u"valid fields are {}, got {} (type: {})").format(
                            func_name, invalid_fields, repr(valid_fields), fields, type(fields)
                        ))
                return

            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, "
                  u"expect a string or a list of string, got {} (type: {})").format(
                    func_name, self._arg_name, repr(fields), type(fields)
                ))

        self._rules.append(check_are_valid_fields)
        return self

    def are_valid_assets(self):
        """
        校验是否是内容为 Asset类型 的 Iterable object
        :return: self
        """
        self._rules.append(self._are_valid_assets)
        return self

    def is_valid_date(self, ignore_none=True):
        """
        校验是否是date类型
        :param ignore_none: bool 如果 value 为 None 则跳过
        :return: self
        """
        def check_is_valid_date(func_name, value):
            if ignore_none and value is None:
                return None
            if isinstance(value, (datetime.date, pd.Timestamp)):
                return
            if isinstance(value, int):
                value = str(value)
            if isinstance(value, six.string_types):
                try:
                    parse_date(value)
                    return
                except ValueError:
                    raise exception.IQInvalidArgument(
                        _(u"function {}: invalid {} argument, "
                          u"expect a valid date, got {} (type: {})").format(
                            func_name, self._arg_name, value, type(value)
                        ))

            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, "
                  u"expect a valid date, got {} (type: {})").format(
                    func_name, self._arg_name, value, type(value)
                ))

        self._rules.append(check_is_valid_date)
        return self

    def compare(self, operator, value_compared):
        """
        比较校验
        :param operator: const.CompareEnum/
        :param value_compared:
        :return:
        """
        if isinstance(operator, const.CompareEnum):
            compare_str, operator = operator.value
        elif callable(operator):
            compare_str = operator.__name__
        else:
            return

        def check_compare(func_name, value):
            if not operator(value, value_compared):
                raise exception.IQInvalidArgument(
                    _(u"function {}: invalid {} argument, "
                      u"expect a value {} {}, got {} (type: {})").format(
                        func_name, self._arg_name, compare_str, value_compared, value, type(value)
                    ))
        self._rules.append(check_compare)
        return self

    def is_valid_interval(self):
        """
        校验是否分钟区间
        :return: self
        """
        self._rules.append(self._is_valid_interval)
        return self

    def is_valid_quarter(self):
        """
        校验是否季度字符串
        :return: self
        """
        self._rules.append(self._is_valid_quarter)
        return self

    def are_valid_query_entities(self):
        """
        校验 query_entities 类型数据
        :return: self
        """
        self._rules.append(self._are_valid_query_entities)
        return self

    def is_valid_frequency(self):
        self._rules.append(self._is_valid_frequency)
        return self
    
    def is_valid_search_direction(self):
        self._rules.append(self._is_valid_search_direction)
        return self

    # -------------------------------- 抛出错误 --------------------------------

    def raise_invalid_asset_error(self, func_name, arg_name, value):
        raise exception.IQInvalidArgument(
            _(u"function {}: invalid {} argument, expect a valid asset/symbol, "
              u"got {} (type: {})").format(
                func_name, self._arg_name, value, type(value)
            ))

    def raise_not_valid_stock_error(self, func_name, arg_name, value):
        raise exception.IQInvalidArgument(
            _(u"function {}: invalid {} argument, "
              u"expect a valid stock asset/symbol, "
              u"got {} (type: {})").format(
                func_name, self._arg_name, value, type(value)
            ))

    def raise_not_valid_future_error(self, func_name, arg_name, value):
        raise exception.IQInvalidArgument(
            _(u"function {}: invalid {} argument, "
              u"expect a valid future asset/symbol, "
              u"got {} (type: {})").format(
                func_name, self._arg_name, value, type(value)
            ))

    # -------------------------------- 校验函数 --------------------------------

    def _is_valid_asset(self, func_name, value):
        asset_object = None
        if isinstance(value, six.string_types):
            asset_object = self._engine_get_asset(value)
        elif self._engine_is_valid_asset(value):
            asset_object = value
        if asset_object is None:
            self.raise_invalid_asset_error(func_name, self._arg_name, value)
        return asset_object

    def _is_valid_stock(self, func_name, value):
        asset_object = self._is_valid_asset(func_name, value)
        if asset_object.type != const.AssetType.STOCK.value:
            self.raise_not_valid_stock_error(func_name, self._arg_name, value)

    def _is_valid_future(self, func_name, value):
        asset_object = self._is_valid_asset(func_name, value)
        if asset_object.type != const.AssetType.FUTURE.value:
            self.raise_not_valid_future_error(func_name, self._arg_name, value)

    def _are_valid_assets(self, func_name, values):

        if isinstance(values, list):
            for v in values:
                self._is_valid_asset(func_name, v)
            return

        self._is_valid_asset(func_name, values)

    def _is_number(self, func_name, value):
        try:
            float(value)
        except (ValueError, TypeError):
            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, "
                  u"expect a number, got {} (type: {})").format(
                    func_name, self._arg_name, value, type(value))
            )

    def _is_valid_interval(self, func_name, value):
        valid = isinstance(value, six.string_types) and value[-1] in {'d', 'm', 'q', 'y'}
        if valid:
            try:
                valid = int(value[:-1]) > 0
            except (ValueError, TypeError):
                valid = False

        if not valid:
            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, "
                  u"interval should be in form of '1d', '3m', '4q', '2y', "
                  u"got {} (type: {})").format(
                    func_name, self.arg_name, value, type(value)
                ))

    def _is_valid_quarter(self, func_name, value):
        if value is None:
            valid = True
        else:
            valid = isinstance(value, six.string_types) and value[-2] == 'q'
            if valid:
                try:
                    valid = 1990 <= int(value[:-2]) <= 9999 and 1 <= int(value[-1]) <= 4
                except (ValueError, TypeError):
                    valid = False

        if not valid:
            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, "
                  u"quarter should be in form of '2018q3', "
                  u"got {} (type: {})").format(
                    func_name, self.arg_name, value, type(value)
                ))

    def _are_valid_query_entities(self, func_name, entities):
        from sqlalchemy.orm.attributes import InstrumentedAttribute
        for e in entities:
            if not isinstance(e, InstrumentedAttribute):
                raise exception.IQInvalidArgument(
                    _(u"function {}: invalid {} argument, should be entity like "
                      u"Fundamentals.balance_sheet.total_equity, got {} (type: {})").format(
                        func_name, self.arg_name, e, type(e)
                    ))

    def _is_valid_frequency(self, func_name, value):
        valid = isinstance(value, six.string_types)
        if valid:
            if value[-1] in ("d", "m"):
                try:
                    valid = int(value[:-1]) > 0
                except (ValueError, TypeError):
                    valid = False
            elif value == 'tick':
                pass
            else:
                valid = False
        if not valid:
            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, frequency should be in form of "
                  u"'1m', '5m', '1d', 'tick' got {} (type: {})").format(
                    func_name, self.arg_name, value, type(value)
                ))
    
    def _is_valid_search_direction(self, func_name, value):
        valid = isinstance(value, six.integer_types)
        if valid:
            if value in (1, 2):
                pass
            else:
                valid = False
        if not valid:
            raise exception.IQInvalidArgument(
                _(u"function {}: invalid {} argument, search_direction should be in"
                  u"1, 2 got {} (type: {})").format(
                    func_name, self.arg_name, value, type(value)
                ))

    def _engine_get_asset(self, asset):
        raise NotImplementedError

    def _engine_is_valid_asset(self, asset):
        raise NotImplementedError


class IQDataArgumentChecker(ArgumentChecker):

    _iqdata = None
    @property
    def iqdata(self):
        if self._iqdata is None:
            import IQData
            self._iqdata = IQData
        return self._iqdata

    def _engine_get_asset(self, asset):
        # noinspection PyUnresolvedReferences
        return self.iqdata.get_security_info(asset)

    def _engine_is_valid_asset(self, asset):
        # noinspection PyUnresolvedReferences
        return self.iqdata.get_security_info(asset) is not None


def verify_arg(arg_name, checker=IQDataArgumentChecker):
    return checker(arg_name)


def apply_rules(*rules):
    """
    参数校验装饰器
    该装饰器用于对函数进行参数校验
    注意：该校验会在函数执行抛出异常时才会对参数进行校验
    :param rules: tuple ArgumentChecker 校验规则
    :return:
    """
    def decorator(func):
        @wraps(func)
        def api_rule_check_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception.IQInvalidArgument:
                raise
            except Exception as e:
                exc_info = sys.exc_info()
                t, v, tb = exc_info

                try:
                    call_args = inspect.getcallargs(
                        utils.get_original_function(func), *args, **kwargs)
                except TypeError as e:
                    six.reraise(exception.IQTypeError, exception.IQTypeError(*e.args), tb)
                    return

                try:
                    for r in rules:
                        r.verify(func.__name__, call_args[r.arg_name])
                except exception.IQInvalidArgument as e:
                    six.reraise(exception.IQInvalidArgument, e, tb)
                    return

                if getattr(e, const.EXC_EXT_NAME, const.ExcType.NOTSET) == const.ExcType.NOTSET:
                    exception.system_exc(e)

                raise

        api_rule_check_wrapper.exception_checked = True
        return api_rule_check_wrapper

    return decorator
