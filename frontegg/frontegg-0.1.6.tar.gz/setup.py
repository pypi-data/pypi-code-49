# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['frontegg']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=0.15.5,<0.16.0', 'requests>=2.22.0,<3.0.0']

extras_require = \
{'flask': ['flask>=1.0,<2.0']}

setup_kwargs = {
    'name': 'frontegg',
    'version': '0.1.6',
    'description': 'Frontegg is a web platform where SaaS companies can set up their fully managed, scalable and brand aware - SaaS features and integrate them into their SaaS portals in up to 5 lines of code.',
    'long_description': '.. image:: https://fronteggstuff.blob.core.windows.net/frongegg-logos/logo-transparent.png\n   :alt: Frontegg\n\nFrontegg is a web platform where SaaS companies can set up their fully managed, scalable and brand aware - SaaS features and integrate them into their SaaS portals in up to 5 lines of code.\n\nInstallation\n------------\n\nYou can install this library by using pip::\n\n    pip install frontegg\n\nIf you\'d like to use Frontegg in your flask project use the flask extra dependency::\n\n    pip install frontegg[flask]\n\nUsage\n-----\n\nYou can directly use the Frontegg REST client to access your data when you need to.\nThe raw client directly returns a `requests.Response`.\n\nThis is useful in Python scripts or in cases where you need to access the data from the server side:\n\n.. code-block:: pycon\n\n    >>> from frontegg import FronteggRESTClient\n    >>> client = FronteggRESTClient(\'your-client-id\', \'your-client-secret\')\n    >>> response = client.request(\'/metadata\', \'GET\', params={\'entityName\': \'audits\'})\n    >>> print(response.json())\n    {\'rows\': [{\'_id\': \'5d3d2ee54a04a50033da91df\', \'entityName\': \'audits\', \'properties\': [\n        {\'_id\': \'5d3d2ee54a04a50033da91e6\', \'name\': \'createdAt\', \'displayName\': \'Date\', \'type\': \'Timestamp\',\n         \'filterable\': True, \'sortable\': True},\n        {\'_id\': \'5d3d2ee54a04a50033da91e5\', \'name\': \'user\', \'displayName\': \'User\', \'type\': \'UserIdentity\',\n         \'filterable\': True, \'sortable\': True},\n        {\'_id\': \'5d3d2ee54a04a50033da91e4\', \'name\': \'resource\', \'displayName\': \'Resource\', \'type\': \'AlphaNumeric\',\n         \'filterable\': True, \'sortable\': True},\n        {\'_id\': \'5d3d2ee54a04a50033da91e3\', \'name\': \'action\', \'displayName\': \'Action\', \'type\': \'AlphaNumeric\',\n         \'filterable\': True, \'sortable\': True}, {\n            \'_id\': \'5d3d2ee54a04a50033da91e2\', \'name\': \'severity\', \'displayName\': \'Severity\', \'type\': \'AlphaNumeric\',\n            \'filterable\': True, \'sortable\': True},\n        {\'_id\': \'5d3d2ee54a04a50033da91e1\', \'name\': \'ip\', \'displayName\': \'IP Address\', \'type\': \'AlphaNumeric\',\n         \'filterable\': True, \'sortable\': True},\n        {\'_id\': \'5d3d2ee54a04a50033da91e0\', \'name\': \'message\', \'displayName\': \'Message\', \'type\': \'AlphaNumeric\',\n         \'filterable\': True, \'sortable\': False}], \'vendorId\': \'2fb835d0-8f17-48cb-8489-3a2f8f50ce4a\',\n                          \'id\': \'39372f0f-1d14-4ecd-8462-1b22d5ca9264\', \'createdAt\': \'2019-07-28T05:13:09.723Z\',\n                          \'updatedAt\': \'2019-07-28T05:13:09.723Z\', \'__v\': 0}]}\n\nYou can pass a context callback to provide the user id and the tenant id that are relevant to the request:\n\n.. code-block:: pycon\n\n    >>> from frontegg import FronteggRESTClient, FronteggContext\n    >>> client = FronteggRESTClient(\'your-client-id\', \'your-client-secret\', context_callback=lambda request: FronteggContext(\'user_id@user.com\', \'tenant-id\'))\n    >>> response = client.request(\'/audits/stats\', \'GET\')\n    >>> print(response.json())\n    {\'totalToday\': 2, \'severeThisWeek\': 0}\n\nHigher Level Client\n~~~~~~~~~~~~~~~~~~~\n\nYou can access the audits API directly using the `FronteggClient`:\n\n.. code-block:: pycon\n\n    >>> from frontegg import FronteggClient\n    >>> client = FronteggClient(\'your-client-id\', \'your-client-secret\')\n    >>> client.send_audits({"username": "test", "severity": "Info"}, tenantId=\'my-tenant-id\')\n\nProxying Requests From Other Clients\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nThe browser and possibly other clients in your architecture need to access Frontegg from your proxy\nas it determines the context of the request.\n\nThis package currently only supports doing so from Flask. In the future, more frameworks may be added.\n\nFlask\n+++++\n\nTo proxy requests to Frontegg in your Flask application the following configuration must be provided:\n\n.. code-block:: python\n\n    from flask import Flask\n    app = Flask(\'example\')\n    app.config[\'FRONTEGG_CLIENT_ID\'] = \'your client id\'\n    app.config[\'FRONTEGG_API_KEY\'] = \'your api key\'\n\nYou can optionally provide the context callback as a configuration setting as well:\n\n.. code-block:: python\n\n    from frontegg import FronteggContext\n    app.config[\'FRONTEGG_CONTEXT_RESOLVER\'] = lambda request: FronteggContext(\'user_id@user.com\', \'my-tenant-id\')\n\nThe request argument will be filled with the `flask.request` object.\nYou can use it to determine the user id and the tenant id.\n\nIn addition, different users may or may not access specific data and thus have different permissions.\nYou can use the `frontegg.FronteggPermissions` enum to limit access to your data.\n\n.. code-block:: python\n\n    from frontegg import FronteggContext, FronteggPermissions\n\n    def context_resolver(request):\n        if is_admin_user(request):\n            permissions = (FronteggPermissions.All,)\n        else:\n            permissions = (FronteggPermissions.Teams.value.Read,)\n\n        return FronteggContext(\'user_id@user.com\', \'my-tenant-id\', permissions=permissions)\n\n\nTo begin proxying requests you should\n\n.. code-block:: python\n\n    from flask import Flask\n    from frontegg import FronteggContext\n    from frontegg.flask import Frontegg\n    app = Flask(\'example\')\n    app.config[\'FRONTEGG_CLIENT_ID\'] = \'your client id\'\n    app.config[\'FRONTEGG_API_KEY\'] = \'your api key\'\n    app.config[\'FRONTEGG_CONTEXT_RESOLVER\'] = lambda request: FronteggContext(\'user_id@user.com\', \'my-tenant-id\')\n    frontegg = Frontegg(app)\n\nYou can use the Frontegg object as a higher level client as well.\n',
    'author': 'Frontegg LTD',
    'author_email': 'hello@frontegg.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://frontegg.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
