'''
ScrapyWarcIo class
~~~~~~~~~~~~~~~~~~
'''
import json
import logging
import os
import socket
import sys
import uuid
from collections import OrderedDict

from datetime import datetime
from io import BytesIO
from urllib.parse import urlparse

from warcio import StatusAndHeaders
from warcio import WARCWriter
from scrapy import __version__ as scrapy_version
import scrapy

def _bytes(val):
    '''
    always returns bytes from str or bytes
    '''
    return val if isinstance(val, bytes) else bytes(val, 'utf-8')


def _str(val):
    '''
    always returns string from str or bytes
    '''
    return val if isinstance(val, str) else str(val, 'utf-8')


def warc_date():
    '''
    returns UTC now in WARC-Date format (YYYY-mm-ddTHH:ii:ssZ)
    '''
    return datetime.utcnow().isoformat() + 'Z'


class ScrapyWarcIo:
    '''
    Scrapy DownloaderMiddleware WARC input/output methods
    '''

    REQUIRED = [
        'WARC_COLLECTION',
        'WARC_DESCRIPTION',
        'WARC_MAX_SIZE',
        'WARC_OPERATOR',
        'WARC_ROBOTS',
        'WARC_USER_AGENT',
        'JOBDIR',
        'WARC_PREFIX',
        'WARC_SPEC']
    WARC_LINE_SEP = '\r\n'
    WARC_SERIAL_ZFILL = 5

    warc_dest = None
    warc_fname = None
    warc_count = 0
    warc_size = 0
    warc_writer = WARCWriter

    def __init__(self, config):
        self.log = logging.getLogger(__name__)
        self.max_serial = int('9' * self.WARC_SERIAL_ZFILL)
        self.req_date_set = False
        self.config = config
        for item in self.REQUIRED:
            if self.config.get(item) is None:
                raise ValueError(
                    'required config item: {} is None'.format(item))

    def bump_serial(self, content_bytes):
        '''
        increment WARC serial number and create a new WARC file iff
        file size + (uncompressed) additional content may exceed
        max_warc_size in settings
        :param  content_bytes  size in bytes of new content (uncompressed)
        '''
        create_new_warc = False

        if self.warc_fname is None:
            create_new_warc = True
        else:
            if os.path.exists(self.warc_fname):
                self.warc_size = os.stat(self.warc_fname).st_size
                estimate = self.warc_size + content_bytes
                if estimate >= self.config['WARC_MAX_SIZE']:
                    create_new_warc = True

        if create_new_warc:
            self.warc_fname = self.warcfile()
            self.log.info('New WARC file: %s', self.warc_fname)
            self.write_warcinfo()
            self.warc_count += 1

    @staticmethod
    def __record_id():
        '''
        returns WARC-Record-ID (globally unique UUID) as a string
        '''
        return '<urn:uuid:{}>'.format(uuid.uuid1())

    def get_headers(self, record):
        '''
        returns WARC record headers as a string from Scrapy object
        if record.method, returns request headers
        if record.status, returns response headers
        else raises ValueError
        :param  record  <scrapy.http.Request> or <scrapy.http.Response>
        '''
        if not hasattr(record, 'headers'):
            return ''

        if hasattr(record, 'method'):  # request record
            purl = urlparse(record.url)
            http_line = ' '.join([record.method, purl.path, 'HTTP/1.0'])
        elif hasattr(record, 'status'):  # response record
            http_line = ' '.join(['HTTP/1.0', str(record.status)])
        else:
            raise ValueError('Unable to form http_line from record.')

        headers = []
        for key in record.headers:
            val = record.headers[key]
            headers.append((_str(key), _str(val)))

        return http_line,headers

    def warcfile(self):
        '''
        returns new WARC filename from warc_prefix setting and current
        WARC count. WARC filename format compatible with
        internetarchive/draintasker warc naming #1:
        {TLA}-{timestamp}-{serial}-{fqdn}.warc.gz
        raises IOError if WARC file exists
        '''
        if self.warc_count > self.max_serial:
            raise ValueError('warc_count: {} exceeds max_serial: {}'.format(
                self.warc_count, self.max_serial))

        tla = self.config['WARC_PREFIX']
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        serial = str(self.warc_count).zfill(self.WARC_SERIAL_ZFILL)
        fqdn = socket.gethostname().split('.')[0]

        warc_name = '-'.join([tla, timestamp, serial, fqdn]) + '.warc.gz'
        warc_dest = self.config['JOBDIR'] or ''

        if warc_dest and not os.path.exists(warc_dest):
            raise IOError('warc_dest not found: {}'.format(warc_dest))

        fname = os.path.join(warc_dest, warc_name)

        if os.path.exists(fname):
            raise IOError('WARC file exists: {}'.format(fname))

        return fname

    def write(self, response:scrapy.http.Response, request:scrapy.http.Request):
        '''
        write WARC-Type: response, then WARC-Type: request records
        from Scrapy response and request
        Notes:
        1) It is customary to write the request record immediately
           after the response record to protect against a
           request-response pair spanning more than one WARC file.
        2) The WARC-Date of the response must be identical to the
           WARC-Date of the request.
        :param  response  <scrapy.http.Response>
        :param  request   <scrapy.http.Request>
        '''
        if not hasattr(response, 'status'):
            raise ValueError('Response missing HTTP status')

        if not hasattr(response, 'body'):
            raise ValueError('Response missing body')

        if not hasattr(request, 'method'):
            raise ValueError('Request missing method')

        if not hasattr(request, 'meta'):
            raise ValueError('Request missing meta')

        if not request.meta.get('WARC-Date'):
            raise ValueError('Request missing WARC-Date')

        if request.meta.get('dont_cache', False):
            return

        warc_headers_dict = {'WARC-Date': request.meta['WARC-Date']}
        self.bump_serial(sys.getsizeof(response.body) + sys.getsizeof(request.body))
        with open(self.warc_fname, 'ab') as _fh:
            writer = self.warc_writer(_fh)
            resp = writer.create_warc_record(response.url, 'response',
                                             payload=BytesIO(response.body),
                                             length=len(response.body),
                                             warc_content_type='application/http;msgtype=response',
                                             warc_headers_dict=warc_headers_dict,
                                             http_headers=StatusAndHeaders(*self.get_headers(response),is_http_request=True))

            req = writer.create_warc_record(request.url, 'request',
                                            payload=BytesIO(request.body),
                                            length=len(request.body),
                                            warc_content_type='application/http;msgtype=request',
                                            warc_headers_dict=warc_headers_dict,
                                            http_headers=StatusAndHeaders(*self.get_headers(response)))
            url = resp.rec_headers.get_header('WARC-Target-URI')
            dt = resp.rec_headers.get_header('WARC-Date')

            req.rec_headers.replace_header('WARC-Target-URI', url)
            req.rec_headers.replace_header('WARC-Date', dt)

            resp_id = resp.rec_headers.get_header('WARC-Record-ID')
            if resp_id:
                req.rec_headers.add_header('WARC-Concurrent-To', resp_id)
            req_id = req.rec_headers.get_header('WARC-Record-ID')
            writer.write_record(req)
            writer.write_record(resp)
            if request.meta:
                if req_id and len(request.meta) > 1:
                    req_payload = json.dumps(request.meta).encode('utf-8')
                    req_meta = writer.create_warc_record(request.url, 'metadata',
                                                         payload=BytesIO(req_payload),
                                                         length=len(req_payload),
                                                         warc_content_type='application/json')
                    req_meta.rec_headers.add_header('WARC-Concurrent-To', req_id)
                    writer.write_record(req_meta)

            if response.meta:
                if resp_id and len(response.meta)>1:
                    resp_payload = json.dumps(response.meta).encode('utf-8')
                    resp_meta=writer.create_warc_record(response.url, 'metadata',
                                                      payload=BytesIO(resp_payload),
                                                      length=len(resp_payload),
                                                      warc_content_type='application/json')
                    resp_meta.rec_headers.add_header('WARC-Concurrent-To', resp_id)
                    writer.write_record(resp_meta)

    def write_warcinfo(self):
        '''
        write WARC-Type: warcinfo record
        '''
        with open(self.warc_fname, 'ab') as _fh:
            writer = self.warc_writer(_fh)
            record = writer.create_warcinfo_record(self.warc_fname, self.warc_info())
            writer.write_record(record)

    def warc_info(self):
        '''
        create warcinfos
        '''
        return OrderedDict([
            ('software', 'Scrapy/{} (+https://scrapy.org)'.format(scrapy_version)),
            ('ip', '{}'.format(socket.gethostbyname(socket.gethostname()))),
            ('hostname', '{}'.format(socket.gethostname())),
            ('format', 'WARC file version 1.0'),
            ('conformsTo', '{}'.format(self.config['WARC_SPEC'])),
            ('operator', '{}'.format(self.config['WARC_OPERATOR'])),
            ('isPartOf', '{}'.format(self.config['WARC_COLLECTION'])),
            ('description', '{}'.format(self.config['WARC_DESCRIPTION'])),
            ('robots', '{}'.format(self.config['WARC_ROBOTS'])),
            ('http-header-user-agent', '{}'.format(self.config['WARC_USER_AGENT'])),
        ])
