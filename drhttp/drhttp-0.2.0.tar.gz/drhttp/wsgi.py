import datetime
import logging
from uuid import uuid4
     
from .defines import DRHTTP_HEADER_USER
from .client import DrHTTPClient
from .proxies import IteratableProxy, ReadableProxy
from .utils import extract_user_from_response_headers, format_header_name, url_from_wsgi_env

logger = logging.getLogger('drhttp.wsgimiddleware')

class WSGIMiddleware:
    def __init__(self, app, dsn):
        self.app = app
        self.client = DrHTTPClient(dsn=dsn)

    def __call__(self, environ, start_response):
        # Extract request infos
        content_length = environ.get('CONTENT_LENGTH', '')
        self.request = {
            'id': str(uuid4()),
            'datetime': datetime.datetime.now(),
            'method': environ['REQUEST_METHOD'],
            'url': url_from_wsgi_env(environ),
            'headers': { format_header_name(k): v for k, v in environ.items() if k.startswith('HTTP_') },
            'data': bytearray(),
            'length': int(content_length) if len(content_length) else 0
        }

        # Request body capture
        self.wsgi_input = \
            environ['wsgi.input'] = ReadableProxy(environ['wsgi.input'], self.on_request_body_read)

        # Extract response infos
        self.response = {
            'status_code': 0,
            'headers': {},
            'data': bytearray()
        }

        # Response body capture
        try:
            app_output = self.app(environ, self.captured_start_response(start_response))
            # Warning : on_response_body_end will be called after all the stream is streamed to wsgi's client
            # thus any long operation it can do (send data to drhttp servers) won't impact wsgi response performances
            return IteratableProxy(app_output, self.on_response_body_iterated, self.on_response_body_end) 
        except Exception as exception:
            self.on_app_exception(exception)
            raise exception
        
    def captured_start_response(self, start_response):
        def captured(status, headers, exc_info=None):
            # Capture response status code
            self.response['status_code'] = int(status.split()[0])
            
            # Capture identified user
            user, self.response['headers'] = extract_user_from_response_headers({k: v for k, v in headers}, DRHTTP_HEADER_USER)
            if user is not None:
                self.request['user'] = user
            
            return start_response(status, headers, exc_info)
        
        return captured

    # ---------------------
    # Events
    # ---------------------

    def on_request_body_read(self, data):
        self.request['data'].extend(data)

    def on_response_body_iterated(self, data):
        self.response['data'].extend(data)

    def on_response_body_end(self):
        self.send_record()

    def on_app_exception(self, exception):
        self.response['status_code'] = 500
        self.send_record()

    def send_record(self):
        # Make sure request body has been read
        self.wsgi_input.read(self.request['length'] - len(self.request['data']))
        
        logger.info("Captured " + self.request['id'] + " [" + self.request['url'] + "]")

        self.client.record(self.request['id'], self.request['datetime'], self.request.get('user'),
            self.request['method'], self.request['url'], self.request['headers'], self.request['data'],
            self.response['status_code'], self.response['headers'], self.response['data'])

