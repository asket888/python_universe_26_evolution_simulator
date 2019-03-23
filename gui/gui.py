import numpy as np
from termcolor import colored

from gui.make_gif import make_gif


def get_generation_stats(generation):
    stats = {'BEST': -100, 'WORST': 100, 'SURVIVED': 0, 'SUM': 0, 'COUNT': 0}
    for org in generation:
        if org.fitness > stats['BEST']:
            stats['BEST'] = org.fitness
        if org.fitness < stats['WORST']:
            stats['WORST'] = org.fitness
        if org.fitness > 0:
            stats['SURVIVED'] += 1
        stats['SUM'] += org.fitness
        stats['COUNT'] += 1

    stats['AVG'] = stats['SUM'] / stats['COUNT']

    return stats


def print_generation_stats(gen, stats):
    print(
        ' > GEN-' + str(gen + 1), ':',
        colored(('BEST:', np.round(stats['BEST'], 2)), 'green'),
        colored(('AVG:', np.round(stats['AVG'], 2)), 'blue'),
        colored(('WORST:', np.round(stats['WORST'], 2)), 'red'),
        colored(('SURVIVED:', stats['SURVIVED']), 'yellow')
    )


def build_generation_gif(settings, gen):
    print(' > GEN-' + str(gen + 1), '.gif file is building...\n')
    make_gif(settings, gen)
