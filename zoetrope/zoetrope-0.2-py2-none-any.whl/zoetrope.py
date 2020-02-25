#!/usr/bin/env python

import argparse
import os
import types
import sys
import os
import re
import zoetrope.templates.unittest_template as unittest_template

class Module(object):
    def __init__(
        self,
        path=None,
        python_path=None,
        module=None,
        name=None,
        functions=[],
        classes=[],
        dependencies=[]
    ):
        self._path = path
        self._python_path = python_path
        self._name = name
        self._module = module
        self._functions = functions
        self._classes = classes
        self._dependencies = dependencies

    @property
    def path(self):
        return self._path

    @property
    def python_path(self):
        if not self._python_path:
            if not self._path:
                raise AttributeError('You need a path before you can have a Python Path!')
            self._python_path = self._path.replace('/', '.').replace('-', '_')
        return self._python_path

    @property
    def name(self):
        if not self._name:
            if not self._python_path:
                raise AttributeError('You need a valid path name before you can have a Module Name!')

            self._name = self._python_path.split('.')[-1]

        return self._name

    @property
    def module(self):
        if not self._module:
            self._module = __import__(module.python_path, globals(), locals(), [module.name], 0)
        return self._module

    @property
    def functions(self):
        if not self._functions:
            self.get_elements()
        return self._functions

    @functions.setter
    def functions(self, values):
        if isinstance(values, list):
            for value in values:
                if isinstance(value, types.FunctionType):
                    continue
                else:
                    raise TypeError('Module.function objects must be of type FunctionType')
            self._functions = values
        else:
            raise TypeError('Module.functions can only be set by passing a list of FunctionType objects')

    @property
    def classes(self):
        if not self._classes:
            self.get_elements()
        return self._classes

    @classes.setter
    def classes(self, values):
        if isinstance(values, list):
            for value in values:
                if isinstance(value, (type, types.ClassType)):
                    continue
                else:
                    raise TypeError('Module.class objects must be of type ClassType')
            self._classes = values
        else:
            raise TypeError('Module.functions can only be set by passing a list of ClassType objects')

    @property
    def dependencies(self):
        dependencies = []
        if not self._dependencies:
            for obj in self.module.__dict__:
                obj = self.module.__dict__.get(obj)
                if isinstance(obj, types.ModuleType):
                    dependencies.append(obj)

            self._dependencies = dependencies

        return self._dependencies

    def get_elements(self):
        functions=[]
        classes=[]
        for obj in self.module.__dict__:
            obj = self.module.__dict__.get(obj)
            if hasattr(obj, '__module__') and obj.__module__==self.python_path:
                if isinstance(obj, types.FunctionType):
                    functions.append(obj)
                elif isinstance(obj, type):
                    classes.append(obj)
                else:
                    continue

        self.classes = classes
        self.functions = functions

    def to_dict(self):
        return {
            "path": self.path,
            "python_path": self.python_path,
            "name": self.name,
            "module": self.module,
            "functions": self.functions,
            "classes": self.classes
        }


def create_test_stub(module):
    module.get_elements()
    print(unittest_template.headers(module))
    print(unittest_template.class_test(module.name, indentation=0))
    for x in module.functions:
        print(unittest_template.function_test(x, indentation=1))

    for _class in module.classes:
        print(unittest_template.class_test(_class.__name__, indentation=0))
        for x in _class.__dict__:
            x = _class.__dict__.get(x)
            if isinstance(x, types.FunctionType):
                 print(unittest_template.function_test(x, indentation=1))

    print(unittest_template.main())


def pathify(path):
    """
    Convert file path from a/b/c syntax to a.b.c syntax
    """
    return path.replace('.py', '').replace('/', '.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A tool for generating unittest stubs."
    )

    parser.add_argument(
        'paths',
        metavar='N',
        type=str,
        nargs='+',
        help='File path or paths for analysis and stub generation'
    )

    parser.add_argument(
        "--directory",
        "-d",
        type=bool,
        default=False,
        help="When true the positional arg is a directory with multiple files in it."
    )

    args = parser.parse_args()
    if args.directory:
        paths = list_files_in_dir(path)

    for path in args.paths:
        module = Module(path=pathify(path))
        create_test_stub(module)
