# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auri']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'jsonschema>=3.2.0,<4.0.0',
 'pillow>=7.0.0,<8.0.0',
 'psutil>=5.6.7,<6.0.0',
 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['auri = auri.command_line:cli']}

setup_kwargs = {
    'name': 'auri',
    'version': '1.3.4',
    'description': 'CLI to control Nanoleaf Aurora devices',
    'long_description': '# Auri - Nanoleaf Aurora CLI [![Build Status](https://travis-ci.org/MrTrustworthy/auri.svg?branch=master)](https://travis-ci.org/MrTrustworthy/auri)\n\nA simple, light-weight tool for controlling multiple Aurora devices from the CLI. Supports the most important functionality of the Nanoleaf app (registering new devices, switching effects, changing brightness, on/off,...) as well as an Ambilight feature that is based on the colors of your main display.\n\n\n## Usage \n\n![Auri Gif Sample](https://raw.githubusercontent.com/MrTrustworthy/auri/master/preview.gif)\n\n### Installation\n\nAs it\'s a Python3-based application, you can install the CLI simply via `pip`. `pip install auri` or `python3 -m pip install auri` (if your default pip is for Python2) are both acceptable ways of installing.\n\n### Device management and setup\n\nTo find and generate credentials for the Nanoleaf Aurora device in your home, make sure your PC/Laptop is in the same network and run `auri device setup`. Auri will then guide you through the setup for each device it can find and allow you to set a name for each device in your home. Auri saves the device data and access tokens in a small file in your application config folder, so you only have to do this once. \n\nYou can switch the currently active device by running `auri device activate <device name>`. In general, all commands will only affect the currently active device. If you want a command to apply to a different device, either `auri device activate` it or target a specific device like `auri -a <device name> play Flames`.\n\n### Playing and changing effects\n\nSwitching effects is done via `auri play`, like `auri play rain`. There is a best-effort spelling correction to find the effect you meant even if you mistype or only provide a part of the effect name. The most common operations are easily accessible, for example `on`, `off`, `brighter` and `darker` will do exactly what you\'d expect. `auri list` will show you all available effects including a small color preview in the terminal.\n\n\n### Ambilight\n\nThere is a built-in ambilight functionality that is based on your primary display. Use `auri ambi` to toggle the _ambi_ mode that will update the effect each seconds. It needs to create a new effect on the device to do so, which will be called `AuriAmbi` so you know what it is.\n\nYou can customize the behaviour of the ambilight, just check your config file (see "Device management and setup") to see which parameters you can play with, though the default settings should work quite nicely without any tuning. The Ambilight functionality only works on MacOS and Windows, but not on Linux due to the dependency on `ImageGrab`. If you\'re using Linux and know of a way to get this working, feel free to shoot me a PR.\n\n### Alfred Integration\n\nIf you\'re on MacOS, you can also use this CLI to easily build a [Alfred](https://www.alfredapp.com/) workflow to change effects and have preview images for each effect in your search bar. Simply run `auri alfred images` to generate some preview images for all your effects, then create a simple workflow that has `auri alfred prompt` as a script filter and pipes the result to `auri alfred command` as a "run script" action.\n\n## Contributing\n\nIn case you want new features, feel free to implement them and shoot me a PR. The codebase is small and pretty easy to understand, and in case you\'re missing a feature it\'s probably not because it\'s hard to implement but because I didn\'t think of it.\n\n## Acknowledgements\n\nSome of the code has been (in altered form) taken from [Anthony Brians GitHub Project "Nanoleaf"](https://github.com/software-2/nanoleaf). Thanks for figuring out the device discovery Anthony!\n',
    'author': 'MrTrustworthy',
    'author_email': 'tinywritingmakesmailhardtoread@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MrTrustworthy/auri',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
