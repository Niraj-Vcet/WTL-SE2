# Q4: A* Search - find least-cost path from A to H using f(n) = g(n) + h(n)
import heapq

h = {"A": 5, "B": 4, "C": 3, "D": 3, "E": 3, "F": 2, "G": 1, "H": 0}
edges = [("A","B",2), ("A","C",3), ("B","D",3), ("B","E",2), ("C","F",2),
         ("C","G",3), ("D","H",3), ("E","H",4), ("F","H",3), ("G","H",2)]   # undirected
graph = {n: [] for n in h}
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))
start, goal = "A", "H"

frontier, best = [(h[start], 0, [start])], {}      # (f, g, path)
while frontier:
    f, g, path = heapq.heappop(frontier)           # smallest f first
    node = path[-1]
    if node == goal:
        break
    if node in best and best[node] <= g:           # already reached with a cheaper cost
        continue
    best[node] = g
    for nxt, w in graph[node]:
        heapq.heappush(frontier, (g + w + h[nxt], g + w, path + [nxt]))

print("Path:", " -> ".join(path))
print("Total cost:", g)


# ===================== EXAMPLE OUTPUT =====================
# Path: A -> B -> D -> H
# Total cost: 8
