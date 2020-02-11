# -*- coding: utf-8 -*-
from distutils.core import setup

package_dir = \
{'': 'src'}

packages = \
['pubsub_worker']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-pubsub>=1.2,<2.0']

setup_kwargs = {
    'name': 'pubsub-worker',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jacob Hayes',
    'author_email': 'jacob.r.hayes@gmail.com',
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
