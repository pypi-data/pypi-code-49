# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

from games.game import Game


class Nim(Game):
    def __init__(self, size):
        """
        Constructeur où on définit le jeu
        """
        self.players = ['Player1', 'Player2']  # liste des joueurs
        self.allumette = size         # le plateau
        self.currentplayer = None     # caractérise le dernier joueur qui a joué

        self.phases = []  # création des différentes phases
        # phase n°1: position du pion
        self.phases.append("Tirage allumettes")  # instruction de la phase 1
        self.currentphase = self.phases[0]  # la phase actuelle
        return

    def play_move(self, choice, currentplayer):  # utilisé par les agents
        """
        Methode pour jouer au jeu
        """
        self.currentplayer = currentplayer
        if choice in self.valid_moves():        # vérification supplémentaire mais normalement c'est forcément vrai
                                                # si on choisit un move parmis les valid_moves()
            self.allumette -= choice            # si ok on change l'état du jeu

    def valid_moves(self, all_moves=False):  # utilisé par les agents
        """
        Methode qui donne sous forme de liste tous les coups jouables possibles
        """
        moves = [
        ]  # tous les coups jouables sous forme de liste de nombres

        # On numérote les coups où l'on peut jouer
        if self.allumette <= 3:
            for i in range(self.minimal_move(),      # on peut choisir au maximum le reste des allumettes
                           self.allumette + 1):      # l'état actuel du jeu
                if (self.check_valid_move(i)):       # vérifie si ce move est valide
                    moves.append(i)
        else:
            for i in range(self.minimal_move(),
                           4):                       # on peut choisir au maximum 3 allumettes
                if (self.check_valid_move(i)):       # vérifie si ce move est valide
                    moves.append(i)

        # print("Coups jouables : " + str(moves))

        return moves

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if (self.allumette - choice < 0):
            return False
        else:
            return True

    def check_current_state(self):  # utilisé par les agents
        """
        Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
        On renvoit un booléen qui représente si le jeu est terminé: true sinon false
        """
        if (self.allumette != 0):
            return False
        else:
            return True

    def winner(self):  # utilisé par les agents
        """
        Methode pour récupérer le joueur victorieux
        Si le match est toujours en cours on retourne "None"
        """
        # le dernier joueur à avoir tiré la dernière allumette est le perdant
        if self.check_current_state():
            if self.currentplayer == self.players[0]:
                winner = self.players[1]
            else:
                winner = self.players[0]
            return winner
        else:
            return None

    def minimal_move(self):
        """
        Le choix minimal qu'on peut faire ici une allumette
        """
        return 1

    def print_game(self):  # utilisé par l'humain et les algorithmes d'apprentissage
        """
        Return the game board as string.
        Représente l'état du jeu pour le reinforcement learning.
        """
        return str("Allumettes restantes : " + str(self.allumette))
