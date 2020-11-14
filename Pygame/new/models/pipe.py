import pygame

class Head:

    def __init__(self):

        self.head_image=pygame.Rect(0,0, 60 , 25)

class pipe(Sprite):
    super.__init__()

    def __init__(self,FlappyBirdGame):
        self.screen = FlappyBirdGame.screen
        self.screen_rect = self.screen.get_rect()

        self.pipe_image = pygame.Rect(0,0,50,200)

        self.pipe_image.topright = self.screen_rect.topright
        self.pipe_image.x -= 50

        #memasukkan kepala pipe_imag
        self.head = Head()
        self.head.head_image.midbottom = self.pipe_image.midbottom

    def show_pipe(self):
        pygame.draw.rect(self.screen,[60,60,60],self.pipe_image)
        pygame.draw.rect(self.screen,[60,60,60],self.head.head_image)
