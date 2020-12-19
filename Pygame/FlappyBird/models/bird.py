import pygame

class Bird:

	def __init__(self, FlappyBirdGame):
		self.settings = FlappyBirdGame.game_settings
		self.screen = FlappyBirdGame.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('img/bird.png')
		self.image_rect = self.image.get_rect()
		self.rect = self.image_rect

		self.re_transform_scale()

		self.image_rect.midleft = self.screen_rect.midleft
		self.image_rect.x += 50

		self.y = self.image_rect.y

		self.is_fly = False
		self.is_fall = False

	def re_transform_scale(self):
		self.image = pygame.transform.scale(self.image, (3*self.image_rect.width//4,3*self.image_rect.height//4))

	def fly(self):
		self.y -= 2
		self.image_rect.y = self.y

	def fall(self):
		self.y += 1
		self.image_rect.y = self.y

	def move(self):
		if self.is_fly:
			self.fly()
		if self.is_fall:
			self.fall()

	def show_bird(self):
		self.screen.blit(self.image, self.image_rect)
