import pygame
import random

file_name = 'img_2'

# Class qui gère la selection des personnages
class Select(pygame.sprite.Sprite):
    def __init__(self, perso_player, perso_player2, perso_player3, perso_player4):
        super().__init__()
        self.player = perso_player
        self.image = pygame.image.load(file_name+f"/img/Element/Menu/Perso/{self.player}Select.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (256, 384))
        self.image.set_colorkey((255, 0, 243))
        self.img_rect = self.image.get_rect()
        self.img_rect.x, self.img_rect.y = 51, 41

        self.player2 = perso_player2
        self.image2 = pygame.image.load(file_name+f"\img\Element\Menu\Perso\{self.player2}Select.png").convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (256, 384))
        self.image2.set_colorkey((255, 0, 243))
        self.img_rect2 = self.image2.get_rect()
        self.img_rect2.x, self.img_rect2.y = 358, 41

        self.player3 = perso_player3
        self.image3 = pygame.image.load(file_name+f"\img\Element\Menu\Perso\{self.player3}Select.png").convert_alpha()
        self.image3 = pygame.transform.scale(self.image3, (256, 384))
        self.image3.set_colorkey((255, 0, 243))
        self.img_rect3 = self.image3.get_rect()
        self.img_rect3.x, self.img_rect3.y = 665, 41

        self.player4 = perso_player4
        self.image4 = pygame.image.load(file_name+f"\img\Element\Menu\Perso\{self.player4}Select.png").convert_alpha()
        self.image4 = pygame.transform.scale(self.image4, (256, 384))
        self.image4.set_colorkey((255, 0, 243))
        self.img_rect4 = self.image4.get_rect()
        self.img_rect4.x, self.img_rect4.y = 972, 41

# Class qui gère le bouton Dé sur le Joueur
class Bt_Game_Loop(pygame.sprite.Sprite):
    def __init__(self, player_turn):
        super(Bt_Game_Loop, self).__init__()
        self.player_dice_bt = player_turn
        self.player_dice_img = pygame.image.load(file_name + f"/img/Element/Ingame/Icon/{self.player_dice_bt}De.png")
        self.player_dice_img = pygame.transform.scale(self.player_dice_img, (64, 64))
        self.player_dice_img.set_colorkey((255, 0, 243))

        self.player_dice_img_rect = self.player_dice_img.get_rect()
        self.player_dice_img_rect.x, self.player_dice_img_rect.y = 1000, 100

# Class qui gère les fleches de validation pour selectionnée le joueur
class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.right_arrow = pygame.image.load(file_name + "\img\Element\Menu\Perso\RightArrow.png").convert_alpha()
        self.right_arrow = pygame.transform.scale(self.right_arrow, (50, 108))
        self.right_arrow.set_colorkey((255, 0, 243))

        self.right_arrow_rect = self.right_arrow.get_rect()
        self.right_arrow_rect.x, self.right_arrow_rect.y = 270, 300

        self.right_arrow_rect2 = self.right_arrow.get_rect()
        self.right_arrow_rect2.x, self.right_arrow_rect2.y = 570, 300

        self.right_arrow_rect3 = self.right_arrow.get_rect()
        self.right_arrow_rect3.x, self.right_arrow_rect3.y = 880, 300

        self.right_arrow_rect4 = self.right_arrow.get_rect()
        self.right_arrow_rect4.x, self.right_arrow_rect4.y = 1190, 300
        # ---------------------------------------------------------------------------------------------------------------
        self.left_arrow = pygame.image.load(file_name + "\img\Element\Menu\Perso\LeftArrow.png").convert_alpha()
        self.left_arrow = pygame.transform.scale(self.left_arrow, (50, 108))
        self.left_arrow.set_colorkey((255, 0, 243))

        self.left_arrow_rect = self.left_arrow.get_rect()
        self.left_arrow_rect.x, self.left_arrow_rect.y = 45, 300

        self.left_arrow_rect2 = self.left_arrow.get_rect()
        self.left_arrow_rect2.x, self.left_arrow_rect2.y = 355, 300

        self.left_arrow_rect3 = self.left_arrow.get_rect()
        self.left_arrow_rect3.x, self.left_arrow_rect3.y = 660, 300

        self.left_arrow_rect4 = self.left_arrow.get_rect()
        self.left_arrow_rect4.x, self.left_arrow_rect4.y = 960, 300

