# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['injecta']

package_data = \
{'': ['*'],
 'injecta': ['autowiring/*',
             'bundle/*',
             'compiler/*',
             'config/*',
             'config/YamlConfigReaderTest/basic/*',
             'config/YamlConfigReaderTest/search/_config/*',
             'config/YamlConfigReaderTest/search/mypackage/*',
             'config/YamlConfigReaderTest/search/mypackage/subpackage/*',
             'container/*',
             'definition/*',
             'definition/argument/*',
             'dtype/*',
             'generator/*',
             'kernel/*',
             'mocks/*',
             'parameter/*',
             'schema/*',
             'service/*',
             'service/class_/*',
             'tag/*']}

install_requires = \
['PyYAML>=5.1.0,<5.2.0', 'python-box>=3.4.0,<3.5.0', 'tomlkit>=0.5.8,<0.6.0']

setup_kwargs = {
    'name': 'injecta',
    'version': '0.5.2',
    'description': 'Dependency Injection Container Library',
    'long_description': 'Hello world',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/injecta',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<3.8.0',
}


setup(**setup_kwargs)
