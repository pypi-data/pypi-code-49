# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['config_file', 'config_file.parsers']

package_data = \
{'': ['*']}

install_requires = \
['nested-lookup>=0.2.19,<0.3.0', 'pyyaml>=5.2,<6.0', 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'config-file',
    'version': '0.9.0',
    'description': 'Manage your configuration files.',
    'long_description': "Config File\n===========\n\n   Manage and manipulate your configuration files\n\n|Python Verison| |Version| |Style| |Documentation Status| |Build Status| |Codecov|\n\n   This python package is currently in rapid development and is in a\n   pre-alpha phase. The API is liable to break until v1 so if you're\n   going to use it, pinning the version is recommended. All notable\n   changes are kept track of in the changelog.\n\nConfig File allows you to use the same simple API for manipulating INI,\nJSON, YAML, and TOML configuration files. For the time being, it only\nsupports INI and JSON.\n\nInstallation\n------------\n\n.. code:: bash\n\n   $ pip install config-file\n\n.. |Python Verison| image:: https://img.shields.io/pypi/pyversions/config-file.svg\n.. |Version| image:: https://img.shields.io/pypi/v/config-file\n   :target: https://pypi.org/project/config-file/\n.. |Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://pypi.org/project/black/\n.. |Documentation Status| image:: https://readthedocs.org/projects/config-file/badge/?version=latest\n   :target: https://config-file.readthedocs.io/en/latest/?badge=latest\n.. |Build Status| image:: https://travis-ci.com/eugenetriguba/config-file.svg?branch=master\n   :target: https://travis-ci.com/eugenetriguba/config-file\n.. |Codecov| image:: https://codecov.io/gh/eugenetriguba/config-file/graph/badge.svg\n   :target: https://codecov.io/gh/eugenetriguba/config-file\n",
    'author': 'Eugene Triguba',
    'author_email': 'eugenetriguba@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eugenetriguba/config_file',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
