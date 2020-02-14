# coding=utf-8

from Plateau import *

class Main():
    """Classe Main

    Lance le jeu.
    """

    p = Plateau()
    compteur = 0

    while(p.finDeJeu is False):
        p.afficherTabDeJeu()

        if(compteur % 2 == 0):
            p.tour(p.j1)
        else:
            p.tour(p.j2)
        
        compteur += 1

