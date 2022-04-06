import pygame
from pygame.locals import *
import InGame
import SelectPerso
from pygame_widgets import *

# Initialisation Pygame
pygame.init()

pygame.display.set_caption('Monopoly')

screen = pygame.display.set_mode((1280, 720))

# Recupération des infos screens
ScreenX = screen.get_width()
ScreenY = screen.get_height()

# Lecture du fichier setting.txt
setting_file = open("Setting.txt", "r")
list_of_lines = setting_file.readlines()

# Creation des Slider Pour le Son
slider = Slider(screen, 300, 200, 200, 40, initial=float(list_of_lines[4].split()[1]) * 100, min=0, max=99, step=1,
                colour=(122, 122, 122),
                handleColour=(48, 48, 48), handleRadius=10)
output = TextBox(screen, 525, 195, 50, 50, fontSize=25)

sliderBackSound = Slider(screen, 800, 200, 200, 40, initial=float(list_of_lines[5].split()[1]) * 100, min=0, max=100,
                         step=1, colour=(122, 122, 122),
                         handleColour=(48, 48, 48), handleRadius=10)
outputBackSound = TextBox(screen, 1025, 195, 50, 50, fontSize=25)

# Mise en place des bruitages
clic = pygame.mixer.Sound('song\Gui\clic.mp3')
clic.set_volume(float(list_of_lines[4].split()[1]))

# Mise en place des Songs
BackSound = pygame.mixer.Sound('song\Gui\BackGround_Sound.mp3')
BackSound.set_volume(float(list_of_lines[5].split()[1]))

# Fermeture de l'enregistrement du fichier
setting_file.close()


# Fonction qui gere le volume du son
def Sound_Vol(sound_volume):
    Sound_volume_Clic = sound_volume / 100
    clic.set_volume(Sound_volume_Clic)
    setting_file = open("Setting.txt", "r")
    list_of_lines = setting_file.readlines()
    list_of_lines[4] = f"Clic: {str(Sound_volume_Clic)}\n"

    setting_file = open("Setting.txt", "w")
    setting_file.writelines(list_of_lines)
    setting_file.close()


# Fonction qui gère la music de fond
def Sound_Vol_BackSound(sound_volume_BackSound):
    Sound_volume_background = sound_volume_BackSound / 100
    BackSound.set_volume(Sound_volume_background)
    setting_file = open("Setting.txt", "r")
    list_of_lines = setting_file.readlines()
    list_of_lines[5] = f"Background_Sound: {str(Sound_volume_background)}\n"

    setting_file = open("Setting.txt", "w")
    setting_file.writelines(list_of_lines)
    setting_file.close()


# Chargement du Background
background = pygame.image.load('img/img/Element/Ingame/Background/MenuBackground.jpg').convert()
background = pygame.transform.scale(background, (ScreenX, ScreenY))

# ============================================In_Game====================================================================
# Chargement du plateau
plateau_img = pygame.image.load('img/img/Plateau_2.png').convert()
plateau_img = pygame.transform.scale(plateau_img, (720, 720))
# =======================================================================================================================
# Chargement des boutons
PlayBt = pygame.image.load("img/img/Element/Menu/Play.png").convert_alpha()
PlayBt = pygame.transform.scale(PlayBt, (256, 128))
PlayBt.set_colorkey((255, 0, 243))

TestBt = pygame.image.load("img/img/Element/Menu/Sound_On.png").convert_alpha()
TestBt = pygame.transform.scale(TestBt, (48, 48))
TestBt.set_colorkey((255, 0, 243))

SettingBt = pygame.image.load("img/img/Element/Menu/Setting.png").convert()
SettingBt = pygame.transform.scale(SettingBt, (64, 64))
SettingBt.set_colorkey((255, 0, 243))

Logo = pygame.image.load("img/img/Element/Menu/Monopoly.png").convert()
Logo = pygame.transform.scale(Logo, (600, 400))
Logo.set_colorkey((195, 138, 60))

ArrowBt = pygame.image.load("img/img/Element/Menu/arrow.png").convert()
ArrowBt = pygame.transform.scale(ArrowBt, (64, 64))
ArrowBt.set_colorkey((255, 0, 243))

GraphicsBt = pygame.image.load("img/img/Element/Menu/Graphique.png").convert()
GraphicsBt = pygame.transform.scale(GraphicsBt, (128, 64))
GraphicsBt.set_colorkey((255, 0, 243))

MuteBt = pygame.image.load("img/img/Element/Menu/Sound_On.png").convert()
MuteBt = pygame.transform.scale(MuteBt, (128, 64))
MuteBt.set_colorkey((255, 0, 243))

SoundBt = pygame.image.load("img/img/Element/Menu/Sound_Setting.png").convert()
SoundBt = pygame.transform.scale(SoundBt, (128, 64))
SoundBt.set_colorkey((255, 0, 243))
# Chargement des boutons de la taille de l'image
size0 = pygame.image.load("img/img/Element/Menu/size0.png").convert()
size0 = pygame.transform.scale(size0, (128, 64))
size0.set_colorkey((255, 0, 243))

size1 = pygame.image.load("img/img/Element/Menu/size1.png").convert()
size1 = pygame.transform.scale(size1, (128, 64))
size1.set_colorkey((255, 0, 243))

size2 = pygame.image.load("img/img/Element/Menu/size2.png").convert()
size2 = pygame.transform.scale(size2, (128, 64))
size2.set_colorkey((255, 0, 243))

# ====================================================================================================================
# Chargement des boutons fleche de droites et gauche dans la selection perso
RightArrow = pygame.image.load("img/img/Element/Menu/Perso/RightArrow.png").convert()
RightArrow = pygame.transform.scale(RightArrow, (48, 96))
RightArrow.set_colorkey((255, 0, 243))

LeftArrow = pygame.image.load("img/img/Element/Menu/Perso/LeftArrow.png").convert()
LeftArrow = pygame.transform.scale(LeftArrow, (48, 96))
LeftArrow.set_colorkey((255, 0, 243))

Valid = pygame.image.load("img/img/Element/Menu/Perso/Validation.png").convert()
Valid = pygame.transform.scale(Valid, (64, 64))
Valid.set_colorkey((255, 0, 243))

ValidOn = pygame.image.load("img/img/Element/Menu/Perso/ValidationOn.png").convert()
ValidOn = pygame.transform.scale(ValidOn, (64, 64))
ValidOn.set_colorkey((255, 0, 243))
ValidOnRect = ValidOn.get_rect(center=(800, 450))
ValidOnRect2 = ValidOn.get_rect(center=(800, 450))
ValidOnRect3 = ValidOn.get_rect(center=(800, 450))

CadreDes = pygame.image.load("img/img/Element/Ingame/Background/CadreDes.png")
CadreDes = pygame.transform.scale(CadreDes, (185, 110))
CadreDes.set_colorkey((255, 0, 243))

# Creation du bouton Inventaire
Inventory_Bt = pygame.image.load("img/img/Element/Ingame/Lucky.png").convert_alpha()
Inventory_Bt = pygame.transform.scale(Inventory_Bt, (32, 32))
Inventory_Bt_rect = Inventory_Bt.get_rect()
Inventory_Bt_rect.x, Inventory_Bt_rect.y = 200, 200

Inventory = pygame.image.load("img/img/Element/Ingame/Background/Inventory.png").convert_alpha()
Inventory = pygame.transform.scale(Inventory, (1280, 720))
Inventory_rect = Inventory.get_rect()
Inventory_rect.x, Inventory_rect.y = 0, 0

