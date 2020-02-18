# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mincli']
install_requires = \
['argparse>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'mincli',
    'version': '0.1.0',
    'description': 'A minimalistic CLI wrapper out to be the best',
    'long_description': None,
    'author': 'pascal',
    'author_email': 'pascal@vks.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
