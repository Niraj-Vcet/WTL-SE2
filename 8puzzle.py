# ==========================================
# 8-Puzzle using Depth Limited Search (DLS)
# Dynamic Input Version
# ==========================================

# Goal state
GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Possible movements of blank tile
# Up, Down, Left, Right
ROW_MOVE = [-1, 1, 0, 0]
COL_MOVE = [0, 0, -1, 1]


# ==========================================
# Find blank tile
# ==========================================

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j


# ==========================================
# Check valid position
# ==========================================

def is_valid(row, col):
    return 0 <= row < 3 and 0 <= col < 3


# ==========================================
# Convert board to tuple
# ==========================================

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)


# ==========================================
# Copy board
# ==========================================

def copy_board(board):
    return [row[:] for row in board]


# ==========================================
# Depth Limited Search
# ==========================================

def dls(board, depth, visited_in_path, path):

    key = board_to_tuple(board)

    # Avoid cycles in current path
    if key in visited_in_path:
        return False

    visited_in_path.add(key)

    # Add current board to path
    path.append(board)

    # Goal reached
    if key == GOAL:
        return True

    # Depth limit reached
    if depth == 0:
        path.pop()
        visited_in_path.remove(key)
        return False

    # Find blank position
    row, col = find_blank(board)

    # Try all four possible moves
    for d in range(4):

        new_row = row + ROW_MOVE[d]
        new_col = col + COL_MOVE[d]

        if is_valid(new_row, new_col):

            # Create new board
            new_board = copy_board(board)

            # Move blank tile
            new_board[row][col] = new_board[new_row][new_col]
            new_board[new_row][new_col] = 0

            # Recursive DLS call
            if dls(
                new_board,
                depth - 1,
                visited_in_path,
                path
            ):
                return True

    # Backtracking
    path.pop()
    visited_in_path.remove(key)

    return False


# ==========================================
# Print solution path
# ==========================================

def print_path(path):

    print("\n========== SOLUTION PATH ==========\n")

    for step, board in enumerate(path):

        print(f"Step {step}:")

        for row in board:
            print(row)

        print("-------------------")


# ==========================================
# Display board
# ==========================================

def print_board(board):

    for row in board:
        print(row)


# ==========================================
# Dynamic Input
# ==========================================

print("==========================================")
print("       8-PUZZLE USING DLS")
print("==========================================")

print("\nEnter the starting puzzle.")
print("Use numbers 0-8.")
print("0 represents the blank tile.\n")


# Take puzzle input
start = []

for i in range(3):

    while True:

        row = list(map(int, input(
            f"Enter Row {i + 1}: "
        ).split()))

        if len(row) != 3:
            print("Please enter exactly 3 numbers.")
            continue

        start.append(row)
        break


# ==========================================
# Validate puzzle
# ==========================================

numbers = [num for row in start for num in row]

if sorted(numbers) != list(range(9)):

    print("\nInvalid puzzle!")

    print("You must enter every number from 0 to 8 exactly once.")

    exit()


# ==========================================
# Maximum depth
# ==========================================

max_depth = int(
    input("\nEnter maximum depth limit: ")
)


# ==========================================
# Display initial state
# ==========================================

print("\n========== INITIAL STATE ==========")

print_board(start)


# ==========================================
# Iterative Depth Limited Search
# ==========================================

found = False

for depth in range(max_depth + 1):

    path = []
    visited_in_path = set()

    found = dls(
        start,
        depth,
        visited_in_path,
        path
    )

    if found:

        print(
            "\nSolution found at depth limit:",
            depth
        )

        print_path(path)

        break


# ==========================================
# No solution
# ==========================================

if not found:

    print(
        "\nNo solution found within depth limit",
        max_depth
    )




#OUTPUT
# Enter Row 1: 1 2 3
# Enter Row 2: 4 0 6
# Enter Row 3: 7 5 8

# Enter maximum depth limit: 10