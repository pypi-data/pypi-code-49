# coding=utf-8

class Joueur():
    """Classe Joueur

    Deux joueurs sont créés et positionnés aux extrémités du plateau de jeu.
    """


    # Liste des déplacements possibles
        # -4 : à gauche ou en haut (saute-mouton)
        # -2 : à gauche ou en haut
        # -1 : en haut (pour atteindre la ligne d'arrivée)
        # 1 : en bas (pour atteindre la ligne d'arrivée)
        # 2 : à droite ou en bas
        # 4 : à droite ou en bas (saute-mouton)
    deplacements = [-4, -2, -1, 1, 2, 4]


    def __init__(self, i, a, y, x):
        """Constructeur de la classe Joueur

        Un joueur possède:
            - un identifiant permettant de le distinguer,
            - une ligne d'arrivee à franchir pour gagner,
            - une position x (colonne),
            - une position y (ligne),
            - un nombre de mur à poser.
        """

        self.identifiant = i
        self.arrivee = a
        self.posX = x
        self.posY = y
        self.nbMurs = 10


    def seDeplacer(self, choix, plateau):
        """Méthode seDeplacer

        Actualise la position du joueur en fonction :
            - de son choix,
            - des murs posés,
            - des limites du plateau.
        """

        # Efface l'ancienne position du joueur sur le plateau de jeu
        plateau.tabDeJeu[self.posY][self.posX] = 0


        # Cas d'un déplacement vers le haut (choix = 1)
        if(choix == 1):

            # Pour atteindre la ligne d'arrivée
            if(self.posY == 1):
                self.posY += self.deplacements[2]
            
            else:
                # Cas général
                if(plateau.tabDeJeu[self.posY-1][self.posX] != 1):
                    if(plateau.tabDeJeu[self.posY-2][self.posX] == 0):
                        self.posY += self.deplacements[1]
                    
                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY-3][self.posX] != 1):
                            self.posY += self.deplacements[0]
                        else:
                            self.message("mur", plateau)
                else:
                    self.message("mur", plateau)
        

        # Cas d'un déplacement vers le bas (choix = 2)
        elif(choix == 2):

            # Pour atteindre la ligne d'arrivée
            if(self.posY == plateau.ligne-2):
                self.posY += self.deplacements[3]
            
            else:
                # Cas général
                if(plateau.tabDeJeu[self.posY+1][self.posX] != 1):
                    if(plateau.tabDeJeu[self.posY+2][self.posX] == 0):
                        self.posY += self.deplacements[4]
                    
                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY+3][self.posX] != 1):
                            self.posY += self.deplacements[5]
                        else:
                            self.message("mur", plateau)
                else:
                    self.message("mur", plateau)


        # Cas d'un déplacement vers la gauche (choix = 3)
        elif(choix == 3):

            # Cas où le joueur se trouve à l'extrémité gauche du plateau
            if(self.posX == 0):
                self.message("limite", plateau)
            
            else:
                # Cas général
                if(plateau.tabDeJeu[self.posY][self.posX-1] != 1):
                    if(plateau.tabDeJeu[self.posY][self.posX-2] == 0):
                        self.posX += self.deplacements[1]
                    
                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY][self.posX-3] != 1):
                            self.posX += self.deplacements[0]
                        else:
                            self.message("mur", plateau)
                else:
                    self.message("mur", plateau)
        

        # Cas d'un déplacement vers la droite (choix = 4)
        elif(choix == 4):

            # Cas où le joueur se trouve à l'extrémité droite du plateau
            if(self.posX == plateau.colonne-1):
                self.message("limite", plateau)
            
            else:
                # Cas général
                if(plateau.tabDeJeu[self.posY][self.posX+1] != 1):
                    if(plateau.tabDeJeu[self.posY][self.posX+2] == 0):
                        self.posX += self.deplacements[4]
                    
                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY][self.posX+3] != 1):
                            self.posX += self.deplacements[5]
                        else:
                            self.message("mur", plateau)
                else:
                    self.message("mur", plateau)
        

        # Cas où le joueur entre une autre valeur que celles autorisées
        else:
            self.message("invalide", plateau)
        
        
        # Ajoute la nouvelle position du joueur sur le plateau de jeu
        plateau.tabDeJeu[self.posY][self.posX] = self.identifiant


    def message(self, erreur, plateau):
        """Méthode message

        Affiche un message d'erreur :
            - soit lorsqu'un mur sépare le joueur de la case dans laquelle il veut se déplacer,
            - soit lorsque le joueur est à l'extrémité du plateau et qu'il veut la dépasser.
        
        Ensuite, demande au joueur de faire un autre choix.
        """

        # Cas où l'erreur est due à une réponse invalide
        if(erreur == "invalide"):
            self.seDeplacer(int(input("Veuillez donner une reponse valide : ")), plateau)
        
        else:
            # Cas où l'erreur est due à un mur
            if(erreur == "mur"):
                print("Un mur se trouve devant vous, vous ne pouvez pas le traverser !")
            
            # Cas où l'erreur est due aux extrémités du plateau
            else:
                print("Vous êtes à l'extrémité du plateau, vous ne pouvez pas aller plus loin !")
            
            self.seDeplacer(int(input("Veuillez indiquer un autre déplacement : ")), plateau)


    def poserMur(self, murs, num, plateau):
        """Méthode poserMur

        Pose un mur sur la case dont le numéro est celui choisi.
        """

        murY = murs[num-1]['y']
        murX = murs[num-1]['x']
        print("y : ", murY, " x : ", murX)

        if(plateau.tabDeJeu[murY][murX] == 'm'):

            # Si le joueur peut poser un mur horizontalement et verticalement
            if(plateau.tabDeJeu[murY+1][murX] == 'm' and plateau.tabDeJeu[murY][murX+1] == 'm'):
                direction = input("Le mur doit-il être posé horizontalement ou verticalement ? (h/v) ")

                # Si le joueur entre 'h' ou 'H'
                if(direction == 'h' or direction == 'H'):
                    plateau.tabDeJeu[murY][murX+1] = 1
                
                # Si le joueur entre 'v' ou 'V'
                elif(direction == 'v' or direction == 'V'):
                    plateau.tabDeJeu[murY+1][murX] = 1
                
                # Si le joueur entre autre chose
                else:
                    self.poserMur(murs, int(input("Réponse invalide, veuillez indiquer de nouveau le numéro de la position du mur à poser : ")), plateau)
            
            # Si le joueur peut poser un mur horizontalement
            elif(plateau.tabDeJeu[murY][murX+1] == 'm'):
                plateau.tabDeJeu[murY][murX+1] = 1
            
            # Si le joueur peut poser un mur verticalement
            elif(plateau.tabDeJeu[murY+1][murX] == 'm'):
                plateau.tabDeJeu[murY+1][murX] = 1
            
            # Si le joueur ne peut pas poser de mur ni horizontalement ni verticalement (à cause de la deuxième case)
            else:
                print("Vous ne pouvez pas poser de mur à cet endroit-là...")
                self.poserMur(murs, int(input("Veuillez indiquer un autre numéro pour la position du mur à poser : ")), plateau)
            
            # Lorsqu'au moins l'une des conditions ci-dessus est satisfaite
            plateau.tabDeJeu[murY][murX] = 1
            self.retraitMur()
        
        # Si le joueur ne peut pas poser de mur (à cause de la première case)
        else:
            print("Vous ne pouvez pas poser de mur à cet endroit-là...")
            self.poserMur(murs, int(input("Veuillez indiquer un autre numéro pour la position du mur à poser : ")), plateau)


    def retraitMur(self):
        """Méthode retraitMur

        Décrémente le stock des murs à poser du joueur.
        """

        self.nbMurs -= 1
        print("Joueur ", self.identifiant, ", il vous reste ", self.nbMurs, " murs.")

