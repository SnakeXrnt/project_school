import pygame

from controller import settings
from models import platform
from models import bird,pipe

class FlappyBirdGame():

    def __init__(self):
        pygame.init()
        self.sett = settings.Settings()
        self.screen = pygame.display.set_mode([self.sett.screen_width,self.sett.screen_height])


        self.platfrm = platform.Platform(self)

        self.title = pygame.display.set_caption('Flappy Bird Game')
        self.bg_screen = self.sett.bg
        self.platfrm = platform.Platform(self)
        self.bird = bird.Bird(self)
        self.pipe = pipe.pipe(self)

        self.running = True

    def run_game(self):
        while self.running:
            self.rg_check_events()
            self.rg_update_screen()

    def rg_check_events(self):
        events = pygame.event.get()
        #print(events)

        for event in events :
            if event.type == pygame.QUIT:
                self.running = False

    def rg_update_screen(self):
        self.screen.blit(self.bg_screen,[0,0])
        self.platfrm.show_platform()
        self.bird.show_bird()
        #self.pipe.show_pipe()

    def create_pipe(self):
        pipe_top = pipe.Pipe(self)
        pipe_bottom = pipe.Pipe(self)

        self.game_pipes.add(pipe_top)
        se;f.game_pipes.add(pipe_bottom)

        pygame.display.flip()

game = FlappyBirdGame()
game.run_game()
