import unittest

from Maze.maze import Maze
from Graphics.graphics import Window

class Tests(unittest.TestCase):
    win = Window(800, 600)
    def test_maze_create_cells(self):
        """
        Check if correct number of cells can be made
        """
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win)
        self.assertEqual(
            (len(m1.cells) * len(m1.cells[0])),
            num_cols*num_rows
        )

    def test_large_maze(self):
        """
        Check if able to make a large maze
        """
        num_cols = 6
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win)
        self.assertEqual(
            (len(m1.cells) * len(m1.cells[0])),
            num_cols*num_rows
        )

    def test_reset_vist(self):
        """
        Check if able to clear 'visited' status of cells
        """
        num_cols = 6
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, self.win)
        m1.break_walls(0, 0)
        m1.reset_cells_visited()
        for col in m1.cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
