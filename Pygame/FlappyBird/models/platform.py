import pygame

class Platform:

	def __init__(self, FlappyBirdGame):
		self.settings = FlappyBirdGame.game_settings

		self.screen = FlappyBirdGame.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("img/land.png")
		self.image_rect = self.image.get_rect()
		self.re_transform_width()
		
		self.image_rect.midbottom = self.screen_rect.midbottom

		self.x = self.image_rect.x

		
	def re_transform_width(self):
		self.image = pygame.transform.scale(self.image, (2*self.screen_rect.width, self.image_rect.height))
		self.image_rect = self.image.get_rect()

	def re_position(self):
		self.image_rect.left = 0
		self.x = self.image_rect.left

	def move(self):
		if self.image_rect.right <= self.screen_rect.right:
			self.re_position()
		self.x -= self.settings.platform_speed
		self.image_rect.x = self.x

	def show_platform(self):
		self.screen.blit(self.image, self.image_rect)