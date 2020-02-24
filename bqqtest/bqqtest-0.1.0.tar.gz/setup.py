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
    'version': '0.1.0',
    'description': 'Test BigQuery query using BigQuery',
    'long_description': '# WIP: BigQueryのクエリをテストするためのツール\n<img alt="Run pytest" src="https://github.com/tamanobi/bq-query-unittest/workflows/Run%20Tests/badge.svg">\n\nBigQueryへのクエリロジックのテストができます\n\n## 特徴\n\n * CSV形式のファイルを元にBigQueryにテーブルを一時的に作成します\n * 一時的に作成したテーブルに対して、クエリを発行し、結果を得ます\n * 結果と、期待しているテーブル(CSVファイル)と突合し、違いがなければテストをパスします\n\n## 注意\nBigQueryへ直接クエリを発行します。\n',
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
