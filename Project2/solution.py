# ============================
# Reece Gerhart & Mason Lohnes
# ----------------------------
# Imports:
# Numpy Matplotlib SciPy Math
# ----------------------------
# Approach to implementation:
# Create an algorithm for RK
# Define the equation
# Run the RK solver
# Run the ODEint solver
# Create graph plots
# Calculate the error
# ============================

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def RK(x, y, h):
    k1 = equation(x, y)
    k2 = equation(x + h/2, y + (h/2)*k1)
    k3 = equation(x + h/2, y + (h/2)*k2)
    k4 = equation(x + h, y + h*k3)
    T4 = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return y + h * T4

def equation(x, y):
    return y/((math.exp(x))-1)

def ode_equation(y, x):
    return y/((math.exp(x))-1)

print("Runge-Kutta vs ODEint Comparison for dy/dx = y/(e^x - 1)")
x0 = float(input("Input x0: "))
y0 = float(input("Input y0: "))
h = float(input("Input h: "))
runs = int(input("Input number of runs: "))

# Runge-Kutta solution
x_rk = [x0]
y_rk = [y0]
x_current = x0
y_current = y0

for step in range(runs):
    y_current = RK(x_current, y_current, h)
    x_current = x_current + h
    x_rk.append(x_current)
    y_rk.append(y_current)
    print("Step " + str(step + 1) + ": (" + str(round(x_current,4)) + "," + str(round(y_current,4)) + ")")

# ODEint solution
x_ode = np.linspace(x0, x0 + runs*h, runs*10 + 1)  # More points for smoother curve
y_ode = odeint(ode_equation, y0, x_ode)

# Plot Runge-Kutta solution alone
plt.figure(figsize=(10, 6))
plt.plot(x_rk, y_rk, 'ro-', label='Runge-Kutta (RK4)', markersize=6, linewidth=2)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Runge-Kutta (RK4) Solution', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot ODEint solution alone
plt.figure(figsize=(10, 6))
plt.plot(x_ode, y_ode, 'b-', label='ODEint (scipy)', linewidth=2)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('ODEint Solution', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Plot comparison
plt.figure(figsize=(12, 8))
plt.plot(x_rk, y_rk, 'ro-', label='Runge-Kutta (RK4)', markersize=6, linewidth=2)
plt.plot(x_ode, y_ode, 'b-', label='ODEint (scipy)', linewidth=2, alpha=0.7)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Comparison: Runge-Kutta vs ODEint\ndy/dx = y/(e^x - 1)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Compute error
x_rk_array = np.array(x_rk)
y_rk_array = np.array(y_rk)
y_ode_interp = np.interp(x_rk_array, x_ode, y_ode.flatten())
errors = np.abs(y_rk_array - y_ode_interp)
print(f"\nMaximum absolute error: {max(errors):.6f}")
print(f"Average absolute error: {np.mean(errors):.6f}")
