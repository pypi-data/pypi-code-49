from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer, HTTPServer
from http import HTTPStatus
import socketserver
from threading import Thread
from .invoker import URIInvoker
import logging
import copy
import inspect
import os

logger = logging.getLogger('pinspector')


class PinHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, pin_server=None, **kwargs):
        if pin_server is None:
            self.directory = None
        else:
            self.directory = pin_server.directory
        self.pin_server = pin_server
        super().__init__(*args, directory=self.directory, **kwargs)


    def do_GET(self):
        path = self.path.replace('/' + self.pin_server.prefix + '/', '/', 1)
        if path.startswith('/do/'):
            uri_info = path.split('/', 3)
            # from invoker
            res = self.pin_server.invoker.run(uri_info[2], uri_info[3])
            self.send_response_only(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(bytes(str(res), 'utf-8'))
        else:
            super().do_GET()


class PinServer():

    def __init__(self, port=5678, host='0.0.0.0', title='PIN - Python Inspector', targets=dict()):
        self.port = port
        self.host = host
        self.title = title
        self.prefix = 'pin'
        self.directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/static'
        self.started = False
        all_targets = {'service': self}
        if isinstance(targets, dict):
            for k, v in targets.items():
                all_targets[k] = v
        self.invoker = URIInvoker(all_targets)
        def finish_request(self, request, client_address):
            pin_server = getattr(self, 'pin_server', None)
            if pin_server:
                PinHandler(request, client_address, self, pin_server=pin_server)
            else:
                self.RequestHandlerClass(request, client_address, self)
        ThreadingHTTPServer.finish_request = finish_request

    def __call__(self):
        with ThreadingHTTPServer((self.host, self.port), PinHandler) as httpd:
            httpd.pin_server = self
            self.httpd = httpd
            httpd.serve_forever()

    def start(self):
        if not self.started:
            Thread(target=self).start()
            self.started = True

    def stop(self):
        if self.started:
            self.httpd.shutdown()
            self.started = False

