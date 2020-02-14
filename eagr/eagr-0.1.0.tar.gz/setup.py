# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eagr',
 'eagr.client',
 'eagr.flask_bridge',
 'eagr.protos',
 'eagr.server',
 'eagr.tests',
 'eagr.tests.client',
 'eagr.tests.grpc_utils',
 'eagr.tests.reflection',
 'eagr.tests.server']

package_data = \
{'': ['*'], 'eagr': ['grpc_utils/*', 'reflection/*']}

install_requires = \
['Flask>=0.12.2,<0.13.0',
 'backoff>=1.6.0,<2.0.0',
 'funcy>=1.7.2,<2.0.0',
 'grpcio-opentracing>=1.1,<2.0',
 'grpcio-reflection>=1.25,<2.0',
 'grpcio-tools>=1.25,<2.0',
 'grpcio>=1.25,<2.0',
 'opentracing>=2.2,<3.0',
 'opentracing_instrumentation>=3.2,<4.0',
 'prometheus_client>=0.7.1,<0.8.0',
 'protobuf>=3.6.0,<4.0.0',
 'pytz>=2019.3,<2020.0']

setup_kwargs = {
    'name': 'eagr',
    'version': '0.1.0',
    'description': 'A collection of utilities for making GRPC easier to use in python.',
    'long_description': None,
    'author': 'Louis Ades',
    'author_email': 'louis.ades@kensho.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
