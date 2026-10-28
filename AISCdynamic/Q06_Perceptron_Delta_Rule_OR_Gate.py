# Q6: Single Layer Perceptron using Delta Rule - OR gate

# Truth table of OR gate: [x1, x2, target]
data = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

# Step function: output is 1 if net >= 0, else 0
def step(net):
    if net >= 0:
        return 1
    return 0

lr = float(input("Learning rate: "))
w1, w2, b = input("Initial w1 w2 bias: ").split()
w1, w2, b = float(w1), float(w2), float(b)

epoch = 0
while True:
    epoch = epoch + 1
    errors = 0
    for x1, x2, target in data:
        net = w1*x1 + w2*x2 + b
        output = step(net)
        error = target - output
        # Delta rule: new weight = old weight + lr * error * input
        w1 = round(w1 + lr*error*x1, 2)
        w2 = round(w2 + lr*error*x2, 2)
        b = round(b + lr*error, 2)
        if error != 0:
            errors = errors + 1
    print(f"Epoch {epoch}: w1={w1:.2f} w2={w2:.2f} b={b:.2f} errors={errors}")
    if errors == 0 or epoch == 100:    # stop when no mistakes
        break

print(f"Converged at epoch {epoch} | Final w1={w1:.2f}, w2={w2:.2f}, bias={b:.2f}")
print("x1 x2 target predicted")
for x1, x2, target in data:
    print(f" {x1}  {x2}    {target}       {step(w1*x1 + w2*x2 + b)}")


# Q6: SLP Delta Rule - OR gate (run again with a different learning rate to experiment)
# Example Input:
#   Learning rate: 0.1
#   Initial w1 w2 bias: 0.1 0.1 0.1
# Example Output:
#   Epoch 1: w1=0.10 w2=0.10 b=0.00 errors=1
#   Epoch 2: w1=0.10 w2=0.10 b=-0.10 errors=1
#   Epoch 3: w1=0.10 w2=0.10 b=-0.10 errors=0
#   Converged at epoch 3 | Final w1=0.10, w2=0.10, bias=-0.10
#   x1 x2 target predicted
#    0  0    0       0
#    0  1    1       1
#    1  0    1       1
#    1  1    1       1
