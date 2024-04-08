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

        self.visited = []

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

        # for col in self.cells:
        #     for cell in col:
        #         self._draw_cell(cell.x1, cell.y1, cell)

        for x in range(0, self.num_rows):
            for y in range(0,self.num_cols):
                self._draw_cell(x, y)

    def _draw_cell(self, i, j):
        x2 = i + self.cell_size_x
        y2 = j + self.cell_size_y

        x1 = (i * self.cell_size_x) + self.x1
        y1 = (j * self.cell_size_y) + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

 
        #c = Cell(self.win, i, x2, j, y2)
        self.cells[i][j].x1 = x1
        self.cells[i][j].y1 = y1
        self.cells[i][j].x2 = x2
        self.cells[i][j].y2 = y2

        self.cells[i][j].draw()
        #self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        
        self.cells[len(self.cells)-1][len(self.cells)-1].has_bottom_wall = False
        # bottom = self.cells[len(self.cells)-1][len(self.cells)-1]
        self._draw_cell(len(self.cells)-1, len(self.cells)-1)


    def _break_walls(self, i, j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []

            #Vertical Movement
            if (j-1) > 0:
                if not self.cells[i][j-1].visited:
                    to_visit.append([i, j-1])
            if (j+1) < self.num_cols:
                if not self.cells[i][j+1].visited:
                    to_visit.append([i, j+1])

            #Horizontal Movement:
            if (i-1) > 0:
                if not self.cells[i-1][j].visited:
                    to_visit.append([i-1, j])
            if (i+1) < self.num_cols:
                if not self.cells[i+1][j].visited:
                    to_visit.append([i+1, j])

            if len(to_visit) == 0:
                return
            

            ran_index = random.randrange(0, len(to_visit))
            coord = to_visit[ran_index]

            # right
            if coord[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if coord[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # down
            if coord[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # up
            if coord[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # print(f"{x}, {y}")
            self._draw_cell(coord[0], coord[1])

            self._break_walls(coord[0], coord[1])

    def reset_cells_visited(self):
        for x in range(0, self.num_rows):
            for y in range(0,self.num_cols):
                self.cells[x][y].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i=0, j=0):
        self._animate()
        self.cells[i][j].visited = True

        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        

        #Vertical Movement
        if (j-1) > 0:
            if not self.cells[i][j-1].visited and not self.cells[i][j-1].has_bottom_wall:
                self.cells[i][j].draw_move(self.cells[i][j-1])
                if self.solve_r(i, j-1):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j-1], True)

        if (j+1) < self.num_cols:
            if not self.cells[i][j+1].visited and not self.cells[i][j+1].has_top_wall:
                self.cells[i][j].draw_move(self.cells[i][j+1])
                if self.solve_r(i, j+1):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j+1], True)

        #Horizontal Movement:
        if (i-1) > 0:
            if not self.cells[i-1][j].visited and not self.cells[i-1][j].has_right_wall:
                self.cells[i][j].draw_move(self.cells[i-1][j])
                if self.solve_r(i-1, j):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i-1][j], True)

        if (i+1) < self.num_cols:
            if not self.cells[i+1][j].visited and not self.cells[i+1][j].has_left_wall:
                self.cells[i][j].draw_move(self.cells[i+1][j])
                if self.solve_r(i+1, j):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i+1][j], True)

        return False