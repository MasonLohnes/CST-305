import numpy as np
import matplotlib.pyplot as plt

# ========== EQUATION 1: y'' + 2y' + y = 2t ==========
# Solve characteristic equation: r² + 2r + 1 = 0
a1, b1, c1 = 1, 2, 1
discriminant1 = b1**2 - 4*a1*c1
r1 = -b1 / (2*a1)  # Repeated root: r = -1

# Find particular solution for y_p'' + 2y_p' + y_p = 2t
# Try y_p = At + B, then y_p' = A, y_p'' = 0
# Substituting: 0 + 2A + At + B = 2t
A1 = 2
B1 = -2 * A1  # B1 = -4

# Apply initial conditions: y(0) = 0, y'(0) = 0
c1_eq1 = -B1  # c1 = 4
c2_eq1 = c1_eq1 - A1  # c2 = 2

# ========== EQUATION 2: y'' + y = t² ==========
# Solve characteristic equation: r² + 1 = 0
a2, b2, c2 = 1, 0, 1
discriminant2 = b2**2 - 4*a2*c2  # -4, complex roots ±i

# Find particular solution for y_p'' + y_p = t²
# Try y_p = At² + Bt + C, then y_p' = 2At + B, y_p'' = 2A
# Substituting: 2A + At² + Bt + C = t²
A2 = 1
B2 = 0
C2 = -2 * A2  # C2 = -2

# Apply initial conditions: y(0) = 0, y'(0) = 0
c1_eq2 = -C2  # c1 = 2
c2_eq2 = 0  # c2 = 0

# ========== NUMERICAL EVALUATION ==========
t = np.linspace(0, 8, 1000)

# Equation 1 components
green_eq1 = (c1_eq1 + c2_eq1*t) * np.exp(-t)
particular_eq1 = A1*t + B1
total_eq1 = green_eq1 + particular_eq1

# Equation 2 components
green_eq2 = c1_eq2 * np.cos(t) + c2_eq2 * np.sin(t)
particular_eq2 = A2*t**2 + B2*t + C2
total_eq2 = green_eq2 + particular_eq2

# ========== PLOTTING ==========
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# --- Plot Equation 1 ---
ax1.plot(t, green_eq1, 'g--', linewidth=2.5, label="Green's Function Component: (4-2t)e^(-t)")
ax1.plot(t, particular_eq1, 'r-.', linewidth=2.5, label="Particular Solution: 2t - 4")
ax1.plot(t, total_eq1, 'b-', linewidth=2.5, label="Total Solution")
ax1.set_title("Equation 1: y'' + 2y' + y = 2x, y(0)=y'(0)=0", fontsize=14, fontweight='bold')
ax1.set_xlabel("t", fontsize=12)
ax1.set_ylabel("y(t)", fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11, loc='best')
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axvline(x=0, color='k', linewidth=0.5)

# --- Plot Equation 2 ---
ax2.plot(t, green_eq2, 'g--', linewidth=2.5, label="Green's Function Component: 2cos(t)")
ax2.plot(t, particular_eq2, 'r-.', linewidth=2.5, label="Particular Solution: t² - 2")
ax2.plot(t, total_eq2, 'b-', linewidth=2.5, label="Total Solution")
ax2.set_title("Equation 2: y'' + y = x², y(0)=y'(0)=0", fontsize=14, fontweight='bold')
ax2.set_xlabel("t", fontsize=12)
ax2.set_ylabel("y(t)", fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=11, loc='best')
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.show()

# Print analytical solutions
print("=" * 60)
print("ANALYTICAL SOLUTIONS")
print("=" * 60)
print("\nEquation 1: y'' + 2y' + y = 2x, y(0)=y'(0)=0")
print("Solution: y(t) = (4 - 2t)e^(-t) + 2t - 4")
print("  • Green's Function Component: (4 - 2t)e^(-t)")
print("  • Particular Solution: 2t - 4")
print("\nEquation 2: y'' + y = x², y(0)=y'(0)=0")
print("Solution: y(t) = 2cos(t) + t² - 2")
print("  • Green's Function Component: 2cos(t)")
print("  • Particular Solution: t² - 2")
print("=" * 60)
