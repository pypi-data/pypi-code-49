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
    'version': '0.5.1',
    'description': 'Test BigQuery query using BigQuery',
    'long_description': '# BigQueryのクエリをテストするためのツール\n<img alt="Run pytest" src="https://github.com/tamanobi/bq-query-unittest/workflows/Run%20Tests/badge.svg">\n\nBigQueryへのクエリロジックのテストができます\n\n## Basic Usage\n\n### Simple\n\n```python\nfrom bqqtest import QueryTest\nfrom google.cloud import bigquery\n\n# expected\nexpected_schema = [\n    {"name": "name", "type": "STRING", "mode": "NULLABLE"},\n    {"name": "value", "type": "INT64", "mode": "NULLABLE"},\n]\nexpected_datum = [["abc", 100], ["bbb", 333]]\nexpected = {"schema": expected_schema, "datum": expected_datum}\n\n# actual\ntarget_schema = [\n    {"name": "name", "type": "STRING", "mode": "NULLABLE"},\n    {"name": "value", "type": "INT64", "mode": "NULLABLE"},\n]\ntarget_datum = [["abc", 100], ["bbb", 333]]\ntables = {"test.target_table": {"schema": target_schema, "datum": target_datum}}\neval_query = {"query": "SELECT * FROM test.target_table", "params": []}\n\nqt = QueryTest(bigquery.Client(), expected, tables, eval_query)\nsuccess, diff = qt.run()\nsuccess  # True\n```\n\n## Group By\n\n```python\nfrom bqqtest import QueryTest\nfrom google.cloud import bigquery\n\n# expected\nexpected_schema = [\n    {"name": "item", "type": "STRING", "mode": "NULLABLE"},\n    {"name": "total", "type": "INT64", "mode": "NULLABLE"},\n]\nexpected_datum = [["abc", 300], ["bbb", 333]]\nexpected = {"schema": expected_schema, "datum": expected_datum}\n\n# actual\ntarget_schema = [\n    {"name": "item", "type": "STRING", "mode": "NULLABLE"},\n    {"name": "value", "type": "INT64", "mode": "NULLABLE"},\n]\ntarget_datum = [["abc", 100], ["bbb", 333], ["abc", 200]]\ntables = {"test.target_table": {"schema": target_schema, "datum": target_datum}}\neval_query = {\n    "query": "SELECT item, SUM(value) AS total FROM test.target_table GROUP BY item",\n    "params": [],\n}\n\nqt = QueryTest(bigquery.Client(), expected, tables, eval_query)\nsuccess, diff = qt.run()\nsuccess  # True\n```\n\n## Multi Table\n\n```python\nfrom bqqtest import QueryTest\nfrom google.cloud import bigquery\n\n\n# expected\nexpected_schema = [\n    {"name": "item", "type": "STRING", "mode": "NULLABLE"},\n    {"name": "value", "type": "INT64", "mode": "NULLABLE"},\n]\nexpected_datum = [["abc", 100], ["bbb", 333], ["xxxx", 888], ["zzzz", 999]]\nexpected = {"schema": expected_schema, "datum": expected_datum}\n\n# actual\ntarget_schema = [\n    {"name": "item", "type": "STRING", "mode": "NULLABLE"},\n    {"name": "value", "type": "INT64", "mode": "NULLABLE"},\n]\ntarget_datum1 = [["abc", 100], ["bbb", 333]]\ntarget_datum2 = [["xxxx", 888], ["zzzz", 999]]\ntables = {\n    "test.table1": {"schema": target_schema, "datum": target_datum1},\n    "test.table2": {"schema": target_schema, "datum": target_datum2},\n}\neval_query = {\n    "query": "SELECT * FROM `test.table1` UNION ALL SELECT * FROM `test.table2`",\n    "params": [],\n}\n\nqt = QueryTest(bigquery.Client(), expected, tables, eval_query)\nsuccess, diff = qt.run()\nsuccess  # True\n```\n\n## 特徴\n\nsee also https://qiita.com/tamanobi/items/9434ca0dbd5f0d3018d9\n\n * WITH を利用して、 BigQuery に保存されないテストデータを一時的に生成します。\n    * BigQuery は保存されているデータ走査した量とAPIリクエスト数で課金されるため、費用抑えてユニットテストができます。\n    * 料金の詳細は、 BigQuery の公式ドキュメントを参照してください\n * テストをするために、クエリを書き直す必要はありません\n    * ライブラリ内部では、対象テーブルの Identifier を書き換えてテーブルを差し替えます\n\n## 注意\n\nBigQuery へ直接クエリを発行します。\n',
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
