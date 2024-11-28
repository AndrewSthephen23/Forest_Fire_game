class Level:
    def __init__(self, player, fires, power_ups, animals, refills):
        self.player = player
        self.fires = fires
        self.power_ups = power_ups
        self.animals = animals
        self.refills = refills

    def update(self, keys):
        # Lógica para interactuar con el fuego, rescatar animales, recargar agua, etc.
        pass

    def render(self, screen):
        # Dibujar todo en la pantalla
        pass
