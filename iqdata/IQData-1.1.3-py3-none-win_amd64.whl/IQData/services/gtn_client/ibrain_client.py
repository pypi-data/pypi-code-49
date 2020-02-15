# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：ibrain_client.py
# 摘    要：ibrain数据服务的http客户端
#
# 当前版本：V1.0.0
# 作    者：
# 完成日期：2019-04-04
# 备    注：
###############################################################################
import json

from .base_http_client import RequestChannel, BaseHTTPClient


class IbrainClient(object):
    """
    面向Ibrain服务的HTTP客户端
    """
    def __init__(self, channel, max_request_times=5):
        self._library = BaseHTTPClient(channel)
        self._max_request_times = max_request_times

    def send_by_get(self, url, data=None, request_times=0, default_error_return={}):
        try:
            res = self._library.request(method='GET', url=url, params=data)
            # 正常返回
            if res['status_code'] == 200:
                body_dict = json.loads(res['body'])
                return body_dict
            else:
                if request_times < self._max_request_times:
                    request_times += 1
                    return self.send_by_get(url, data, request_times)
                else:
                    error_no = 105001
                    error_info = '服务器处理异常，http状态码%s' % res['status_code']
                    return {'error_no': error_no, 'error_info': error_info, 'data': default_error_return}
        except Exception as e:
            if request_times < self._max_request_times:
                request_times += 1
                return self.send_by_get(url, data, request_times)
            else:
                error_no = 105002
                error_info = '连接异常，异常信息：%s' % e
                return {'error_no': error_no, 'error_info': error_info, 'data': default_error_return}

    def send_by_post(self, url, data=None, request_times=0, default_error_return={}):
        try:
            res = self._library.request(method='POST', url=url, data=data)
            # 正常返回
            if res['status_code'] == 200:
                body_dict = json.loads(res['body'])
                return body_dict
            else:
                if request_times < self._max_request_times:
                    request_times += 1
                    return self.send_by_post(url, data, request_times)
                else:
                    error_no = 105001
                    error_info = '服务器处理异常，http状态码%s' % res['status_code']
                    return {'error_no': error_no, 'error_info': error_info, 'data': default_error_return}
        except Exception as e:
            if request_times < self._max_request_times:
                request_times += 1
                return self.send_by_post(url, data, request_times)
            else:
                error_no = 105002
                error_info = '连接异常，异常信息：%s' % e
                return {'error_no': error_no, 'error_info': error_info, 'data': default_error_return}


def create_ibrain_client():
    ibrain_channel = RequestChannel()
    ibrain_client = IbrainClient(ibrain_channel)
    return ibrain_client
