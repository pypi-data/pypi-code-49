# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['barbara']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0.0,<8.0.0',
 'poetry-version>=0.1.3,<1.0.0',
 'python-dotenv>=0.10.1,<1.0.0',
 'pyyaml>=5.1.0,<6.0.0']

extras_require = \
{'ssm': ['boto3>=1.9,<2.0']}

entry_points = \
{'console_scripts': ['barb = barbara.cli:barbara_develop',
                     'barb-deploy = barbara.cli:barbara_deploy']}

setup_kwargs = {
    'name': 'barbara',
    'version': '1.2.0',
    'description': 'Environment variable management',
    'long_description': '.. image:: https://repository-images.githubusercontent.com/131429006/7eb3f680-8572-11e9-8c3d-68b1476c50e8#\n\n|python| |downloads| |license| |version|\n\nEnvironment variable management\n\nInstallation\n------------\n\n.. code:: shell\n\n    $ pip install barbara\n\nUsage\n-----\n\nYAML Format (.env.yml)\n----------------------\n\n1. Create an ``.env.yml`` for your project\n\n.. code:: yaml\n\n   project: your_project\n\n   environment:\n     ENVIRONMENT_NAME: development\n     DATABASE_URL:\n       template: "{user}:{password}@{host}:{port}/{db_name}"\n       subvariables:\n           user: root\n           password: root\n           host: 127.0.0.1\n           port: 5432\n           db_name: sample\n\n\n2. Run ``barb`` and you\'ll be prompted for the values\n\n.. code:: bash\n\n   $ barb\n   .env does not exist. Create it? [y/N]: y\n   Creating environment: .env\n   Skip Existing: True\n   DATABASE_URL:\n   user [root]:\n   password [root]: wordpass\n   host [127.0.0.1]:\n   port [5432]:\n   db_name [sample]:\n   ENVIRONMENT_NAME [development]:\n   Environment ready!\n\n3. Inspect the generated file, see your values!\n\n.. code:: bash\n\n   $ cat .env\n   DATABASE_URL=root:wordpass@127.0.0.1:5432/sample\n   ENVIRONMENT_NAME=development\n\nSubvariables\n------------\n\n*Subvariables* work by using the following syntax:\n\n.. code:: yaml\n\n   VARIABLE_NAME:\n     template: "{subvariable1} {subvariable2}"\n     subvariables:\n       subvariable1: default value for subvariable 1\n       subvariable2: default value for subvariable 2\n\nFor the given example, the user is shown ``VARIABLE_NAME`` as a title, and then prompted for the two values and offered\na default value. Any subvariable that appears in the template must also appear in the subvariables dictionary or the\nstring formatting operation will fail. Python string template syntax is used and formatting can be applied using the\nstandard colon syntax.\n\n\nAdvanced Usage (AWS SSM)\n------------------------\n\n.. note:: You must create the values in AWS SSM before they can be retrieved. You will also need the correct IAM\n          permissions to retrieve the values from AWS. All values are assumed to be encrypted at rest.\n\n1. Create an ``.env.yml`` for your project with the ``deployments`` section. This section is a declarative heirarchy\n   of overrides. At the root of deployments is the most general and therefore the lowest priority. For reference, the\n   paths have been provided as comments and are not required in practice.\n\n.. code:: yaml\n\n   project: your_project\n\n   environment:\n     DEBUG: 1\n     ENVIRONMENT_NAME: development\n     DATABASE_URL:\n       template: "{user}:{password}@{host}:{port}/{db_name}"\n       subvariables:\n           user: root\n           password: root\n           host: 127.0.0.1\n           port: 5432\n           db_name: sample\n     HOST_TYPE: local\n\n   deployments:\n     - DEBUG                 # /your_project/DEBUG\n     - staging:\n       - DATABASE_URL        # /your_project/staging/DATABASE_URL\n       - ENVIRONMENT_NAME    # /your_project/staging/ENVIRONMENT_NAME\n       - app_server:\n         - HOST_TYPE         # /your_project/staging/app_server/HOST_TYPE\n       - worker:\n         - HOST_TYPE         # /your_project/staging/worker/HOST_TYPE\n     - production:\n       - DATABASE_URL        # /your_project/production/DATABASE_URL\n       - ENVIRONMENT_NAME    # /your_project/production/ENVIRONMENT_NAME\n       - app_server:\n         - HOST_TYPE         # /your_project/production/app_server/HOST_TYPE\n       - worker:\n         - HOST_TYPE         # /your_project/production/worker/HOST_TYPE\n\n2. Run ``barb-deploy -p /your_project/staging/app_server/`` and a new ``.env`` will be produced using that search path\n   to determine the override priority of each variable.\n\n.. code:: bash\n\n   $ barb-deploy -p /your_project/staging/app_server/\n   Creating environment: .env (using search_path: /your_project/staging/app_server/)\n   Environment ready!\n\n3. Inspect the generated file, see your values!\n\n.. code:: bash\n\n   $ cat .env\n   DATABASE_URL=postgres://staging:staging@localhost:5432/staging_db\n   DEBUG=0\n   ENVIRONMENT_NAME=staging\n   HOST_TYPE=app_server\n\n\n\nLegacy Format (.env.template)\n-----------------------------\n\n1. Create an ``.env.template`` for your project\n\n.. code:: ini\n\n   DATABASE_HOST=127.0.0.1\n   COMPLEX_KEY=[username:user]:[password:pass]@$DATABASE_HOST\n\n\n2. Run ``barb`` and you\'ll be prompted for the values\n\n.. code:: bash\n\n   $ barb\n   .env does not exist. Create it? [y/N]: y\n   Creating environment: .env\n   Skip Existing: True\n   COMPLEX_KEY:\n   username [user]:\n   password [pass]: wordpass\n   DATABASE_HOST [127.0.0.1]:\n   Environment ready!\n\n\n3. Inspect the generated file, see your values!\n\n.. code:: bash\n\n   $ cat .env\n   COMPLEX_KEY=user:wordpass@$DATABASE_HOST\n   DATABASE_HOST=127.0.0.1\n\n*Legacy subvariables* work by using the ``[variable_name:variable_default]`` syntax within an ``.env`` template. You\ncan use as many as you wish in a row, but they cannot be nested.\n\n\nWhy ``barbara``?\n----------------\n\nBecause `Barbara Liskov <https://en.wikipedia.org/wiki/Barbara_Liskov>`__ created the `Liskov Substitution\nPrinciple <https://en.wikipedia.org/wiki/Liskov_substitution_principle>`__ and is a prolific contributor to\ncomputer science and software engineering. Barbara is one of the Newton\'s metaphorical giants that enables us\nto see further. I humbly dedicate my project to her and her contributions and offer this project to its\nconsumers with a license befitting that dedication.\n\n\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/barbara.svg?logo=python&logoColor=yellow&style=for-the-badge\n.. |downloads| image:: https://img.shields.io/pypi/dm/barbara.svg?style=for-the-badge\n.. |license| image:: https://img.shields.io/pypi/l/barbara.svg?style=for-the-badge\n.. |version| image:: https://img.shields.io/pypi/v/barbara.svg?style=for-the-badge\n',
    'author': 'Matthew de Verteuil',
    'author_email': 'onceuponajooks@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
