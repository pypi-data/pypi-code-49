#!/usr/bin/env python3

from functools import wraps


class Value(object):
	"""
	stores property values
	"""

	def __init__(self, name, getter=None, value=None):
		@wraps(getter)
		def _getter(object):
			# print object, self.value
			value = getter(object)
			if value:
				return value
			if hasattr(self, 'value'):
				return self.value
			return None

		self.getter = _getter
		self.value = value
	
	def setter(self, object, value):
		# print 'setter=', value
		self.value = value

	def deleter(self, object):
		self.value = None
		# print 'deleter=', self.value
		del self.value
