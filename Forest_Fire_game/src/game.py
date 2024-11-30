import pygame
import random
from src.player import Player
from src.fire import Fire
from src.water_refill import WaterRefill
from src.animal import Animal
from src.powerup import PowerUp

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.fires = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.animals = pygame.sprite.Group()
        self.refills = pygame.sprite.Group()

        # Crear objetos iniciales
        for _ in range(5):
            fire = Fire(x=random.randint(0, 760), y=random.randint(0, 560))
            self.fires.add(fire)

        for _ in range(2):
            refill = WaterRefill(x=random.randint(0, 760), y=random.randint(0, 560))
            self.refills.add(refill)

    def is_running(self):
        return self.running

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        # Extinguir fuegos
        if keys[pygame.K_SPACE] and self.player.water_supply > 0:
            for fire in self.fires:
                if self.player.rect.colliderect(fire.rect):
                    self.fires.remove(fire)
                    self.player.water_supply -= 10
                    break

        # Recargar agua
        for refill in self.refills:
            if self.player.rect.colliderect(refill.rect):
                self.player.water_supply = 100
                self.refills.remove(refill)
                break

    def render(self):
        self.player.draw(self.screen)
        self.fires.draw(self.screen)
        self.refills.draw(self.screen)

        # Mostrar suministro de agua
        font = pygame.font.Font(None, 36)
        text = font.render(f"Agua: {self.player.water_supply}", True, (0, 0, 255))
        self.screen.blit(text, (10, 10))
