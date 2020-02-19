# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfglib', 'cfglib.sources']

package_data = \
{'': ['*']}

extras_require = \
{'docs': ['Sphinx>=1.8,<2.0',
          'sphinxcontrib-apidoc>=0.3.0,<0.4.0',
          'sphinxcontrib-fulltoc>=1.2,<2.0']}

setup_kwargs = {
    'name': 'cfglib',
    'version': '1.0.1',
    'description': 'An extensible configuration library',
    'long_description': '======\ncfglib\n======\n\n\n.. image:: https://img.shields.io/pypi/v/cfglib.svg\n        :target: https://pypi.python.org/pypi/cfglib\n\n.. image:: https://github.com/swarmer/cfglib-py/workflows/CI/badge.svg\n        :target: https://github.com/swarmer/cfglib-py/actions\n        :alt: CI Status\n\n.. image:: https://readthedocs.org/projects/cfglib/badge/?version=latest\n        :target: https://cfglib.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n.. image:: https://codecov.io/gh/swarmer/cfglib-py/branch/master/graph/badge.svg\n  :target: https://codecov.io/gh/swarmer/cfglib-py\n\n\nAn extensible configuration library\n\n\n* Free software: MIT license\n* Documentation: https://cfglib.readthedocs.io.\n\n\nFeatures\n--------\n\n* Describe config schema and perform validation\n* Numerous utils to compose configs from multiple sources, etc.\n* Read settings from environment\n',
    'author': 'Anton Barkovsky',
    'author_email': 'anton@swarmer.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/swarmer/cfglib-py',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
