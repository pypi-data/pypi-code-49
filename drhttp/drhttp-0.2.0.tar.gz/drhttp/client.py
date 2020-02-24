import base64
import logging
import requests
import threading
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

ENCODING = 'utf-8'

logger = logging.getLogger('drhttp')

class DrHTTPClient:
    # dsn example : https://<api_key>@api.drhttp.com/
    def __init__(self, dsn, event_loop=None):
        self.dsn = urlparse(dsn)

    def sendData(self, data):
        headers = {
            'Content-Type': 'application/json; charset=%s' % ENCODING,
            'DrHTTP-ApiKey': self.dsn.username
        }
        url = '{protocol}://{url}/api/v1/http_record/record'.format(protocol=self.dsn.scheme, url=self.dsn.hostname)
        try:
            r = requests.post(url, json=data, headers=headers)
            logger.info(" Sent %s [%d - %.0fms]" % (data['id'], r.status_code, r.elapsed.total_seconds() * 1000))
        except requests.exceptions.ConnectionError as e:
            logger.error(e)
            
    def record(self, request_id, datetime, user_identifier,
                    method, uri, request_headers, request_data,
                    status, response_headers=None, response_data=None):
        data = {
            'datetime': datetime.isoformat(),
            'method': method,
            'uri': uri,
            'status': status,
            'request' : {
                'headers': {k: v for k,v in request_headers.items()},
                'body': self.data_to_json(request_data)
            }
        }
        if request_id:
            data['id'] = request_id
        if user_identifier:
            data['user_identifier'] = user_identifier
        if response_headers or response_data:
            data['response'] = {}
        if response_headers:
            data['response']['headers'] = {k: v for k,v in response_headers.items()}
        if response_data:
            data['response']['body'] = self.data_to_json(response_data)
        
        self.sendData(data)
                
    def data_to_json(self, data):
        try:
            return data.decode(ENCODING)
        except UnicodeError:
            return "Data could not be decoded with %s" % ENCODING
