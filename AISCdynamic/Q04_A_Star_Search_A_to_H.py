# Q4: A* Search - choose the node with the smallest f = g + h
#   g = actual cost from start till now, h = heuristic (guess) to goal

# Step 1: make the graph from edges like "A-B:2"
def make_graph(text):
    graph = {}
    for item in text.split():
        edge, cost = item.upper().split(':')
        a, b = edge.split('-')
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append([b, int(cost)])   # undirected, so add both ways
        graph[b].append([a, int(cost)])
    return graph

# Step 2: read heuristic values like "A=5 B=4"
def read_heuristics(text):
    h = {}
    for item in text.split():
        name, value = item.upper().split('=')
        h[name] = int(value)
    return h

# Step 3: A* search
def astar(graph, h, start, goal):
    open_list = [[h[start], 0, [start]]]   # each item = [f, g, path]
    best_cost = {}
    while len(open_list) > 0:
        open_list.sort()                   # smallest f comes first
        f, g, path = open_list.pop(0)
        node = path[-1]
        if node == goal:
            print("Path:", ' -> '.join(path), "| Cost:", g)
            return
        if node in best_cost and best_cost[node] <= g:
            continue                       # already reached cheaper, skip
        best_cost[node] = g
        for next_node, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[next_node]
            open_list.append([new_f, new_g, path + [next_node]])
    print("No path found")

graph = make_graph(input("Edges with cost: "))
h = read_heuristics(input("Heuristics: "))
start = input("Start: ").upper()
goal = input("Goal: ").upper()
astar(graph, h, start, goal)


# Q4: A* Search (A to H)
# Edges format: A-B:2 (node-node:cost), Heuristics format: A=5 B=4 ...
# Example Input:
#   Edges with cost: A-B:2 A-C:3 B-D:3 B-E:2 C-F:2 C-G:3 D-H:3 E-H:4 F-H:3 G-H:2
#   Heuristics: A=5 B=4 C=3 D=3 E=3 F=2 G=1 H=0
#   Start: A
#   Goal: H
# Example Output:
#   Path: A -> B -> D -> H | Cost: 8
# (Note: A-B-D-H, A-B-E-H, A-C-F-H and A-C-G-H all cost 8, so any one of them is a correct optimal path)
