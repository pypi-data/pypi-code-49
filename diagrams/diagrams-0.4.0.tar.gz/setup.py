# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['diagrams',
 'diagrams.alibabacloud',
 'diagrams.aws',
 'diagrams.azure',
 'diagrams.base',
 'diagrams.gcp',
 'diagrams.k8s']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.13.2,<0.14.0', 'jinja2>=2.10,<3.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['contextvars>=2.4,<3.0']}

setup_kwargs = {
    'name': 'diagrams',
    'version': '0.4.0',
    'description': 'Diagram as Code',
    'long_description': "![diagrams logo](assets/img/diagrams.png)\n\n# Diagrams\n\n[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)\n[![pypi version](https://badge.fury.io/py/diagrams.svg)](https://badge.fury.io/py/diagrams)\n![python version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python)\n\n**Diagram as Code**.\n\nDiagrams lets you draw the cloud system architecture **in Python code**. It was born for **prototyping** a new system architecture design without any design tools. You can also describe or visualize the existing system architecture as well. Diagrams currently supports five major providers: `AWS`, `Azure`, `GCP`, `Kubernetes` and `Alibaba Cloud`.\n\n**Diagram as Code** also allows you to **tracking** the architecture diagram changes on any **version control** system.\n\n>  NOTE: It does not control any actual cloud resources nor generate cloud formation or terraform code, but just for drawing the cloud system architecture diagrams.\n\n## Getting Started\n\nIt uses [Graphviz](https://www.graphviz.org/) to render the diagram, so you need to [install Graphviz](https://graphviz.gitlab.io/download/) to use **diagrams**. After installing graphviz (or already have it), install the **diagrams**.\n\n> macOS users can download the Graphviz via `brew install graphviz` if you're using [Homebrew](https://brew.sh).\n\n```shell\n# using pip (pip3)\n$ pip install diagrams\n\n# using pipenv\n$ pipenv install diagrams\n\n# using poetry\n$ poetry add diagrams\n```\n\nYou can start with [quick start](https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start). Check out [guides](https://diagrams.mingrammer.com/docs/guides/diagram) for more details, and you can find all available nodes list in [here](https://diagrams.mingrammer.com/docs/nodes/aws).\n\n## Examples\n\n| Grouped Workers on AWS                                       | Stateful Architecture on k8s                                 | Event Processing on AWS                                      |\n| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |\n| ![grouped workers](https://diagrams.mingrammer.com/img/grouped_workers_diagram.png) | ![stateful architecture](https://diagrams.mingrammer.com/img/stateful_architecture_diagram.png) | ![event processing](https://diagrams.mingrammer.com/img/event_processing_diagram.png) |\n\nYou can find all the examples on the [examples](https://diagrams.mingrammer.com/docs/getting-started/examples) page.\n\n## Contributing\n\nTo contribute to diagram, check out [contribution guidelines](CONTRIBUTING.md).\n\n> Let me know if you are using diagrams! I'll add you in showcase page. (I'm working on it!) :)\n\n## License\n\n[MIT](LICENSE)\n",
    'author': 'mingrammer',
    'author_email': 'mingrammer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://diagrams.mingrammer.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
