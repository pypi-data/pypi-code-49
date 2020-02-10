import codecs
import os
import sys
try:
    from setuptools import setup
except:
    from distutils.core import setup

NAME = "HTMLTestRunner_Python3"
PACKAGES = ['HTMLTestRunner']
DESCRIPTION = "suite original HTMLTestRunner to python3"
LONG_DESCRIPTION = "the original package did not support python3, this one just fixed a few crash, the code based on tungwaiyip's code"
KEYWORDS = "HTMLTestRunner"
AUTHOR = "tungwaiyip"
AUTHOR_EMAIL = "wy@tungwaiyip.info"
URL = "http://tungwaiyip.info/"
VERSION = "0.8.0"
LICENSE = "MIT"
setup(
    name =NAME,version = VERSION,
    description = DESCRIPTION,long_description =LONG_DESCRIPTION,
    classifiers =[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords =KEYWORDS,author = AUTHOR,
    author_email = AUTHOR_EMAIL,url = URL,
    packages = PACKAGES,include_package_data=True,zip_safe=True,

)
