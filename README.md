# Python Game Collection

Welcome to the **Python Game Collection** repository! This repository houses a collection of classic games implemented in Python, including Sudoku, 8-Puzzle, and Tic-Tac-Toe. Each game showcases different algorithms and problem-solving techniques, making this repository a great resource for both game enthusiasts and programmers looking to enhance their understanding of game development in Python.

## Games Included

### 1. Sudoku Solver
- **Description**: Solve any given Sudoku puzzle using a backtracking algorithm. The solver ensures that each row, column, and 3x3 subgrid contains all digits from 1 to 9 without repetition.
- **Features**:
  - Efficient backtracking algorithm to solve puzzles.
  - Validates Sudoku puzzles for correctness.
  - Provides step-by-step solutions.

### 2. 8-Puzzle Game
- **Description**: The 8-Puzzle is a sliding puzzle consisting of a 3x3 grid with tiles numbered from 1 to 8 and one blank space. The goal is to rearrange the tiles to reach the ordered configuration.
- **Features**:
  - Implementation of A* search algorithm to find the optimal solution.
  - Heuristic functions to guide the search process.
  - Step-by-step display of the moves to solve the puzzle.

### 3. Tic-Tac-Toe
- **Description**: A classic two-player game where the aim is to place three marks in a row, column, or diagonal on a 3x3 grid.
- **Features**:
  - Playable against another player.
  - User-friendly interface for gameplay.

### 4. Rock-Paper-Scissors
- **Description**: A simple implementation of the classic Rock-Paper-Scissors game where you play against the computer.
- **Features**:
  - User input for Rock, Paper, or Scissors.
  - Random choice generation for the computer's move.
  - Keeps track of and displays the number of wins for both the user and the computer.
  - Allows the user to quit the game at any time by entering 'Q'.

### 5. Connect Four (AI vs. Player)
- **Description**: A two-player game where the objective is to connect four of your pieces in a row, either horizontally, vertically, or diagonally. This version allows the player to compete against an AI powered by the minimax algorithm.
- **Features**:
  - Playable against an AI opponent.
  - AI uses the minimax algorithm with alpha-beta pruning for optimal moves.
  - The game ends when a player connects four pieces or the board is full.

## Getting Started

### Prerequisites
- Python 3.x
### Installation
Clone the repository to your local machine using:
```bash
git clone https://github.com/Am1rreza/Python-Game-Collection.git
```
Navigate to the game you want to play or study:
```bash
cd Python-Game-Collection/sudoku
```
### Running the Games
Each game has its own directory. Follow the instructions in the respective README files to run the games.

For example, to run the Sudoku Solver:
```bash
python sudoku.py
```
## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the games or add new features.
