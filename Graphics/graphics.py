# Purpose - The GUI that the maze will take place in

import time
from tkinter import Tk, Canvas, Button, Frame
from Maze.maze_solver import MazeSolver

class Window:
    """
    Represents the Window that would hold all of the GUI objects.
    
    Includes the maze, timer, and buttons for user input

    Attributes:
        width (int): Width of the window
        height (int): Height of the window
        root (Tk): Root widget using Tk
        canvas (Canvas): Canvas that would have the GUI elements drawn on it
        maze (Maze): The maze that will be on the window
        finished (bool): True if the solver finished solving the maze
        timer: Represents the timer showing how long it takes to solve a maze
        start_time (float): Represents the number that the timer will display
    """
    def __init__(self, width, height):
        """
        Initializes the window
        """
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.maze = None
        self.finished = False

        # Timer related variables
        self.timer = None
        self.start_time = None
        self.init_timer()

        # Buttons
        self.create_buttons()

    def redraw(self):
        """
        Updates the maze while it is being solved
        """
        self.root.update_idletasks()
        self.root.update()

        # Run timer while maze is being solved
        if not self.finished:
            self.update_timer()

    def wait_for_close(self):
        """
        Keeps the window open after the maze is solved
        """
        self.finished = True
        
        while self.finished:
            self.redraw()

    def close(self):
        """
        Closes the window
        """
        self.finished = False

    def draw_line(self, line, fill_color):
        """
        Draws a line on the canvas

        Arguments:
            line (Line): Represents the line to be drawn
            fill_color (str): Represents the color to use
        """
        line.draw(self.canvas, fill_color)

    def init_timer(self):
        """
        Sets the timer to 0
        """
        self.start_time = time.perf_counter()
        self.timer = self.canvas.create_text(self.width-50, 50, text='0.00s', font=('Arial', 16), fill='black')

    def update_timer(self):
        """
        Update the timer as the maze is being solved
        """
        elapsed_time = time.perf_counter() - self.start_time
        self.canvas.itemconfigure(self.timer, text=f"{elapsed_time: 0.2f}s")

    def create_buttons(self):
        """
        Creates and displays the buttons on the canvas
        """
        button_frame = Frame(self.root)
        button_frame.pack(expand=True)

        new_maze_button = Button(button_frame, text="New Maze", command=self.reset_maze)
        dfs_button = Button(button_frame, text="DFS", command=lambda: self.solve_func('dfs'))
        bfs_button = Button(button_frame, text="BFS", command=lambda: self.solve_func('bfs'))
        astar_button = Button(button_frame, text="A*", command=lambda: self.solve_func('A*'))

        new_maze_button.pack(side='left')
        dfs_button.pack(side='left')
        bfs_button.pack(side='left')
        astar_button.pack(side='left')

    def solve_func(self, algorithm=''):
        """
        Has the maze be solved using the algorithm provided by the selected button

        Argument:
            alogorithm (str): Represents the algorithm to be used
        """
        self.canvas.delete("all")
        self.maze.reset_cells_visited()
        self.maze.create_cells()
        self.finished = False

         # Timer related variables
        self.timer = None
        self.start_time = None
        self.init_timer()

        maze_solver = MazeSolver(self.maze, algorithm=algorithm)
        maze_solver.solve()
        self.wait_for_close()

    def reset_maze(self):
        """
        Resets the maze by making a new one
        """
        self.canvas.delete("all")
        self.maze.refresh_maze()
        self.maze.break_entrance_and_exit()
        self.maze.break_walls(0, 0)
        self.maze.reset_cells_visited()