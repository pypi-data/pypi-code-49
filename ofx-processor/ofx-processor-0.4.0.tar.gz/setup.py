# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ofx_processor',
 'ofx_processor.bpvf_processor',
 'ofx_processor.revolut_processor',
 'ofx_processor.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'dateparser>=0.7.2,<0.8.0',
 'ofxtools>=0.8.20,<0.9.0',
 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['process-bpvf = ofx_processor.bpvf_processor.main:cli',
                     'process-revolut = '
                     'ofx_processor.revolut_processor.main:cli']}

setup_kwargs = {
    'name': 'ofx-processor',
    'version': '0.4.0',
    'description': 'Personal ofx processor',
    'long_description': '# ofx-processor\n\n## Usage\n\n```shell script\nprocess-bpvf /path/to/ofxfile.ofx\n# Or\nprocess-revolut /path/to/csvfile.csv\n```\n\nIt will write a `processed` file in the same folder with the same extension.\n\nIt will not overwrite the original file.\n',
    'author': 'Gabriel Augendre',
    'author_email': 'gabriel@augendre.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
