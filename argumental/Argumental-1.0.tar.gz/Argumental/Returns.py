#!/usr/bin/env python3


class Returns(object):
	"""
	defines the return settings for a method
	"""
	def __init__(self, help=None, type=str):
		self.help = help
		self.type = type

