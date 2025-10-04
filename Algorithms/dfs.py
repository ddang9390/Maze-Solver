# Purpose - Solve the maze using the DFS algorithm

def solve_DFS(maze_solver, i=0, j=0):
    maze_solver.maze.animate()
    maze_solver.cells[i][j].visited = True

    if i == maze_solver.num_cols-1 and j == maze_solver.num_rows-1:
        return True
    
    #Vertical Movement
    if (j-1) > 0:
        if not maze_solver.cells[i][j-1].visited and not maze_solver.cells[i][j-1].has_bottom_wall:
            maze_solver.cells[i][j].draw_move(maze_solver.cells[i][j-1])
            if solve_DFS(maze_solver, i, j-1):
                return True
            else:
                maze_solver.cells[i][j].draw_move(maze_solver.cells[i][j-1], True)

    if (j+1) < maze_solver.num_cols:
        if not maze_solver.cells[i][j+1].visited and not maze_solver.cells[i][j+1].has_top_wall:
            maze_solver.cells[i][j].draw_move(maze_solver.cells[i][j+1])
            if solve_DFS(maze_solver, i, j+1):
                return True
            else:
                maze_solver.cells[i][j].draw_move(maze_solver.cells[i][j+1], True)

    #Horizontal Movement:
    if (i-1) > 0:
        if not maze_solver.cells[i-1][j].visited and not maze_solver.cells[i-1][j].has_right_wall:
            maze_solver.cells[i][j].draw_move(maze_solver.cells[i-1][j])
            if solve_DFS(maze_solver, i-1, j):
                return True
            else:
                maze_solver.cells[i][j].draw_move(maze_solver.cells[i-1][j], True)

    if (i+1) < maze_solver.num_cols:
        if not maze_solver.cells[i+1][j].visited and not maze_solver.cells[i+1][j].has_left_wall:
            maze_solver.cells[i][j].draw_move(maze_solver.cells[i+1][j])
            if solve_DFS(maze_solver, i+1, j):
                return True
            else:
                maze_solver.cells[i][j].draw_move(maze_solver.cells[i+1][j], True)

    return False