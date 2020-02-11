from setuptools import setup

with open("README.md") as fh:
	long_description = fh.read()

setup(name='beryl_plugin',
	version='0.0.1-alpha.1',
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
