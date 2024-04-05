from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win

    def draw(self):
        if self.has_left_wall:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, "black")

        if self.has_top_wall:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, "black")

        if self.has_right_wall:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, "black")
            
        if self.has_bottom_wall:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, "black")