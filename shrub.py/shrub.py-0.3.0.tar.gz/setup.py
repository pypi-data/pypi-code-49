# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['shrub']

package_data = \
{'': ['*']}

install_requires = \
['PyYaml>=5.1,<6.0']

setup_kwargs = {
    'name': 'shrub.py',
    'version': '0.3.0',
    'description': 'Library for creating evergreen configurations',
    'long_description': '# shrub.py -- A python based Evergreen project config generation library\n\n## Overview\n\nBased on [shrub](https://github.com/evergreen-ci/shrub/), shrub.py is a library for programatically \nbuilding Evergreen project configurations described [here](https://github.com/evergreen-ci/evergreen/wiki/Project-Files).\n\n## Example\n\nThe following snippet will create a set of parallel tasks reported under a single display task. It\nwould generate json used by ```generate.tasks```:\n\n```\n        n_tasks = 10\n        c = Configuration()\n\n        task_names = []\n        task_specs = []\n\n        for i in range(n_tasks):\n            name = "aggregation_multiversion_fuzzer_{0:03d}".format(i)\n            task_names.append(name)\n            task_specs.append(TaskSpec(name))\n            t = c.task(name)\n            t.dependency(TaskDependency("compile")).commands([\n                CommandDefinition().function("do setup"),\n                CommandDefinition().function("do multiversion setup"),\n                CommandDefinition().function("run jstestfuzz").vars({\n                    "jstestfuzz_var": "--numGeneratedFiles 5",\n                    "npm_command": "agg-fuzzer",\n                }),\n                CommandDefinition().function("run tests").vars({\n                    "continue_on_failure": "false",\n                    "resmoke_args": "--suites=generational_fuzzer",\n                    "should_shuffle": "false",\n                    "task_path_suffix": "false",\n                    "timeout_secs": "1800",\n                })\n            ])\n\n        dt = DisplayTaskDefinition("aggregation_multiversion_fuzzer")\\\n            .components(task_names)\n        c.variant("linux-64").tasks(task_specs).display_task(dt)\n        \n        c.to_json()\n```\n\n## Run tests\n\n```\npip install tox\ntox\n```\n',
    'author': 'David Bradford',
    'author_email': 'david.bradford@mongodb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/evergreen-ci/shrub.py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
