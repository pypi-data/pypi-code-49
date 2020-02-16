#!/usr/bin/env python3

from Argumental.NamedShort import NamedShort


class Parameter(NamedShort):
	"""
	extract PyDoc :param: details and create argparse settings
	"""

	def __init__(self,
		param=None,
		name=None,
		short=None,
		flag=False,
		choices=None,
		oneof=None,
		default=None,
		nargs=None,
		type=str,
		format=None,
		help=None,
		positional=False,
		required=False,
		metavar=None
	):
		super(Parameter, self).__init__(None)
		self.param = param or name  # str
		self.name = name or param  # str
		self.short = short  # str[1]
		self.flag = flag  # bool
		self.choices = choices  # list
		self.oneof = oneof  # list
		self.default = default  # object
		self.nargs = nargs  # [N,'?','+','*',R]
		self.type = type  # type
		self.format = format  # %Y-%m-%d %H:%M:%S
		self.help = help  # str
		self.positional = positional  # bool
		self.required = required  # bool
		self.metavar = metavar  # str
