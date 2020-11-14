import pygame

class Bird:

    def __init__(self, FlappyBirdGame):

        self.screen = FlappyBirdGame.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("img/bird.png")
        self.image_rect = self.image.get_rect()

        self.image_rect.midleft = self.screen_rect.midleft

    def show_bird(self):

        self.screen.blit(self.image, self.image_rect)
