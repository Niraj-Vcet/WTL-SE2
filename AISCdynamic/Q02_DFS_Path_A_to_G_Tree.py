# Q2: Depth First Search (DFS) - find path from Start node to Goal node

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

# Step 2: DFS using a stack (last in, first out)
def dfs(graph, start, goal):
    stack = [[start]]                  # stack stores paths
    order = []
    while len(stack) > 0:
        path = stack.pop()             # take the LAST path
        node = path[-1]
        if node in order:
            continue                   # already visited, skip it
        order.append(node)
        if node == goal:
            print("Visited order:", ' '.join(order))
            print("Path:", ' -> '.join(path))
            return
        # push in reverse so that A, B, C... are explored left to right
        for next_node in sorted(graph[node], reverse=True):
            if next_node not in order:
                stack.append(path + [next_node])
    print("No path found")

graph = make_graph(input("Edges: "))
start = input("Start: ").upper()
goal = input("Goal: ").upper()
dfs(graph, start, goal)


# Q2: DFS (Start A, Goal G)
# Input format: edges as A-B A-C ... (undirected, no spaces inside an edge)
# Example Input:
#   Edges: A-B A-C B-D B-E E-H C-F C-G
#   Start: A
#   Goal: G
# Example Output:
#   Visited order: A B D E H C F G
#   Path: A -> C -> G
