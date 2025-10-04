# Purpose - To solve a given maze using the selected algorithm

import time
from Algorithms.astar import solve_astar
from Algorithms.bfs import solve_BFS
from Algorithms.dfs import solve_DFS

class MazeSolver:
    def __init__(self, maze, algorithm=''):
        self.maze = maze
        self.cells = maze.cells
        self.num_cols = maze.num_cols
        self.num_rows = maze.num_rows
        self.algorithm = algorithm

    def solve(self):
        if self.algorithm == 'bfs':
            return solve_BFS(self)
        if self.algorithm == 'A*':
            return solve_astar(self)
        return solve_DFS(self, 0, 0)


    
    


    
                
            