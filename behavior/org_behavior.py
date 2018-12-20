from functions import maths_functions


def behave_on_food(closest_dist, eat_dist, org1, food):
    # get the closest food
    food_org_dist = maths_functions.dist_to_food(org1, food)
    if food_org_dist < closest_dist:
        closest_dist = food_org_dist
        org1.x_distance_to_food, org1.y_distance_to_food = maths_functions.xy_dist_to_food(org1, food)

    # update organism fitness function and food status
    if food_org_dist <= eat_dist:
        org1.fitness += food.energy
        food.energy = 0

    return closest_dist


def behave_on_other_organism(closest_dist, penalty_dist, penalty_value, org1, org2):
    # get the closest neighbour
    if org1 is org2:
        pass
    org_org_dist = maths_functions.dist_to_neighbour(org1, org2)
    if org_org_dist < closest_dist:
        closest_dist = org_org_dist
        org1.x_distance_to_neighbour, org1.y_distance_to_neighbour = maths_functions.xy_dist_to_neighbour(org1, org2)

    # update organism fitness function
    if org_org_dist <= penalty_dist:
        org1.fitness -= penalty_value

    return closest_dist
