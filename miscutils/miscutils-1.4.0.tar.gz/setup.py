# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['miscutils',
 'miscutils.dbg',
 'miscutils.func',
 'miscutils.insp',
 'miscutils.insp.experimental',
 'miscutils.io',
 'miscutils.io.experimental',
 'miscutils.iter',
 'miscutils.os',
 'miscutils.os.experimental',
 'miscutils.str',
 'miscutils.tools',
 'miscutils.tools.experimental',
 'miscutils.user',
 'miscutils.user.experimental']

package_data = \
{'': ['*']}

install_requires = \
['ruamel.yaml>=0.16.7,<0.17.0']

entry_points = \
{'console_scripts': ['pylisting = miscutils.tools.experimental.listing:main']}

setup_kwargs = {
    'name': 'miscutils',
    'version': '1.4.0',
    'description': 'Miscellaneous utilities for general use',
    'long_description': '# miscutils\n\nThese are miscellaneous python utilities for general use. This package includes following submodules:\n\n* **dbg** - Debugging utilities.\n* **func** - Utilities related to functions.\n* **insp** - Utilities for inspecting the code.\n* **io** - Interacting with input/output of python script.\n* **iter** - Interacting with iterators and collections.\n* **os** - Operating system related utilities.\n* **str** - Handling strings.\n* **tools** - Not the code, but utilities for programmers.\n* **user** - User data processing.\n\n## Developing\n\nStart from preparing venv:\n\n```sh\npython3.7 -m poetry install\n```\n\n## Building Docs\n\nUpdate `.rst` manually. Then:\n\n```sh\npython3.7 -m poetry run make -C docs html\n```\n\n## Testing\n\n```sh\npython3.8 -m poetry run pytest tests\n```\n\n## Releasing\n\nUpdate version in `pyproject.toml`. Then:\n\n```sh\npython3.7 -m poetry build\ngit tag X.Y.Z\ngit push\ngit push --tags\npython3.7 -m poetry publish\n```\n\nlog into readthedocs.io and trigger a Build\n\n## References\n\n[Documentation](http://pymiscutils.readthedocs.io/)\n\n[Source code](https://github.com/gergelyk/pymiscutils/)\n\n[Package](https://pypi.python.org/pypi/miscutils/)\n',
    'author': 'Grzegorz Krason',
    'author_email': 'grzegorz.krason@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
