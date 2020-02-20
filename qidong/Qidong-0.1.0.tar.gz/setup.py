#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Liuqidong
# Mail: dong_liuqi@163.com
# Created Time:  2020-2-20
#############################################


from setuptools import setup, find_packages

setup(
    name = "Qidong",
    version = "0.1.0",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "Qidong's study",
    long_description = "Qidong study how to publish a python package on pypi",
    license = "MIT Licence",

    author = "Qidong",
    author_email = "dong_liuqi@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
