# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awscli_plugin_yubikeytotp']

package_data = \
{'': ['*']}

install_requires = \
['botocore>=1.14.14,<2.0.0']

setup_kwargs = {
    'name': 'awscli-plugin-yubikeytotp',
    'version': '0.1.1.dev1',
    'description': '',
    'long_description': "[![PyPI version fury.io](https://badge.fury.io/py/awscli-plugin-yubikeytotp.svg)](https://pypi.python.org/pypi/awscli-plugin-yubikeytotp/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\n# Yubikey authentication for AWS CLI (and boto) made easy\n\nThis plugin enables aws-cli to directly talk to your [YubiKey](https://www.yubico.com/)\nto acquire an OATH-TOTP code using the YubiKey's CCID application.\n\nCurrently, FIDO-U2F is unsupported on both, [botocore](https://github.com/aws/aws-cli/issues/3607)\nand [aws-cli](https://github.com/aws/aws-cli/issues/3607).\nUsing aws-cli with roles and a regular OATH-TOTP token at least prompts you for\nthe TOTP code but this is quite cumbersome to use with a YubiKey.\n\n\n## Installation\n\n`awscli-plugin-yubikeytotp` can be installed from PyPI:\n```\n$ pip install awscli-plugin-yubikeytotp\n```\nIt's also possible to install it just for your user in case you don't have\npermission to install packages system-wide:\n```\n$ pip install --user awscli-plugin-yubikeytotp\n```\n\n\n### Configure AWS CLI\nTo enable the plugin, add this to your `~/.aws/config`:\n```\n[plugins]\nyubikeytotp = awscli_plugin_yubikeytotp\n```\nAlso make sure to have your MFA ARN configured for your profile:\n```\n[profile myprofile]\nrole_arn = arn:aws:iam::...\nmfa_serial = arn:aws:iam::...\nsource_profile = default\n```\n\n\n## Usage\n\nJust use the `aws` command with a custom role and the plugin will do the rest:\n```\n$ aws s3 ls --profile myprofile\nGenerating OATH code on YubiKey. You may have to touch your YubiKey to proceed...\nSuccessfully created OATH code.\n2013-07-11 17:08:50 mybucket\n2013-07-24 14:55:44 mybucket2\n```\n\n\n## Acknowledgements\n* Thanks to [@woowa-hsw0](https://github.com/woowa-hsw0) for this\n  [inspiration for this plugin](https://gist.github.com/woowa-hsw0/caa3340e2a7b390dbde81894f73e379d)\n",
    'author': 'Thomas Liebetraut',
    'author_email': 'thomas@tommie-lie.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tommie-lie/awscli-plugin-yubikeytotp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
