# Purpose - To solve a given maze using the selected algorithm

import time

class MazeSolver:
    def __init__(self, maze, algorithm=''):
        self.maze = maze
        self.cells = maze.cells
        self.num_cols = maze.num_cols
        self.num_rows = maze.num_rows
        self.algorithm = algorithm

    def solve(self):
        if self.algorithm == 'bfs':
            return self.solve_BFS()
        return self.solve_DFS(0, 0)

    def solve_DFS(self, i=0, j=0):
        self.maze.animate()
        self.cells[i][j].visited = True

        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        #Vertical Movement
        if (j-1) > 0:
            if not self.cells[i][j-1].visited and not self.cells[i][j-1].has_bottom_wall:
                self.cells[i][j].draw_move(self.cells[i][j-1])
                if self.solve_DFS(i, j-1):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j-1], True)

        if (j+1) < self.num_cols:
            if not self.cells[i][j+1].visited and not self.cells[i][j+1].has_top_wall:
                self.cells[i][j].draw_move(self.cells[i][j+1])
                if self.solve_DFS(i, j+1):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j+1], True)

        #Horizontal Movement:
        if (i-1) > 0:
            if not self.cells[i-1][j].visited and not self.cells[i-1][j].has_right_wall:
                self.cells[i][j].draw_move(self.cells[i-1][j])
                if self.solve_DFS(i-1, j):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i-1][j], True)

        if (i+1) < self.num_cols:
            if not self.cells[i+1][j].visited and not self.cells[i+1][j].has_left_wall:
                self.cells[i][j].draw_move(self.cells[i+1][j])
                if self.solve_DFS(i+1, j):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i+1][j], True)

        return False
    
    def solve_BFS(self):
        self.maze.animate()

        queue = []
        queue.append(self.cells[0][0])
        self.cells[0][0].visited = True

        while queue:
            current_cell = queue.pop(0)
            x, y = current_cell.placement[0], current_cell.placement[1]
            if x == self.num_cols-1 and y == self.num_rows-1:
                return True
            
            if not current_cell.has_left_wall and x - 1 >= 0:
                if not self.cells[x-1][y].visited:
                    queue.append(self.cells[x-1][y])
                    current_cell.draw_move(self.cells[x-1][y])
                    

            if not current_cell.has_right_wall and x + 1 < self.num_cols:
                if not self.cells[x+1][y].visited:
                    queue.append(self.cells[x+1][y])
                    current_cell.draw_move(self.cells[x+1][y])
                

            if not current_cell.has_top_wall and y - 1 >= 0:
                if not self.cells[x][y-1].visited:
                    queue.append(self.cells[x][y-1])
                    current_cell.draw_move(self.cells[x][y-1])

            if not current_cell.has_bottom_wall and y + 1 < self.num_rows:
                if not self.cells[x][y+1].visited:
                    queue.append(self.cells[x][y+1])
                    current_cell.draw_move(self.cells[x][y+1])

            # TODO - find alternative to animating path, the time.sleep works differently
            #        in a while loop causing inaccurate results
            self.maze.win.redraw()
            time.sleep(0.0005)

