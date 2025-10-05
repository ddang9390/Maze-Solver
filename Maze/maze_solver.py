# Purpose - To solve a given maze using the selected algorithm

from Algorithms.astar import solve_astar
from Algorithms.bfs import solve_BFS
from Algorithms.dfs import solve_DFS

class MazeSolver:
    """
    Manages the execution of a maze solving algorithm

    Holds a reference to the maze to be solved and the user's selected algorithm
    Provides a single 'solve' method to utilize the selected algorithm

    Attributes:
        maze (Maze): Reference to instance of maze to be solved
        cells (list): List of cells from the maze
        num_cols (int): Number of columns in the maze
        num_rows (int): Number of rows in the maze
        algorithm (str): Indentifier for the algorithm to be used
    """
    def __init__(self, maze, algorithm=''):
        """
        Initializes the maze solver

        Arguments:
            maze (Maze): Reference to instance of maze to be solved
            algorithm (str): Indentifier for the algorithm to be used. Defaults to DFS
        """
        self.maze = maze
        self.cells = maze.cells
        self.num_cols = maze.num_cols
        self.num_rows = maze.num_rows
        self.algorithm = algorithm

    def solve(self):
        """
        Solves the maze using the algorithm selected by the user

        Returns:
            bool: True if solution was found, False if not
        """
        if self.algorithm == 'bfs':
            return solve_BFS(self)
        if self.algorithm == 'A*':
            return solve_astar(self)
        
        return solve_DFS(self, 0, 0)
