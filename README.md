# MazePath Visualizer

<details>
    <summary>Table of Contents</summary>
    <ol>
            <li><a href="#about">About the Project</a></li>
            <ul>
                <li><a href="#demo">Demo</a></li>
                <li><a href="#key_features">Key Features</a></li>
            </ul>
            <li><a href="#getting_started">Getting Started</a></li>
            <ul>
                <li><a href="#prereq">Prerequisites</a></li>
                <li><a href="#installation">Installation</a></li>
            </ul>
            <li><a href="#algos">Algorith Explanations</a></li>
            <ul>
                <li><a href="#backtracking">Recursive Backtracking</a></li>
                <li><a href="#dfs">Depth-First Search (DFS)</a></li>
                <li><a href="#bfs">Breadth-First Search (BFS)</a></li>
                <li><a href="#astar">A* Search</a></li>
            </ul>
            <li><a href="#Contact">Contact</a></li>
    </ol>
</details>

## About the Project

### Demo

### Key Features


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

### Recursive Back Tracking
Recursive backtracking is what is used to randomly generate the mazes. We would start by making a grid filled with walls. Then starting from a certain cell, we would select a random unvisited neighbor of that cell and break the walls between them. We would then recursively call ourself on that neighbor and repeat the process until all cells in the grid have been visited.

### Depth-First Search (DFS)
DFS is a recursive algorithm that would randomly choose a path and go as far down as it can. Once it cannot go further, it backtracks until it reaches a point where it can choose a different path. It repeats itself until it reaches the goal.  

This algorithm does not guarantee that it will find the shortest path, it is entirely up to luck. For smaller and simpler mazes, it could find a path relatively quickly. But for more complex mazes, it may often reach dead-ends further delaying the time it takes to reach the end. With some especially bad luck, DFS may reach a solution where it would take the longest possible time.

### Breadth-First Search (BFS)
Once BFS reaches a crossroad, it would not choose a random path like DFS. Instead it would choose to go through every single possible path. It would repeat this process until the goal is reached.

BFS would have a better chance than DFS when it comes to finding the sortest path to the goal. However the time it takes to reach the goal will be dependent on the complexity of the maze since it would have to go through every possible path before reaching the goal. Because of this, there are moments when DFS would be faster than BFS. There may even be moments that BFS would take the longest possible time to solve the maze.

### A* Search
The A* algorithm would be making use of a heuristic function to find its way to the goal. In the case of this project, the Manhattan distance formula is being used. Manhattan distance is the sum of the absolute differences between the coordinates of two points in a path. 

This Manhattan distance formula would be used to find two things:
1. The g-score: The distance from the start to the current cell in the maze
2. The h-score: The distance from the current cell in the maze to the goal

These two scores are then summed up to find the f-score of the cell. The f-score is what is used to determine the optimal path from the start to the goal. 

## Contact
Daniel Dang - https://www.linkedin.com/in/daniel-dang-704791a6/

https://github.com/ddang9390/MazePath-Visualizer