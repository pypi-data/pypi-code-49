# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wagtail_srcset', 'wagtail_srcset.templatetags']

package_data = \
{'': ['*']}

modules = \
['commands']
install_requires = \
['wagtail>=2.8,<3.0']

entry_points = \
{'console_scripts': ['autoformat = commands:black',
                     'docs = commands:docs',
                     'lint = commands:flake8',
                     'notebook = commands:notebook',
                     'show_coverage = commands:coverage',
                     'test = commands:test']}

setup_kwargs = {
    'name': 'wagtail-srcset',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jochen Wersdörfer',
    'author_email': 'jochen@wersdoerfer.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
