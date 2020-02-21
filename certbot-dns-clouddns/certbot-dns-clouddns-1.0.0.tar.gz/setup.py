# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['certbot_dns_clouddns']

package_data = \
{'': ['*']}

install_requires = \
['acme>=0.29.0,<0.30.0', 'certbot>=0.34.0,<0.35.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'certbot.plugins': ['dns-clouddns = '
                     'certbot_dns_clouddns.dns_clouddns:Authenticator']}

setup_kwargs = {
    'name': 'certbot-dns-clouddns',
    'version': '1.0.0',
    'description': 'CloudDNS Authenticator plugin for Certbot',
    'long_description': None,
    'author': 'Radek SPRTA',
    'author_email': 'sprta@vshosting.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vshosting/certbot-dns-clouddns',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
