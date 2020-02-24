#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: super1207
# Mail: pengyao1210@gmail.com
# Created Time:  2020-2-24 15:25:30
#############################################


from setuptools import setup, find_packages

setup(
    name = "ggtranslate",
    version = "1.0.1",
    keywords = ("pip", "ggtranslate","google", "translate"),
    description = "translate anything use google api",
    long_description = "translate anything use google api",
    license = "MIT Licence",

    url = "http://www.super1207.top",
    author = "super1207",
    author_email = "pengyao1210@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["js2py","requests"]
)