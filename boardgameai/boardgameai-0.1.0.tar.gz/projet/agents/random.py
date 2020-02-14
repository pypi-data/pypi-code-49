"""
@author: Aurelien Castel
"""

import numpy as np
from random import randrange

from agents.agent import Agent
# les noeuds:
from agents.node import Node


class Random(Agent):
    """
    Agent qui sélectionne aléatoirement
    """

    def choose_move(self, node):
        """
        Methode pour faire des choix aléatoires
        """
        try:
            isinstance(node, Node)
        except AttributeError:
            raise Exception("AttributeError")

        random_index = randrange(len(node.game.valid_moves()))
        print("Coup décidé : " + str(node.game.valid_moves()[random_index]))
        return node.game.valid_moves()[random_index]
