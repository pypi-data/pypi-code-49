# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 01:15:48 2019

@author: Nicolas
"""

"""
TODO
- Verification si il y a un mur des murs pendant la coupe : le mur doit etre considéré comme étant une pierre adversaire pendant la coupe
- Verifier si la coupe marche (sans etre a proximité d'un mur): coupe qui verifie si il y a une coupe 
- victoire qui compte les points de chaque joueur et qui renvoie le gagnant
"""


class Plateau():
    """
    Plateau de jeu représenté par une liste de listes (équivalent 
    d'un tableau à deux dimensions) de dimension 19x19.
    """
    
    tab = []
    
    def __init__(self):
        """
        Attributs de la classe Plateau :
            - nombre de colonnes
            - nombre de lignes
            - Joueur 1
            - Joueur 2
            - etat du jeu
        """
        self.ligne = 19
        self.colonne = 19
        self.j1 = 'A'
        self.j2 = 'B'
        self.fin = 0
        # Ajout de la liste pour obtenir un tableau à 2 dimensions.

        for i in range(self.ligne):
            self.tab.append([])
            for j in range(self.colonne):
                self.tab[i].append('.')

    def afficheJeu(self):
        """
        Affichage du plateau
        """

        print()
        
        print("\n       ------------------------------------------------------------------------\n")

        for i in range(self.ligne):
            for j in range(self.colonne):
                print(self.tab[i][j], end=' ')
            print()

    def verifChoix(self,ligne,colonne):
        """
        Délimite le placement de la pierre.

        Arguments : int, int
        """
        print(self.tab[ligne][colonne])
        if(self.tab[ligne][colonne]=='.'):
            return True
        else:
            return False

    def placerPierre(self,ligne,colonne,joueur):
        """
        Ajoute le caractère du joueur sur la case.

        Arguments : int, int, String
        """
        self.tab[ligne][colonne]=joueur

    def finDeJeu(self):
        if self.fin==2:
            return True
        else:
            return False
    
    def verifCoupe(self,ligne,colonne,joueur):
        liste = []
        tabCheckPoint = []
        liste.append([ligne,colonne])
        pierreUndo = 0
        while self.tab[ligne][colonne-1] != '.' or self.tab[ligne-1][colonne] != '.' or self.tab[ligne][colonne+1] != '.' or self.tab[ligne+1][colonne] != '.':
            
            if self.tab[ligne][colonne-1] != joueur and pierreUndo != 1:

                tabCheckPoint.append(ligne)
                tabCheckPoint.append(colonne-1)
                pierreUndo = 1
            
            if self.tab[ligne-1][colonne] != joueur and pierreUndo != 2:

                tabCheckPoint.append(ligne-1)
                tabCheckPoint.append(colonne)
                pierreUndo = 2

            if self.tab[ligne][colonne+1] != joueur and pierreUndo != 3:
                tabCheckPoint.append(ligne)
                tabCheckPoint.append(colonne+1)
                pierreUndo = 3

            if self.tab[ligne+1][colonne] != joueur and pierreUndo != 4:
                tabCheckPoint.append(ligne+1)
                tabCheckPoint.append(colonne)
                pierreUndo = 4

            if len(tabCheckPoint) != 0:
                colonne = tabCheckPoint.pop()
                ligne = tabCheckPoint.pop()

            else:
                for i in range(len(liste)):
                    self.tab[liste[i][0]][liste[i][1]] = '.'
                break
            liste.append([ligne,colonne]) 


    def coupe(self,ligne,colonne,joueur):
        
        if self.tab[ligne][colonne-1] != '.' or self.tab[ligne][colonne-1] != joueur:
            colonne-=1


            self.verifCoupe(ligne,colonne,joueur)

        if self.tab[ligne-1][colonne] != '.' or self.tab[ligne-1][colonne] != joueur:
            ligne-=1
            self.verifCoupe(ligne,colonne,joueur)
   

        if self.tab[ligne][colonne+1] != '.' or self.tab[ligne][colonne+1] != joueur:
            colonne+=1
            self.verifCoupe(ligne,colonne,joueur)

        if self.tab[ligne+1][colonne]!= '.' or self.tab[ligne+1][colonne != joueur]:
            ligne+=1
            self.verifCoupe(ligne,colonne,joueur)
            
        else:
            #useless
            return True

        print("Coupe !")


    def victoire(self): #TODO
        print("Victoire !")
        return True
        
    def tour(self, joueur):
        """
        Tour de jeu pour un joueur (poser une pierre).

        Arguments : String
        """

        print("\n-------------------------------------------------------------------------------")
        print("Joueur ", joueur, ", à vous de jouer !")
        print("-------------------------------------------------------------------------------\n")

        # Choix du joueur.
        choix = input("Voulez vous jouer votre tour ? (o/n) ")
        print()

        while True:
            if choix=='o':
                self.fin=0

                placerPierre = input("Ou placez-vous votre pierre ? (ligne,colonne) ").split(",")
                print()
                
                while len(placerPierre)<2:
                    placerPierre = input("Respecter la syntaxe (ligne,colonne) ").split(",")
                    print()
                
                ligne = int(placerPierre[0])
                colonne = int(placerPierre[1])

                while True:
                    if(self.verifChoix(ligne,colonne)):
                        self.placerPierre(ligne,colonne,joueur)
                        break
                    else:   
                        placerPierre = input("Cette case est dejà occupé, ou placez-vous votre pierre ? (ligne,colonne) ").split(",")
                        print()
                        ligne = int(placerPierre[0])
                        colonne = int(placerPierre[1])
                        
                self.coupe(ligne,colonne,joueur)
                break

            elif choix == 'n':
                self.fin+=1
                break

            else:
                choix = input("Veuillez respecter la syntaxe (o/n) ")
                print()

"""
Main.
"""

p = Plateau()

count = 0

#print(p.copy_game_state())

while p.finDeJeu() == False:
    if count % 2 == 0:
        p.afficheJeu()
        p.tour(p.j1)
        if p.finDeJeu():
            break 
    else:
        p.afficheJeu()
        p.tour(p.j2)

    count += 1

p.victoire()
