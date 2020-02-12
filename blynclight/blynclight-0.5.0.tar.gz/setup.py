# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blynclight', 'blynclight.hid']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'requests>=2.21,<3.0', 'typer>=0.0.8,<0.0.9']

entry_points = \
{'console_scripts': ['blync = blynclight.__main__:blync_cli',
                     'fli = blynclight.__main__:fli_cli',
                     'rainbow = blynclight.__main__:rainbow_cli',
                     'throbber = blynclight.__main__:throbber_cli']}

setup_kwargs = {
    'name': 'blynclight',
    'version': '0.5.0',
    'description': 'Python language bindings for Embrava BlyncLight devices.',
    'long_description': 'Embrava BlyncLight\n==================\n\n|pypi| |license| |python|\n\n**blynclight** is a Python 3 package that provides bindings for the\n`Embrava`_ BlyncLight family of products. These bindings have been\ntested on MacOS and Linux using Embrava models V30, and BLYNCUSB40S-181\nUSB connected lights.\n\n\nInstall\n-------\n\n0. Install `hidapi`_ for your platform:\n\n.. code:: bash\n\n          (rpm Linux distros)# yum install XXXX\n          (apt Linux distros)# apt-get install XXXX\n          (macOS using brew) $ brew install hidapi\n\n1. pip\n\n.. code:: bash\n\n\t  $ python3 -m pip install blynclight\n\t  $ python3 -m pip install git+https://github.com/JnyJny/blynclight.git\n\n2. Install the Cloned Repository\n\n.. code:: bash\n\n\t  $ git clone https://github.com/JnyJny/blynclight.git\n\t  $ cd blynclight\n\t  $ python3 -m pip install .\n\t  \n\n\nDevelopment\n-----------\n\n.. code:: bash\n\n\t  $ pip install poetry\n\t  $ git clone https://github.com/JnyJny/blynclight.git\n\t  $ cd blynclight\n\t  $ poetry shell\n\t  $ ..\n\t  \n\nUninstall\n---------\n\n.. code:: bash\n\n\t  $ python3 -m pip uninstall blynclight\n\n\n\nUsage\n-----\n\nOnce installed, the BlyncLight is yours to command!\n\n.. code:: python\n\n\tfrom blynclight import BlyncLight\n\n\tlight = BlyncLight.get_light()\n\n\tred, blue, green = (255, 0, 0), (0, 255, 0), (0, 0, 255)\n\n\tlight.color = green           # the light is off and green\n\tlight.on = True               # the light is on and green\n\tlight.flash = True            # the light is on, flashing and green\n\tlight.color = red             # the light is on, flashing and red\n\tlight.flash = False           # the light is on and red\n\tlight.bright = False          # the light is on, dim and red\n\tlight.color = blue            # the light is on, dim and blue\n\tlight.bright = True           # the light is on and blue\n\tlight.on = False              # the light is off and blue\n\n\nSeveral command line interfaces are provided when blynclight is installed:\n\n- blync\n    Provides command-line access to all light attributes.\n\n- fli\n    Flashes the light.. impressively.\n\n- rainbow\n    Smoothly transitions the color of the light in a rainbow pattern.\n\n- throbber\n    Menacingly ramps the color intensity and then recedes. Over and over again.\n\n.. |pypi| image:: https://img.shields.io/pypi/v/blynclight.svg?style=flat-square&label=version\n    :target: https://pypi.org/pypi/blynclight\n    :alt: Latest version released on PyPi\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/blynclight.svg?style=flat-square\n   :target: https://pypi.org/project/blynclight/\n   :alt: Python Versions\n\n.. |license| image:: https://img.shields.io/badge/license-apache-blue.svg?style=flat-square\n    :target: https://github.com/erikoshaughnessy/blynclight/blob/master/LICENSE\n    :alt: Apache license version 2.0\n\n.. _Embrava: https://embrava.com\n\n.. _hidapi: https://github.com/signal11/hidapi\n',
    'author': "Erik O'Shaughnessy",
    'author_email': 'erik.oshaughnessy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/JnyJny/blynclight.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
