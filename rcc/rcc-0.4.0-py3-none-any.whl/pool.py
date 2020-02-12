'''A connection pool'''

from rcc.connection import Connection


class ConnectionPool(object):
    '''Not asyncio 'thread' safe (yet)
    '''

    def __init__(self):
        self.connections = {}

    def get(self, url: str):
        if url not in self.connections:
            connection = Connection(url, '')  # FIXME password
            self.connections[url] = connection

        return self.connections[url]
