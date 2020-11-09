import pygame

class Settings():

    def __init__(self):

        self.base_dimension = 30
        self.screen_width = self.base_dimension*9
        self.screen_height = self.base_dimension*16

        self.title = 'FlappyBirdGame'
        self.bg = pygame.image.load('img/bg.png')

        self.bg_screen = pygame.transform.scale(self.bg,(self.screen_width,self.screen_height))

        
