# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bcf_api_xml', 'bcf_api_xml.models']

package_data = \
{'': ['*'], 'bcf_api_xml': ['Schemas/*']}

install_requires = \
['generateDS>=2.35.13,<3.0.0',
 'lxml>=4.5.0,<5.0.0',
 'python-dateutil>=2.8.1,<3.0.0']

setup_kwargs = {
    'name': 'bcf-api-xml',
    'version': '0.2.4',
    'description': 'Convert BCF-API to BCF-XML',
    'long_description': None,
    'author': 'Hugo Duroux',
    'author_email': 'hugo@bimdata.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
