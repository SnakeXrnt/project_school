####################################
#            ASSET BIRD            #
####################################

import pygame

class Bird:

    def __init__(self, FlappyBirdGame):
        self.screen = FlappyBirdGame.screen
        self.screen_rect = self.screen.get_rect()

        self.bird = pygame.image.load('img/bird.png')
        self.bird_rect = self.bird.get_rect()

        self.bird_rect.midleft = self.screen_rect.midleft
        self.bird_rect.x = self.screen_rect.width//8
        print(self.bird_rect)

        self.is_fly = False
        self.is_fall = False
    def re_transform_clace(self):
        self.image = pygame.transform.scale(self.image,(3*self.image_rect.width//4,3*self.image_rect.height//4))

    def fly(self):
        pass

    def fall(self):
        pass

    def show_bird(self):
        self.screen.blit(self.bird, self.bird_rect)
