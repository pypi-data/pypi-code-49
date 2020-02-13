import os
import sys
import glob

from setuptools import setup, find_packages

setup(
	name = "hgmd",
	version = "0.0.4",
	description = "Automatic calculation script for VASP calculation",
	author = "Jong Goo Park",
	author_email = "jgp505@gmail.com",
	#url = "",
	#downloadurl = "",
	install_requires= ["numpy>=1.9","pymatgen>=2019.3.13","matplotlib>=1.1"],
	packages = find_packages(),
	python_requires = ">=3",
	zip_safe = False,
	clssifiers = [
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',\
		],
	scripts = glob.glob(os.path.join(os.path.dirname(__file__),"argument",'*'))
	)

