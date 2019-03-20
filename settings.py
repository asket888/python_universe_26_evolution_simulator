def settings():
    settings = {}

    # FILE DETAILS
    settings['name'] = 'universe_26'
    settings['gens'] = 50                     # number of generations

    # POPULATION SETTINGS
    settings['org_num'] = 30                   # number of organisms
    settings['food_num'] = 15                  # number of food particles
    settings['pred_num'] = 3                   # number of predator particles

    # ORGANISM SETTINGS
    settings['org_start_fitness'] = 5          # organism start energy
    settings['org_max_velocity'] = 1.0         # organism maximum speed
    settings['org_vision_dist'] = 10           # organism vision distance
    settings['org_momentum'] = 0.50            # velocity decay factor, so the organisms have momentum
    settings['org_eat_dist'] = 0.75            # food to be eaten distance
    settings['org_org_dist'] = 0.10            # other organism clumping penalty distance
    settings['org_org_penalty'] = 0.05         # other organism clumping penalty value

    # FOOD SETTINGS
    settings['food_create'] = True             # option to seed food to pool
    settings['food_energy'] = 1                # food energy

    # POISON SETTINGS
    settings['poison_create'] = False          # option to seed poison to pool
    settings['poison_energy'] = 1              # poison energy

    # PREDATOR SETTINGS
    settings['pred_create'] = True            # option to seed predator to pool
    settings['pred_start_fitness'] = 7         # predator start energy
    settings['pred_max_velocity'] = 0.5        # organism maximum speed
    settings['pred_vision_dist'] = 10          # organism vision distance
    settings['pred_momentum'] = 0.80           # velocity decay factor, so the organisms have momentum
    settings['pred_eat_dist'] = 0.10           # organism to be eaten distance

    # EVOLUTION SETTINGS
    settings['elitism_org'] = 0.30             # elitism (percent of population to keep and allow to have children)
    settings['elitism_pred'] = 0.50            # elitism (percent of population to keep and allow to have children)
    settings['mutate'] = 0.2                   # mutation rate

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
    settings['plot_gens'] = [0, 9, 49, 199]  # plot following generations (list(range(10, 100, 10)))
    settings['gif_fps'] = 12                   # frames per second
    settings['ts_in_gif'] = settings['ticks']  # gif duration

    return settings
