import numpy as np
import random

ROWS = 6
COLUMNS = 7

def create_grid():
    return np.zeros((ROWS, COLUMNS))

# Print the grid, flipping it so the bottom row is displayed at the bottom
def print_grid(grid):
    print(np.flip(grid, 0))

def is_valid_location(grid, col):
    # If the top row of the column is 0, it's empty and valid
    return grid[ROWS-1][col] == 0

# Find the first open row in the specified column
def get_next_open_row(grid, col):
    for row in range(ROWS):
        if grid[row][col] == 0:  # Look for the first empty space in this column
            return row

def drop_piece(grid, row, col, piece):
    grid[row][col] = piece

def check_winner(grid, piece):
    # Check horizontal locations for win
    for row in range(ROWS):
        for col in range(COLUMNS - 3):  # Only need to check columns 0-3 for horizontal win
            if grid[row][col] == piece and grid[row][col + 1] == piece and grid[row][col + 2] == piece and grid[row][col + 3] == piece:
                return True

    # Check vertical locations for win
    for row in range(ROWS - 3):  # Only need to check rows 0-3 for vertical win
        for col in range(COLUMNS):
            if grid[row][col] == piece and grid[row + 1][col] == piece and grid[row + 2][col] == piece and grid[row + 3][col] == piece:
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if grid[row][col] == piece and grid[row + 1][col + 1] == piece and grid[row + 2][col + 2] == piece and grid[row + 3][col + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if grid[row][col] == piece and grid[row - 1][col + 1] == piece and grid[row - 2][col + 2] == piece and grid[row - 3][col + 3] == piece:
                return True

    return False

# Minimax Algorithm
def minimax(grid, depth, alpha, beta, maximizing_player):
    valid_columns = [col for col in range(COLUMNS) if is_valid_location(grid, col)]
    
    # Check if the game is over (either a winner or a full grid)
    is_terminal = check_winner(grid, 1) or check_winner(grid, 2) or len(valid_columns) == 0
    
    # If depth is 0 or a terminal state is reached, return evaluation score
    if depth == 0 or is_terminal:
        if check_winner(grid, 2):  # AI has won
            return 100000000000
        elif check_winner(grid, 1):  # Player has won
            return -100000000000
        else:
            # Heuristic evaluation: evaluate based on potential opportunities
            score = 0
            for col in valid_columns:
                row = get_next_open_row(grid, col)
                temp_grid = grid.copy()
                drop_piece(temp_grid, row, col, 2)  # Simulate AI move
                if check_winner(temp_grid, 2):  # AI wins
                    score += 10
                elif check_winner(temp_grid, 1):  # Opponent wins
                    score -= 10
                else:
                    # Evaluate potential for AI to create 4-in-a-row or block opponent
                    score += evaluate_board(temp_grid, 2)  # AI evaluation
                    score -= evaluate_board(temp_grid, 1)  # Player evaluation
            return score

    # Maximizing player's turn (AI)
    if maximizing_player:
        max_eval = -float('inf')
        for col in valid_columns:
            row = get_next_open_row(grid, col)
            temp_grid = grid.copy()
            drop_piece(temp_grid, row, col, 2)  # AI makes a move
            eval = minimax(temp_grid, depth - 1, alpha, beta, False)  # Recursive call for minimizing player
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)  # Alpha is the best score for maximizing player
            if beta <= alpha:  # Beta cutoff, prune the tree
                break
        return max_eval
    
    # Minimizing player's turn (Opponent)
    else:
        min_eval = float('inf')
        for col in valid_columns:
            row = get_next_open_row(grid, col)
            temp_grid = grid.copy()
            drop_piece(temp_grid, row, col, 1)  # Opponent makes a move
            eval = minimax(temp_grid, depth - 1, alpha, beta, True)  # Recursive call for maximizing player
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)  # Beta is the best score for minimizing player
            if beta <= alpha:  # Alpha cutoff, prune the tree
                break
        return min_eval

# New heuristic function to evaluate board
def evaluate_board(grid, player):
    score = 0
    
    # Evaluate horizontal, vertical, and diagonal opportunities for the given player
    for row in range(ROWS):
        for col in range(COLUMNS):
            if col + 3 < COLUMNS:  # Check horizontally
                window = [grid[row][col+i] for i in range(4)]
                score += score_window(window, player)
            if row + 3 < ROWS:  # Check vertically
                window = [grid[row+i][col] for i in range(4)]
                score += score_window(window, player)
            if row + 3 < ROWS and col + 3 < COLUMNS:  # Check diagonal \
                window = [grid[row+i][col+i] for i in range(4)]
                score += score_window(window, player)
            if row - 3 >= 0 and col + 3 < COLUMNS:  # Check diagonal /
                window = [grid[row-i][col+i] for i in range(4)]
                score += score_window(window, player)
                
    return score

# Evaluate a specific window of 4 cells
def score_window(window, player):
    score = 0
    opponent = 1 if player == 2 else 2
    
    # Count the occurrences of player's and opponent's pieces in the window
    player_count = window.count(player)
    opponent_count = window.count(opponent)
    
    if player_count == 4:
        score += 100  # Player wins this window
    elif player_count == 3 and opponent_count == 0:
        score += 5  # Potential winning move for player
    elif player_count == 2 and opponent_count == 0:
        score += 2  # Potential for a future move
    if opponent_count == 3 and player_count == 0:
        score -= 4  # Block opponent's winning move
    return score

# AI move using Minimax
def ai_move(grid):
    valid_columns = [col for col in range(COLUMNS) if is_valid_location(grid, col)]
    best_score = -float('inf')
    best_col = random.choice(valid_columns)  # Default to a random move if no better move is found
    
    for col in valid_columns:
        row = get_next_open_row(grid, col)
        temp_grid = grid.copy()
        drop_piece(temp_grid, row, col, 2)  # AI is piece '2'
        score = minimax(temp_grid, 4, -float('inf'), float('inf'), True)
        if score > best_score:
            best_score = score
            best_col = col
    
    return best_col

def play_game():
    grid = create_grid()
    game_over = False
    turn = 0  #0 for Player, 1 for AI

    while not game_over:
        print_grid(grid)

        if turn == 0:  # Player's turn
            col = int(input("Player, choose a column (0-6): "))
            if is_valid_location(grid, col):
                row = get_next_open_row(grid, col)
                drop_piece(grid, row, col, 1)  # Player is '1'
                if check_winner(grid, 1):
                    print("Player wins!")
                    game_over = True
        else:  # AI's turn
            print("AI is thinking...")
            col = ai_move(grid)
            row = get_next_open_row(grid, col)
            drop_piece(grid, row, col, 2)  # AI is '2'
            if check_winner(grid, 2):
                print("AI wins!")
                game_over = True

        if np.all(grid != 0):  # Check for draw
            print("It's a draw!")
            game_over = True

        turn = 1 - turn  # Toggle between Player and AI

play_game()