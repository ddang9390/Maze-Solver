# Purpose - To draw cells for a grid and lines showing movement between the cells

from line import Line
from point import Point

class Cell:
    """
    Represents a single cell in the maze grid.

    Attributes:
        win (Window): The Window to be drawn on
        x1, y1 (int): The top-left coordinate of the cell.
        x2, y2 (int): The bottom-right coordinate of the cell.
        has_left_wall (bool): True if the cell has a wall on its left side.
        has_right_wall (bool): True if the cell has a wall on its right side.
        has_top_wall (bool): True if the cell has a wall on its top side.
        has_bottom_wall (bool): True if the cell has a wall on its bottom side.
        visited (bool): True if the cell was visited before.
        placement (list[int]): The coordinates of the cell in the maze grid.
        parent (Cell | None): The previous cell that led to this one in a path
        f (float): The f-score used by the A* algorithm (g-score + h-score).
    """
     
    def __init__(self, win, x1=None, x2=None, y1=None, y2=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, placement=[], parent=None, f=0):
        """
        Initializes a cell in a maze
        """
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
        self.placement = placement

        self.visited = False
        self.parent = parent
        self.f = f
        
    def draw(self, color="black"):
        """
        Draw the walls of a cell. Uses black if there is supposed to be a wall,
        uses white when removing a wall.

        Argument:
            color (str) - Color of the line
        """
        # Handling left walls
        if self.has_left_wall:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, color)
        else:
            l = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l, "white")

        # Handling right walls
        if self.has_right_wall:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, color)
        else:
            l = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(l, "white")

        # Handling upper walls
        if self.has_top_wall:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, color)
        else:
            l = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(l, "white")

        # Handling bottom walls
        if self.has_bottom_wall:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, color)
        else:
            l = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(l, "white")

        

    def draw_move(self, to_cell, undo=False):
        """
        Draws a line representing a move from one cell to another

        Arguments:
            to_cell (Cell): The destination cell
            undo (bool): If True, draws a gray line representing backtracking
                         Else draw a red line
        """
        if not undo:
            color = "red"
        else:
            color = "gray"

        center_self = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        center_to = Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)
        
        self.win.draw_line(Line(center_self, center_to), color)



