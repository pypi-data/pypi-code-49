# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['filecheck']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['filecheck = filecheck.FileCheck:main']}

setup_kwargs = {
    'name': 'filecheck',
    'version': '0.0.12',
    'description': "Python port of LLVM's FileCheck, flexible pattern matching file verifier",
    'long_description': None,
    'author': 'Stanislav Pankevich',
    'author_email': 's.pankevich@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
