#!/usr/bin/env python
# -*- coding: utf-8 -*
# Copyright - See LICENSE for details
# Authors: Guannan Ma @mythmgn
"""
:description:
    sms related class
"""
import copy
import urlparse

from cup.bidu.cloud import bcesigner
from cup.thirdp import requests

class BceSMS(object):
    """
    bce sms
    """
    URI = '/api/v3/sendsms'
    SMS_TYPES = ['normal', 'sales']
    DEFAULAT_DATA = {
        'mobile': None,
        'template': None,
        'sign': None,
        'type': 'normal',
        'contentVar': None
    }

    def __init__(self, access_key, secret_key, sign, internal=True):
        """
        :param internal:
            if you are NOT using it internally, plz set it to False
        """
        self._ak = access_key
        self._sk = secret_key
        self._signer = bcesigner.ClassBceSigner(
            self._ak, self._sk
        )
        self._endpoint = 'smsv3.bj.baidubce.com'
        if internal:
            self._endpoint = 'smsv3.bce-internal.baidu.com'
        self._port = 80
        self._sign = sign

    def service_url(self):
        """
        return service url
        """
        return 'http://{0}{1}'.format(self._endpoint, self.URI)

    def gen_sms_headers(self, headers=None, method='POST'):
        """
        gen_bcesigner_headers
        """
        module_header = {
            'x-bce-date': str(bcesigner.get_utc_time()),
            'host': ('%s:%s' % (self._endpoint, self._port)),
            'Content-type': 'application/json'
        }
        # if header is not none, put it in header
        if headers is not None:
            for key in headers.keys():
                module_header[key] = headers[key]
        request = {
            'method': method,
            'uri': urlparse.urlsplit(self.URI).path,
            'params': {},
            'headers': module_header.copy()
        }
        # if there is query parameters in uri, put it in request['params']
        query = urlparse.urlsplit(self.URI).query
        if query:
            query_list = query.split('&')
            for eachquery in query_list:
                query_params = eachquery.split('=')
                request['params'][query_params[0]] = query_params[1]
        auth = self._signer.gen_authorization(
            request, bcesigner.get_utc_time()
        )
        module_header['authorization'] = auth
        return module_header

    def send(self, tmpl, kvs, mobiles, sms_type='normal'):
        """
        send sms with template.

        Code Example:

        ::

        import cup
        from cup.bidu.cloud import sms
        s = sms.BceSMS(
            'access_key', 'secret_key', '签名')
        ret = s.send(
            'sms-tmpl-xxxxxxxx', {'content': '试验sms可达'},
            '185136xxxxx'
        )
        if ret.status_code == 200:
            log.info('send success')
        else:
            log.error('failed, msg detail:{0}'.format(ret['content']))

        :param tmpl:
            sms template id in str
        :param kvs:
            customized code key values.
            For example:
            example 1: templateid='xxxxx', kvs={'code': 7860}
            example 2: templateid='xyyyy', kvs={'content':
        :param mobiles:
            mobile phone no, multiple ones seperated by commas
            e.g.    13xxxxxxxx, 13xxxxxxxx
        :param sms_type:
            'normal' by default. you can set up to 'sales' if needed
        :raise exception:
            if any value of tmpl, kvs, mobiles are None, will raise ValueError
        :return:
            a object of requests response.
            on success, response.status_code == 200.
            response.content will tell you info like below {
                "requestId":"223ad7f9-xxxx",
                "code":"1000", "message":"success",
                "data":[{"code":"1000","message":"success",
                "mobile":"138xxxxxxx","messageId":"223ad7f9-xxxxx"}]
            }

            on failure, response['status_code'] will a number other than 200
        """
        if any([
            tmpl is None,
            mobiles is None,
            kvs is None,
            sms_type not in self.SMS_TYPES
        ]):
            raise ValueError('tmpl kvs and mobiles are required')
        data = copy.deepcopy(self.DEFAULAT_DATA)
        data['mobile'] = mobiles
        data['template'] = tmpl
        data['contentVar'] = kvs
        data['sign'] = self._sign
        data['type'] = sms_type
        hdrs = self.gen_sms_headers()
        return requests.post(self.service_url(), headers=hdrs, json=data)

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
