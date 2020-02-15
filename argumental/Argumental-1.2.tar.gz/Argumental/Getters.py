#!/usr/bin/env python3

import inspect


def getRoot(fn):
	"""
	dig down the closure stack to find the root function
	"""
	# print('fn=', fn, ', name=', fn.__name)
	while hasattr(fn, 'func_closure') and fn.func_closure:
		# print('fn.func_closure=', fn.func_closure)
		if len(fn.func_closure) == 0:
			break
		fn = fn.func_closure[0].cell_contents
	return fn
	
	
def getSpec(fn):
	"""
	get functional specification
	"""
	signature = inspect.signature(fn)
	#print(signature)
	#print(signature.parameters)
	
	_args = list()
	_kwargs = dict()
	
	for name, parameter in signature.parameters.items():
		#print(name,parameter)
		if '=' in str(parameter):
			_kwargs[parameter.name] = parameter.default
		else:
			if name != 'self':
				_args.append(name)
	
	return fn, _args, _kwargs

if __name__ == '__main__':
	def method(a,b=2):
		return
	print(getSpec(method))
