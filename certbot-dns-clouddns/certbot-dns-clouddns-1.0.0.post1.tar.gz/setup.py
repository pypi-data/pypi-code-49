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
    'version': '1.0.0.post1',
    'description': 'CloudDNS Authenticator plugin for Certbot',
    'long_description': 'certbot-dns-clouddns\n====================\n\nThe `~certbot_dns_clouddns.dns_clouddns` plugin automates the process of\ncompleting a ``dns-01`` challenge (`~acme.challenges.DNS01`) by creating, and\nsubsequently removing, TXT records using the CloudDNS_ REST API.\n\n.. _CloudDNS: https://github.com/vshosting/clouddns\n\n\nNamed Arguments\n---------------\n\n===========================================================  =====================================\n``--authenticator certbot-dns-clouddns:dns-clouddns``        Select the plugin. (Required)\n``--certbot-dns-clouddns:dns-clouddns-credentials``          CloudDNS Remote API credentials_\n                                                             INI file. (Required)\n``--certbot-dns-clouddns:dns-clouddns-propagation-seconds``  The number of seconds to wait for DNS\n                                                             to propagate before asking the ACME\n                                                             server to verify the DNS record.\n                                                             (Default: 60)\n===========================================================  =====================================\n\n\nInstallation\n------------\n\n``certbot-dns-clouddns`` requires Python 2.7 or 3.5+ to run.\n\n.. code:: bash\n\n   pip install certbot-dns-clouddns\n\n\nCredentials\n-----------\n\nUse of this plugin requires a configuration file containing CloudDNS Remote API\n.\n\nExample credentials file:\n\n.. code:: ini\n\n   # CloudDNS API credentials used by Certbot\n   certbot-dns-clouddns:dns_clouddns_clientip = myclientid\n   certbot-dns-clouddns:dns_clouddns_email = myemailaddress\n   certbot-dns-clouddns:dns_clouddns_password = mysecretpassword\n\nThe path to this file can be provided interactively or using the\n``--certbot-dns-clouddns:dns-clouddns-credentials`` command-line argument.\nCertbot records the path to this file for use during renewal, but does not store\nthe file\'s contents.\n\n**Caution**\n\n   You should protect these API credentials as you would a password. Users who\n   can read this file can use these to issue arbitrary CloudDNS API calls on\n   your behalf. Users who can cause Certbot to run using these credentials can\n   complete a ``dns-01`` challenge to acquire new certificates or revoke\n   existing certificates for associated domains, even if those domains aren\'t\n   being managed by this server.\n\nCertbot will emit a warning if it detects that the credentials file can be\naccessed by other users on your system. The warning reads "Unsafe permissions\non credentials configuration file", followed by the path to the credentials\nfile. This warning will be emitted each time Certbot uses the credentials file,\nincluding for renewal, and cannot be silenced except by addressing the issue\n(e.g., by using a command like ``chmod 600`` to restrict access to the file).\n\n\nExamples\n--------\n\nTo acquire a certificate for ``example.com``\n\n.. code:: bash\n\n   certbot certonly \\\n     --authenticator certbot-dns-clouddns:dns-clouddns \\\n     --certbot-dns-clouddns:dns-clouddns-credentials ~/.secrets/certbot/clouddns.ini \\\n     -d example.com\n\nTo acquire a single certificate for both ``example.com`` and ``*.example.com``\n\n.. code:: bash\n\n   certbot certonly \\\n     --authenticator certbot-dns-clouddns:dns-clouddns \\\n     --certbot-dns-clouddns:dns-clouddns-credentials ~/.secrets/certbot/clouddns.ini \\\n     -d example.com \\\n     -d \'*.example.com\'\n\nTo acquire a certificate for ``example.com``, waiting 240 seconds for DNS propagation\n\n.. code:: bash\n\n   certbot certonly \\\n     --authenticator certbot-dns-clouddns:dns-clouddns \\\n     --certbot-dns-clouddns:dns-clouddns-credentials ~/.secrets/certbot/clouddns.ini \\\n     --certbot-dns-clouddns:dns-clouddns-propagation-seconds 240 \\\n     -d example.com\n',
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
