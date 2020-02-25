# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sight_api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'sight-api',
    'version': '1.0.1',
    'description': "Official client for Siftrics' Sight API, which is a text recognition service",
    'long_description': 'This repository contains the official [Sight API](https://siftrics.com/) Python client. The Sight API is a text recognition service.\n\n# Quickstart\n\n1. Install the package.\n\n```\npip install sight-api\n```\n\nor\n\n```\npoetry add sight-api\n```\n\netc.\n\n2. Grab an API key from the [Sight dashboard](https://siftrics.com/).\n3. Create a client, passing your API key into the constructor, and recognize text:\n\n```\nimport sight_api\n\nclient = sight_api.Client(\'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\')\n\npages = client.recognize([\'invoice.pdf\', \'receipt_1.png\'])\n```\n\n`pages` looks like this:\n\n```\n[\n    {\n        "Error": "",\n        "FileIndex": 0,\n        "PageNumber": 1,\n        "NumberOfPagesInFile": 3,\n        "RecognizedText": [ ... ]\n    },\n    ...\n]\n```\n\n`FileIndex` is the index of this file in the original request\'s "files" array.\n\n`RecognizedText` looks like this:\n\n```\n"RecognizedText": [\n    {\n        "Text": "Invoice",\n        "Confidence": 0.22863210084975458\n        "TopLeftX": 395,\n        "TopLeftY": 35,\n        "TopRightX": 449,\n        "TopRightY": 35,\n        "BottomLeftX": 395,\n        "BottomLeftY": 47,\n        "BottomRightX": 449,\n        "BottomRightY": 47,\n    },\n    ...\n]\n```\n\n## Streaming in Results\n\nIf you process more than one page in a single `.recognize([ ... ])` call, results may come in over time, instead of all at once.\n\nTo access results (`pages` objects) as soon as they come in, there is a generator you can use:\n\n```\nfor pages in self.recognizeAsGenerator([\'invoice.pdf\', \'receipt_1.png\']):\n    print(pages)\n```\n\nIn fact, `.recognize([ ... ])` is defined in terms of that generator:\n\n```\nclass Client:\n    ...\n    def recognize(self, files):\n        ...\n        pages = list()\n        for ps in self.recognizeAsGenerator(files):\n            pages.extend(ps)\n        return pages\n```\n\nHere is the [official documentation for the Sight API](https://siftrics.com/docs/sight.html).\n\n# Apache V2 License\n\nThis code is licensed under Apache V2.0. The full text of the license can be found in the "LICENSE" file.\n',
    'author': 'Siftrics Founder',
    'author_email': 'siftrics@siftrics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://siftrics.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
