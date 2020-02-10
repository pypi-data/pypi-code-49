# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['show_meetings']

package_data = \
{'': ['*']}

install_requires = \
['PILLOW>=7.0.0,<8.0.0', 'pywin32>=227,<228']

entry_points = \
{'console_scripts': ['show-meetings = show_meetings.cli:main']}

setup_kwargs = {
    'name': 'show-meetings',
    'version': '0.1.0',
    'description': 'Show upcoming Outlook meetings, either as text or on the Windows lock screen',
    'long_description': 'Show-Meetings\n=============\n\nShow meetings, either in the terminal or on the Windows lock screen.\n',
    'author': 'Blair Conrad',
    'author_email': 'blair@blairconrad.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/blairconrad/notions.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
