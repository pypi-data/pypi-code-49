# -*- coding: utf8 -*-

from os import path

from setuptools import find_packages, setup
from crawl_wx import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='crawl_wx',
    version=__version__,
    license='PRIVATE',
    author='fatelei',
    author_email='fatelei@gmail.com',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/fatelei/crawl_wx',
    description='crawl wechat public account contents',
    packages=find_packages(where='.', exclude=['tests', 'scripts']),
    zip_safe=False,
    install_requires=[
        'uncurl',
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'crawl_wx = crawl_wx.cmd:cmd'
        ],
    }
)
