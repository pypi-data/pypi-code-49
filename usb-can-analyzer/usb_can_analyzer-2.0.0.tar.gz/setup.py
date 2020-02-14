#!/usr/bin/env python3
# coding: utf-8


from setuptools import setup, find_packages

from usb_can_analyzer import __version__


if __name__ == "__main__":
	try:
		setup(
			name="usb_can_analyzer",
			version=__version__,
			packages=find_packages(),

			author1="Jean-Florian TASSART",
			author1_email="jean-florian.tassart@isen.yncrea.fr",
			author2="Gilles HUBERT",
			author2_email="gilles.hubert97@gmail.com",

			description="Python library for the usb can analyzer.",
			long_description=open("README.md").read(),

			install_requires=["pyserial"],

			url="https://github.com/yncreahdf-robotics/usb_can_analyzer_py/tree/master/usb_can_analyzer",

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
