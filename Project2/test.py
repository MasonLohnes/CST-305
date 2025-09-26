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

# For odeint, we need the equation in the form dy/dx = f(y, x)
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

# Create the comparison plot
plt.figure(figsize=(12, 8))

# Plot both solutions
plt.plot(x_rk, y_rk, 'ro-', label='Runge-Kutta (RK4)', markersize=6, linewidth=2)
plt.plot(x_ode, y_ode, 'b-', label='ODEint (scipy)', linewidth=2, alpha=0.7)

# Formatting
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Comparison: Runge-Kutta vs ODEint\ndy/dx = y/(e^x - 1)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Add some styling
plt.tight_layout()

# Show error between methods at RK points
x_rk_array = np.array(x_rk)
y_rk_array = np.array(y_rk)
y_ode_interp = np.interp(x_rk_array, x_ode, y_ode.flatten())
errors = np.abs(y_rk_array - y_ode_interp)

print(f"\nMaximum absolute error: {max(errors):.6f}")
print(f"Average absolute error: {np.mean(errors):.6f}")

plt.show()

# Optional: Create a second plot showing the error
plt.figure(figsize=(10, 6))
plt.plot(x_rk, errors, 'go-', markersize=4)
plt.xlabel('x', fontsize=12)
plt.ylabel('Absolute Error |RK4 - ODEint|', fontsize=12)
plt.title('Absolute Error between Runge-Kutta and ODEint', fontsize=14)
plt.grid(True, alpha=0.3)
plt.yscale('log')  # Log scale to better see small errors
plt.tight_layout()
plt.show()
