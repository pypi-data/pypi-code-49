# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['video_utils']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.0,<0.5.0',
 'ffmpy>=0.2.2,<0.3.0',
 'pymediainfo>=4.1,<5.0',
 'tqdm>=4.40.2,<5.0.0']

setup_kwargs = {
    'name': 'video-utils',
    'version': '2.0.7',
    'description': 'This library is used for lots of shared functionality around parsing TV shows and movies',
    'long_description': '# Video Utils\n\n![Test Status](https://github.com/justin8/video_utils/workflows/Tests/badge.svg?branch=master)\n[![codecov](https://codecov.io/gh/justin8/video_utils/branch/master/graph/badge.svg)](https://codecov.io/gh/justin8/video_utils)\n\nThis library provides utilities for dealing with TV show and Movie files and the metadata around them.\n\n## Example Usage\n\n```python\nfrom video_utils import FileMap\n\nf = FileMap("/path/to/videos")\nf.load() # By default, this will load the cached metadata, and then update files that have changed in size\n\nfor directory in f.contents:\n    for video in f.contents[directory]:\n        codec = video.codec\n        print(codec.pretty_name) # x265\n        print(video.quality) # 1080p\n        print(video.full_path)\n        print(video.size) # in bytes\n        print(video)\n        video.refresh() # force a refresh of the video metadata, will only occur if filesize has changed.\n```\n',
    'author': 'Justin Dray',
    'author_email': 'justin@dray.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
