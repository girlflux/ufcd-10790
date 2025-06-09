import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Esta classe vai gerir as balas disparadas da nave"""
    def __init__(self, jogo_invasao):
        """Criar objeto bullet a partir da posição onde a nave se encontra"""
        super().__init__()
        self.screen = jogo_invasao.screen
        self.settings = jogo_invasao.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = jogo_invasao.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect)