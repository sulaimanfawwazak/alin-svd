import numpy as np
import matplotlib.pyplot as plt
import math

# Initialize all the matrices
# A
A = np.array([[4, 0], [3, -5]])

# U
U = np.array([[-2/math.sqrt(20), 4/math.sqrt(20)], [-4/math.sqrt(20), -2/math.sqrt(20)]])

# Sigma
S = np.array([[math.sqrt(40), 0], [0, math.sqrt(10)]])

# V and V transpose
V = np.array([[-1/math.sqrt(2), 1/math.sqrt(2)], [1/math.sqrt(2), 1/math.sqrt(2)]])
V_T = np.transpose(V)

# Initialize the vector
x = np.array([1, 1])

# Make the resulting vectors
x_1 = V_T @ x
x_2 = S @ x_1
x_3 = U @ x_2

# Plot the resulting vectors
# Initial vector x
plt.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', scale=1)
plt.axhline(0)
plt.axvline(0)
plt.title('Initial Vector x')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid(True)
plt.show()

# V_T * x
plt.quiver(0, 0, x_1[0], x_1[1], angles='xy', scale_units='xy', scale=1)
plt.axhline(0)
plt.axvline(0)
plt.title('V_Transpose * x')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid(True)
plt.show()

# S * V_T * x
plt.quiver(0, 0, x_2[0], x_2[1], angles='xy', scale_units='xy', scale=1)
plt.axhline(0)
plt.axvline(0)
plt.title('Sigma * V_Transpose * x')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid(True)
plt.show()

# U * S * V_T * x
plt.quiver(0, 0, x_3[0], x_3[1], angles='xy', scale_units='xy', scale=1)
plt.axhline(0)
plt.axvline(0)
plt.title('U * Sigma * V_Transpose * x')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid(True)
plt.show()

# All the resulting vectors
plt.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', color = 'black', scale=1)
ax = plt.gca()
ax.annotate(f'x', (x[0], x[1]), fontsize=10)

plt.quiver(0, 0, x_1[0], x_1[1], angles='xy', scale_units='xy', color = 'blue', scale=1)
ax.annotate(f'V_T*x', (x_1[0], x_1[1]), fontsize=10)

plt.quiver(0, 0, x_2[0], x_2[1], angles='xy', scale_units='xy', color = 'r', scale=1)
ax.annotate(f'S*V_T*x', (x_2[0], x_2[1]), fontsize=10)

plt.quiver(0, 0, x_3[0], x_3[1], angles='xy', scale_units='xy', color = 'g', scale=1)
ax.annotate(f'U*S*V_T', (x_3[0], x_3[1]), fontsize=10)

plt.axhline(0)
plt.axvline(0)
plt.title('All vectors')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid(True)
plt.show()