# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['command_log', 'command_log.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2,<4.0']

setup_kwargs = {
    'name': 'django-command-log',
    'version': '0.2.2',
    'description': 'Django management command auditing app',
    'long_description': '# Django Management Command Log\n\nApp to enable simple auditing of Django management commands\n\n### Version support\n\nThis project now support Django 2.2 and 3.0, and Python 3.7 and 3.8. Python 3.6 has been deprecated\nbecause the lack of support for `__future__.annotations` makes type hinting across 3.6-3.7\ncomplicated. See git tags and PyPI classifiers for support.\n\n## Background\n\nThis app wraps the standad Django management command base class to record the running of a command.\nIt logs the name of the command, start and end time, and the output (if any). If the command fails\nwith a Python exception, the error message is added to the record, and the exception itself is\nlogged using `logging.exception`.\n\n![Screenshot of admin list view](https://github.com/yunojuno/django-management-command-log/blob/master/screenshots/list-view.png)\n\n![Screenshot of admin detail view](https://github.com/yunojuno/django-management-command-log/blob/master/screenshots/detail-view.png)\n\nSee the `test_command` and `test_transaction_command` for examples.\n\n## TODO\n\nDocumentation.\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yunojuno/django-management-command-log',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
