# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:55:19 2019

@author: Kevin
"""

class Joueur():
    """
    Classe Joueur qui permet au joueur de se déplacer à travers le plateau.
    """
    
    # Liste des déplacements possibles.
    deplacement = [[0,-2], [0,2], [-2,0], [2,0]]

    # Déplacements lorsqu'un joueur veut atteindre sa ligne d'arrivée.
    arrivee = [[0,-1], [0,1]]
    
    
    def __init__(self, l, posx, posy):
        """
        Constructeur.

        Attributs de la classe Joueur :
            - (argument) lettre correspondant au joueur
            - (argument) position du joueur en x
            - (argument) position du joueur en y
            - nombre de murs en possession
        """
        self.letter = l
        self.x = posx
        self.y = posy
        self.nbMur = 10
        
    
    def seDeplacer(self, choix, plateau):
        """
        Actualise la position du joueur en fonction de son choix.

        arguments : int, Plateau
        """

        # vérification de la possibilité de se déplacer
        self.verifDep(choix, plateau)

        # déplacement vers le haut (1)
        if(choix == 1):
            if(self.y == 1):
                self.x += self.arrivee[0][0]
                self.y += self.arrivee[0][1]
            else:
                self.x += self.deplacement[0][0]
                self.y += self.deplacement[0][1]
        
        # déplacement vers le bas (2)
        elif(choix == 2):
            if(self.y == plateau.ligne - 1):
                self.x += self.arrivee[1][0]
                self.y += self.arrivee[1][1]
            else:
                self.x += self.deplacement[1][0]
                self.y += self.deplacement[1][1]
        
        # déplacement vers la gauche (3)
        elif(choix == 3):
            self.x += self.deplacement[2][0]
            self.y += self.deplacement[2][1]
            
        # déplacement vers la droite (4)
        elif(choix == 4):
            self.x += self.deplacement[3][0]
            self.y += self.deplacement[3][1]
        # on invite le joueur à réessayer
        else:
            self.seDeplacer(int(input("Veuillez donner une reponse valide : ")), plateau)
        

    def verifDep(self, choix, plateau):
        """
        Vérifie qu'il n'y a pas de mur bloquant le joueur dans son déplacement.
        """
        if(choix == 1):
            if(plateau.tab[self.y + (self.deplacement[0][1] + 1)][self.x] == 1):
                print("Un mur se trouve devant vous, vous ne pouvez pas le traverser !")
                self.seDeplacer(int(input("Veuillez indiquer un autre déplacement : ")), plateau)
        elif(choix == 2):
            if(plateau.tab[self.y + (self.deplacement[1][1] - 1)][self.x] == 1):
                print("Un mur se trouve devant vous, vous ne pouvez pas le traverser !")
                self.seDeplacer(int(input("Veuillez indiquer un autre déplacement : ")), plateau)
        elif(choix == 3):
            if(plateau.tab[self.x + (self.deplacement[2][0] + 1)][self.y] == 1):
                print("Un mur se trouve devant vous, vous ne pouvez pas le traverser !")
                self.seDeplacer(int(input("Veuillez indiquer un autre déplacement : ")), plateau)
        elif(choix == 4):
            if(plateau.tab[self.x + (self.deplacement[3][0] - 1)][self.y] == 1):
                print("Un mur se trouve devant vous, vous ne pouvez pas le traverser !")
                self.seDeplacer(int(input("Veuillez indiquer un autre déplacement : ")), plateau)


    def retraitMur(self):
        """
        Retire les murs au joueur à mesure qu'il les pose.
        """

        self.nbMur -= 1
        print("Joueur ", self.letter, ", il vous reste ", self.nbMur, " murs.")

