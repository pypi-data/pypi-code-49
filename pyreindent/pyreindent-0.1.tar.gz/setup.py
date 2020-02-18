from setuptools import setup

setup(
	name='pyreindent',
	version='0.1',
	scripts=['bin/pyreindent.py'],
	packages=['pylineblocks'],
	author='Anton Bernatskiy',
	author_email='abernats@uvm.edu',
	description='Freely switch between various Python indentation styles',
	long_description='See `project homepage <https://github.com/abernatskiy/pyreindent>`_.',
	classifiers=[
	  'Development Status :: 4 - Beta',
	  'License :: OSI Approved :: MIT License',
	  'Programming Language :: Python :: 3',
	  'Topic :: Text Processing :: Filters'
	],
	url='https://github.com/abernatskiy/pyreindent',
	license='MIT',
)
