# -*- coding: utf-8 -*-
#!/usr/bin/env python

import ConfigParser
class Config:
    def __init__(self, configPath = '/etc/.bcs/config.ini'):
        self.config = None
        f = open(configPath, 'r')
        self.config = ConfigParser.RawConfigParser(allow_no_value = True)
        self.config.readfp(f)
            
        f.close()

    def Get(self, section, option):
        return self.config.get(section, option)

    def GetInt(self, section, option):
        return self.config.getint(section, option)

    def GetFloat(self, section, option):
        return self.config.getfloat(section, option)

    def GetBoolean(self, section, option):
        return self.config.getboolean(section, option)

    def TryGet(self, section, option, defaultValue = ''):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        return defaultValue 

    def TryGetInt(self, section, option, defaultValue = None):
        if self.config.has_option(section, option):
            return self.config.getint(section, option)
        return defaultValue
    
    def TryGetFloat(self, section, option, defaultValue = None):
        if self.config.has_option(section, option):
            return self.config.getfloat(section, option)
        return defaultValue
       
    def TryGetBoolean(self, section, option, defaultValue = None):
        if self.config.has_option(section, option):
            return self.config.getboolean(section, option)
        return defaultValue

    def GetAllSections(self):
        return self.config.sections()