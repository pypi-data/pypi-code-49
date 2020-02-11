# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ses_device_driver', 'ses_device_driver.filesystem', 'ses_device_driver.ur10']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3,<6.0']

setup_kwargs = {
    'name': 'ses-device-driver',
    'version': '0.2.1',
    'description': 'Device drivers/helper classes for each device',
    'long_description': None,
    'author': 'Vinu ESB',
    'author_email': 'vinu.vijayakumaran_nair@reutlingen-university.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
