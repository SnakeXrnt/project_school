import pygame
from random import randint
#OUR OWN MODULE
from controller.settings import Settings
from controller.game_stats import GameStats

from models.platform import Platform
from models.pipe import Pipe
from models.bird import Bird

class FlappyBirdGame:

	def __init__(self):
		pygame.init()
		##############################################
		#OBJECT yang INVISIBLE behind the screen
		#############################################
		self.game_settings = Settings()
		self.game_stat = GameStats(self)

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		##############################################
		#SINGLE OBJECT/MODELS in OUR GAME (Object in Object)
		##############################################
		self.game_platform = Platform(self)
		self.game_bird = Bird(self)

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
			elif event.type == pygame.KEYDOWN:
				self.rg_e_check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self.rg_e_check_keyup_events(event)

	def rg_e_check_keydown_events(self, event):
		if event.key == pygame.K_SPACE:
			self.game_bird.is_fly = True
			self.update_pipes()

	def update_pipes(self):
 		self.show_pipes()





	def rg_e_check_keyup_events(self, event):
		if event.key == pygame.K_SPACE:
			self.game_bird.is_fly = False
			self.game_bird.is_fall = True

	def rg_update_screen(self):
		FPS = 180
		fpsClock = pygame.time.Clock()
		self.screen.blit(self.bg_screen, [0,0])
		self.update_bird()
		self.update_pipes()
		self.update_platform()
		pygame.display.flip()
		fpsClock.tick(FPS)

	######################
	#BIRD
	######################
	def bird_hit_pipe(self):
		if pygame.sprite.spritecollideany(self.game_bird,self.game_pipes):
			return True
		else :
			return False



	def bird_on_platform(self):
		if self.game_bird.image_rect.bottom >= self.game_platform.image_rect.top:
			return True
		else :
			return False

	def bird_on_top_edge(self):
		screen_rect = self.screen.get_rect()
		if self.game_bird.image_rect.top <= screen_rect.top:
			return True
		else :
			return False


	def update_bird(self):
		if self.bird_on_platform() == False and self.bird_on_top_edge() == False and self.bird_hit_pipe() == False:
			self.game_bird.move()

		self.game_bird.show_bird()


	######################
	#PLATFORM
	######################

	def update_platform(self):
		self.game_platform.show_platform()
		self.game_platform.move()


	######################
	#PIPE
	######################




	def check_pipes(self, pipe):
		if pipe.head.head_image.right <= 0:
			self.game_pipes.remove(pipe)
			#print(len(self.game_pipes))
			#print('removed')
		if len(self.game_pipes) == 0:
			self.create_pipes()



	def show_pipes(self):
		pipes = self.game_pipes.sprites()
		for pipe in pipes:
			self.check_pipes(pipe)
			pipe.show_pipe()
			pipe.move()


	def create_pipes(self):
		#self.game_settings.pipe_number += 1
		screen_rect = self.screen.get_rect()
		platform_rect = self.game_platform.image_rect
		gap = screen_rect.height//5

		pipe_top = Pipe(self)
		pipe_bottom = Pipe(self)

		#Atur ulang tinggi dari pipe_top
		random_height_pipe_top = randint(screen_rect.height//5 + 100, 4*screen_rect.height//5) - (platform_rect.height+50)
		pipe_top.pipe_image.height = random_height_pipe_top
		pipe_top.head.head_image.midbottom = pipe_top.pipe_image.midbottom

		#Atur ulang tinggi dari pipe_bottom
		pipe_bottom.pipe_image.height = screen_rect.height - pipe_top.pipe_image.height - gap

		pipe_bottom.pipe_image.bottomright = screen_rect.bottomright
		pipe_bottom.pipe_image.x += 50
		pipe_bottom.head.head_image.midtop = pipe_bottom.pipe_image.midtop

		self.game_pipes.add(pipe_top)
		self.game_pipes.add(pipe_bottom)


game = FlappyBirdGame()
game.run_game()
