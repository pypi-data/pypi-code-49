# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['debug_toolbar_user_switcher']

package_data = \
{'': ['*'],
 'debug_toolbar_user_switcher': ['templates/debug_toolbar_user_switcher/*']}

setup_kwargs = {
    'name': 'django-debug-toolbar-user-switcher',
    'version': '2.0.3',
    'description': 'Panel for the Django Debug toolbar to quickly switch between users.',
    'long_description': None,
    'author': 'Thread Engineering',
    'author_email': 'tech@thread.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
