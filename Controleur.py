from Grille import *

class Controleur:

	def __init__(self):
		self.grille = Grille()
		self.tour = 1

	def obtenir_case(self, ligne, colonne):
		"""
			ligne: indice de la ligne de la case
			colonne: indice de la colonne de la case
			retourne le code contenu dans la case (0: case vide, 1: rond, 2: croix)
			retourne -1 si les coordonnées de la case sont hors du tableau
		"""
		return self.grille.obtenir_case(ligne, colonne)


	def marquer_case(self, ligne, colonne):
		"""
			ligne: indice de la ligne de la case
			colonne: indice de la colonne de la case
			code: le code à inscrire dans la case (0: case vide, 1: rond, 2: croix)
			retourne True si la case a été marquée
			retourne False si la case n'est pas disponible ou si le code n'est pas valide
		"""
		return self.grille.marquer_case(ligne, colonne, self.tour)


	def changer_tour(self):
		"""
		Donne la main au deuxième joueur
		"""
		if self.tour == 1:
			self.tour = 2
		elif self.tour == 2:
			self.tour = 1


	def gagnant(self):
		"""
			retourne 0 s'il n'y a pas de gagnant
			retourne 1 si le joueur 1 a gagné
			retourne 2 si le joueur 2 a gagné
		"""
		return self.grille.gagnant()


	def est_rempli(self):
		"""
			retourne True si la grille est remplie
			sinon, retourne False
		"""
		return self.grille.est_rempli()