PauseScreen = pygame.image.load("img/img/Element/Ingame/Background/PauseScreen.png").convert_alpha()
# Lancement de la music de fond
BackSound.play()


# Fonction de la boucle MENU
def Menu():
    ''' Fonction qui gere le menu du jeux
    Contient la boucle du jeux et dautres composants'''

    running = True
    while running:
        screen_x = screen.get_width()
        screen_y = screen.get_height()

        pygame.transform.scale(Logo, (int(screen_x / 3), int(screen_y / 6)))

        ButtonRect = PlayBt.get_rect()
        ButtonRect.x, ButtonRect.y = (screen_x / 5) * 2, (screen_y / 4) * 2.3

        SetRect = SettingBt.get_rect()
        SetRect.x, SetRect.y = (screen_x / 5) * 2.1, (screen_y / 4) * 3.2

        screen.blit(background, (0, 0))
        screen.blit(PlayBt, ((screen_x / 5) * 2, (screen_y / 4) * 2.3))
        screen.blit(SettingBt, ((screen_x / 5) * 2.1, (screen_y / 4) * 3.2))
        screen.blit(Logo, ((screen_x / 5) * 1.3, (screen_y / 5) * 0.1))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            x, y = pygame.mouse.get_pos()
            PlayCollide = ButtonRect.collidepoint(x, y)
            SettingCollide = SetRect.collidepoint(x, y)
            if PlayCollide and event.type == MOUSEBUTTONUP:
                clic.play()
                running = False
                PersoSelection()
            if SettingCollide and event.type == MOUSEBUTTONUP:
                clic.play()
                running = False
                SettingMenu()


# Fonction de la boucle Settings
def SettingMenu():
    running = True
    while running:
        screen_x = screen.get_width()
        screen_y = screen.get_height()

        GraphicsRect = GraphicsBt.get_rect()
        GraphicsRect.x = (screen_x / 5) * 2.3
        GraphicsRect.y = (screen_y / 5) * 1

        SoundRect = SoundBt.get_rect()
        SoundRect.x = (screen_x / 5) * 2.3
        SoundRect.y = (screen_y / 5) * 1.5

        ArrowRect = ArrowBt.get_rect()
        ArrowRect.x = (screen_x / 5) * 0.1
        ArrowRect.y = (screen_y / 5) * 4.4

        screen.blit(background, (0, 0))
        screen.blit(ArrowBt, ((screen_x / 5) * 0.1, (screen_y / 5) * 4.4))
        screen.blit(GraphicsBt, ((screen_x / 5) * 2.3, (screen_y / 5) * 1))
        screen.blit(SoundBt, ((screen_x / 5) * 2.3, (screen_y / 5) * 1.5))

        pygame.display.flip()
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            ArrowCollide = ArrowRect.collidepoint(x, y)
            if ArrowCollide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                running = False
                Menu()

            GraphicsCollide = GraphicsRect.collidepoint(x, y)
            if GraphicsCollide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                running = False
                Graphique()

            if SoundRect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                running = False
                Sound_Controle()


# Fonction de la boucle Graphiques
def Graphique():
    running = True
    while running:
        screen_x = screen.get_width()
        screen_y = screen.get_height()

        ArrowRect = ArrowBt.get_rect()
        ArrowRect.x = (screen_x / 5) * 0.1
        ArrowRect.y = (screen_y / 5) * 4.4

        size0Rect = size0.get_rect()
        size0Rect.x = (screen_x / 5) * 2.3
        size0Rect.y = (screen_y / 5) * 1

        size1Rect = size1.get_rect()
        size1Rect.x = (screen_x / 5) * 2.3
        size1Rect.y = (screen_y / 5) * 1.6

        size2Rect = size2.get_rect()
        size2Rect.x = (screen_x / 5) * 2.3
        size2Rect.y = (screen_y / 5) * 2.2

        screen.blit(background, (0, 0))

        screen.blit(ArrowBt, ((screen_x / 5) * 0.1, (screen_y / 5) * 4.4))
        screen.blit(size0, ((screen_x / 5) * 2.3, (screen_y / 5) * 1.0))
        screen.blit(size1, ((screen_x / 5) * 2.3, (screen_y / 5) * 1.6))
        screen.blit(size2, ((screen_x / 5) * 2.3, (screen_y / 5) * 2.2))

        pygame.display.flip()
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            ArrowCollide = ArrowRect.collidepoint(x, y)
            if ArrowCollide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                running = False
                SettingMenu()

            size0Collide = size0Rect.collidepoint(x, y)
            if size0Collide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                pygame.display.set_mode((1280, 720))
                pygame.transform.scale(background, (200, screen_y))

            size1Collide = size1Rect.collidepoint(x, y)
            if size1Collide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                pygame.display.set_mode((1080, 640))
                pygame.transform.scale(background, (200, screen_y))

            size2Collide = size2Rect.collidepoint(x, y)
            if size2Collide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                pygame.display.set_mode((1400, 900))
                pygame.transform.scale(background, (200, 200))
                pygame.display.flip()


# Fonction de la boucle Sound Controle
def Sound_Controle():
    running = True
    while running:
        screen_x = screen.get_width()
        screen_y = screen.get_height()

        TestRect = TestBt.get_rect()
        TestRect.x, TestRect.y = 220, 200

        screen.blit(background, (0, 0))
        screen.blit(ArrowBt, ((screen_x / 5) * 0.1, (screen_y / 5) * 4.4))
        screen.blit(TestBt, TestRect)

        ArrowRect = ArrowBt.get_rect()
        ArrowRect.x = (screen_x / 5) * 0.1
        ArrowRect.y = (screen_y / 5) * 4.4

        output.draw()
        slider.draw()

        outputBackSound.draw()
        sliderBackSound.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            ArrowCollide = ArrowRect.collidepoint(x, y)
            if ArrowCollide and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                running = False
                Menu()

            slider.listen(pygame.event.get())
            sound_volume = slider.getValue()
            Sound_Vol(sound_volume)

            sliderBackSound.listen(pygame.event.get())
            sound_volume_BackSound = sliderBackSound.getValue()
            Sound_Vol_BackSound(sound_volume_BackSound)
            if TestRect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                clic.play()

            output.setText(slider.getValue())
            outputBackSound.setText(sliderBackSound.getValue())


