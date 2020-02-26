# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auto_mlops']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=1.3.0,<2.0.0',
 'requests>=2.23.0,<3.0.0',
 'scikit-learn>=0.22.1,<0.23.0']

setup_kwargs = {
    'name': 'auto-mlops',
    'version': '0.1.9',
    'description': 'Deploy your model in one line of code',
    'long_description': None,
    'author': 'Datarmada',
    'author_email': 'contact@datarmada.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
