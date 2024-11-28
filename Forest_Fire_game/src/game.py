import pygame
import random
from src.player import Player
from src.fire import Fire
from src.water_refill import WaterRefill
from src.animal import Animal
from src.levels import Level

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.fires = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.animals = pygame.sprite.Group()
        self.refills = pygame.sprite.Group()
        self.level = Level(self.player, self.fires, self.power_ups, self.animals, self.refills)

        # Crear algunos objetos para el juego (por ejemplo, fuegos)
        for _ in range(5):
            fire = Fire(x=random.randint(0, 760), y=random.randint(0, 560))  # Usamos random.randint
            self.fires.add(fire)
        
        # Agregar recargas de agua
        for _ in range(2):
            refill = WaterRefill(x=random.randint(0, 760), y=random.randint(0, 560))  # Usamos random.randint
            self.refills.add(refill)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Lógica de actualización de objetos
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        # Verificar si el jugador presiona la tecla espacio para extinguir fuego
        if keys[pygame.K_SPACE] and self.player.water_supply > 0:
            for fire in self.fires:
                if self.player.rect.colliderect(fire.rect):
                    self.fires.remove(fire)  # Apagar el fuego
                    self.player.water_supply -= 10  # Reducir agua
                    break  # Si apaga un fuego, no seguir verificando

        # Verificar colisión con puntos de recarga
        for refill in self.refills:
            if self.player.rect.colliderect(refill.rect):
                self.player.water_supply = 100  # Recargar agua al máximo
                self.refills.remove(refill)  # Eliminar el punto de recarga
                break  # Recargar agua solo una vez por colisión

    def render(self):
        # Dibujar todo en la pantalla
        self.screen.fill((255, 255, 255))  # Fondo blanco
        self.player.draw(self.screen)  # Dibujar al jugador
        self.fires.draw(self.screen)  # Dibujar todos los fuegos
        self.refills.draw(self.screen)  # Dibujar puntos de recarga
        self.animals.draw(self.screen)  # Dibujar animales si están

        # Mostrar el suministro de agua
        font = pygame.font.Font(None, 36)
        text = font.render(f"Agua: {self.player.water_supply}", True, (0, 0, 255))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()
