# !/usr/bin/env python
# -*- coding:utf-8 -*-
# !@Time   : 2020/2/23 7:04
# !@Author : Lu Chenjun
# !@File   : setup.py
import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='say_hello_pkg',
	version='0.1.0',
	author='james Lu',
	auther_email='birdfly8888@gmail.com',
	description='an example for teaching how to publish a Python package',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/pypa/sampleproject',
	packages=setuptools.find_packages(),
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
)
