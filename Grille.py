class Grille:

	def __init__(self):
		self.plateau = [0]*3
		for i in range(3):
			self.plateau[i] = [0]*3




	def obtenir_case(self, ligne, colonne):
		"""
			ligne: indice de la ligne de la case
			colonne: indice de la colonne de la case
			retourne le code contenu dans la case (0: case vide, 1: rond, 2: croix)
			retourne -1 si les coordonnées de la case sont hors du tableau
		"""

		if (not (0 <= ligne < 3)) or (not(0 <= colonne < 3)):
			return -1

		return self.plateau[ligne][colonne]

	def marquer_case(self, ligne, colonne, code):
		"""
			ligne: indice de la ligne de la case
			colonne: indice de la colonne de la case
			code: le code à inscrire dans la case (0: case vide, 1: rond, 2: croix)
			retourne True si la case a été marquée
			retourne False si la case n'est pas disponible ou si le code n'est pas valide
		"""

		if self.obtenir_case(ligne, colonne) == 0 and 1 <= code <= 2:
			self.plateau[ligne][colonne] = code
			return True

		return False


	def gagnant(self):
		"""
			retourne 0 s'il n'y a pas de gagnant
			retourne 1 si le joueur 1 a gagné
			retourne 2 si le joueur 2 a gagné
		"""

		# On test ligne par ligne
		for l in range(3):
			if self.plateau[l] == [1]*3:
				return 1
			elif self.plateau[l] == [2]*3:
				return 2

		# On test colonne par colonne
		for col in range(3):
			T = []
			for l in range(3):
				T.append(self.plateau[l][col])

			if T == [1]*3:
				return 1
			elif T == [2]*3:
				return 2


		# On test les diagonales
		if self.plateau[0][0] == 1 and self.plateau[1][1] == 1 and self.plateau[2][2] == 1:
			return 1
		elif self.plateau[0][2] == 2 and self.plateau[1][1] == 2 and self.plateau[2][0] == 2:
			return 2


		# Pas de gagnant
		return 0


	def est_rempli(self):
		"""
			retourne True si la grille est remplie
			sinon, retourne False
		"""
		rempli = True
		for l in range(3):
			for col in range(3):
				if self.plateau[l][col] == 0:
					rempli = False
					break

		return rempli


	def afficher(self):
		"""
			Affiche le plateau de morpion
		"""
		msg = ""
		for l in range(3):
			for col in range(3):

				code = self.obtenir_case(l, col)
				if code == 0:
					msg += " "

				elif code == 1:
					msg += "O"

				elif code == 2:
					msg += "X"

				if col < 2:
					msg += "|"

			msg += "\n"

		return msg