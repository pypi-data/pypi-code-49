# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup
   Description :
   Author :       zhangfujun
   date：          2020/2/12
-------------------------------------------------
   Change Activity:
                   2020/2/12:
-------------------------------------------------
"""
__author__ = 'zhangfujun'


from distutils.core import setup
import os

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(name='dubbofortelnet',
      version='1.0',
      description='test dubbo use telnet',
      author='fujun.zhang',
      author_email='yirandexin@163.com',
      long_description=read_file('README.txt'),

      url='http://github.com'
      )