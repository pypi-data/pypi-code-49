# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rues',
 'rues.crossover_algorithms',
 'rues.mutation_algorithms',
 'rues.reinsertion_algorithms',
 'rues.selection_algorithms',
 'rues.utils',
 'rues.utils.multiprocessing']

package_data = \
{'': ['*']}

install_requires = \
['corner>=2.0.1,<3.0.0',
 'matplotlib>=3.1.3,<4.0.0',
 'numpy>=1.18.1,<2.0.0',
 'scipy>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'rues',
    'version': '0.1.1.1',
    'description': 'rues - genetic algorithms in python',
    'long_description': None,
    'author': 'Kamuish',
    'author_email': 'andremiguel952@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
