# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['intake_hive']

package_data = \
{'': ['*'],
 'intake_hive': ['tests/catalog.yaml',
                 'tests/catalog.yaml',
                 'tests/catalog.yaml',
                 'tests/catalog.yaml',
                 'tests/conftest.py',
                 'tests/conftest.py',
                 'tests/conftest.py',
                 'tests/conftest.py',
                 'tests/dal-catalog.yaml',
                 'tests/dal-catalog.yaml',
                 'tests/dal-catalog.yaml',
                 'tests/dal-catalog.yaml',
                 'tests/data/*',
                 'tests/test_hive_source.py',
                 'tests/test_hive_source.py',
                 'tests/test_hive_source.py',
                 'tests/test_hive_source.py']}

install_requires = \
['intake>=0.5.3', 'pyspark>=2.3.0']

entry_points = \
{'intake.drivers': ['hive = intake_hive.hive_source:HiveSource']}

setup_kwargs = {
    'name': 'intake-hive',
    'version': '0.1.1',
    'description': 'Intake Hive DataSource Plugin.',
    'long_description': '.. image:: https://travis-ci.org/zillow/intake-hive.svg?branch=master\n    :target: https://travis-ci.org/zillow/intake-hive\n\n.. image:: https://coveralls.io/repos/github/zillow/intake-hive/badge.svg?branch=master\n    :target: https://coveralls.io/github/zillow/intake-hive?branch=master\n\n\nWelcome to the Intake Hive plugin\n==================================================\nThis `Intake <https://intake.readthedocs.io/en/latest/quickstart.html>`_ plugin \n:\n\nExample where the Hive table is user_events_hive partitioned by userid:\n\n.. code-block:: yaml\n\n    sources:\n      user_events_hive:\n        driver: hive\n        args:\n          urlpath: \'user_events_yaml_catalog?userid={{userid}}\'\n\n\n\n.. code-block:: python\n\n  import pandas as pd\n  import intake\n\n  catalog = intake.open_catalog(catalog_path)\n\n  # Reads partition userid=42\n  pandas_df: pd.DataFrame = catalog.entity.user.user_events_partitioned(userid="42").read()\n',
    'author': 'Zillow AI Platform',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
