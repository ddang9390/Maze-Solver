from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()

    def _create_cells(self):
        sizeX = self.x1
        sizeY = self.y1
        for x in range(0, self.num_rows):
            for y in range(0,self.num_cols):
                c = Cell(self.win, sizeX, None, sizeY)
                self.cells.append(c)
                sizeY += self.cell_size_y

            sizeX += self.cell_size_x
            sizeY = self.y1

        for cell in self.cells:
            self._draw_cell(cell.x1, cell.y1)

    def _draw_cell(self, i, j):
        x2 = i + self.cell_size_x
        y2 = j - self.cell_size_y

        c = Cell(self.win, i, x2, j, y2)

        c.draw()
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)