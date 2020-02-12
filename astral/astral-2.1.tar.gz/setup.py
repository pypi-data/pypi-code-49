# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['astral', 'doc', 'test']

package_data = \
{'': ['*'], 'doc': ['static/*']}

install_requires = \
['pytz']

extras_require = \
{':python_version == "3.6"': ['dataclasses']}

setup_kwargs = {
    'name': 'astral',
    'version': '2.1',
    'description': 'Calculations for the position of the sun and moon.',
    'long_description': "Astral\n======\n\n|travis_status| |pypi_ver|\n\n.. |travis_status| image:: https://travis-ci.org/sffjunkie/astral.svg?branch=master\n    :target: https://travis-ci.org/sffjunkie/astral\n\n.. |pypi_ver| image:: https://img.shields.io/pypi/v/astral.svg\n    :target: https://pypi.org/project/astral/\n\nThis is 'astral' a Python module which calculates\n\n    * Times for various positions of the sun: dawn, sunrise, solar noon,\n      sunset, dusk, solar elevation, solar azimuth and rahukaalam.\n    * The phase of the moon.\n\nFor documentation see the https://astral.readthedocs.io/en/latest/index.html\n",
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sffjunkie/astral',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
