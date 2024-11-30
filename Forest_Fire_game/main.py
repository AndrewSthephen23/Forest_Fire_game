import pygame
from src.game import Game
from src.levels import Level

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Forest Firefighter - Save the Forest")

game = Game(screen)
level = Level(game.player, game.fires, game.power_ups, game.animals, game.refills)
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(30)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fondo blanco
    if game.is_running():
        game.handle_events(events)
        game.update()
        game.render()
    else:
        level.render_end_screen(screen)

    pygame.display.flip()

pygame.quit()
