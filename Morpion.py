from Controleur import *

def jouer():
    controleur = Controleur()
    fini = False
    gagnant = 0
    print(controleur.grille.afficher())
    while not fini:
        print(f"Tour du joueur: {controleur.tour}")
        ligne = int(input("Ligne: "))
        colonne = int(input("Colonne: "))
        if controleur.marquer_case(ligne, colonne):
            print(controleur.grille.afficher())
            controleur.changer_tour()

        gagnant = controleur.gagnant()
        fini = gagnant > 0 or controleur.est_rempli()

    if gagnant > 0:
        print(f"Le gagnant est le joueur {gagnant} !")
    else:
        print("Pas de gagnant !")


    reponse = " "
    while reponse not in "oOnN":
        reponse = input("Rejouer ? (o/n): ")

    if reponse in "oO":
        jouer()



if __name__ == '__main__':
    jouer()