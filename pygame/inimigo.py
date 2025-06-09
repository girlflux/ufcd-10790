import pygame
from pygame.sprite import Sprite

class Inimigo(Sprite):
    def __init__(self, jogo_invasao):
        super().__init__()
        self.screen = jogo_invasao.screen

        self.image = pygame.image.load('images/inimigo.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def update(self):
        # adicionar futuramente movimento
        pass