# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: Feb 21, 2020
# LastChg: Feb 21, 2020

from siki.basics import TimeTicker as ticker
from siki.basics import Convert as convert
from siki.basics import JsonUtils as jutil
from siki.basics import Exceptions as excepts

from siki.pyredis.PyRedisPool import PyRedisPool

import sys
import base64

class RedisDataToken(object):

    """
    {'data':base64/str, 'type':str, 'timestamp':float}
    """


    def __init__(self):
        self.reset()

    def reset(self):
        self.data = None
        self.dtype = None
        self.timestamp = None
        self.token = None


    def decode(self, token: bytes):
        """
        since obtained token from redis, use this method to 
        convert the bytes into correct data type

        Args:
        * [token(bytes)] obtained bytes from redis

        Returns:
        * [token(dict)] contains data, timestamp, type infomation
        """
        # reset all
        self.reset()

        if token is not None:
            # 1, convert the bytes into dictionary
            self.token = convert.binary_to_dict(token)

            # 2. assign to attributes
            self.dtype = self.token["type"]
            self.timestamp = self.token["timestamp"]

            # 3. if bytes, process them carefully
            if self.dtype == "bytes":
                self.data = base64.b64decode(convert.string_to_binary(self.token["data"]))
            else: # normal data
                self.data = self.token["data"]

            # 4. return to caller
            self.token = {"data":self.data, "type":self.dtype, "timestamp": self.timestamp}
            return self.token

        else:
            raise excepts.NullPointerException("token cannot be a null type")

    
    def encode(self, data):
        """
        convert given data into redis token

        Args:
        * [data(any)] data can be anything, bytes, int, float or whatever

        Returns:
        * [token(bytes)] composed token consisted of data, type, timestamp
        """
        # reset
        self.reset()

        if data is None:
            raise excepts.NullPointerException("data cannot be a null type")

        # 1. create timestamp
        self.timestamp = ticker.time_since1970()

        # 2. assign bytes to self.data
        if type(data) is bytes:
            self.dtype = "bytes"
            self.data = convert.binary_to_string(base64.b64encode(data))
        else: # other types
            self.data = data

            if type(data) is int:
                self.dtype = "int"
            elif type(data) is float:
                self.dtype = "float"
            elif type(data) is str:
                self.dtype = "str"
            elif type(data) is list:
                self.dtype = "list"
            elif type(data) is dict:
                self.dtype = "dict"
            else:
                raise excepts.InvalidParamException("{} cannot be processed into string nor bytes"
                    .format(type(data)))

        # 3. composing a token dictionary type
        self.token = {"data":self.data, "type":self.dtype, "timestamp":self.timestamp}

        # return to caller
        return convert.dict_to_binary(self.token)