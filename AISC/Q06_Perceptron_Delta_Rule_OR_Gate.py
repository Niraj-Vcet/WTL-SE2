# Q6: Single Layer Perceptron (Delta Learning Rule) - two-input OR gate, try several learning rates
data = [((0,0),0), ((0,1),1), ((1,0),1), ((1,1),1)]     # ((x1, x2), target)
step = lambda w, b, x1, x2: 1 if round(w[0]*x1 + w[1]*x2 + b, 6) >= 0 else 0

for lr in (0.1, 0.3, 0.5):                               # experiment with learning rates
    w, b = [0.1, 0.1], 0.1                               # same small initial weights each time
    for epoch in range(1, 101):
        errors = 0
        for (x1, x2), t in data:
            e = t - step(w, b, x1, x2)                   # delta = target - output
            w[0] += lr*e*x1; w[1] += lr*e*x2; b += lr*e
            errors += abs(e)
        if errors == 0:
            break
    predicted = [step(w, b, x1, x2) for (x1, x2), _ in data]
    target = [t for _, t in data]
    print(f"lr={lr}: converged at epoch {epoch}, w1={w[0]:.2f}, w2={w[1]:.2f}, bias={b:.2f}")
    print(f"        target={target} predicted={predicted} match={predicted == target}")


# ===================== EXAMPLE OUTPUT =====================
# lr=0.1: converged at epoch 3, w1=0.10, w2=0.10, bias=-0.10
#         target=[0, 1, 1, 1] predicted=[0, 1, 1, 1] match=True
# lr=0.3: converged at epoch 4, w1=0.40, w2=0.40, bias=-0.20
#         target=[0, 1, 1, 1] predicted=[0, 1, 1, 1] match=True
# lr=0.5: converged at epoch 4, w1=0.60, w2=0.60, bias=-0.40
#         target=[0, 1, 1, 1] predicted=[0, 1, 1, 1] match=True
