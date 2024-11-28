import pygame
from src.player import Player
from src.fire import Fire
from src.powerup import PowerUp
from src.animal import Animal
from src.water_refill import WaterRefill
from src.levels import Level
#from src.utils import load_assets

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
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        # Lógica de fuego, animales, recarga de agua
        self.level.update(keys)

    def render(self):
        self.screen.fill((255, 255, 255))  # Fondo blanco
        self.level.render(self.screen)
        pygame.display.flip()
