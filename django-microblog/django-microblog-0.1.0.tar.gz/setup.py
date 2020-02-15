# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['microblog', 'microblog.migrations']

package_data = \
{'': ['*'], 'microblog': ['fixtures/*']}

install_requires = \
['django>=3.0,<4.0', 'pillow>=7.0,<8.0']

setup_kwargs = {
    'name': 'django-microblog',
    'version': '0.1.0',
    'description': 'Simple blogging application for Django',
    'long_description': '# django-microblog\n\n![](https://img.shields.io/badge/Version-0.1.0-orange.svg?style=flat-square)\n![](https://img.shields.io/badge/Django-2.0+-green.svg?style=flat-square)\n![](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)\n\ndjango-microblog minimal blogging application for Django\n\n## Getting started\n\n1. Installation\n\n```bash\npip install django-microblog\n```\n\n2. Add **microblog** into **INSTALLED_APPS** in your settings file.',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lukasvinclav/django-microblog',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
