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

    c1 = Cell(50, 200, 50, 200, win)
    c1.has_bottom_wall = False
    c1.has_right_wall = False    
    c1.draw("black")

    c2 = Cell(125, 200, 125, 200, win)
    c2.has_bottom_wall = False
    c2.has_right_wall = False    
    c2.draw("black")

    c1.draw_move(c2)

    win.wait_for_close()


main()