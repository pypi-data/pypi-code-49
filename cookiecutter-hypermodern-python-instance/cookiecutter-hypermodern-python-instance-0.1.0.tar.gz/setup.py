# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cookiecutter_hypermodern_python_instance']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5.0,<2.0.0']}

entry_points = \
{'console_scripts': ['cookiecutter-hypermodern-python-instance = '
                     'cookiecutter_hypermodern_python_instance.console:main']}

setup_kwargs = {
    'name': 'cookiecutter-hypermodern-python-instance',
    'version': '0.1.0',
    'description': 'Cookiecutter Hypermodern Python Instance',
    'long_description': '[![Tests](https://github.com/cjolowicz/cookiecutter-hypermodern-python-instance/workflows/Tests/badge.svg)](https://github.com/cjolowicz/cookiecutter-hypermodern-python-instance/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/cjolowicz/cookiecutter-hypermodern-python-instance/branch/master/graph/badge.svg)](https://codecov.io/gh/cjolowicz/cookiecutter-hypermodern-python-instance)\n[![PyPI](https://img.shields.io/pypi/v/cookiecutter-hypermodern-python-instance.svg)](https://pypi.org/project/cookiecutter-hypermodern-python-instance/)\n[![Python Version](https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance)](https://pypi.org/project/cookiecutter-hypermodern-python-instance)\n[![Read the Docs](https://readthedocs.org/projects/cookiecutter-hypermodern-python-instance/badge/)](https://cookiecutter-hypermodern-python-instance.readthedocs.io/)\n[![License](https://img.shields.io/pypi/l/cookiecutter-hypermodern-python-instance)](https://opensource.org/licenses/MIT)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# cookiecutter-hypermodern-python-instance\n',
    'author': 'Claudio Jolowicz',
    'author_email': 'mail@claudiojolowicz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cjolowicz/cookiecutter-hypermodern-python-instance',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
