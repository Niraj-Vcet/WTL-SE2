# Q7: Perceptron (Delta Rule) AND gate - compare learning rates 0.1, 0.3, 0.5
data = [((0,0),0), ((0,1),0), ((1,0),0), ((1,1),1)]     # ((x1, x2), target)

for lr in (0.1, 0.3, 0.5):
    w, b = [0.3, 0.2], -0.1                              # identical initial weights and bias for every rate
    for epoch in range(1, 101):
        errors = 0
        for (x1, x2), t in data:
            y = 1 if round(w[0]*x1 + w[1]*x2 + b, 6) >= 0 else 0
            e = t - y
            w[0] += lr*e*x1; w[1] += lr*e*x2; b += lr*e
            errors += abs(e)
        if errors == 0:                                  # a full epoch with no errors = converged
            break
    print(f"lr={lr}: converged at epoch {epoch}, w1={w[0]:.2f}, w2={w[1]:.2f}, bias={b:.2f}")

# Analysis: with the same start, a larger learning rate changes the weights in bigger steps, so here it needed
# MORE epochs (2 -> 5 -> 8). Small lr = small gentle steps, large lr = big jumps.
# With all-zero initial weights every rate needs the same number of epochs.


# ===================== EXAMPLE OUTPUT =====================
# lr=0.1: converged at epoch 2, w1=0.20, w2=0.10, bias=-0.30
# lr=0.3: converged at epoch 5, w1=0.60, w2=0.20, bias=-0.70
# lr=0.5: converged at epoch 8, w1=1.30, w2=0.70, bias=-1.60
