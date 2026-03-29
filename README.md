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
