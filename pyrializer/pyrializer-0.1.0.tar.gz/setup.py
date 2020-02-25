# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrializer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyrializer',
    'version': '0.1.0',
    'description': 'A Python object (de)serializer',
    'long_description': '# Pyrializer\n\nA Python object (de)serializer\n\n## Basic usage\n\nYou must define classes and describe what attributes and their types using\nclass attributes like this:\n\n~~~ python\nclass Example\n  field_name = type1\n  other_field_name = type2\n~~~\n\nSee [Supported types](#supported-types) below.\n\n\n### Decoding from a serialized value\n\nDecoding an object maps a serialized value into a Python object:\n\n~~~ python\n\nfrom serializer import decode\n\npayload = {\n  \'name\': \'John Doe\',\n  \'age\': 52,\n  \'job\': {\n    \'name\': \'Software Engineer\',\n    \'salary\': 24000\n  }},\n  \'hobbies\': [\'fishing\', \'skating\']\n}\n\nclass Job:\n  name = str\n  role = str\n  salary = float\n\nclass Person:\n  name = str\n  age = int\n  job = Job\n  hobbies = [str]\n\nperson = decode(Person, person_payload)\n\nperson.name # "John Doe\'\nperson.job.salary # 24000\nperson.job.role # None\nperson.job.hobbies[1] # "skating"\n~~~\n\n\n### Encoding to a serialized value\n\nEncoding an object transform a Python object into a serializable format that can\nbe easily exported to others formats, such as JSON:\n\n~~~ python\nfrom serializer import encode\n\nencode(Person, person) # --> { \'name\': \'John Doe\', ... }\n~~~\n\nAdditionaly, you can decorate the classes you want to (de)serialize with the\n```serializable``` decorator. This decorator extends the classes with two\nadditional methods:\n\n~~~ python\nfrom pyrializer import serializable\n\n@serializable\nclass Person:\n  ...\n\nperson = Person.decode(person_payload)\n\nperson.encode() # --> { \'name\': \'John Doe\', ... }\n~~~\n\n\n## Supported types\n\nHere is some examples of supported types\n\n| \\<type>     | JSON equivalent  |\n|-------------|------------------|\n| `None`      | Any value        |\n| `str`       | String           |\n| `int`       | Integer          |\n| `float`     | Float            |\n| `bool`      | Boolean          |\n| `[<type>]`  | Array of \\<type> |\n| `ClassName` | Object           |\n\nMore advanced examples:\n\n~~~ python\nclass Example:\n  array_of_array_of_ints = [ [ int ] ]  # [ [1,2], [3, 4], [], [5, 6] ]\n  whatever = None  # 42, False, AnotherObject(), etc...\n~~~\n',
    'author': 'Alfonso Ruzafa',
    'author_email': 'alfonso.ruzafa@movo.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
