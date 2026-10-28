# Q12: Fuzzy membership functions - Washing machine
import math
import matplotlib.pyplot as plt

# Triangular: rises from a to b, falls from b to c
def triangular(x, p):
    a, b, c = p
    if x <= a or x >= c:
        return 0
    elif x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

# Trapezoidal: rises a to b, flat (=1) b to c, falls c to d
def trapezoidal(x, p):
    a, b, c, d = p
    if x <= a or x >= d:
        return 0
    elif x < b:
        return (x - a) / (b - a)
    elif x <= c:
        return 1
    else:
        return (d - x) / (d - c)

# Gaussian: bell curve with centre m and width s
def gaussian(x, p):
    m, s = p
    return math.exp(-((x - m)**2) / (2 * s**2))

# Assumed values for each level
names = ["Lightly Soiled", "Moderately Soiled", "Heavily Soiled"]
tri_values = [[-50, 0, 50], [0, 50, 100], [50, 100, 150]]
trap_values = [[-10, 0, 20, 40], [20, 40, 60, 80], [60, 80, 100, 110]]
gauss_values = [[0, 20], [50, 15], [100, 20]]

value = float(input("Enter Dirt level (%) (0-100): "))

print("\nTriangular memberships at", value)
for i in range(3):
    print(f"  {names[i]}: {triangular(value, tri_values[i]):.2f}")
print("\nTrapezoidal memberships at", value)
for i in range(3):
    print(f"  {names[i]}: {trapezoidal(value, trap_values[i]):.2f}")
print("\nGaussian memberships at", value)
for i in range(3):
    print(f"  {names[i]}: {gaussian(value, gauss_values[i]):.2f}")

# Plot all three types side by side
x_list = []
x = 0
while x <= 100:
    x_list.append(x)
    x = x + 0.5

titles = ["Triangular", "Trapezoidal", "Gaussian"]
plt.figure(figsize=(15, 4))
for n in range(3):
    plt.subplot(1, 3, n + 1)
    for i in range(3):
        y_list = []
        for x in x_list:
            if n == 0:
                y_list.append(triangular(x, tri_values[i]))
            elif n == 1:
                y_list.append(trapezoidal(x, trap_values[i]))
            else:
                y_list.append(gaussian(x, gauss_values[i]))
        plt.plot(x_list, y_list, label=names[i])
    plt.title(titles[n]); plt.xlabel("Dirt level (%)"); plt.ylabel("Membership")
    plt.legend(); plt.grid(True)
plt.tight_layout()
plt.show()


# Q12: Fuzzy membership - Washing machine
# Example Input:   Enter Dirt level (%) (0-100): 30
# Example Output:
#   Triangular memberships at 30.0
#     Lightly Soiled: 0.40
#     Moderately Soiled: 0.60
#     Heavily Soiled: 0.00
#
#   Trapezoidal memberships at 30.0
#     Lightly Soiled: 0.50
#     Moderately Soiled: 0.50
#     Heavily Soiled: 0.00
#
#   Gaussian memberships at 30.0
#     Lightly Soiled: 0.32
#     Moderately Soiled: 0.41
#     Heavily Soiled: 0.00
# (also opens a window with 3 plots)
