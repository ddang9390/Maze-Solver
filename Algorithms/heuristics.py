# Purpose - To provide functions for estimating cost to goal

def manhattan_dist(start, goal):
    """
    Calculates the distance between the start and goal cells

    Arguments:
        start (Cell): The starting cell
        goal (Cell): The goal cell

    Returns:
        int: The distance between the start and goal cells
    """
    return abs(start.placement[0] - goal.placement[0]) + abs(start.placement[1] - goal.placement[1])

