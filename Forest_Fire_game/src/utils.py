import pygame

def load_image(filename):
    return pygame.image.load(filename).convert_alpha()
