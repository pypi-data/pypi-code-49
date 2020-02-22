#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tornado Blueprint蓝图的实现。"""
import asyncio
import collections
import inspect
import logging
import signal

import tornado.netutil
import tornado.process
import tornado.web
import uvloop
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define
from tornado.options import options
from utils import get_ip

__all__ = ['Blueprint', 'Application']


class BlueprintMeta(type):
    derived_class = []

    def __new__(cls, name, bases, attr):
        _class = super(BlueprintMeta, cls).__new__(cls, name, bases, attr)
        cls.derived_class.append(_class)
        return _class

    @classmethod
    def register(cls, app):
        for _class in cls.derived_class:
            for blueprint in _class.blueprints:
                app.register(blueprint)


class Blueprint(metaclass=BlueprintMeta):
    blueprints = []

    def __init__(self, name=None, url_prefix='/', host='.*', strict_slashes=False):
        self.name = name
        self.host = host
        self.url_prefix = url_prefix
        self.strict_slashes = strict_slashes
        self.rules = []
        self.events = collections.defaultdict(list)
        self.blueprints.append(self)

    def route(self, uri, params=None, name=None):
        def decorator(handler):
            assert uri[0] == '/'
            rule_name = name or handler.__name__
            if self.name:
                rule_name = f'{self.name}.{rule_name}'
            rule_uri = self.url_prefix.rstrip('/') + uri
            self.rules.append((rule_uri, handler, params, rule_name))
            if not self.strict_slashes and rule_uri.endswith('/'):
                self.rules.append((rule_uri.rstrip('/'), handler, params, None))
            return handler
        return decorator

    def listen(self, event):
        def decorater(func):
            self.events[event].append(func)
        return decorater


class Application(Blueprint):

    def __init__(self, name=None, url_prefix='/', host='.*', strict_slashes=False, **kwargs):
        super().__init__(name, url_prefix, host, strict_slashes)
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        self.logger = logging
        self.kwargs = kwargs
        self.handlers = []
        self.prefix = 'web'
        self.options = options
        self.ioloop = IOLoop.current()
        self.loop = self.ioloop.asyncio_loop
        self.events = collections.defaultdict(list)

        define("debug", default=True, help="debug mode", type=bool)
        define("port", default=8000, help="listen port", type=int)
        define("workers", default=1, help="running workers", type=int)
        options.parse_command_line()

    def register(self, *blueprints, url_prefix='/'):
        assert url_prefix[0] == '/'
        url_prefix = url_prefix.rstrip('/')
        for blueprint in blueprints:
            rules = [(url_prefix + x[0], *x[1:]) for x in blueprint.rules]
            self.handlers.append((blueprint.host, rules))
            for rule in rules:
                setattr(rule[1], 'app', self)
            if blueprint != self:
                for k, v in blueprint.events.items():
                    self.events[k].extend(v)

    def url_for(self, endpoint, *args, **kwargs):
        return self.app.reverse_url(endpoint, *args, **kwargs)

    def make_app(self, **kwargs):
        kwargs.setdefault('static_path', 'static')
        kwargs.setdefault('template_path', 'templates')
        kwargs.setdefault('cookie_secret', 'YWpzYWhkaDgyMTgzYWpzZGphc2RhbDEwMjBkYWph')
        kwargs.setdefault('xsrf_cookie', True)
        kwargs.setdefault('login_url', '/signin')
        kwargs.setdefault('gzip', True)
        kwargs.setdefault('debug', options.debug)
        app = tornado.web.Application(**kwargs)
        for host, rules in self.handlers:
            app.add_handlers(host, rules)
        return app

    async def shutdown(self):
        for func in self.events['before_server_stop']:
            ret = func(self)
            if inspect.isawaitable(ret):
                await ret

        self.server.stop()
        self.logger.info('shutting down')
        tasks = [task for task in asyncio.Task.all_tasks() if task is not
                 asyncio.tasks.Task.current_task()]
        if tasks:
            self.logger.warning(f'canceling {len(tasks)} pending tasks')
            await asyncio.sleep(1)
            task = asyncio.gather(*tasks, return_exceptions=True)
            task.cancel()

        self.ioloop.stop()

    def sig_handler(self, sig, frame):
        self.logger.warning(f'received signal {sig}')
        self.ioloop.add_callback_from_signal(self.shutdown)

    def run(self, port=None, workers=None, xheaders=True, max_buffer_size=None):
        port = port or options.port
        workers = workers or options.workers
        sockets = tornado.netutil.bind_sockets(port)
        if not options.debug and workers > 1:
            tornado.process.fork_processes(workers)

        signal.signal(signal.SIGTERM, self.sig_handler)
        signal.signal(signal.SIGINT, self.sig_handler)

        if hasattr(self, 'initialize'):
            ret = self.initialize()
            if inspect.isawaitable(ret):
                self.loop.run_until_complete(ret)
        for func in self.events['before_server_start']:
            ret = func(self)
            if inspect.isawaitable(ret):
                self.loop.run_until_complete(ret)

        self.register(self)
        self.app = self.make_app(**self.kwargs)
        self.server = HTTPServer(self.app, xheaders=xheaders, max_buffer_size=max_buffer_size)
        self.server.add_sockets(sockets)
        self.logger.info(f"Debug: {self.app.settings['debug']}, Running: http://{get_ip()}:{port}")
        self.ioloop.start()
