#!/usr/bin/env python3

from Argumental.Argument import Argument


class Attribute(Argument):
	"""
	used for class attributes
	
	examples:
	@args.attribute(
		...
	)
	"""
	def __init__(self, fn, kwargs=None):
		super(Attribute, self).__init__(fn, kwargs)

