# Initialize the game board
def create_board():
    return [' ' for _ in range(9)]

# Display the game board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if a move is valid
def is_valid_move(board, move):
    return board[move] == ' '

# Make a move on the board
def make_move(board, move, player):
    board[move] = player

# Check if the game is won
def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

# Check if the game is a draw
def is_draw(board):
    return ' ' not in board

# Main function to test the board and moves
def main():
    board = create_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (0-8): "))
        
        if is_valid_move(board, move):
            make_move(board, move, current_player)
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
