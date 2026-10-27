from queue import PriorityQueue


# ==========================================
# Best First Search
# ==========================================

def best_first_search(graph, heuristic, start, goal):

    pq = PriorityQueue()

    # Insert start node based on heuristic value
    pq.put((heuristic[start], start))

    visited = set()

    # Store parent of each node
    parent = {start: None}

    while not pq.empty():

        h, current = pq.get()

        # Skip if already visited
        if current in visited:
            continue

        print("Visited:", current)

        visited.add(current)

        # Goal reached
        if current == goal:
            break

        # Explore neighbors
        for neighbor in graph[current]:

            if neighbor not in visited:

                # Add neighbor based on heuristic
                pq.put((heuristic[neighbor], neighbor))

                # Store parent
                if neighbor not in parent:
                    parent[neighbor] = current

    # ==========================================
    # Check if path exists
    # ==========================================

    if goal not in parent:

        print("\nNo path found!")
        return

    # ==========================================
    # Construct path
    # ==========================================

    path = []

    node = goal

    while node is not None:

        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nOptimal Path:", " -> ".join(path))


# ==========================================
# Input Graph
# ==========================================

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))


# ==========================================
# Enter Node Details
# ==========================================

print("\nEnter node details:")

for _ in range(n):

    node = input("\nNode name: ")

    h = int(
        input(f"Heuristic value of {node}: ")
    )

    heuristic[node] = h

    neighbors = input(
        f"Enter neighbors of {node} "
        "(space separated, press Enter if none): "
    ).split()

    graph[node] = neighbors


# ==========================================
# Start and Goal Nodes
# ==========================================

start = input("\nEnter Start Node: ")

goal = input("Enter Goal Node: ")


# ==========================================
# Perform Best First Search
# ==========================================

print("\nBest First Search Traversal:")

best_first_search(
    graph,
    heuristic,
    start,
    goal
)