from graphics import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    num_rows = 6
    num_cols = 6
    margin = 30
    screen_x = 800
    screen_y = 600
    cell_size_x = 30
    cell_size_y = 30
    win = Window(screen_x, screen_y)
    # line = Line(Point(50, 50), Point(100, 50))
    # win.draw_line(line, "black")

    # c1 = Cell(win, 50, 100, 50, 100)  
    # c1.draw("black")
    # c2 = Cell(win, 50, 100, 50, 150)  
    # c2.draw("black")
    #(50,50), (100, 0)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()

    #for x in range(0, maze.num_rows):
    #    for y in range(0, maze.num_cols):
    maze._break_walls(0, 0)
    maze.reset_cells_visited()
    
    win.wait_for_close()


main()