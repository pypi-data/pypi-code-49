# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""


class Node:
    """
    Tous les agents ont les mêmes informations du jeu qui sont contenues dans un objet de type Node.
    Classe qui caractérise un noeud du jeu qui a:
    game, player, move=None, leaf_value=None
    On donne donc le jeu mais aussi le joueur qui a joué (pour bien se repérer dans le jeu)
    leaf_value est à none au début pour les noeuds.
    On fait remonter le leaf_value des feuilles vers le haut de l'arbre dans l'algorithme Minimax.
    """

    def __init__(self, game, player=None, move=None, leaf_value=None):
        self.game = game
        self.player = player
        self.move = move
        self.value = leaf_value

    def __repr__(self):
        """
        Pour récupérer un noeud, si on fait Node(...) on récupère tout ça:
        """
        return str((object.__repr__(self), self.game, self.player, self.move,
                    self.value))[1:-1]
