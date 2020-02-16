#!/usr/bin/env python3

from Argumental.NamedShort import NamedShort


class Argument(NamedShort):
	"""
	used for global level argument
	examples:
	@args.argument(
		flag=False,        # flag on/off arg or arg=value
		required=False,    # optional argument
		choices=['a','b'], # options list
		oneof=['a','b'],   # exclusive choice
		default=None,      # default value
		nargs='*',         # plurality
		type=str,          # define argument type
		format=None        # %Y-%m-%d %H:%M:%S
		positional=False   # flag on/off for positional arg
		metavar=None       # the meta name to use
	)
	"""
	
	def __init__(self, fn, kwargs=None):
		super(Argument, self).__init__(fn, kwargs)
		self.flag       = kwargs.get('flag')       or False  # bool
		self.required   = kwargs.get('required')   or False  # bool
		self.choices    = kwargs.get('choices')    or None   # list
		self.oneof      = kwargs.get('oneof')      or None   # list
		self.default    = kwargs.get('default')    or None   # object
		self.nargs      = kwargs.get('nargs')      or None   # [N,'?','+','*',R]
		self.type       = kwargs.get('type')       or None   # type
		self.format     = kwargs.get('format')     or None   # %Y-%m-%d %H:%M:%S
		self.positional = kwargs.get('positional') or False  # bool
		self.metavar    = kwargs.get('metavar')    or None   # str

