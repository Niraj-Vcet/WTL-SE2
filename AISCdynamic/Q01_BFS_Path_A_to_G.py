# Q1: Breadth First Search (BFS) - find path from Start node to Goal node

# Step 1: make the graph from the edges typed by the user
def make_graph(text):
    graph = {}
    for edge in text.split():          # edge looks like "A-B"
        a, b = edge.upper().split('-')
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)             # undirected, so add both ways
        graph[b].append(a)
    return graph

# Step 2: BFS using a queue (first in, first out)
def bfs(graph, start, goal):
    queue = [[start]]                  # queue stores paths
    visited = [start]
    order = []
    while len(queue) > 0:
        path = queue.pop(0)            # take the FIRST path
        node = path[-1]                # last node of that path
        order.append(node)
        if node == goal:
            print("Visited order:", ' '.join(order))
            print("Path:", ' -> '.join(path))
            return
        for next_node in sorted(graph[node]):
            if next_node not in visited:
                visited.append(next_node)
                queue.append(path + [next_node])
    print("No path found")

graph = make_graph(input("Edges: "))
start = input("Start: ").upper()
goal = input("Goal: ").upper()
bfs(graph, start, goal)


# Q1: BFS (Start A, Goal G)
# Input format: edges as A-B A-C ... (undirected, no spaces inside an edge)
# Example Input:
#   Edges: A-B A-D A-E B-C B-E C-E C-F C-G D-E E-F F-G
#   Start: A
#   Goal: G
# Example Output:
#   Visited order: A B D E C F G
#   Path: A -> B -> C -> G
