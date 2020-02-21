# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: May 10, 2018
# Modifi: May 10, 2018

from siki.basics import FileUtils as futil

class KeyValue(object):
    
    def __init__(self, key, value = None):
        self._key = key
        self._value = value
        self._md5 = futil.compute_str_md5(str(value))
        
    def __str__(self):
        return str(self._key) + ' : ' + str(self._value)
        
    def set_key(self, key):
        self._key = key
        
    def set_value(self, value):
        self._value = value
        self._md5 = futil.compute_str_md5(str(value))
        
    def md5(self):
        return self._md5
        
    def key(self):
        return self._key
        
    def value(self):
        return self._value
        
    def same_entity(self, keyv):
        if type(keyv) is KeyValue:
            return self.md5() == keyv.md5()
        else:
            return False
    
    def same_key(self, keyv):
        if type(keyv) is KeyValue:
            return self._key == keyv.key()