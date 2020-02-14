# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:51:50 2019

@author: Kevin
"""

from draw_tree import draw_tree
from minimax_tree import Minimax
from game_tree import GameTree


players = ['Human', 'Bot']


class Nim():
    def __init__(self, nbAllumette, firstplayer=None):
        """
        Constructeur où on définit le jeu et le premier joueur
        """
        self.allumette = nbAllumette
        self.currentplayer = firstplayer

    def play_move(self, choice, currentplayer):
        """
        Methode pour jouer au jeu
        """
        self.currentplayer = currentplayer
        if (self.check_valid_move(choice)) and (
                choice not in self.invalid_moves()):
            self.allumette -= choice
        else:
            print("Vous ne pouvez pas effectuer cette action")
            self.play_move(int(input("Donnez un nombre valide : ")), player[0])

    def check_valid_move(self, choice):
        """
        Methode qui vérifie si le coup est valide
        """
        if (self.allumette - choice < 0 or self.allumette == 0):
            return False
        else:
            return True

    def invalid_moves(self):
        """
        Methode qui renvoie les coups impossibles
        """
        invalid = []
        invalid.append(0)
        if (self.allumette > 1
            ):  # s'il reste une allumette alors on peut jouer le coup de 1
            invalid.append(self.allumette)

        print("invalid moves" + str(invalid))
        return invalid

    def minimal_move(self):
        """
        Le coup minimal qu'on peut faire
        """
        return 1

    def check_current_state(self):
        """
        Methode qui vérifie l'état du jeu (victoire/défaite/match nul)
        """
        if (self.allumette != 0):
            return self.currentplayer, False
        else:
            # return le joueur courant: donc le gagnant et un booléen True: la partie est finie
            return self.currentplayer, True

    def current_state(self):
        """
        Pour connaitre l'état du jeu actuel
        """
        return self.allumette

    def gameover(self):
        """
        Message de fin de jeu
        """
        return ("Il n'y a plus d'allumette, victoire à " +
                str(self.check_current_state()[0]))


game = Nim(6)

gtree = GameTree(game)

nim_tree = gtree.create_tree(game, players[0])  # le premier joueur est humain

draw_tree(nim_tree)  # pour dessiner l'arbre

minimax = Minimax(nim_tree)

i = 0

player = players[0]

while ((game.check_current_state()[1]) == False):

    if i == 0:
        player = players[0]  # human
        print("___ " + player + " ___")

        print("Nombre restant d'allumettes " + str(game.current_state()))
        choix = int(input("Donner le nombre d'allumette : "))
        game.play_move(choix, player)
        print("\n")
    else:
        player = players[1]  # bot
        print("___ " + player + " ___")

        nim_tree = gtree.create_tree(game, players[1])
        choix = minimax.choose_move(nim_tree)
        game.play_move(choix, player)
        print("\n")

    i ^= 1

print(game.gameover())
