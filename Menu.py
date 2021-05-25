import pygame
from Controleur import *

class Menu:

    def __init__(self):
        self.surface = pygame.Surface(pygame.display.get_window_size())
        self.fnc_changer_menu = None


    def on_event(self, event:pygame.event.Event):
        pass

    def update(self):
        pass



class Accueil(Menu):

    _bouton_x_, _bouton_y_ = None, None
    _bouton_l_, _bouton_h_ = 150, 50

    def __init__(self):
        super().__init__()
        self._bouton_x_ = (self.surface.get_width() - self._bouton_l_) / 2
        self._bouton_y_ = (self.surface.get_height()-self._bouton_h_)/2



    def update(self):
        self.surface.fill([255]*3)
        bouton = pygame.Surface((self._bouton_l_, self._bouton_h_))
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        if self._bouton_x_ <= mouse_x <= self._bouton_x_+self._bouton_l_ and self._bouton_y_ <= mouse_y <= self._bouton_y_+self._bouton_h_:
            bouton.fill([255//4]*3)
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bouton.fill([0]*3)
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

        police = pygame.font.SysFont(pygame.font.get_default_font(), 24)
        txt = police.render("Joueur VS Joueur", True, [255] * 3)

        bouton.blit(txt, ((self._bouton_l_ - txt.get_width()) / 2, (self._bouton_h_ - txt.get_height()) / 2))
        self.surface.blit(bouton, (self._bouton_x_, self._bouton_y_))



    def on_event(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            if self._bouton_x_ <= mouse_x <= self._bouton_x_+self._bouton_l_ and self._bouton_y_ <= mouse_y <= self._bouton_y_+self._bouton_h_:
                self.fnc_changer_menu()
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


class Plateau(Menu):

    _grille_case_taille_ = 150
    _grille_case_contour_ = 5
    _grille_x, _grille_y_ = None, None
    _decalage_ = 10
    _controleur_:Controleur = None
    _case_police_:pygame.font.Font = None
    _police_:pygame.font.Font = None
    _score_ = [0, 0]
    _fini_ = False
    _rejouer_x_, rejouer_y_ = None, 10
    _rejouer_l_, _rejouer_h_ = 100, 50
    _accueil_x_, _accueil_y_ = 25, None
    _accueil_l_, _accueil_h_ = 100, 50
    _passe_btn_ = False

    def __init__(self):
        super().__init__()
        self._grille_x = (self.surface.get_width()-(3*(self._grille_case_taille_)+2*self._decalage_))/2
        self._grille_y_ = (self.surface.get_height()-(3*(self._grille_case_taille_)+2*self._decalage_))/2
        self._controleur_ = Controleur()
        self._case_police_ = pygame.font.SysFont(pygame.font.get_default_font(), 120)
        self._police_ = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        self._score_ = [0, 0]
        self._rejouer_x_ = self.surface.get_width()-150
        self._accueil_y_ = self.surface.get_height()-55



    def update(self):
        self.surface.fill([255]*3)

        (mouse_x, mouse_y) = pygame.mouse.get_pos()

        if self._passe_btn_:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


        self.surface.blit(self._police_.render("Score", True, [0]*3), (10, 10))
        self.surface.blit(self._police_.render(f"O: {self._score_[0]}", True, [0, 0, 255]), (10, 40))
        self.surface.blit(self._police_.render(f"X: {self._score_[1]}", True, [255, 0, 0]), (10, 70))

        rejouer = pygame.Surface((self._rejouer_l_, self._rejouer_h_))
        rejouer_txt = self._police_.render("Rejouer", True, [255] * 3)

        if not self._fini_:
            rejouer.fill([255//2]*3)
        else:
            if self._rejouer_x_ <= mouse_x <= self._rejouer_x_ + self._rejouer_l_ and self.rejouer_y_ <= mouse_y <= self.rejouer_y_ + self._rejouer_h_:
                rejouer.fill([255//3] * 3)
                self._passe_btn_ = True
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                rejouer.fill([0]*3)
                self._passe_btn_ = False

        rejouer.blit(rejouer_txt, ((self._rejouer_l_ - rejouer_txt.get_width()) / 2, (self._rejouer_h_ - rejouer_txt.get_height()) / 2))
        self.surface.blit(rejouer, (self._rejouer_x_, self.rejouer_y_))

        for i in range(3):
            for j in range(3):
                case_contour = pygame.Surface((self._grille_case_taille_, self._grille_case_taille_))
                case_contour.fill([0]*3)
                case = pygame.Surface((self._grille_case_taille_-2*self._grille_case_contour_, self._grille_case_taille_-2*self._grille_case_contour_))
                case.fill([255]*3)

                code = self._controleur_.obtenir_case(i, j)
                if code == 1:
                    txt = self._case_police_.render("O", True, [0, 0, 255])
                    case.blit(txt, ((case.get_width()-txt.get_width())/2, (case.get_height()-txt.get_height())/2 ))
                elif code == 2:
                    txt = self._case_police_.render("X", True, [255, 0, 0])
                    case.blit(txt, ((case.get_width() - txt.get_width()) / 2, (case.get_height() - txt.get_height()) / 2))

                case_contour.blit(case, (self._grille_case_contour_, self._grille_case_contour_))
                self.surface.blit(case_contour, (self._grille_x+j*(self._grille_case_taille_+self._decalage_), self._grille_y_+i*(self._grille_case_taille_+self._decalage_)))



        accueil = pygame.Surface((self._accueil_l_, self._accueil_h_))
        accueil_txt = self._police_.render("Accueil", True, [255]*3)

        if self._accueil_x_ <= mouse_x <= self._accueil_x_+self._accueil_l_ and self._accueil_y_ <= mouse_y <= self._accueil_y_+self._accueil_h_:
            accueil.fill([255//3]*3)
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            self._passe_btn_ = True
        else:
            accueil.fill([0]*3)
            self._passe_btn_ = False

        accueil.blit(accueil_txt, ((self._accueil_l_ - accueil_txt.get_width()) / 2, (self._accueil_h_ - accueil_txt.get_height()) / 2))
        self.surface.blit(accueil, (self._accueil_x_, self._accueil_y_))

        car = ""
        if self._controleur_.tour == 1:
            car = "O"
        else:
            car = "X"

        gagnant, coords = self._controleur_.gagnant()
        if gagnant > 0:
            txt = self._police_.render(f"Le joueur {gagnant}: a gagné", True, [0] * 3)

            a = self._grille_x+coords[0][1]*(self._grille_case_taille_+self._decalage_)+self._grille_case_taille_/2, self._grille_y_+coords[0][0]*(self._grille_case_taille_+self._decalage_)+self._grille_case_taille_/2
            b = self._grille_x+coords[2][1]*(self._grille_case_taille_+self._decalage_)+self._grille_case_taille_/2, self._grille_y_+coords[2][0]*(self._grille_case_taille_+self._decalage_)+self._grille_case_taille_/2
            pygame.draw.line(self.surface, [0]*3, a, b, 10)
        else:
            if self._fini_:
                txt = self._police_.render("Match nul !", True, [0] * 3)
            else:
                txt = self._police_.render(f"Tour du joueur {self._controleur_.tour}: {car}", True, [0]*3)



        self.surface.blit(txt, ((self.surface.get_width()-txt.get_width())/2, self.surface.get_height()-25))



    def on_event(self, event:pygame.event.Event):

        if event.type == pygame.MOUSEBUTTONUP:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            if self._accueil_x_ <= mouse_x <= self._accueil_x_ + self._accueil_l_ and self._accueil_y_ <= mouse_y <= self._accueil_y_ + self._accueil_h_:
                self.fnc_changer_menu()
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if not self._fini_:
                for i in range(3):
                    for j in range(3):
                        min_x = self._grille_x + j * (self._grille_case_taille_ + self._decalage_) + self._grille_case_contour_
                        max_x = min_x + self._grille_case_taille_ - self._grille_case_contour_

                        min_y = self._grille_y_ + i * (self._grille_case_taille_ + self._decalage_) + self._grille_case_contour_
                        max_y = min_y + self._grille_case_taille_ - self._grille_case_contour_
                        if min_x <= mouse_x <= max_x and min_y <= mouse_y <= max_y:
                            if self._controleur_.marquer_case(i, j):
                                self._controleur_.changer_tour()

                            gagnant = self._controleur_.gagnant()[0]
                            if gagnant > 0:
                                self._score_[gagnant-1] = self._score_[gagnant-1] + 1

                            self._fini_ = gagnant > 0 or self._controleur_.est_rempli()


            else:
                if self._rejouer_x_ <= mouse_x <= self._rejouer_x_+self._rejouer_l_ and self.rejouer_y_ <= mouse_y <= self.rejouer_y_+self._rejouer_h_:
                    self._fini_ = False
                    self._controleur_ = Controleur()
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)