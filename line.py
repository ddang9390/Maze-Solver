# Purpose - The lines that would be drawn on the canvas

from point import Point
from tkinter import Tk, BOTH, Canvas

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )
        canvas.pack()