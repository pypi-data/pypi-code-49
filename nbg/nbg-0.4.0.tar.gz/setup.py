# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nbg', 'nbg.auth', 'nbg.base']

package_data = \
{'': ['*'], 'nbg.auth': ['certs/*']}

install_requires = \
['python-jose[cryptography]>=3.1.0,<4.0.0', 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'nbg',
    'version': '0.4.0',
    'description': 'Official Python SDK for NBG APIs',
    'long_description': '# NBG Python SDK\n\nPython wrapper with unified developer experience for the APIs of the National Bank of Greece.\n\n## Requirements\n\n- Python 3.6 or newer\n\n## Installation\n\n```shell\npoetry add nbg\n```\n\n## API clients\n\nThe National Bank of Greece provides a set of multiple APIs. To use each one of these APIs, you should pick the corresponding client from the `nbg` package.\n\n### Accounts Information PSD2 API\n\n```python\nfrom nbg.account_information import AccountInformationPSD2Client\n\n\n# Step 1 - Set up client and authentication\nclient = nbg.AccountInformationPSD2Client(\n    client_id="your_client_id",\n    client_secret="your_client_secret",\n    production=False,\n)\nclient.set_access_token("access_token_of_your_user")\n\n# Step 2 - Set up a sandbox, when in development\nclient.create_sandbox("sandbox_id")\nclient.set_sandbox("sandbox_id")\n\n# Step 3 - Start working with the Account information API\n\n## Account resource\nclient.accounts("your_user_id")\n```\n',
    'author': 'Paris Kasidiaris',
    'author_email': 'paris@sourcelair.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
