from graphics import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    

    p1 = Point(100, 100)
    p2 = Point(200, 100)

    l1 = Line(p1, p2)
    #win.draw_line(l1, "black")

    c = Cell(100, 200, 100, 200, win)
    c.draw()

    win.wait_for_close()


main()