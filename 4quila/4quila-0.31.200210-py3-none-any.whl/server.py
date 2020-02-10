#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import _4quila
import asyncio
from tornado.web import RequestHandler, Application
import json

def parse_ip_port(ip_port):
    if isinstance(ip_port, int) or ":" not in ip_port:
        return "127.0.0.1", int(ip_port)
    else:
        ip, port = ip_port.split(":")
        return ip, int(port)

def http(ip_port, handlers):
    class _Handler(RequestHandler):
        SUPPORTED_METHODS = ["GET", "POST"]

        async def get(self):
            await self.handle()

        async def post(self):
            await self.handle()

        async def handle(self):
            match_handler = None
            max_match_length = 0
            for path, handler in handlers.items():
                if self.request.path.startswith(path):
                    match_length = len(path)
                    if match_length > max_match_length:
                        max_match_length = match_length
                        match_handler = handler

            if match_handler is None:
                self.set_status(404)
                self.finish()
                return

            func_name = "handle_%s" % self.request.path[max_match_length:]
            func = getattr(match_handler, func_name, None)
            if func is None:
                self.set_status(404)
                self.finish()
                return

            if self.request.arguments:
                request = dict(
                    (i, j[0].decode()) for i, j in self.request.arguments.items()
                )
            else:
                request = json.loads(self.request.body or "{}")

            request = dict((i, str(j)) for i, j in request.items())

            response = await func(**request)

            if isinstance(response, dict):
                self.write(json.dumps(response))
            else:
                self.write(response)
            self.finish()

    ip, port = parse_ip_port(ip_port)
    Application([(r".*", _Handler,)]).listen(port, address=ip)

    asyncio.get_event_loop().run_forever()
