# coding: utf-8

from setuptools import find_packages, setup

setup(
    name='informer',
    version='0.0.1',
    author='Wang Yunkai',
    author_email='wangyunkai.zju@gmail.com',
    url='https://github.com/IamWangYunKai/informer',
    description=u'debug tool',
    packages=find_packages(),
    install_requires=[
        "opencv-python",
    ]
)