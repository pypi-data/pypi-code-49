# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataget', 'dataget.toy', 'dataget.vision']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.4.0,<0.5.0',
 'httpx>=0.11.1,<0.12.0',
 'idx2numpy>=1.2.2,<2.0.0',
 'kaggle>=1.5.6,<2.0.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'tqdm>=4.42.1,<5.0.0']

setup_kwargs = {
    'name': 'dataget',
    'version': '0.4.2',
    'description': 'A framework-agnostic datasets library for Machine Learning research and education.',
    'long_description': '# Dataget\n\nDataget is an easy to use, framework-agnostic, dataset library that gives you quick access to a collection of Machine Learning datasets through a simple API.\n\nMain features:\n\n* **Minimal**: Downloads entire datasets with just 1 line of code.\n* **Compatible**: Loads data as `numpy` arrays or `pandas` dataframes which can be easily used with the majority of Machine Learning frameworks.\n* **Transparent**: By default stores the data in your current project so you can easily inspect it.\n* **Memory Efficient**: When a dataset doesn\'t fit in memory it will return metadata instead so you can iteratively load it.\n* **Integrates with Kaggle**: Supports loading datasets directly from Kaggle in a variety of formats.\n\nCheckout the [documentation](https://cgarciae.github.io/dataget/) for the list of available datasets.\n\n## Getting Started\n\nIn dataget you just have to do two things:\n\n* Instantiate a `Dataset` from our collection.\n* Call the `get` method to download the data to disk and load it into memory.\n\nBoth are usually done in one line:\n\n```python\nimport dataget\n\n\nX_train, y_train, X_test, y_test = dataget.vision.mnist().get()\n```\n\nThis example downloads the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset to `./data/vision_mnist` and loads it as `numpy` arrays.\n\n### Kaggle Support\n\nKaggle [promotes](https://www.kaggle.com/docs/datasets#supported-file-types) the use of `csv` files and `dataget` loves it! With dataget you can quickly download any dataset from the platform and have immediate access to the data:\n\n```python\nimport dataget\n\ndf_train, df_test = dataget.kaggle("cristiangarcia/pointcloudmnist2d").get(\n    files=["train.csv", "test.csv"]\n)\n```\nTo start using Kaggle datasets just make sure you have properly installed and configured the [Kaggle API](https://github.com/Kaggle/kaggle-api). In the future we want to expand Kaggle support in the following ways:\n\n* Be able to load any file that `numpy` or `pandas` can read.\n* Have generic support for other types of datasets like images, audio, video, etc. \n    * e.g `dataget.data.kaggle(..., type="vision").get(...)`\n\n\n## Installation\n\n`dataget` is available at [pypi](https://pypi.org/) so you can use your favorite package manager.\n\n##### pip\n```bash\npip install dataget\n```\n\n##### pipenv\n```bash\npipenv install pytest\n```\n##### poetry\n```bash\npoetry add dataget\n```\n\n## Contributing\n\nRead our guide on [Creating a Dataset](https://cgarciae.github.io/dataget/dataset/) if you are interested in adding a dataset to dataget.\n\n## License\nMIT License\n',
    'author': 'Cristian Garcia',
    'author_email': 'cgarcia.e88@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://cgarciae.github.io/dataget',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
