import pygame
from pygame.sprite import Sprite

class Head:

	def __init__(self, width, height):

		self.head_image = pygame.Rect(0,0, width, height)

class Pipe(Sprite):

	def __init__(self, FlappyBirdGame):
		super().__init__()
		
		self.screen = FlappyBirdGame.screen
		self.game_settings = FlappyBirdGame.game_settings

		self.screen_rect = self.screen.get_rect()

		self.pipe_image = pygame.Rect(0,0,self.game_settings.pipe_width,self.game_settings.pipe_height)

		self.pipe_image.topright = self.screen_rect.topright
		self.pipe_image.x -= 50


		#Memasukkan Kepala Pipa
		self.head = Head(self.game_settings.pipe_head_width, self.game_settings.pipe_head_height)
		self.head.head_image.midbottom = self.pipe_image.midbottom

	def show_pipe(self):
		pygame.draw.rect(self.screen, self.game_settings.pipe_color, self.pipe_image)
		pygame.draw.rect(self.screen, self.game_settings.pipe_color, self.head.head_image)