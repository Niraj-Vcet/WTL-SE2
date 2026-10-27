# Q1: Breadth-First Search (BFS) - find path from start node A to goal node G
from collections import deque

# Undirected graph taken from the diagram
graph = {"A": ["B", "D", "E"], "B": ["A", "C", "E"], "C": ["B", "E", "F", "G"],
         "D": ["A", "E"], "E": ["A", "B", "C", "D", "F"], "F": ["C", "E", "G"], "G": ["C", "F"]}
start, goal = "A", "G"

queue, visited, order = deque([[start]]), {start}, []
while queue:
    path = queue.popleft()            # oldest path first (FIFO queue)
    node = path[-1]
    order.append(node)
    if node == goal:
        break
    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(path + [nxt])

print("Visited order:", " -> ".join(order))
print("Path:", " -> ".join(path) if node == goal else "No path found")


# ===================== EXAMPLE OUTPUT =====================
# Visited order: A -> B -> D -> E -> C -> F -> G
# Path: A -> B -> C -> G
