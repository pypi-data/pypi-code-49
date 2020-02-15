# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['desdeo_emo',
 'desdeo_emo.EAs',
 'desdeo_emo.Problem',
 'desdeo_emo.othertools',
 'desdeo_emo.population',
 'desdeo_emo.recombination',
 'desdeo_emo.selection',
 'desdeo_emo.surrogatemodelling']

package_data = \
{'': ['*']}

install_requires = \
['desdeo-problem>=0.10.0,<0.11.0',
 'desdeo-tools>=0.2.0,<0.3.0',
 'diversipy>=0.8.0,<0.9.0',
 'numpy>=1.16,<2.0',
 'optproblems>=1.2,<2.0',
 'pandas>=0.25,<0.26',
 'plotly>=4.1,<5.0',
 'pyDOE>=0.3.8,<0.4.0',
 'pygmo>=2.10,<3.0',
 'scikit-learn>=0.21.2,<0.22.0',
 'scipy>=1.2,<2.0']

setup_kwargs = {
    'name': 'desdeo-emo',
    'version': '0.4.0',
    'description': 'The python version reference vector guided evolutionary algorithm.',
    'long_description': '# desdeo-emo\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/industrial-optimization-group/desdeo-emo/master)\n\nThe evolutionary algorithms package within the `desdeo` framework.\n\nCurrently supported:\n* Multi-objective optimization with visualization and interaction support.\n* Preference is accepted as a reference point.\n* Surrogate modelling (neural networks and genetic trees) evolved via EAs.\n* Surrogate assisted optimization\n\nCurrently _NOT_ supported:\n* Constraint handling\n\nThe documentation is currently being worked upon\n\nTo test the code, open the [binder link](https://mybinder.org/v2/gh/industrial-optimization-group/desdeo-emo/master) and read example.ipynb.\n\nRead the documentation [here](https://pyrvea.readthedocs.io/en/latest/)\n\n### Requirements:\n* Python 3.7 or up\n* [Poetry dependency manager](https://github.com/sdispater/poetry): Only for developers\n\n### Installation process for normal users:\n* Create a new virtual enviroment for the project\n* Run: `pip install desdeo_emo`\n\n### Installation process for developers:\n* Download and extract the code or `git clone`\n* Create a new virtual environment for the project\n* Run `poetry install` inside the virtual environment shell.\n\n## See the details of various algorithms in the following papers (to be updated)\n\nR. Cheng, Y. Jin, M. Olhofer and B. Sendhoff,\nA Reference Vector Guided Evolutionary Algorithm for Many-objective\nOptimization, IEEE Transactions on Evolutionary Computation, 2016\n\nThe source code of pyrvea is implemented by Bhupinder Saini\n\nIf you have any questions about the code, please contact:\n\nBhupinder Saini: bhupinder.s.saini@jyu.fi\\\nProject researcher at University of Jyväskylä.',
    'author': 'Bhupinder Saini',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
