#!/usr/bin/env python

import setuptools
import sys


requirements = [
	'aiohttp >= 3.5.4, < 3.6',
]

if sys.version_info < (3, 7):
	requirements.append('async-exit-stack')


setuptools.setup(
	name='lightbringer',
	version='0.0.4',
	description='Modern, simple and robust asyncio NSQ client library',
	author='Glose',
	author_email='hello+lightbringer@glose.com',
	url='http://git.glose.com/opensource/lightbringer',
	license='MIT',
	packages=['lightbringer'],
	install_requires=requirements,
	setup_requires=[
		'pytest-runner >= 5.1, < 6',
	],
	tests_require=requirements + [
		'pytest',
		'pytest-cov',
		'pytest-asyncio',
	],
	test_suite='test',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
