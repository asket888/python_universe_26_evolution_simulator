from numpy.random import uniform


class Food():

    def __init__(self, settings):
        self.x = uniform(settings['x_min'], settings['x_max'])
        self.y = uniform(settings['y_min'], settings['y_max'])
        self.energy = settings['food_energy']

    def respawn(self, settings):
        if self.energy == 0:
            self.x = uniform(settings['x_min'], settings['x_max'])
            self.y = uniform(settings['y_min'], settings['y_max'])
            self.energy = settings['food_energy']
