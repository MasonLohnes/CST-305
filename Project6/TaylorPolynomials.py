# ============================
# Reece Gerhart Mason Lohnes
# ----------------------------
# Imports:
# Numpy    Matplotlib    SciPy
# ----------------------------
# Approach to implementation:
# Part 1: Define Taylor polynomial functions for parts (a) and (b)
#         Create visualization with two subplots
#         Part (a): 4th order Taylor series around x=0
#         Part (b): 2nd order Taylor polynomial around x=3
#         Display equations and key points on graphs
# Part 2: Implement power series solution using recurrence relation
#         Calculate coefficients using recurrence formula
#         Evaluate and plot series solution for n <= 8
# Part 3: Define and solve CPU utilization ODE system
#         Set initial conditions and time range
#         Solve ODE numerically using odeint
#         Compute and visualize dynamics and steady-state
# ============================

# ============================
# Imports
# ============================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # Numerical ODE solver

# ============================
# Part 1: Taylor Polynomial Functions
# ============================
def taylor_part_a(x):
    """
    Calculate the Taylor series expansion around x=0.
    
    For differential equation: y'' - 2xy' + x²y = 0
    Initial conditions: y(0) = 1, y'(0) = -1
    
    Returns:
        y(x) = 1 - x - x³/3 - x⁴/12
    """
    return 1 - x - (x**3)/3 - (x**4)/12

def taylor_part_b(x):
    """
    Calculate the second-order Taylor polynomial around x=3.
    
    For differential equation: y'' - (x-2)y' + 2y = 0
    Initial conditions: y(3) = 6, y'(3) = 1
    
    Returns:
        y(x) = 6 + (x-3) - (11/2)(x-3)²
    """
    return 6 + (x - 3) - (11/2) * (x - 3)**2

# ============================
# Part 2: Power Series Functions
# ============================
def series_coeffs(a0=0.0, a1=16.0, N=8):
    """
    Calculate power series coefficients using recurrence relation.
    
    Recurrence: a_{n+2} = - (n² - n + 1)/(4(n+2)(n+1)) * a_n
    Homogeneous series with specified initial coefficients
    
    Args:
        a0: Initial coefficient (default 0.0)
        a1: First coefficient (default 16.0)
        N: Maximum order of series
        
    Returns:
        Array of coefficients [a0, a1, ..., aN]
    """
    a = np.zeros(N + 1)
    a[0] = a0
    a[1] = a1
    for n in range(N - 1):
        a[n+2] = -((n*n - n + 1) / (4*(n+2)*(n+1))) * a[n]
    return a

def series_solution(a_coeffs, x):
    """
    Evaluate power series at a given x value.
    
    Computes: sum(a_i * x^i) for i = 0 to N
    
    Args:
        a_coeffs: Array of series coefficients
        x: Point at which to evaluate series
        
    Returns:
        Series value at x
    """
    return sum(a_coeffs[n] * x**n for n in range(len(a_coeffs)))

# ============================
# Part 3: CPU Utilization ODE
# ============================
def cpu_util(u, t, lam, mu):
    """
    Define the CPU utilization ODE system.
    
    Given:
        u: Current CPU utilization (fraction)
        t: Time
        lam: Job arrival rate
        mu: Job decay rate
        
    Returns:
        du/dt: Rate of change of CPU utilization
    """
    return lam * (1 - u) - mu * u

# ============================
# Part 1: Visualization
# ============================
print("=" * 50)
print("PART 1: TAYLOR POLYNOMIALS")
print("=" * 50)

# Set up the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Part (a): Taylor Series around x=0 ---
# Create x values for plotting
x_a = np.linspace(0, 4, 500)
y_a = taylor_part_a(x_a)

# Plot the Taylor series curve
ax1.plot(x_a, y_a, 'b-', linewidth=2)
# Mark the evaluation point at x=3.5
ax1.plot(3.5, taylor_part_a(3.5), 'ro', markersize=10)

# Configure grid and labels
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y(x)', fontsize=12)
ax1.set_title(r"Part (a): Taylor Series Expansion for $y'' - 2xy' + x^2y = 0$", fontsize=11)

# Add text at bottom left with equation and point value
ax1.text(0.5, -38, r'$f(x) = 1 - x - \frac{x^3}{3} - \frac{x^4}{12}$', 
         fontsize=11, color='blue', verticalalignment='top')
