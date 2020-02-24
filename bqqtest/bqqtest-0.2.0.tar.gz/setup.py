# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bqqtest']

package_data = \
{'': ['*'], 'bqqtest': ['testdata/*']}

install_requires = \
['google-cloud-bigquery>=1.24.0,<2.0.0', 'pandas>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'bqqtest',
    'version': '0.2.0',
    'description': 'Test BigQuery query using BigQuery',
    'long_description': '# WIP: BigQueryのクエリをテストするためのツール\n<img alt="Run pytest" src="https://github.com/tamanobi/bq-query-unittest/workflows/Run%20Tests/badge.svg">\n\nBigQueryへのクエリロジックのテストができます\n\n# Usage\n\n```python\nfrom bqqtest import QueryTest\nfrom google.cloud import bigquery\n\nexpected = {\'schema\': [(\'name\', \'STRING\'), (\'value\', \'INT64\')], \'datum\': [[\'abc\', 100]]}\ntables = [{\'schema\': [(\'name\', \'STRING\'), (\'value\', \'INT64\')], \'datum\': [[\'abc\', 100]], \'name\': \'INPUT_DATA\'}]\nquery = {\'query\': \'SELECT * FROM hogehoge\', \'map\': {\'hogehoge\': \'INPUT_DATA\'}, \'params\': []}\nqt = QueryTest(bigquery.Client(), expected, tables, query)\nsuccess, diff = qt.run()\nsuccess # True\n```\n\n## 特徴\n\n * WITHを利用してテストデータを一時的に生成します。このデータはBigQueryに保存されません。BigQueryは保存されているデータ走査した量とAPIリクエスト数で課金されるため、課金額を抑えた状態でテストできます\n\n## 注意\nBigQueryへ直接クエリを発行します。\n',
    'author': 'tamanobi',
    'author_email': 'tamanobi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tamanobi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
