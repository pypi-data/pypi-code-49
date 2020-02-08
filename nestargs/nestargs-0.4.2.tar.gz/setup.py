# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nestargs']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5,<2.0']}

setup_kwargs = {
    'name': 'nestargs',
    'version': '0.4.2',
    'description': 'Nested arguments parser',
    'long_description': '# nestargs\n\nnestargs is a Python library that defines nested program arguments. It is based on argparse.\n\n[![PyPI](https://img.shields.io/pypi/v/nestargs.svg)](https://pypi.org/project/nestargs/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nestargs.svg)](https://pypi.org/project/nestargs/)\n[![Python Tests](https://github.com/speg03/nestargs/workflows/Python%20Tests/badge.svg)](https://github.com/speg03/nestargs/actions?query=workflow%3A%22Python+Tests%22)\n[![codecov](https://codecov.io/gh/speg03/nestargs/branch/master/graph/badge.svg)](https://codecov.io/gh/speg03/nestargs)\n\nRead this in Japanese: [\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e](https://github.com/speg03/nestargs/blob/master/README.ja.md)\n\n## Installation\n\n```\npip install nestargs\n```\n\n## Basic usage\n\nDefine program arguments in the same way as argparse. A nested structure can be represented by putting a dot in the program argument name.\n\n```python\nimport nestargs\n\nparser = nestargs.NestedArgumentParser()\n\nparser.add_argument("--apple.n", type=int)\nparser.add_argument("--apple.price", type=float)\n\nparser.add_argument("--banana.n", type=int)\nparser.add_argument("--banana.price", type=float)\n\nargs = parser.parse_args(\n    ["--apple.n=2", "--apple.price=1.5", "--banana.n=3", "--banana.price=3.5"]\n)\n# => NestedNamespace(apple=NestedNamespace(n=2, price=1.5), banana=NestedNamespace(n=3, price=3.5))\n```\n\nLet\'s take out only the program argument apple.\n\n```python\nargs.apple\n# => NestedNamespace(n=2, price=1.5)\n```\n\nYou can also get each value.\n\n```python\nargs.apple.price\n# => 1.5\n```\n\nIf you want a dictionary format, you can get it this way.\n\n```python\nvars(args.apple)\n# => {\'n\': 2, \'price\': 1.5}\n```\n\n## Define program arguments from functions\n\nThe function `register_arguments` can be used to define program arguments from the parameters any function.\n\nIn the following example, program arguments with multiple prefixes are defined as the `n` and `price` parameters of the function `total_price`. At this time, the behavior of the program argument is automatically determined according to the default value of the parameter.\n\n```python\nimport nestargs\n\n\ndef total_price(n=1, price=1.0):\n    return n * price\n\n\nparser = nestargs.NestedArgumentParser()\nparser.register_arguments(total_price, prefix="apple")\nparser.register_arguments(total_price, prefix="banana")\n\nargs = parser.parse_args(\n    ["--apple.n=2", "--apple.price=1.5", "--banana.n=3", "--banana.price=3.5"]\n)\n# => NestedNamespace(apple=NestedNamespace(n=2, price=1.5), banana=NestedNamespace(n=3, price=3.5))\n```\n\nYou can call the function with the values obtained from the program arguments as follows:\n\n```python\napple = total_price(**vars(args.apple))\nbanana = total_price(**vars(args.banana))\n\nprint(apple + banana)\n# => 13.5\n```\n\n### Option decorator\n\nProgram argument settings can be added by attaching an `option` decorator to the target function. The settings that can be added are based on `ArgumentParser.add_argument` of `argparse`.\n\n```python\n@nestargs.option("n", help="number of ingredients")\n@nestargs.option("price", help="unit price of ingredients")\ndef total_price(n=1, price=1.0):\n    return n * price\n\n\nparser = nestargs.NestedArgumentParser()\nparser.register_arguments(total_price, prefix="apple")\n```\n\nThis code is equivalent to the following code:\n\n```python\ndef total_price(n=1, price=1.0):\n    return n * price\n\n\nparser = nestargs.NestedArgumentParser()\nparser.add_argument("--apple.n", type=int, default=1, help="number of ingredients")\nparser.add_argument(\n    "--apple.price", type=float, default=1.0, help="unit price of ingredients"\n)\n```\n\n### Ignores decorator\n\nBy attaching an `ignores` decorator to the target function, you can specify parameters that do not register in the program arguments.\n\n```python\n@nestargs.ignores("tax", "shipping")\ndef total_price(n=1, price=1.0, tax=1.0, shipping=0.0):\n    return n * price * tax + shipping\n\n\nparser = nestargs.NestedArgumentParser()\nparser.register_arguments(total_price, prefix="apple")\n\nargs = parser.parse_args(["--apple.n=2", "--apple.price=1.5"])\n# => NestedNamespace(apple=NestedNamespace(n=2, price=1.5))\n# Not included tax and shipping parameters\n\napple = total_price(**vars(args.apple))\n# => 3.0\n```\n',
    'author': 'Takahiro Yano',
    'author_email': 'speg03@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/speg03/nestargs',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
