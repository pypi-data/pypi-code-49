# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dbxdeploy']

package_data = \
{'': ['*'],
 'dbxdeploy': ['_config/*',
               'cluster/*',
               'dbc/*',
               'deploy/*',
               'job/*',
               'notebook/*',
               'notebook/converter/*',
               'package/*',
               'string/*',
               'whl/*',
               'workspace/*']}

install_requires = \
['console-bundle>=0.2.0,<0.3.0',
 'databricks-api>=0.3.0,<0.4.0',
 'dbx-notebook-exporter>=0.2.0,<0.3.0',
 'nbconvert>=5.6.0,<5.7.0',
 'pyfony-bundles>=0.2.0,<0.3.0',
 'pygit2>=0.28.0,<0.29.0',
 'python-box>=3.4.0,<3.5.0',
 'tomlkit>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'dbx-deploy',
    'version': '0.8.0',
    'description': 'Databrics Deployment Tool',
    'long_description': 'Databricks project deployment package\n',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/dbx-deploy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<3.8.0',
}


setup(**setup_kwargs)
