# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['format_textview', 'format_textview.gtk', 'format_textview.tests']

package_data = \
{'': ['*']}

install_requires = \
['pygobject>=3.32.2,<4.0.0', 'rfc3987>=1.3.8,<2.0.0']

setup_kwargs = {
    'name': 'gtk-formatted-textview',
    'version': '0.2.0',
    'description': 'A Gtk Textview widget with a toolbar for adding formatting as bold, italics, underline, linkx, etc',
    'long_description': None,
    'author': 'BeatLink',
    'author_email': 'beatlink@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
