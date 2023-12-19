import numpy as np

class random_starter:
    position = None
    velocity = None

    def start(dimensions):
        random_starter.position = np.random.randint(2, size=dimensions)
        random_starter.velocity = np.random.randint(2, size=dimensions)