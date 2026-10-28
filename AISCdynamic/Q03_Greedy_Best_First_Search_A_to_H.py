# Q3: Greedy Best First Search - always go to the node with the SMALLEST heuristic value

# Step 1: make the graph from the edges typed by the user
def make_graph(text):
    graph = {}
    for edge in text.split():          # edge looks like "A-B"
        a, b = edge.upper().split('-')
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

# Step 2: read heuristic values like "A=6 B=4"
def read_heuristics(text):
    h = {}
    for item in text.split():
        name, value = item.upper().split('=')
        h[name] = int(value)
    return h

# Step 3: Greedy search
def greedy(graph, h, start, goal):
    open_list = [[h[start], [start]]]  # each item = [heuristic, path]
    visited = []
    while len(open_list) > 0:
        open_list.sort()               # smallest heuristic comes first
        value, path = open_list.pop(0)
        node = path[-1]
        if node == goal:
            print("Path:", ' -> '.join(path))
            return
        if node in visited:
            continue
        visited.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                open_list.append([h[next_node], path + [next_node]])
    print("No path found")

graph = make_graph(input("Edges: "))
h = read_heuristics(input("Heuristics: "))
start = input("Start: ").upper()
goal = input("Goal: ").upper()
greedy(graph, h, start, goal)


# Q3: Greedy Best First Search (A to H)
# Heuristics format: A=6 B=4 ...
# Example Input:
#   Edges: A-B A-C B-D B-E C-F C-G D-H E-H F-H G-H
#   Heuristics: A=6 B=4 C=3 D=2 E=3 F=2 G=1 H=0
#   Start: A
#   Goal: H
# Example Output:
#   Path: A -> C -> G -> H
