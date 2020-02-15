# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bubblegum']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4,<2.0',
 'click>=7.0,<8.0',
 'pyperclip>=1.7,<2.0',
 'requests>=2.0,<3.0']

entry_points = \
{'console_scripts': ['bubblegum = bubblegum.__main__:commands']}

setup_kwargs = {
    'name': 'bubblegum',
    'version': '1.0.0',
    'description': 'A script to make and manage uploads to image hosts.',
    'long_description': "# bubblegum\n\n[![Build Status](https://travis-ci.org/azuline/bubblegum.svg?branch=master)](https://travis-ci.org/azuline/bubblegum)\n[![Pypi](https://img.shields.io/pypi/v/bubblegum.svg)](https://pypi.python.org/pypi/bubblegum)\n[![Pyversions](https://img.shields.io/pypi/pyversions/bubblegum.svg)](https://pypi.python.org/pypi/bubblegum)\n\nbubblegum is a script to make and manage uploads to image hosts. Several image\nhosts are supported, to which one can directly upload images or rehost images\nby URL.\n\n## Usage\n\nBasic image uploading can be done via the `bubblegum upload` command. To upload\na local image file, run `bubblegum upload /path/to/image.png`. To rehost a URL,\nrun `bubblegum upload https://this.url.serves.an/image.png`.\n\nThe default image host is https://vgy.me, as it does not require client\nauthorization. The image host that will be used can be changed with the\n`--host` flag in the upload command, e.g. `bubblegum upload --host=imgur.com\n/path/to/image.png`. The default image host can also be changed in the config\nfile. Host options can be viewed with the `bubblegum upload --help` command.\n\nUploading/rehosting multiple images simultaneously is also supported, via\nmultiple arguments to the `upload` command. `bubblegum upload a.jpg b.png` will\nupload both images simultaneously. By default, 4 workers are spawned for image\nuploading. The number of workers can be increased or decreased in the config.\n\nA history of uploaded images can be viewed with `bubblegum history`. The\noutputted list can be manipulated with the `--sort`, `--limit` and `--offset`\noptions.\n\n### Config\n\nThe configuration can be edited with the `bubblegum config` command. A default\nconfiguration file is created when the script first runs.\n\n#### Image Host Profiles\n\nbubblegum includes loaded profiles for the following two hosts by default:\n\n- `imgur.com` (https://imgur.com)\n- `vgy.me` (https://vgy.me)\n\nOther image host profiles can be found in the `extra_profiles/` directory.\n\nImage host profiles can be created/added to the application by adding a profile\ndictionary to the list of `profiles` in your config file. Each profile must\ncontain 8 key/value pairs:\n\n- `image_host_name` - The name of the image host, for use with the `--host=`\n  option.\n- `image_host_url` - The URL of the host's image uploading endpoint.\n- `request_headers` - Extra headers to include in the upload request.\n- `upload_form_file_argument` - The name of the key for the image file in the\n  form.\n- `upload_form_data_argument` - A dictionary sent as the form data in a file\n  upload.\n- `rehost_form_url_argument` - If the host supports URL rehosting, the name of\n  the key for the URL in the form. Otherwise, set it to `null`.\n- `rehost_form_data_argument` - A dictionary sent as the form data in a URL\n  rehost.\n- `json_response` - A boolean indicating whether or not the returned data is\n  JSON or not. If True, the `data response` variable will be the deserialized\n  JSON. If False, the `data` request response variable will be the response\n  text.\n- `image_url_template` - A string of an f-string (yeah, sounds confusing) for\n  the image URL. Can access the request response via the `data` variable.\n- `deletion_url_template` - A string of an f-string for the deletion URL. Can\n  access the request response via the `data` variable.\n\n### Imgur\n\nTo upload to imgur, a Client ID must be created and supplied. Details on\ncreating a Client ID can be found at\nhttps://apidocs.imgur.com/#authorization-and-oauth. Once created, the Client ID\ncan be added to the config, as the `imgur_client_id`.\n",
    'author': 'azuline',
    'author_email': 'azuline@riseup.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/azuline/bubblegum',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
