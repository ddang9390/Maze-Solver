# Purpose - The GUI that the maze will take place in

import time
from tkinter import Tk, Canvas, Button, Frame
from maze_solver import MazeSolver

class Window:
    def __init__(self, width, height):
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

    # Update maze while it is being solved
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

        # Run timer while maze is being solved
        if not self.finished:
            self.update_timer()

    # Keep window open after maze is solved
    def wait_for_close(self):
        self.finished = True
        
        while self.finished:
            self.redraw()

    def close(self):
        self.finished = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def init_timer(self):
        self.start_time = time.perf_counter()
        self.timer = self.canvas.create_text(self.width-50, 50, text='0.00s', font=('Arial', 16), fill='black')

    def update_timer(self):
        elapsed_time = time.perf_counter() - self.start_time
        self.canvas.itemconfigure(self.timer, text=f"{elapsed_time: 0.2f}s")

    def create_buttons(self):
        button_frame = Frame(self.root)
        button_frame.pack(expand=True)

        new_maze_button = Button(button_frame, text="New Maze", command=self.resolve_func)
        dfs_button = Button(button_frame, text="DFS", command=lambda: self.resolve_func('dfs'))
        bfs_button = Button(button_frame, text="BFS", command=lambda: self.resolve_func('bfs'))
        astar_button = Button(button_frame, text="A*", command=lambda: self.resolve_func('A*'))

        new_maze_button.pack(side='left')
        dfs_button.pack(side='left')
        bfs_button.pack(side='left')
        astar_button.pack(side='left')

    def resolve_func(self, algorithm=''):
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