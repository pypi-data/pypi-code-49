# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymatched']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pymatched',
    'version': '0.2.1',
    'description': 'A library which provides simple functional pattern matching.',
    'long_description': '*<h1 align="center">py<b>matched⇒</b></h1>*\n\n# What is pymatched?\npymatched is a library which provides functional pattern matching.\n\n# Installation\n```bash\npip install pymatched\n```\n\n# Syntax\n```python\nresult = match(<\'func\'>) >> Mapping[Hashable, Any]\n```\n\n## Match order\n1. exact match\n2. oneof match\n3. placeholder match (if target is immutable iterable)\n4. type match with guard (Contravariant match)\n5. type match (Invariant match)\n6. type match (Contravariant match)\n7. handling default if exists\n\n# Usage\n\n### Note: How to match mutable value?\nas you know, mutable things cannot be key of dict so we can not match easly.\n\nthis is the example of list.\n\n#### Case A: use type guards\n\n```python\nx = match([1, 2, 3]) >> {\n    list                            : "list",\n    oneof([1], [1, 2], [1, 2, 3])   : "[1] | [1, 2] | [1, 2, 3]",\n    (list, lambda x: x == [1, 2, 3]): "(list, f(list) -> bool)",\n    # [1, 2, 3]: "[1, 2, 3]",  --> list is unhashable so not working\n}\n```\n\n#### Case B: use nested match\n\n```python\nx = match([1, 2, 3]) >> {\n    list: match(...) >> {\n        (list, lambda v: v == [1, _, 3]): "pattern is (1, * ,3)",\n        ...                             : "default"\n    } \n}\n```\n\n\n## Value match\n\n```python\nfrom pymatched import match\n\nmatch(1) >> {\n    1: "It\'s 1",\n    5: "It\'s 5",\n}\n```\n\n## Handling default case\nuse elipsis `...` or `typing.Any`\n\nif nothing catched but default handler not defined, RuntimeError will be raised.\n\n```python\nfrom typing import Any\nfrom pymatched import match\n\nmatch(None) >> {\n    ...: "default",\n    # Any: "also default",\n}\n```\n\n## Type match\n```python\nfrom pymatched import match\n\nmatch(42) >> {\n    int: "int caught",\n    ...: lambda v: f"{type(v)} caught"\n}\n```\n\n###  Type match with guard\n\nIf tuple\'s first element is type and second element is lambda, this case will be considered as type match with guard.\n\n```python\nfrom pymatched import match\n\nmatch(42) >> {\n    (int, lambda: v: v == 42): "42 caught",\n    int                      : "int except 42",\n}\n```\n\ntype match with guard can use `typing.Any`.\n\n```python\nfrom typing import Any\nfrom pymatched import match\n\nmatch(42) >> {\n    (Any, lambda: v: v in (42, "42")): "42 caught",\n    int                              : "int except 42",\n}\n```\n\n### Exception match in type match\n\n`pymatched.do` wraps executing function. when wrapped function raises error, `do` catch it and return it as normal return. \n\n```python\nfrom pymatched import match, do\n\ndef fx(v):\n    raise Exception("Ooops!")\n\nmatch(do(fx, None)) >> {\n    Exception: "exception caught",\n    ...      : lambda v: f"{v} caught",\n}\n```\n\n## Oneof match\n```python\nfrom pymatched import oneof, match\n\nfx = lambda x: x\n\nmatch(fx(5)) >> {\n    oneof(1, 2, 3): "one of 1, 2, 3",\n    oneof(4, 5, 6): "one of 4, 5, 6",\n}\n```\n\n# Placeholder match\n\n```python\nfrom pymatched import oneof, match\n\nmatch((1, 2, 3, 4)) >> {  # change (1, 2, 3, 4) into (100, 2, 3, 4) or (1, 9, 3, 9)\n    (1, _, 3, _): "pattern (1, *, 3, *)",\n    (_, 2, _, 4): "pattern (*, 2, *, 4)",\n}\n```\n\n## Nested match\n\nIf match with `pymatchied._` (PlaceholderTyoe) or `...` (Ellipsis), this match will be considered as nested match.\n\n```python\nfrom pymatched import match, _\n\nmatch(5) >> {\n    int: match(_) >> {\n        5: "It\'s 5",\n        ...: "default"\n    },\n}\n```\n\n## Mixed match\n\ncases could be mixed, but resolved by designated match order.\n\n```python\nfrom pymatched import oneof, match\n\nv = (1, 2, 3)\n\nx = match(v) >> {\n    tuple                         : "Tuple caught",\n    (tuple, lambda v: v[-1] == 3) : "last item of tuple is 3",\n    (1, _, 3)                     : "pattern is (1, *, 3)".\n    oneof((1,), (1, 2), (1, 2, 3)): "one of (1,) | (1, 2) | (1, 2, 3)",\n    (1, 2, 3)                     : "(1, 2, 3)"\n}\n```\n',
    'author': 'Seonghyeon Kim',
    'author_email': 'k.seonghyeon@mymusictaste.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NovemberOscar/pymatched',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
