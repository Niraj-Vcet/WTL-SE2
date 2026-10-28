# Q10: Fuzzy membership functions - Room temperature
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
names = ["Cold", "Comfortable", "Hot"]
tri_values = [[-10, 0, 20], [10, 22, 34], [24, 40, 56]]
trap_values = [[-10, 0, 10, 20], [15, 20, 26, 31], [26, 32, 45, 50]]
gauss_values = [[5, 6], [22, 4], [38, 6]]

value = float(input("Enter Temperature (°C) (0-40): "))

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
while x <= 40:
    x_list.append(x)
    x = x + 0.1

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
    plt.title(titles[n]); plt.xlabel("Temperature (°C)"); plt.ylabel("Membership")
    plt.legend(); plt.grid(True)
plt.tight_layout()
plt.show()


# Q10: Fuzzy membership - Room temperature
# Example Input:   Enter Temperature (°C) (0-40): 28
# Example Output:
#   Triangular memberships at 28.0
#     Cold: 0.00
#     Comfortable: 0.50
#     Hot: 0.25
#
#   Trapezoidal memberships at 28.0
#     Cold: 0.00
#     Comfortable: 0.60
#     Hot: 0.33
#
#   Gaussian memberships at 28.0
#     Cold: 0.00
#     Comfortable: 0.32
#     Hot: 0.25
# (also opens a window with 3 plots)
