# Q14: Depth-First Search (DFS) - find path from start node A to goal node G
# Undirected tree taken from the diagram
graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F", "G"], "D": ["B"],
         "E": ["B", "H"], "F": ["C"], "G": ["C"], "H": ["E"]}
start, goal = "A", "G"
visited = []

def dfs(node, path):
    visited.append(node)
    if node == goal:
        return path
    for nxt in graph[node]:           # go deep into the first unvisited neighbour
        if nxt not in visited:
            result = dfs(nxt, path + [nxt])
            if result:
                return result

path = dfs(start, [start])
print("Visited order:", " -> ".join(visited))
print("Path:", " -> ".join(path) if path else "No path found")


# ===================== EXAMPLE OUTPUT =====================
# Visited order: A -> B -> D -> E -> H -> C -> F -> G
# Path: A -> C -> G
