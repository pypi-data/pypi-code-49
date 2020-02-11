# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['intflags']
setup_kwargs = {
    'name': 'intflags',
    'version': '1.1.0',
    'description': 'The simplest way to create bit-flags',
    'long_description': '# intflags\n\nSimplest way to create bit-flags.\n\n```console\n$ pip install intflags\n```\n\n## Usage\n\nCreate any number of intflags by using `intflags.get()`. You can create a union of any amount using the pipe (`|`) operator.\n\n```python\n>>> import intflags\n\n>>> a, b, c = intflags.get(3)\n>>> bin(a | b | c)\n\'0b111\'\n\n>>> flags = a | b\n>>> a in flags\nTrue\n>>> c in flags\nFalse\n```\n\nFlags can be subtracted.\n\n```python\n# ...\n>>> new_flags = flags - b\n>>> b in new_flags\nFalse\n>>> new_flags == a\nTrue\n```\n\nYou could use classes as a pseudo-namespace.\n\n```python\n>>> class RegexFlags:\n...     I, L, M, S, U, X = intflags.get(6)\n```\n\nFlags share an internal "namespace" ID to prevent accidental conflicts between sets. This allows multiple sets of flags to exist within the same class or module, without risk of accidentally creating a union between them.\n\n```python\n>>> x = intflags.get(1)\n>>> y = intflags.get(1)\n>>> x | y\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  ...\nValueError: Flags must share a namespace to create a union.\n```\n',
    'author': 'SeparateRecords',
    'author_email': 'me@rob.ac',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SeparateRecords/intflags',
    'py_modules': modules,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
