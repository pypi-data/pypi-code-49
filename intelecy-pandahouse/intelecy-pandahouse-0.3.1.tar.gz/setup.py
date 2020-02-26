# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandahouse', 'pandahouse.tests']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=0.25.3,<0.26.0', 'requests>=2.22.0,<3.0.0', 'toolz>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'intelecy-pandahouse',
    'version': '0.3.1',
    'description': 'Pandas interface for Clickhouse HTTP API',
    'long_description': 'Pandahouse\n==========\n\n> Note: this is a fork. You probably want to use https://github.com/kszucs/pandahouse\n\nPandas interface for ClickHouse HTTP API\n\nInstall\n-------\n\n```bash\npip install pandahouse\n```\n\nUsage\n-----\n\nWriting a dataframe to ClickHouse\n\n```python\nconnection = {"host": "http://clickhouse-host:8123",\n              "database": "test"}\naffected_rows = to_clickhouse(df, table="name", connection=connection)\n```\n\nReading arbitrary ClickHouse query to pandas\n\n```python\ndf = read_clickhouse("SELECT * FROM {db}.table", index_col="id",\n                     connection=connection)\n```',
    'author': 'Krisztián Szűcs',
    'author_email': 'szucs.krisztian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Intelecy/pandahouse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
