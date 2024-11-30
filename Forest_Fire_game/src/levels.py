import pygame

class Level:
    def __init__(self, player, fires, power_ups, animals, refills):
        self.player = player
        self.fires = fires
        self.power_ups = power_ups
        self.animals = animals
        self.refills = refills

    def render_end_screen(self, screen):
        font = pygame.font.Font(None, 48)
        message = "¡Gracias por proteger el bosque!"
        text = font.render(message, True, (0, 128, 0))
        screen.blit(text, (200, 300))
