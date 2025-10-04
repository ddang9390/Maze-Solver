from graphics import Window
from maze import Maze

# Constants
NUM_ROWS = 8
NUM_COLS = 8
CELL_SIZE_X = 30
CELL_SIZE_Y = 30
MARGIN = 30

def main():
    """
    Sets up the application and runs the main function
    """
    # Calculates dimensions of the screen
    screen_x = (2 * CELL_SIZE_X) * NUM_ROWS
    screen_y = (1.5 * CELL_SIZE_Y) * NUM_COLS
    win = Window(screen_x, screen_y)

    # Create maze
    maze = Maze(MARGIN, MARGIN, NUM_ROWS, NUM_COLS, CELL_SIZE_X, CELL_SIZE_Y, win)
    maze.break_entrance_and_exit()
    maze.break_walls(0, 0)
    maze.reset_cells_visited()
    win.maze = maze
    
    win.wait_for_close()

if __name__ == "__main__":
    main()