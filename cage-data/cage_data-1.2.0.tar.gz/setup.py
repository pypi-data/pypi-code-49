#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Xuan Ma
# Mail: xuan.ma1@northwestern.edu
#############################################

from setuptools import setup, find_packages

setup(
    name = "cage_data",
    version = "1.2.0",
    keywords = ("cage", "limbLab","data loading"),
    description = "Loading cage_data structure",
    long_description = "Python codes for loading cage data structure",
    license = "MIT Licence",

    url = "https://github.com/xuanma/cage_data",    
    author = "Xuan Ma",
    author_email = "xuan.ma1@northwestern.edu",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["scipy", "h5py"] 
)