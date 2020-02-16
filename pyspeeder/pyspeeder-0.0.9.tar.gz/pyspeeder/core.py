import base64
import abc
import os
import traceback
from threading import Thread, Timer
import platform
from copy import deepcopy
import time
import json
import re

import requests
import gevent
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException

from .helper import user_agent, get_logger, redis, md5
from .config import config

key_spider = ''
key_request = ''
key_response = ''
key_error = ''
debug_mode = False


class Spider(abc.ABC):
    __metaclass__ = abc.ABCMeta

    def __init__(self, spider_name, debug=False):
        """Create spider.
        :param spider_name: Name of spider
        :param debug: Spider will raise error in debug mode
        """
        global key_spider, key_request, key_response, key_error, debug_mode
        key_spider = f'{spider_name}:spider-{os.getpid()}'
        key_request = f'{spider_name}:request'
        key_response = f'{spider_name}:response'
        key_error = f'{spider_name}:error'
        debug_mode = debug
        self.add_request = add_request
        self.spider_name = spider_name
        self.redis = redis
        self.logger = get_logger('spider')
        self._filter = BloomFilter(spider_name, config.blocks)

    def gen_request(self, url, callback, method='GET', params=None,
                    data=None, json=None, headers=None, cookies=None,
                    proxies=None, timeout=10, meta=None, auth=None,
                    encoding='utf-8', allow_redirects=True, verify=False,
                    stream=None, binary=False, delay=0, filter=False, force=False):
        """Generate request into redis.
        :param url: Url for this request(web request)
        :param callback: Name of callback function for the request. Set blank str('') if there's no callback
        :param method: Method for this request, support "get" and "post", lower and upper case both work
        :param params: Dict to be sent in the query string
        :param data: Form data to send
        :param json: Json data to send
        :param headers: Dict of HTTP Headers to send
        :param cookies: Dict of cookies to send
        :param proxies: Dict mapping protocol to the URL of the proxy
        :param timeout: Max read time of request
        :param meta: Context for your project, <Dict> required
        :param auth: Auth tuple to enable Basic/Digest/Custom HTTP Auth
        :param encoding: Encode type for response parser
        :param allow_redirects: Enable/disable redirection
        :param verify: Boolean to enable/disable verify the server's TLS certificate, or a string of CA path
        :param stream: Whether to immediately download the response content
        :param binary: Set "True" for binary response
        :param delay: Seconds you want to delay the request
        :param filter: Set "True" to filter the request
        :param force: Set "True" to force add the request without filter
        """
        if callback and not hasattr(self, callback):
            raise AttributeError(f'callback "{callback}" not exists')
        if method.upper() != 'GET' and method.upper() != 'POST':
            raise ValueError('invalid method')

        request = {
            'url': url,
            'callback': callback,
            'method': method.upper(),
            'params': params,
            'data': data,
            'json': json,
            'headers': headers,
            'cookies': cookies,
            'auth': auth,
            'encoding': encoding,
            'timeout': timeout,
            'allow_redirects': allow_redirects,
            'proxies': proxies,
            'stream': stream,
            'verify': verify,
            'meta': meta,
            'binary': binary,
            'retry': -1,
        }
        if filter and self.is_duplicate(request) and not force:
            return
        Timer(delay, add_request, args=[deepcopy(request)]).start()

    def start(self, init=True):
        """Start spider and waiting for requests."""
        if debug_mode:
            self.logger.warning('spider running in debug mode.')
        if len(redis.keys(f'{self.spider_name}:spider-*')) == 0 or init:
            redis.delete(key_request)
            redis.delete(key_response)
            redis.delete(key_error)
            self.logger.warning('redis cache has been removed.')
            self.init()

        # init & sign up spider
        if redis.exists(key_spider):
            raise KeyError(f'<{key_spider}> already exists')
        redis.hmset(key_spider, {
            'node': platform.node(),
            'os': platform.system(),
            'spider_name': self.spider_name,
            'pid': os.getpid(),
            'concurrency': config.concurrency,
            'create_at': int(time.time()),
            'heartbeat': int(time.time()),
            'downloads': 0,
        })
        start_child_thread(func=self._heartbeat, name='heartbeat')
        worker = Worker(self.spider_name, self.patch_request)
        start_child_thread(func=worker.start)
        self.logger.info('init complete, spider is running')

        # polling & waiting for requests
        while True:
            response = redis.rpop(key_response)
            if response is None:
                time.sleep(1)
            else:
                response = json.loads(response)
                try:
                    callback = response['callback']
                    if self.check_response(response):
                        continue
                    getattr(self, callback)(response) if callback else None
                except Exception as error:
                    request = response['request']
                    info = traceback.format_exc()
                    html = response['text'] if not request['binary'] else 'binary file'
                    self.logger.info(f'error occurred:\n[request]\n{request}\n[html]\n{html}\n[info]\n{info}')
                    if debug_mode:
                        raise error

    def _heartbeat(self):
        if redis.exists(key_spider):
            redis.hset(key_spider, 'heartbeat', int(time.time()))
            redis.expire(key_spider, 60 * 5)
        Timer(interval=60, function=self._heartbeat).start()

    @abc.abstractmethod
    def init(self):
        """Generate start urls."""
        pass

    def patch_request(self, request):
        """
        This function must be staticmethod!
        Override to set dynamic params for request before using, eg: proxies, cookies, auth.
        """
        pass

    def check_response(self, response):
        """
        Override to check response before callback function.
        :return: return True to skip callback function
        """
        return False

    def is_duplicate(self, request):
        """Filter duplicated urls by bloom-filter."""
        url = request['url']
        params = request['params'] if request['params'] else dict()
        string = url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()])
        if self._filter.has_str(string):
            return True  # duplicated
        else:
            self._filter.insert(string)
            return False  # not duplicated


