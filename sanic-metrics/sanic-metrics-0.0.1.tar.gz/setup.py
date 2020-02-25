# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sanic_metrics']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.10.0,<0.11.0',
 'sanic-plugins-framework>=0.9.2,<0.10',
 'sanic>=18.12.0']

entry_points = \
{'sanic_plugins': ['SanicMetrics = sanic_metrics.plugin:instance']}

setup_kwargs = {
    'name': 'sanic-metrics',
    'version': '0.0.1',
    'description': 'Sanic plugin for capturing and logging access',
    'long_description': 'Sanic-Metrics\n=============\n\n|Build Status| |Latest Version| |Supported Python versions| |License|\n\nSanic-Metrics is a simple Sanic Plugin to capture and log access requests.\n\nLog formats supported:\n * Common (and V:Common)\n * Combined (and V:Combined)\n * W3C (aka W3C extended aka IIS)\n\nDetailed documentation coming soon.\n\nContributing\n------------\n\nQuestions, comments or improvements? Please create an issue on\n`Github <https://github.com/ashleysommer/sanic-metrics>`__\n\nCredits\n-------\n\nAshley Sommer `ashleysommer@gmail.com <ashleysommer@gmail.com>`__\n\n\n.. |Build Status| image:: https://api.travis-ci.org/ashleysommer/sanic-metrics.svg?branch=master\n   :target: https://travis-ci.org/ashleysommer/sanic-metrics\n\n.. |Latest Version| image:: https://img.shields.io/pypi/v/Sanic-Plugins-Framework.svg\n   :target: https://pypi.python.org/pypi/sanic-metrics/\n\n.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/sanic-metrics.svg\n   :target: https://img.shields.io/pypi/pyversions/sanic-metrics.svg\n\n.. |License| image:: http://img.shields.io/:license-mit-blue.svg\n   :target: https://pypi.python.org/pypi/sanic-metrics/\n',
    'author': 'Ashley Sommer',
    'author_email': 'ashleysommer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ashleysommer/sanic-metrics',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
