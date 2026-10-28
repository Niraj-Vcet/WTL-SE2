# Q8: Kohonen Self Organizing Map (SOM) - group points into clusters
import random
import matplotlib.pyplot as plt

k = int(input("Number of clusters: "))      # 2, 3 or 4
epochs = int(input("Epochs: "))

# Step 1: assumed input data - 15 random points around each centre
centres = [[1, 1], [5, 5], [1, 5], [5, 1]]
random.seed(1)                              # same data every run
points = []
for i in range(k):
    for j in range(15):
        x = centres[i][0] + random.uniform(-1, 1)
        y = centres[i][1] + random.uniform(-1, 1)
        points.append([x, y])

# Step 2: one neuron per cluster, start each neuron at a random point
weights = []
for p in random.sample(points, k):
    weights.append([p[0], p[1]])

def distance(p, w):
    return (p[0] - w[0])**2 + (p[1] - w[1])**2

# winner = neuron closest to the point
def winner(p):
    best = 0
    for i in range(k):
        if distance(p, weights[i]) < distance(p, weights[best]):
            best = i
    return best

# Step 3: training - move the winner (and its neighbour) towards each point
for ep in range(epochs):
    lr = 0.5 * (1 - ep/epochs)              # learning rate slowly decreases
    for p in points:
        win = winner(p)
        for i in range(k):
            if i == win:
                rate = lr                   # winner moves the most
            elif abs(i - win) == 1 and ep < epochs/2:
                rate = lr / 2               # neighbour moves half (only early)
            else:
                continue
            weights[i][0] = weights[i][0] + rate * (p[0] - weights[i][0])
            weights[i][1] = weights[i][1] + rate * (p[1] - weights[i][1])

# Step 4: give every point the cluster of its winner neuron
labels = []
for p in points:
    labels.append(winner(p))
for i in range(k):
    print(f"Cluster {i}: {labels.count(i)} points, weight = [{weights[i][0]:.2f} {weights[i][1]:.2f}]")

# Step 5: plot the clusters
colours = ['blue', 'green', 'orange', 'purple']
for i in range(len(points)):
    plt.scatter(points[i][0], points[i][1], color=colours[labels[i]])
for w in weights:
    plt.scatter(w[0], w[1], color='red', marker='X', s=200)
plt.title("Kohonen SOM Clusters (red X = neurons)")
plt.show()


# Q8: Kohonen SOM clustering
# Data: 15 random 2-D points around each centre (1,1) (5,5) (1,5) (5,1); first k centres are used.
# Example Input:
#   Number of clusters: 3
#   Epochs: 50
# Example Output (a scatter plot window also opens):
#   Cluster 0: 15 points, weight = [0.91 0.86]
#   Cluster 1: 15 points, weight = [1.04 5.08]
#   Cluster 2: 15 points, weight = [5.13 4.97]
# (k can be 2, 3 or 4)
