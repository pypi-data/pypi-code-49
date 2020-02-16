import setuptools

from setuptools import setup

with open("README.md", "r") as fh:
	lg = fh.read()
	
setup(
	name="instantmailer",
	author="mischievousdev",
	author_email="miscdev.py@gmail.com",
	version="1.0.2",
	url="https://github.com/Pythonastics/instant-mailer",
	long_description=lg,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	license="MIT",
	keywords='gmail email wrapper'
)