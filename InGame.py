import pygame

file_name = 'img_2'


# Class qui gère les paramètres du joueurs
class Joueur(pygame.sprite.Sprite):
	def __init__(self, joueur, scale, X, Y, Money):
		super().__init__()
		self.joueur = joueur
		self.image_frame = pygame.image.load(file_name + f"/img/Element/Menu/Perso/{self.joueur}Select.png")
		self.image_frame = pygame.transform.scale(self.image_frame, (128, 192))
		self.image_frame.set_colorkey((255, 0, 243))

		self.image_money = pygame.image.load(file_name + f"/img/Element/Menu/Perso/En jeu/Money_{self.joueur}.png")
		self.image_money = pygame.transform.scale(self.image_money, (128, 64))
		self.image_money.set_colorkey((255, 0, 243))

		self.image_joueur = pygame.image.load(file_name + f"/img/Element/Menu/Perso/En jeu/{self.joueur}_Pion.png")
		self.image_joueur = pygame.transform.scale(self.image_joueur, scale)
		self.image_joueur.set_colorkey((255, 0, 243))

		self.image_joueur_rect = self.image_joueur.get_rect()
		self.image_joueur_rect.centerx = X
		self.image_joueur_rect.centery = Y

		self.image_joueur_rect_2 = self.image_joueur.get_rect()
		self.image_joueur_rect_2.centerx = -200
		self.image_joueur_rect_2.centery = -200

		self.image_money_rect = self.image_money.get_rect()
		self.image_money_rect.x = X
		self.image_money_rect.y = (Y + 130)

		self.image_frame_rect = self.image_frame.get_rect()
		self.image_frame_rect.x = X
		self.image_frame_rect.y = Y

		self.money = int(Money)
		self.inventory = []

		if joueur == "None":
			self.image_frame_rect.x = -10000
			self.image_money_rect.x = -10000
			self.image_joueur_rect.centerx = -10000

	def money_lost(self, amount):
		self.money -= amount


# Class qui gère toutes les propriété des cartes
class Card(pygame.sprite.Sprite):
	def __init__(self, name, base_cost, one_house, two_house, three_house, fore_house, hotel, hypotheque, house_price,
				 Case_price, ownered, owner_name, type, tier, class_name):
		self.name = name
		self.ownered = ownered
		self.owner_name = owner_name
		self.class_name = class_name
		self.tier = tier
		if type == "house":
			self.image = pygame.image.load(file_name + f"/Carte/{self.name}.png").convert_alpha()
			self.image = pygame.transform.scale(self.image, (210, 340))
			self.rect = self.image.get_rect()
			self.price = Case_price
			if self.tier == 0:
				self.cost = base_cost
			elif self.tier == 1:
				self.cost = one_house
			elif self.tier == 2:
				self.cost = two_house
			elif self.tier == 3:
				self.cost = three_house
			elif self.tier == 4:
				self.cost = fore_house
			elif self.tier == 5:
				self.cost == hotel
		self.type = type

		if self.ownered:
			print("Acheter par ", self.owner_name)

	def zoom_IN(self):
		if self.type == "house":
			self.image = pygame.transform.scale(self.image, (420, 680))
			self.rect = self.image.get_rect()
			self.rect.centerx = 640
			self.rect.centery = 360

	def zomm_OUT(self):
		if type == "house":
			self.image = pygame.transform.scale(self.image, (210, 340))
			self.rect = self.image.get_rect()


# Class qui gère le menu entre chaque joueurs
class Screen_loading(pygame.sprite.Sprite):
	def __init__(self, joueur, numero):
		super().__init__()
		self.Joueur = joueur
		self.numero = numero
		self.image = pygame.image.load(
			f"img_commun/Joueur screen menu/Joueur_{self.Joueur}/Screen_Joueur_{self.Joueur + 1}1 ({self.numero}).jpg").convert_alpha()


# class qui gère les images du tuto
class img_tuto(pygame.sprite.Sprite):
	def __init__(self, image):
		self.link = image
		self.image = pygame.image.load(f"img_2/img/Element/Ingame/Tutoriel/{self.link}")
		self.rect = self.image.get_rect()
