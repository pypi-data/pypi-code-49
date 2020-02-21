# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['red_fill']

package_data = \
{'': ['*']}

install_requires = \
['keyring>=19.2,<20.0']

setup_kwargs = {
    'name': 'red-fill',
    'version': '9.1.0',
    'description': 'RED-fill is part of the Curious Containers project. It provides functionality to resolve template keys for RED clients.',
    'long_description': '## RED-fill\n\nRED-fill is part of the Curious Containers project.\nIt enables researchers to implement RED variables resolution\nby using a keyring or interactive user input.\n\n## Acknowledgements\n\nThe Curious Containers software is developed at [CBMI](https://cbmi.htw-berlin.de/) (HTW Berlin - University of Applied Sciences). The work is supported by the German Federal Ministry of Economic Affairs and Energy (ZIM project BeCRF, grant number KF3470401BZ4), the German Federal Ministry of Education and Research (project deep.TEACHING, grant number 01IS17056 and project deep.HEALTH, grant number 13FH770IX6) and HTW Berlin Booster.\n',
    'author': 'Christoph Jansen',
    'author_email': 'Christoph.Jansen@htw-berlin.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.curious-containers.cc/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