class Worker:
    adapter = HTTPAdapter(
        pool_connections=config.concurrency * 3,
        pool_maxsize=config.concurrency * 3,
        max_retries=3
    )

    def __init__(self, spider_name, patch_request):
        requests.packages.urllib3.disable_warnings()
        self.spider_name = spider_name
        self.patch_request = patch_request
        self.downloads = 0
        self.logger = get_logger('worker')

    def start(self):
        self.logger.info('start a new worker')
        start_child_thread(func=self.count_downloads)

        while True:
            request_list = list()
            for _ in range(config.concurrency):
                request = redis.rpop(key_request)
                if request is None:
                    time.sleep(1)
                    break
                request_list.append(json.loads(request))

            spawn_list = list()
            for request in request_list:
                spawn = gevent.spawn(self.download, request)
                spawn_list.append(spawn)
            gevent.joinall(spawn_list)

    def download(self, request):
        self.patch_request(request)
        response = {
            'request': deepcopy(request),
            'callback': request['callback'],
            'meta': request['meta'],
        }
        try:
            session = requests.session()
            session.mount('http://', self.adapter)
            [session.cookies.set(k, v) for k, v in request['cookies'].items()] if request['cookies'] else None
            rsp = session.request(
                url=request['url'],
                method=request['method'],
                params=request['params'],
                data=request['data'],
                headers=request['headers'] if request['headers'] else {'User-Agent': user_agent()},
                cookies=request['cookies'],
                auth=request['auth'],
                timeout=(5, request['timeout']),
                allow_redirects=request['allow_redirects'],
                proxies={
                    'http': f'http://{request["proxies"]}',
                    'https': f'http://{request["proxies"]}'
                } if request["proxies"] else None,
                stream=request['stream'],
                verify=request['verify'],
                json=request['json'],
            )
            self.downloads += 1
        except RequestException as e:
            if debug_mode:
                self.logger.error(e)
            add_request(response['request'])
        else:
            encoding = re.findall(r'<meta.*?charset="?(utf-8|UTF-8|gbk|GBK).*?>', rsp.text)
            rsp.encoding = request['encoding'] if len(encoding) == 0 else encoding[0].lower()
            response.update({
                'url': rsp.url,
                'text': rsp.text if not request.get('binary') else None,
                'content': base64.b64encode(rsp.content).decode() if request.get('binary') else None,
                'status_code': rsp.status_code,
                'cookies': session.cookies.get_dict(),
                'headers': dict(rsp.headers),
            })
            redis.lpush(key_response, json.dumps(response, ensure_ascii=False))
            if config.worker_log:
                self.logger.info(f'{request["callback"]} {request["url"]} {request["meta"]}')

    def count_downloads(self):
        if redis.exists(key_spider):
            redis.hincrby(key_spider, 'downloads', self.downloads)
        self.downloads = 0
        Timer(interval=1, function=self.count_downloads).start()


def add_request(request):
    request['retry'] += 1
    if request['retry'] < config.max_retry:
        data = json.dumps(request, ensure_ascii=False)
        redis.lpush(key_request, data) if request['retry'] == 0 else redis.rpush(key_request, data)
    elif debug_mode is False and config.cache_error_request:
        redis.sadd(key_error, json.dumps(request, ensure_ascii=False))


def start_child_thread(func, args=(), name=None, daemon=True, join=False):
    thread = Thread(target=func, args=args, name=name)
    thread.daemon = daemon
    thread.start()
    thread.join() if join else None
    return thread


class BloomFilter(object):
    def __init__(self, name, blocks):
        """
        :param name: redis key name
        :param blocks: each block cost 8M memory, filter 1,040,000 str, keep error bellow 0.001%
        """
        self.bit_size = 1 << 25
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.name = name
        self.block_size = blocks
        self.hash_func = []
        for seed in self.seeds:
            self.hash_func.append(SimpleHash(self.bit_size, seed))

    def has_str(self, str_input):
        if not str_input:
            return False
        str_input = md5(str_input)
        result = True
        for f in self.hash_func:
            loc = f.hash(str_input)
            result = result & redis.getbit(self._key(str_input), loc)
        return result

    def insert(self, str_input):
        str_input = md5(str_input)
        for f in self.hash_func:
            loc = f.hash(str_input)
            redis.setbit(self._key(str_input), loc, 1)

    def _key(self, str_input):
        return f'{self.name}:filter:{int(str_input[0:2], 16) % self.block_size}'


class SimpleHash(object):
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret
