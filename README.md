# MazePath Visualizer

<details>
    <summary>Table of Contents</summary>
    <ol>
            <li><a href="#about-the-project">About the Project</a></li>
            <ul>
                <li><a href="#demo">Demo</a></li>
                <li><a href="#key-features">Key Features</a></li>
            </ul>
            <li><a href="#getting-started">Getting Started</a></li>
            <ul>
                <li><a href="#prerequisites">Prerequisites</a></li>
                <li><a href="#installation">Installation</a></li>
            </ul>
            <li><a href="#algorithm-explanations">Algorithm Explanations</a></li>
            <ul>
                <li><a href="#recursive-backtracking">Recursive Backtracking</a></li>
                <li><a href="#depth-first-search-dfs">Depth-First Search (DFS)</a></li>
                <li><a href="#breadth-first-search-bfs">Breadth-First Search (BFS)</a></li>
                <li><a href="#a-search">A* Search</a></li>
            </ul>
            <li><a href="#contact">Contact</a></li>
    </ol>
</details>

## About the Project
This project randomly generates a solvable maze and visualizes three different search algorithms with each having their own unique strategy for solving the maze.

### Demo

### Key Features
1. Randomly generates a maze with an actual solution
2. Visualizes the possible solutions from 3 different algorithms


## Getting Started
### Prerequisites
Python 3.7+

### Installation
1. Download the code or clone the repository  
git clone https://github.com/ddang9390/MazePath-Visualizer.git
2. Navigate to the project directory  
cd MazePath-Visualizer
3. Run the main file  
python3 main.py

## Algorithm Explanations
This project utilizes the Recursive Backtracking algorithm to generate the mazes and also visualizes the way three classic search algorithms can solve a maze.

### Recursive Backtracking
Recursive backtracking is what is used to randomly generate the mazes. This is how the process goes after making a grid filled with walls:
1. Starting from a certain cell, we would select a random unvisited neighbor of that cell  
2. Break the walls between the cell and the neighbor 
3. Then recursively call ourself on that neighbor
4. If a cell has no unvisited neighbors, we would have hit a dead end. Thus we backtrack to a previous cell and start over
5. Repeat the process until all cells in the grid have been visited 

### Depth-First Search (DFS)
#### How it Works
DFS is a recursive algorithm that would randomly choose a path and go as far down as it can. Once it cannot go further, it backtracks until it reaches a point where it can choose a different path. It repeats itself until it reaches the goal.  

#### Performance Analysis
This algorithm does not guarantee that it will find the shortest path, it is entirely up to luck. For smaller and simpler mazes, it could find a path relatively quickly. But for more complex mazes, it may often reach dead-ends further delaying the time it takes to reach the end. With some especially bad luck, DFS may reach a solution where it would take the longest possible time.

### Breadth-First Search (BFS)
#### How it Works
Once BFS reaches a crossroad, it would not choose a random path like DFS. Instead it would choose to go through every single possible path. It would repeat this process until the goal is reached.

#### Performance Analysis
BFS would have a better chance than DFS when it comes to finding the sortest path to the goal. However the time it takes to reach the goal will be dependent on the complexity of the maze since it would have to go through every possible path before reaching the goal. Because of this, there are moments when DFS would be faster than BFS. There may even be moments that BFS would take the longest possible time to solve the maze.

### A* Search
#### How it Works
The A* algorithm would be making use of a heuristic function to find its way to the goal. In the case of this project, the Manhattan distance formula is being used. Manhattan distance is the sum of the absolute differences between the coordinates of two points in a path. 

This Manhattan distance formula would be used to find two things:
1. The g-score: The distance from the start to the current cell in the maze
2. The h-score: The distance from the current cell in the maze to the goal

These two scores are then summed up to find the f-score of the cell. The f-score is what is used to determine the optimal path from the start to the goal. 

#### Performance Analysis
The shortest path is guaranteed to be found. Since it does not have to go through every path like BFS, A* would prove to be a more efficient algorithm thus resulting in it being the faster algorithm in the majority of cases.

## Contact
Daniel Dang - https://www.linkedin.com/in/daniel-dang-704791a6/

https://github.com/ddang9390/MazePath-Visualizer