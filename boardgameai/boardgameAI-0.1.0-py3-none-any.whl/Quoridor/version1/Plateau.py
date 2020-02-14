# coding=utf-8

from Joueur import *
from math import *

class Plateau():
    """Classe Plateau

    Le plateau de jeu est représenté par une liste de listes
    (càd un tableau à deux dimensions) de taille 19 * 17.
    """

    # Tableau représentant l'état des cases du plateau
    tabDeJeu = []

    # Flag indiquant la fin du jeu (initialisé à False)
    finDeJeu = False

    def __init__(self):
        """Constructeur de la classe Plateau

        Un plateau possède :
            - un nombre de ligne,
            - un nombre de colonnes,
            - deux joueurs.
        """

        self.ligne = 19
        self.colonne = 17
        self.j1 = Joueur('A', self.ligne-1, 1, 8)
        self.j2 = Joueur('B', 0, self.ligne-2, 8)

        self.initTabDeJeu()


    def initTabDeJeu(self):
        """Méthode initTabDeJeu

        Remplit le tableau :
            - de 5 pour la ligne d'arrivée du joueur B
            - de 7 pour la ligne d'arrivée du joueur A
            - de 0 pour les cases libres dédiées aux joueurs
            - de m pour les cases libres dédiées aux murs
        """

        for i in range(self.ligne):
            self.tabDeJeu.append([])

            if(i == 0):
                for j in range(self.colonne):
                    self.tabDeJeu[i].append(5)
            
            elif(i == self.ligne-1):
                for j in range(self.colonne):
                    self.tabDeJeu[i].append(7)
            
            elif(i % 2 == 0):
                for j in range(self.colonne):
                    self.tabDeJeu[i].append('m')
            
            else:
                for j in range(self.colonne):
                    if(j % 2 == 0):
                        self.tabDeJeu[i].append(0)
                    else:
                        self.tabDeJeu[i].append('m')
        
        # Ajout des joueurs sur le plateau de jeu
        self.tabDeJeu[self.j1.posY][self.j1.posX] = self.j1.identifiant
        self.tabDeJeu[self.j2.posY][self.j2.posX] = self.j2.identifiant
    

    def afficherTabDeJeu(self):
        """Méthode afficherTabDeJeu

        Affiche le plateau de jeu avec les coordonnées de chacune des cases.
        """

        # Numérotation des colonnes
        print("\n", end = '       ')

        for j in range(self.colonne):
            print(j, end = '   ')
        
        print("\n       ------------------------------------------------------------------------", end = '\n\n')

        # Numérotation des lignes et affichage du tableau de jeu
        for i in range(self.ligne):
            for j in range(self.colonne):

                # Numérotation des lignes comprenant un seul chiffre
                if(i < 10):
                    if(j == 0):
                        print("", i, end = ' |   ')
                
                # Numérotation des lignes comprenant deux chiffres
                elif(i > 9):
                    if(j == 0):
                        print(i, end = ' |   ')
                
                # Affichage des valeurs pour les colonnes comprenant un seul chiffre
                if(j < 10):
                    print(self.tabDeJeu[i][j], end = '   ')
                
                # Affichage des valeurs pour les colonnes comprenant deux chiffres
                elif(j > 9):
                    print(self.tabDeJeu[i][j], end = '    ')
            
            # Si c'est la dernière ligne
            if(i == self.ligne-1):
                print("\n")
            
            # Sinon
            else:
                print("\n   |")
    

    def victoire(self):
        """Méthode victoire

        Détermine la fin du jeu et le joueur gagnant.
        """

        if(self.j1.posY == self.ligne-1 or self.blocage(self.j1)):
            gagnant = self.j1
        elif(self.j2.posY == 0 or self.blocage(self.j2)):
            gagnant = self.j2
        else:
            gagnant = None

        if(gagnant is not None):
            print("\n-------------------------------------------------------------------------------")
            print("Joueur ", gagnant.identifiant, ", vous avez gagné !")
            print("-------------------------------------------------------------------------------\n")
            self.finDeJeu = True


    def numMurs(self):
        """Méthode numMurs

        Attribut un numéro à chacune des cases disponibles pour la pose d'un mur.
        """

        # Numérotation des cases
        num = 0

        # Tableau regroupant le résultat de l'attribution
        murs = []

        for i in range(1, self.ligne-2):
            for j in range(self.colonne-1):
                if(self.tabDeJeu[i][j] == 'm'):
                    num += 1
                    attribution = {'numéro': num, 'y': i, 'x': j}
                    murs.append(attribution)
                    print(attribution)
            
            print("\n")
        
        return murs


    def tour(self, joueur):
        """Méthode tour

        Lance le tour d'un joueur qui peut se déplacer ou poser un mur.
        """

        print("\n-------------------------------------------------------------------------------")
        print("Joueur ", joueur.identifiant, ", à vous de jouer !")
        print("-------------------------------------------------------------------------------\n")

        # Choix du joueur (o : se déplacer / n : poser un mur)
        choix = input("Voulez-vous déplacer votre pion ? (o/n) ")

        # Si le joueur entre 'o' ou 'O'
        if(choix == 'o' or choix == 'O'):
            print("Déplacements : Haut (1), Bas (2), Gauche (3), Droite (4)")
            deplacement = int(input("Choisissez un déplacement parmi 1, 2, 3 ou 4 : "))
            joueur.seDeplacer(deplacement, self)
        
        # Si le joueur entre 'n' ou 'N'
        elif(choix == 'n' or choix == 'N'):

            # S'il lui reste des murs à poser
            if(joueur.nbMurs > 0):
                murs = self.numMurs()
                num = int(input("Donnez le numéro de la position du mur à poser : "))
                joueur.poserMur(murs, num, self)
            
            # Sinon
            else:
                print("Vous êtes obligé de vous déplacer, il ne vous reste aucun mur à poser...")
                self.tour(joueur)
        
        # Si le joueur entre autre chose
        else:
            print("Réponse invalide, nous vous prions de recommencer...")
            self.tour(joueur)
        
        # On vérifie à chaque fin de tour si l'un des joueurs a gagné
        self.victoire()


    def initMatrice(self):
        """Méthode initMatrice

        Initialise la matrice d'adjacence du plateau de jeu.
        Ces états correspondent aux cases '0' voisines.
        """

        # Initialisation des variables
        matrice = {}
        voisins = []
        key = 1
        decalage = 9

        # On attribut une liste (des voisins) vide à chaque état
        for i in range(0, 83):
            matrice[i] = voisins

        for i in range(1, self.ligne-1):
            for j in range(0, self.colonne):
                if(self.tabDeJeu[i][j] == 0 or self.tabDeJeu[i][j] == 'A' or self.tabDeJeu[i][j] == 'B'):

                    # S'il n'y a pas de mur en haut
                    if(self.tabDeJeu[i-1][j] == 'm'):
                        voisins.append(key-decalage)

                    # Si on n'est pas sur la dernière colonne
                    if(j != self.colonne-1):
                        # S'il n'y a pas de mur à droite
                        if(self.tabDeJeu[i][j+1] == 'm'):
                            voisins.append(key+1)

                    # S'il n'y a pas de mur en bas
                    if(self.tabDeJeu[i+1][j] == 'm'):
                        voisins.append(key+decalage)

                    # Si on n'est pas sur la première colonne
                    if(j != 0):
                        # S'il n'y a pas de mur à gauche
                        if(self.tabDeJeu[i][j-1] == 'm'):
                            voisins.append(key-1)

                    # Réinitialisation
                    matrice[key] = voisins
                    voisins = []
                    key += 1

        # Ajout des voisins pour la ligne d'arrivée de 'B'
        matrice[0] = [1,2,3,4,5,6,7,8,9]

        # Ajout des voisins pour la ligne d'arrivée de 'A'
        matrice[82] = [81,80,79,78,77,76,75,74,73]

        for j in range(1, 10):
            matrice[j].append(0)

        for k in range(73, 82):
            matrice[k].append(82)

        for key in matrice:
            print(key, ' : ', matrice[key], end = '\n')

        return matrice


    def getNoeudJoueur(self, joueur):
        """Méthode getNoeudJoueur

        Détermine le numéro du noeud du joueur à partir de ses coordonnées.
        """

        return floor(joueur.posY/2)*9 + ceil((joueur.posX+1)/2)


    def cheminVersSortie(self, graphe, debut, fin, chemin):
        """Méthode cheminVersSortie

        Retourne un chemin de 'debut' vers 'fin' dans le 'graphe' s'il existe,
        Sinon retourne 'None'.
        """

        chemin.append(debut)

        if(debut == fin):
            return chemin

        if(debut not in graphe):
            return None

        for noeud in graphe[debut]:

            if(noeud not in chemin):
                newChemin = self.cheminVersSortie(graphe, noeud, fin, chemin)

                if(newChemin):
                    return newChemin

        return None


    def blocage(self, joueur):
        """Méthode blocage

        Vérifie si le 'joueur' est bloqué.
        """

        graphe = self.initMatrice()
        debut = self.getNoeudJoueur(joueur)
        chemin = []

        if(joueur is self.j1):
            fin = 82
        else:
            fin = 0

        if(self.cheminVersSortie(graphe, debut, fin, chemin) is not None):
            print(chemin)
            return False
        else:
            return True


    def copierEtatJeu(self):
        """Méthode copierEtatJeu

        Fait une copie du plateau à un instant t et la retourne.
        """

        etat = []

        for i in range(self.ligne):
            etat.append([])

            for j in range(self.colonne):
                etat[i].append(self.tabDeJeu[i][j])
        
        return etat

