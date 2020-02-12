# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['curlipie']

package_data = \
{'': ['*']}

install_requires = \
['first>=2.0.2,<3.0.0',
 'hh>=2.0.0,<3.0.0',
 'multidict>=4.7.4,<5.0.0',
 'single-version>=1.1,<2.0',
 'typed-argument-parser>=1.4,<2.0',
 'yarl>=1.4.2,<2.0.0']

extras_require = \
{':python_version >= "3.7"': ['orjson>=2.2.0,<3.0.0'],
 ':python_version ~= "3.6"': ['python-rapidjson>=0.9.1,<0.10.0']}

setup_kwargs = {
    'name': 'curlipie',
    'version': '0.7.0',
    'description': 'Library to convert cURL command line to HTTPie',
    'long_description': '========\nCurliPie\n========\n\n.. image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d\n.. image:: https://badgen.net/pypi/v/curlipie\n\nPython library to convert `cURL`_ command to `HTTPie`_.\n\nIt will convert\n\n.. code-block:: sh\n\n    curl -d name=admin -d shoesize=12 -d color=green&food=wet http://quan.hoabinh.vn\n\nto\n\n.. code-block:: sh\n\n    http -f http://quan.hoabinh.vn name=admin shoesize=12 color=green food=wet\n\n\nMotivation\n----------\n\nThis library was born when I join a project with a team of non-Linux, non-Python developers. Because the project doesn\'t have proper documentation, the other team often share API usage example to me in form of cURL command, generated from their daily-used Postman. Those cURL commands are usually ugly, like this:\n\n\n.. code-block:: sh\n\n    curl --location --request POST \'http://app-staging.dev/api\' \\\n    --header \'Content-Type: application/json\' \\\n    --data-raw \'{\n        "userId": "abc-xyz",\n        "planAmount": 50000,\n        "isPromotion": false,\n        "createdAt": "2019-12-13 10:00:00"\n    }\'\n\nI am more comfortable with HTTPie (shorter syntax, has highlighting and is a Python application), so I often convert it to HTTPie:\n\n.. code-block:: sh\n\n    http -F app-staging.dev/api userId=abc-xyz planAmount:=50000 isPromotion:=false createdAt=\'2019-12-13 10:00:00\'\n\nThe Postman tool can generate HTTPie, but with even uglier command:\n\n.. code-block:: sh\n\n    printf \'{\n        "userId": "abc-xyz",\n        "planAmount": 50000,\n        "isPromotion": false,\n        "createdAt": "2019-12-13 10:00:00"\n    }\'| http  --follow --timeout 3600 POST app-staging.dev/api \\\n    Content-Type:\'application/json\'\n\nInitially, I had to do conversion manually and quickly got tired from it. I tried to find a conversion tool but failed. There is an online tool `curl2httpie.online`_, but it failed with above example. So I decide to write my own tool.\n\nI don\'t bother to help fix the online tool above, because it is written in Go. The rich ecosystem of Python, with these built-in libraries, enable me to finish the job fast:\n\n- |shlex|_: Help parse the command line in form of shell language, handle the string escaping, quoting for me.\n- |argparse|_: Help parse cURL options and arguments. Note that, cURL arguments syntax follow GNU style, which is common in Linux (and Python) world but not popular in Go world (see `this tutorial <go_tutorial_>`_), so it feels more natural with Python.\n\n\nUsage\n-----\n\n.. code-block:: python\n\n    >>> from curlipie import curl_to_httpie\n\n    >>> curl = """curl -XPUT elastic.dev/movies/_doc/1 -d \'{"director": "Burton, Tim", "year": 1996, "title": "Mars Attacks!"}\' -H \'Content-Type: application/json\'"""\n\n    >>> curl_to_httpie(curl)\n    ConversionResult(httpie="http PUT elastic.dev/movies/_doc/1 director=\'Burton, Tim\' year:=1996 title=\'Mars Attacks!\'", errors=[])\n\n    >>> result = curl_to_httpie(curl)\n\n    >>> result.httpie\n    "http PUT elastic.dev/movies/_doc/1 director=\'Burton, Tim\' year:=1996 title=\'Mars Attacks!\'"\n\n\nOnline tool\n-----------\n\nCurliPie is not very usable if it stays in library form, so I made an online tool for you to use it quickly:\n\nhttps://curlipie.now.sh/\n\nThe site also provide HTTP API for you to develop a client for it.\n\n\n.. _cURL: https://curl.haxx.se\n.. _HTTPie: https://httpie.org\n.. _curl2httpie.online: https://curl2httpie.online/\n.. |shlex| replace:: ``shlex``\n.. _shlex: https://docs.python.org/3/library/shlex.html\n.. |argparse| replace:: ``argparse``\n.. _argparse: https://docs.python.org/3/library/argparse.html\n.. _go_tutorial: https://gobyexample.com/command-line-flags\n',
    'author': 'Nguyễn Hồng Quân',
    'author_email': 'ng.hong.quan@gmail.com',
    'maintainer': 'Nguyễn Hồng Quân',
    'maintainer_email': 'ng.hong.quan@gmail.com',
    'url': 'https://github.com/hongquan/CurliPie.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
