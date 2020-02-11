# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['laziest', 'laziest.conf']

package_data = \
{'': ['*']}

install_requires = \
['black>=18.3-alpha.0,<19.0',
 'clifier>=0.0.3,<0.0.4',
 'codegraph>=0.0.4,<0.0.5']

entry_points = \
{'console_scripts': ['lazy = laziest.conf.cli:init_cli']}

setup_kwargs = {
    'name': 'laziest',
    'version': '0.0.dev3',
    'description': '',
    'long_description': "Laziest\n=======\nGenerator of test_*.py files for your Python code\n\n\nInstallation:\n*************\n\n    pip install laziest\n\nUsage:\n*************\n\n    lazy /path/to/python/code/files\n\n\nFor example:\n\n    lazy /home/yourUser/laziest/tests/code_sample/done/conditions.py\n\n\nIt will generate test file in directory:\n\n    /home/yourUser/laziest/tests/test_conditions.py\n\n\nRun tests with 'pytest' to check that they are valid:\n\n    pytest /home/yourUser/laziest/tests/functional/test_primitive_code.py\n\n\nYou can run laziest tests with tox and check output.\n\n\nDocs:\n*****\n\nComing soon.",
    'author': 'xnuinside',
    'author_email': 'xnuinside@gmail.com',
    'url': 'https://github.com/xnuinside/laziest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
