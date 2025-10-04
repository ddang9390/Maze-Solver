# Purpose - Solve the maze using the A* algorithm

from Algorithms.heuristics import *

def solve_astar(maze_solver):
    maze_solver.maze.animate()
    queue = []

    start = maze_solver.cells[0][0]
    goal = maze_solver.cells[maze_solver.num_cols-1][maze_solver.num_rows-1]

    queue.append(start)
    start.visited = True
    g_score = {start: 0}
    h_score = {start: manhattan_dist(start, goal)}
    path = None
    while queue:
        current_cell = min(queue, key=lambda item: item.f)
        
        x, y = current_cell.placement[0], current_cell.placement[1]
        if x == maze_solver.num_cols-1 and y == maze_solver.num_rows-1:
            path = current_cell
            break
        
        queue.remove(current_cell)
        current_cell.visited = True

        # Gather neighbors
        neighbors = []
        if not current_cell.has_left_wall and x - 1 >= 0:
            if not maze_solver.cells[x-1][y].visited:
                neighbors.append(maze_solver.cells[x-1][y])

        if not current_cell.has_right_wall and x + 1 < maze_solver.num_cols:
            if not maze_solver.cells[x+1][y].visited:
                neighbors.append(maze_solver.cells[x+1][y])

        if not current_cell.has_top_wall and y - 1 >= 0:
            if not maze_solver.cells[x][y-1].visited:
                neighbors.append(maze_solver.cells[x][y-1])

        if not current_cell.has_bottom_wall and y + 1 < maze_solver.num_rows:
            if not maze_solver.cells[x][y+1].visited:
                neighbors.append(maze_solver.cells[x][y+1])

        for neighbor in neighbors:
            if neighbor.visited:
                continue

            # Estimated cost from current location to goal
            h_val = manhattan_dist(neighbor, goal)

            tentative_g = g_score[current_cell] + 1
            if neighbor not in queue:
                queue.append(neighbor)
            elif tentative_g >= g_score[neighbor]:
                continue
            
            neighbor.parent = current_cell
            g_score[neighbor] = tentative_g
            h_score[neighbor] = h_val
            neighbor.f = g_score[neighbor] + h_score[neighbor]

    true_path = []
    while path is not None:
        true_path.append(path)
        path = path.parent

    true_path.reverse()
    for n in range(0, len(true_path)):
        if n+1 < len(true_path):
            true_path[n].draw_move(true_path[n+1])
            maze_solver.maze.animate()