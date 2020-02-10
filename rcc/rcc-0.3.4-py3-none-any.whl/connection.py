'''Connection class / deals with the underlying socket / TCP transport

Copyright (c) 2020 Machine Zone, Inc. All rights reserved.
'''

import sys
import asyncio
from urllib.parse import urlparse

import hiredis


class Connection(object):
    def __init__(self, url, password, verbose=False):
        netloc = urlparse(url).netloc
        host, _, port = netloc.partition(':')
        if port:
            self.port = int(port)
        else:
            self.port = 6379

        self.host = host

        self.password = password
        self.verbose = verbose

        self._reader = hiredis.Reader()

        self.reader = None
        self.writer = None

        self.read_size = 4 * 1024

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

        if self.password:
            await self.auth(self.password)

    async def readResponse(self):
        '''
        # hiredis.ReplyError
        '''
        response = self._reader.gets()
        while response is False:
            try:
                buf = await self.reader.read(self.read_size)
            except asyncio.CancelledError:
                raise
            except Exception:
                e = sys.exc_info()[1]
                raise ConnectionError(
                    "Error {} while reading from stream: {}".format(type(e), e.args)
                )
            if not buf:
                raise ConnectionError("Socket closed on remote end")

            self._reader.feed(buf)
            response = self._reader.gets()

        # breakpoint()
        return response

    def close(self):
        try:
            if self.writer.can_write_eof():
                self.writer.write_eof()
        except Exception:
            pass

        self.writer.close()

    def writeString(self, data):
        '''
        data should have a type for string or bytes
        '''
        # import pdb; pdb.set_trace()
        # data = data.encode('utf-8')

        self.writer.write(b'$%d\r\n' % len(data))

        if not isinstance(data, bytes):
            self.writer.write(data.encode())
        else:
            self.writer.write(data)

        self.writer.write(b'\r\n')

    async def send(self, cmd, key=None, *args):
        '''key will be used by redis cluster '''

        if len(args) == 0:
            self.writer.write(cmd.encode() + b'\r\n')
        else:
            size = len(args) + 1
            s = f'*{size}\r\n'
            self.writer.write(s.encode())

            self.writeString(cmd)
            for arg in args:
                self.writeString(arg)

        await self.writer.drain()
