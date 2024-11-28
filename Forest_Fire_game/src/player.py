import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Crear una superficie para el jugador
        self.image.fill((0, 255, 0))  # Rellenar la superficie con un color (verde)
        self.rect = self.image.get_rect()  # Obtener el rectángulo de la superficie
        self.rect.center = (400, 300)  # Ubicar al jugador en el centro de la pantalla
        self.water_supply = 100  # Suministro de agua inicial

    def move(self, keys):
        speed = 5  # Velocidad del jugador
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed

    def update(self):
        # Este método puede usarse para actualizar cualquier comportamiento del jugador,
        # pero principalmente para dibujarlo en la pantalla.
        pass

    def draw(self, screen):
        # Método para dibujar al jugador en la pantalla
        screen.blit(self.image, self.rect)
