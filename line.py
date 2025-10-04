# Purpose - The lines that would be drawn on the canvas

class Line:
    """
    Represents the line that would be drawn on the canvas

    Attributes:
        p1 (Point): First vertice of the line
        p2 (Point): Second vertice of the line
    """
    def __init__(self, p1, p2):
        """
        Initializes the line
        """
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        """
        Draws the line

        Arguments:
            canvas (Canvas): Represents the canvas that the line would be drawn on
            fill_color (str): Represents the color that the line will use
        """
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )
        canvas.pack()