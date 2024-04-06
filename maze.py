from cell import Cell
import time
import random

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
            cols = []
            for y in range(0,self.num_cols):
                c = Cell(self.win, sizeX, None, sizeY)
                #self.cells.append(c)
                cols.append(c)
                sizeY += self.cell_size_y

            sizeX += self.cell_size_x
            sizeY = self.y1
            self.cells.append(cols)

        for col in self.cells:
            for cell in col:
                self._draw_cell(cell.x1, cell.y1, cell)

    def _draw_cell(self, i, j, cell):
        x2 = i + self.cell_size_x
        y2 = j + self.cell_size_y

        #print(f"({i},{j}), ({x2}, {y2})")
        #c = Cell(self.win, i, x2, j, y2)
        cell.x1 = i
        cell.y1 = j
        cell.x2 = x2
        cell.y2 = y2

        cell.draw()
        #self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(self.cells[0][0].x1, self.cells[0][0].y1, self.cells[0][0])

        
        self.cells[len(self.cells)-1][len(self.cells)-1].has_bottom_wall = False
        bottom = self.cells[len(self.cells)-1][len(self.cells)-1]
        self._draw_cell(bottom.x1, bottom.y1, bottom)


    def _break_walls(self):
        visited = []
        for x in range(1, self.num_rows+1):
            for y in range(1,self.num_cols+1):
                cell = self.cells[x-1][y-1]
                visited.append(cell)

        
