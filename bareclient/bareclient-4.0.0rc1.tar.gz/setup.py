# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bareclient', 'bareclient.acgi']

package_data = \
{'': ['*']}

install_requires = \
['baretypes>=3.1,<4.0',
 'bareutils>=3.2,<4.0',
 'h11>=0.9.0,<0.10.0',
 'h2>=3.1,<4.0']

setup_kwargs = {
    'name': 'bareclient',
    'version': '4.0.0rc1',
    'description': 'A lightweight asyncio HTTP client',
    'long_description': '# bareClient\n\nA simple asyncio http client supporting HTTP versions 1.0, 1.1 and 2.\n\nThe docs are [here](https://rob-blackbourn.github.io/bareClient/).\n\n## Description\n\nThis package provides the asyncio transport for\n[h11](https://h11.readthedocs.io/en/latest/index.html),\nand [h2](https://python-hyper.org/projects/h2/en/stable/).\n\nIt makes little attempt to provide any helpful features which might do\nunnecessary work.\n\n## Installation\n\nThis is a Python 3.7 package.\n\n```bash\npip install bareclient\n```\n\n## Usage\n\nThe basic usage is to create an `HttpClient`.\n\n```python\nimport asyncio\nfrom typing import List, Optional\nfrom baretypes import Header\n\nfrom bareclient import HttpClient\n\n\nasync def main(url: str, headers: Optional[List[Header]]) -> None:\n    async with HttpClient(url, method=\'GET\', headers=headers) as response:\n        print(response)\n        if response[\'status_code\'] == 200 and response[\'more_body\']:\n            async for part in response[\'body\']:\n                print(part)\n\n\nURL = \'https://docs.python.org/3/library/cgi.html\'\nHEADERS = None\n\nasyncio.run(main(URL, HEADERS))\n```\n\nThere is also an `HttpSession` for maintaining a session.\n\n```python\nimport asyncio\nimport logging\n\nimport bareutils.response_code as response_code\nfrom bareclient import HttpSession\n\nlogging.basicConfig(level=logging.DEBUG)\n\n\nasync def main() -> None:\n    session = HttpSession(\n        \'https://shadow.jetblack.net:9009\',\n        capath=\'/etc/ssl/certs\'\n    )\n    headers = [\n        (b\'host\', b\'shadow.jetblack.net\'),\n        (b\'connection\', b\'close\')\n    ]\n    for path in [\'/example1\', \'/example2\', \'/empty\']:\n        async with session.request(path, method=\'GET\', headers=headers) as response:\n            print(response)\n            if not response_code.is_successful(response[\'status_code\']):\n                print("failed")\n            else:\n                if response[\'status_code\'] == response_code.OK and response[\'more_body\']:\n                    async for part in response[\'body\']:\n                        print(part)\n\n\nasyncio.run(main())\n```\n\nFinally there is a single helper function to get json.\n\n```python\nimport asyncio\n\nfrom bareclient import get_json\n\n\nasync def main(url: str) -> None:\n    """Get some JSON"""\n    obj = await get_json(url, headers=[(b\'accept-encoding\', b\'gzip\')])\n    print(obj)\n\n\nURL = \'https://jsonplaceholder.typicode.com/todos/1\'\n\nasyncio.run(main(URL))\n```\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareclient',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
