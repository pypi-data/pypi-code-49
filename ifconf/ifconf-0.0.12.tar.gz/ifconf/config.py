# -*- coding: utf-8 -*-

import sys
import os
import os.path

import json

from pathlib import Path

import argparse
import configparser

class Config:

    def __init__(self, argparser = None):
        self.argparser = argparser if argparser is not None else argparse.ArgumentParser()
        self.parser = configparser.ConfigParser()
        self.err = []
        
    def parse(self, config_path = None):
        self.args = self.argparser.parse_args()
        self.config_path = []
        
        if hasattr(self.args, 'config') and self.args.config:
            for p in self.args.config.split(os.pathsep):
                self.config_path.append(p)

        if hasattr(self.args, 'current_dir') and self.args.current_dir:
            if self.args.current_dir != '.':
                os.chdir(self.args.current_dir)

        if config_path:
            if type(config_path) != str and hasattr(config_path, '__iter__'):
                for p in config_path:
                    self.config_path.append(p)
            else:
                self.config_path.append(config_path)
                

        for p in reversed(self.config_path):
            if os.path.exists(p):
                try:
                    with open(p, "r") as f:
                        self.parser.read_file(f)
                except Exception as e:
                    self.err.append('設定ファイル[{}]の読み込みに失敗しました。エラー：{}'.format(p, e))
            else:
                self.err.append('設定ファイル[{}]が見つかりません。'.format(p))

    def get_attr(self, section, option, default='', required=False):
        if required or self.parser.has_option(section, option):
            return self.parser.get(section, option)
        else:
            return default

    def get_attr_boolean(self, section, option, default=False, required=False):
        if required or self.parser.has_option(section, option):
            return self.parser.getboolean(section, option)
        else:
            return default
        
    def get_attr_int(self, section, option, default=0, required=False):
        if required or self.parser.has_option(section, option):
            return self.parser.getint(section, option)
        else:
            return default

    def get_attr_float(self, section, option, default=0.0, required=False):
        if required or self.parser.has_option(section, option):
            return self.parser.getfloat(section, option)
        else:
            return default

    def get_attr_dict(self, section, option, default={}, required=False):
        return self.get_attr_json(section, option, default, required)
        
    def get_attr_list(self, section, option, default=[], required=False):
        return self.get_attr_json(section, option, default, required)
        
    def get_attr_json(self, section, option, default, required):
            if required or self.parser.has_option(section, option):
                value_string = self.parser.get(section, option)
                try:
                    return json.loads(value_string)
                except Exception as e:
                    raise ValueError('JSONデータのフォーマットにエラーがあります。[{}][{}][{}]'.format(section, option, value_string), e)
            else:
                return default

    def get_attr_path(self, section, option, default, required):
        if required or self.parser.has_option(section, option):
            return Path(self.parser.get(section, option))
        else:
            return default if type(default) == Path else Path(default)
        
