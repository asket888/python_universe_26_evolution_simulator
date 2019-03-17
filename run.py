import warnings
import numpy as np

from settings import settings
from simulation import simulate_all_generations


SETTINGS = settings()
warnings.filterwarnings("ignore")


def run(settings):
    np.random.seed(settings['seed'])
    simulate_all_generations(settings)


if __name__ == '__main__':
    run(SETTINGS)
