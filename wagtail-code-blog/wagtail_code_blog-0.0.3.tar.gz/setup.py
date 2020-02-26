# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wagtail_code_blog', 'wagtail_code_blog.migrations']

package_data = \
{'': ['*'],
 'wagtail_code_blog': ['static/wagtail_code_blog/css/*',
                       'static/wagtail_code_blog/images/*',
                       'templates/wagtail_code_blog/*']}

install_requires = \
['wagtail-metadata>=3.0.0,<4.0.0', 'wagtail>=2.8,<3.0']

setup_kwargs = {
    'name': 'wagtail-code-blog',
    'version': '0.0.3',
    'description': '',
    'long_description': None,
    'author': 'Dani Hodovic',
    'author_email': 'dani.hodovic@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
