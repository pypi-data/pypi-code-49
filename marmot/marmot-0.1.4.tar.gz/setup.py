# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marmot']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0',
 'optuna>=0.18.1,<0.19.0',
 'pandas>=0.25.3,<0.26.0',
 'scikit-learn>=0.21.3,<0.22.0',
 'scipy>=1.3,<2.0',
 'xgboost>=0.90.0,<0.91.0']

setup_kwargs = {
    'name': 'marmot',
    'version': '0.1.4',
    'description': 'Ensemble modeling with hyperparameter tuner',
    'long_description': '=====================================================\nMarmot: Ensemble modeling with hyperparameter tuner\n=====================================================\n\n.. image:: https://travis-ci.org/horoiwa/marmot.svg?branch=master\n    :target: https://travis-ci.org/horoiwa/marmot\n\n\nOverview\n========\n\n\nKey Features\n============\n\n- Ready to use ensemble models extended from sklearn\n\n- Rapid hyperparameter tuning powered by `optuna`\n\n\nGetting started\n===============\n\nExample: Boston housing dataset\n',
    'author': 'horoiwa',
    'author_email': 'horoiwa195@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
