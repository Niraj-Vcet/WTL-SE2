# Q10: Fuzzy membership functions - room temperature (Cold / Comfortable / Hot)
import numpy as np
import matplotlib.pyplot as plt

def tri(x, a, b, c):    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)
def trap(x, a, b, c, d): return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)
def gauss(x, m, s):     return np.exp(-(x - m) ** 2 / (2 * s ** 2))

names = ["Cold", "Comfortable", "Hot"]
x = np.linspace(0, 40, 500)
sets = {"Triangular":  (tri,   [(-10, 0, 20), (10, 22, 34), (24, 40, 56)]),       # (a, b, c)
        "Trapezoidal": (trap,  [(-10, 0, 10, 20), (15, 20, 26, 31), (26, 32, 40, 50)]),    # (a, b, c, d)
        "Gaussian":    (gauss, [(5, 6), (22, 4), (38, 6)])}    # (mean, sigma)
value = 28                             # sample input to test

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (title, (f, params)) in zip(axes, sets.items()):
    for n, p in zip(names, params):
        ax.plot(x, f(x, *p), label=n)
    print(f"{title} at Temperature (C) = {value}:", {n: round(float(f(value, *p)), 2) for n, p in zip(names, params)})
    ax.set(title=title, xlabel="Temperature (C)", ylabel="Membership"); ax.legend(); ax.grid(True)
plt.tight_layout(); plt.show()


# ===================== EXAMPLE OUTPUT =====================
# Triangular at Temperature (C) = 28: {'Cold': 0.0, 'Comfortable': 0.5, 'Hot': 0.25}
# Trapezoidal at Temperature (C) = 28: {'Cold': 0.0, 'Comfortable': 0.6, 'Hot': 0.33}
# Gaussian at Temperature (C) = 28: {'Cold': 0.0, 'Comfortable': 0.32, 'Hot': 0.25}
# (a plot window also opens)
