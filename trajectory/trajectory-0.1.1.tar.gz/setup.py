# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trajectory']

package_data = \
{'': ['*']}

install_requires = \
['six>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'trajectory',
    'version': '0.1.1',
    'description': "Trajectory data lossy compression format based on Google's Encoded Polyline Algorithm Format",
    'long_description': ".. image:: https://github.com/adonmo/trajectory/workflows/Tests/badge.svg\n   :target: https://github.com/adonmo/trajectory/actions\n   :alt: Test Status\n\n.. image:: https://img.shields.io/pypi/dm/trajectory.svg\n   :target: https://pypistats.org/packages/trajectory\n   :alt: PyPI downloads\n\n.. image:: https://img.shields.io/github/license/adonmo/trajectory.svg\n   :target: https://github.com/adonmo/trajectory/blob/master/LICENSE\n   :alt: MIT License\n\ntrajectory\n============\n\n``trajectory`` is a library for lossy compression of trajectory data based on Google's Encoded Polyline Algorithm Format (http://goo.gl/PvXf8Y). It is heavily based on (in fact forked from) https://github.com/hicsail/polyline.\n\nInstallation\n============\n\n``trajectory`` can be installed using ``pip`` or ``easy_install``\n\n.. code-block:: sh\n\n    $ pip install trajectory\n    or\n    $ easy_install trajectory\n\nAPI Documentation\n=================\n\nEncoding\n--------\n\nTo serialize a trajectory (set of (lat, lon, unix time in seconds) tuples)\n\n.. code-block:: py\n\n    import trajectory\n    trajectory.encode([\n        (38.500, -120.200, 1582482601),\n        (40.700, -120.950, 1582482611),\n        (43.252, -126.453, 1582482627)\n    ], 5)\n\nThis should return ``_p~iF~ps|U_ynpijgz~G_ulLnnqC_c`|@_mqNvxq`@__t`B``.\n\nYou can set the required precision with the optional ``precision`` parameter. The default value is 5.\n\nDecoding\n--------\n\nTo deserialize a trajectory (set of (lat, lon, unix time in seconds) tuples) represented by an encoded string\n\n.. code-block:: py\n\n    import trajectory\n    trajectory.decode('_p~iF~ps|U_ynpijgz~G_ulLnnqC_c`|@_mqNvxq`@__t`B', 5)\n\nThis should return the following:\n\n.. code-block:: py\n\n    [\n        (38.500, -120.200, 1582482601),\n        (40.700, -120.950, 1582482611),\n        (43.252, -126.453, 1582482627)\n    ]\n\nYou can set the required precision with the optional ``precision`` parameter. The default value is 5.\n\n\nDevelopment\n===========\n\nSetup Dependencies\n------------------\n\n.. code-block:: sh\n\n    $ poetry install\n\nRunning Tests\n-------------\n\n.. code-block:: sh\n\n    $ poetry run pytest\n\nContributing\n------------\n\nIssues and pull requests are welcome.\n\n* For proposing new features/improvements or reporting bugs, `create an issue <https://github.com/adonmo/trajectory/issues/new/choose>`_.\n* Check `open issues <https://github.com/adonmo/trajectory/issues>`_ for viewing existing ideas, verify if it is already proposed/being worked upon.\n* When implementing new features make sure to add relavant tests and documentation before sending pull requests.\n",
    'author': 'B Krishna Chaitanya',
    'author_email': 'bkchaitan94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adonmo/trajectory',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
