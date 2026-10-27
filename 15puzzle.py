import heapq


# ==========================================
# 15-Puzzle Configuration
# ==========================================

N = 4

GOAL = (
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 0
)


# ==========================================
# Heuristic Function
# Manhattan Distance
# ==========================================

def heuristic(state):

    distance = 0

    for index, value in enumerate(state):

        # Ignore blank tile
        if value == 0:
            continue

        current_row = index // N
        current_col = index % N

        goal_index = value - 1

        goal_row = goal_index // N
        goal_col = goal_index % N

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# ==========================================
# Generate Neighboring States
# ==========================================

def get_neighbors(state):

    neighbors = []

    zero_index = state.index(0)

    row = zero_index // N
    col = zero_index % N

    # Up, Down, Left, Right
    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid position
        if 0 <= new_row < N and 0 <= new_col < N:

            new_index = new_row * N + new_col

            new_state = list(state)

            # Move blank tile
            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]

            neighbors.append(tuple(new_state))

    return neighbors


# ==========================================
# Check Whether Puzzle is Solvable
# ==========================================

def is_solvable(state):

    values = [
        x for x in state
        if x != 0
    ]

    inversions = 0

    # Count inversions
    for i in range(len(values)):

        for j in range(i + 1, len(values)):

            if values[i] > values[j]:
                inversions += 1

    # Find blank row from bottom
    zero_index = state.index(0)

    blank_row_from_bottom = N - (zero_index // N)

    # Solvability condition for even-sized puzzle
    if blank_row_from_bottom % 2 == 0:

        return inversions % 2 == 1

    else:

        return inversions % 2 == 0


# ==========================================
# A* Search Algorithm
# ==========================================

def a_star(start):

    # Check solvability
    if not is_solvable(start):
        return None

    # Priority Queue
    pq = []

    # Initial heuristic
    h = heuristic(start)

    # Store (f, g, state)
    heapq.heappush(
        pq,
        (h, 0, start)
    )

    # Cost from start node
    g_cost = {
        start: 0
    }

    # Store parent of each state
    parent = {
        start: None
    }

    while pq:

        f, g, current = heapq.heappop(pq)

        # Goal reached
        if current == GOAL:

            path = []

            while current is not None:

                path.append(current)
                current = parent[current]

            return path[::-1]

        # Explore neighbors
        for neighbor in get_neighbors(current):

            new_g = g + 1

            # If new path is better
            if (
                neighbor not in g_cost
                or new_g < g_cost[neighbor]
            ):

                g_cost[neighbor] = new_g

                h = heuristic(neighbor)

                f = new_g + h

                heapq.heappush(
                    pq,
                    (f, new_g, neighbor)
                )

                parent[neighbor] = current

    return None


# ==========================================
# Display Puzzle State
# ==========================================

def display(state):

    for i in range(0, 16, 4):

        row = state[i:i + 4]

        print(
            " ".join(
                "  " if x == 0 else f"{x:2}"
                for x in row
            )
        )

    print()


# ==========================================
# Main Program
# ==========================================

print("==========================================")
print("       15-PUZZLE USING A* ALGORITHM")
print("==========================================")

print("\nEnter the puzzle row by row.")
print("Use 0 for the blank space.\n")


# ==========================================
# Input Puzzle
# ==========================================

numbers = []

for i in range(16):

    value = int(
        input(f"Enter value {i + 1}: ")
    )

    numbers.append(value)


start = tuple(numbers)


# ==========================================
# Display Initial State
# ==========================================

print("\n========== INITIAL STATE ==========\n")

display(start)


# ==========================================
# Check Solvability
# ==========================================

if not is_solvable(start):

    print("This puzzle is NOT solvable.")

else:

    print("This puzzle is solvable.")
    print("\nSolving using A*...\n")

    # ==========================================
    # Solve Puzzle
    # ==========================================

    solution = a_star(start)

    if solution is None:

        print("No solution found.")

    else:

        print("Solution found!")

        print(
            "Number of moves:",
            len(solution) - 1
        )

        # ==========================================
        # Display Solution Path
        # ==========================================

        print("\n========== SOLUTION PATH ==========\n")

        for step, state in enumerate(solution):

            print("Step", step)

            display(state)