# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['optga']

package_data = \
{'': ['*'], 'optga': ['tools/*']}

install_requires = \
['dataclasses_json>=0.3.7,<0.4.0',
 'llvmlite==0.30.0',
 'numba==0.45.0',
 'numpy>=1.17,<2.0',
 'pandas>=0.25.3,<0.26.0']

entry_points = \
{'console_scripts': ['main = tests.test_optga:main']}

setup_kwargs = {
    'name': 'optga',
    'version': '0.2.0',
    'description': 'Framework to find pareto-optimum inputs of your machine learning models',
    'long_description': None,
    'author': 'horoiwa',
    'author_email': 'horoiwa195@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
