import pygame
from pygame.locals import *
import random

pygame.init()

# Titre
pygame.display.set_caption("PONG")  # donner un titre à la fenêtre

# Mise en place Son
pygame.mixer.init()
ping = pygame.mixer.Sound("ping.mp3")
ping.play()

# Ouverture de la fenêtre Pygame
taille = largeur, hauteur = 1280, 720
fenetre = pygame.display.set_mode(taille)
taille_barre = 100

# Création des variables
font = pygame.font.Font(None, 80)
sub_font = pygame.font.Font(None, 30)
Money = 9000

# Mise en place de certaines couleurs
noir = 0, 0, 0
GREY = 200, 200, 200

# Boolean Boucle de jeux
continuer = 1

# Boolean lock Item Shop
locking = True
locking2 = True
locking3 = True
locking8 = False
locking9 = True
locking10 = True
locking11 = True
locking15 = False
locking16 = True

ball_name = "ball_unlock"
# Liste PowerUp
liste_powerup = ["Speed", 'Increased', "Decreased", "Speed"]

# Rafraîchissement de l'écran
pygame.display.flip()

# Mise en place d'image Présente dans différentes Fenetre
background = pygame.image.load("default_unlock.png")
background = pygame.transform.scale(background, (largeur, hauteur))

# Creation Liste Background
BG_List = ["default", "foot"]

# Mise en place Back Arrow
back_arrow = pygame.image.load("Back Arrow.png").convert_alpha()
back_arrow = pygame.transform.scale(back_arrow, (64, 64))
back_arrow_rect = back_arrow.get_rect()
back_arrow_rect.x = 10
back_arrow_rect.y = 650

# Chargement des barres
barre_gauche = pygame.image.load("barre_unlock.png").convert_alpha()
barre_gauche = pygame.transform.scale(barre_gauche, (15, taille_barre))
barrerect_gauche = barre_gauche.get_rect()
barrerect_gauche.x, barrerect_gauche.y = 10, 300

barre_droite = pygame.image.load("barre_unlock.png").convert_alpha()
barre_droite = pygame.transform.scale(barre_droite, (15, taille_barre))
barrerect_droite = barre_droite.get_rect()
barrerect_droite.x, barrerect_droite.y = 1255, 300


