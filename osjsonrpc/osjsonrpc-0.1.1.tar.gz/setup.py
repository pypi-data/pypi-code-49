# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['osjsonrpc']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0']

setup_kwargs = {
    'name': 'osjsonrpc',
    'version': '0.1.1',
    'description': 'Over-simple JSON-RPC Python implementation for aiohttp',
    'long_description': '# Over-Simple JSON RPC Implementation\n\nOver-simple JSON-RPC Python implementation for aiohttp\n\n## Install\n\n    pip install osjsonrpc\n\n## Usage\n\nExample:\n\n```python\nfrom aiohttp import web\nfrom osjsonrpc import JsonRpcEndpoint\n\ndef ping():\n    return "pong"\n\ndef multiply(a, b):\n    return {"a": a, "b": b, "a*b": a * b}\n\nrpc = (\n    JsonRpcEndpoint()\n    .register_method(ping)\n    .register_method(multiply)\n)\n\napp = web.Application()\napp.add_routes([rpc.route("/api")])\nweb.run_app(app)\n```\n\nCall the `ping` method without arguments:\n\n    ~ curl -s -H "Content-Type: application/json" -H "Accept: application/json" -X POST \\\n      -d \'{"jsonrpc":"2.0", "method": "ping", "id": 1}\' \\\n      http://localhost:8080/api | jq\n\n    {\n      "jsonrpc": "2.0",\n      "result": "pong",\n      "id": 1\n    }\n\nCall the `multiply` with a couple of positional arguments:\n\n    ~ curl -s -H "Content-Type: application/json" -H "Accept: application/json" -X POST \\\n      -d \'{"jsonrpc":"2.0", "method": "multiply", "params": [3, 5], "id": 1}\' \\\n      http://localhost:8080/api | jq\n\n    {\n      "jsonrpc": "2.0",\n      "result": {\n        "a": 3,\n        "b": 5,\n        "a*b": 15\n      },\n      "id": 1\n    }\n\nCall the `ping` argument with invalid keyword argument:\n\n    ~ curl -s -H "Content-Type: application/json" -H "Accept: application/json" -X POST \\\n      -d \'{"jsonrpc":"2.0", "method": "ping", "params": {"key": "value"}, "id": 1}\' \\\n      http://localhost:8080/api | jq\n\n    {\n      "jsonrpc": "2.0",\n      "error": {\n        "code": -32602,\n        "message": "Invalid params",\n        "data": {\n          "detail": "TypeError: ping() got an unexpected keyword argument \'key\'",\n          "request": {\n            "jsonrpc": "2.0",\n            "method": "ping",\n            "params": {\n              "key": "value"\n            },\n            "id": 1\n          }\n        }\n      },\n      "id": 1\n    }\n',
    'author': 'Konstantin V.',
    'author_email': 'mail@k-vinogradov.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/k-vinogradov/osjsonrpc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