# Fonction de la boucle Selection perso
def PersoSelection():
    Game = ["None", "Mario", "Luigi", "Peach", "Toad", "Yoshi"]
    Gameloop, Gameloop2, Gameloop3, Gameloop4 = 0, 0, 0, 0
    running = True
    perso_player, perso_player2, perso_player3, perso_player4 = 'None', 'None', 'None', 'None'
    J1, J2, J3, J4 = 'None', 'None', 'None', 'None'
    Valide, Valide2, Valide3, Valide4 = True, True, True, True

    valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4 = -150, -150, -150, -150
    valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4 = 150, 450, 760, 1070

    player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
    arrow = SelectPerso.Arrow()
    Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4, valid_pos_x,
                                    valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

    screen.blit(background, (0, 0))

    while running:
        screen.blit(background, (0, 0))

        SetRect = PlayBt.get_rect()
        SetRect.x, SetRect.y = 520, 500

        screen.blit(player.image, player.img_rect)
        screen.blit(arrow.right_arrow, arrow.right_arrow_rect)
        screen.blit(arrow.left_arrow, arrow.left_arrow_rect)
        screen.blit(Validate.validation, Validate.validation_rect)
        screen.blit(Validate.validation_on, Validate.validation_on_rect)

        screen.blit(player.image2, player.img_rect2)
        screen.blit(arrow.right_arrow, arrow.right_arrow_rect2)
        screen.blit(arrow.left_arrow, arrow.left_arrow_rect2)
        screen.blit(Validate.validation, Validate.validation_rect2)
        screen.blit(Validate.validation_on, Validate.validation_on_rect2)

        screen.blit(player.image3, player.img_rect3)
        screen.blit(arrow.right_arrow, arrow.right_arrow_rect3)
        screen.blit(arrow.left_arrow, arrow.left_arrow_rect3)
        screen.blit(Validate.validation, Validate.validation_rect3)
        screen.blit(Validate.validation_on, Validate.validation_on_rect3)

        screen.blit(player.image4, player.img_rect4)
        screen.blit(arrow.right_arrow, arrow.right_arrow_rect4)
        screen.blit(arrow.left_arrow, arrow.left_arrow_rect4)
        screen.blit(Validate.validation, Validate.validation_rect4)
        screen.blit(Validate.validation_on, Validate.validation_on_rect4)

        screen.blit(PlayBt, (520, 500))

        pygame.display.flip()
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if arrow.right_arrow_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide:
                Gameloop += 1

                if Gameloop >= len(Game):
                    Gameloop = 0

                while Game[Gameloop] == '0':
                    Gameloop += 1

                if Gameloop >= len(Game):
                    Gameloop = 0

                perso_player = Game[Gameloop]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                pygame.display.flip()
                clic.play()
            if arrow.left_arrow_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide:
                Gameloop -= 1

                while Game[Gameloop] == "0":
                    Gameloop -= 1

                if Gameloop == -1:
                    Gameloop = len(Game) - 1

                perso_player = Game[Gameloop]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)

                pygame.display.flip()
                clic.play()

            if arrow.right_arrow_rect2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide2:
                Gameloop2 += 1

                if Gameloop2 >= len(Game):
                    Gameloop2 = 0

                while Game[Gameloop2] == "0":
                    Gameloop2 += 1

                if Gameloop2 >= len(Game):
                    Gameloop2 = 0

                perso_player2 = Game[Gameloop2]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                pygame.display.flip()
                clic.play()
            if arrow.left_arrow_rect2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide2:
                Gameloop2 -= 1

                while Game[Gameloop2] == "0":
                    Gameloop2 -= 1

                if Gameloop2 == -1:
                    Gameloop2 = len(Game) - 1

                perso_player2 = Game[Gameloop2]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)

                pygame.display.flip()
                clic.play()

            if arrow.right_arrow_rect3.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide3:
                Gameloop3 += 1

                if Gameloop3 >= len(Game):
                    Gameloop3 = 0

                while Game[Gameloop3] == "0":
                    Gameloop3 += 1

                if Gameloop3 >= len(Game):
                    Gameloop3 = 0

                perso_player3 = Game[Gameloop3]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                pygame.display.flip()
                clic.play()
            if arrow.left_arrow_rect3.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide3:
                Gameloop3 -= 1

                while Game[Gameloop3] == "0":
                    Gameloop3 -= 1

                if Gameloop3 == -1:
                    Gameloop3 = len(Game) - 1

                perso_player3 = Game[Gameloop3]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                pygame.display.flip()
                clic.play()

            if arrow.right_arrow_rect4.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide4:
                Gameloop4 += 1

                if Gameloop4 >= len(Game) - 1:
                    Gameloop4 = 0

                while Game[Gameloop4] == "0":
                    Gameloop4 += 1

                if Gameloop4 >= len(Game) - 1:
                    Gameloop4 = 0

                perso_player4 = Game[Gameloop4]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                pygame.display.flip()
                clic.play()
            if arrow.left_arrow_rect4.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide4:
                Gameloop4 -= 1

                while Game[Gameloop4] == "0":
                    Gameloop4 -= 1

                if Gameloop4 == -1:
                    Gameloop4 = len(Game) - 1

                perso_player4 = Game[Gameloop4]
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                pygame.display.flip()
                clic.play()
            # -----------------------------------------------------------------------------------------------------------------------

            if Validate.validation_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide:
                Valide = False

                valid_on_pos_x = 150
                valid_pos_x = -150
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                if Gameloop == Gameloop2:
                    if Gameloop == len(Game) - 1:
                        Gameloop2 = 0
                    Gameloop2 += 1
                    while Game[Gameloop2] == "0":
                        Gameloop2 += 1
                    perso_player2 = Game[Gameloop2]
                if Gameloop == Gameloop3:
                    if Gameloop == len(Game) - 1:
                        Gameloop3 = 0
                    Gameloop3 += 1
                    while Game[Gameloop3] == "0":
                        Gameloop3 += 1
                    perso_player3 = Game[Gameloop3]
                if Gameloop == Gameloop4:
                    if Gameloop == len(Game) - 1:
                        Gameloop4 = 0
                    Gameloop4 += 1
                    while Game[Gameloop4] == "0":
                        Gameloop4 += 1
                    perso_player4 = Game[Gameloop4]

                J1 = perso_player

                Game[Gameloop] = "0"

                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                clic.play()
            elif Validate.validation_on_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                Valide = True

                valid_on_pos_x = -150
                valid_pos_x = 150
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                Game[Gameloop] = perso_player

                J1 = "None"

                if Game[Gameloop] == Game[Gameloop2]:
                    Gameloop2 += 1
                if Game[Gameloop] == Game[Gameloop3]:
                    Gameloop3 += 1
                if Game[Gameloop] == Game[Gameloop4]:
                    Gameloop4 += 1
                clic.play()

            if Validate.validation_rect2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide2:
                Valide2 = False

                valid_on_pos_x_2 = 450
                valid_pos_x_2 = -150
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                Gameloop_player2 = Game[Gameloop2]

                if Gameloop_player2 == Game[Gameloop]:
                    if Gameloop2 == len(Game) - 1:
                        Gameloop = 0
                    Gameloop += 1
                    while Game[Gameloop] == "0":
                        Gameloop += 1
                    perso_player = Game[Gameloop]
                if Gameloop_player2 == Game[Gameloop3]:
                    if Gameloop2 == len(Game) - 1:
                        Gameloop3 = 0
                    Gameloop3 += 1
                    while Game[Gameloop3] == "0":
                        Gameloop3 += 1
                    perso_player3 = Game[Gameloop3]
                if Gameloop_player2 == Game[Gameloop4]:
                    if Gameloop2 == len(Game) - 1:
                        Gameloop4 = 0
                    Gameloop4 += 1
                    while Game[Gameloop4] == "0":
                        Gameloop4 += 1
                    perso_player4 = Game[Gameloop4]

                J2 = perso_player2

                Game[Gameloop2] = "0"
                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                clic.play()
            elif Validate.validation_on_rect2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                Valide2 = True

                valid_on_pos_x_2 = -150
                valid_pos_x_2 = 450
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                Game[Gameloop2] = perso_player2

                J2 = "None"

                if Game[Gameloop2] == Game[Gameloop]:
                    Gameloop += 1
                if Game[Gameloop2] == Game[Gameloop3]:
                    Gameloop3 += 1
                if Game[Gameloop2] == Game[Gameloop4]:
                    Gameloop4 += 1
                clic.play()

            if Validate.validation_rect3.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide3:
                Valide3 = False

                valid_on_pos_x_3 = 760
                valid_pos_x_3 = -150
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                if Game[Gameloop3] == Game[Gameloop]:
                    if Gameloop3 == len(Game) - 1:
                        Gameloop = 0
                    Gameloop += 1
                    while Game[Gameloop] == "0":
                        Gameloop += 1
                    perso_player = Game[Gameloop]
                if Game[Gameloop3] == Game[Gameloop2]:
                    if Gameloop3 == len(Game) - 1:
                        Gameloop2 = 0
                    Gameloop2 += 1
                    while Game[Gameloop2] == "0":
                        Gameloop2 += 1
                    perso_player2 = Game[Gameloop2]
                if Game[Gameloop3] == Game[Gameloop4]:
                    if Gameloop3 == len(Game) - 1:
                        Gameloop4 = 0
                    Gameloop4 += 1
                    while Game[Gameloop4] == "0":
                        Gameloop4 += 1
                    perso_player4 = Game[Gameloop4]

                J3 = perso_player3

                Game[Gameloop3] = "0"

                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                clic.play()
            elif Validate.validation_on_rect3.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                Valide3 = True

                valid_on_pos_x_3 = -150
                valid_pos_x_3 = 760
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                Game[Gameloop3] = perso_player3

                J3 = "None"

                if Game[Gameloop3] == Game[Gameloop]:
                    Gameloop += 1
                if Game[Gameloop3] == Game[Gameloop2]:
                    Gameloop2 += 1
                if Game[Gameloop3] == Game[Gameloop4]:
                    Gameloop4 += 1
                clic.play()

            if Validate.validation_rect4.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP and Valide4:
                Valide4 = False

                valid_on_pos_x_4 = 1070
                valid_pos_x_4 = -150
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                if Game[Gameloop4] == Game[Gameloop]:
                    if Gameloop4 == len(Game) - 1:
                        Gameloop = 0
                    Gameloop += 1
                    while Game[Gameloop] == "0":
                        Gameloop += 1
                    perso_player = Game[Gameloop]
                if Game[Gameloop4] == Game[Gameloop2]:
                    if Gameloop4 == len(Game) - 1:
                        Gameloop2 = 0
                    Gameloop2 += 1
                    while Game[Gameloop2] == "0":
                        Gameloop2 += 1
                    perso_player2 = Game[Gameloop2]
                if Game[Gameloop4] == Game[Gameloop3]:
                    if Gameloop4 == len(Game) - 1:
                        Gameloop3 = 0
                    Gameloop3 += 1
                    while Game[Gameloop3] == "0":
                        Gameloop3 += 1
                    perso_player3 = Game[Gameloop3]

                J4 = perso_player4

                Game[Gameloop4] = "0"

                player = SelectPerso.Select(perso_player, perso_player2, perso_player3, perso_player4)
                clic.play()
            elif Validate.validation_on_rect4.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                Valide4 = True

                valid_on_pos_x_4 = -150
                valid_pos_x_4 = 1070
                Validate = SelectPerso.Validate(valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4,
                                                valid_pos_x, valid_pos_x_2, valid_pos_x_3, valid_pos_x_4)

                Game[Gameloop4] = perso_player4

                J4 = "None"

                if Game[Gameloop4] == Gameloop:
                    Gameloop += 1
                if Game[Gameloop4] == Game[Gameloop2]:
                    Gameloop2 += 1
                if Game[Gameloop4] == Game[Gameloop3]:
                    Gameloop3 += 1
                clic.play()

            if SetRect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                clic.play()
                running = False
                In_Game(J1, J2, J3, J4)


