# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autodecrypt']

package_data = \
{'': ['*']}

install_requires = \
['pyquery>=1.4.1,<2.0.0', 'remotezip>=0.9.2,<0.10.0']

entry_points = \
{'console_scripts': ['autodecrypt = autodecrypt.main:main']}

setup_kwargs = {
    'name': 'autodecrypt',
    'version': '2.0.6',
    'description': 'Tool to decrypt iOS firmware images',
    'long_description': '# autodecrypt\n[![PyPI version](https://badge.fury.io/py/autodecrypt.svg)](https://badge.fury.io/py/autodecrypt)\n\nSimple tool to decrypt iOS firmware images.\n\nGoing to the iPhone wiki and copying and pasting firmware keys to your terminal is boring.\n\nautodecrypt will grab keys for you and decrypt the firmware image you want.\n\n## Usage\n```\nusage: autodecrypt.py [-h] -f IMG_FILE -d DEVICE [-i IOS_VERSION]\n                      [-b BUILD_ID] [-c CODENAME] [-l] [--beta] [--download]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -f IMG_FILE, --file IMG_FILE\n                        img file you want to decrypt\n  -d DEVICE, --device DEVICE\n                        device ID (eg : iPhone8,1)\n  -i IOS_VERSION, --ios IOS_VERSION\n                        iOS version for the said file\n  -b BUILD_ID, --build BUILD_ID\n                        build ID to set instead of iOS version\n  -c CODENAME, --codename CODENAME\n                        codename of iOS version\n  -l, --local           don\'t download firmware image\n  --beta                specify beta firmware\n  --download            download firmware image\n```\n\n## Dependencies\n- [img4](https://github.com/xerub/img4lib)\n\nTo run autodecrypt, use poetry with a virtualenv:\n- `virtualenv -p python3 env`\n- `pip3 install poetry`\n- `poetry install`\n\n\n## Installation\n`pip3 install autodecrypt`\n\n\n## Examples\n\n#### Download a decrypt iBSS using keys from theiphonewiki \n```\n» autodecrypt -f iBSS -i 10.3.3 -d iPhone6,2                                                                                                             \n[i] downloading iBSS.iphone6.RELEASE.im4p\n[i] image : ibss\n[i] grabbing keys for iPhone6,2/14G60\n[x] iv  : f2aa35f6e27c409fd57e9b711f416cfe\n[x] key : 599d9b18bc51d93f2385fa4e83539a2eec955fce5f4ae960b252583fcbebfe75\n[i] decrypting iBSS.iphone6.RELEASE.im4p to iBSS.iphone6.RELEASE.im4p.dec...\n[x] done\n```\n\n#### Download and decrypt SEP firmware by specifying keys\n```\n» autodecrypt -f sep-firmware -b 17C5053a -d iPhone11,8 -k 9f974f1788e615700fec73006cc2e6b533b0c6c2b8cf653bdbd347bc1897bdd66b11815f036e94c951250c4dda916c00\n[i] downloading sep-firmware.n841.RELEASE.im4p\n[x] iv  : 9f974f1788e615700fec73006cc2e6b5\n[x] key : 33b0c6c2b8cf653bdbd347bc1897bdd66b11815f036e94c951250c4dda916c00\n[i] decrypting sep-firmware.n841.RELEASE.im4p to sep-firmware.n841.RELEASE.im4p.dec...\n[x] done\n```\n\n#### Use [foreman](https://github.com/GuardianFirewall/foreman) instance to grab firmware keys \n```\n» export FOREMAN_HOST="https://foreman-public.sudosecuritygroup.com"\n» autodecrypt -f LLB -i 13.2.3 -d iPod9,1                           \n[i] downloading LLB.n112.RELEASE.im4p\n[i] image : llb\n[i] grabbing keys for iPod9,1/17B111\n[i] grabbing keys from https://foreman-public.sudosecuritygroup.com\n[x] iv  : 85784a219eb29bcb1cc862de00a590e7\n[x] key : f539c51a7f3403d90c9bdc62490f6b5dab4318f4633269ce3fbbe855b33a4bc7\n[i] decrypting LLB.n112.RELEASE.im4p to LLB.n112.RELEASE.im4p.dec...\n[x] done\n```\n\n#### Log\n\nFor debugging purposes you can check `autodecrypt.log` :\n```\n11/02/2019 21:39:41 Launching "[\'autodecrypt/autodecrypt.py\', \'-d\', \'iPhone9,3\', \'-f\', \'iBoot\', \'-i\', \'12.3.1\']"\n11/02/2019 21:39:41 requesting IPSW\'s API for iPhone9,3\n11/02/2019 21:39:41 done, now looking for version or build\n11/02/2019 21:39:41 grabbing firmware codename for 16F203\n11/02/2019 21:39:42 codename : PeaceF\n11/02/2019 21:39:42 grabbing IPSW file URL for iPhone9,3/12.3.1\n11/02/2019 21:39:42 downloading iBoot...\n11/02/2019 21:39:43 img4 -i iBoot.d10.RELEASE.im4p iBoot.d10.RELEASE.im4p.dec 978fd4680cd4b624b0dfea22a417f51f0ee2b871defed42277fe18885053b1eb5c7ffe82f38ab8cf7772c69a0db5d386\n```\n\n### Credits\n- kennytm for img3 stuff (removed for the moment)\n- xerub for [img4](https://github.com/xerub/img4lib)\n- tihmstar for wiki parsing ([my method](https://github.com/matteyeux/ios-tools/blob/master/scrapkeys.py) was pretty bad)\n',
    'author': 'matteyeux',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/matteyeux/autodecrypt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
