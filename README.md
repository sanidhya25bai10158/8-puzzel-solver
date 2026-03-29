# 8-Puzzle Solver

## This is a command line based solver for the classic 8-Puzzle (sliding tile puzzle), using the A\* search method to find the best solution.What is the 8-Puzzle?

The game of 8-Puzzle consists of 8 numbered squares and 1 empty square on a 3x3 grid. The goal is to arrange these squares by sliding them around on the grid until they match the final arrangement below.

1 2 3  
4 5 6  
7 8 _

## How It Works

### A\* Search Algorithm

To solve this using the A\* (A-star) algorithm, which is an AI-priced-solving algorithm (A\*), it is necessary to consider both of the two costs of each node when searching for the shortest possible solution.

f(n) = g(n) + h(n)

| Term | Meaning |
| --- | --- |
| g(n) | Number of moves taken so far |
| h(n) | Estimated moves still needed (heuristic) |
| f(n) | Total estimated cost — A\* always expands the lowest f first |


### The A\* algorithm uses a min-heap (priority queue) to always explore the next node with the lowest cost, ensuring that the solution found will always be the optimal (minimum number of moves).Manhattan Distance Heuristic

The cost estimate function h(n), which provides a value for the search algorithm, is based on the "Manhattan Distance" for each tile. To calculate the Manhattan distance, it is necessary to determine both the number of rows and columns each tile is away from its goal, and then sum the distance each tile is from its goal position to obtain the total distance for all tiles, to arrive at the total cost estimate. A\* will find the optimal solution because the h(n) function is admissible, meaning that it will not overestimate the actual cost of moving from the current state to the final state, and therefore A\* will always find the optimal solution.

### Solvability Check

 Some configurations of the puzzle are not solvable. The solver counts the number of tile inversions (a tile with a higher number precedes a tile with a lower number) prior to solving any configuration. If there are an odd number of inversions, the puzzle is not solvable and will not be solved.Running the Solver

python puzzle_solver.py

You’ll be prompted to either pick a preset puzzle or enter your own row by row (use 0 for the blank tile).

row 1: 1 2 3  
row 2: 4 0 5  
row 3: 7 8 6

After solving, you can view the full step-by-step solution or just the move sequence.

## Preset Difficulty Levels

| Level | Moves to Solve |
| --- | --- |
| Easy | 1   |
| Medium | 10  |
| Hard | 20  |
| Expert | 26  |

## Project Structure

puzzle_solver.py  
│  
├── solve() — A\* search engine  
├── heuristic() — Manhattan distance  
├── get_moves() — generates valid next states  
├── can_solve() — inversion-based solvability check  
├── get_path() — traces solution back from goal to start  
└── main() — CLI interface
