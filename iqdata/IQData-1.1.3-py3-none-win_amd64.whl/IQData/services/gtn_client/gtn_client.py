# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：GTNClinet.py
# 摘    要：面向GTN的HTTP客户端
#
# 当前版本：V1.0.0
# 作    者：
# 完成日期：2018-12-19
# 备    注：
###############################################################################
import base64
import json

from .base_http_client import BaseHTTPClient, RequestChannel

# from IQData.utils.common_func import get_parse_config_obj
# from IQData.utils.logger import system_log


TOKEN_ERROR = PermissionError('token获取失败，无数据返回')


def token_check(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionError as e:
            if e is TOKEN_ERROR:
                return {
                           'error_no': -1, 'error_info': 'token获取失败，无数据返回'
                       }, {}
            raise
    return wrapper


class GTNClient(object):
    """
    面向GTN的HTTP客户端
    """
    _token_url = None

    def __init__(self, channel, id, secret):
        self._library = BaseHTTPClient(channel)
        self._id = id
        self._secret = secret
        self._token = None
        self._base_url = None

    def set_id(self, id):
        """
        设置用户名
        """
        self._id = id

    def get_id(self):
        """
        获取用户名
        """
        return self._id

    def set_secret(self, secret):
        """
        设置密码
        """
        self._secret = secret

    def get_secret(self):
        """
        获取密码
        """
        return self._secret

    def set_base_url(self, url):
        self._base_url = url

    def get_base_url(self):
        return self._base_url

    def set_token_url(self, url):
        """
        设置获取token时的url
        """
        self._token_url = url

    def get_token_url(self):
        """
        获取token时的url
        """
        if self._token_url is None:
            self._token_url = '{self._base_url}/oauth2/oauth2/token'.format(self=self)
        return self._token_url

    def clear_token(self):
        """
        清除token
        """
        self._token = None

    def flush_token(self):
        """
        刷新并存储token
        """
        # id和secret加密
        authorization = "Basic " + base64.b64encode(
            ("%s:%s" % (self._id, self._secret)).encode(encoding="utf-8")).decode("utf-8")
        # 获取token时请求头
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': authorization
        }
        data = {"grant_type": "CLIENT_CREDENTIALS"}
        error_info, token = self._library.get_token(
            'POST', self.get_token_url(),
            data=data, headers=headers, token_key='access_token'
        )

        if error_info['error_no'] == 0:
            self._token = token
        else:
            # system_log.warning('token未成功刷新')
            self._token = None
        return self._token

    @property
    def token(self):
        if not self._token:
            token = self.flush_token()
            if not token:
                raise TOKEN_ERROR
        return self._token

    @token_check
    def send_by_get(self, url, data=None, request_times=0):
        """
        通过GET方式请求数据
        :param url|str: 请求地址
        :param data|dict: 请求时携带的数据
        :param request_times| int: 请求次数
        :return:
        """
        return self._do_request(
            headers={
                'Authorization': 'Bearer %s' % self.token
            },
            method='GET',
            url=url,
            params=data,
            request_times=request_times
        )

    @token_check
    def send_by_post(self, url, data=None, request_times=0):
        """
        通过Post方式请求数据
        :param url|str: 请求地址
        :param data|dict: 请求时携带的数据
        :param request_times| int: 请求次数
        :return:
        """
        return self._do_request(
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            params={"access_token": self.token},
            method='POST',
            url=url,
            data=data,
            request_times=request_times
        )

    def _do_request(self, method, url, request_times=0, **kwargs):

        if url.startswith('/'):
            url = self._base_url + url

        try:
            res = self._library.request(method=method, url=url, **kwargs)
            # 正常返回
            if res['status_code'] == 200:
                body_dict = json.loads(res['body'])
                if body_dict.get('error_code'):
                    return {
                               'error_no': body_dict['error_code'],
                               'error_info': body_dict['error_info']
                           }, {}
                else:
                    return {
                               'error_no': 0, 'error_info': ''
                           }, body_dict
            # token过期后刷新
            elif res['status_code'] == 401:
                # system_log.debug('刷新token')
                token = self.flush_token()
                if token and request_times < 5:
                    # token刷新次数限制
                    request_times += 1
                    return self._do_request(
                        method, url, request_times, **kwargs
                    )
                else:
                    error_no = -1
                    error_info = 'token刷新异常，应答错误号:[%d]' % res['status_code']
                    return {'error_no': error_no, 'error_info': error_info}, {}
            elif 400 <= res['status_code'] <= 499:
                error_no = res['status_code']
                error_info = res['body']
                return {'error_no': error_no, 'error_info': error_info}, {}
            else:
                error_no = -1
                error_info = '服务器处理异常，应答错误号:[%d]' % res['status_code']
                return {'error_no': error_no, 'error_info': error_info}, {}
        except ConnectionRefusedError as e1:
            error_no = -1
            error_info = e1
            return {'error_no': error_no, 'error_info': error_info}, {}
        except Exception as e2:
            error_no = -1
            error_info = e2

            return {'error_no': error_no, 'error_info': error_info}, {}


def create_gtn_client(id, secret, base_url):
    gtn_channel = RequestChannel()
    gtn_client = GTNClient(gtn_channel, id, secret)
    gtn_client.set_base_url(base_url)
    return gtn_client
