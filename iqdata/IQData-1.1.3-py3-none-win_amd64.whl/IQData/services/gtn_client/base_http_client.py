# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：base_http_client.py
# 摘    要：通用http客户端
#
# 当前版本：V1.0.0
# 作    者：
# 完成日期：2018-12-19
# 备    注：
###############################################################################
import json
import errno
from functools import partial
from socket import error as SocketError

import requests


class RequestChannel(object):
    """
    这个类使用了第三方包requests
    """
    def request(self, method, url, **kwargs):
        """
        通用的request请求
        """
        res = requests.request(method.lower(), url, **kwargs)
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        result = {'status_code': res.status_code, 'cookies': cookies, 'body': res.text}
        return result


class BaseHTTPClient(object):
    def __init__(self, channel):
        self._channel = channel

    def request(self, **kwargs):
        return self._channel.request(**kwargs)

    def get_token(self, method, url, token_key, request_times=0, **kwargs):
        """
        获取token
        :param method: str, 请求方式，'GET'、'POST'等
        :param url: str, token请求地址
        :param data: dict, 请求时传入的数据
        :param headers: dict, 请求头
        :param token_key: str, 从dict中获取token时其键值
        :param request_times: int, 连接异常时请求次数
        :return: http请求状态，token值
        """
        return self._do_request(
            method, url,
            request_times=request_times,
            default='', on_success=partial(
                self._get_token_on_success, token_key
            ),
            ** kwargs
        )

    @staticmethod
    def _get_token_on_success(token_key, res):
        res_body = res['body']
        res_body_dict = json.loads(res_body)
        token = res_body_dict[token_key]
        return token

    def get_cookies(self, method, url, request_times=0, **kwargs):
        """
        获取cookies
        :param method|str: 请求方式，'GET'、'POST'等
        :param url|str: token请求地址
        :param data|dict: 请求时传入的数据
        :param headers|dict: 请求头
        :param request_times|int: 连接异常时请求次数
        :return:
        """

        return self._do_request(
            method, url, 
            request_times=request_times,
            default={}, on_success=self._get_token_on_success,
            ** kwargs
        )

    @staticmethod
    def _get_cookies_on_success(res):
        cookies = res['cookies']
        return cookies

    def _do_request(
            self, method, url,
            request_times=0, default=None, on_success=None,
            **kwargs
    ):
        try:
            res = self.request(method=method, url=url, **kwargs)
            res_body = res['body']
            # 状态码为200时，正常返回
            if res['status_code'] == 200:
                if on_success is not None:
                    res = on_success(res)
                return {'error_no': 0, 'error_info': ''}, res
            elif 400 <= res['status_code'] <= 499:
                error_no = res['status_code']
                error_info = res_body
                return {'error_no': error_no, 'error_info': error_info}, default
            else:
                error_no = -1
                error_info = '服务器处理异常，内部错误号:%s' % res['status_code']
                return {'error_no': error_no, 'error_info': error_info}, default
        except SocketError as e:
            if e.errno == errno.ECONNRESET:
                # 连接异常时，尝试多次发送请求
                if request_times <= 5:
                    request_times += 1
                    return self._do_request(
                        method=method,
                        url=url,
                        request_times=request_times,
                        default=default,
                        on_success=on_success,
                        ** kwargs
                    )
                else:
                    error_no = e.errno
                    error_info = '请求异常，错误:%s' % e
                    return {'error_no': error_no, 'error_info': error_info}, default
            else:
                error_no = -1
                error_info = e
                return {'error_no': error_no, 'error_info': error_info}, default
        except ConnectionRefusedError as e1:
            error_no = -1
            error_info = e1
            return {'error_no': error_no, 'error_info': error_info}, default
        except Exception as e2:
            error_no = -1
            error_info = e2
            return {'error_no': error_no, 'error_info': error_info}, default
