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

    def draw(self, color="black"):
        if self.has_left_wall:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, color)

        if self.has_top_wall:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, color)

        if self.has_right_wall:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, color)
            
        if self.has_bottom_wall:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, color)

    def draw_move(self, to_cell, undo=False):
        if not undo:
            color = "red"
        else:
            color = "gray"

        center_x = (self.x2 + self.x1) / 2
        center_y = (self.y1 + self.y2) / 2

        to_x = (to_cell.x2 + to_cell.x1) / 2
        to_y = (to_cell.y1 + to_cell.y2) / 2

        #moving left
        if self.x1 > to_cell.x1:
            line = Line(Point(self.x1, center_y), Point(center_x, center_y))
            self.win.draw_line(line, color)
            line = Line(Point(to_x, to_y), Point(to_cell.x2, to_y))
            self.win.draw_line(line, color)

        # moving right
        elif self.x1 < to_cell.x1:
            line = Line(Point(center_x, center_y), Point(self.x2, center_y))
            self.win.draw_line(line, color)
            line = Line(Point(to_cell.x1, to_y), Point(to_x, to_y))
            self.win.draw_line(line, color)

        # moving up
        elif self.y1 > to_cell.y1:
            line = Line(Point(center_x, center_y), Point(center_x, self.y1))
            self.win.draw_line(line, color)
            line = Line(Point(to_x, to_cell.y2), Point(to_x, to_y))
            self.win.draw_line(line, color)

        # moving down
        elif self.y1 < to_cell.y1:
            line = Line(Point(center_x, center_y), Point(center_x, self.y2))
            self.win.draw_line(line, color)
            line = Line(Point(to_x, to_y), Point(to_x, to_cell.y1))
            self.win.draw_line(line, color)


