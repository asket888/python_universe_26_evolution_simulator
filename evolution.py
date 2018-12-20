import operator

from numpy import floor

from numpy.random import randint
from numpy.random import random
from numpy.random import choice
from numpy.random import uniform

from functions.name_functions import next_gen_org_name_template
from objects.organism import Organism


def evolve(settings, old_generation, gen):
    ancestors_num = int(floor(settings['elitism'] * settings['pop_size']))
    descendants_num = settings['pop_size'] - ancestors_num

    new_generation = _calculate_new_generation(settings, gen, old_generation, ancestors_num, descendants_num)

    return new_generation


def _calculate_new_generation(settings, gen, old_generation, ancestors_num, descendants_num):
    sorted_old_generation = sorted(old_generation, key=operator.attrgetter('fitness'), reverse=True)

    # keep best organisms from previous generation
    new_generation = []
    for org in range(0, ancestors_num):
        best_candidate = sorted_old_generation[org]
        new_generation.append(Organism(settings,
                                       wih=best_candidate.wih,
                                       who=best_candidate.who,
                                       name=best_candidate.name))

    # generate children of best organisms from previous generation
    for org in range(0, descendants_num):
        all_parents_candidates = range(0, ancestors_num)
        random_parents_indexes = choice(a=all_parents_candidates, size=2, replace=False)
        org_1 = sorted_old_generation[random_parents_indexes[0]]
        org_2 = sorted_old_generation[random_parents_indexes[1]]

        wih_new, who_new = _calculate_child_mutations(settings, org_1, org_2)

        new_generation.append(Organism(settings,
                                       wih=wih_new,
                                       who=who_new,
                                       name=next_gen_org_name_template(gen, org)))

    return new_generation


def _calculate_child_mutations(settings, org_1, org_2):
    # crossover
    crossover_weight = random()
    wih_new = (crossover_weight * org_1.wih) + ((1 - crossover_weight) * org_2.wih)
    who_new = (crossover_weight * org_1.who) + ((1 - crossover_weight) * org_2.who)

    # mutation
    mutate = random()
    if mutate <= settings['mutate']:

        # pick which weight matrix to mutate
        mat_pick = randint(0, 2)

        # mutate: wih weights
        if mat_pick == 0:
            index_row = randint(0, settings['hnodes'])
            index_col = randint(0, settings['inodes'])
            wih_new[index_row][index_col] = wih_new[index_row][index_col] * uniform(0.9, 1.1)

        # mutate: who weights
        if mat_pick == 1:
            index_row = randint(0, settings['onodes'])
            index_col = randint(0, settings['hnodes'])
            who_new[index_row][index_col] = who_new[index_row][index_col] * uniform(0.9, 1.1)

    return wih_new, who_new
