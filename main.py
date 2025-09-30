from graphics import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
from maze_solver import MazeSolver

def main():
    #TODO - allow for num of rows not equaling num of cols
    num_rows = 6
    num_cols = 6
    margin = 30
    
    cell_size_x = 30
    cell_size_y = 30

    #TODO - fix screen size, seems to do nothing
    screen_x = 10
    screen_y = 1000
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