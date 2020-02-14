# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tankersdk_identity', 'tankersdk_identity.crypto', 'tankersdk_identity.test']

package_data = \
{'': ['*']}

install_requires = \
['PyNacl>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'tankersdk-identity',
    'version': '1.3.2',
    'description': 'Tanker identity library',
    'long_description': 'Identity SDK\n============\n\nTanker identity generation in Python for the `Tanker SDK <https://tanker.io/docs/latest>`_.\n\n.. image:: https://github.com/TankerHQ/identity-python/workflows/Tests/badge.svg\n    :target: https://github.com/TankerHQ/identity-python/actions\n\n.. image:: https://img.shields.io/pypi/v/tankersdk_identity.svg\n    :target: https://pypi.org/project/tankersdk_identity\n\n.. image:: https://img.shields.io/codecov/c/github/TankerHQ/identity-python.svg?label=Coverage\n    :target: https://codecov.io/gh/TankerHQ/identity-python\n\n\nInstallation\n------------\n\n\nWith `pip`:\n\n.. code-block:: console\n\n    $ pip install tankersdk-identity\n\n\nAPI\n---\n\n\n.. code-block:: python\n\n    tankersdk_identity.create_identity(app_id, app_secret, user_id)\n\nCreate a new Tanker identity. This identity is secret and must only be given to a user who has been authenticated by your application. This identity is used by the Tanker client SDK to open a Tanker session\n\n**app_id**\n   The app ID. You can access it from the `Tanker dashboard <https://dashboard.tanker.io>`_.\n\n**app_secret**\n   The app secret. A secret that you have saved right after the creation of your app.\n**user_id**\n   The ID of a user in your application.\n\n.. code-block:: python\n\n    tankersdk_identity.create_provisional_identity(app_id, email)\n\nCreate a Tanker provisional identity. It allows you to share a resource with a user who does not have an account in your application yet.\n\n**app_id**\n   The app ID. You can access it from the `Tanker dashboard <https://dashboard.tanker.io>`_.\n\n**email**\n   The email of the potential recipient of the resource.\n\n.. code-block:: python\n\n    tankersdk_identity.get_public_identity(identity)\n\nReturn the public identity from an identity. This public identity can be used by the Tanker client SDK to share encrypted resource.\n\n**identity**\n   A secret identity.\n\n\nGoing further\n-------------\n\n\nRead more about identities in the `Tanker guide <https://tanker.io/docs/latest/guide/server/>`_.\n\nCheck the `examples <https://github.com/TankerHQ/identity-python/tree/master/examples>`_ folder for usage examples.\n',
    'author': 'Tanker team',
    'author_email': 'tech@tanker.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TankerHQ/identity-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
