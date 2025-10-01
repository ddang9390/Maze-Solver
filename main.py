from graphics import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
from maze_solver import MazeSolver

# Constants
CELL_SIZE_X = 30
CELL_SIZE_Y = 30
MARGIN = 30

def main():
    #TODO - allow for num of rows not equaling num of cols, allow for user input
    num_rows = 5
    num_cols = 5

    screen_x = (2 * CELL_SIZE_X) * num_rows
    screen_y = (1.5 * CELL_SIZE_Y) * num_cols
    win = Window(screen_x, screen_y)

    # Create maze
    maze = Maze(MARGIN, MARGIN, num_rows, num_cols, CELL_SIZE_X, CELL_SIZE_Y, win)
    maze.break_entrance_and_exit()
    maze.break_walls(0, 0)
    maze.reset_cells_visited()
    win.maze = maze

    # Solve maze
    maze_solver = MazeSolver(maze)
    maze_solver.solve()
    
    win.wait_for_close()


main()