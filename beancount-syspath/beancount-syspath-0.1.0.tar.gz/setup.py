# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beancount_syspath']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'beancount-syspath',
    'version': '0.1.0',
    'description': 'Manipulate sys.path within the beancount file',
    'long_description': '# beancount-syspath\n\nManipulate `sys.path` from within the beancount file. This is a plugin for\n[Beancount](http://furius.ca/beancount/\n), a double-entry bookkeeping computer language.\n\n## Installation\n\nInstall via pip\n\n```shell\npip install beancount-syspath\n```\n\n## Usage\n\nPrepend list of paths\n\n```beancount\nplugin "beancount_syspath.prepend" "[\n    \'some/dir\',\n    \'other/dir\'\n]"\n```\n\nor append list of paths\n\n```beancount\nplugin "beancount_syspath.append" "[\n    \'some/dir\',\n    \'other/dir\'\n]"\n```\n\nPlace the directive before other plugin loading ones, so they can make use of the updated `sys.path`.\n\nThe config value is a python list literal, which will be evaluated by `ast.literal_eval`, and then\nprepended/appended to `sys.path`.\n',
    'author': 'Aetf',
    'author_email': 'aetf@unlimited-code.works',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Aetf/beancount-syspath',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
