from graphics import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
from maze_solver import MazeSolver

def main():
    #TODO - allow for num of rows not equaling num of cols
    num_rows = 10
    num_cols = 10
    margin = 30
    
    cell_size_x = 30
    cell_size_y = 30

    screen_x = (1.5 * cell_size_x) * num_rows
    screen_y = (1.5 * cell_size_y) * num_cols
    win = Window(screen_x, screen_y)

    # Create maze
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.break_entrance_and_exit()
    maze.break_walls(0, 0)
    maze.reset_cells_visited()

    # Solve maze
    maze_solver = MazeSolver(maze)
    maze_solver.solve()
    
    win.wait_for_close()


main()