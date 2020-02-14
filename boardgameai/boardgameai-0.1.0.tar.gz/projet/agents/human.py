# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""

from agents.agent import Agent
# les noeuds:
from agents.node import Node


class Human(Agent):
    """
    Agent humain, pour jouer manuellement
    """

    def choose_move(self, node):
        """
        Methode pour faire des choix en tant qu'humain
        """
        try:
            isinstance(node, Node)
        except AttributeError:
            raise Exception("AttributeError")

        consigne = node.game.currentphase
        consigne += " : "

        print(node.game.print_game())
        print("Choix disponibles :")
        # ───────────────────────────────────────────────────────────────── coups jouables
        i = 0
        j = 0
        while i < len(node.game.valid_moves()):
            print(i, ":", node.game.valid_moves()[i], end="")
            i += 1
            j += 1
            if j == 4:
                print("")
                j = 0
            elif i != len(node.game.valid_moves()):
                print(" | ", end="")
        print("")
        # ─────────────────────────────────────────────────────────────────
        print("[Aide] Choisissez selon l'index : de",
              0, "à", len(node.game.valid_moves())-1,)

        choix = input(consigne)

        while True:

            if choix.isdigit():
                choix = int(choix)
                if 0 <= choix < len(node.game.valid_moves()):
                    return node.game.valid_moves()[choix]
                else:
                    choix = input(consigne)
            else:
                choix = input(consigne)
