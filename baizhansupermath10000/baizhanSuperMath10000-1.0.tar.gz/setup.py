#coding=utf-8

from distutils.core import setup

setup(
    name="baizhanSuperMath10000",#对外模块名称
    version='1.0', #版本号
    description='这是第一个对外发布的模块，测试', #描述
    author='Jack',
    author_email='Jack@163.com',
    py_modules=['baizhanSuperMath10000.demo1','baizhanSuperMath10000.demo2'] #发布的模块
)