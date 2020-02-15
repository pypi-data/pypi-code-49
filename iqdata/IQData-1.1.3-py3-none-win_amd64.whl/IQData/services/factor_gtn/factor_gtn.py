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
from ruamel import yaml
import os
import pandas as pd

from . import settings
from IQData.interface import AbstractFactor
from IQData.utils import BASE_PATH
from IQCommon.logger import system_log
from IQCommon.exception import ParamsError, RequestException
from . import const


config_path = os.path.join(BASE_PATH, 'utils', 'default_config.yml')


class FactorGtn(AbstractFactor):
    def __init__(self):
        self.init_flag = False
        self.app_key = ''
        self.secret = ''
        self.key = 'hs600570'
        self.iv = '075006sh'
        self.client = None

    @property
    def read_config(self):
        with open(config_path, 'r+', encoding='utf-8') as f:
            config = yaml.load(f.read(), Loader=yaml.Loader)

        return config

    def write_config(self, config):
        try:
            with open(config_path, 'w+', encoding='utf-8') as f:
                yaml.dump(config, f, Dumper=yaml.RoundTripDumper)
        except Exception as e:
            system_log.info("GTN对应的app_key与app_secret信息保存失败！，原因为{}".format(e))
            raise e

    def init(self, user_name=None, password=None, **kwargs):
        """
        初始化GTN的app_key和app_secret
        :param user_name:
        :param password:
        :param kwargs:
        :return:
        """

        config = self.read_config

        if user_name is not None and password is not None:
            try:
                from IQData import create_gtn_client
                client = create_gtn_client(user_name, password)
                token = client.token
            except PermissionError as e:
                raise PermissionError("获取token失败，请检查app_key是否过期")

            if token is None:
                raise ParamsError("请输入正确的用户名及密码")
            else:
                self.app_key = user_name
                self.secret = password
                self.client = client

                from IQData.utils.encrypt import DESEncrypt
                config["services"]["factor_gtn"]["gtn"]["app_key"] = DESEncrypt().encrypt(user_name, self.key, self.iv)
                config["services"]["factor_gtn"]["gtn"]["secret"] = DESEncrypt().encrypt(password, self.key, self.iv)
                self.write_config(config)

        elif user_name is None and password is None:
            app_key_tmp = settings.gtn.app_key
            secret_tmp = settings.gtn.secret

            if app_key_tmp is None or secret_tmp is None:
                raise RuntimeError("初始化连接异常，读取配置参数失败，请调用init进行初始化")
            else:
                from IQData.utils.encrypt import DESEncrypt
                app_key = DESEncrypt().decrypt(app_key_tmp, self.key, self.iv)
                secret = DESEncrypt().decrypt(secret_tmp, self.key, self.iv)

                return self.init(user_name=app_key, password=secret)

        else:
            raise ParamsError("参数异常：请输入正确的user_name和password")

        self.init_flag = True

    def get_factor_list(self, factor_type='0', company_id='91000'):
        """
        获取指定分类因子列表
        :param factor_type:    因子类型，默认基本面类型
        :param company_id:     机构编码，默认'91000', 恒生电子
        :return:
        """
        factor_list_url = "/alphamind/v1/factor/get_factor_list"

        if not self.init_flag:
            self.init()

        params = {
            "factor_type": factor_type,
            "company_id": company_id,
            "data_belong": 'prd',
        }

        result = self._request(factor_list_url, params, 'GET')
        if "data" in result:
            rsp_str = result['data']
            return pd.DataFrame(rsp_str)
        else:
            return pd.DataFrame()

    def get_index_stocks(self, index_code=None, date=None):
        """
        获取指定分类因子列表
        :param index_code: 指数代码, str类型
        :param date: 指定日期，int/str/datetime.date类型， 默认当前日期
        :return:
        """
        index_stocks_url = "/alphamind/v1/basic/get_category_content"

        if not self.init_flag:
            self.init()

        params = {
            "category_code": index_code,
            "category_sub_type": "zs",
            "query_date": date
        }

        result = self._request(index_stocks_url, params, 'GET')
        if "data" in result:
            return result['data']

        return list()

    def get_Ashares(self, date=None):
        """
        获取全市场A股列表
        :param date: 指定日期，int/str/datetime.date类型， 默认当前日期
        :return:
        """
        index_stocks_url = "/alphamind/v1/basic/get_category_content"

        if not self.init_flag:
            self.init()

        params = {
            "category_code": "A",
            "category_sub_type": "zs",
            "query_date": date
        }

        result = self._request(index_stocks_url, params, 'GET')
        if "data" in result:
            return result['data']

        return list()

    def get_factor_value(self, factor_list, stock_list,
                         start_date=None, end_date=None, company_id='91000', factor_type=None):
        """
        获取高频因子数据
        :param factor_list: 因子列表
        :param stock_list: 股票代码列表
        :param start_date: 开始日期
        :param end_date: 结束日期
        :param company_id: 机构编码
        :param factor_type: 因子类型
        :return:
        """
        if isinstance(factor_list, str):
            factor_list = [factor_list]

        factor_list_gtn = factor_list

        if isinstance(factor_list, list):
            factor_list = ','.join(factor for factor in factor_list)

        if not self.init_flag:
            self.init()

        if stock_list is not None:
            if isinstance(stock_list, str):
                stock_list = [stock_list]
            if isinstance(stock_list, list):
                stock_list = ','.join(stock for stock in stock_list)

        if start_date is None:
            start_date = datetime.datetime.now().strftime("%Y%m%d")
        if end_date is None:
            end_date = datetime.datetime.now().strftime("%Y%m%d")

        params = {
            "factor_list": factor_list,
            "stock_list": stock_list,
            "start_date": start_date,
            "end_date":  end_date,
            "company_id": company_id
        }

        factor_url = const.FACTOR_TYPE[factor_type]
        return self._process_request(factor_url, params, factor_list_gtn)

    def _process_request(self, url, params, factor_list_gtn):
        df, last_date = self._parse_response(self._request(url, params))

        result_df = df
        end_date = params['end_date']

        # 最后数据的日期等于结束时间，无需翻页查询
        if last_date >= end_date:
            return result_df[factor_list_gtn].astype(float).sort_values(by=['trading_day'])

        end_date_int = int(end_date)
        # 下一个交易日
        next_date_tmp = datetime.datetime.strptime(last_date, "%Y%m%d") + datetime.timedelta(days=1)
        next_date = int(next_date_tmp.strftime('%Y%m%d'))

        # 翻页查询，上一次查询的最后数据日期小于结束时间

        while int(last_date) < end_date_int:

            params['start_date'] = next_date
            params['end_date'] = end_date

            df, last_date = self._parse_response(self._request(url, params))
            next_date_tmp = datetime.datetime.strptime(last_date, "%Y%m%d") + datetime.timedelta(days=1)
            next_date = int(next_date_tmp.strftime('%Y%m%d'))

            if df.empty:
                continue

            result_df = pd.concat([result_df, df])
            if next_date > end_date_int:
                break

        result_df[factor_list_gtn] = result_df[factor_list_gtn].astype(float)

        return result_df.sort_values(by=['trading_day'])

    def _request(self, url, params, method='POST'):
        if method == "POST":
            error_dict, response = self.client.send_by_post(url, params)
        else:
            error_dict, response = self.client.send_by_get(url, params)

        if error_dict['error_no'] != 0:
            raise RequestException(error_dict['error_info'])

        if response['error_no'] != 0:
            error_info = '服务器处理异常，应答错误号:[%d]，错误信息[%s]' % (response['error_no'], response['error_info'])
            raise RequestException(error_info)

        return response

    def _parse_response(self, response):
        try:
            if "data" in response:
                data = response['data']
                df = pd.DataFrame(columns=data['fields'].split(','), data=data['items'])
                df.set_index(['trading_day', 'stock_code'], inplace=True)
                return df, data['last_tradeday']
            else:
                return pd.DataFrame(), None
        except KeyError:
            return pd.DataFrame(), None


factor_gtn = FactorGtn()
