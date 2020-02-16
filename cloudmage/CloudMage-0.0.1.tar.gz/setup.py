# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudmage']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['CloudMage = cloudmage.CloudMage']}

setup_kwargs = {
    'name': 'cloudmage',
    'version': '0.0.1',
    'description': 'Cloud Simplifaction and Automation Magic.',
    'long_description': '# CloudMage Python3 Utility Package\n\n<br>\n\n![CloudMage](https://github.com/TheCloudMage/Common-Images/raw/master/cloudmage/cloudmage-glow-banner.png)\n\n<br><br>\n\n## Changelog\n\nTo view the project changelog see: [ChangeLog:](CHANGELOG.md)\n\n<br><br>\n\n## ![TheCloudMage](https://github.com/TheCloudMage/Common-Images/raw/master/cloudmage/cloudmage-profile.png) &nbsp;&nbsp;Contacts and Contributions\n\nThis project is owned and maintained by: [@rnason](https://github.com/rnason)\n\n<br>\n\nTo contribute, please:\n\n* Fork the project\n* Create a local branch\n* Submit Changes\n* Create A Pull Request\n',
    'author': 'Rich Nason',
    'author_email': 'rnason@cloudmage.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TheCloudMage/PyPkgs-JinjaUtils',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