# Fonction de la boucle En jeu
def In_Game(J1, J2, J3, J4):
    setting_file = open("Setting.txt", "r")
    list_of_lines = setting_file.readlines()
    # Creation de la variable inv_On (inventaire)
    inv_On = False
    # Creation de la variable Buy_Gui_On
    Buy_Gui_On = False

    # Creation des variables des affichages Oui ou Non
    inv_1_On = False
    inv_2_On = False
    inv_3_On = False
    inv_4_On = False

    Buy_bt_gui_1 = False
    Buy_bt_gui_2 = False
    Buy_bt_gui_3 = False
    Buy_bt_gui_4 = False

    # Liste Pseudo Joueur
    GamePlayerLoop = []

    lancer_de = {}
    lancer_de["de_1_lancer"] = 1
    lancer_de["de_2_lancer"] = 0
    lancer_de["de_3_lancer"] = 0
    lancer_de["de_4_lancer"] = 0

    buy_dico = {}
    buy_dico["can_buy_1"] = 1
    buy_dico["can_buy_2"] = 1
    buy_dico["can_buy_3"] = 1
    buy_dico["can_buy_4"] = 1

    end_dico = {}
    end_dico['end_loop'] = 0
    end_dico['end_loop_2'] = 0
    end_dico['end_loop_3'] = 0
    end_dico['end_loop_4'] = 0

    # Creation des Noms des Joueurs
    Player_Dico = {}

    Player_Dico["joueur_1"] = InGame.Joueur(J1, (32, 32), 10, 10, int(list_of_lines[7].split()[1]))
    Player_Dico["joueur_2"] = InGame.Joueur(J2, (32, 32), 1140, 10, int(list_of_lines[7].split()[1]))
    Player_Dico["joueur_3"] = InGame.Joueur(J3, (32, 32), 10, 510, int(list_of_lines[7].split()[1]))
    Player_Dico["joueur_4"] = InGame.Joueur(J4, (32, 32), 1140, 510, int(list_of_lines[7].split()[1]))

    joueur_1 = InGame.Joueur(J1, (32, 32), 10, 10, int(list_of_lines[7].split()[1]))
    joueur_2 = InGame.Joueur(J2, (32, 32), 1140, 10, int(list_of_lines[7].split()[1]))
    joueur_3 = InGame.Joueur(J3, (32, 32), 10, 510, int(list_of_lines[7].split()[1]))
    joueur_4 = InGame.Joueur(J4, (32, 32), 1140, 510, int(list_of_lines[7].split()[1]))
    setting_file.close()

    # Generation Bouton d'achat
    Buy_button = pygame.image.load("img/img/Element/Ingame/Icon/Buy.png").convert_alpha()
    Buy_button = pygame.transform.scale(Buy_button, (64, 64))
    Buy_button_rect = Buy_button.get_rect()

    Buy_button_rect.x, Buy_button_rect.y = -900, 320

    # Generation d'un bouton Upgrade Button
    Upgrade_bt = pygame.image.load("img/img/Element/InGame/Icon/Upgrade.png").convert_alpha()
    Upgrade_bt = pygame.transform.scale(Upgrade_bt, (64, 64))
    Upgrade_bt_rect = Upgrade_bt.get_rect()
    Upgrade_bt_rect.x, Upgrade_bt_rect.y = -900, 390

    # Generation du bouton pour finir le tour
    End_button = pygame.image.load("img/img/Element/Ingame/Icon/End.png").convert_alpha()
    End_button = pygame.transform.scale(End_button, (64, 64))
    End_button_rect = End_button.get_rect()
    End_button_rect.x, End_button_rect.y = -900, 250

    # Creation du dictionary
    d = {}

    # Generation de toute les cartes
    d["Card_0"] = InGame.Card("Start", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_1"] = InGame.Card("Tuyaux", 2, 10, 30, 90, 160, 250, 30, 50, 60, False, None, "house", 0, None)

    d["Card_2"] = InGame.Card("Carte de l'étoile", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_3"] = InGame.Card("Champignion ressort", 4, 20, 60, 180, 320, 450, 30, 50, 60, False, None, "house", 0,
                              None)

    d["Card_4"] = InGame.Card("Impôts", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)
    d["Card_5"] = InGame.Card("Coupe Carapace", 0, 0, 0, 0, 0, 0, 0, 0, 0, False, None, None, None, None)

    d["Card_6"] = InGame.Card("Bateau Abandonnee", 6, 30, 90, 270, 400, 550, 50, 50, 100, False, None, "house", 0, None)

    d["Card_7"] = InGame.Card("Chance", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_8"] = InGame.Card("Mini-Chateau de Brjunior", 6, 30, 90, 270, 400, 550, 50, 50, 100, False, None, "house",
                              0, None)
    d["Card_9"] = InGame.Card("Vaisseau Volant de BrJunior", 6, 30, 90, 270, 400, 550, 50, 50, 120, False, None,
                              "house", 0, None)

    d["Card_10"] = InGame.Card("Simple Visite", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_11"] = InGame.Card("Koopa", 10, 50, 150, 450, 625, 750, 70, 100, 140, False, None, "house", 0, None)

    d["Card_12"] = InGame.Card("Compagnie de la fleur de feu", 0, 0, 0, 0, 0, 0, 0, 0, 0, False, None, None, None, None)

    d["Card_13"] = InGame.Card("Goomba", 10, 50, 150, 450, 625, 750, 70, 100, 140, False, None, "house", 0, None)
    d["Card_14"] = InGame.Card("Kamec", 12, 60, 180, 500, 700, 900, 80, 100, 160, False, None, "house", 0, None)

    d["Card_15"] = InGame.Card("Coupe Banane", 0, 0, 0, 0, 0, 0, 0, 0, 0, False, None, None, None, None)

    d["Card_16"] = InGame.Card("Casquette Mario-Odyssey", 14, 70, 200, 550, 750, 950, 90, 100, 180, False, None,
                               "house", 0, None)

    d["Card_17"] = InGame.Card("Carte de l'étoile", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_18"] = InGame.Card("Champignion Mario-Helice", 14, 70, 200, 550, 750, 950, 90, 100, 180, False, None,
                               "house", 0, None)
    d["Card_19"] = InGame.Card("Marteau des freres", 16, 80, 220, 600, 800, 1000, 100, 100, 200, False, None, "house",
                               0, None)

    d["Card_20"] = InGame.Card("Case evenements", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_21"] = InGame.Card("Casquette Luigi", 18, 90, 250, 700, 925, 1050, 110, 150, 220, False, None, "house", 0,
                               None)

    d["Card_22"] = InGame.Card("Chance", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_23"] = InGame.Card("Aspirateur Luigi", 18, 90, 250, 700, 925, 1050, 110, 150, 220, False, None, "house", 0,
                               None)
    d["Card_24"] = InGame.Card("Manoir De Luigi", 20, 100, 300, 750, 925, 1100, 30, 150, 240, False, None, "house", 0,
                               None)

    d["Card_25"] = InGame.Card("Coupe Feuille", 0, 0, 0, 0, 0, 0, 0, 0, 0, False, None, None, None, None)

    d["Card_26"] = InGame.Card("Vaisseau Toad", 22, 110, 330, 800, 975, 1150, 130, 150, 260, False, None, "house", 0,
                               None)
    d["Card_27"] = InGame.Card("Magazin Toad", 22, 110, 330, 800, 975, 1150, 130, 150, 260, False, None, "house", 0,
                               None)

    d["Card_28"] = InGame.Card("Compagnie du champignion", 0, 0, 0, 0, 0, 0, 0, 0, 0, False, None, None, None, None)

    d["Card_29"] = InGame.Card("Village Toad", 24, 120, 360, 850, 1025, 1200, 140, 150, 280, False, None, "house", 0,
                               None)

    d["Card_30"] = InGame.Card("Prison", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_31"] = InGame.Card("Chateau de Bowser", 26, 130, 390, 900, 1100, 1275, 150, 200, 300, False, None, "house",
                               0, None)
    d["Card_32"] = InGame.Card("Chateau de la Princesse Peach", 26, 130, 390, 900, 1100, 1275, 150, 200, 300, False,
                               None,
                               "house", 0, None)

    d["Card_33"] = InGame.Card("Carte de l'étoile", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_34"] = InGame.Card("Chateau de la Princesse Xhampi", 28, 150, 450, 1000, 1200, 1400, 160, 200, 320, False,
                               None,
                               "house", 0, None)

    d["Card_35"] = InGame.Card("Coupe Eclair", 0, 0, 0, 0, 0, 0, 0, 0, 0, False, None, None, None, None)
    d["Card_36"] = InGame.Card("Chance", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_37"] = InGame.Card("Vaisseau Mario", 35, 175, 500, 1100, 1300, 1500, 175, 200, 350, False, None, "house", 0,
                               None)

    d["Card_38"] = InGame.Card("Taxe de luxe", 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None)

    d["Card_-1"] = InGame.Card("Observatoire de la Comète", 50, 200, 600, 1400, 1700, 1200, 200, 200, 400, False, None,
                               "house", 0, None)

    if joueur_1.joueur != "None":
        GamePlayerLoop.append(joueur_1.joueur)
    if joueur_2.joueur != "None":
        GamePlayerLoop.append(joueur_2.joueur)
    if joueur_3.joueur != "None":
        GamePlayerLoop.append(joueur_3.joueur)
    if joueur_4.joueur != "None":
        GamePlayerLoop.append(joueur_4.joueur)

    print(GamePlayerLoop)

    Dice = SelectPerso.dice()

    running = True

    loop = 0

    # Creation des differentes places des joueurs
    Gameloop_1, Gameloop_2, Gameloop_3, Gameloop_4 = 0, 0, 0, 0

    Case = [(920, 680), (835, 660), (770, 660), (715, 660), (655, 660), (595, 660), (540, 660), (475, 660), (420, 660),
            (360, 660), (270, 660),
            (280, 580), (280, 525), (280, 460), (280, 405), (280, 340), (280, 280), (280, 225), (280, 165), (280, 105),
            (290, 45),
            (360, 30), (420, 30), (480, 30), (540, 30), (600, 30), (655, 30), (715, 30), (775, 30), (835, 30),
            (915, 30),
            (920, 110), (920, 170), (920, 225), (920, 285), (920, 345), (920, 405), (920, 465), (920, 525), (920, 585)]

    Case_player_1 = Case[Gameloop_1]
    Case_player_2 = Case[Gameloop_2]
    Case_player_3 = Case[Gameloop_3]
    Case_player_4 = Case[Gameloop_4]

    PlayerLoop = SelectPerso.Bt_Game_Loop(GamePlayerLoop[0])
    if J2 != "None":
        PlayerLoop_2 = SelectPerso.Bt_Game_Loop(GamePlayerLoop[1])
    if J3 != "None":
        PlayerLoop_3 = SelectPerso.Bt_Game_Loop(GamePlayerLoop[2])
    if J4 != "None":
        PlayerLoop_4 = SelectPerso.Bt_Game_Loop(GamePlayerLoop[3])
    # ============================================ Boucle de Jeu =======================================================
    while running:
        screen.blit(background, (0, 0))
        screen.blit(plateau_img, (250, 0))

        Upgrade_bt_rect.x, Upgrade_bt_rect.y = -900, 390

        font_text = pygame.font.Font('Divers/Font/MATURASC.TTF', 28)
        text_money = font_text.render(str(joueur_1.money) + " $", False, (255, 255, 255))

        text_money2 = font_text.render(str(joueur_2.money) + " $", False, (255, 255, 255))
        text_money3 = font_text.render(str(joueur_3.money) + " $", False, (255, 255, 255))
        text_money4 = font_text.render(str(joueur_4.money) + " $", False, (255, 255, 255))

        screen.blit(Inventory_Bt, Inventory_Bt_rect)

        screen.blit(joueur_1.image_frame, joueur_1.image_frame_rect)
        screen.blit(joueur_2.image_frame, joueur_2.image_frame_rect)
        screen.blit(joueur_3.image_frame, joueur_3.image_frame_rect)
        screen.blit(joueur_4.image_frame, joueur_4.image_frame_rect)

        screen.blit(joueur_1.image_money, joueur_1.image_money_rect)
        screen.blit(joueur_2.image_money, joueur_2.image_money_rect)
        screen.blit(joueur_3.image_money, joueur_3.image_money_rect)
        screen.blit(joueur_4.image_money, joueur_4.image_money_rect)

        screen.blit(text_money, (joueur_1.image_money_rect.x + 30, joueur_1.image_money_rect.y + 20))
        screen.blit(text_money2, (joueur_2.image_money_rect.x + 30, joueur_2.image_money_rect.y + 20))
        screen.blit(text_money3, (joueur_3.image_money_rect.x + 30, joueur_3.image_money_rect.y + 20))
        screen.blit(text_money4, (joueur_4.image_money_rect.x + 30, joueur_4.image_money_rect.y + 20))

        screen.blit(joueur_1.image_joueur, Case_player_1)
        screen.blit(joueur_2.image_joueur, Case_player_2)
        screen.blit(joueur_3.image_joueur, Case_player_3)
        screen.blit(joueur_4.image_joueur, Case_player_4)

        screen.blit(CadreDes, (520, 100))
        screen.blit(Dice.dice_image, (540, 120))
        screen.blit(Dice.dice_image_two, (620, 120))

        # =====================================================Logique du jeu===========================================
        if Gameloop_1 >= len(Case) - 1: Gameloop_1 = 0
        if Gameloop_2 >= len(Case) - 1: Gameloop_2 = 0
        if Gameloop_3 >= len(Case) - 1: Gameloop_3 = 0
        if Gameloop_4 >= len(Case) - 1: Gameloop_4 = 0

        # ==================================Boucle de jeu===============================================================

        if lancer_de["de_1_lancer"] == 1:
            PlayerLoop.player_dice_img_rect.x = 1020
        if lancer_de["de_2_lancer"] == 1:
            if J2 != "None": PlayerLoop_2.player_dice_img_rect.x = 1020
        if lancer_de["de_3_lancer"] == 1:
            if J3 != "None": PlayerLoop_3.player_dice_img_rect.x = 1020
        if lancer_de["de_4_lancer"] == 1:
            if J4 != "None": PlayerLoop_4.player_dice_img_rect.x = 1020

        if lancer_de["de_1_lancer"] == 0:
            PlayerLoop.player_dice_img_rect.x = -1020
        if lancer_de["de_2_lancer"] == 0:
            if J2 != "None": PlayerLoop_2.player_dice_img_rect.x = -1020
        if lancer_de["de_3_lancer"] == 0:
            if J3 != "None": PlayerLoop_3.player_dice_img_rect.x = -1020
        if lancer_de["de_4_lancer"] == 0:
            if J4 != "None": PlayerLoop_4.player_dice_img_rect.x = -1020

        # disparition des boutons
        if end_dico["end_loop"] == 0:
            if J1 != "None":
                End_button_rect.x = -1020
                Buy_button_rect.x = -1020
        if end_dico["end_loop_2"] == 0:
            if J2 != "None":
                End_button_rect.x = -1020
                Buy_button_rect.x = -1020
        if end_dico["end_loop_3"] == 0:
            if J3 != "None":
                End_button_rect.x = -1020
                Buy_button_rect.x = -1020
        if end_dico["end_loop_4"] == 0:
            if J4 != "None":
                End_button_rect.x = -1020
                Buy_button_rect.x = -1020

        # Reaparition des boutons
        if end_dico["end_loop"] == 1:
            if J1 != "None":
                End_button_rect.x = 1020
                if buy_dico["can_buy_1"] == 1:
                    Buy_button_rect.x = 1020
                    if d[f"Card_{Gameloop_1}"].type is None or d[f"Card_{Gameloop_1}"].ownered == True:
                        Buy_button_rect.x = -1020
                    else:
                        Buy_button_rect.x = 1020
        if end_dico["end_loop_2"] == 1:
            if J2 != "None":
                End_button_rect.x = 1020
                if buy_dico["can_buy_2"] == 1:
                    Buy_button_rect.x = 1020
                    if d[f"Card_{Gameloop_2}"].type is None or d[f"Card_{Gameloop_2}"].ownered == True:
                        Buy_button_rect.x = -1020
                    else:
                        Buy_button_rect.x = 1020
        if end_dico["end_loop_3"] == 1:
            if J3 != "None":
                End_button_rect.x = 1020
                if buy_dico["can_buy_3"] == 1:
                    Buy_button_rect.x = 1020
                    if d[f"Card_{Gameloop_3}"].type is None or d[f"Card_{Gameloop_3}"].ownered == True:
                        Buy_button_rect.x = -1020
                    else:
                        Buy_button_rect.x = 1020
        if end_dico["end_loop_4"] == 1:
            if J4 != "None":
                End_button_rect.x = 1020
                if buy_dico["can_buy_3"] == 1:
                    Buy_button_rect.x = 1020
                    if d[f"Card_{Gameloop_4}"].type is None or d[f"Card_{Gameloop_4}"].ownered == True:
                        Buy_button_rect.x = -1020
                    else:
                        Buy_button_rect.x = 1020
        # ==============================================================================================================

        if J1 != "None":
            if lancer_de["de_1_lancer"] == 1:
                screen.blit(PlayerLoop.player_dice_img, PlayerLoop.player_dice_img_rect)
        if J2 != "None":
            if lancer_de["de_2_lancer"] == 1:
                screen.blit(PlayerLoop_2.player_dice_img, PlayerLoop_2.player_dice_img_rect)
        if J3 != "None":
            if lancer_de["de_3_lancer"] == 1:
                screen.blit(PlayerLoop_3.player_dice_img, PlayerLoop_3.player_dice_img_rect)
        if J4 != "None":
            if lancer_de["de_4_lancer"] == 1:
                screen.blit(PlayerLoop_4.player_dice_img, PlayerLoop_4.player_dice_img_rect)
        # ===================================== Buy Gui ================================================================
        if Buy_Gui_On:
            if Buy_bt_gui_1:
                screen.blit(image_buy_inv, (0, 0))
                d[f"Card_{Gameloop_1}"].rect.x, d[f"Card_{Gameloop_1}"].rect.y = 380, 200
                screen.blit(d[f"Card_{Gameloop_1}"].image, d[f"Card_{Gameloop_1}"].rect)
                if not d[f"Card_{Gameloop_1}"].ownered:
                    Buy_button_rect.x, Buy_button_rect.y = 600, 320
                screen.blit(Buy_button, Buy_button_rect)
            if Buy_bt_gui_2:
                screen.blit(image_buy_inv, (0, 0))
                d[f"Card_{Gameloop_2}"].rect.x, d[f"Card_{Gameloop_2}"].rect.y = 380, 200
                screen.blit(d[f"Card_{Gameloop_2}"].image, d[f"Card_{Gameloop_2}"].rect)
                if not d[f"Card_{Gameloop_2}"].ownered:
                    Buy_button_rect.x, Buy_button_rect.y = 600, 320
                screen.blit(Buy_button, Buy_button_rect)
            if Buy_bt_gui_3:
                screen.blit(image_buy_inv, (0, 0))
                d[f"Card_{Gameloop_3}"].rect.x, d[f"Card_{Gameloop_3}"].rect.y = 380, 200
                screen.blit(d[f"Card_{Gameloop_3}"].image, d[f"Card_{Gameloop_3}"].rect)
                if not d[f"Card_{Gameloop_4}"].ownered:
                    Buy_button_rect.x, Buy_button_rect.y = 600, 320
                screen.blit(Buy_button, Buy_button_rect)
            if Buy_bt_gui_4:
                screen.blit(image_buy_inv, (0, 0))
                d[f"Card_{Gameloop_4}"].rect.x, d[f"Card_{Gameloop_4}"].rect.y = 380, 200
                screen.blit(d[f"Card_{Gameloop_4}"].image, d[f"Card_{Gameloop_4}"].rect)
                if not d[f"Card_{Gameloop_4}"].ownered:
                    Buy_button_rect.x, Buy_button_rect.y = 600, 320
                screen.blit(Buy_button, Buy_button_rect)

        # ===================================== Upgrade Bt =============================================================
        if d[f"Card_{Gameloop_1}"].owner_name == joueur_1.joueur and loop == 0:
            Upgrade_bt_rect.x, Upgrade_bt_rect.y = 1080, 390
            screen.blit(Upgrade_bt, Upgrade_bt_rect)
            print('yes')
        if d[f"Card_{Gameloop_2}"].owner_name == joueur_2.joueur and loop == 1:
            Upgrade_bt_rect.x, Upgrade_bt_rect.y = 1080, 390
            screen.blit(Upgrade_bt, Upgrade_bt_rect)
        if d[f"Card_{Gameloop_3}"].owner_name == joueur_2.joueur and loop == 2:
            Upgrade_bt_rect.x, Upgrade_bt_rect.y = 1080, 390
            screen.blit(Upgrade_bt, Upgrade_bt_rect)
        if d[f"Card_{Gameloop_4}"].owner_name == joueur_2.joueur and loop == 3:
            Upgrade_bt_rect.x, Upgrade_bt_rect.y = 1080, 390
            screen.blit(Upgrade_bt, Upgrade_bt_rect)
        # =========================================Event du jeu=========================================================
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if Inventory_Bt_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                inv_On = True
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE and inv_On:
                    inv_On = False
                    print("coucou")

            if not inv_On:
                if PlayerLoop.player_dice_img_rect.collidepoint(x,
                                                                y) and event.type == pygame.MOUSEBUTTONUP and not Buy_Gui_On:
                    Dice.lancer_de()
                    clic.play()
                    if loop == 0:
                        Gameloop_1 += Dice.dice_one + Dice.dice_two
                        if Gameloop_1 >= 39:
                            Gameloop_1 -= 40
                        Case_player_1 = Case[Gameloop_1]
                        buy_dico["can_buy_1"] = 1
                        lancer_de["de_1_lancer"] = 0
                        end_dico["end_loop"] = 1
                    if d[f"Card_{Gameloop_1}"].ownered:
                        if joueur_1.money - d[f"Card_{Gameloop_1}"].cost < 0:
                            old_cost = joueur_1.money - d[f"Card_{Gameloop_1}"].cost
                            cost = d[f"Card_{Gameloop_1}"].cost - old_cost
                            joueur_1.money -= cost

                        else:
                            joueur_1.money -= d[f"Card_{Gameloop_1}"].cost
                            Player_Dico[f"{d[f'Card_{Gameloop_1}'].class_name}"].money += d[f"Card_{Gameloop_1}"].cost

                # Système d'achat des cases
                if Buy_button_rect.collidepoint(x, y) and event.type == MOUSEBUTTONUP and loop == 0:
                    if joueur_1.money - int(d[f"Card_{Gameloop_1}"].price) >= 0 and Buy_bt_gui_1:
                        joueur_1.money -= int(d[f"Card_{Gameloop_1}"].price)
                        buy_dico["can_buy_1"] = 0
                        d[f"Card_{Gameloop_1}"].ownered = True
                        d[f"Card_{Gameloop_1}"].owner_name = J1
                        d[f"Card_{Gameloop_1}"].class_name = "joueur_1"
                        joueur_1.inventory += [str("Card_" + str(Gameloop_1))]
                        print(joueur_1.inventory)
                    else:
                        print("Tu n'as pas assez d'argent")
                    Buy_Gui_On = True
                    Buy_bt_gui_1 = True
                    image_buy_inv = pygame.image.load(
                        f"img/img/Element/Ingame/Background/Gui/{joueur_1.joueur}_back.png")

                    if d[f"Card_{Gameloop_1}"].ownered == joueur_1.joueur and loop == 0:
                        if Upgrade_bt_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                            screen.blit(image_inv, (0, 0))

                # Gestion des boutons Joueur 2
                if J2 != "None":
                    if PlayerLoop_2.player_dice_img_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                        Dice.lancer_de()
                        clic.play()
                        if loop == 1:
                            Gameloop_2 += Dice.dice_one + Dice.dice_two
                            if Gameloop_2 >= 39:
                                Gameloop_2 -= 40
                            Case_player_2 = Case[Gameloop_2]
                            buy_dico["can_buy_2"] = 1
                            lancer_de["de_2_lancer"] = 0
                            end_dico["end_loop_2"] = 1
                        if d[f"Card_{Gameloop_2}"].ownered:
                            if joueur_2.money - d[f"Card_{Gameloop_2}"].cost < 0:
                                old_cost = joueur_2.money - d[f"Card_{Gameloop_2}"].cost
                                cost = d[f"Card_{Gameloop_2}"].cost - old_cost
                                joueur_2.money -= cost

                            else:
                                joueur_2.money -= d[f"Card_{Gameloop_2}"].cost
                                Player_Dico[f"{d[f'Card_{Gameloop_2}'].class_name}"].money += d[
                                    f"Card_{Gameloop_2}"].cost
                    if Buy_button_rect.collidepoint(x, y) and event.type == MOUSEBUTTONUP and loop == 1:

                        image_buy_inv = pygame.image.load(
                            f"img/img/Element/Ingame/Background/Gui/{joueur_2.joueur}_back.png")
                        if joueur_2.money - int(d[f"Card_{Gameloop_2}"].price) >= 0 and Buy_bt_gui_2:
                            joueur_2.money -= int(d[f"Card_{Gameloop_2}"].price)
                            buy_dico["can_buy_2"] = 0
                            d[f"Card_{Gameloop_2}"].ownered = True
                            d[f"Card_{Gameloop_2}"].owner_name = J2
                            d[f"Card_{Gameloop_2}"].class_name = "joueur_2"
                            joueur_2.inventory += [str("Card_" + str(Gameloop_2))]
                        else:
                            print("Tu n'as pas assez d'argent")
                        Buy_Gui_On = True
                        Buy_bt_gui_2 = True

                # Gestion des boutons Joueur 3
                if J3 != "None":
                    if PlayerLoop_3.player_dice_img_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                        Dice.lancer_de()
                        clic.play()
                        if loop == 2:
                            Gameloop_3 += Dice.dice_one + Dice.dice_two
                            if Gameloop_3 >= 39:
                                Gameloop_3 -= 40
                            Case_player_3 = Case[Gameloop_3]
                            buy_dico["can_buy_3"] = 1
                            lancer_de["de_3_lancer"] = 0
                            end_dico["end_loop_3"] = 1
                        if d[f"Card_{Gameloop_3}"].ownered:
                            if joueur_3.money - d[f"Card_{Gameloop_3}"].cost < 0:
                                old_cost = joueur_1.money - d[f"Card_{Gameloop_3}"].cost
                                cost = d[f"Card_{Gameloop_3}"].cost - old_cost
                                joueur_3.money -= cost

                            else:
                                joueur_3.money -= d[f"Card_{Gameloop_3}"].cost
                                Player_Dico[f"{d[f'Card_{Gameloop_3}'].class_name}"].money += d[
                                    f"Card_{Gameloop_3}"].cost
                    if Buy_button_rect.collidepoint(x,
                                                    y) and event.type == MOUSEBUTTONUP and loop == 2 and Buy_bt_gui_3:

                        image_buy_inv = pygame.image.load(
                            f"img/img/Element/Ingame/Background/Gui/{joueur_3.joueur}_back.png")
                        if joueur_3.money - int(d[f"Card_{Gameloop_3}"].price) >= 0 and Buy_bt_gui_3:
                            joueur_3.money -= int(d[f"Card_{Gameloop_3}"].price)
                            buy_dico["can_buy_3"] = 0
                            d[f"Card_{Gameloop_3}"].ownered = True
                            d[f"Card_{Gameloop_3}"].owner_name = J3
                            d[f"Card_{Gameloop_3}"].class_name = "joueur_3"
                            joueur_3.inventory += [str("Card_" + str(Gameloop_3))]
                        else:
                            print("Tu n'as pas assez d'argent")
                        Buy_Gui_On = True
                        Buy_bt_gui_3 = True

                # Gestion des boutons Joueur 4
                if J4 != "None":
                    if PlayerLoop_4.player_dice_img_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                        Dice.lancer_de()
                        clic.play()
                        if loop == 3:
                            Gameloop_4 += Dice.dice_one + Dice.dice_two
                            if Gameloop_4 >= 39:
                                Gameloop_4 -= 40
                            Case_player_4 = Case[Gameloop_4]
                            buy_dico["can_buy_4"] = 1
                            lancer_de["de_4_lancer"] = 0
                            end_dico["end_loop_4"] = 1
                        if d[f"Card_{Gameloop_4}"].ownered:
                            if joueur_4.money - d[f"Card_{Gameloop_4}"].cost < 0:
                                old_cost = joueur_4.money - d[f"Card_{Gameloop_4}"].cost
                                cost = d[f"Card_{Gameloop_4}"].cost - old_cost
                                joueur_4.money -= cost

                            else:
                                joueur_4.money -= d[f"Card_{Gameloop_4}"].cost
                                Player_Dico[f"{d[f'Card_{Gameloop_4}'].class_name}"].money += d[
                                    f"Card_{Gameloop_4}"].cost
                    if Buy_button_rect.collidepoint(x,
                                                    y) and event.type == MOUSEBUTTONUP and loop == 3 and Buy_bt_gui_4:

                        image_buy_inv = pygame.image.load(
                            f"img/img/Element/Ingame/Background/Gui/{joueur_4.joueur}_back.png")
                        if joueur_4.money - int(d[f"Card_{Gameloop_4}"].price) >= 0 and Buy_bt_gui_4:
                            joueur_4.money -= int(d[f"Card_{Gameloop_4}"].price)
                            buy_dico["can_buy_4"] = 0
                            d[f"Card_{Gameloop_4}"].ownered = True
                            d[f"Card_{Gameloop_4}"].owner_name = J4
                            d[f"Card_{Gameloop_4}"].class_name = "joueur_4"
                            joueur_4.inventory += [str("Card_" + str(Gameloop_4))]
                        else:
                            print("Tu n'as pas assez d'argent")
                        Buy_Gui_On = True
                        Buy_bt_gui_4 = True

                if event.type == MOUSEBUTTONUP and End_button_rect.collidepoint(x, y):
                    loop += 1
                    if loop == len(GamePlayerLoop):
                        loop = 0
                    print(loop)
                    end_dico["end_loop"] = 0
                    end_dico["end_loop_2"] = 0
                    end_dico["end_loop_3"] = 0
                    end_dico["end_loop_4"] = 0

                    Buy_Gui_On = False

                    Buy_bt_gui_1 = False
                    Buy_bt_gui_2 = False
                    Buy_bt_gui_3 = False
                    Buy_bt_gui_4 = False

                    lancer_de[f"de_{loop + 1}_lancer"] = 1
            if inv_On:
                if joueur_1.image_joueur_rect_2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                    image_inv = pygame.image.load(
                        f"img/img/Element/Ingame/Background/Background_Inv/{joueur_1.joueur}_1.png")
                    inv_1_On, inv_2_On, inv_3_On, inv_4_On = True, False, False, False
                if joueur_2.image_joueur_rect_2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                    image_inv = pygame.image.load(
                        f"img/img/Element/Ingame/Background/Background_Inv/{joueur_2.joueur}_2.png")
                    inv_1_On, inv_2_On, inv_3_On, inv_4_On = False, True, False, False
                if joueur_3.image_joueur_rect_2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                    image_inv = pygame.image.load(
                        f"img/img/Element/Ingame/Background/Background_Inv/{joueur_3.joueur}_3.png")
                    inv_1_On, inv_2_On, inv_3_On, inv_4_On = False, False, True, False
                if joueur_4.image_joueur_rect_2.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONUP:
                    image_inv = pygame.image.load(
                        f"img/img/Element/Ingame/Background/Background_Inv/{joueur_4.joueur}_4.png")
                    inv_1_On, inv_2_On, inv_3_On, inv_4_On = False, False, False, True
        # =========================================Inventaire=======================================================

        # Système d'upgrade du prix des maison

        screen.blit(Buy_button, Buy_button_rect)
        screen.blit(End_button, End_button_rect)

        if inv_On:
            screen.blit(Inventory, Inventory_rect)
            if inv_1_On:
                screen.blit(image_inv, (0, 0))
                coords = 120
                for items in joueur_1.inventory:
                    d[f"{items}"].rect.x, d[f"{items}"].rect.y = coords, 240
                    screen.blit(d[f"{items}"].image, (coords, 240))
                    coords += 40
            joueur_1.image_joueur_rect_2.x, joueur_1.image_joueur_rect_2.y = 165, 130
            screen.blit(joueur_1.image_joueur, joueur_1.image_joueur_rect_2)
            if J2 != "None":
                if inv_2_On:
                    screen.blit(image_inv, (0, 0))
                    if inv_2_On:
                        screen.blit(image_inv, (0, 0))
                        coords = 120
                        for items in joueur_2.inventory:
                            screen.blit(d[f"{items}"].image, (coords, 240))
                            coords += 40
                joueur_2.image_joueur_rect_2.x, joueur_2.image_joueur_rect_2.y = 225, 130
                screen.blit(joueur_2.image_joueur, joueur_2.image_joueur_rect_2)
            if J3 != "None":
                if inv_3_On:
                    screen.blit(image_inv, (0, 0))
                    if inv_1_On:
                        screen.blit(image_inv, (0, 0))
                        coords = 120
                        for items in joueur_3.inventory:
                            screen.blit(d[f"{items}"].image, (coords, 240))
                            coords += 40
                joueur_3.image_joueur_rect_2.x, joueur_3.image_joueur_rect_2.y = 290, 130
                screen.blit(joueur_3.image_joueur, joueur_3.image_joueur_rect_2)
            if J4 != "None":
                if inv_4_On:
                    screen.blit(image_inv, (0, 0))
                    if inv_4_On:
                        screen.blit(image_inv, (0, 0))
                        coords = 120
                        for items in joueur_4.inventory:
                            screen.blit(d[f"{items}"].image, (coords, 240))
                            coords += 40
                joueur_4.image_joueur_rect_2.x, joueur_4.image_joueur_rect_2.y = 355, 130
                screen.blit(joueur_4.image_joueur, joueur_4.image_joueur_rect_2)

        pygame.display.flip()


# Lancement du Menu
Menu()
# matthéo
