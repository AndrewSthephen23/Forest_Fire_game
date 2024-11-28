import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Tamaño del fuego
        self.image.fill((255, 0, 0))  # Rellenar de color rojo (fuego)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
