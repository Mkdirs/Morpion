import pygame
from Menu import *


def jouer():
    print("Prout !")
    """controleur = Controleur()
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
    """


MENU: Menu = None


def play():
    global MENU
    MENU = Plateau()
    MENU.fnc_changer_menu = home

def home():
    global MENU
    MENU = Accueil()
    MENU.fnc_changer_menu = play


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Morpion")
    screen = pygame.display.set_mode((1000, 720))

    home()
    running = True
    while running:

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False

            MENU.on_event(e)

        screen.fill([255] * 3)
        MENU.update()
        screen.blit(MENU.surface, (0, 0))

        pygame.display.flip()

    pygame.quit()
