#!/usr/bin/env python3

import re,json

from Argumental.Getters import getSpec
from Argumental.NamedShort import NamedShort
from Argumental.Parameter import Parameter


class Operation(NamedShort):
	"""
	stores the operation details for a class method
	examples:
	@args.operation(
		name="mymethod",  # use mymethod instead of __func__.__name__
		short="m"         # use m instead
	)

	method parameters will be processed using PyDoc notation
	"""

	def __init__(self, fn, kwargs=None):
		super(Operation, self).__init__(fn, kwargs)
		self.parameters = dict()
		# process help
		self.parameters = {}
		funct, _args, _kwargs = getSpec(fn)
		for a in _args:
			self.parameters[a] = Parameter(a)
		for a in _kwargs.keys():
			self.parameters[a] = Parameter(a)

		if '@args.parameter' in self.help:
			self.propHelp()
		else:
			self.docHelp()
		self.parser = None
		return

	def __str__(self):
		return json.dumps(dict(
			name=self.name,
			fn=self.fn.__name__,
		))
		
	def propHelp(self):
		string = self.help.replace('\n', '')
		while '  ' in string:
			string = string.replace('  ', ' ')
		lines = re.split('@args.', string)
		lines = map(lambda x: x.lstrip().rstrip(), lines)
		if '@' not in lines[0]:
			self.help = lines.pop(0)
		# print help
		lines = map(lambda x: x[0].upper() + x[1:], lines)
		# print '\n'.join(lines)
		objects = map(lambda x: eval(x), lines)
		for _object in objects:
			if isinstance(_object, Parameter):
				self.parameters[_object.param] = _object
		return

	def docHelp(self):
		patterns = dict()
		for name in ['param', 'type', 'format', 'short', 'name', 'flag', 'choices', 'oneof', 'default', 'required', 'nargs', 'metavar']:
			patterns[name] = re.compile('^:%s\s*(\S+|)\s*:\s*(\S.*)$ ' % name)
		for name in ['return', 'rtype']:
			patterns[name] = re.compile('^:%s\s*:\s*(\S.*)$ ' % name)
		lines = []
		for line in self.help.split('\n'):
			lean = line.lstrip(' ')
			if len(lean.strip()) == 0:
				continue
			if lean.startswith('#'):
				continue
			matched = False
			_param = None
			for name, pattern in patterns.items():
				m = pattern.match(lean)
				if m:
					matched = True
					param = m.group(1)
					if len(param) == 0:
						param = _param
					else:
						_param = param
					if len(m.groups()) == 1:
						continue
					value = m.group(2)
					if name == 'param':
						self.parameters[param].help = value
					for n in ['help', 'format', 'short', 'name', 'default', 'nargs', 'metavar']:
						if name == n:
							setattr(self.parameters[param], n, value)
					for n in ['type', 'flag', 'choices', 'oneof', 'required']:
						if name == n:
							setattr(self.parameters[param], n, eval(value))
					break
			if matched:
				continue
			if lean.startswith(':Example'):
				break
			lines.append(line)
		self.help = '\n'.join(lines)
		return
