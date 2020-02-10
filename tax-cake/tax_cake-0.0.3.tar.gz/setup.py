#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='tax_cake',
    version='0.0.3',
    author='gujitao',
    author_email='taojigu@163.com',
    url='https://github.com/taojigu',
    description=u'个税和年终奖计算工具',
    packages= find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'year_tax=tax_cake.__init_:yearSalaryTaxMain'
        ]
    }
)