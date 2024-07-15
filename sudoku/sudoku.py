def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is already in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # No empty space left, solution found
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


# Example
sudoku_board = [
    [0, 0, 0, 6, 1, 5, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 3, 0, 0, 0, 0, 5, 0, 0],
    [7, 0, 0, 4, 5, 0, 0, 0, 2],
    [0, 0, 0, 2, 9, 7, 6, 0, 0],
    [2, 1, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 2, 3, 0, 0, 9],
    [3, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 3, 0, 7]
]

if solve_sudoku(sudoku_board):
    print_board(sudoku_board)
else:
    print("No solution exists")
