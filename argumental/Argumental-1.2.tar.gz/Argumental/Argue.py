#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

import os, sys, re, json, argparse, time, logging, inspect, traceback, atexit, argcomplete

from io import StringIO
from datetime import datetime, date
from collections import namedtuple
from functools import wraps

from Argumental.Getters import getRoot, getSpec
from Argumental.NamedShort import NamedShort
from Argumental.Argument import Argument
from Argumental.Attribute import Attribute
from Argumental.Command import Command
from Argumental.Operation import Operation
from Argumental.Parameter import Parameter
from Argumental.Returns import Returns
from Argumental.Value import Value


#________________________________________________________________________________________
class Argue(object):
	"""
	Argue provides a way to wrap a class with methods using decorators
	to automagially create an argparse version of the app that can be called from the command line.
	"""

	def __init__(self, name=None, help=None):
		"""
		create a new parser
		"""
		self.logger = logging.getLogger(Argue.__qualname__)
		self.name = name
		self.parser = argparse.ArgumentParser(name, conflict_handler='resolve')
		self.singles = set()
		self.help = help
		self.subParsers = None
		self.arguments  = dict() # key=function, value=Argument
		self.commands   = dict() # key=class,    value=Command
		self.attributes = dict() # key=method,   value=Attribute
		self.operations = dict() # key=method,   value=Operation
		self.parameters = dict() # key=method,   value=dict() key=param, value=Parameter
		self.properties = dict() # key=method,   value=Value
		self.returnss   = dict() # key=class,    value=Returns
		self.parsed = None
		return

	def __del__(self):
		del self.parsed
		del self.arguments
		del self.commands
		del self.attributes
		del self.operations
		del self.parser
		return

	def values(self):
		return {
			'arguments': self.arguments,
			'commands': self.commands
		}

	def clean(self, target=None):
		if not target:
			for value in list(self.arguments.values()) + list(self.commands.values()):
				self.clean(value)
		if type(target) in [list, dict]:
			for value in target:
				self.clean(value)
		if type(target) not in [
			NamedShort,
			Argument,
			Command,
			Attribute,
			Operation,
			Parameter,
			Returns
		]:
			return
		if hasattr(target, 'parser'):
			delattr(target, 'parser')
		if hasattr(target, 'fn'):
			delattr(target, 'fn')
		if hasattr(target, 'type'):
			if getattr(target, 'type') is None:
				delattr(target, 'type')
			else:
				setattr(target, 'type', str(getattr(target, 'type')))
		if hasattr(target, 'flag'):
			if getattr(target, 'flag') is False:
				delattr(target, 'flag')
		if hasattr(target,'required'):
			if getattr(target, 'required') is False:
				delattr(target, 'required')
		if type(target) is Command:
			for value in target.attributes.values():
				self.clean(value)
			for value in target.operations.values():
				self.clean(value)
		if type(target) is Operation:
			for value in target.parameters.values():
				self.clean(value)
			if hasattr(target, 'returns'):
				self.clean(target.returns)
		return

	def super(self, clasz, target):
		"""
		this helper function resolves the super to the real class instantiator rather than the decorator.
		replace super() with args.super()
		"""
		fn = getRoot(clasz)
		return super(fn, target)

	def addArgument(self, _argument):
		if _argument.flag:
			_action = 'store_true'
		else:
			_action = 'store'
		_args = list()

		if _argument.positional:
			if _argument.short:
				_args.append('%s' % _argument.short)
			else:
				_args.append('%s' % _argument.name)
			_argument.required = None
		else:
			if _argument.short:
				_args.append('-%s' % _argument.short)
			_args.append('--%s' % _argument.name)

		_kwargs = dict(
			action=_action,
		)

		for key in ['help', 'required', 'choices', 'default', 'nargs', 'metavar']:
			if not hasattr(_argument, key):
				continue
			value = getattr(_argument, key)
			if value:
				_kwargs[key] = value

		_type = None
		if hasattr(_argument, 'type'):
			if _argument.type == datetime:
				_format = '%Y-%m-%d %H:%M:%S'
				if hasattr(_argument, 'format') and _argument.format:
					_format = _argument.format
				_type = _format.replace('%', '%%')
				_kwargs['type'] = lambda x: datetime.strptime(x, _format)
			elif _argument.type == date:
				_format = '%Y-%m-%d'
				if hasattr(_argument, 'format') and _argument.format:
					_format = _argument.format
				_type = _format.replace('%', '%%')
				_kwargs['type'] = lambda x: datetime.strptime(x, _format).date()
			elif _argument.type == time:
				_format = '%H:%M:%S'
				if hasattr(_argument, 'format') and _argument.format:
					_format = _argument.format
				_type = _format.replace('%', '%%')
				_kwargs['type'] = lambda x: datetime.strptime(x, _format).time()
			else:
				if _argument.type:
					_type = _argument.type.__qualname__
				_kwargs['type'] = _argument.type

		if _argument.flag:
			if 'type' in _kwargs.keys():
				del _kwargs['type']

		if _argument.default:  # and _argument.default != '==SUPPRESS==':
			if 'help' in _kwargs.keys():
				_kwargs['help'] = '%s, default=%s' % (_kwargs['help'], _argument.default)
			else:
				_kwargs['help'] = 'default=%s' % _argument.default

		if _type and _type != 'str':
			if 'help' in _kwargs.keys():
				_kwargs['help'] = '%s, type=%s' % (_kwargs['help'], _type)
			else:
				_kwargs['help'] = 'default=%s' % _type

		return _args, _kwargs

	def addGlobal(self, _argument):
		"""
		private method to add a global argument
		"""
		_args, _kwargs = self.addArgument(_argument)
		self.arguments[_argument.fn.__qualname__] = _argument

		argument = self.parser.add_argument(*_args, **_kwargs)
		return

	def addCommand(self, _command):
		"""
		private method to add a command
		"""
		name = _command.name

		parent = _command.fn.__bases__[0]
		if parent is object:
			parent = None
		# print _command.fn, parent

		if _command.single:
			if parent in self.singles:
				self.singles.add(_command.fn)
				_command.parser = self.parser
			elif len(self.singles) == 0:
				if len(self.commands) == 0:
					self.singles.add(_command.fn)
					_command.parser = self.parser
				else:
					sys.stderr.write('non single already defined, ignoring single %s\n' % name)
					return
			else:
				sys.stderr.write('single already defined, ignoring single %s\n' % name)
				return
		else:
			if len(self.singles) > 0:
				sys.stderr.write('single already defined, ignoring non single %s\n' % name)
				return
			if not self.subParsers:
				self.subParsers = self.parser.add_subparsers(help='commands')
			_command.parser = self.subParsers.add_parser(name, help=_command.help)

		_command.parser.set_defaults(command=name, clasz=_command.fn)
		self.commands[name] = _command

		if _command.parser._subparsers:
			operations = self.subParsers
		else:
			operations = _command.parser.add_subparsers(help='operations')

		if len(self.singles) > 0:
			self.subParsers = operations

		properties = list()
		for name, property in inspect.getmembers(_command.fn, predicate=inspect.isdatadescriptor):
			#print(name, property)
			if hasattr(property, 'fget') and property.fget not in properties:
				self.addMethod(_command, operations, property.fget)
				properties.append(property.fget)

		for name, method in inspect.getmembers(_command.fn, predicate=inspect.isfunction) + inspect.getmembers(_command.fn, predicate=inspect.ismethod):
			#print(name, method)
			m = getRoot(method)
			self.addMethod(_command, operations, m)
		return

	def addMethod(self, _command, operations, method):
		"""
		private method to add an operation or class method
		"""
		fn = method #.__func__
		#print(fn)
		fn, _args, _kwargs = getSpec(fn)
		#print(fn,_args,_kwargs)
		
		if fn.__qualname__ in self.attributes.keys():
			#print(fn.__qualname__, self.attributes.keys())
			_attribute = self.attributes[fn.__qualname__]
			if _attribute.oneof:
				self.addOneOf(_command.parser, _attribute)
				return

			_args, _kwargs = self.addArgument(_attribute)
			_command.parser.add_argument(*_args, **_kwargs)
			_command.attributes[_attribute.name] = _attribute
			return

		if fn.__qualname__ in self.operations.keys():
			_operation = self.operations[fn.__qualname__]
			#print(fn,_operation)
			
			if fn in self.returnss.keys():
				_operation.returns = self.returnss[fn]
			if hasattr(_operation, 'returns'):
				_operation.help += ', returns: %s %s' % (_operation.returns.type, _operation.returns.help or '')

			try:
				operation = operations.add_parser(_operation.short or _operation.name, help=_operation.help)
			except:
				sys.stderr.write('%s\n' % sys.exc_info()[0])
				return

			operation.set_defaults(operation=_operation.short or _operation.name, method=fn)

			if fn.__qualname__ in self.parameters.keys():
				for n, p in self.parameters[fn.__qualname__].items():
					_operation.parameters[n] = p
					#print(n,p)

			for a in _args:
				if a in _operation.parameters.keys():
					p = _operation.parameters[a]
					p.positional = True
					__args, __kwargs = self.addArgument(p)
					operation.add_argument(*__args, **__kwargs)

			for a in _kwargs.keys():
				if a in _operation.parameters.keys():
					p = _operation.parameters[a]
					if p.oneof:
						self.addOneOf(operation, p)
						continue
					__args, __kwargs = self.addArgument(p)
					operation.add_argument(*__args, **__kwargs)

			_command.operations[_operation.name] = _operation

		return

	def addOneOf(self, parent, parameter):
		r = False
		if hasattr(parameter, 'required'):
			r = parameter.required
		g = parent.add_mutually_exclusive_group(
			required=r
		)
		kwargs = dict()

		if parameter.flag:
			kwargs['action'] = 'store_true'
		else:
			kwargs['action'] = 'store'

		if not parameter.flag:
			kwargs['type'] = parameter.type

		oneof = parameter.oneof
		if type(oneof) == list:
			oneof = dict.fromkeys(oneof)

		for o in sorted(oneof.keys()):
			kwargs['help'] = oneof[o] or parameter.help
			args = list()
			if parameter.short:
				args.append('-%s' % o[0])
			args.append('--%s' % o)
			if parameter.default == o:
				kwargs['help'] += ', default=%s' % o

			g.add_argument(*args, **kwargs)

		if parameter.default:
			parent.set_defaults(default=parameter.default)

		return

	def getReturn(self, fn):
		"""
		private method to return the results method
		"""
		if self.parsed:
			fn, args, kwargs = getSpec(fn)
			if fn.__qualname__ in self.attributes.keys():
				attribute = self.attributes[fn.__qualname__]
			if fn.__qualname__ in self.arguments.keys():
				attribute = self.arguments[fn.__qualname__]
			if hasattr(attribute, 'oneof') and attribute.oneof:
				for o in attribute.oneof:
					v = getattr(self.parsed, o)
					if v:
						if attribute.flag:
							return o
						return v
				return None
			if hasattr(self.parsed, attribute.name):
				return getattr(self.parsed, attribute.name)
		return None

	def report(self, fn, args, kwargs):
		"""
		private method to log the method calls
		"""
		return '%s(args="%s", kwargs="%s")' % (
			fn.__qualname__,
			','.join(args[1:]),
			','.join(
				map(
					lambda x: '%s=%s' % (
						x, kwargs.get(x)
					),
					kwargs.keys()
				)
			)
		)

	def argument(self, *fargs, **fkwargs):
		"""
		decorator function to define a global argument
		usage: @args.argument(<Argument>...)
		where the class Argument defines the parameters to the decorator call
		"""
		def _wrapit(fn):
			fn = getRoot(fn)
			_argument = Argument(fn, kwargs=fkwargs)
			self.arguments[fn.__qualname__] = _argument

			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return self.getReturn(fn) or fn(*args, **kwargs)
			return _wrapper

		if len(fargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = fargs[0]
			return _wrapit(fn)

	def command(self, *cargs, **ckwargs):
		"""
		decorator function to define a class command or root level option
		usage: @args.command(<Command>...)
		where the class Command defines the parameters to the decorator call
		"""

		# todo, store and review children before building args

		def _wrapit(fn):
			fn = getRoot(fn)
			self.addCommand(Command(fn, ckwargs))

			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return fn(*args, **kwargs)
			return _wrapper

		if len(cargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = cargs[0]
			return _wrapit(fn)

	def property(self, *fargs, **fkwargs):
		"""
		decorator function to define a class attribute property
		usage: @args.property(<Attribute>...)
		where the class Attribute defines the parameters to the decorator call
		"""
		def _wrapit(fn):
			fn = getRoot(fn)
			_attribute = Attribute(fn, kwargs=fkwargs)
			self.attributes[fn.__qualname__] = _attribute

			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return self.getReturn(fn) or fn(*args, **kwargs)
			value = Value(fn.__qualname__,
				getter = _wrapper,
				value = _attribute.default
			)
			p = property(
				value.getter,
				value.setter,
				value.deleter
			)
			self.properties[fn] = p
			return p
			# return property(_wrapper)

		if len(fargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = fargs[0]
			return _wrapit(fn)

	def attribute(self, *fargs, **fkwargs):
		"""
		decorator function to define a class attribute argument
		usage: @args.attribute(<Attribute>...)
		where the class Attribute defines the parameters to the decorator call
		"""

		def _wrapit(fn):
			fn = getRoot(fn)
			_attribute = Attribute(fn, kwargs=fkwargs)
			self.attributes[fn.__qualname__] = _attribute

			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return self.getReturn(fn) or fn(*args, **kwargs)
			return _wrapper

		if len(fargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = fargs[0]
			return _wrapit(fn)

	def operation(self, *oargs, **okwargs):
		"""
		decorator function to define a the second level class method operation inside the class command
		usage: @args.operation(<Operation>...)
		where the class Operation defines the parameters to the decorator call
		"""

		def _wrapit(fn):
			fn = getRoot(fn)
			#print(fn.__qualname__)
			
			self.operations[fn.__qualname__] = Operation(fn, okwargs)
			
			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return fn(*args, **kwargs)
			return _wrapper

		if len(oargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = oargs[0]
			return _wrapit(fn)

	def parameter(self, *oargs, **okwargs):
		"""
		decorator function to define a the parameters for a class operation
		usage: @args.parameter(<Parameter>...)
		"""
		def _add(fn, p):
			fn = getRoot(fn)
			if fn.__qualname__ not in self.parameters.keys():
				self.parameters[fn.__qualname__] = dict()
			self.parameters[fn.__qualname__][p.param] = p

		def _wrapit(fn):
			fn = getRoot(fn)
			_add(fn, Parameter(**okwargs))

			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return fn(*args, **kwargs)
			return _wrapper

		if len(oargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = oargs[0]
			return _wrapit(fn)

	def returns(self, *oargs, **okwargs):
		"""
		decorator function to define a the returns from a class operation
		usage: @args.parameter(<Parameter>...)
		"""
		def _wrapit(fn):
			fn = getRoot(fn)
			self.returnss[fn] = Returns(**okwargs)

			@wraps(fn)
			def _wrapper(*args, **kwargs):
				# self.logger.info(self.report(fn,args,kwargs))
				return fn(*args, **kwargs)
			return _wrapper

		if len(oargs) == 0:
			def _actualWrapper(fn):
				return _wrapit(fn)
			return _actualWrapper
		else:
			fn = oargs[0]
			return _wrapit(fn)

	def parse(self, args=None):
		"""
		Parse the command line arguments into the args variable
		usage: args.parse(sys.argv[1:])
		or:    args.parse('-f mycommand mymethod p1 p2'.split(' '))
		"""

		if not self.parsed:
			argcomplete.autocomplete(self.parser)

			if self.subParsers:
				argsParser = self.subParsers.add_parser('args', help='print the values for the args')
				argsParser.set_defaults(command='args')

			# add the global arguments
			for key in self.arguments.keys():
				_argument = self.arguments[key]
				if _argument.oneof:
					self.addOneOf(self.parser, _argument)
					continue
				self.addGlobal(_argument)

			if args:
				self.parsed = self.parser.parse_args(args)
			else:
				self.parsed = self.parser.parse_args()

		return self.parsed

	def getValue(self, params, name):
		if hasattr(params[name], 'oneof') and params[name].oneof:
			for o in params[name].oneof:
				v = getattr(self.parsed, o)
				if v:
					if params[name].flag:
						return o
					return v
			return None
		v = getattr(self.parsed, params[name].name)
		if type(v) is property:
			v = v.fget(self.parsed)
		return v

	def execute(self):
		"""
		Reslove the class by mycommand
		Resolve the class.method by myoperation
		Map paramters to the method
		Resolve globals
		then execute the class.method and return results
		usage:
		if __name__ == '__main__':
			print args.execute()
		"""
		self.parse()

		if getattr(self.parsed, 'command', None) == 'args':
			self.clean()
			return self.values()

		if hasattr(self.parsed, 'clasz'):
			command = self.parsed.clasz()

			if hasattr(self.parsed, 'method'):
				operation = getattr(command, self.parsed.method.__name__)

				_funct, _args, _kwargs = getSpec(self.parsed.method)
				params = self.commands[self.parsed.command].operations[self.parsed.operation].parameters

				__args = list()
				__kwargs = dict()

				for arg in _args:
					__args.append(self.getValue(params, arg))

				for key, value in _kwargs.items():
					__kwargs[key] = self.getValue(params, key) or value

				# if hasattr(command,'__del__'): atexit.register(command.__del__)

				return operation(*__args, **__kwargs)

				if hasattr(command, '__del__'): command.__del__()

			del self.parsed

		return


def main():
	"""
	is this the room for an arguement ?
	"""

	# the argument decorator
	args = Argue()

	# create a root level argparse argument.
	@args.argument(short='v', flag=True)
	def verbose():
		"""
		detailed output mode
		"""
		return False

	# create a subparser based on the class
	@args.command(name="class")
	class MyClass(object):
		"""
		My Class
		"""

		# add an argparse value as a property, override class attributes
		@args.property(
			short='v',
			default='abc123',
			help='with built in setter and deleter'
		)
		def value(self): return

		# declare the method as a sub parser with method parameters
		@args.operation(
			name='method'
		)
		@args.parameter(
			param='myParameter',
			short='p',
			name='parameter',
			required=True,
			help='My Parameter'
		)
		@args.returns(
			type=dict,
			help='test values'
		)
		def myOperation(self, myParameter=None):
			"""
			My Operation
			"""
			return dict(
				myParameter=myParameter,
				value=self.value
			)

	sys.stderr.write('verbose=%s\n' % verbose())

	# stand alone object test
	mc = MyClass()
	if verbose(): print('before=%s' % mc.value)
	assert('abc123' == mc.value)
	mc.value = '321cba'
	if verbose(): print('after=%s' % mc.value)
	assert('321cba' == mc.value)

	# get the args tree in colour
	if len(sys.argv) == 1:
		args.parse('args'.split())
		j = args.execute()
		print(j)

	# process other requests
	else:
		# parse the args
		args.parse(sys.argv[1:])
		# could just do this below
		result = args.execute()
		if result:
			print(json.dumps(result, indent=4))

if __name__ == '__main__': main()
