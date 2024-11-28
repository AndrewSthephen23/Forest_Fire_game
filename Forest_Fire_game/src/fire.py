import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Rojo para fuego
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def extinguish(self):
        self.kill()  # El fuego es apagado
