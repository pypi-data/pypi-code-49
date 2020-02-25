# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflow_ecr_plugin', 'airflow_ecr_plugin.tests']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10,<2.0']

extras_require = \
{'airflow': ['apache-airflow>=1.10.9,<2.0.0']}

setup_kwargs = {
    'name': 'airflow-ecr-plugin',
    'version': '0.1.3',
    'description': 'Airflow ECR plugin',
    'long_description': '# Airflow AWS ECR Plugin\n\n[![Build Status](https://travis-ci.org/asandeep/airflow-ecr-plugin.svg?branch=master)](https://travis-ci.org/asandeep/airflow-ecr-plugin)\n[![codecov](https://codecov.io/gh/asandeep/airflow-ecr-plugin/branch/master/graph/badge.svg)](https://codecov.io/gh/asandeep/airflow-ecr-plugin)\n[![Python Versions](https://img.shields.io/pypi/pyversions/airflow-ecr-plugin.svg)](https://pypi.org/project/airflow-ecr-plugin/)\n[![Package Version](https://img.shields.io/pypi/v/airflow-ecr-plugin.svg)](https://pypi.org/project/airflow-ecr-plugin/)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nThis plugin exposes an operator that refreshes ECR login token at regular intervals.\n\n## About\n\n[Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a AWS managed Docker registry to host private Docker container images. Access to Docker repositories hosted on ECR can be controlled with resource based permissions using AWS IAM.\n\nTo push/pull images, Docker client must authenticate to ECR registry as an AWS user. An authorization token can be generated using AWS CLI `get-login-password` command that can be passed to `docker login` command to authenticate to ECR registry. For instructions on setting up ECR and obtaining login token to authenticate Docker client, click [here](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html).\n\nThe authorization token obtained using `get-login-password` command is only valid for 12 hours and Docker client needs to authenticate with fresh token after every 12 hours to make sure it can access Docker images hosted on ECR. Moreover, ECR registries are region specific and separate token should be obtained to authenticate to each registry.\n\nThe whole process can be quite cumbersome when combined with Apache Airflow. Airflow\'s `DockerOperator` accepts `docker_conn_id` parameter that it uses to authenticate and pull images from private repositories. In case this private registry is ECR, a connection can be created with login token obtained from `get-login-password` command and the corresponding ID can be passed to `DockerOperator`. However, since the token is only valid for 12 hours, `DockerOperator` will fail to fetch images from ECR once token is expired.\n\nThis plugin implements `RefreshEcrDockerConnectionOperator` Airflow operator that can automatically update the ECR login token at regular intervals.\n\n## Installation\n\n#### Pypi\n\n```bash\npip install airflow-ecr-plugin\n```\n\n#### Poetry\n\n```bash\npoetry add airflow-ecr-plugin@latest\n```\n\n## Getting Started\n\nOnce installed, plugin can be loaded via [setuptools entrypoint](https://packaging.python.org/guides/creating-and-discovering-plugins/#using-package-metadata) mechanism.\n\nUpdate your package\'s setup.py as below:\n\n```python\nfrom setuptools import setup\n\nsetup(\n    name="my-package",\n    ...\n    entry_points = {\n        \'airflow.plugins\': [\n            \'aws_ecr = airflow_ecr_plugin:AwsEcrPlugin\'\n        ]\n    }\n)\n```\n\nIf you are using Poetry, plugin can be loaded by adding it under `[tool.poetry.plugin."airflow.plugins"]` section as below:\n\n```toml\n[tool.poetry.plugins."airflow.plugins"]\n"aws_ecr" = "airflow_ecr_plugin:AwsEcrPlugin"\n```\n\nOnce plugin is loaded, same will be available for import in python modules.\n\nNow create a DAG to refresh ECR tokens,\n\n```python\nfrom datetime import timedelta\n\nimport airflow\nfrom airflow.operators import aws_ecr\n\n\nDEFAULT_ARGS = {\n    "depends_on_past": False,\n    "retries": 0,\n    "owner": "airflow",\n}\n\nREFRESH_ECR_TOKEN_DAG = airflow.DAG(\n    dag_id="Refresh_ECR_Login_Token",\n    description=(\n        "Fetches the latest token from ECR and updates the docker "\n        "connection info."\n    ),\n    default_args=DEFAULT_ARGS,\n    schedule_interval=<token_refresh_interval>,\n    # Set start_date to past date to make sure airflow picks up the tasks for\n    # execution.\n    start_date=airflow.utils.dates.days_ago(2),\n    catchup=False,\n)\n\n# Add below operator for each ECR connection to be refreshed.\naws_ecr.RefreshEcrDockerConnectionOperator(\n    task_id=<task_id>,\n    ecr_docker_conn_id=<docker_conn_id>,\n    ecr_region=<ecr_region>,\n    aws_conn_id=<aws_conn_id>,\n    dag=REFRESH_ECR_TOKEN_DAG,\n)\n```\n\nPlaceholder parameters in above code snippet are defined below:\n\n- `token_refresh_interval`: Time interval to refresh ECR login tokens. This should be less than 12 hours to prevent any access issues.\n- `task_id`: Unique ID for this task.\n- `docker_conn_id`: The Airflow Docker connection ID corresponding to ECR registry, that will be updated when this operator runs. The same connection ID should be passed to `DockerOperator` that pulls image from ECR registry. If connection does not exist in Airflow DB, operator will automatically create it.\n- `ecr_region`: AWS region of ECR registry.\n- `aws_conn_id`: Airflow connection ID corresponding to AWS user credentials that will be used to authenticate and retrieve new login token from ECR. This user should at minimum have `ecr:GetAuthorizationToken` permissions.\n\n## Known Issues\n\nIf you are running Airflow v1.10.7 or earlier, the operator will fail due to: [AIRFLOW-3014](https://issues.apache.org/jira/browse/AIRFLOW-3014).\n\nThe work around is to update Airflow `connection` table `password` column length to 5000 characters.\n\n## Acknowledgements\n\nThe operator is inspired from [Brian Campbell](https://www.linkedin.com/in/bvcampbell3)\'s post on [Using Airflow\'s Docker operator with ECR](https://www.lucidchart.com/techblog/2019/03/22/using-apache-airflows-docker-operator-with-amazons-container-repository/).\n',
    'author': 'Sandeep Aggarwal',
    'author_email': 'asandeep.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/asandeep/airflow-ecr-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
