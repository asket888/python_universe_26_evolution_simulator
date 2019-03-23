from numpy.random import uniform


class Food:

    def __init__(self, settings):
        self.x = uniform(settings['x_min'] - 1, settings['x_max'] + 1)
        self.y = uniform(settings['y_min'] - 1, settings['y_max'] + 1)
        self.energy = settings['food_energy']

    def respawn(self, settings):
        if self.energy == 0:
            self.x = uniform(settings['x_min'] - 1, settings['x_max'] + 1)
            self.y = uniform(settings['y_min'] - 1, settings['y_max'] + 1)
            self.energy = settings['food_energy']
