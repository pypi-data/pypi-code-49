# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypeln', 'pypeln.process', 'pypeln.task', 'pypeln.thread']

package_data = \
{'': ['*']}

install_requires = \
['pytest-sugar>=0.9.2,<0.10.0']

setup_kwargs = {
    'name': 'pypeln',
    'version': '0.2.0',
    'description': '',
    'long_description': '# Pypeln\n\n_Pypeln (pronounced as "pypeline") is a simple yet powerful python library for creating concurrent data pipelines._\n\n* **Simplicity**: Pypeln was designed to solve _medium_ data tasks that require parallelism and concurrency but where using frameworks like Spark or Dask feels exaggerated or unnatural.\n* **Easy-to-use**: Pypeln exposes a familiar functional API compatible with regular Python code.\n* **Flexible**: Pypeln enables you to build pipelines using Processes, Threads and asyncio.Tasks via the exact same API.\n* **Fine-grained Control**: Pypeln allows you to have control over the memory and cpu resources used at each stage of your pipeline.\n\n## Installation\n\nInstall Pypeln using pip:\n```bash\npip install pypeln\n```\n\n## Basic Usage\nWith Pypeln you can easily create multi-stage data pipelines using 3 type of workers:\n\n### Processes\nYou can create a pipeline based on [multiprocessing.Process](https://docs.python.org/3.4/library/multiprocessing.html#multiprocessing.Process) workers by using the `process` module:\n\n```python\nimport pypeln as pl\nimport time\nfrom random import random\n\ndef slow_add1(x):\n    time.sleep(random()) # <= some slow computation\n    return x + 1\n\ndef slow_gt3(x):\n    time.sleep(random()) # <= some slow computation\n    return x > 3\n\ndata = range(10) # [0, 1, 2, ..., 9] \n\nstage = pl.process.map(slow_add1, data, workers = 3, maxsize = 4)\nstage = pl.process.filter(slow_gt3, stage, workers = 2)\n\ndata = list(stage) # e.g. [5, 6, 9, 4, 8, 10, 7]\n```\nAt each stage the you can specify the numbers of `workers`. The `maxsize` parameter limits the maximum amount of elements that the stage can hold simultaneously.\n\n### Threads\nYou can create a pipeline based on [threading.Thread](https://docs.python.org/3/library/threading.html#threading.Thread) workers by using the `thread` module:\n```python\nimport pypeln as pl\nimport time\nfrom random import random\n\ndef slow_add1(x):\n    time.sleep(random()) # <= some slow computation\n    return x + 1\n\ndef slow_gt3(x):\n    time.sleep(random()) # <= some slow computation\n    return x > 3\n\ndata = range(10) # [0, 1, 2, ..., 9] \n\nstage = pl.thread.map(slow_add1, data, workers = 3, maxsize = 4)\nstage = pl.thread.filter(slow_gt3, stage, workers = 2)\n\ndata = list(stage) # e.g. [5, 6, 9, 4, 8, 10, 7]\n```\nHere we have the exact same situation as in the previous case except that the worker are Threads.\n\n### Tasks\nYou can create a pipeline based on [asyncio.Task](https://docs.python.org/3.4/library/asyncio-task.html#asyncio.Task) workers by using the `task` module:\n```python\nimport pypeln as pl\nimport asyncio\nfrom random import random\n\nasync def slow_add1(x):\n    await asyncio.sleep(random()) # <= some slow computation\n    return x + 1\n\nasync def slow_gt3(x):\n    await asyncio.sleep(random()) # <= some slow computation\n    return x > 3\n\ndata = range(10) # [0, 1, 2, ..., 9] \n\nstage = pl.task.map(slow_add1, data, workers = 3, maxsize = 4)\nstage = pl.task.filter(slow_gt3, stage, workers = 2)\n\ndata = list(stage) # e.g. [5, 6, 9, 4, 8, 10, 7]\n```\nConceptually similar but everything is running in a single thread and Task workers are created dynamically.\n\n## Mixed Pipelines\nYou can create pipelines using different worker types such that each type is the best for its given task so you can get the maximum performance out of your code:\n```python\ndata = get_iterable()\ndata = pl.task.map(f1, data, workers = 100)\ndata = pl.thread.flat_map(f2, data, workers = 10)\ndata = filter(f3, data)\ndata = pl.process.map(f4, data, workers = 5, maxsize = 200)\n```\nNotice that here we even used a regular python `filter`, since stages are iterables Pypeln integrates smoothly with any python code, just be aware of how each stage behaves.\n\n\n## Pipe Operator\nIn the spirit of being a true pipeline library, Pypeln also lets you create your pipelines using the pipe `|` operator:\n\n```python\ndata = (\n    range(10)\n    | pl.process.map(slow_add1, workers = 3, maxsize = 4)\n    | pl.process.filter(slow_gt3, workers = 2)\n    | list\n)\n```\n\n## Benchmarks\n* [Making an Unlimited Number of Requests with Python aiohttp + pypeln](https://medium.com/@cgarciae/making-an-infinite-number-of-requests-with-python-aiohttp-pypeln-3a552b97dc95)\n    * [Code](https://github.com/cgarciae/pypeln/tree/master/benchmarks/100_million_downloads)\n\n\n## Related Stuff\n* [mpipe](https://vmlaker.github.io/mpipe/)\n* [Process Pools](https://docs.python.org/3.4/library/multiprocessing.html?highlight=process#module-multiprocessing.pool)\n* [Making 100 million requests with Python aiohttp](https://www.artificialworlds.net/blog/2017/06/12/making-100-million-requests-with-python-aiohttp/)\n* [Python multiprocessing Queue memory management](https://stackoverflow.com/questions/52286527/python-multiprocessing-queue-memory-management/52286686#52286686)\n\n## Contributors\n* [cgarciae](https://github.com/cgarciae)\n\n## License\nMIT',
    'author': 'Cristian Garcia',
    'author_email': 'cgarcia.e88@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://cgarciae.github.io/pypeln',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
