# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['projet',
 'projet.Go',
 'projet.Quoridor',
 'projet.Quoridor.version0',
 'projet.Quoridor.version1',
 'projet.agents',
 'projet.agents.apprentissage_RL',
 'projet.agents.optimisation_MinMax',
 'projet.agents.optimisation_MinMax.tree',
 'projet.games',
 'projet.games.TicTacToe_new',
 'projet.games.TicTacToe_old',
 'projet.utilities']

package_data = \
{'': ['*'],
 'projet.agents': ['apprentissage_RL/images/*', 'optimisation_MinMax/images/*']}

install_requires = \
['matplotlib>=3.1.3,<4.0.0']

setup_kwargs = {
    'name': 'boardgameai',
    'version': '0.1.0',
    'description': 'an API for playing turn by turn games using IA',
    'long_description': None,
    'author': 'Aurelien Castel',
    'author_email': 'dummy@g.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
