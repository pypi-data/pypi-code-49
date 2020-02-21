# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpr_complex']

package_data = \
{'': ['*']}

install_requires = \
['bokeh>=1.4.0,<2.0.0', 'numpy>=1.18.1,<2.0.0', 'scipy>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'gpr-complex',
    'version': '0.2.0.post1',
    'description': 'A GPR library that can work with complex numbers',
    'long_description': 'A Gaussian Process Regression (GPR) library that can work with complex numbers.\n\n\n# Development\n\nRun `poetry install` to create the virtual environment and `pre-commit install`\nto install the commit hooks.\n',
    'author': 'Darlan Cavalcante Moreira',
    'author_email': 'darcamo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/darcamo/gpr_complex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
