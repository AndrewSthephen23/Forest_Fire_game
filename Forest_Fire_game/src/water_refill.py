import pygame

class WaterRefill(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Tamaño de la recarga
        self.image.fill((0, 0, 255))  # Rellenar de color azul (agua)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
