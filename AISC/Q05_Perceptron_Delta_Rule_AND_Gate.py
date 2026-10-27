# Q5: Single Layer Perceptron (Delta Learning Rule) - two-input AND gate
data = [((0,0),0), ((0,1),0), ((1,0),0), ((1,1),1)]     # ((x1, x2), target)
w, b, lr = [0.1, 0.1], 0.1, 0.1                          # small initial weights, bias, learning rate
print(f"Initial: w1={w[0]}, w2={w[1]}, bias={b}")

for epoch in range(1, 101):
    errors = 0
    for (x1, x2), t in data:
        y = 1 if round(w[0]*x1 + w[1]*x2 + b, 6) >= 0 else 0     # step activation
        e = t - y                                                 # delta = target - output
        w[0] += lr*e*x1; w[1] += lr*e*x2; b += lr*e               # delta rule update
        errors += abs(e)
    print(f"Epoch {epoch}: w1={w[0]:.2f}, w2={w[1]:.2f}, bias={b:.2f}, errors={errors}")
    if errors == 0:
        break

print(f"\nFinal: w1={w[0]:.2f}, w2={w[1]:.2f}, bias={b:.2f}")
print("x1 x2 target output")
for (x1, x2), t in data:
    print(f" {x1}  {x2}    {t}      {1 if round(w[0]*x1 + w[1]*x2 + b, 6) >= 0 else 0}")


# ===================== EXAMPLE OUTPUT =====================
# Initial: w1=0.1, w2=0.1, bias=0.1
# Epoch 1: w1=0.10, w2=0.10, bias=-0.10, errors=4
# Epoch 2: w1=0.20, w2=0.10, bias=-0.10, errors=2
# Epoch 3: w1=0.20, w2=0.10, bias=-0.20, errors=3
# Epoch 4: w1=0.20, w2=0.20, bias=-0.20, errors=2
# Epoch 5: w1=0.20, w2=0.10, bias=-0.30, errors=1
# Epoch 6: w1=0.20, w2=0.10, bias=-0.30, errors=0
#
# Final: w1=0.20, w2=0.10, bias=-0.30
# x1 x2 target output
#  0  0    0      0
#  0  1    0      0
#  1  0    0      0
#  1  1    1      1
