# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linuxinfo']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'linuxinfo',
    'version': '0.1.0',
    'description': 'A python library to get linux/raspberry pi info',
    'long_description': '# Linux Information\n\n**work in progress**\n\nAnswers:\n\n- is this a raspberry pi?\n    - functions return `None` on error\n- is this a raspbian or ubuntu distro?\n- is this distro based on debian?\n- reads `/proc/cpuinfo` for revision code\n- reads `/etc/os-release` for linux OS info\n\n## Info\n\nReads the [revision code](https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md)\nwhich encodes a bunch of information as `uuuuuuuuFMMMCCCCPPPPTTTTTTTTRRRR`. This library\ndecodes that number.\n\n```python\nRPiInfo = namedtuple("RPiInfo", "type processor memory revision manufacturer flag")\nLinuxInfo = namedtuple("LinuxInfo", "distro distro_pretty debian_based version version_codename")\n```\n\n## Example\n\n```python\nfrom linuxinfo import linux_info()\nfrom linuxinfo import pi_info\nfrom linuxinfo import RPiInfo, LinuxInfo  # not sure you need these\nfrom linuxinfo.rpi import decode          # normally you don\'t use this!\n\n# given a revision code, it decodes it (see below). Normally you\n# wouldn\'t do this ... this is just a test\nprint(decode(0xa020a0))  # compute module 3\nprint(decode(0xa22042))  # Pi2B\nprint(decode(0xc03111))  # Pi4B\n\nprint(pi_info())  # reads /proc/cpuinfo and get revision code\n```\n\n```\nRPiInfo(type=\'CM3\', processor=\'BCM2837\', memory=\'1GB\', revision=0, manufacturer=\'Sony UK\', flag=\'new-style revision\')\nRPiInfo(type=\'2B\', processor=\'BCM2837\', memory=\'1GB\', revision=2, manufacturer=\'Embest\', flag=\'new-style revision\')\nRPiInfo(type=\'4B\', processor=\'BCM2711\', memory=\'4GB\', revision=1, manufacturer=\'Sony UK\', flag=\'new-style revision\')\n```\n\n# Change Log\n\n| Date        | Version | Notes      |\n|-------------|---------|------------|\n| 2020 Dec 4  | 0.1.0   | changed name because it does more |\n| 2019 Oct 27 | 0.0.3   | simple clean up |\n| 2019 Oct 27 | 0.0.1   | init            |\n\n\n# MIT License\n\n**Copyright (c) 2019 Kevin J. Walchko**\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/linuxinfo/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
