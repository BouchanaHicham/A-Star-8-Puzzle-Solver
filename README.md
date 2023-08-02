# A_Star_8_Puzzle_Solver

![Sliding Puzzle](https://github.com/BouchanaHicham/A_Star_8_Puzzle_Solver/blob/main/8_Puzzle_Pic.png)

## Description

This Python program uses the A* search algorithm to efficiently solve 3x3 sliding puzzles. It explores the puzzle state space, finds the optimal solution, and prints the path with corresponding moves. Challenge your puzzle-solving skills with this intelligent solver!

## Features

- A* Search: The program employs the A* search algorithm for an efficient and optimal solution.
- Heuristic Function: A Manhattan distance-based heuristic is used to estimate the cost to reach the goal state.
- Solution Path: The solver prints the solution path along with corresponding moves.

## Requirements

- Python (version 3.x)

## Usage

1. Define the initial 3x3 puzzle state in the `initial_state` and `goal_state` variable of the `A_Star_8_Puzzle_Solver.py` file.
2. Run the program: `python A_Star_8_Puzzle_Solver.py`
3. The program will display the initial board and then start solving the puzzle.

## Puzzle Representation

- The puzzle is represented as a 2D list (matrix), where the empty space is denoted by 0.
- The goal state is defined in the `goal_state` variable of the `A_Star_8_Puzzle_Solver.py` file.

## Example Usage

```python
# Define the initial state
initial_state = [[2, 8, 3],
                 [1, 6, 4],
                 [7, 0, 5]]
# Define the goal state
goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]
# Output:
Path is Shown Here ... Cost = ? | H = ? |G = ?
Action:  Up or Down or Left or Right
------------------------------
Parent State [[x, x, x],
              [x, x, x],
              [x, x, x]]

Current State [[y, y, y],
               [y, y, y],
               [y, y, y]]
------------------------------
Solution found in 5 
Moves: ['right', 'down', 'left', 'up', 'up']
```
## Author

**Bouchana Hicham**