#Class qui gère le bouton de validation du joueur
class Validate(pygame.sprite.Sprite):
    def __init__(self, valid_on_pos_x, valid_on_pos_x_2, valid_on_pos_x_3, valid_on_pos_x_4, valid_pos_x, valid_pos_x_2,
                 valid_pos_x_3, valid_pos_x_4):
        super().__init__()
        self.validation = pygame.image.load(file_name + "\img\Element\Menu\Perso\Validation.png").convert_alpha()
        self.validation = pygame.transform.scale(self.validation, (64, 64))
        self.validation.set_colorkey((255, 0, 243))

        self.validation_rect = self.validation.get_rect()
        self.validation_rect.x, self.validation_rect.y = valid_pos_x, 400

        self.validation_rect2 = self.validation.get_rect()
        self.validation_rect2.x, self.validation_rect2.y = valid_pos_x_2, 400

        self.validation_rect3 = self.validation.get_rect()
        self.validation_rect3.x, self.validation_rect3.y = valid_pos_x_3, 400

        self.validation_rect4 = self.validation.get_rect()
        self.validation_rect4.x, self.validation_rect4.y = valid_pos_x_4, 400
        # ---------------------------------------------------------------------------------------------------------------
        self.validation_on = pygame.image.load(file_name + "\img\Element\Menu\Perso\ValidationOn.png")
        self.validation_on = pygame.transform.scale(self.validation_on, (64, 64))
        self.validation_on.set_colorkey((255, 0, 243))

        self.validation_on_rect = self.validation_on.get_rect()
        self.validation_on_rect.x, self.validation_on_rect.y = valid_on_pos_x, 400

        self.validation_on_rect2 = self.validation_on.get_rect()
        self.validation_on_rect2.x, self.validation_on_rect2.y = valid_on_pos_x_2, 400

        self.validation_on_rect3 = self.validation_on.get_rect()
        self.validation_on_rect3.x, self.validation_on_rect3.y = valid_on_pos_x_3, 400

        self.validation_on_rect4 = self.validation_on.get_rect()
        self.validation_on_rect4.x, self.validation_on_rect4.y = valid_on_pos_x_4, 400

#Class qui gère l'affichage du dé Ingame
class dice(pygame.sprite.Sprite):
    def __init__(self):
        self.dice_image = pygame.image.load(file_name + '/img/Element/Ingame/d/de1.png').convert()
        self.dice_image = pygame.transform.scale(self.dice_image, (64, 64))
        self.dice_image.set_colorkey((255, 0, 243))

        self.dice_image_two = pygame.image.load(file_name + '/img/Element/Ingame/d/de1.png').convert()
        self.dice_image_two = pygame.transform.scale(self.dice_image, (64, 64))
        self.dice_image_two.set_colorkey((255, 0, 243))

    def lancer_de(self):
        ''' Fonction qui permet de lancer les dée et d'en afficher le chiffre correspondant sur le jeu'''
        self.dice_one = random.randint(1, 6)
        self.dice_image = pygame.image.load(file_name + f'/img/Element/Ingame/d/de{self.dice_one}.png').convert()
        self.dice_image = pygame.transform.scale(self.dice_image, (64, 64))
        self.dice_image.set_colorkey((255, 0, 243))

        self.dice_two = random.randint(1, 6)
        self.dice_image_two = pygame.image.load(file_name + f'/img/Element/Ingame/d/de{self.dice_two}.png').convert()
        self.dice_image_two = pygame.transform.scale(self.dice_image_two, (64, 64))
        self.dice_image_two.set_colorkey((255, 0, 243))
