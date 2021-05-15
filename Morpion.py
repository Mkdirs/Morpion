from Controleur import *
import pygame


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
    pygame.init()
    screen = pygame.display.set_mode((1000, 720))
    pygame.display.set_caption("Morpion")
    font = pygame.font.SysFont(pygame.font.get_default_font(), 24)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        txt = font.render("Hello World", True, [0]*3)
        screen.blit(txt, (500-txt.get_width()/2, 720/2-txt.get_height()/2))
        pygame.display.update()

    pygame.quit()