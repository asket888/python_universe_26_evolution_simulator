import numpy as np


class Predator:
    def __init__(self, settings, wih=None, who=None, name=None):

        self.fitness = settings['pred_start_fitness']  # fitness (organism energy)

        self.max_velocity = settings['pred_max_velocity']
        self.velocity_decay_factor = settings['pred_momentum']

        self.x_max = settings['x_max'] + 1
        self.x_min = settings['x_min'] - 1
        self.y_max = settings['y_max'] + 1
        self.y_min = settings['y_min'] - 1

        self.x = np.random.uniform(settings['x_min'], settings['x_max'])
        self.y = np.random.uniform(settings['y_min'], settings['y_max'])

        self.x_tail = self.x
        self.y_tail = self.y

        self.x_velocity = 0  # velocity in the x direction
        self.y_velocity = 0  # velocity in the y direction

        self.x_distance_to_food = 0  #
        self.y_distance_to_food = 0  #

        self.x_distance_to_neighbour = 0  #
        self.y_distance_to_neighbour = 0  #

        self.wih = wih  # weights from input to hidden layer
        self.who = who  # weights from hidden layer to output

        self.name = name

    # NEURAL NETWORK
    def think(self):

        # SIMPLE MLP
        def af(x):
            return np.tanh(x)

        inputs = [
            self.x_velocity,
            self.y_velocity,
            self.x_distance_to_food,
            self.y_distance_to_food,
            self.x_distance_to_neighbour,
            self.y_distance_to_neighbour
        ]
        h1 = af(np.dot(self.wih, inputs))  # hidden layer
        out = np.multiply(af(np.dot(self.who, h1)), 0.5)  # output layer

        # UPDATE TAIL
        self.x_tail = self.x
        self.y_tail = self.y

        # UPDATE VELOCITIES
        self.x_velocity = float(out[0]) + self.x_velocity * self.velocity_decay_factor
        if abs(self.x_velocity) > self.max_velocity:
            self.x_velocity = self.max_velocity

        self.y_velocity = float(out[1]) + self.y_velocity * self.velocity_decay_factor
        if abs(self.y_velocity) > self.max_velocity:
            self.y_velocity = self.max_velocity

        # UPDATE POSITION
        self.x += self.x_velocity
        if abs(self.x) > self.x_max:
            if self.x > 0:
                self.x = self.x_max
            else:
                self.x = self.x_min

        self.y += self.y_velocity
        if abs(self.y) > self.y_max:
            if self.y > 0:
                self.y = self.y_max
            else:
                self.y = self.y_min
