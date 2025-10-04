# Purpose - To provide functions for estimating cost to goal

def manhattan_dist(start, goal):
    return abs(start.placement[0] - goal.placement[0]) + abs(start.placement[1] - goal.placement[1])

