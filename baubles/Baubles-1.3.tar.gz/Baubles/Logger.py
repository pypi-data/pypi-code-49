#!/usr/bin/env python3

import os, sys, re, inspect, logging

from functools import wraps

from Baubles.Colours import Colours
from Baubles.LogColour import ColouredLogger

for name in logging.Logger.manager.loggerDict.keys():
	logging.getLogger(name).setLevel(logging.ERROR)


#________________________________________________________________________________________
class Logger(object):
	'''
	logging decorators to log method calls with detail derived from the method they wrap
	'''
	
	levels = {
		'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'critical': logging.CRITICAL,
	}

	def __init__(self, name=None):
		if not name:
			# use the name of the calling function
			stack = inspect.stack()
			#print(stack
			name = os.path.basename(stack[1][1]).replace('.py', '')
		logging.setLoggerClass(ColouredLogger)
		self.colours = Colours(colour=True)
		self.__logger = logging.getLogger(name)
		self.__logger.setLevel(logging.DEBUG)
		return

	def getRoot(self, fn):
		'''
		to find the function behind the decorators
		'''
		while hasattr(fn, 'func_closure') and fn.func_closure:
			if len(fn.func_closure) == 0:
				break
			fn = fn.func_closure[0].cell_contents
		return fn

	def __log(self, f, args, kwargs, result, level):
		'''
		private function to log the function, request parameters and response value
		'''
		c = self.colours
		td = []

		td.append('%s%s%s(' % (c.Off, f.__name__, c.Off))

		if args:
			td.append(', '.join(map(lambda x: '%s%s%s' % (c.Green, x, c.Off), args)))

		if args and kwargs:
			td.append(', ')

		if kwargs:
			td.append(', '.join(
				map(
					lambda x: '%s%s%s=%s%s%s' % (c.Green, x, c.Off, c.Purple, kwargs[x], c.Off),
					kwargs.keys())))

		td.append('): %s%s%s' % (c.Orange, result if result else '', c.Off))

		self.__logger.log(level, ''.join(td))

		return

	def setLevel(self, level):
		self.__logger.setLevel(level)

	def __getattr__(self, name):
		'''
		get logging wrapper for the named level
		'''
		if name not in self.levels.keys():
			return

		def wrap(*_args, **_kwargs):
			if len(_args) == 0: return
			fn = _args[0]
			if not hasattr(fn, '__call__'):
				# not in a wrapper 
				level = self.levels[name]
				self.__logger.log(level, ' '.join(map(str, _args)))
				return

			fn = self.getRoot(fn)

			@wraps(fn)
			def wrapper(*args, **kwargs):
				result = fn(*args, **kwargs)
				level = self.levels[name]
				self.__log(fn, args, kwargs, result, level)
				return result

			return wrapper

		return wrap

	def handle(self, *fns, **kwargs):
		'''
		execute wrapper and swallow if exception, optional handler called on exception
		'''
		handler = kwargs.get('handler')
		level = kwargs.get('level', logging.ERROR)

		def wrap(fn):
			fn = self.getRoot(fn)

			@wraps(fn)
			def wrapper(*args, **kwargs):
				try:
					return fn(*args, **kwargs)
				except:
					result = sys.exc_info()[1]
					self.__log(fn, args, kwargs, result, level)
					if handler:
						return handler(*args, **kwargs)
					return

			return wrapper

		if len(fns):
			return wrap(fns[0])

		return wrap


#========================================================================================
logger = Logger()


@logger.warning
def handler(*args, **kwargs):
	return 'in handler (%s, %s)' % (args, kwargs)


class Test(object):
	@logger.debug
	def __init__(self):
		pass

	@logger.debug
	def __del__(self):
		pass

	@logger.info
	def run(self, a, k=None):
		return 'kk'

	@logger.handle
	def noFail(self, arg1, arg2, kwargs1=None):
		logger.info('did not fail')
		return True

	@logger.handle
	def willFail(self, arg1, arg2, kwargs1=None):
		raise Exception('failed and logged')
		return False

	@logger.handle(handler=handler)
	def doFail(self, arg1, arg2, kwargs1=None):
		raise Exception('failed and handled')
		return False


def main():
	@logger.critical
	def testCritical(arg1, arg2, kwargs1=None):
		return 'W'

	@logger.error
	def testError(arg1, arg2, kwargs1=None):
		return 'W'

	@logger.warning
	def testWarning(arg1, arg2, kwargs1=None):
		return 'X'

	@logger.info
	def testInfo(arg1, arg2, kwargs1=None):
		return 'Y'

	@logger.debug
	def testDebug(arg1, arg2, kwargs1=None):
		return 'Z'

	@logger.info
	def testLog(arg1, arg2, kwargs1=None):
		logger.info('yay')
		return 'A'

	@logger.handle
	def noFail(arg1, arg2, kwargs1=None):
		logger.info('did not fail')
		return True

	@logger.handle
	def willFail(arg1, arg2, kwargs1=None):
		raise Exception('failed and logged')
		return False

	@logger.handle(handler=handler)
	def doFail(arg1, arg2, kwargs1=None):
		raise Exception('failed and handled')
		return False

	if True:
		print(testCritical('a', 2, kwargs1=True))
		print(testError('a', 2, kwargs1=True))
		print(testWarning('a', 2, kwargs1=True))
		print(testInfo('a', 2, kwargs1=True))
		print(testDebug('a', 2, kwargs1=True))
		print(testLog('a', 2, kwargs1=True))

	if True:
		print
		print(noFail('a', 2, kwargs1=True))
		print(willFail('a', 2, kwargs1=True))
		print(doFail('a', 2, kwargs1=True))

	if True:
		print
		test = Test()
		print(test.run('aye', k='kye'))
		print(test.noFail('a', 2, kwargs1=True))
		print(test.willFail('a', 2, kwargs1=True))
		print(test.doFail('a', 2, kwargs1=True))
		del test

	if True:
		print
		logger.debug('_debug')
		logger.info('_info')
		logger.warning('_warning')
		logger.error('_error')
		logger.critical('_critical')

	return


if __name__ == '__main__': main()

