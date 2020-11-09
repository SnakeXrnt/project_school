import pygame
class Platform():


    def __init__(self, FlappyBirdGame):
        self.screen = FlappyBirdGame.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('img/land.png')
        self.image_rect = self.image.get_rect()
        self.re_transform_width()

        self.image_rect.midbottom = self.screen_rect.midbottom

    def re_transform_width(self):
        self.image = pygame.transform.scale(self.image , (self.screen_rect.width, self.image_rect.height) )
        self.image_rect = self.image.get_rect()


    def show_platform(self):
        self.screen.blit(self.image,self.image_rect)
