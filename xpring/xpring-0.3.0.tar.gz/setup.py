# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xpring', 'xpring.algorithms', 'xpring.proto', 'xpring.proto.v1']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses>=0.6.0,<0.7.0',
 'ecdsa>=0.15.0,<0.16.0',
 'grpcio>=1.24,<2.0',
 'protobuf>=3.0,<4.0',
 'pynacl>=1.3,<2.0',
 'typing_extensions>=3.7,<4.0']

extras_require = \
{'docs': ['sphinx>=1.8,<2.0',
          'sphinx-autobuild>=0.7.1,<0.8.0',
          'sphinx_rtd_theme>=0.4.3,<0.5.0',
          'toml>=0.10.0,<0.11.0'],
 'py': ['fastecdsa>=2.0,<3.0']}

setup_kwargs = {
    'name': 'xpring',
    'version': '0.3.0',
    'description': '',
    'long_description': '.. start-include\n\n======\nxpring\n======\n\nThe Xpring SDK for Python.\n\n.. image:: https://travis-ci.org/thejohnfreeman/xpring-py.svg?branch=master\n   :target: https://travis-ci.org/thejohnfreeman/xpring-py\n   :alt: Build status: Linux and OSX\n\n.. image:: https://ci.appveyor.com/api/projects/status/github/thejohnfreeman/xpring-py?branch=master&svg=true\n   :target: https://ci.appveyor.com/project/thejohnfreeman/xpring-py\n   :alt: Build status: Windows\n\n.. image:: https://readthedocs.org/projects/xpring-py/badge/?version=latest\n   :target: https://xpring-py.readthedocs.io/\n   :alt: Documentation status\n\n.. image:: https://img.shields.io/pypi/v/xpring.svg\n   :target: https://pypi.org/project/xpring/\n   :alt: Latest PyPI version\n\n.. image:: https://img.shields.io/pypi/pyversions/xpring.svg\n   :target: https://pypi.org/project/xpring/\n   :alt: Python versions supported\n\n\nInstall\n=======\n\n.. code-block:: shell\n\n   pip install xpring[py]\n\n\nAPI\n===\n\n------\nWallet\n------\n\nConstruct\n---------\n\nYou can construct a ``Wallet`` from its seed.\nIf you do not have your own wallet yet, you can `generate one with some free\nXRP on the testnet`__.\n\n.. __: https://xrpl.org/xrp-testnet-faucet.html\n\n.. code-block:: python\n\n   import xpring\n\n   seed = \'sEdSKaCy2JT7JaM7v95H9SxkhP9wS2r\'\n   wallet = xpring.Wallet.from_seed(seed)\n   print(wallet.private_key.hex())\n   # b4c4e046826bd26190d09715fc31f4e6a728204eadd112905b08b14b7f15c4f3\n   print(wallet.public_key.hex())\n   # ed01fa53fa5a7e77798f882ece20b1abc00bb358a9e55a202d0d0676bd0ce37a63\n   print(wallet.account_id.hex())\n   # d28b177e48d9a8d057e70f7e464b498367281b98\n   print(wallet.address)\n   # rLUEXYuLiQptky37CqLcm9USQpPiz5rkpD\n\n\nSign / Verify\n-------------\n\nA ``Wallet`` can sign and verify arbitrary bytes, but you\'ll generally\nwant to leave these low-level responsibilities to the ``Client``.\n\n.. code-block:: python\n\n   message = bytes.fromhex(\'DEADBEEF\')\n   signature = wallet.sign(message)\n   wallet.verify(message, signature)\n   # True\n\n\n------\nClient\n------\n\n``Client`` is the gateway to the XRP Ledger.\nIt is constructed with the URL of the gRPC service of a rippled_ server.\nIf you are running the server yourself,\nyou need to configure the ``[port_grpc]`` stanza in your configuration file.\nIn the example_ configuration file, it is commented_ out.\n\n.. _rippled: https://github.com/ripple/rippled\n.. _example: https://github.com/ripple/rippled/blob/develop/cfg/rippled-example.cfg\n.. _commented: https://github.com/ripple/rippled/blob/0c6d380780ae368a2236a2e8e3e42efa4a1d2b46/cfg/rippled-example.cfg#L1181-L1183\n\n.. code-block:: python\n\n   url = \'localhost:50051\'\n   client = xpring.Client.from_url(url)\n\n\nAccount\n-------\n\n.. code-block:: python\n\n   >>> client.get_account(wallet.address)\n   account_data {\n     account {\n       address: "rDuKotkyx18D5WqWCA4mVhRWK2YLqDFKaY"\n     }\n     balance {\n       drops: 999999820\n     }\n     sequence: 10\n     previous_transaction_id: b"..."\n     previous_transaction_ledger_sequence: 4845872\n   }\n   ledger_index: 4869818\n\n\nFee\n---\n\n.. code-block:: python\n\n   >>> client.get_fee()\n   current_ledger_size: 6\n   drops {\n     base_fee {\n       drops: 10\n     }\n     median_fee {\n       drops: 5000\n     }\n     minimum_fee {\n       drops: 10\n     }\n     open_ledger_fee {\n       drops: 10\n     }\n   }\n   expected_ledger_size: 25\n   ledger_current_index: 4869844\n   levels {\n     median_level: 128000\n     minimum_level: 256\n     open_ledger_level: 256\n     reference_level: 256\n   }\n   max_queue_size: 2000\n\n\nSubmit\n------\n\n.. code-block:: python\n\n   >>> unsigned_transaction = {\n   ...     \'Account\': \'rDuKotkyx18D5WqWCA4mVhRWK2YLqDFKaY\',\n   ...     \'Amount\': \'10\',\n   ...     \'Destination\': \'rNJDvXkaBRwJYdeEcx9pchE2SecMkH3FLz\',\n   ...     \'Fee\': \'10\',\n   ...     \'Flags\': 0x80000000,\n   ...     \'Sequence\': 9,\n   ...     \'TransactionType\': \'Payment\'\n   ... }\n   >>> signed_transaction = wallet.sign_transaction(unsigned_transaction)\n   >>> client.submit(signed_transaction)\n   engine_result {\n     result_type: RESULT_TYPE_TES\n     result: "tesSUCCESS"\n   }\n   engine_result_message: "The transaction was applied. Only final in a validated ledger."\n   hash: b"..."\n\n\n.. end-include\n\n\nDevelop\n=======\n\n------------\nDependencies\n------------\n\nThe protocol buffers and definitions file are in submodules:\n\n.. code-block:: shell\n\n   git submodule update --init\n\nUse Poetry_ to install dependencies, build the protocol buffers, and copy the\ndefinitions file:\n\n.. code-block:: shell\n\n   poetry install\n   poetry run invoke prebuild\n\n.. _Poetry: https://python-poetry.org/docs/\n\n-----\nTasks\n-----\n\nThere are several Invoke_ tasks:\n\n.. _Invoke: http://www.pyinvoke.org/\n\n.. code-block:: shell\n\n   poetry run invoke ${task}\n\n- ``test``: Pytest_ with coverage and doctests.\n- ``lint``: Mypy_, Pylint_, and Pydocstyle_.\n- ``serve``: Serve the docs locally and rebuild them on file changes.\n\n.. _Pytest: https://docs.pytest.org/\n.. _Mypy: https://mypy.readthedocs.io/\n.. _Pylint: https://www.pylint.org/\n.. _Pydocstyle: http://www.pydocstyle.org/\n',
    'author': 'John Freeman',
    'author_email': 'jfreeman@ripple.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thejohnfreeman/xpring-py/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
