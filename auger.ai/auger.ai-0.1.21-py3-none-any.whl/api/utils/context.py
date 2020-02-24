import os
import sys
import logging

from auger.api.credentials import Credentials
from auger.api.cloud.rest_api import RestApi
from auger.api.utils.config import Config

log = logging.getLogger("auger")


class Context(object):

    def __init__(self, name=''):
        super(Context, self).__init__()
        self.config = Config()
        if name and len(name) > 0:
            self.name = "{:<9}".format('[%s]' % name)
        else:
            self.name = name
        self.debug = self.config.get('debug', False)
        self.credentials = Credentials(self).load()
        self.rest_api = RestApi(
            self.credentials.api_url, self.credentials.token, debug=self.debug)

    def copy(self, name):
        new = Context(name)
        new.config = self.config
        return new

    def log(self, msg, *args, **kwargs):
        log.info('%s%s' %(self.name, msg), *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        log.debug('%s%s' %(self.name, msg), *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        log.error('%s%s' %(self.name, msg), *args, **kwargs)

    @staticmethod
    def setup_logger(format='%(asctime)s %(name)s | %(message)s'):
        logging.basicConfig(
            stream=sys.stdout,
            datefmt='%H:%M:%S',
            format=format,
            level=logging.INFO)
