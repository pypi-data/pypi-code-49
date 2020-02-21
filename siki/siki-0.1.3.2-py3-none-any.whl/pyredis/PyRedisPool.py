# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: Sep 20, 2018
# LastChg: Feb 20, 2020

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
        """
        stores data to redis

        Args:
        * [key] str key of data
        * [val] string value or anything can be cast to bytes
        * [secs] expiration time in seconds, default is None
        * [millisecs] expiration time in milliseconds, default is None
        """
        try:
            redis.Redis(connection_pool=self.pool).set(key, val, secs, millisecs)
        except Exception as e:
            logger.message(p.ERROR, msg="set variable failed", exception=e)
    



    def set_mulvars(self, dicts, secs=None, millisecs=None):
        """
        stores multiply data to redis

        Args:
        * [dicts(dict)] dictionary type of data with key and value, the key and value should
            both be string or anything that can be cast to bytes
        * [secs] expiration time in seconds, default is None
        * [millisecs] expiration time in milliseconds, default is None
        """
        try:
            r = redis.Redis(connection_pool=self.pool)

            # pipeline
            pipe = r.pipeline()

            for key, val in dicts.items():
                pipe.set(key, val, secs, millisecs)

        except Exception as e:
            logger.message(p.ERROR, msg="set variable(s) failed", exception=e)




    def get_variable(self, key):
        """
        get variable from redis

        Args:
        * [key] the key name to the data
        
        Returns:
        * [str/bytes] the data can be string or bytes
        """
        try:
            return redis.Redis(connection_pool=self.pool).get(key)
        except Exception as e:
            logger.message(p.ERROR, msg="get variable failed", exception=e)




    def get_mulvars(self, keys):
        """
        get variables from redis
        
        Args:
        * [key] the key name to the data
        
        Returns:
        * [list] list of the data can be string or bytes
        """

        try:
            return redis.Redis(connection_pool=self.pool).mget(*keys)
        except Exception as e:
            logger.message(p.ERROR, msg="get variable(s) failed", exception=e)


    

    def ping(self):
        """
        ping the server
        """
        try:
            return redis.Redis(connection_pool=self.pool).ping()
        except Exception as e:
            logger.message(p.ERROR, msg="ping redis failed", exception=e)

    


    def get_keys(self, pattern="*"):
        """
        get a list of keys

        Args:
        * [pattern] pattern to match the keys, default is *

        Returns:
        * [list] list of keys
        """
        try:
            return redis.Redis(connection_pool=self.pool).keys(pattern=pattern)
        except Exception as e:
            logger.message(p.ERROR, msg="get keys failed", exception=e)




    def empty(self):
        """
        clear all keys
        """
        try:
            redis.Redis(connection_pool=self.pool).flushall()
        except Exception as e:
            logger.message(p.ERROR, msg="flush all keys failed", exception=e)



    
    def remove(self, keys):
        """
        remove a key or list of keys from redis

        Args:
        * [key(str/list)] a key string or list of key strings to remove
        """
        try:
            if type(keys) is str:
                redis.Redis(connection_pool=self.pool).delete(keys)
            elif type(key) is str:
                redis.Redis(connection_pool=self.pool).delete(*keys)
            else:
                logger.message(p.Error, msg="remove key with an invalid key type")
        except Exception as e:
            logger.message(p.ERROR, msg="remove key(s) failed", exception=e)




    def exists(self, key):
        """
        chekc a key if exists
        """
        try:
            return redis.Redis(connection_pool=self.pool).exists(key)
        except Exception as e:
            logger.message(p.ERROR, msg="failed with some uncertain errors", exception=e)




    def set_key_exp(self, key, exp):
        """
        set expiration for key

        Args:
        * [key] string key name
        * [exp] expiration time in seconds
        """
        try:
            redis.Redis(connection_pool=self.pool).expire(key, exp)
        except Exception as e:
            logger.message(p.ERROR, msg="set expiration failed", exception=e)