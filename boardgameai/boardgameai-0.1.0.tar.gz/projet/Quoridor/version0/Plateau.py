# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:44:48 2019

@author: Kevin
"""
from math import *
from Joueur import *

"""
TODO
- play_move qui prend un état, le joueur qui joue et le coup à jouer et qui renvoi l'état après ce coup
- check_current_state qui prend un état du jeu et qui renvoi le vainqueur et si le jeu est terminé/s'il y a une victoire
- check_playable qui prend une case en argument pour savoir si on peut jouer dessus (ex: savoir si la case est vide dans le tic tac toe)
"""

class Plateau():
	"""
	Plateau de jeu représenté par une liste de listes (équivalent 
	d'un tableau à deux dimensions) de dimension 19x17.
	"""
	
	tab = []
	tabMurs = []
	finDeJeu = False
	
	def __init__(self):
		"""
		Attributs de la classe Plateau :
			- nombre de colonnes
			- nombre de lignes
			- Joueur 1
			- Joueur 2
		"""
		self.ligne = 19
		self.colonne = 17
		self.j1 = Joueur('A', 8, 1)
		self.j2 = Joueur('B', 8, 17)
		

		# Ajout de la liste pour obtenir un tableau à 2 dimensions.

		for i in range(self.ligne):
			self.tab.append([])
			
			"""
			Remplissage du tableau :
				5 : zone d'arrivée pour le joueur B
				7 : zone d'arrivée pour le joueur A
				0 : cellule vide (pour les déplacements du joueur)
				m : cellule pour la pose des murs

			PS : schéma à l'appui pour plus de details.
			"""
			if(i == 0):
				for c in range(self.colonne):
					self.tab[i].append(5)
					
			elif(i == self.ligne - 1):
				for c in range(self.colonne):
					self.tab[i].append(7)
			elif(i % 2 == 0):
				for c in range(self.colonne):
					self.tab[i].append('m')
			else:
				for c in range(self.colonne):
					if(c % 2 == 0):
						self.tab[i].append(0)
					else:
						self.tab[i].append('m')
		

		# Ajout des joueurs au centre de chaque extrémité du plateau.

		self.tab[self.j1.y][self.j1.x] = self.j1.letter
		self.tab[self.j2.y][self.j2.x] = self.j2.letter
	
	
	def initTabMurs(self):
		"""
		Attribution d'un numéro pour chaque case où l'on peut poser un mur.
		"""

		num = 0

		for i in range(1, self.ligne-2):
			for j in range(self.colonne-1):
				if(((i % 2 != 0) and (j % 2 != 0)) or (i % 2 == 0)):
					num += 1
					dictCoordonnees = {'coordonneeY': i, 'coordonneeX': j}
					self.tabMurs.append(dictCoordonnees)
					print(num, " ", dictCoordonnees)
		
			print("\n")


	def victoire(self, joueur):
		"""
		On vérifie si le joueur actuel a atteint sa ligne d'arrivée (ligne de 
		7 pour A et ligne de 5 pour B) puis on affiche le message de victoire.

		Arguments : Joueur
		Return : boolean
		"""


		if(self.check_is_stuck(joueur) or (joueur.letter == 'A' and joueur.y == 18) or (joueur.letter == 'B' and joueur.y == 0)):
			print("\n-------------------------------------------------------------------------------")
			print("Joueur ", joueur.letter, ", vous avez gagné !")
			print("-------------------------------------------------------------------------------\n")

			return True
		else:
			return False


	def affichejeu(self):
		"""
		Affichage du plateau avec numérotation des lignes et des
		colonnes.
		"""

		print("\n      ", end=" ")
		for col in range(self.colonne):
			print(col, end="   ")
		
		print("\n       ------------------------------------------------------------------------\n")

		for i in range(self.ligne):
			for j in range(self.colonne):
				if(i < 10):
					if(j == 0):
						print("", i, end=" |   ")
					
					if(j < 10):
						print(self.tab[i][j], end="   ")
					elif(j > 9):
						print(self.tab[i][j], end="    ")
					
				elif(i > 9):
					if(j == 0):
						print(i, end=" |   ")
					
					if(j < 10):
						print(self.tab[i][j], end="   ")
					elif(j > 9):
						print(self.tab[i][j], end="    ")
			
			if i != 18:
				print("\n   |")
			else:
				print("\n")
			
	
	def enleveJoueur(self, joueur):
		"""
		Enlève le caractère du joueur de la cellule.

		Arguments : Joueur
		"""

		self.tab[joueur.y][joueur.x] = 0


	def placeJoueur(self, joueur):
		"""
		Ajoute le caractère du joueur sur la cellule.

		Arguments : Joueur
		"""

		self.tab[joueur.y][joueur.x] = joueur.letter


	def limitesDep(self, joueur, choix):
		"""
		Délimite les déplacements du joueur.

		Arguments : Joueur, int
		"""

		if((joueur.x == 0 and choix == 3) or (joueur.x == self.colonne - 1 and choix == 4)):
			return False
		else:
			return True
	

	def poserMur(self, joueur, murY, murX):
		"""
		Pose du mur aux coordonnées choisies par le joueur.

		Arguments : Joueur, int, int
		"""

		if(self.tab[murY][murX] == 'm'):

			if(murY % 2 != 0 and murX % 2 != 0 and self.tab[murY+1][murX] == 'm'):
				self.tab[murY+1][murX] = 1
			elif(murY % 2 == 0 and murX % 2 == 0 and self.tab[murY][murX+1] == 'm'):
				self.tab[murY][murX+1] = 1
			elif(murY % 2 == 0 and murX % 2 != 0):
				direction = input("Le mur doit-il être posé horizontalement ou verticalement ? (h/v) ")

				if(direction == 'h' or direction == 'H'):
					if(self.tab[murY][murX+1] == 'm'):
						self.tab[murY][murX+1] = 1
					else:
						print("Vous ne pouvez pas poser de mur à cet endroit-là...")

						"""
						coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

						murYtmp = int(coordonnees[0])
						murXtmp = int(coordonnees[1])

						self.poserMur(joueur, murYtmp, murXtmp)
						"""

						numero = int(input("Donnez le numéro de la position du mur à poser : "))
						self.poserMurIA(joueur, numero)

				elif(direction == 'v' or direction == 'V'):
					if(self.tab[murY+1][murX] == 'm'):
						self.tab[murY+1][murX] = 1
					else:
						print("Vous ne pouvez pas poser de mur à cet endroit-là...")

						"""
						coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

						murYtmp = int(coordonnees[0])
						murXtmp = int(coordonnees[1])

						self.poserMur(joueur, murYtmp, murXtmp)
						"""

						numero = int(input("Donnez le numéro de la position du mur à poser : "))
						self.poserMurIA(joueur, numero)

				else:
					print("Réponse invalide, nous vous prions de recommencer...")
					self.tour(joueur)

			else:
				print("Vous ne pouvez pas poser de mur à cet endroit-là...")

				"""
				coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

				murYtmp = int(coordonnees[0])
				murXtmp = int(coordonnees[1])
				
				self.poserMur(joueur, murYtmp, murXtmp)
				"""
				
				numero = int(input("Donnez le numéro de la position du mur à poser : "))
				self.poserMurIA(joueur, numero)

			self.tab[murY][murX] = 1
			joueur.retraitMur()

		else:
			print("Vous ne pouvez pas poser de mur à cet endroit-là...")

			"""
			coordonnees = input("Veuillez indiquer d'autres coordonnées : ").split(" ")

			murYtmp = int(coordonnees[0])
			murXtmp = int(coordonnees[1])

			self.poserMur(joueur, murYtmp, murXtmp)
			"""

			numero = int(input("Donnez le numéro de la position du mur à poser : "))
			self.poserMurIA(joueur, numero)


	def poserMurIA(self, joueur, num):
		"""
		Récupère les coordonnées du mur à poser à partir de son numéro.
		"""

		murY = self.tabMurs[num-1]['coordonneeY']
		murX = self.tabMurs[num-1]['coordonneeX']

		self.poserMur(joueur, murY, murX)


	def tour(self, joueur):
		"""
		Tour de jeu pour un joueur (se déplacer ou poser un mur).

		Arguments : Joueur
		"""

		print("\n-------------------------------------------------------------------------------")
		print("Joueur ", joueur.letter, ", à vous de jouer !")
		print("-------------------------------------------------------------------------------\n")

		# Choix du joueur.
		deplacerPion = input("Voulez-vous déplacer votre pion ? (o/n) ")

		# Si le joueur veut se déplacer.
		if(deplacerPion == 'o' or deplacerPion == 'O'):
			print("Déplacements : Haut (1), Bas (2), Gauche (3), Droite (4)")
			deplacement = int(input("Choisissez un déplacement parmi 1, 2, 3 ou 4 : "))

			if(self.limitesDep(joueur, deplacement) == True):
				self.enleveJoueur(joueur)
				joueur.seDeplacer(deplacement, self)
				self.placeJoueur(joueur)
			else:
				print("Vous êtes à l'extrémité du plateau ! Vous ne pouvez pas vous déplacer à cet endroit-là...")
				self.tour(joueur)

		elif(deplacerPion == 'n' or deplacerPion == "N"):
			"""
			coordonnees = input("Donnez les coordonnées du mur à poser (ligne puis colonne) séparées par un espace : ").split(" ")

			murY = int(coordonnees[0])
			murX = int(coordonnees[1])

			self.poserMur(joueur, murY, murX)
			"""

			numero = int(input("Donnez le numéro de la position du mur à poser : "))
			self.poserMurIA(joueur, numero)
			

		# Dans le cas d'une réponse erronée.
		else:
			print("Réponse invalide, nous vous prions de recommencer...")
			self.tour(joueur)
		
		# On vérifie à chaque fin de tour si le joueur actuel a gagné.
		if(self.victoire(joueur)):
			self.finDeJeu = True


	def copy_game_state(self):
		"""
		Fonction qui copie le plateau.
		Return : copie du plateau à l'instant t
		"""

		new_state = []

		for i in range(self.ligne):
			new_state.append([])

			for j in range(self.colonne):
				new_state[i].append(self.tab[i][j])

		return new_state


	def init_matrice(self):
		"""
		Fonction qui initialise le graphe à parcourir (composé des
		cases voisines sur lesquelles on peut jouer).
		"""

		# Initialisation
		matrice = {}
		voisins = []
		key = 1

		for i in range(0, 83):
			matrice[i] = voisins

		for i in range(1, self.ligne-1):
			for j in range(0, self.colonne):
				if(self.tab[i][j] == 0 or self.tab[i][j] == 'A' or self.tab[i][j] == 'B'):
					if(self.tab[i-1][j] == 'm'):
						voisins.append(key-9)
					if(j != self.colonne-1):
						if(self.tab[i][j+1] == 'm'):
							voisins.append(key+1)
					if(self.tab[i+1][j] == 'm'):
						voisins.append(key+9)
					if(j != 0):
						if(self.tab[i][j-1] == 'm'):
							voisins.append(key-1)

					# Réinitialisation
					matrice[key] = voisins
					voisins = []
					key += 1

		matrice[0] = [1,2,3,4,5,6,7,8,9]
		matrice[82] = [81,80,79,78,77,76,75,74,73]

		for j in range(1, 10):
			matrice[j].append(0)

		for k in range(73, 82):
			matrice[k].append(82)

		for key in matrice:
			print(key, ' : ', matrice[key], end='\n')

		return matrice


	def find_path(self, graph, start, end, path):
		path.append(start)

		if start == end:
			return path
		if start not in graph:
			return None
		for node in graph[start]:
			if node not in path:
				newpath = self.find_path(graph, node, end, path)
				if newpath: return newpath

		return None


	def get_node_player(self, joueur):
		# à déterminer car calcul actuel faux
		return (((joueur.y-1)/2)*9) + ceil(joueur.x/2)


	def check_is_stuck(self, joueur):
		graph = self.init_matrice()
		start = self.get_node_player(joueur)
		path = []

		if(joueur.letter == 'A'):
			end = 82
		else:
			end = 0

		if(self.find_path(graph, start, end, path) == None):
			return True
		else:
			print(path)
			return False


	#def check_is_stuck(self, joueur):
		"""
		L'algorithme:

		On simule un personnage qui va d'abord aller tout droit vers le haut jusqu'à rencontrer un mur et on marque la case où il a rencontré le mur.
		A partir de cette case, il va à droite et il longe le mur.
		S'il retrouve la case marquée, on considèrera que le pion est bloqué.
		Sinon, après un certain nombre de déplacements, on considèrera que le joueur n'est pas bloqué.
		"""

		"""
		jAventurier = Joueur('T', joueur.x, joueur.y)

		haut = 1
		bas = 2
		gauche = 3
		droite = 4

		nbMaxDeplacements = 10
		count = 0

		while(self.tab[jAventurier.y - 1][jAventurier.x] != 1 and count < nbMaxDeplacements):
			if(self.limitesDep(jAventurier, haut) == True):
				joueur.seDeplacer(haut, self)
				count += 1

		posXPremierMur = jAventurier.x
		posYPremierMur = jAventurier.y

		while(self.tab[jAventurier.y][jAventurier.x + 1] != 1 and count < nbMaxDeplacements):
			if(self.limitesDep(jAventurier, droite) == True):
				joueur.seDeplacer(droite, self)
				count += 1
			if(self.tab[jAventurier.y - 1][jAventurier.x] != 1):
				return False

		while(self.tab[jAventurier.y + 1][jAventurier.x] != 1 and count < nbMaxDeplacements):
			if(self.limitesDep(jAventurier, bas) == True):
				joueur.seDeplacer(bas, self)
				count += 1
			if(self.tab[jAventurier.y][jAventurier.x + 1] != 1):
				return False

		while(self.tab[jAventurier.y][jAventurier.x - 1] != 1 and count < nbMaxDeplacements):
			if(self.limitesDep(jAventurier, gauche) == True):
				joueur.seDeplacer(gauche, self)
				count += 1
			if(self.tab[jAventurier.y + 1][jAventurier.x] != 1):
				return False

		while(self.tab[jAventurier.y - 1][jAventurier.x] != 1 and count < nbMaxDeplacements):
			if(self.limitesDep(jAventurier, haut) == True):
				joueur.seDeplacer(haut, self)
				count += 1
			if(self.tab[jAventurier.y][jAventurier.x - 1] != 1):
				return False

		if(jAventurier.x == posXPremierMur and jAventurier.y == posYPremierMur):
			return True
		else:
			return False
	"""
