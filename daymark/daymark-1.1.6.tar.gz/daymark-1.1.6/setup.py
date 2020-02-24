from setuptools import setup

setup(name = 'daymark',
	version = '1.1.6',
	licence = 'MIT',
	description = 'daymark is a helper package.',
	author = 'Samarthya Choudhary',
	author_email = 'samarthyachoudhary7@gmail.com',
	url = 'https://gitlab.com/aman.indshine/lighthouse-function-helper.git',
	setup_requires=['wheel'],
	install_requires =['requests', 'redis'],
	classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Topic :: Software Development :: Build Tools', 'License :: OSI Approved :: MIT License'])