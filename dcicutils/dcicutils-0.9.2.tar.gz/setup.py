# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['dcicutils']

package_data = \
{'': ['*'], 'dcicutils': ['kibana/*']}

install_requires = \
['aws-requests-auth==0.4.2',
 'boto3==1.10.46',
 'botocore==1.13.46',
 'elasticsearch==5.5.3',
 'requests>=2.21.0,<3.0.0',
 'structlog==19.2.0',
 'urllib3>=1.24.3,<2.0.0']

setup_kwargs = {
    'name': 'dcicutils',
    'version': '0.9.2',
    'description': 'Utility package for interacting with the 4DN Data Portal and other 4DN resources',
    'long_description': '=====\nutils\n=====\n\nCheck out our full documentation `here <https://dcic-utils.readthedocs.io/en/latest/>`_\n\nThis repository contains various utility modules shared amongst several projects in the 4DN-DCIC. It is meant to be used internally by the DCIC team and externally as a Python API to `Fourfront <https://data.4dnucleome.org>`_\\ , the 4DN data portal.\n\npip installable as the ``dcicutils`` package with: ``pip install dcicutils``\n\nSee `this document <./docs/getting_started.md>`_ for tips on getting started. `Go here <./docs/examples.md>`_ for examples of some of the most useful functions.\n\n\n.. image:: https://travis-ci.org/4dn-dcic/utils.svg?branch=master\n   :target: https://travis-ci.org/4dn-dcic/utils\n   :alt: Build Status\n\n\n.. image:: https://coveralls.io/repos/github/4dn-dcic/utils/badge.svg?branch=master\n   :target: https://coveralls.io/github/4dn-dcic/utils?branch=master\n   :alt: Coverage\n\n.. image:: https://readthedocs.org/projects/dcic-utils/badge/?version=latest\n   :target: https://dcic-utils.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n',
    'author': 'William Ronchetti',
    'author_email': 'william_ronchetti@hms.harvard.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/4dn-dcic/utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
