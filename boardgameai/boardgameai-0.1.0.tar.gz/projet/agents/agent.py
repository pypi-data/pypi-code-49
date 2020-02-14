# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Agent:
    __metaclass__ = ABCMeta
    """
    Classe abstraite représentant un agent jouant à un jeu
    """

    @abstractmethod
    def choose_move(self, node): pass
    """
    Methode pour faire des choix selon l'agent
    """


"""
Introduisons quelques terminologies.
1. Agent : Le résolveur de problèmes, peut effectuer certaines actions.
2. Environnement : Un agent réside ici. Un environnement fournit des réponses à un agent en fonction des actions qu'il effectue.
3. Récompense : Lorsqu'un agent effectue une action dans un environnement, il y a une récompense associée ; les récompenses peuvent être positives, négatives (punition) ou nulles.
4. État : L'action d'un agent peut le faire entrer dans un état qui est un instantané de l'environnement. (Comme échec et mat (état) sur un échiquier (environnement))
5. Politique : Définit le comportement d'un agent, peut répondre à des questions comme quelle action doit être effectuée dans cet état ?
6. Valeur : Suit l'impact à long terme de l'action. Fournit une partie de la récompense aux états intermédiaires qui ont conduit à un état final positif.
"""
