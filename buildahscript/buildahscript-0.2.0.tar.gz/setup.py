# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['buildahscript']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['buildahscript-py = buildahscript.cli:main']}

setup_kwargs = {
    'name': 'buildahscript',
    'version': '0.2.0',
    'description': 'Tool for buildah scripts',
    'long_description': '# buildahscript\n\nBuildahscript is a new container definition language built to be imperative and flexible.\n\nIt allows you to do more with buildargs, create actually re-usable modules, and in general create more flexible container builders.\n\n## Example\n\n```python\n#!/usr/bin/env buildahscript-py\n#| pip: requests\n#| arg: eula: bool\n#| arg: version: str = "latest"\n#| arg: type: str = "vanilla"\n\nimport tarfile\n\nimport requests\n\n\nwith TemporaryDirectory() as td:\n    bin = td / \'bin\'\n    bin.mkdir()\n    with Container(\'rust:buster\') as build:\n        build.copy_in(\'cmd\', \'/tmp/cmd\')\n        build.copy_in(\'localmc\', \'/tmp/localmc\')\n        build.run([\'cargo\', \'build\', \'--release\'], pwd=\'/tmp/cmd\')\n        build.copy_out(\'/tmp/cmd/target/release/cmd\', bin / \'cmd\')\n\n    with Container(\'rust:buster\') as build:\n        build.copy_in(\'status\', \'/tmp/status\')\n        build.copy_in(\'localmc\', \'/tmp/localmc\')\n        build.copy_in(\'mcproto-min-async\', \'/tmp/mcproto-min-async\')\n        build.run([\'cargo\', \'build\', \'--release\'], pwd=\'/tmp/status\')\n        build.copy_out(\'/tmp/status/target/release/status\', bin / \'status\')\n\n    # Download & extract mc-server-runner\n    with requests.get(\'https://github.com/itzg/mc-server-runner/releases/download/1.3.3/mc-server-runner_1.3.3_linux_amd64.tar.gz\') as resp:\n        resp.raise_for_status()\n        with tarfile.open(resp, \'r|*\') as tf:\n            for entry in tf:\n                if entry.name == \'mc-server-runner\':\n                    tf.extract(entry, bin / \'mc-server-runner\')\n\n    with Container(\'openjdk:8-jre-slim\') as cont:\n        cont.copy_in(bin / \'cmd\', \'/usr/bin/cmd\')\n        cont.copy_in(bin / \'status\', \'/usr/bin/status\')\n        cont.copy_in(bin / \'mc-server-runner\', \'/mc-server-runner\')\n\n        cont.volumes |= {\n            "/mc/world", "/mc/server.properties", "/mc/logs",\n            "/mc/crash-reports", "/mc/banned-ips.json",\n            "/mc/banned-players.json", "/mc/ops.json", "/mc/whitelist.json",\n        }\n        cont.entrypoint = ["/mc-server-runner", "-shell", "/bin/sh"]\n        cont.command = ["/mc/launch"]\n        cont.healthcheck_cmd = ["status"]\n        cont.healthcheck_start_period = "5m"\n\n        return cont.commit()\n```\n\n\n### shpipe\n\nshpipe (`#|`) lines are used to specify metadata used by buildahscript. The basic form is `#| type: data`.\n\n* `pip`: Gives a dependency to install from PyPI, as a [requirement specifier](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers)\n* `arg`: Defines a build arg, in the Python `name:type=default` form, where type\n  is a dotted-form name to a type/parsing function, and default is a python literal.\n\n\n## Licensing\n\nThis package is free to use for commercial purposes for a trial period under the terms of the [Prosperity Public License](./LICENSE).\n\nLicenses for long-term commercial use are available via [licensezero.com](https://licensezero.com).\n\n[![licensezero.com pricing](https://licensezero.com/projects/6aeb69c8-088b-41c2-b6ef-e7327ded1b7b/badge.svg)](https://licensezero.com/projects/6aeb69c8-088b-41c2-b6ef-e7327ded1b7b)',
    'author': 'Jamie Bliss',
    'author_email': 'jamie@ivyleav.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://buildahscript.github.io/',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