ax1.text(0.5, -42, f'y(3.5) ≈ {taylor_part_a(3.5):.2f}', 
         fontsize=11, color='red', verticalalignment='top')

# Set axis limits
ax1.set_xlim(0, 4.2)
ax1.set_ylim(-45, 5)

# --- Part (b): Taylor Polynomial around x=3 ---
# Create x values centered around x=3
x_b = np.linspace(2.5, 3.5, 500)
y_b = taylor_part_b(x_b)

# Plot the Taylor polynomial curve
ax2.plot(x_b, y_b, 'b-', linewidth=2, label=r'$f(x) = 6 + (x-3) - \frac{11}{2}(x-3)^2$')
# Mark the expansion point
ax2.axvline(x=3, color='brown', linestyle='--', linewidth=2, label='Expansion Point (x=3)')

# Configure grid and labels
ax2.grid(True, alpha=0.3)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y(x)', fontsize=12)
ax2.set_title(r"Part (b): Second-Order Taylor Polynomial for $y'' - (x-2)y' + 2y = 0$", fontsize=11)
ax2.legend(fontsize=10)

# Set axis limits
ax2.set_xlim(2.5, 3.5)
ax2.set_ylim(4.2, 6.2)

# Display Part 1 plots
plt.tight_layout()
plt.show()

# Print Part 1 results
print("\nPart (a): Taylor Series around x=0")
print(f"y(x) = 1 - x - x³/3 - x⁴/12")
print(f"y(3.5) = {taylor_part_a(3.5):.6f}")
print()
print("Part (b): Taylor Polynomial around x=3")
print(f"y(x) = 6 + (x-3) - 11/2(x-3)²")
print(f"y(3) = {taylor_part_b(3):.6f}")
print(f"y'(3) = 1 (from initial condition)")
print(f"y''(3) = -11 (calculated)")

# ============================
# Part 2: Power Series Solution
# ============================
print("\n" + "=" * 50)
print("PART 2: POWER SERIES SOLUTIONS")
print("=" * 50)

# --- User Parameters ---
a0 = 0.0
a1 = 16.0
N_series = 8    
x_min, x_max = 0.0, 9.0
n_points = 1000

# --- Build series and evaluate ---
coeffs = series_coeffs(a0=a0, a1=a1, N=N_series)
print("\nSeries coefficients a0..aN:")
for i, c in enumerate(coeffs):
    print(f"  a_{i} = {c:.8f}")

# Evaluate series at each point
x_vals = np.linspace(x_min, x_max, n_points)
y_vals = [series_solution(coeffs, xi) for xi in x_vals]

print(f"\nPower Series Solution (n <= {N_series})")

# --- Plot Part 2 ---
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, color='blue', linestyle='-', linewidth=2, 
         label=f"Power Series Solution n<={N_series}")

plt.title(f"Part 2: Power Series Solution with n <= {N_series}", 
          fontsize=14, fontweight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("y(x)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("ALL COMPUTATIONS COMPLETE")
print("=" * 50)

# ============================
# Part 3: CPU Utilization Dynamics
# ============================
print("\n" + "=" * 50)
print("PART 3: CPU UTILIZATION DYNAMICS")
print("=" * 50)

# --- Parameters ---
lam = 2.0      # Job arrival rate
mu = 1.0       # Job decay rate
u0 = 0.2       # Initial condition
t = np.linspace(0, 10, 10000)  # Time grid from 0 to 10

print(f"\nParameters:")
print(f"  λ (arrival rate) = {lam}")
print(f"  μ (decay rate) = {mu}")
print(f"  u(0) (initial utilization) = {u0}")
print(f"  Steady-state utilization = {lam/(lam+mu):.4f}")

# --- Solve ODE ---
sol = odeint(cpu_util, u0, t, args=(lam, mu))
u = sol[:, 0]  # Extract solution

# --- Create Graph ---
plt.figure(figsize=(8, 5))
plt.plot(t, u, label="CPU Utilization", linewidth=2)
plt.axhline(y=lam/(lam+mu), linestyle="--", color='red', 
            label="Steady-State Utilization", linewidth=2)

plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("CPU Utilization (fraction)", fontsize=12)
plt.title("CPU Utilization Dynamics in a Computer System", fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("ALL PARTS COMPLETE")
print("=" * 50)