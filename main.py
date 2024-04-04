from graphics import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    

    p1 = Point(100, 100)
    p2 = Point(200, 100)

    l1 = Line(p1, p2)
    l1.draw(win.canvas, "red")

    win.wait_for_close()


main()