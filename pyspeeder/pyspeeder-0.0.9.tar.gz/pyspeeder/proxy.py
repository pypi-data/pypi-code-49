import abc
import json
import time
from random import choice

import requests

from pyspeeder.helper import md5, get_logger, redis


class Proxy(abc.ABC):
    logger = get_logger('proxy')

    @classmethod
    def get(cls, _all=False):
        pool = list()
        key_proxies = redis.keys('proxy:*')
        if len(key_proxies) > 0 and _all is False:
            proxy = redis.get(choice(key_proxies))
            if proxy is None:
                return
            proxy = json.loads(proxy)
            host, port = proxy['host'], proxy['port']
            return f'{host}:{port}'
        if len(key_proxies) > 0 and _all is True:
            for key in key_proxies:
                try:
                    proxy = json.loads(redis.get(key))
                    host, port = proxy['host'], proxy['port']
                    pool.append(f'{host}:{port}')
                except:
                    continue
            return pool

    def _save(self, host, port, ttl=60, platform=None):
        key_proxy = f'proxy:{md5(f"{host}:{port}")}'
        if not redis.exists(key_proxy):
            redis.set(key_proxy, json.dumps({
                'host': host,
                'port': port,
                'ttl': ttl,
                'expire_at': int(time.time()) + ttl,
                'platform': platform
            }, ensure_ascii=False))
            redis.expire(key_proxy, ttl)
            self.logger.info(f'{host}:{port}')

    @abc.abstractmethod
    def start(self, *args):
        pass


class Data5u(Proxy):
    def __init__(self, token):
        self.token = token

    def start(self):
        while True:
            time.sleep(1)
            try:
                url = 'http://api.ip.data5u.com/dynamic/get.html'
                params = {'order': self.token, 'json': True, 'ttl': ''}
                rsp = requests.get(url, params=params, timeout=20)

                if 'too many request' in rsp.text:
                    pass
                elif rsp.json()['success'] is False:
                    self.logger.info(f'invalid token: {self.token}')
                else:
                    for item in rsp.json()['data']:
                        host, port, ttl = item['ip'], item['port'], item['ttl'] // 1000
                        self._save(host, port, ttl, platform='data5u')
            except Exception as error:
                self.logger.info(f'{error}')
