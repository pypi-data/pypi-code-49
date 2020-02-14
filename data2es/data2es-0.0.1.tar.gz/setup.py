#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: stosc
# Mail: stosc@sidaxin.com
# Created Time:  2020-2-8 19:17:34
#############################################

from setuptools import setup, find_packages  #这个包没有的可以pip一下
import codecs          
import data2es as pack

def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()

setup(
    name = pack.__title__,      #这里是pip项目发布的名称
    version = pack.__version__,  #版本号，数值大的会优先被pip
    keywords = (pack.__serverName__,pack.__daemonName__,"mysql","elasticsearch","import","data"),
    description = "A tool to import data from mysql into elasticsearch",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    license = "MIT Licence",

    url = "https://github.com/stosc/data2es",     #项目相关文件地址，一般是github
    author = pack.__author__,
    author_email = "stosc@sidaxin.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["pymysql","croniter","argparse","elasticsearch","pyhocon","tornado"],          #这个项目需要的第三方库
    classifiers=[        
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            '%s = pack.main:run'%(pack.__serverName__),#把业务模块打包为可系统执行的命令
            '%s = pack.maind:run'%(pack.__daemonName__),
        ]
    },
    python_requires='>=3.6',
)
