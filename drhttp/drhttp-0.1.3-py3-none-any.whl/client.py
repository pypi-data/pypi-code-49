#import aiohttp      TODO async if app is running in an sync application server
#import asyncio      TODO async
import base64
import requests
import threading
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

ENCODING = 'utf-8'

class DrHTTPClient:
    # dsn example : https://<api_key>@api.drhttp.com/
    def __init__(self, dsn, event_loop=None):
        self.dsn = urlparse(dsn)
        # if event_loop:      TODO async
        #     self.event_loop = event_loop 
        # else:
        #     self.event_loop = asyncio.new_event_loop()
        #     self.event_loop.set_debug(True)
        #     self.event_loop_thread = threading.Thread(target = self.event_loop.run_forever)
        #     self.event_loop_thread.setDaemon(True)
        #     self.event_loop_thread.start()

    def sendData(self, data):
        headers = {
            'Content-Type': 'application/json; charset=%s' % ENCODING,
            'DrHTTP-ApiKey': self.dsn.username
        }
        url = '{protocol}://{url}/api/v1/http_record/record'.format(protocol=self.dsn.scheme, url=self.dsn.hostname)
        requests.post(url, json=data, headers=headers)
        # """      TODO async
        # async with aiohttp.ClientSession(loop=self.event_loop) as session:
        #     async with session.post(url, json=data, headers=headers) as response:
        #         resp = await response.text()
        #         return resp

    def record(self, datetime, user_identifier,
                    method, uri, request_headers, request_data,
                    status, response_headers=None, response_data=None):
        data = {
            "datetime": datetime.isoformat(),
            "method": method,
            "uri": uri,
            "status": status,
            "request" : {
                'headers': {k: v for k,v in request_headers.items()},
                'body': self.data_to_json(request_data)
            }
        }
        if user_identifier:
            data["user_identifier"] = user_identifier
        if response_headers or response_data:
            data["response"] = {}
        if response_headers:
            data["response"]['headers'] = {k: v for k,v in response_headers.items()}
        if response_data:
            data["response"]['body'] = self.data_to_json(response_data)
        
        self.sendData(data)
        
        # asyncio.run_coroutine_threadsafe(self.sendData(data), self.event_loop)      TODO async
        
    def data_to_json(self, data):
        try:
            return data.decode(ENCODING)
        except UnicodeError:
            return "Data could not be decoded with %s" % ENCODING
