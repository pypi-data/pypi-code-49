# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ink_cms', 'ink_cms.management.commands', 'ink_cms.migrations']

package_data = \
{'': ['*'],
 'ink_cms': ['static/ink_cms/admin/css/*',
             'static/ink_cms/assets/*',
             'static/ink_cms/dist/*',
             'static/ink_cms/dist/assets/css/*',
             'static/ink_cms/dist/assets/fonts/*',
             'static/ink_cms/dist/assets/js/*',
             'templates/ink_cms/*']}

install_requires = \
['django>=3.0.2,<4.0.0',
 'djangorestframework>=3.11.0,<4.0.0',
 'easy-thumbnails>=2.7,<3.0',
 'psycopg2>=2.8.4,<3.0.0']

setup_kwargs = {
    'name': 'ink-cms',
    'version': '0.2.0',
    'description': 'A headless CMS for the Django Admin',
    'long_description': None,
    'author': 'Robert Townley',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
