# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: Sep 20, 2018
# Modifi: Sep 20, 2018

import redis

from siki.basics import Logger as logger
from siki.basics.Logger import Priority as p
from siki.basics import Exceptions as excepts
from siki.dstruct.Queue import Queue


class PyRedisPool(object):

    def __init__(self, **params):
        """
        setting up a process pool for sql handling
        Args:
        * [params] host, port, db, bstd, blog, dir, fname
        """
        
        self.pool = redis.ConnectionPool(host=params['host'], port=params['port'], db=params['db'])

        if 'bstd' in params.keys() and 'blog' in params.keys() \
            and 'dir' in params.keys() and 'fname' in params.keys():
            logger.init(bool(params['bstd']), bool(params['blog']), params['dir'], params['fname'])
        else:
            logger.init(True, False)
        
        logger.message(p.INFO, msg="redis pool ready")
    

    def set_variable(self, key, val, secs=None, millisecs=None):
        try:
            redis.Redis(connection_pool=self.pool).set(key, val, secs, millisecs)
        except Exception as e:
            logger.message(p.ERROR, msg="set variable failed", exception=e)
    

    def get_variable(self, key):
        try:
            return redis.Redis(connection_pool=self.pool).get(key)
        except Exception as e:
            logger.message(p.ERROR, msg="get variable failed", exception=e)

    
    def ping(self):
        try:
            return redis.Redis(connection_pool=self.pool).ping()
        except Exception as e:
            logger.message(p.ERROR, msg="ping redis failed", exception=e)

    
    def get_keys(self, pattern="*"):
        try:
            return redis.Redis(connection_pool=self.pool).keys(pattern=pattern)
        except Exception as e:
            logger.message(p.ERROR, msg="get keys failed", exception=e)