# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dophon',
 'dophon.annotation',
 'dophon.annotation.description',
 'dophon.annotation.request',
 'dophon.annotation.request.param_adapter',
 'dophon.annotation.response',
 'dophon.errors',
 'dophon.tools',
 'dophon.tools.framework_const',
 'dophon.tools.gc',
 'dophon.web_templates']

package_data = \
{'': ['*']}

install_requires = \
['dophon-logger',
 'dophon-manager',
 'dophon-properties',
 'flask',
 'tornado',
 'tqdm',
 'urllib3',
 'xmltodict']

setup_kwargs = {
    'name': 'dophon',
    'version': '1.3.6a2',
    'description': 'dophon web framework like springboot',
    'long_description': None,
    'author': 'CallMeE',
    'author_email': 'ealohu@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
