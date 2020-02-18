# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rigorous']

package_data = \
{'': ['*']}

extras_require = \
{'cli': ['click>=7.0,<8.0']}

entry_points = \
{'console_scripts': ['rigorous-latex = rigorous.latex:main']}

setup_kwargs = {
    'name': 'rigorous',
    'version': '0.0.1',
    'description': 'A Python interpreter based on a formal semantics for Python.',
    'long_description': 'Rigorous Python\n===============\n\nA Python interpreter based on a formal semantics for Python.\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dgit.cs.uni-saarland.de/koehlma/rigorous-python',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
