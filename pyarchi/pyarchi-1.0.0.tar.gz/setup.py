# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyarchi',
 'pyarchi.data_objects',
 'pyarchi.initial_detection',
 'pyarchi.masks_creation',
 'pyarchi.output_creation',
 'pyarchi.routines',
 'pyarchi.star_track',
 'pyarchi.utils',
 'pyarchi.utils.data_export',
 'pyarchi.utils.factors_handler',
 'pyarchi.utils.misc',
 'pyarchi.utils.noise_metrics',
 'pyarchi.utils.optimization']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.0,<5.0',
 'matplotlib>=3.1.2,<4.0.0',
 'opencv-python>=4.1.2,<5.0.0',
 'pyyaml>=5.3,<6.0',
 'scipy>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'pyarchi',
    'version': '1.0.0',
    'description': "Photometry for CHEOPS's background stars",
    'long_description': None,
    'author': 'Kamuish',
    'author_email': 'andremiguel952@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
