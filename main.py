from graphics import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    num_rows = 6
    num_cols = 6
    margin = 25
    screen_x = 800
    screen_y = 600
    cell_size_x = 50
    cell_size_y = 50
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)


    win.wait_for_close()


main()