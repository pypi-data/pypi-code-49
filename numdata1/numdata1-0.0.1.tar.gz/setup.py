import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()
	
setuptools.setup(
	name="numdata1",
	version="0.0.1",
	author="Charles Chen",
	author_email = "yc414@duke.edu",
	description="A simple package calculating valuews for a simple number",
	long_description=long_description,
	long_description_content_type = "text/markdown",
	url="",
	keywords = 'package numbers calculations',
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 2",
		"Operating System :: OS Independent"
	],
	)