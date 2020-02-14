#!/usr/bin/env python3
# coding: utf-8


from setuptools import setup, find_packages

from coulomb_counter_cc75 import __version__


if __name__ == "__main__":
	try:
		setup(
			name="coulomb_counter_cc75",
			version=__version__,
			packages=find_packages(),

			author="Gilles HUBERT",
			author_email="gilles.hubert97@gmail.com",

			description="Python library for the coulomb counter cc75.",
			long_description=open("README.md").read(),

			install_requires=["pyserial"],

			url="https://github.com/yncreahdf-robotics/coulomb_counter_cc75_py/tree/master/coulomb_counter_cc75",

			classifiers=[
				"Programming Language :: Python",
				"Natural Language :: English",
				"Operating System :: OS Independent",
				"Programming Language :: Python :: 3.5",
			],
		)
	except KeyboardInterrupt:
		pass
	finally:
		pass
