# Q3: Greedy Best First Search - find path from A to H (always expand the node with smallest h)
import heapq

h = {"A": 6, "B": 4, "C": 3, "D": 2, "E": 3, "F": 2, "G": 1, "H": 0}
edges = [("A","B"), ("A","C"), ("B","D"), ("B","E"), ("C","F"), ("C","G"),
         ("D","H"), ("E","H"), ("F","H"), ("G","H")]            # undirected
graph = {n: [] for n in h}
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
start, goal = "A", "H"

frontier, visited, order = [(h[start], [start])], set(), []
while frontier:
    _, path = heapq.heappop(frontier)   # node with the lowest heuristic value
    node = path[-1]
    if node in visited:
        continue
    visited.add(node)
    order.append(node)
    if node == goal:
        break
    for nxt in graph[node]:
        if nxt not in visited:
            heapq.heappush(frontier, (h[nxt], path + [nxt]))

print("Expanded order:", " -> ".join(order))
print("Path:", " -> ".join(path))


# ===================== EXAMPLE OUTPUT =====================
# Expanded order: A -> C -> G -> H
# Path: A -> C -> G -> H
