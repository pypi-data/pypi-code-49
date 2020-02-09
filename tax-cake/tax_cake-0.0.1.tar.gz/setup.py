#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='tax_cake',
    version='0.0.1',
    author='gujitao',
    author_email='taojigu@163.com',
    url='https://github.com/taojigu',
    description=u'个税和年终奖计算工具',
    packages=['tax_cake'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'year_tax=tax_cake.year_salary_tax:yearSalaryTaxMain'
        ]
    }
)