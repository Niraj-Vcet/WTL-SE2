# Q12: Fuzzy membership functions - washing machine (Lightly / Moderately / Heavily Soiled)
import numpy as np
import matplotlib.pyplot as plt

def tri(x, a, b, c):    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)
def trap(x, a, b, c, d): return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)
def gauss(x, m, s):     return np.exp(-(x - m) ** 2 / (2 * s ** 2))

names = ["Lightly Soiled", "Moderately Soiled", "Heavily Soiled"]
x = np.linspace(0, 100, 500)
sets = {"Triangular":  (tri,   [(-50, 0, 50), (0, 50, 100), (50, 100, 150)]),       # (a, b, c)
        "Trapezoidal": (trap,  [(-10, 0, 20, 40), (20, 40, 60, 80), (60, 80, 100, 110)]),    # (a, b, c, d)
        "Gaussian":    (gauss, [(0, 20), (50, 15), (100, 20)])}    # (mean, sigma)
value = 30                             # sample input to test

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (title, (f, params)) in zip(axes, sets.items()):
    for n, p in zip(names, params):
        ax.plot(x, f(x, *p), label=n)
    print(f"{title} at Dirt level (%) = {value}:", {n: round(float(f(value, *p)), 2) for n, p in zip(names, params)})
    ax.set(title=title, xlabel="Dirt level (%)", ylabel="Membership"); ax.legend(); ax.grid(True)
plt.tight_layout(); plt.show()


# ===================== EXAMPLE OUTPUT =====================
# Triangular at Dirt level (%) = 30: {'Lightly Soiled': 0.4, 'Moderately Soiled': 0.6, 'Heavily Soiled': 0.0}
# Trapezoidal at Dirt level (%) = 30: {'Lightly Soiled': 0.5, 'Moderately Soiled': 0.5, 'Heavily Soiled': 0.0}
# Gaussian at Dirt level (%) = 30: {'Lightly Soiled': 0.32, 'Moderately Soiled': 0.41, 'Heavily Soiled': 0.0}
# (a plot window also opens)
