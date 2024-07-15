import heapq

# Find the position of the blank space (0) in the puzzle
def find_blank(puzzle):
    for i, row in enumerate(puzzle):
        if 0 in row:
            return (i, row.index(0))

# Check if the move is within the bounds of the puzzle
def is_valid_move(row, col):
    return 0 <= row < 3 and 0 <= col < 3

# Move the blank space in the specified direction if the move is valid
def move_blank(puzzle, move):
    new_puzzle = [row[:] for row in puzzle]
    blank_row, blank_col = find_blank(new_puzzle)
    new_row, new_col = blank_row + move[0], blank_col + move[1]

    if is_valid_move(new_row, new_col):
        moved_tile = new_puzzle[new_row][new_col]
        new_puzzle[blank_row][blank_col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[blank_row][blank_col]
        return new_puzzle, moved_tile
    return None, None

# Heuristic function: count the number of misplaced tiles
def heuristic(puzzle, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j] != goal[i][j]:
                distance += 1
    return distance

# A* algorithm to solve the puzzle
def a_star(puzzle, goal):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    pq = []
    heapq.heappush(pq, (0 + heuristic(puzzle, goal), 0, puzzle, [], []))
    visited = set()

    while pq:
        _, cost, current_puzzle, path, move_path = heapq.heappop(pq)

        if current_puzzle == goal:
            return move_path

        visited.add(tuple(map(tuple, current_puzzle)))

        for move in moves:
            new_puzzle, moved_tile = move_blank(current_puzzle, move)
            if new_puzzle and tuple(map(tuple, new_puzzle)) not in visited:
                new_path = path + [new_puzzle]
                new_move_path = move_path + [moved_tile]
                heapq.heappush(pq, (cost + 1 + heuristic(new_puzzle, goal),
                               cost + 1, new_puzzle, new_path, new_move_path))

    return None


# Initial puzzle state
initial_puzzle = [
    [2, 0, 8],
    [7, 6, 3],
    [5, 4, 1]
]

# Goal puzzle state
goal_puzzle = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Find the solution path using A* algorithm
move_path = a_star(initial_puzzle, goal_puzzle)

# Print the steps to solve the puzzle
if move_path:
    print("Moves to solve the puzzle:")
    for move in move_path:
        print(move)
else:
    print("No solution found.")

# Print final puzzle state
print("Final puzzle state:")
for row in goal_puzzle:
    print(" ".join(str(num) for num in row))
