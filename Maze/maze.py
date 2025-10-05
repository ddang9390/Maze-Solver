# Purpose - To create a maze

from Graphics.cell import Cell
import time
import random

class Maze:
    """
    Represents a randomly generated maze

    Attributes:
        cells (list): List of cells
        x1 (int): x-coordinate of top left corner
        y1 (int): y-coordinate of top left corner
        num_cols (int): Number of columns
        num_rows (int): Number of rows
        algorithm (str): Indentifier for the algorithm to be used
        cell_size_x (int): How wide a cell is
        cell_size_y (int): How tall a cell is
    """
    def __init__(self, x1, y1, num_rows, num_cols,
                cell_size_x, cell_size_y, win
    ):
        """
        Initializes the maze
        """
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.visited = []

        self.create_cells()

    def refresh_maze(self):
        """
        Refreshes the maze
        """
        self.cells = []
        self.visited = []
        self.create_cells()

    def create_cells(self):
        """
        Creates the cells in the maze
        """
        sizeX = self.x1
        sizeY = self.y1
        for x in range(0, self.num_rows):
            cols = []
            for y in range(0,self.num_cols):
                c = Cell(self.win, sizeX, None, sizeY, placement=[x,y])

                cols.append(c)
                sizeY += self.cell_size_y

            sizeX += self.cell_size_x
            sizeY = self.y1
            self.cells.append(cols)

        for x in range(0, self.num_rows):
            for y in range(0,self.num_cols):
                self.draw_cell(x, y)

    def draw_cell(self, i, j):
        """
        Actually draw the cells in the maze

        Arguments:
            i (int): x-coordinate of cell in a grid
            j (int): y-coordinate of cell in a grid
        """
        x2 = i + self.cell_size_x
        y2 = j + self.cell_size_y

        x1 = (i * self.cell_size_x) + self.x1
        y1 = (j * self.cell_size_y) + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        # The four coordinates that make up a square cell
        self.cells[i][j].x1 = x1
        self.cells[i][j].y1 = y1
        self.cells[i][j].x2 = x2
        self.cells[i][j].y2 = y2

        self.cells[i][j].draw()


    def animate(self):
        """
        Animates the drawing process
        """
        self.win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        """
        Creates the entrance and exit for the maze
        """
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)

        
        self.cells[len(self.cells)-1][len(self.cells)-1].has_bottom_wall = False
        self.draw_cell(len(self.cells)-1, len(self.cells)-1)


    def break_walls(self, i, j):
        """
        Breaks random walls in the maze through recursive backtracking

        Starts at a cell of coordinates (i, j), randomly chooses un unvisited neighbor,
        and breaks the wall between them. Then calls itself recursively on the neighbor
        and continue this process until all cells have been visited.

        Arguments:
            i (int): x coordinate of the cell in a grid
            j (int): y coordinate of the cell in a grid
        """
        self.cells[i][j].visited = True
        while True:
            to_visit = []

            # Check vertical neighbors
            if (j-1) > 0:
                if not self.cells[i][j-1].visited:
                    to_visit.append([i, j-1])
            if (j+1) < self.num_cols:
                if not self.cells[i][j+1].visited:
                    to_visit.append([i, j+1])

            # Check horizontal neighbors
            if (i-1) > 0:
                if not self.cells[i-1][j].visited:
                    to_visit.append([i-1, j])
            if (i+1) < self.num_cols:
                if not self.cells[i+1][j].visited:
                    to_visit.append([i+1, j])

            # Returns when there are no more cells to visit
            if len(to_visit) == 0:
                return

            # Randomly choose a neighbor
            ran_index = random.randrange(0, len(to_visit))
            coord = to_visit[ran_index]

            # Moving right
            if coord[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # Moving left
            if coord[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # Moving down
            if coord[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # Moving up
            if coord[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            self.draw_cell(coord[0], coord[1])
            self.break_walls(coord[0], coord[1])

    def reset_cells_visited(self):
        """
        Mark all cells in the maze as not being visited yet
        """
        for x in range(0, self.num_rows):
            for y in range(0,self.num_cols):
                self.cells[x][y].visited = False

    