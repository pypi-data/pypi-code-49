# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatserver']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy>=1.3.13,<2.0.0', 'werkzeug>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['chatserver = chatserver:chatserver.main',
                     'run = chatserver:chatserver.main']}

setup_kwargs = {
    'name': 'chatserver',
    'version': '0.1.3',
    'description': 'A chatserver written in python',
    'long_description': "# Chat Server\n\nA simple chat server written in python.\n\n## Features\n\nThe features of chatserver include:\n\n* Optional TLS\n* User accounts\n* Chat Rooms\n\n## TLS Certificates\n\nSetup is only currently required if you want to use tls.\nTo do this you need to generate a crt and key file.\n\n```bash\nmkdir certs\ncd certs\nopenssl req -newkey rsa:2048 -nodes -keyout chatserv.key -x509 -days 365 -out chatserv.crt\n```\n\n## Running The Server\n\n### Pip\n\nYou can install chatserver using pip.\n\n```bash\npip install --upgrade chatserver\nchatserver\n```\n\n### Build Locally\n\nMake sure poetry is installed and up to date.\n\n```bash\npip install --upgrade poetry\n```\n\nInstall all the dependencies\n\n```bash\npoetry install\n```\n\nYou can now run the project from outside poetry's virtual env\n\n```bash\npoetry run chatserver\n```\n\nOr from within it\n\n```bash\nchatserver\n```\n\nIf you want to use TLS you need to set environment variables>\n\n* `CERT_FILE`\n* `KEY_FILE`\n\n### With Docker\n\nYou can either build locally or use the image from the registry\n\n```bash\n# Build locally\ndocker build -t chatserver .\ndocker run --name chatserver_name -p 7878:7878 chatserver\n```\n\n```bash\n# Using the image from the registry\ndocker build -t chatserver .\ndocker run --name chatserver_name -p 7878:7878 registry.gitlab.com/mokytis/python-chatserver:latest\n```\n\nTo use tls you will need to mount a direcory containg the crt and key files and set enviornment variables.\n\nExample:\n\n```bash\ndocker run -i -t -d \\\n    -p 7878:7878 \\\n    -v /path/to/certs/directory:/certs \\\n    -e CERT_FILE='/certs/chatserv.crt' \\\n    -e KEY_FILE='/certs/chatserv.key' \\\n    --name chatserver\n    chatserver\n```\n\n## Connecting To The Server\n\n### No TLS\n\nIf the server is not using tls you can connect to the server using any TCP client.\n\n```bash\nnc localhost 7878\n```\n\n### TLS\n\nIf the server is using TLS you can connect using openssl\n\n```bash\nopenssl s_client -connect localhost:7878\n```\n",
    'author': 'Luke Spademan',
    'author_email': 'info@lukespademan.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mokytis/python-chatserver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
