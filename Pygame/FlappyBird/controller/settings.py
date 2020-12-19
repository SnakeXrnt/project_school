import pygame

class Settings:

	def __init__(self):

		#GAME BASIC SETTINGS
		self.base_dimension = 30

		self.screen_width = 9*self.base_dimension
		self.screen_height = 16*self.base_dimension

		self.title = "Flappy Bird Game"
		self.bg = pygame.image.load('img/bg.png')
		self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))


		#PIPE SETTINGS
		self.pipe_width = 50
		self.pipe_height = 200
		self.pipe_color = [60, 60, 60]

		self.pipe_head_width = 60
		self.pipe_head_height = 25

		#self.pipe_number = 0


		#PLATFORM SETTINGS
		self.platform_speed = 0.00000001

		self.bird_life = 3
