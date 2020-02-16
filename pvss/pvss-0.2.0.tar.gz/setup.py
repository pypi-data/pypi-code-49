# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pvss']

package_data = \
{'': ['*']}

install_requires = \
['asn1crypto>=1.3.0,<2.0.0', 'click>=7.0,<8.0', 'lazy>=1.4,<2.0']

extras_require = \
{'docs': ['sphinx>=2.4,<3.0', 'sphinx-rtd-theme>=0.4,<0.5']}

entry_points = \
{'console_scripts': ['pvss = pvss.cli:cli']}

setup_kwargs = {
    'name': 'pvss',
    'version': '0.2.0',
    'description': 'Public Verifiable Secret Splitting in Python',
    'long_description': "Publicly Verifiable Secret Splitting in python\n==============================================\nThis project is a python (>= 3.7) implementation (library and CLI) of\n`Publicly Verifiable Secret Splitting (PVSS)\n<https://en.wikipedia.org/wiki/Publicly_Verifiable_Secret_Sharing>`_.\n\nPVSS is a non-interactive cryptographic protocol between multiple participants\nfor splitting a random secret into multiple shares and distributing them amongst a\ngroup of users.  An arbitrary subset of those users (e.g. any 3 out of 5) can\nlater cooperate to reassemble the secret.\n\nThe common use case for secret splitting is to create a highly durable backup of\nhighly sensitive data such as cryptographic keys.\n\nAll communication between the participants is public and everyone can verify\nthat all messages have been correctly created according to the protocol. This\nverification is done through `non-interactive zero-knowledge proofs\n<https://en.wikipedia.org/wiki/Non-interactive_zero-knowledge_proof>`_.\n\nThe math is based upon the paper `Non-Interactive and Information-Theoretic\nSecure Publicly Verifiable Secret Sharing <https://eprint.iacr.org/2004/201.ps>`_\nby *Chunming Tang* et al. who extended *Berry Schoenmaker*'s paper\n`A Simple Publicly Verifiable Secret Sharing Scheme and its Application to Electronic Voting\n<https://www.win.tue.nl/~berry/papers/crypto99.pdf>`_ which in turn is based on\n`Shamir's Secret Sharing <https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing>`_.\n\nOne notable difference to prior work is the addition of a receiver user:\nIn their scheme the secret is made public while it is being reassembled, which\nviolates the goal to keep the secret secret. To address this issue, the users no longer\ndisclose their share of the secret but use `ElGamal encryption\n<https://en.wikipedia.org/wiki/ElGamal_encryption>`_ to securely convey the share to a\nseparate receiver user who will then reassemble the secret. Like all other communication,\nthe encrypted share is public and it can be verified that the users followed the protocol.\n\nDocumentation\n-------------\nFull documentation can be found at https://pvss.1e8.de/.\n\nInstallation\n------------\n``PVSS``'s dependencies are:\n\n* python (>= 3.7)\n* At least one of:\n    + `libsodium <https://libsodium.org/>`_ (>= 1.0.18, recommended, for `Ristretto255 <https://ristretto.group/>`_ group)\n\n      On Debian (Bullseye / 11 and later) or Ubuntu (Eoan / 19.10 and later):\n\n      .. code-block:: console\n\n          # apt install libsodium23\n\n    + `gmpy2 <https://pypi.org/project/gmpy2/>`_ (Group of quadratic residues modulo a large safe prime)\n\nYou can install ``PVSS`` with ``pip``:\n\n.. code-block:: console\n\n    $ pip install pvss\n\nAnd optionally:\n\n.. code-block:: console\n\n    $ pip install gmpy2\n\n\nExample\n-------\nThe following sequence of shell commands is executed by six different users who\nshare a data directory. E.g. use git to synchronize it between the users. All\nfiles inside ``datadir`` are public. All files outside of it are private.\n\n.. code-block:: console\n\n    (init)     $ pvss datadir genparams rst255 \n    (alice)    $ pvss datadir genuser Alice alice.key \n    (boris)    $ pvss datadir genuser Boris boris.key \n    (chris)    $ pvss datadir genuser Chris chris.key \n    (dealer)   $ pvss datadir splitsecret 2 secret0.der \n    (receiver) $ pvss datadir genreceiver recv.key \n    (boris)    $ pvss datadir reencrypt boris.key \n    (alice)    $ pvss datadir reencrypt alice.key \n    (receiver) $ pvss datadir reconstruct recv.key secret1.der \n\n``secret0.der`` and ``secret1.der`` should compare equal.\nThe *dealer* and *receiver* can encrypt an actual payload by using that file as a shared key.\n",
    'author': 'Jörn Heissler',
    'author_email': 'nosuchaddress@joern.heissler.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joernheissler/pvss',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
