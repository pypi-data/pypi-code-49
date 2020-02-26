# -*- coding: utf-8 -*-

import sys
import os.path

import json

from pathlib import Path
import argparse

class PrintConfigAction(argparse.Action):

    @classmethod
    def set_callback_methods(cls, callback_methods):
        cls.callback_methods = callback_methods if callback_methods else []
    
    def __init__(self
                 , option_strings
                 , dest
                 , default=False
                 , required=False
                 , help=None):
        super().__init__(option_strings=option_strings
                         , dest=dest
                         , nargs=0
                         , const=True
                         , default=default
                         , required=required
                         , help=help)                                       

    def __call__(self, parser, namespace, values, option_string=None):
        assert self.callback_methods is not None, 'callback_method cannot be null.'
        if len(self.callback_methods) == 0:
            print('callback_methods must be given to print_conf', file = sys.stderr)
            exit(1)
        for callback_method in self.callback_methods:
            loader = PrintConfig(callback_method.__SECTION__, sys.stdout)
            callback_method(loader)
        exit(0)
            
class PrintConfig:

    def __init__(self, section, out):
        self.section = section
        self.out = out
        print(file = self.out)
        print(file = self.out)
        print('[{}]'.format(section), file = self.out)
        print(file = self.out)

    def add_attr(self, name, default=None, required=False, help=''):
        self.print_attr(name, default, required, help, str)
        
    def add_attr_boolean(self, name, default=False, required=False, help=''):
        self.print_attr(name, default, required, help, bool)

    def add_attr_int(self, name, default=0, required=False, help=''):
        self.print_attr(name, default, required, help, int)

    def add_attr_float(self, name, default=0.0, required=False, help=''):
        self.print_attr(name, default, required, help, float)

    def add_attr_dict(self, name, default={}, required=False, help=''):
        self.print_attr(name, default, required, help, dict, json_data=True)
        
    def add_attr_list(self, name, default=[], required=False, help=''):
        self.print_attr(name, default, required, help, list, json_data=True)
        
    def add_attr_path(self, name, default=None, required=False, help=''):
        self.print_attr(name, default, required, help, Path)

    def print_attr(self, name, default, required, help, typestring, json_data=False):
        if required:
            print('# REQUIRED', file = self.out)
        print('# {} ({})'.format(help, typestring), file = self.out)
        if default is not None:
            print('# {} = {}'.format(name, default if not json_data else json.dumps(default)), file = self.out)
        else:
            print('# {} (no default value)'.format(name), file = self.out)
        if required:
            if default:
                print('{} = {}'.format(name, default), file = self.out)
            else:
                print('{} = '.format(name), file = self.out)
        print('', file = self.out)
        

