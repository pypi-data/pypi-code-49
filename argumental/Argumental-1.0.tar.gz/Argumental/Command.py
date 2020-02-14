#!/usr/bin/env python3

from Argumental.NamedShort import NamedShort


class Command(NamedShort):
	"""
	stores a class command base item, used as a decorator parameter options list for the @args.command
	examples:
	@args.command(
		single=True,     # if True skip class choice as first
		name="myclass",  # use myclass instead of __class__.__name__
		short="c"        # use c instead
	)
	"""
	def __init__(self, fn, kwargs=None):
		super(Command, self).__init__(fn, kwargs)
		# single : bool
		self.single = kwargs.get('single') or False
		self.parent = None  # is the first instance for inheritance checks
		self.attributes = dict()
		self.operations = dict()
		self.parser = None

