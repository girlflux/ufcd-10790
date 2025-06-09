import sys
import pygame
import random

from settings import Settings
from ship import Ship
from bullet import Bullet
from inimigo import Inimigo
from bullet_inimigo import BulletInimigo

class Invasao:
    """Classe que controla todos os elementos e comportamentos do jogo"""

    def __init__(self):
        """Iniciar o jogo e criar os recursos do jogo"""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invasão Espacial")

        self.background = pygame.image.load('images/bg.gif')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()
        self._create_fleet()
        self.bullets_inimigo = pygame.sprite.Group()
        self.inimigo_disparo_timer = 0

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet(self):
        inimigo = Inimigo(self)
        inimigo_width = inimigo.rect.width

        current_x = inimigo_width
        while current_x < (self.settings.screen_width - 2 * inimigo_width):
            novo_inimigo = Inimigo(self)
            novo_inimigo.x = current_x
            novo_inimigo.rect.x = current_x
            self.inimigos.add(novo_inimigo)
            current_x += 2 * inimigo_width

    def _inimigos_disparam(self):
        inimigos_lista = list(self.inimigos.sprites())

        # Disparar de 1 a 3 inimigos aleatórios (ou menos, se houver poucos)
        num_disparos = random.randint(1, min(5, len(inimigos_lista)))
        inimigos_que_disparam = random.sample(inimigos_lista, num_disparos)

        for inimigo in inimigos_que_disparam:
            nova_bala = BulletInimigo(self, inimigo)
            self.bullets_inimigo.add(nova_bala)


    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()            

            self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.background, (0, 0))
            self.ship.update()
            self.ship.blitime()
            self.inimigos.draw(self.screen)
            self.bullets.update()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))

            self.inimigo_disparo_timer += 1
            if self.inimigo_disparo_timer >= 45:  # A cada 1.5 segundos
                self._inimigos_disparam()
                self.inimigo_disparo_timer = 0
            
            self.bullets_inimigo.update()
            for bala in self.bullets_inimigo.sprites():
                bala.draw_bullet()

            for bala in self.bullets_inimigo.copy():
                if bala.rect.top >= self.settings.screen_height:
                    self.bullets_inimigo.remove(bala)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    """Inicia uma instancia da classe e corre o jogo"""
    invasao = Invasao()
    invasao.run_game()