"""
This module adds overloading in python

Usage:

from pyover import overload, This

class Foo:

    @overload(This, int) # We need to add 'This' to overload method (class or instance)
    def bar(self, x):
        print(x**2)
    
    @bar.overload(This, str)
    def bar(self, x):
        print(x + x)
    
@overload(int, int)
def spam(x, y):
    print(x - y)

@spam.overload(str, int)
def spam(x, y):
    print(x + " - %i" % y)

obj = Foo()
obj.bar(3) # 9
obj.bar('egg') # eggegg

spam(3, 2) # 1
spam('3', 2) # 3 - 2 
"""

import types

class This:
    """
    In instance or class methods we need to add type of 'self' or 'cls'

    """
    pass

class TODOError(Exception):
    """
    This feature is not realised yet

    """
    pass

def overload(*args):
    """
    Overloads a function. Remember that to overload class or instance method,
    you need to add 'This' as first argument

    """
    def decor(fn):
        over = overloading(fn, *args)
        over.overload(fn, *args)
        return over
    return decor

class overloading:
    """
    Overloaded functions actually are object. Where you
    trying to call it, it's checking arguments, and calling requred function,
    or raising ValueError if the function is not found
    
    """

    def __init__(self, func, *args):
        if type(func) is not types.FunctionType:
            raise ValueError(
                "cannot overload %s, function or method requred" % type(func).__name__
            )
        self.name = func.__code__.co_name
        self.functions = {} # Tuple-of-types: function
        if args:
            self.is_method = args[0] is This
        self._overload(func, *args)

    def _check_args(self, func, args):
        if not hasattr(func, "__code__"):
            raise ValueError("cannot overload non-python function")
        elif func.__code__.co_argcount != len(args):
            raise ValueError(
                "too many/not enought arguments to overload this function" + \
                ("(argc = %i, args = "+str(args)) % func.__code__.co_argcount
            )
        elif not all([type(arg) is type for arg in args]):
            raise ValueError("arguments for overload must be types")
    
    def __call__(self, *args, **kwargs):
        """
        Check args, choose requred function, call it and return result

        """
        if self.is_method:
            args = (This(), ) + args
        if kwargs:
            raise TODOError("keyword args are not support yet")
        elif not tuple([type(arg) for arg in args]) in self.functions.keys():
            raise ValueError(
                "no definition found for function %s" % self.name + str(
                    tuple([type(arg) for arg in args])
                )
            )
        else:
            func = self.functions[tuple([type(arg) for arg in args])]
            return func(*args)
    
    def overload(self, *args):
        """
        Overloads other function with same name. Remember that to overload class or instance method,
        you need to add 'This' as first argument

        """
        def decor(fn):
            return self._overload(fn, *args)
        return decor

    def _overload(self, func, *args):
        self._check_args(func, args)
        self.functions[args] = func
        return self