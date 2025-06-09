import pygame

class Ship:
    """Classe para gerir a nave"""

    def __init__(self, jogo_invasao):
        """Incializa a nave numa determinada posição"""
        self.screen = jogo_invasao.screen
        self.settings = jogo_invasao.settings
        self.screen_rect = jogo_invasao.screen.get_rect()


        # Carregar a imagem da nave
        self.image = pygame.image.load('images/DurrrSpaceShip.png')
        self.rect = self.image.get_rect()

        # Iniciar a nave no centro e embaixo da janela do jogo
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitime(self):
        """Desenha a nave na sua localização atual"""
        self.screen.blit(self.image, self.rect)

    def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed

            self.rect.x = self.x