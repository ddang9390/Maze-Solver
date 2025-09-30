
class MazeSolver:
    def __init__(self, maze, algorithm=''):
        self.maze = maze
        self.cells = maze.cells
        self.num_cols = maze.num_cols
        self.num_rows = maze.num_rows
        self.algorithm = algorithm

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i=0, j=0):
        self.maze.animate()
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