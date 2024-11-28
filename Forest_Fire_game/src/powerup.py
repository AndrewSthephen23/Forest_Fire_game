import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.type = type
        if self.type == "speed":
            self.image.fill((0, 0, 255))  # Azul para velocidad
        elif self.type == "water":
            self.image.fill((0, 255, 255))  # Cian para agua
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def apply(self, player):
        if self.type == "speed":
            # Aumentar la velocidad del jugador
            pass
        elif self.type == "water":
            # Recargar el agua al jugador
            player.water_supply = 100
