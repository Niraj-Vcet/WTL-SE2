# Q8: Kohonen Self-Organizing Map - cluster 12 two-dimensional patterns into 3 groups and plot them
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,1], [1.2,0.8], [0.8,1.1], [1.1,1.3],        # group near (1,1)
              [5,5], [5.2,4.8], [4.8,5.1], [5.1,5.3],        # group near (5,5)
              [1,5], [1.2,4.8], [0.8,5.1], [1.1,5.3]])       # group near (1,5)
k, epochs = 3, 100                                           # 3 output neurons, 100 epochs
np.random.seed(0)
W = X[np.random.choice(len(X), k, replace=False)].copy()    # initial neuron weights

for ep in range(epochs):
    lr = 0.5 * (1 - ep / epochs)                             # learning rate decreases
    radius = 1.0 * (1 - ep / epochs) + 0.1                   # neighbourhood shrinks
    for x in np.random.permutation(X):
        win = np.argmin(((W - x) ** 2).sum(axis=1))          # winner = closest neuron
        for j in range(k):
            nb = np.exp(-(j - win) ** 2 / (2 * radius ** 2)) # neighbourhood function
            W[j] += lr * nb * (x - W[j])                     # move neuron towards the pattern

labels = np.argmin(((X[:, None] - W) ** 2).sum(axis=2), axis=1)
for j in range(k):
    print(f"Cluster {j}: patterns {np.where(labels == j)[0].tolist()}, neuron weight = {W[j].round(2)}")

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=60, label="Patterns")
plt.scatter(W[:, 0], W[:, 1], c="red", marker="X", s=200, label="Neurons")
plt.title("Kohonen SOM Clusters"); plt.xlabel("x1"); plt.ylabel("x2"); plt.legend(); plt.show()


# ===================== EXAMPLE OUTPUT =====================
# Cluster 0: patterns [0, 1, 2, 3], neuron weight = [1.03 1.05]
# Cluster 1: patterns [8, 9, 10, 11], neuron weight = [1.03 5.05]
# Cluster 2: patterns [4, 5, 6, 7], neuron weight = [5.02 5.05]
# (a plot window also opens)
