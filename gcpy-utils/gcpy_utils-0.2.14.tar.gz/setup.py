# coding:utf-8
__author__ = 'qinman'
# create by qinman on 2018/4/13

from setuptools import setup, find_packages

setup(
    name='gcpy_utils',
    version='0.2.14',
    description=(
        '<公用函数的封装>'
    ),
    author='zhoukunpeng',
    author_email='zhoukunpeng504@163.com',
    packages=find_packages(),
    install_requires=['happybase', 'redis']
)
