# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beancount_syspath']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'beancount-syspath',
    'version': '0.2.1',
    'description': 'Manipulate sys.path within the beancount file',
    'long_description': '# beancount-syspath\n\nManipulate `sys.path` from within the beancount file. This is a plugin for\n[Beancount](http://furius.ca/beancount/\n), a double-entry bookkeeping computer language.\n\n## Installation\n\nInstall via pip\n\n```shell\npip install beancount-syspath\n```\n\n## Usage\n\nPrepend list of paths\n\n```beancount\nplugin "beancount_syspath.plugin" "{\n    \'append\': [\'some/dir\', \'other/dir\'],\n    \'prepend\': [\'some/dir\', \'other/dir\'],\n}"\n```\n\nNote: Place the directive before other plugin loading ones, so they can make use of the updated `sys.path`.\n\n### Configuration\nThe config value is a python dict literal, contains the following keys\n\n| Key | Type | Optional | Default | Meaning |\n|:-:|:-:|:-:|:-:|:-:|\n| `append` | `List[str]` | yes | `[]` | Append the list of path to `sys.path` |\n| `prepend` | `List[str]` | yes | `[]` | Prepend the list of path to `sys.path` |\n| `normalize_to_root` | `bool` | yes | `True` | If the path is relative, it is considered to be relative to the root beancount file, and normalized to absolute path before adding to `sys.path`. |\n',
    'author': 'Aetf',
    'author_email': 'aetf@unlimited-code.works',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Aetf/beancount-syspath',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
