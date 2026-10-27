# Q11: Fuzzy membership functions - traffic density (Low / Medium / High)
import numpy as np
import matplotlib.pyplot as plt

def tri(x, a, b, c):    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)
def trap(x, a, b, c, d): return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)
def gauss(x, m, s):     return np.exp(-(x - m) ** 2 / (2 * s ** 2))

names = ["Low", "Medium", "High"]
x = np.linspace(0, 60, 500)
sets = {"Triangular":  (tri,   [(-30, 0, 30), (10, 30, 50), (30, 60, 90)]),       # (a, b, c)
        "Trapezoidal": (trap,  [(-10, 0, 10, 25), (15, 25, 35, 45), (35, 50, 60, 70)]),    # (a, b, c, d)
        "Gaussian":    (gauss, [(0, 10), (30, 8), (60, 10)])}    # (mean, sigma)
value = 35                             # sample input to test

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (title, (f, params)) in zip(axes, sets.items()):
    for n, p in zip(names, params):
        ax.plot(x, f(x, *p), label=n)
    print(f"{title} at Traffic density (vehicles/min) = {value}:", {n: round(float(f(value, *p)), 2) for n, p in zip(names, params)})
    ax.set(title=title, xlabel="Traffic density (vehicles/min)", ylabel="Membership"); ax.legend(); ax.grid(True)
plt.tight_layout(); plt.show()


# ===================== EXAMPLE OUTPUT =====================
# Triangular at Traffic density (vehicles/min) = 35: {'Low': 0.0, 'Medium': 0.75, 'High': 0.17}
# Trapezoidal at Traffic density (vehicles/min) = 35: {'Low': 0.0, 'Medium': 1.0, 'High': 0.0}
# Gaussian at Traffic density (vehicles/min) = 35: {'Low': 0.0, 'Medium': 0.82, 'High': 0.04}
# (a plot window also opens)
