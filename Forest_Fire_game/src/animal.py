import pygame

class Animal(pygame.sprite.Sprite):
    def __init__(self, x, y, key_combination):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 255, 0))  # Amarillo para los animales
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.key_combination = key_combination  # Combinación de teclas

    def rescue(self, keys):
        if all(keys[pygame.key.key_code(k)] for k in self.key_combination):
            self.kill()  # Rescatado
            return True
        return False
