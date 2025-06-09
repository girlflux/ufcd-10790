class Settings:
    """Classe que define todas as definições do jogo"""
    def __init__(self):
        """Definições do ecra"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (54, 1, 63)
        self.ship_speed = 5

        """Definições das balas da nave"""
        self.bullet_speed = 6.0
        self.bullet_width = 6
        self.bullet_height = 17
        self.bullet_color = (255, 177, 77)

        """Definições das balas dos inimigos"""
        self.enemy_bullet_speed = 5.0
        self.enemy_bullet_radius = 6
        self.enemy_bullet_color = (255, 0, 0)