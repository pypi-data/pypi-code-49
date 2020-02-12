from setuptools import setup
from beryl_plugin import __version__ as beryl_ph_version

with open("README.md") as fh:
	long_description = fh.read()

setup(name='beryl_plugin',
	version=beryl_ph_version,
	description='A helper library for creating plugins for the Beryl Timing System.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='http://github.com/zPaw/beryl_plugin',
	author='Brenek Harrison',
	author_email='brenekharrison@gmail.com',
	license='MIT',
	packages=['beryl_plugin'],
	zip_safe=False,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6")

# Commands to deploy
# Clean step: (linux) rm -rf dist;  (Windows CMD) rmdir /s /q dist;  (Windows Powershell)  rm dist -r -force
# Build step: python setup.py sdist bdist_wheel
# Release step: python -m twine upload dist/*
