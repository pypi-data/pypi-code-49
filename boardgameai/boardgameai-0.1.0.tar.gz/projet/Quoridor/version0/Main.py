# -*- coding: utf-8 -*-

from Plateau import *


class Main():
    """
    Crée un plateau de jeu.
    """


    p = Plateau()

    p.init_matrice()

    count = 0

    while(p.finDeJeu == False):
        p.initTabMurs()
        p.affichejeu()
        if(count % 2 == 0):
            p.tour(p.j1)
        else:
            p.tour(p.j2)
        
        count += 1
