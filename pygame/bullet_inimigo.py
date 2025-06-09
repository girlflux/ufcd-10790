import pygame
from pygame.sprite import Sprite

class BulletInimigo(Sprite):
    """Classe para gerir as balas disparadas pelos inimigos"""
    def __init__(self, jogo_invasao, inimigo):
        super().__init__()
        self.screen = jogo_invasao.screen
        self.settings = jogo_invasao.settings

        self.radius = self.settings.enemy_bullet_radius
        self.color = self.settings.enemy_bullet_color

        self.x = inimigo.rect.centerx
        self.y = inimigo.rect.bottom

        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius * 2, self.radius * 2)

    def update(self):
        self.y += self.settings.enemy_bullet_speed
        self.rect.centery = self.y

    def draw_bullet(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.radius)