# Création de la Classe Power_Up (ajout d'evenement in game)
class Power_Up(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = liste_powerup[random.randint(0, len(liste_powerup) - 1)]
        self.image = pygame.image.load(f"{self.name}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

    # fonction qui va mettre le powerup en dehors de la fenetre
    def pos0(self):
        self.rect.x = -100
        self.rect.y = -100


# Creation de la classe qui va afficher les powerUp
class In_Game:
    def __init__(self):
        # ajout des differents powerup dans les Groupes
        self.SpeedGrp = pygame.sprite.Group()
        self.Increased = pygame.sprite.Group()
        self.Decreased = pygame.sprite.Group()

    # Fonction qui va afficher les powerUp
    def spawn_powerup(self):
        action = Power_Up()
        action.rect.x = random.randint(64, largeur - 64)
        action.rect.y = random.randint(64, hauteur - 64)
        if action.name == "Speed":
            self.SpeedGrp.add(action)

        if action.name == "Increased":
            self.Increased.add(action)

        if action.name == "Decreased":
            self.Decreased.add(action)


# Creation de la classe Balle qui va permettre la detection de collions entre la balle et les powerUp
# Classe qui va aussi faire apparaitre la balle
class Balle(pygame.sprite.Sprite):
    def __init__(self, name):
        super(Balle, self).__init__()
        self.image = pygame.image.load(f"{name}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.centery, self.rect.centerx = hauteur / 2, largeur / 2


# Creation des Items du Shop
class ItemShop(pygame.sprite.Sprite):
    def __init__(self, name, lock, cost, posx, posy, nametype):
        super(ItemShop, self).__init__()
        # Mise en place de leurs attributs
        self.name = name
        self.lock = lock
        self.cost = cost
        self.nametype = nametype

        # Generation d'un item
        self.image = pygame.image.load(f"{self.name}.png")

        # Generation des Items sauf ceux par default
        if not lock and self.name != "default_unlock":
            if not lock and self.name != "barre_unlock":
                if not lock and self.name != "ball_unlock":
                    self.image = pygame.image.load(f"{self.name}_unlock.png")

        # Mise en place d'un rect de base pour les images
        self.image_rect = self.image.get_rect()
        self.image_rect.x, self.image_rect.y = posx, posy
        # Creation du cadre de chaque images en fonction de leur type (background, bar, balle) et de leur propriété lock
        if not lock:
            if self.nametype == "background":
                self.image = pygame.transform.scale(self.image, (256, 144))
            elif self.nametype == "bar":
                self.image = pygame.transform.scale(self.image, (15, 144))
                self.image_rect.x, self.image_rect.y = posx + 120, posy
            elif self.nametype == "ball":
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.image_rect.x, self.image_rect.y = posx + 95, posy + 80
            else:
                self.image = pygame.transform.scale(self.image, (256, 144))

        if lock:
            self.image = pygame.transform.scale(self.image, (256, 144))
            self.image_rect = self.image.get_rect()
            self.image_rect.x, self.image_rect.y = posx, posy

        # Mise en place du bouton Buy
        self.BuyBt = pygame.image.load("Buy.png").convert_alpha()
        self.BuyBt = pygame.transform.scale(self.BuyBt, (128, 64))
        self.rect = self.BuyBt.get_rect()
        self.rect.x, self.rect.y = self.image_rect.x + 60, self.image_rect.y + 160

        # Mise en place du prix de l'Item
        text_Money = font.render("$" + str(self.cost), True, (180, 180, 180))
        if lock:
            fenetre.blit(self.BuyBt, self.rect)
            fenetre.blit(text_Money, (self.rect.x, self.rect.y - 220))

        # Mise en place du Bouton Select si déja acheter
        self.Select = pygame.image.load("Select.png").convert_alpha()
        self.Select = pygame.transform.scale(self.Select, (128, 64))
        self.rect_select = self.Select.get_rect()
        self.rect_select.x, self.rect_select.y = posx + 60, posy + 160
        if not lock:
            fenetre.blit(self.Select, self.rect_select)

    # Fonction Buy qui ne sert pas a grand chose
    def buy(self):
        self.Selected()

    # Fonction Selected qui va permettre de choisir l'item
    def Selected(self):
        global background
        global barre_gauche
        global barre_droite
        global ball_name
        # Mise en place de l'affichage des elements en fonction de leur type
        if self.nametype == "background":
            if self.name == "default_unlock":
                background = pygame.image.load(f"{self.name}.png")
            else:
                background = pygame.image.load(f"{self.name}_unlock.png")
            background = pygame.transform.scale(background, (1280, 720))
        if self.nametype == "bar":
            if self.name == "barre_unlock":
                barre_droite = pygame.image.load(f"{self.name}.png")
                barre_gauche = pygame.image.load(f"{self.name}.png")
            else:
                barre_droite = pygame.image.load(f"{self.name}_unlock.png")
                barre_gauche = pygame.image.load(f"{self.name}_unlock.png")

            barre_gauche = pygame.transform.scale(barre_gauche, (15, taille_barre))
            barre_droite = pygame.transform.scale(barre_droite, (15, taille_barre))
        if self.nametype == "ball":
            if self.name == "ball_unlock":
                ball_name = self.name
            else:
                ball_name = self.name + "_unlock"


# Creation du Menu Principale
def Menu(Argent):
    global barre_gauche, barre_droite
    # Variable permetant le fonctionnement de la boucle while
    continuer = True

    # remise a 100 de la taille de la barre
    barre_gauche = pygame.transform.scale(barre_gauche, (15, 100))
    barre_droite = pygame.transform.scale(barre_droite, (15, 100))
    # Mise en place du bouton Play Versus
    play = pygame.image.load("Play_versus.png").convert_alpha()
    play = pygame.transform.scale(play, (200, 100))
    playrect = play.get_rect()
    playrect.x, playrect.y = 540, 200

    # Mise en place du bouton Play Coop
    play_coop = pygame.image.load("Play_Coop.png").convert_alpha()
    play_coop = pygame.transform.scale(play_coop, (200, 100))
    play_coop_rect = play_coop.get_rect()
    play_coop_rect.x, play_coop_rect.y = 540, 320

    # Mise en place du bouton Shop
    Shop_Bt = pygame.image.load("Shop.png").convert_alpha()
    Shop_Bt = pygame.transform.scale(Shop_Bt, (64, 64))
    Shop_Bt_Rect = Shop_Bt.get_rect()
    Shop_Bt_Rect.x, Shop_Bt_Rect.y = 610, 440

    help_Bt = pygame.image.load("Help.png").convert_alpha()
    help_Bt = pygame.transform.scale(help_Bt, (108, 128))
    help_Bt_rect = help_Bt.get_rect()
    help_Bt_rect.x, help_Bt_rect.y = largeur - 130, hauteur - 130

    Ball = Balle(ball_name)
    Ball.rect.x = 200
    Ball.rect.y = 200
    vitesse = [3, 3]

    line = pygame.Surface((5, hauteur))

    while continuer:
        # Affichage du backGround et des autres éléments
        fenetre.blit(background, (0, 0))

        Ball.rect = Ball.rect.move(vitesse)
        fenetre.blit(line, (largeur / 2, 0))

        # Creation de rectangle de collision permettant le deplacement des barres de droite et gauche
        rectangle = pygame.Surface((largeur / 2, hauteur))
        rectangle.fill((255, 255, 255))
        rectangle.set_alpha(0)
        rectangle_rect = rectangle.get_rect()
        rectangle_rect.x = largeur / 2

        rectangle_gauche = pygame.Surface((largeur / 2, hauteur))
        rectangle_gauche.set_alpha(0)
        rectangle_gauche.fill((255, 255, 255))
        rectangle_gauche_rect = rectangle_gauche.get_rect()
        # Affichage de ses rectangles
        fenetre.blit(rectangle_gauche, (0, 0))
        fenetre.blit(rectangle, (largeur / 2, 0))

        fenetre.blit(play, playrect)
        fenetre.blit(play_coop, play_coop_rect)
        fenetre.blit(Shop_Bt, Shop_Bt_Rect)
        fenetre.blit(Ball.image, Ball.rect)
        fenetre.blit(help_Bt, help_Bt_rect)

        fenetre.blit(barre_gauche, barrerect_gauche)
        fenetre.blit(barre_droite, barrerect_droite)

        text_Money = font.render("$" + str(Argent), True, (200, 200, 200))
        fenetre.blit(text_Money, (20, 20))

        # Collision Contre les côtés
        if Ball.rect.right > largeur or Ball.rect.left < 0:
            vitesse[0] = -vitesse[0]

        if Ball.rect.top < 0 or Ball.rect.bottom > hauteur:  # changement de direction de la balle si atteint les bords bas ou ahut
            vitesse[1] = -vitesse[1]

        # Collision contre le Bouton Play Versus
        if Ball.rect.colliderect(playrect) and (Ball.rect.top < playrect.top and Ball.rect.colliderect(playrect
                                                                                                       ) or Ball.rect.bottom > playrect.bottom):
            vitesse[1] = -vitesse[1]
            vitesse[0] = -vitesse[0]

        if Ball.rect.colliderect(playrect) and (Ball.rect.right > playrect.left and Ball.rect.colliderect(
                playrect) or Ball.rect.left > playrect.right):
            vitesse[0] = -vitesse[0]

        # Collision contre le Bouton Play Coop
        if Ball.rect.colliderect(play_coop_rect) and (
                Ball.rect.top < play_coop_rect.top and Ball.rect.colliderect(play_coop_rect
                                                                             ) or Ball.rect.bottom > play_coop_rect.bottom):
            vitesse[1] = -vitesse[1]
        if Ball.rect.colliderect(play_coop_rect) and (Ball.rect.right > play_coop_rect.left and Ball.rect.colliderect(
                play_coop_rect) or Ball.rect.left > play_coop_rect.right):
            vitesse[0] = -vitesse[0]

        # Collision contre le bouton Shop
        if Ball.rect.colliderect(Shop_Bt_Rect) and (
                Ball.rect.top < Shop_Bt_Rect.top and Ball.rect.colliderect(Shop_Bt_Rect
                                                                           ) or Ball.rect.bottom > Shop_Bt_Rect.bottom):
            vitesse[1] = -vitesse[1]
        if Ball.rect.colliderect(Shop_Bt_Rect) and (Ball.rect.right > Shop_Bt_Rect.left and Ball.rect.colliderect(
                Shop_Bt_Rect) or Ball.rect.left < Shop_Bt_Rect.right):
            vitesse[0] = -vitesse[0]

        # Collision avec les barres
        if Ball.rect.colliderect(
                barrerect_gauche):  # changement de direction de la balle si atteint les bords gauche ou droit
            vitesse[0] = -vitesse[0]
            ping.play()

        if Ball.rect.colliderect(
                barrerect_droite):  # changement de direction de la balle si atteint les bords gauche ou droit
            vitesse[0] = -vitesse[0]
            ping.play()

        # Deplacement Verticale de la barre Droite

        if Ball.rect.colliderect(rectangle_rect) and barrerect_droite.top < Ball.rect.top:
            barrerect_droite.y += 3

        if Ball.rect.colliderect(rectangle_rect) and barrerect_droite.bottom > Ball.rect.bottom:
            barrerect_droite.y -= 3

        if barrerect_droite.bottom > hauteur:
            barrerect_droite.y = hauteur - 101

        # Deplacement Verticale de la barre Droite

        if Ball.rect.colliderect(rectangle_gauche_rect) and barrerect_gauche.top < Ball.rect.top:
            barrerect_gauche.y += 3

        if Ball.rect.colliderect(rectangle_gauche_rect) and barrerect_gauche.bottom > Ball.rect.bottom:
            barrerect_gauche.y -= 3

        if barrerect_gauche.bottom > hauteur:
            barrerect_gauche.y = hauteur - 101

        # update de la fenetre
        pygame.display.update()
        # Detection des evenements
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0

            # Detection des clics sur les boutons
            if playrect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                continuer = False
                In_game(Argent)
            if play_coop_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                continuer = False
                Coop(Argent)

            if Shop_Bt_Rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                continuer = False
                Shop(Argent)

            if help_Bt_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                continuer = False
                help_menu(Argent)

#Creation menu help
def help_menu(Argent):
    continuer = True

    # Creation des différents textes et images
    up = pygame.image.load("Fleche_haut.png").convert_alpha()
    up = pygame.transform.scale(up, (64, 64))

    down = pygame.image.load("Fleche_bas.png").convert_alpha()
    down = pygame.transform.scale(down, (64, 64))

    z = pygame.image.load("Z.png").convert_alpha()
    z = pygame.transform.scale(z, (64, 64))

    s = pygame.image.load("S.png").convert_alpha()
    s = pygame.transform.scale(s, (64, 64))

    text = font.render("Player 1:", True, (200, 200, 200))
    text_2 = font.render("Player 2:", True, (200, 200, 200))

    text_control_1 = sub_font.render("Haut : ", True, (250, 250, 250))
    text_control_2 = sub_font.render("Bas : ", True, (250, 250, 250))

    text_rules = sub_font.render("Score Limit : 5 ", True, (250, 250, 250))
    text_rules_2 = sub_font.render("In coop, 10s = 100$ | powerup = 50$ ", True, (250, 250, 250))

    while continuer:
        # Mise en place background
        fenetre.blit(background, (0, 0))
        fenetre.blit(back_arrow, back_arrow_rect)

        # Mise en place des textes, et images des commandes et des regles
        fenetre.blit(up, (880, 170))
        fenetre.blit(down, (880, 270))
        fenetre.blit(z, (280, 170))
        fenetre.blit(s, (280, 270))

        fenetre.blit(text, (200, 100))
        fenetre.blit(text_2, (800, 100))

        fenetre.blit(text_control_1, (200, 200))
        fenetre.blit(text_control_2, (200, 300))

        fenetre.blit(text_control_1, (800, 200))
        fenetre.blit(text_control_2, (800, 300))

        fenetre.blit(text_rules, (570, 500))
        fenetre.blit(text_rules_2, (450, 530))

        pygame.display.update()

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0

            # Mise en place touche return
            if back_arrow_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                continuer = False
                Menu(Argent)

# Creation du Menu Shop
def Shop(Argent):
    global locking, locking2, locking3, locking8, locking9, locking10, locking11
    global locking15, locking16
    En_Marche = True
    continuer = True
    continuer_2 = False
    continuer_3 = False

    # Mise en place des fleches droite et gauche
    Right_arr = pygame.image.load("Right_arrow.png").convert_alpha()
    Right_arr_rect = Right_arr.get_rect()
    Right_arr_rect.x, Right_arr_rect.y = 1200, 350

    Left_arr = pygame.image.load("Left_arrow.png").convert_alpha()
    Left_arr_rect = Left_arr.get_rect()
    Left_arr_rect.x, Left_arr_rect.y = 30, 350

    while En_Marche:
        # Creation des différents menu dans le shops
        while continuer:

            # affichage de l'argent
            text_Money = font.render("$" + str(Argent), True, (200, 200, 200))
            fenetre.blit(background, (0, 0))
            fenetre.blit(back_arrow, back_arrow_rect)

            fenetre.blit(text_Money, (20, 20))

            # Creation des Items
            Item_Shop = ItemShop("default_unlock", False, None, 100, 100, "background")
            fenetre.blit(Item_Shop.image, Item_Shop.image_rect)

            Item_Shop_2 = ItemShop("foot_lock", locking, 500, 380, 100, "background")
            fenetre.blit(Item_Shop_2.image, Item_Shop_2.image_rect)

            Item_Shop_3 = ItemShop("Neon_lock", locking2, 900, 660, 100, "background")
            fenetre.blit(Item_Shop_3.image, Item_Shop_3.image_rect)

            Item_Shop_4 = ItemShop("blur_lock", locking3, 2500, 940, 100, "background")
            fenetre.blit(Item_Shop_4.image, Item_Shop_4.image_rect)

            fenetre.blit(Right_arr, Right_arr_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == QUIT:
                    continuer = False
                    En_Marche = False
                if event.type == MOUSEBUTTONDOWN and back_arrow_rect.collidepoint(x, y):
                    En_Marche = False
                    continuer = False
                    Menu(Argent)
                # Bouton Fleche droite
                if event.type == MOUSEBUTTONDOWN and Right_arr_rect.collidepoint(x, y):
                    continuer = False
                    continuer_2 = True
                # Creation des bouton d'achat et de selection des Items
                if event.type == MOUSEBUTTONDOWN and Item_Shop.rect_select.collidepoint(x, y) and not Item_Shop.lock:
                    Item_Shop.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_2.rect.collidepoint(x, y) and Item_Shop_2.lock:
                    if Argent >= Item_Shop_2.cost:
                        Argent -= Item_Shop_2.cost
                        Item_Shop_2.buy()
                        locking = False

                if not Item_Shop_2.lock and event.type == MOUSEBUTTONDOWN and Item_Shop_2.rect_select.collidepoint(x,
                                                                                                                   y):
                    Item_Shop_2.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_3.rect.collidepoint(x, y) and Item_Shop_3.lock:
                    if Argent >= Item_Shop_3.cost:
                        Argent -= Item_Shop_3.cost
                        Item_Shop_3.buy()
                        locking2 = False

                if not Item_Shop_3.lock and event.type == MOUSEBUTTONDOWN and Item_Shop_3.rect_select.collidepoint(x,
                                                                                                                   y):
                    Item_Shop_3.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_4.rect.collidepoint(x, y) and Item_Shop_4.lock:
                    if Argent >= Item_Shop_4.cost:
                        Argent -= Item_Shop_4.cost
                        Item_Shop_4.buy()
                        locking3 = False

                if Item_Shop_4.lock or event.type != MOUSEBUTTONDOWN or not Item_Shop_4.rect_select.collidepoint(x, y):
                    continue
                Item_Shop_4.Selected()
        # Creation du deuxieme menu
        while continuer_2:
            # Affichage de l'argent
            text_Money = font.render("$" + str(Argent), True, (200, 200, 200))
            fenetre.blit(background, (0, 0))
            fenetre.blit(back_arrow, back_arrow_rect)
            fenetre.blit(text_Money, (20, 20))

            fenetre.blit(Right_arr, Right_arr_rect)
            fenetre.blit(Left_arr, Left_arr_rect)

            # Creation des Items du Shop
            Item_Shop_9 = ItemShop("barre_unlock", locking8, None, 100, 100, "bar")
            fenetre.blit(Item_Shop_9.image, Item_Shop_9.image_rect)

            Item_Shop_10 = ItemShop("Neon_bar_lock", locking9, 500, 380, 100, "bar")
            fenetre.blit(Item_Shop_10.image, Item_Shop_10.image_rect)

            Item_Shop_11 = ItemShop("Candy_bar_lock", locking10, 1500, 660, 100, "bar")
            fenetre.blit(Item_Shop_11.image, Item_Shop_11.image_rect)

            Item_Shop_12 = ItemShop("flamme_lock", locking11, 2800, 940, 100, "bar")
            fenetre.blit(Item_Shop_12.image, Item_Shop_12.image_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == QUIT:
                    En_Marche = False
                    continuer_2 = False
                if event.type == MOUSEBUTTONDOWN and back_arrow_rect.collidepoint(x, y):
                    En_Marche = False
                    continuer_2 = False
                    Menu(Argent)

                # Creation des boutons fleches droites fleches gauche
                if event.type == MOUSEBUTTONDOWN and Right_arr_rect.collidepoint(x, y):
                    continuer_2 = False
                    continuer_3 = True

                if event.type == MOUSEBUTTONDOWN and Left_arr_rect.collidepoint(x, y):
                    continuer_2 = False
                    continuer = True
                # Creation des bouton Select et Buy
                if event.type == MOUSEBUTTONDOWN and Item_Shop_9.rect_select.collidepoint(x,
                                                                                          y) and not Item_Shop_9.lock:
                    Item_Shop_9.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_10.rect.collidepoint(x, y) and Item_Shop_10.lock:
                    if Argent >= Item_Shop_10.cost:
                        Argent -= Item_Shop_10.cost
                        Item_Shop_10.buy()
                        locking9 = False

                if event.type == MOUSEBUTTONDOWN and Item_Shop_10.rect_select.collidepoint(x,
                                                                                           y) and not Item_Shop_10.lock:
                    Item_Shop_10.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_11.rect.collidepoint(x, y) and Item_Shop_11.lock:
                    if Argent >= Item_Shop_11.cost:
                        Argent -= Item_Shop_11.cost
                        Item_Shop_11.buy()
                        locking10 = False

                if event.type == MOUSEBUTTONDOWN and Item_Shop_11.rect_select.collidepoint(x,
                                                                                           y) and not Item_Shop_11.lock:
                    Item_Shop_11.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_12.rect.collidepoint(x, y) and Item_Shop_12.lock:
                    if Argent >= Item_Shop_12.cost:
                        Argent -= Item_Shop_12.cost
                        Item_Shop_12.buy()
                        locking11 = False

                if event.type == MOUSEBUTTONDOWN and Item_Shop_12.rect_select.collidepoint(x,
                                                                                           y) and not Item_Shop_12.lock:
                    Item_Shop_12.Selected()

        while continuer_3:
            text_Money = font.render("$" + str(Argent), True, (200, 200, 200))
            fenetre.blit(background, (0, 0))
            fenetre.blit(back_arrow, back_arrow_rect)
            fenetre.blit(text_Money, (20, 20))

            fenetre.blit(Left_arr, Left_arr_rect)

            Item_Shop_16 = ItemShop("ball_unlock", locking15, None, 100, 100, "ball")
            fenetre.blit(Item_Shop_16.image, Item_Shop_16.image_rect)

            Item_Shop_17 = ItemShop("football_lock", locking16, 200, 380, 100, "ball")
            fenetre.blit(Item_Shop_17.image, Item_Shop_17.image_rect)

            pygame.display.update()
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == QUIT:
                    En_Marche = False
                    continuer_3 = False
                if event.type == MOUSEBUTTONDOWN and back_arrow_rect.collidepoint(x, y):
                    En_Marche = False
                    continuer_3 = False
                    Menu(Argent)
                if event.type == MOUSEBUTTONDOWN and Left_arr_rect.collidepoint(x, y):
                    continuer_3 = False
                    continuer_2 = True

                if event.type == MOUSEBUTTONDOWN and Item_Shop_16.rect_select.collidepoint(x,
                                                                                           y) and not Item_Shop_16.lock:
                    Item_Shop_16.Selected()

                if event.type == MOUSEBUTTONDOWN and Item_Shop_17.rect.collidepoint(x, y) and Item_Shop_17.lock:
                    if Argent >= Item_Shop_17.cost:
                        Argent -= Item_Shop_17.cost
                        Item_Shop_17.buy()
                        locking16 = False

                if event.type == MOUSEBUTTONDOWN and Item_Shop_17.rect_select.collidepoint(x,
                                                                                           y) and not Item_Shop_17.lock:
                    Item_Shop_17.Selected()


# Creation du Jeux en versus
def In_game(Money):
    global barrerect_gauche, barrerect_droite, barre_gauche, barre_droite
    # Mise en place des variables de la vitesse et de la taille des Barres et du lvl2
    vitesse = [0, 0]
    taille_barre = 100
    Lvl2 = False

    pygame.key.set_repeat(10, 30)  ##pour pouvoir laisser les fleches enfoncées

    # Variable de Scores
    score_g = 0
    score_d = 0
    # Variable de Temps
    i = 1
    minute = 0

    # Mise au centre des barres
    barrerect_gauche.x, barrerect_gauche.y = 10, 300
    barrerect_droite.x, barrerect_droite.y = 1255, 300

    continuer = True
    # Utilisation et attribution des Classes
    action = Power_Up()
    Ingame = In_Game()
    action.pos0()

    Ball = Balle(ball_name)

    while continuer:

        fenetre.blit(background, (0, 0))

        # Création de la boucle de déplacement de la balle
        pygame.time.Clock().tick(130)  # pour ralentir la boucle de jeu
        Ball.rect = Ball.rect.move(vitesse)
        # ajout du temps
        i += 1

        # Transformation des secondes en minutes
        if int(i / 100) == 60:
            minute += 1
            i = i - 6000

        # Stop le compteur de temps si la balle est inactive
        if vitesse == [0, 0]:
            i -= 1

        # Spawn des PowerUp sur la zone
        if i % 1500 == 0:
            Ingame.spawn_powerup()

        # Suppression du powerup Increased à 59s
        if i == 5900:
            del liste_powerup[1]
            Lvl2 = True

        # Passage au lvl2
        if Lvl2 and i % 1500 == 0:
            Ingame.spawn_powerup()

        # Detection des collisions en fonction du PowerUp (ici Vitesse)
        if pygame.sprite.spritecollide(Ball, Ingame.SpeedGrp, True):
            if vitesse[0] < 0:
                vitesse[0] -= 1
            else:
                vitesse[0] += 1
            if vitesse[1] < 0:
                vitesse[1] -= 1
            else:
                vitesse[1] += 1
        # Detection des collisions en fonction du PowerUp (ici Augmentation)
        if pygame.sprite.spritecollide(Ball, Ingame.Increased, True):
            taille_barre = taille_barre + 20
            if taille_barre >= 200:
                taille_barre -= 20
            barre_droite = pygame.transform.scale(barre_droite, (15, taille_barre))
            barre_gauche = pygame.transform.scale(barre_gauche, (15, taille_barre))

            y_droite_pos = barrerect_droite.y

            y_gauche_pos = barrerect_gauche.y

            barrerect_droite = barre_droite.get_rect()
            barrerect_gauche = barre_gauche.get_rect()

            barrerect_droite.x, barrerect_droite.y = 1255, y_droite_pos
            barrerect_gauche.x, barrerect_gauche.y = 10, y_gauche_pos
        # Detection des collisions en fonction du PowerUp (ici Diminution)
        if pygame.sprite.spritecollide(Ball, Ingame.Decreased, True):
            taille_barre = taille_barre - 20
            if taille_barre <= 40:
                taille_barre += 20
            barre_droite = pygame.transform.scale(barre_droite, (15, taille_barre))
            barre_gauche = pygame.transform.scale(barre_gauche, (15, taille_barre))

            y_droite_pos = barrerect_droite.y
            y_gauche_pos = barrerect_gauche.y

            barrerect_droite = barre_droite.get_rect()
            barrerect_gauche = barre_gauche.get_rect()

            barrerect_droite.x, barrerect_droite.y = 1255, y_droite_pos
            barrerect_gauche.x, barrerect_gauche.y = 10, y_gauche_pos

        # Detection des collisions entre les murs et la balle et remise haut centre
        if Ball.rect.left < 0:
            vitesse = [0, 0]
            score_d += 1
            Ball.rect.x, Ball.rect.y = largeur / 2, hauteur / 2

        if Ball.rect.right > largeur:
            vitesse = [0, 0]
            score_g += 1
            Ball.rect.x, Ball.rect.y = largeur / 2, hauteur / 2

        if Ball.rect.top < 0 or Ball.rect.bottom > hauteur:
            vitesse[1] = -vitesse[1]

        # Detection des collisions entre la balle et les barres
        if Ball.rect.colliderect(
                barrerect_gauche):
            vitesse[0] = -vitesse[0]
            ping.play()

        if Ball.rect.colliderect(
                barrerect_droite):
            vitesse[0] = -vitesse[0]
            ping.play()

        # Mise en place du limite au deplacement des barres verticales
        if barrerect_gauche.top < 0:
            barrerect_gauche.y += 10

        if barrerect_gauche.bottom > hauteur:
            barrerect_gauche.y -= 10

        if barrerect_droite.top < 0:
            barrerect_droite.y += 10

        if barrerect_droite.bottom > hauteur:
            barrerect_droite.y -= 10

        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            # Gestion de la fermeture :
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0  # On arrête la boucle
            # mouvement de la barre de gauche:
            if event.type == KEYDOWN:
                if event.key == K_s:  # Si "S"
                    barrerect_gauche = barrerect_gauche.move(0, 15)  # On descend la barre de gauche de 15 pixels

                if event.key == K_z:  # Si "Z"
                    barrerect_gauche = barrerect_gauche.move(0, -15)  # On monte la barre de gauche de 15 pixels

                if event.key == K_DOWN:  # Si "flèche bas"
                    barrerect_droite = barrerect_droite.move(0, 15)  # On descend la barre de gauche de 15 pixels

                if event.key == K_UP:  # Si "flèche haut"
                    barrerect_droite = barrerect_droite.move(0, -15)  # On monte la barre de gauche de 15 pixels

                # Mise en place du demarrage de la partie si appuye sur Entrée
                if event.key == K_RETURN and vitesse == [0, 0]:
                    vitesse = [3, 3]

        # Affichage des éléments de la fenetre

        fenetre.blit(Ball.image, Ball.rect)  # Dessin de la balle
        fenetre.blit(barre_gauche, barrerect_gauche)  # Dessin de la barre gauche
        fenetre.blit(barre_droite, barrerect_droite)  # Dessin de la barre droite

        # affichage du score
        score_gauche = font.render(str(score_g), True, (200, 200, 200))
        score_droite = font.render(str(score_d), True, (200, 200, 200))

        # Affichage du compteur de temps
        Complet_Time = str(minute) + " : " + str(int(i / 100))

        time = font.render(Complet_Time, False, (200, 200, 200))
        time_rect = time.get_rect()
        time_rect.centerx, time_rect.centery = largeur / 2, 100

        fenetre.blit(score_gauche, (largeur / 2 - 100, 10))
        fenetre.blit(score_droite, (largeur / 2 + 70, 10))
        fenetre.blit(time, time_rect)

        # Affichage des PowerUp en Fonction de le grp
        Ingame.SpeedGrp.draw(fenetre)
        Ingame.Increased.draw(fenetre)
        Ingame.Decreased.draw(fenetre)

        # Mise en place d'un score max de 5 Puis affichage du tableau des Scores
        if score_d == 5 or score_g == 5:
            continuer = False
            Score(Complet_Time, 0, score_g, score_d, Money)

        # Rafraîchissement de l'écran
        pygame.display.flip()


# Creation du Jeux en Coop
def Coop(Money):
    print(Money)
    global barrerect_gauche, barrerect_droite, barre_gauche, barre_droite
    # Mise en place des Variable Money, Vitesse et Taille de la barre et Lvl2
    Money_IG = 0
    vitesse = [0, 0]
    taille_barre = 100

    Lvl2 = False

    pygame.key.set_repeat(10, 30)  ##pour pouvoir laisser les fleches enfoncées  # placer la balle au centre au départ

    # Mise en place du score Globale
    score_d = 0
    # Mise en place du compteur de temps
    i = 1
    minute = 0

    # Mise au centre des barres
    barrerect_gauche.x, barrerect_gauche.y = 10, 300
    barrerect_droite.x, barrerect_droite.y = 1255, 300

    continuer = True
    # Attribution des classes
    action = Power_Up()
    Ingame = In_Game()
    action.pos0()

    Ball = Balle(ball_name)

    while continuer:

        fenetre.blit(background, (0, 0))

        # Création de la boucle de déplacement de la balle
        pygame.time.Clock().tick(130)  # pour ralentir la boucle de jeu
        Ball.rect = Ball.rect.move(vitesse)
        # Ajout du temps
        i += 1

        # Transformation des secondes en Minutes
        if int(i / 100) == 60:
            minute += 1
            i = i - 6000

        # Desactivation du comptage du temps si la balle est inactive
        if vitesse == [0, 0]:
            i -= 1

        # Apparition des PowerUp toutes les 15s
        if i % 1500 == 0:
            Ingame.spawn_powerup()

        if i == 6000:
            del liste_powerup[1]
            Lvl2 = True

        if Lvl2 and i % 1500 == 0:
            Ingame.spawn_powerup()

        # Ajout d'argent toute les 10s
        if i % 1000 == 0:
            Money_IG += 100

        # Detection des collisions en fonction du PowerUp (ici Vitesse)
        if pygame.sprite.spritecollide(Ball, Ingame.SpeedGrp, True):
            if vitesse[0] < 0:
                vitesse[0] -= 1
            else:
                vitesse[0] += 1
            if vitesse[1] < 0:
                vitesse[1] -= 1
            else:
                vitesse[1] += 1
            Money_IG += 50
        # Detection des collisions en fonction du PowerUp (ici Augmentation)
        if pygame.sprite.spritecollide(Ball, Ingame.Increased, True):
            taille_barre = taille_barre + 20
            if taille_barre >= 200:
                taille_barre -= 20
            barre_droite = pygame.transform.scale(barre_droite, (15, taille_barre))
            barre_gauche = pygame.transform.scale(barre_gauche, (15, taille_barre))

            y_droite_pos = barrerect_droite.y

            y_gauche_pos = barrerect_gauche.y

            barrerect_droite = barre_droite.get_rect()
            barrerect_gauche = barre_gauche.get_rect()

            barrerect_droite.x, barrerect_droite.y = 1255, y_droite_pos
            barrerect_gauche.x, barrerect_gauche.y = 10, y_gauche_pos
            Money_IG += 50
        # Detection des collisions en fonction du PowerUp (ici Diminution)
        if pygame.sprite.spritecollide(Ball, Ingame.Decreased, True):
            taille_barre = taille_barre - 20
            if taille_barre <= 40:
                taille_barre += 20
            barre_droite = pygame.transform.scale(barre_droite, (15, taille_barre))
            barre_gauche = pygame.transform.scale(barre_gauche, (15, taille_barre))

            y_droite_pos = barrerect_droite.y
            y_gauche_pos = barrerect_gauche.y

            barrerect_droite = barre_droite.get_rect()
            barrerect_gauche = barre_gauche.get_rect()

            barrerect_droite.x, barrerect_droite.y = 1255, y_droite_pos
            barrerect_gauche.x, barrerect_gauche.y = 10, y_gauche_pos
            Money_IG += 50

        # Detection Collision de la balle sur les Murs + remise au centre
        if Ball.rect.left < 0:
            vitesse = [0, 0]
            score_d += 1
            Ball.rect.x, Ball.rect.y = largeur / 2, hauteur / 2

        if Ball.rect.right > largeur:
            vitesse = [0, 0]
            score_d += 1
            Ball.rect.x, Ball.rect.y = largeur / 2, hauteur / 2

        if Ball.rect.top < 0 or Ball.rect.bottom > hauteur:
            vitesse[1] = -vitesse[1]

        # Detectop, de la colision entre la balle et les barres
        if Ball.rect.colliderect(
                barrerect_gauche):
            vitesse[0] = -vitesse[0]
            ping.play()

        if Ball.rect.colliderect(
                barrerect_droite):
            vitesse[0] = -vitesse[0]
            ping.play()

        # Limitation du deplacement Verticale des barres
        if barrerect_gauche.top < 0:
            barrerect_gauche.y += 10

        if barrerect_gauche.bottom > hauteur:
            barrerect_gauche.y -= 10

        if barrerect_droite.top < 0:
            barrerect_droite.y += 10

        if barrerect_droite.bottom > hauteur:
            barrerect_droite.y -= 10

        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            # Gestion de la fermeture :
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0  # On arrête la boucle
            # mouvement de la barre de gauche:
            if event.type == KEYDOWN:
                if event.key == K_s:  # Si "S"
                    barrerect_gauche = barrerect_gauche.move(0, 15)  # On descend la barre de gauche de 15 pixels

                if event.key == K_z:  # Si "Z"
                    barrerect_gauche = barrerect_gauche.move(0, -15)  # On monte la barre de gauche de 15 pixels

                if event.key == K_DOWN:  # Si "flèche bas"
                    barrerect_droite = barrerect_droite.move(0, 15)  # On descend la barre de gauche de 15 pixels

                if event.key == K_UP:  # Si "flèche haut"
                    barrerect_droite = barrerect_droite.move(0, -15)  # On monte la barre de gauche de 15 pixels

                # Mise en place du début de la partie si appuye sur Entrée
                if event.key == K_RETURN and vitesse == [0, 0]:
                    vitesse = [3, 3]

        # Affichage des différents Elements de la fenetre
        fenetre.blit(Ball.image, Ball.rect)  # Dessin de la balle
        fenetre.blit(barre_gauche, barrerect_gauche)  # Dessin de la barre gauche
        fenetre.blit(barre_droite, barrerect_droite)  # Dessin de la barre droite
        # affichage du score
        score_droite = font.render(str(score_d), True, (200, 200, 200))
        # Affichage du compteur de temps
        Complet_Time = str(minute) + " : " + str(int(i / 100))

        time = font.render(Complet_Time, False, (200, 200, 200))
        time_rect = time.get_rect()
        time_rect.centerx, time_rect.centery = largeur / 2, 100

        # Affichage di compteur d'argent
        Money_win = font.render(str(Money_IG) + "€", False, (200, 200, 200))

        fenetre.blit(score_droite, (largeur / 2 - 14, 10))
        fenetre.blit(time, time_rect)
        fenetre.blit(Money_win, (800, 10))

        # Affichage des différentes classes en fonction de leur grp
        Ingame.SpeedGrp.draw(fenetre)
        Ingame.Increased.draw(fenetre)
        Ingame.Decreased.draw(fenetre)

        # Rafraîchissement de l'écran
        pygame.display.flip()

        # Fin de la partie si le score = 5
        if score_d == 5:
            print(Money)
            Money += Money_IG
            continuer = False
            Score(Complet_Time, Money_IG, None, None, Money)


# Creation du Tableau des Scores
def Score(Complet_Time, Money_IG, Score_g, Score_d, Money):
    # Mise en place des texte qui seront affichée
    text_Score = list("Temps du Groupe : " + Complet_Time + "s")
    text_Money_Win = list("Argent Gagnée : " + str(Money_IG) + "€")

    text_Score_D = list("Score Joueur Droite : " + str(Score_d))
    text_Score_G = list("Score Joueur Gauche : " + str(Score_g))

    # Detection si la game d'avant etais le mode Verus Ou Coop
    # Affichage du gagnant
    if Score_g or Score_d is not None:
        if Score_d > Score_g:
            Winner_Name_Text = "Joueur Droite !"
        else:
            Winner_Name_Text = "Joueur Gauche !"
        Winner_Name = list("The Winner Is : " + Winner_Name_Text)
    Score_List = []

    score = pygame.image.load("Score.png").convert_alpha()
    # Creation de la variable qui va faire s'afficher les lettres une par une
    i = 0

    # Mise en place de la police d'écriture
    font = pygame.font.Font(None, 40)

    # Mise en place de variable qui permette l'afficage des différents textes
    continuer = True
    Time_Score = True
    Money_Score = True
    Score_Droite = True
    Score_Gauche = True
    Winner = True
    while continuer:
        # Affichage des différentes Elements de la fenetre
        fenetre.blit(background, (0, 0))
        fenetre.blit(score, (0, 0))
        fenetre.blit(back_arrow, back_arrow_rect)

        # Detection des collisions entre la souris et les boutons
        for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
            x, y = pygame.mouse.get_pos()
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0

            if back_arrow_rect.collidepoint(x, y) and event.type == MOUSEBUTTONDOWN:
                continuer = 0
                if Money is None:
                    Money = 0
                Menu(Money)
        # Mise en place de l'animation des textes
        while Time_Score:
            # Mise en place de la vitesse de la boucle
            pygame.time.Clock().tick(20)
            # Ajout du texte a une liste lettre par lettre du style: c, co, cou, couc, couco, coucou
            Score_List.append(text_Score[i])
            text_str = ''.join(Score_List)

            text = font.render(str(text_str), True, (200, 200, 200))
            fenetre.blit(text, (350, 200))

            i += 1
            if i >= len(text_Score):
                Time_Score = False
            for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                if event.type == QUIT:  # Si un de ces événements est de type QUIT
                    continuer = 0
                    Time_Score = False
                    i = 0
            pygame.display.flip()

        # mise a zero des parametres
        i = 0
        Score_List = []

        # Mise en place de l'animation des textes
        if Money_IG != 0:
            while Money_Score:
                pygame.time.Clock().tick(20)
                Score_List.append(text_Money_Win[i])
                text_str = ''.join(Score_List)

                text_Money = font.render(str(text_str), True, (200, 200, 200))
                fenetre.blit(text_Money, (350, 250))

                i += 1
                if i >= len(text_Money_Win):
                    Money_Score = False
                for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                    if event.type == QUIT:  # Si un de ces événements est de type QUIT
                        continuer = 0
                        Money_Score = False
                pygame.display.flip()
            fenetre.blit(text_Money, (350, 250))

        # mise a zero des parametres
        i = 0
        Score_List = []

        # Mise en place de l'animation des textes
        if Score_d is not None:
            while Score_Droite:
                pygame.time.Clock().tick(20)
                Score_List.append(text_Score_D[i])
                text_str = ''.join(Score_List)

                text_score_d = font.render(str(text_str), True, (200, 200, 200))
                fenetre.blit(text_score_d, (350, 250))

                i += 1
                if i >= len(text_Score_D):
                    Score_Droite = False
                for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                    if event.type == QUIT:  # Si un de ces événements est de type QUIT
                        continuer = 0
                        Score_Droite = False
                        i = 0
                pygame.display.flip()
            fenetre.blit(text_score_d, (350, 250))

        # mise a zero des parametres
        i = 0
        Score_List = []

        # Mise en place de l'animation des textes
        if Score_g is not None:
            while Score_Gauche:
                pygame.time.Clock().tick(20)
                Score_List.append(text_Score_G[i])
                text_str = ''.join(Score_List)

                text_score_g = font.render(str(text_str), True, (200, 200, 200))
                fenetre.blit(text_score_g, (350, 300))

                i += 1
                if i >= len(text_Score_G):
                    Score_Gauche = False
                for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                    if event.type == QUIT:  # Si un de ces événements est de type QUIT
                        continuer = 0
                        Score_Gauche = False
                        i = 0
                pygame.display.flip()
            fenetre.blit(text_score_g, (350, 300))

        # mise a zero des parametres
        i = 0
        Score_List = []

        # Mise en place de l'animation des textes
        if Score_g or Score_d is not None:
            while Winner:
                pygame.time.Clock().tick(20)
                Score_List.append(Winner_Name[i])
                text_str = ''.join(Score_List)

                Winner_text = font.render(str(text_str), True, (0, 0, 0))
                fenetre.blit(Winner_text, (350, 600))

                i += 1
                if i >= len(Winner_Name):
                    Winner = False
                for event in pygame.event.get():  # On parcourt la liste de tous les événements reçus
                    if event.type == QUIT:  # Si un de ces événements est de type QUIT
                        continuer = 0
                        Winner = False
                        i = 0
                pygame.display.flip()
            fenetre.blit(Winner_text, (350, 600))

        fenetre.blit(text, (350, 200))
        #Update de la fenetre
        pygame.display.flip()


# Affichage de la première fenetre
Menu(Money)

pygame.quit()

# Petit recap:
# Ajout du compteur de temps
# Ajout des powerUp
# Ajout d'un systeme Versus et d'un Systeme Coop
# Ajout de l'animation du menu
# Ajout d'un Menu
# Ajout du tableau des Scores + animation
# Ajout du système monaitaire
# Ajout d'un système d'achat de background, barre et balle
# Ajout d'effet Sonore
# Ajout d'un menu d'aide
