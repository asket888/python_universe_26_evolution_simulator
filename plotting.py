from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import matplotlib.lines as lines

from functions.name_functions import frame_img_name_template, result_img_name_template


def plot_frame(settings, organisms, foods, gen, time):

    fig, ax = plt.subplots()
    fig.set_size_inches(9.6, 5.4)

    plt.xlim([settings['x_min'] + settings['x_min'] * 0.45, settings['x_max'] + settings['x_max'] * 0.45])
    plt.ylim([settings['y_min'] + settings['y_min'] * 0.45, settings['y_max'] + settings['y_max'] * 0.45])

    # plot organisms and food
    for organism in organisms:
        _plot_organism(organism, ax)

    for food in foods:
        _plot_food(food, ax)

    # misc plot settings
    ax.set_aspect('equal')
    frame = plt.gca()
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])

    plt.figtext(0.025, 0.95, r'GENERATION: '+str(gen))
    plt.figtext(0.025, 0.90, r'TICK: '+str(time))

    plt.savefig(frame_img_name_template(gen, time), dpi=120)


def plot_stats(settings, gen_stats):

    # get stats
    ng = len(gen_stats)
    gens = list(range(ng))
    bests = [gen_stats[i]['BEST'] for i in range(ng)]
    worsts = [gen_stats[i]['WORST'] for i in range(ng)]
    avgs = [gen_stats[i]['AVG'] for i in range(ng)]
    
    fig, ax = plt.subplots()

    ax.plot(gens, bests)
    ax.plot(gens, avgs)
    ax.plot(gens, worsts)

    ax.legend(['Best', 'Average', 'Worst'], loc='upper left')
    ax.set_xlabel('generation')
    ax.set_ylabel('fitness score')

    fig.savefig(result_img_name_template(settings), dpi=200)


def _plot_food(food, ax):

    circle = Circle([food.x, food.y], 0.03, edgecolor='darkslateblue', facecolor='mediumslateblue', zorder=5)
    ax.add_artist(circle)


def _plot_organism(org, ax):

    circle = Circle([org.x, org.y], 0.05, edgecolor='green', facecolor='lightgreen', zorder=8)
    ax.add_artist(circle)

    ax.add_line(lines.Line2D([org.x, org.x_tail], [org.y, org.y_tail], color='darkgreen', linewidth=1, zorder=10))
