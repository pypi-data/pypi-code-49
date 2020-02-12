# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omicidx',
 'omicidx.db',
 'omicidx.geo',
 'omicidx.mti',
 'omicidx.schema',
 'omicidx.scripts',
 'omicidx.sra']

package_data = \
{'': ['*']}

install_requires = \
['Click',
 'biopython==1.75',
 'boto3>=1.9,<2.0',
 'pydantic',
 'requests>=2.22,<3.0',
 'sd_cloud_utils',
 'sqlalchemy>=1.3,<2.0',
 'ujson>=1.35,<2.0']

entry_points = \
{'console_scripts': ['omicidx_tool = omicidx.scripts.cli:cli']}

setup_kwargs = {
    'name': 'omicidx',
    'version': '0.4.0',
    'description': 'The OmicIDX project collects, reprocesses, and then republishes metadata from multiple public genomics repositories. Included are the NCBI SRA, Biosample, and GEO databases. Publication is via the cloud data warehouse platform Bigquery, a set of performant search and retrieval APIs, and a set of json-format files for easy incorporation into other projects.',
    'long_description': '#\n\n# New process\n\n\n## Steps\n\n- Download xml\n- Create basic json\n- Upload json to s3\n- munge basic json to parquet\n- munge parquet to \n    - experiment joined\n\t- sample joined\n\t- run joined\n\t- study with aggregates\n\t- Include aggs in spark jobs:\n\t\t- number of samples, experiments, runs\n\t\t- sample, experiment, and run accessions (as array)\n- Save munged spark data (json, parquet)\n- Create elasticsearch index mappings\n- Drop existing elasticsearch mappings\n- Load elasticsearch index mappings\n\n\n## lambda\n\nzip lambdas.zip lambda_handlers.py sra_parsers.py\n\n\naws lambda create-function --function-name sra_to_json --zip-file fileb://lambdas.zip --handler lambda_handlers.lambda_return_full_experiment_json --runtime python3.6 --role arn:aws:iam::377200973048:role/lambda_s3_exec_role\n\n\n# Invoke\n\naws lambda invoke --function-name sra_to_json --log-type Tail --payload \'{"accession":"SRX000273"}\' /tmp/abc.txt\n\n# Concurrency\n\n1000 total, reserve for certain functions to limit, etc.\n\naws lambda put-function-concurrency --function-name sra_to_json --reserved-concurrent-executions 20\n\n# timeout and memory\n\naws lambda update-function-configuration --function-name sra_to_json --timeout 15\n\n\n# logging\n\nhttps://github.com/jorgebastida/awslogs\n\nawslogs get /aws/lambda/sra_to_json ALL --watch\n\n\n## dynamodb\n\naws dynamodb scan --table-name sra_experiment --select "COUNT"\n\n# GEO\n\n```\npython -m omicidx.geometa --gse=GSE10\n```\n\nWill print json, one "line" per entity to stdout.\n\n',
    'author': 'Sean Davis',
    'author_email': 'seandavi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/omicidx/omicidx-parsers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
