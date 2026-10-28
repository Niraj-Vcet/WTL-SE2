# Q7: AND gate perceptron - compare learning rates 0.1, 0.3 and 0.5

# Truth table of AND gate: [x1, x2, target]
data = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Step function: output is 1 if net >= 0, else 0
def step(net):
    if net >= 0:
        return 1
    return 0

# Train with one learning rate and return epochs and final weights
def train(lr, w1, w2, b):
    epoch = 0
    while True:
        epoch = epoch + 1
        errors = 0
        for x1, x2, target in data:
            error = target - step(w1*x1 + w2*x2 + b)
            # Delta rule: new weight = old weight + lr * error * input
            w1 = round(w1 + lr*error*x1, 2)
            w2 = round(w2 + lr*error*x2, 2)
            b = round(b + lr*error, 2)
            if error != 0:
                errors = errors + 1
        if errors == 0 or epoch == 100:   # stop when no mistakes
            return epoch, w1, w2, b

w1, w2, b = input("Initial w1 w2 bias: ").split()
w1, w2, b = float(w1), float(w2), float(b)

# same starting weights for every learning rate
for lr in [0.1, 0.3, 0.5]:
    epochs, f1, f2, fb = train(lr, w1, w2, b)
    print(f"lr={lr}: epochs={epochs}, w1={f1:.2f}, w2={f2:.2f}, bias={fb:.2f}")


# Q7: AND gate, learning rates 0.1 / 0.3 / 0.5 (same initial weights for all)
# Example Input:
#   Initial w1 w2 bias: 0.3 0.2 -0.1
# Example Output:
#   lr=0.1: epochs=2, w1=0.20, w2=0.10, bias=-0.30
#   lr=0.3: epochs=5, w1=0.60, w2=0.20, bias=-0.70
#   lr=0.5: epochs=8, w1=1.30, w2=0.70, bias=-1.60
# Analysis: the number of epochs depends on BOTH the learning rate and the initial weights.
# A large lr takes big weight jumps, so it can overshoot and needs more epochs to settle.
# A small lr takes small steady steps - here the starting weights were already close,
# so lr=0.1 converged fastest. If the weights start far away, a small lr can be slower.
