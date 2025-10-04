# Purpose - Solve the maze using the BFS algorithm

def solve_BFS(maze_solver):
    """
    Solves the maze using the BFS algorithm

    Arguments:
        maze_solver (MazeSolver) - Program that will be using the function to solve the maze

    Returns:
        bool: True if solution was found, False if not
    """
    maze_solver.maze.animate()

    start = maze_solver.cells[0][0]
    queue = []
    queue.append(start)
    start.visited = True

    while queue:
        current_cell = queue.pop(0)
        current_cell.visited = True
        x, y = current_cell.placement[0], current_cell.placement[1]
        if x == maze_solver.num_cols-1 and y == maze_solver.num_rows-1:
            return True
        
        if not current_cell.has_left_wall and x - 1 >= 0:
            left_move = maze_solver.cells[x-1][y]
            if not left_move.visited:
                queue.append(left_move)
                current_cell.draw_move(left_move)       

        if not current_cell.has_right_wall and x + 1 < maze_solver.num_cols:
            right_move = maze_solver.cells[x+1][y]
            if not right_move.visited:
                queue.append(right_move)
                current_cell.draw_move(right_move)
            

        if not current_cell.has_top_wall and y - 1 >= 0:
            up_move = maze_solver.cells[x][y-1]
            if not up_move.visited:
                queue.append(up_move)
                current_cell.draw_move(up_move)

        if not current_cell.has_bottom_wall and y + 1 < maze_solver.num_rows:
            down_move = maze_solver.cells[x][y+1]
            if not down_move.visited:
                queue.append(down_move)
                current_cell.draw_move(down_move)

        maze_solver.maze.animate()

    return False