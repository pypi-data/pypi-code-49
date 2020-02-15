# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohomekit',
 'aiohomekit.controller',
 'aiohomekit.controller.ip',
 'aiohomekit.crypto',
 'aiohomekit.http',
 'aiohomekit.model',
 'aiohomekit.model.characteristics',
 'aiohomekit.model.services',
 'aiohomekit.protocol',
 'aiohomekit.zeroconf']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=2.8,<3.0',
 'ed25519>=1.5,<2.0',
 'hkdf>=0.0.3,<0.0.4',
 'zeroconf[IP]>=0.24.4,<0.25.0']

setup_kwargs = {
    'name': 'aiohomekit',
    'version': '0.2.8',
    'description': 'An asyncio HomeKit client',
    'long_description': "# aiohomekit\n\n[![Build Status](https://travis-ci.com/Jc2k/aiohomekit.svg?branch=master)](https://travis-ci.com/Jc2k/aiohomekit)  | [![codecov](https://codecov.io/gh/Jc2k/aiohomekit/branch/master/graph/badge.svg)](https://codecov.io/gh/Jc2k/aiohomekit)\n\nThis library implements the HomeKit protocol for controlling Homekit accessories using asyncio.\n\nIt's primary use is for with Home Assistant. We target the same versions of python as them and try to follow their code standards.\n\nAt the moment we don't offer any API guarantees. API stability and documentation will happen after we are happy with how things are working within Home Assistant.\n\n\n## FAQ\n\n### How do I use this?\n\nIt's published on pypi as `aiohomekit` but its still under early development - proceed with caution.\n\n### Does this support BLE accessories?\n\nNo. Eventually we hope to via aioble which provides an asyncio bluetooth abstraction that works on Linux, macOS and Windows.\n\n### Can i use this to make a homekit accessory?\n\nNo, this is just the client part. You should use one the of other implementations:\n\n * [homekit_python](https://github.com/jlusiardi/homekit_python/)\n * [HAP-python](https://github.com/ikalchev/HAP-python)\n\n\n### Why don't you use library X instead?\n\nAt the time of writing this is the only python 3.7/3.8 asyncio HAP client.\n\n\n## Thanks\n\nThis library wouldn't have been possible without homekit_python, a synchronous implementation of both the client and server parts of HAP. \n",
    'author': 'John Carr',
    'author_email': 'john.carr@unrouted.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Jc2k/aiohomekit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
