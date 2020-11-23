import pygame
from random import randint
#OUR OWN MODULE
from controller.settings import Settings

from models.platform import Platform
from models.pipe import Pipe

class FlappyBirdGame:

	def __init__(self):
		pygame.init()
		##############################################
		#OBJECT yang INVISIBLE behind the screen
		#############################################
		self.game_settings = Settings()

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		##############################################
		#SINGLE OBJECT/MODELS in OUR GAME (Object in Object)
		##############################################
		self.game_platform = Platform(self)

		##############################################
		#GROUP OBJECT/MODELS in OUR GAME (Object in Object)
		##############################################
		self.game_pipes = pygame.sprite.Group()
		self.create_pipes()


		self.title = pygame.display.set_caption(self.game_settings.title)
		self.bg_screen = self.game_settings.bg


		self.running = True

	######################
	#PROPERTY GAME UTAMA
	######################

	def run_game(self):
		while self.running:
			self.rg_check_events()
			self.rg_update_screen()

	def rg_check_events(self):
		events = pygame.event.get()
		#print(events)

		for event in events:
			if event.type == pygame.QUIT:
				self.running = False

	def rg_update_screen(self):
		self.screen.blit(self.bg_screen, [0,0])
		self.game_platform.show_platform()
		self.show_pipes()
		#self.game_pipe.show_pipe()
		pygame.display.flip()

	######################
	#PIPE
	######################
	def show_pipes(self):
		pipes = self.game_pipes.sprites()
		for pipe in pipes:
			pipe.show_pipe()

	def create_pipes(self):
		screen_rect = self.screen.get_rect()
		platform_rect = self.game_platform.image_rect
		gap = screen_rect.height//5

		pipe_top = Pipe(self)
		pipe_bottom = Pipe(self)

		#Atur ulang tinggi dari pipe_top
		random_height_pipe_top = randint(screen_rect.height//5 + 100, 4*screen_rect.height//5) - platform_rect.height
		pipe_top.pipe_image.height = random_height_pipe_top
		pipe_top.head.head_image.midbottom = pipe_top.pipe_image.midbottom

		#Atur ulang tinggi dari pipe_bottom
		pipe_bottom.pipe_image.height = screen_rect.height - pipe_top.pipe_image.height - gap

		pipe_bottom.pipe_image.bottomright = screen_rect.bottomright
		pipe_bottom.pipe_image.x -= 50
		pipe_bottom.head.head_image.midtop = pipe_bottom.pipe_image.midtop

		self.game_pipes.add(pipe_top)
		self.game_pipes.add(pipe_bottom)



game = FlappyBirdGame()
game.run_game()
