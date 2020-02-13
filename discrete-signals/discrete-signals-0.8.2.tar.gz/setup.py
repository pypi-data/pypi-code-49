# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['discrete_signals']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0', 'funcy>=1.14,<2.0', 'sortedcontainers>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'discrete-signals',
    'version': '0.8.2',
    'description': 'A domain specific language for modeling and manipulating discrete time signals.',
    'long_description': '<figure>\n  <img src="assets/logo_text.svg" alt="py-aiger logo" width=300px>\n  <figcaption>\n    A domain specific language for modeling and manipulating discrete\n    time signals.\n  </figcaption>\n</figure>\n\n\n[![Build Status](https://cloud.drone.io/api/badges/mvcisback/DiscreteSignals/status.svg)](https://cloud.drone.io/mvcisback/DiscreteSignals)\n[![codecov](https://codecov.io/gh/mvcisback/DiscreteSignals/branch/master/graph/badge.svg)](https://codecov.io/gh/mvcisback/DiscreteSignals)\n[![Updates](https://pyup.io/repos/github/mvcisback/DiscreteSignals/shield.svg)](https://pyup.io/repos/github/mvcisback/DiscreteSignals/)\n\n[![PyPI version](https://badge.fury.io/py/discrete-signals.svg)](https://badge.fury.io/py/discrete-signals)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\n# About\n\nThis library aims to provide a domain specific language for modeling\nand manipulating discrete time signals. Intuitively, most of the time,\nthe discrete time signal\'s value is undefined.\n\nIf `discrete-signals` isn\'t for you, I recommend checking out\n[traces](https://github.com/datascopeanalytics/traces) (which this\nlibrary took design inspiration from). Both libraries offer a\nconvenient way to model unevenly-spaced discrete time signals.\n\n# Installation\n\n`$ pip install discrete-signals`\n\n# Usage\n\n```python\nfrom discrete_signals import signal\n\nx = signal([(0, 1), (1, 2), (2, 3)], start=0, end=10, tag=\'x\')\ny = signal([(0.5, \'a\'), (1, \'b\'), (2, \'c\')], start=0, end=3, tag=\'y\')\n\nx\n# start, end: [0, 10)\n# data: [(0, {\'x\': 1}), (1, {\'x\': 2}), (2, {\'x\': 3})]\n\ny\n# start, end: [0, 3)\n# data: [(0.5, {\'y\': \'a\'}), (1, {\'y\': \'b\'}), (2, {\'y\': \'c\'})]\n```\n\n## Parallel Composition\n\n```python\nx | y\n# start, end: [0, 10)\n# data: [(0, {\'x\': 1}), (0.5, {\'y\': \'a\'}), (1, {\'x\': 2, \'y\': \'b\'}), (2, {\'x\': 3, \'y\': \'c\'})]\n```\n\n## Concatenation\n\n```python\nx @ y\n# start, end: [0, 13)\n# data: [(0, {\'x\': 1}), (1, {\'x\': 2}), (2, {\'x\': 3}), (10.5, {\'y\': \'a\'}), (11, {\'y\': \'b\'}), (12, {\'y\': \'c\'})]\n```\n\n## Retagging/Relabeling\n\n```python\nx.retag({\'x\': \'z\'})\n# start, end: [0, 10)\n# data: [(0, {\'z\': 1}), (1, {\'z\': 2}), (2, {\'z\': 3})]\n```\n\n## Time shifting\n\n```python\nx >> 1.1\n# start, end: [1.1, 11.1)\n# data: [(1.1, {\'x\': 1}), (2.1, {\'x\': 2}), (3.1, {\'x\': 3})]\n\nx << 1\n# start, end: [-1, 9)\n# data: [(-1, {\'x\': 1}), (0, {\'x\': 2}), (1, {\'x\': 3})]\n```\n\n## Slicing\n\n```python\nx[1:]\n# start, end: [1, 10)\n# data: [(1, {\'x\': 2}), (2, {\'x\': 3})]\n\nx[:1]\n# start, end: [0, 1)\n# data: [(0, {\'x\': 1})]\n```\n\n## Rolling Window\n\n```python\nx.rolling(1, 3)\n# start, end: [-1, 7)\n# data: [(-1, {\'x\': (1, 2)}), (0, {\'x\': (2, 3)}), (1, {\'x\': (3,)})]\n```\n\n## Mapping a Function\n\nOne perform a point wise transform of the signal. For example, the\nfollowing is equivalent to retagging the signal and adding 1.\n\n\n```python\nx.transform(lambda val: {\'y\': val[\'x\'] + 1})\n# start, end: [0, 10)\n# data: [(0, {\'y\': 2}), (1, {\'y\': 3}), (2, {\'y\': 4})]\n```\n\nAlternatively, `DiscreteSignal`s support mapping the dictionary of values to a single value (and optionally tag it):\n\n```python\nx.map(lambda val: str(val[\'x\']), tag=\'z\')\n# start, end: [0, 10)\n# data: [(0, {\'z\': \'1\'}), (1, {\'z\': \'2\'}), (2, {\'z\': \'3\'})]\n```\n\n## Filter a signal\n\n```python\nx.filter(lambda val: val[\'x\'] > 2)\n# start, end: [0, 10)\n# data: [(2, {\'x\': 3})]\n```\n\n## Projecting onto a subset of the tags.\n\n```python\n(x | y).project({\'x\'})\n# start, end: [0, 10)\n# data: [(0, {\'x\': 1}), (1, {\'x\': 2}), (2, {\'x\': 3})]\n```\n\n## Attributes\n```python\n(x | y).tags\n# {\'x\', \'y\'}\n\nx.values()\n# SortedDict_values([defaultdict(None, {\'x\': 1}), defaultdict(None, {\'x\': 2}), defaultdict(None, {\'x\': 3})])\n\nlist(x.times())\n# [0, 1, 2]\n```\n',
    'author': 'Marcell Vazquez-Chanlatte',
    'author_email': 'mvc@linux.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mvcisback/DiscreteSignals',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
