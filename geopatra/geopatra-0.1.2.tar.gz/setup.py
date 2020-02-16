# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geopatra', 'geopatra.folium']

package_data = \
{'': ['*']}

install_requires = \
['folium>=0.10.1,<0.11.0', 'geopandas>=0.6.2,<0.7.0']

setup_kwargs = {
    'name': 'geopatra',
    'version': '0.1.2',
    'description': 'Interactive Maps with Geopandas ',
    'long_description': '![alt text](https://github.com/Sangarshanan/geopatra/blob/master/docs/_static/geopatra.png "Geopatra")\n\n![Travis (.org)](https://img.shields.io/travis/sangarshanan/geopatra?label=travis&logo=travis) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/sangarshanan/geopatra/Test?label=actions&logo=github) [![Documentation Status](https://readthedocs.org/projects/geopatra/badge/?version=latest)](https://geopatra.readthedocs.io/en/latest/?badge=latest) [![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/geopatra) [![image](https://img.shields.io/pypi/v/geopatra.svg)](https://pypi.org/project/geopatra/) \n\n\n> :warning: **This package is still an early protoype**: Will be working on making it better, beware of bad code  \n\n\nCreate Interactive maps 🗺️ with your geodataframe\n\nGeopatra attempts to wrap the goodness of Folium, Plotly, Kepler.gl and maybe even more amazing libraries (Bokeh, Altair) for rapidly creating interactive maps with Geodataframes\n\nYou can already create interactive maps easily with geopandas and Folium/ Plotly/ Kepler.gl. Geopatra is merely meant to make this easier and is more geared towards ease and currently does not support complex maps or intricate style control\n\n\n## Installation \n\nEverything is always a pip away\n\n```\npip install geopatra\n```\n\n## Basic Usage\n\nTo quickly plot a geodataframe with folium, you gotta understand workflows in geopandas and folium.\n\n```python\nimport folium\nimport geopandas\nworld = geopandas.read_file(geopandas.datasets.get_path(\'naturalearth_lowres\'))\nm = folium.Map(location = [4,10], zoom_start = 3)\nfolium.GeoJson(world.__geo_interface__).add_to(m)\n```\n\nWith Geopatra all the parameters you set with folium become optional so you don\'t have to care about folium   \n\n```python\nimport geopatra\nm = world.folium.plot()\n```\nNow you have a folium map object, which you can now use for more complex mapflows \n\nCheck out [docs](https://geopatra.readthedocs.io/en/latest/geopatra.html) for more examples\n\n## Development \n\nClone the repo\n```git\ngit clone git@github.com:Sangarshanan/geopatra.git\n```\n\nRun ```pre-commit install``` to install pre-commit into your git hooks. pre-commit will now run on every commit\n\nInstall the package with the amazing [poetry](https://github.com/python-poetry/poetry)\n\n```\npoetry install\n```\n\nMake the bla-bla-bla changes to code and run the tests, Once merged to master build and publish\n\n```\npoetry build\npoetry publish\n```\n\n',
    'author': 'sangarshanan',
    'author_email': 'sangarshanan1998@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Sangarshanan/geopatra',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
