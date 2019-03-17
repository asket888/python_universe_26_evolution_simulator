def settings():
    settings = {}

    # FILE DETAILS
    settings['name'] = 'universe_26'

    # EVOLUTION SETTINGS
    settings['gens'] = 100                     # number of generations
    settings['pop_size'] = 30                  # number of organisms
    settings['food_num'] = 15                  # number of food particles
    settings['elitism'] = 0.35                 # elitism (percent of population to keep and allow to have children)
    settings['mutate'] = 0.2                   # mutation rate

    # ORGANISM SETTINGS
    settings['org_vision_dist'] = 100          # organism vision distance
    settings['org_momentum'] = 0.12            # velocity decay factor, so the organisms have momentum
    settings['org_org_dist'] = 0.10            # other organism clumping penalty distance
    settings['org_org_penalty'] = 0.05         # other organism clumping penalty value

    # FOOD SETTINGS
    settings['food_eat_dist'] = 0.075          # food to be eaten distance
    settings['food_energy'] = 1                # food energy

    # SIMULATION SETTINGS
    settings['seed'] = 333                     # for reproducibility
    settings['ticks'] = 100                    # time steps in a generation
    settings['x_min'] = -3.0                   # arena western border
    settings['x_max'] = 3.0                    # arena eastern border
    settings['y_min'] = -3.0                   # arena southern border
    settings['y_max'] = 3.0                    # arena northern border

    # NEURAL NETWORK SETTINGS
    settings['inodes'] = 6                     # number of input nodes
    settings['hnodes'] = 5                     # number of hidden nodes
    settings['onodes'] = 2                     # number of output nodes

    # GIF
    settings['plot_gens'] = [0, 9, 99, 199]    # plot following generations (list(range(10, 100, 10)))
    settings['gif_fps'] = 12                   # frames per second
    settings['ts_in_gif'] = settings['ticks']  # gif duration

    return settings
