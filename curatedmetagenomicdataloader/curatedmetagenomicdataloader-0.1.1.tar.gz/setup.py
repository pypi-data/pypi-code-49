# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['curatedmetagenomicdataloader']

package_data = \
{'': ['*']}

install_requires = \
['biopython>=1.74,<2.0',
 'fireworks-ml>=0.3.7,<0.4.0',
 'joblib>=0.14.1,<0.15.0',
 'psycopg2-binary>=2.8.4,<3.0.0',
 'python-dotenv>=0.10.3,<0.11.0',
 'the-whole-caboodle>=0.1.6,<0.2.0',
 'tqdm>=4.41.1,<5.0.0']

setup_kwargs = {
    'name': 'curatedmetagenomicdataloader',
    'version': '0.1.1',
    'description': 'PyTorch DataLoader for curatedMetagenomicData',
    'long_description': None,
    'author': 'smk508',
    'author_email': 'skhan8@mail.einstein.yu.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
