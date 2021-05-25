from Grille import *


class Controleur:
    _grille_ = None

    def __init__(self):
        self._grille_ = Grille()
        self.tour = 1

    def obtenir_case(self, ligne, colonne):
        """
			ligne: indice de la ligne de la case
			colonne: indice de la colonne de la case
			retourne le code contenu dans la case (0: case vide, 1: rond, 2: croix)
			retourne -1 si les coordonnées de la case sont hors du tableau
		"""
        return self._grille_.obtenir_case(ligne, colonne)

    def marquer_case(self, ligne, colonne):
        """
			ligne: indice de la ligne de la case
			colonne: indice de la colonne de la case
			retourne True si la case a été marquée
			retourne False si la case n'est pas disponible
		"""
        return self._grille_.marquer_case(ligne, colonne, self.tour)

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
			retourne le gagnant et les coordonnées des cases gagnantes
			retourne 0, [] s'il n'y a pas de gagnant
			retourne 1, [...] si le joueur 1 a gagné
			retourne 2, [...] si le joueur 2 a gagné
		"""
        return self._grille_.gagnant()

    def est_rempli(self):
        """
			retourne True si la grille est remplie
			sinon, retourne False
		"""
        return self._grille_.est_rempli()
